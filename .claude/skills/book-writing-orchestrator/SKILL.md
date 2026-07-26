---
name: book-writing-orchestrator
description: Orchestrate a full book-writing workflow from topic to finished EPUB with cover image. Use when the user asks to "write a book", "draft a book", "author a book", "책 쓰기", "책 저술해줘", "책 만들어줘", "전자책 만들어줘", "EPUB 생성", provides a topic/audience/outline and asks to turn it into a book, or says "~에 대한 책을 써줘". Also triggers on follow-ups like "다시 저술", "계획 수정", "챕터 다시 써줘", "표지 바꿔", "책 업데이트", "특정 챕터 보완", "이전 책 개선", "리서치만 다시". Coordinates research, planning, review, chapter writing in the active genre voice (auto-detected; defaults to tech-book = Toby's style), style enforcement, editing, cover design, and EPUB assembly. Author defaults to Toby-AI (overridable via user prompt — include "저자: {이름}").
---

# Book Writing Orchestrator

주제·주요 내용·대상 독자를 받아 Toby 스타일의 완성된 EPUB을 산출하는 전 과정을 조율한다. 각 Phase에서 전문 에이전트를 호출하고, 중간 산출물을 `{slug}/` 하위에 축적한 뒤 최종 EPUB을 프로젝트 루트에 만든다.

## 실행 모드

| Phase | 모드 | 왜 이렇게 |
|-------|------|----------|
| 1. 리서치 | 서브 에이전트(팬아웃) | 소스별 독립 수집 → 병렬화가 이득 |
| 2. 저술 계획 | 단일 서브 | 통합적 사고가 필요, 분할 이점 없음 |
| 3. 계획 리뷰 | 에이전트 팀(생성-검증 왕복) | 저자와 리뷰어의 토론이 품질을 높임 |
| 4. 챕터 저술 | **에이전트 팀** | 챕터 저술가 ↔ 스타일 가디언 ↔ 편집자 실시간 조율 |
| 4.5. 통권 수락 검수 | 단일 서브(신선 컨텍스트) | editor와 분리된 새 눈이 통권을 게이트 — 자기 승인 방지 |
| 5. 표지 + EPUB | 서브(부분 병렬) | cover-designer를 background로 띄우고 epub-builder의 cover-독립 준비를 병행, `cover.png` 소비 지점에서 join |

**팀 도구 폴백 (`TeamCreate` 부재 시):** `TeamCreate`/팀 내 `SendMessage`를 쓸 수 없는 환경에서는 Phase 3·4를 **파일 기반 폴백**으로 진행한다 — 검수자(plan-reviewer·style-guardian·fact-checker·continuity-keeper)는 자기 로그 파일에 `## {NN}장` 섹션으로 **판정 + before/after 재작성안**을 쓰고, 오케스트레이터가 저술가에게 "해당 섹션을 읽고 반영하라"고 라우팅한다. **저술가에게 검수자를 직접 호출하라고 지시하지 마라** — 조용히 실패한다. 이때 검수자 지시는 반드시 **실행 가능한 재작성안**이어야 한다 — 저술가는 로그 파일만 보므로 "더 자연스럽게" 류 지시는 반영할 수 없다. 부수 효과로 검수 로그가 곧 감사 추적이 된다(팀 메시지는 휘발된다).

## Phase 0: 컨텍스트 확인

워크플로우를 시작하기 전에 기존 산출물 존재 여부를 확인한다.

1. 사용자 입력에서 **주제, 주요 내용, 대상 독자**를 추출한다. 셋 중 하나라도 불명확하면 사용자에게 짧게 질문한다 (AskUserQuestion 사용). 추가로 `저자: {이름}` 형태의 저자 지정이 있는지 확인한다 — 없으면 기본값 `Toby-AI`를 사용하고, 있으면 해당 값을 매니페스트·표지 메타까지 전파한다. `라이선스: {값}` 형태가 있는지도 확인한다 — 없으면 하네스 기본값 `CC BY-NC-SA 4.0`을 매니페스트에 그대로 두고(또는 `license` 필드를 비워두면 빌드 스크립트가 채움), 있으면 해당 값을 매니페스트의 `license` 필드로 전달한다.
2. **장르 감지 + 확인.** `profiles/_registry.md`의 자동 감지 규칙으로 주제·주요 내용·대상 독자에서 장르를 추정한다 (`tech-book` / `narrative` / `practical` / `essay`, 기본 `tech-book`). 사용자가 `장르: {값}`을 명시했으면 그대로 채택. 아니면 `AskUserQuestion`으로 추정값을 첫 옵션·추천으로 제시해 **확인받는다** (단, 신호가 강하고 명백하면 추정값을 알리고 진행해도 된다). 확정된 `genre`는 이후 모든 Phase로 전파되고, Phase 4의 editor가 `book_manifest.json`의 `genre` 필드에 기록한다. 활성 프로필 경로는 `profiles/{genre}/`.
3. **위임 다이얼 (운영자 학습 루프).** 사용자 입력에서 `모드: 학습` 명시 또는 "이 주제를 공부하려고/잘 몰라서" 류의 명확한 학습 신호를 확인한다. 있으면 `delegation_mode: learning`, 없으면 기본 `production` — **신호가 없으면 묻지 않는다.** 어차피 AskUserQuestion을 쓸 일이 있으면 그 질문에 다이얼 확인을 편승시켜도 된다 (추가 왕복 금지). 확정 값은 Phase 4의 editor에게 전달해 `book_manifest.json`의 `delegation_mode`에 기록하고 (재실행 결정성 — `genre`와 같은 취급), Phase 3·4·완료 보고의 학습 터치포인트가 이 값을 따른다. 정전 스펙은 `docs/learning-loop.md`.
4. 책 제목 후보(슬러그 포함)를 만든다. 예: `AI 시대의 개발자 철학` → 슬러그 `ai-developer-philosophy`.
5. `{slug}/`의 존재 여부를 확인한다.
   - **미존재** → 초기 실행, Phase 1부터 순차 실행
   - **존재 + 사용자가 부분 수정 요청** (예: "챕터 3만 다시", "계획만 수정") → 부분 재실행, 해당 Phase만 재호출. 이때 장르는 기존 `book_manifest.json`의 `genre`를 재사용한다 (사용자가 장르 변경을 명시하지 않는 한)
   - **존재 + 새 입력 제공** → 기존 `{slug}/`를 `{slug}_prev-{timestamp}/`로 이동 후 새 실행

## Phase 1: 리서치 (팬아웃)

**실행 모드:** 서브 에이전트 병렬 호출

`research-lead` 에이전트를 호출하고, 내부에서 `web-researcher`, `paper-researcher`, `community-researcher`를 `run_in_background: true`로 병렬 스폰한 뒤 결과를 종합하도록 지시한다.

**입력:** `genre` (Phase 0에서 확정 — 리서처의 장르별 소스 세트 선택 기준), 주제, 주요 내용, 대상 독자, 슬러그
**출력:**
- `{slug}/01_reference.md` — 리서치 종합 문서 (섹션: 개념·정의, 주요 관점, 사례, 논쟁점, 참고문헌)
- `{slug}/research/web.md`·`papers.md`·`community.md` — 소스별 원본 리서치. `01_reference.md` 합성 후에도 **보존**한다 (Phase 4 `fact-checker`의 1차 대조 근거)

**신선도 메타:** tech-book·최신 기술 주제에서는 리서처가 각 출처의 발행일과 검색 시점("검색: {날짜} 기준")을 기록한다. 버전·릴리스 정보는 "{버전}/{연도} 기준"으로 못 박는다. 이 메타가 Phase 4 `fact-checker`의 대조 기준이 된다.

**모델 라우팅:** 판단·합성이 필요한 Phase(리서치·계획·리뷰·챕터 저술·수락 검수)는 `model: "opus"`를 명시하고, 기계적 Phase(`epub-builder`·`cover-designer`)는 각 에이전트 frontmatter의 `sonnet`을 따른다.

## Phase 2: 저술 계획

**실행 모드:** 단일 서브 에이전트

`book-planner` 에이전트를 호출한다.

**입력:** `genre`, 주제, 주요 내용, 대상 독자, `{slug}/01_reference.md`, 활성 `profiles/{genre}/scaffolds.md`
**출력:** `{slug}/02_plan.md` — 책 구조 설계 문서
- 책 제목 후보 3개
- 책 특성 (장르, 분량, 난이도, 독자 여정)
- 챕터 목록 (번호, 제목, 핵심 질문, 주요 내용, 예상 분량)
- 챕터 간 흐름(내러티브 아크)

## Phase 3: 계획 리뷰 (팀)

**실행 모드:** 에이전트 팀 (생성-검증 왕복)

`TeamCreate`로 `book-planner`와 `plan-reviewer`를 팀으로 구성한다. `plan-reviewer`가 계획을 비판적으로 읽고 `SendMessage`로 `book-planner`에게 피드백을 보낸다. `book-planner`는 피드백을 반영해 계획을 갱신한다.

**수렴 기준:** 왕복은 모든 Critical 항목이 planner가 반영했거나 `03_review_log.md`에 사유와 함께 명시적으로 유보(deferred)될 때, 또는 최대 2회 후 종료한다. 종료 시점에 미해소 Critical이 남아 있으면 위험으로 `03_review_log.md`에 로그한다. 그 뒤 팀을 해체한다.

**산출물:** `{slug}/02_plan.md` (갱신됨) + `{slug}/03_review_log.md` (리뷰 기록)

팀 해체 후 사용자에게 최종 계획을 제시하고 승인을 받는다. 사용자 피드백이 있으면 `book-planner`를 한 번 더 호출해 반영한다.

**선판단 후공개 (운영자 학습 루프 1겹):** 계획을 보여주기 *직전*, 운영자에게 "이 주제·독자라면 어떤 챕터 흐름을 기대하시나요? (한두 줄, 건너뛰어도 됩니다)"를 초대한다 — `learning` 모드에서는 기본 단계로, `production` 모드에서는 승인 요청 메시지에 한 줄로 편승한다. 스케치가 오면 계획 제시 때 **운영자 예상과 갈라진 지점**을 짚어준다 (예측 오류가 학습 신호다). 응답이 없거나 자율 실행 중이면 조용히 생략한다 — 비블로킹. 계획 제시에는 `02_plan.md`의 "설계 근거" 섹션(채택 이유 + 기각 대안)이 포함되어야 한다.

## Phase 4: 챕터 저술 (에이전트 팀)

**실행 모드:** 에이전트 팀 (핵심 Phase)

가장 중요한 Phase다. 팀 구성:

- `chapter-writer` × N (N = min(챕터 수, 3); **narrative는 1~2** — 연속성 보호) — 챕터별 저술
- `style-guardian` × 1 — 실시간 스타일 검수
- `fact-checker` × 1 — **`genre`가 `tech-book`일 때만 합류** (특히 최신 기술 주제). 구체 사실 주장 검증. 다른 장르면 제외
- `continuity-keeper` × 1 — **`genre`가 `narrative`일 때만 합류**. story_bible로 인물·관계·세계관·타임라인·복선 연속성 검수. 다른 장르면 제외
- `editor` × 1 — 챕터 간 전환·일관성 관리

**절차:**

1. `TeamCreate`로 위 팀을 구성한다. 팀 이름: `book-writing-team`.
2. **(narrative만)** `continuity-keeper`가 `02_plan.md`를 읽어 `{slug}/story_bible.md`를 시드한다 (인물·관계·세계관·타임라인·복선 초기 정전). 챕터 저술 전에 끝낸다.
3. `TaskCreate`로 각 챕터를 task로 등록한다. task당 `chapter-writer` 1명을 할당한다. narrative는 이전 챕터의 캐논이 확정된 뒤 다음 챕터로 넘어가도록 순차성을 우선한다.
4. 각 `chapter-writer`는 **저술 시작 전에 `{slug}/style_guide_active.md`·`{slug}/fact_rules_active.md`를 읽고**(없으면 건너뜀) 자기 챕터 초안을 쓰고 `{slug}/chapters/{NN}_draft.md`에 저장한 뒤 `SendMessage`로 `style-guardian`에게 리뷰를 요청한다. (narrative는 `story_bible.md`를 읽고 캐논에 맞춰 쓴다.)
5. `style-guardian`은 활성 프로필의 체크리스트로 검수하고, 편차가 있으면 구체적 수정 제안을 작성해 `SendMessage`로 응답한다.
6. **장르별 전문 검수 (style 합의 후):**
   - **tech-book** — `chapter-writer`가 `fact-checker`에게 검증 요청. 구체 사실 주장·`(사실 확인 필요)` 주석을 레퍼런스 대조로 판정·정정.
   - **narrative** — `chapter-writer`가 `continuity-keeper`에게 검증 요청. story_bible 대조로 인물·관계·세계관·타임라인·복선 모순을 판정. keeper는 새 정전을 bible에 갱신.
   - 두 경우 모두 사실/연속성 오류(❌)는 반드시 반영한다 — style 이견과 달리 저술가 재량으로 덮지 않는다.
7. `chapter-writer`가 style + (fact 또는 continuity) 피드백을 반영하고 `{NN}_final.md`로 저장한다 (미해소 `(사실 확인 필요)` 주석이 남으면 안 된다).
8. 모든 챕터 완료 후 `editor`가 전환부를 점검하고 `{slug}/04_manuscript.md`에 통합 원고를 만든다. (narrative면 `continuity-keeper`에 통합 원고 일괄 대조 + 미회수 복선 점검을 요청한다.)
9. **(tech-book) 뒷부속 검증 패스:** editor 산출 직후 `fact-checker`에게 `04_manuscript.md`의 **front/back matter 한정 검증**을 요청한다 — 서문·에필로그·**참고문헌(항목별 확인 등급 라벨·섹션 헤더·범례 포함)**을 `research/*.md` 원장과 대조한다. 챕터 재검증이 아니라 뒷부속 한정 1패스라 비용이 작다. 챕터 검수 루프는 `chapters/*_draft.md`만 입력으로 받으므로, 이 패스가 없으면 editor가 쓴 부속은 어떤 사실 검증도 없이 Phase 5로 간다.
10. 팀을 해체한다.

**learning 모드 한정 (운영자 학습 루프 3겹):** 첫 챕터의 `{NN}_final.md`가 나오면 운영자에게 알리고 `profiles/{genre}/style-checklist.md`와 함께 직접 읽기를 권한다. 피드백이 오면 반영하고, 없으면 그대로 진행한다 — 저술 풀을 멈추지 않는다 (비블로킹). `production` 모드에서는 생략.

**파(wave) 간 지침 전파 (누적 파일):** 검수자의 통권 관찰은 오케스트레이터의 프롬프트 중계가 아니라 **파일로 전파한다** — 손수 옮기면 누락이 구조적으로 발생한다.
- `style-guardian`은 검수 중 확장·구체화한 규약(카운트 정의 확장, 통권 변주 관찰, 금지 패턴)을 `{slug}/style_guide_active.md`에 누적 append 한다.
- `fact-checker`는 파 종료 시 "다음 파 저술가에게 전할 규율"(관측된 실패 패턴·출처 취급 규칙)을 `{slug}/fact_rules_active.md`에 누적 append 한다.
- 모든 `chapter-writer`는 저술 시작 전에 두 파일을 읽는다(절차 4). 이 규약이 지켜지면 파를 겹쳐 띄워도 최신 지침이 전달된다. 파일 전파를 쓸 수 없는 상황이면 **파 N의 검수가 끝나기 전에 파 N+1을 띄우지 않는다**(배리어 폴백 — 검수의 통권 관찰이 다음 파의 입력이기 때문이다).

**검수 참조 버전 규칙:** 검수자의 자기 파 검수 대상은 `{NN}_draft.md`다. 그러나 **앞 파의 장을 참조할 때는 반드시 `{NN}_final.md`를 읽는다**(존재하면) — draft는 피드백 반영 전 상태라, draft 기준의 교차 참조 판정은 이미 해소된 항목을 미이행으로 오보한다.

**챕터 수가 3개를 초과하면** chapter-writer를 챕터 수만큼 만들지 않고, 3명으로 시작해 각자 여러 챕터를 순차 처리한다(풀 방식). 너무 많은 팀원은 조율 오버헤드를 만든다. **단 `narrative` 장르는** 연속성(인물·복선·타임라인)이 챕터 독립성보다 중요하므로 풀 크기를 1~2로 줄이거나 순차 저술을 우선한다 — 병렬 저술은 서사를 갈라놓기 쉽다.

**스타일 가이드:** 활성 `profiles/{genre}/voice.md`와 `scaffolds.md`를 모든 chapter-writer가 참조한다 (genre는 Phase 0에서 확정, 기본 `tech-book`). 프로필 목록·선택 규칙은 `profiles/_registry.md`. style-guardian은 `profiles/{genre}/style-checklist.md`로 검수한다.

**산출물 (단일 append-only 로그가 단일 진실 원천):**
- `{slug}/chapters/{NN}_draft.md`·`{NN}_final.md` — 챕터별 초안·최종
- `{slug}/04_manuscript.md` — 통합 원고
- `{slug}/book_manifest.json` — EPUB 메타데이터 (editor가 작성)
- `{slug}/style_log.md` — 스타일 검수 로그 (전 장르)
- `{slug}/factcheck_log.md` — 사실 검증 로그 (**tech-book만**)
- `{slug}/continuity_log.md` — 연속성 검수 로그 (**narrative만**)
- `{slug}/length_report.md` — 챕터별 분량 리포트 (editor가 `book-editing` 스킬 절차로 작성 — Phase 4.5 분량 균형 판정의 근거)
- `{slug}/style_guide_active.md`·`{slug}/fact_rules_active.md` — 파 간 지침 전파용 누적 파일 (위 "파 간 지침 전파" 참조)

> 로그는 **단일 append-only 파일**이 단일 진실 원천이다. 풀(pool)로 여러 chapter-writer가 동시에 쓰더라도 같은 파일에 `## {NN}장` 섹션을 append 한다 — `style_log_1-6.md`처럼 샤딩하지 않는다. 샤딩하면 감사 추적이 갈라지고 fact-checker·continuity-keeper의 누적 판정이 흩어진다.
>
> 단, **한 파일에 쓰는 에이전트는 동시에 한 명**이다 (실제 구성이 그렇다 — 파당 style-guardian 1명·fact-checker 1명이 서로 다른 파일을 쓴다). 따라서 append 경합을 막으려고 "마지막에 한 번의 쓰기로 로그를 생성하라"고 지시하지 마라 — 경합은 애초에 없고, 복원력만 없앤다. 검수자는 **한 챕터 판정이 끝날 때마다 즉시 append** 한다. 마지막에 몰아서 쓰면 중단 시 전량 유실된다.

**Phase 4 종료 기준 (모두 충족해야 Phase 4.5로 진행):**
- 모든 챕터가 `{NN}_final.md`로 존재하고 `04_manuscript.md`에 통합됨
- fact-checker의 `editor 메모/재확인 권장` 에스컬레이션과 ❌(오류)·🕒(검증 불가) 판정이 모두 해소되었거나 사용자에 에스컬레이션됨 — **자문이 아니라 BLOCKING** (Phase 5 진행 차단)
- continuity-keeper의 ❌(모순) 판정이 모두 해소되었거나 사용자에 에스컬레이션됨
- `04_manuscript.md`에 `(사실 확인 필요)` / `[리서치 공백]` / `[미완성]` 마커가 남아 있으면 안 된다 — 남으면 해당 Phase로 되돌린다: `[리서치 공백]`은 Phase 1(리서치 보강), `(사실 확인 필요)`는 fact-checker, `[미완성]`은 chapter-writer

## Phase 4.5: 통권 수락 검수 (단일 서브, 신선 컨텍스트)

**실행 모드:** 단일 서브 에이전트 (editor와 분리된 **신선 컨텍스트** — 같은 컨텍스트에서 자기 승인하지 않는다)

챕터를 통합한 editor와 **별개의 새 눈**으로 통권을 게이트한다. `manuscript-reviewer` 에이전트를 `model: "opus"`, FRESH 컨텍스트로 스폰한다 (`manuscript-acceptance` 스킬). editor가 검수자를 겸하지 않는다.

**입력:** `{slug}/04_manuscript.md`, `{slug}/02_plan.md`, `{slug}/book_manifest.json`, 에스컬레이션 로그(`style_log.md`·`factcheck_log.md`·`continuity_log.md` 중 존재하는 것), (있으면) `{slug}/length_report.md` — 분량 균형 판정용
**출력:** `{slug}/05_acceptance.md` — 통권 수락 판정 (계획 대비 커버리지·통권 일관성·미해소 에스컬레이션·금지 마커 잔존 여부, 종합 ACCEPT/BLOCK)

- **ACCEPT** → Phase 5로 진행
- **BLOCK** → Phase 4로 되돌린다(최대 1회 라운드). 1회 라운드 후에도 BLOCK이면 Phase 5로 진행하지 않고 사용자에게 하드 스톱·에스컬레이션한다.

## Phase 5: 표지 + EPUB 빌드 (부분 병렬)

**실행 모드:** 부분 병렬 (cover-designer는 background, epub-builder의 cover-독립 준비를 병행)

표지 생성은 시간이 걸리므로 `cover-designer`를 `run_in_background: true`로 먼저 띄우고, 그 동안 `epub-builder`의 **cover-독립 준비**(매니페스트 검증·콜로폰 작성·책 소개 markdown 초안)를 병행한다. `cover.png`를 실제로 소비하는 지점(EPUB 빌드 호출)에서 join 한다.

- `cover-designer` → 표지 이미지 생성, `{slug}/cover.png` 저장 (background)
- `epub-builder`는 cover-독립 준비를 먼저 진행하고, `cover.png` 준비 완료 후 빌드를 호출 (cover 소비 지점 의존) → `{책-제목}-v{version}.epub` 생성 (프로젝트 루트) **+ 같은 폴더에 책 소개 markdown `{책-제목}-v{version}.md` 동시 산출**

**EPUB 메타데이터:**
- 저자: `Toby-AI` (기본값, Phase 0에서 사용자가 지정한 값이 있으면 그 값 사용)
- 제목: Phase 2에서 확정된 책 제목
- 버전: 초기 실행 시 `1.0.0`, 재실행 시 사용자 요청에 따라 증가 (예: `1.1.0`)
- 언어: `ko`
- 라이선스: `CC BY-NC-SA 4.0` (하네스 기본값, Phase 0에서 사용자가 다른 값을 지정했으면 그 값)
- 장르: Phase 0에서 확정된 `genre`. editor가 매니페스트 `genre` 필드에 기록한다 (재실행 결정성·프로필 재사용용).
- 하네스 버전: Phase 4의 editor가 매니페스트 작성 시 루트 `VERSION` 파일을 읽어 `harness_version` 필드에 주입한다. editor가 빠뜨려도 빌드 스크립트가 백업으로 채운다.

**콜로폰 페이지:** editor가 통합 원고(`04_manuscript.md`)에 `## 판권` 섹션을 작성한다 — 책 버전·발행일·라이선스 명문화·CC 마크/링크·하네스 출처 크레딧·식별자가 한 페이지에 들어간다. 매니페스트의 `license`가 기본값과 다르면 콜로폰 본문도 그 라이선스로 갈음하도록 editor에 명시한다.

**책 소개 markdown:** EPUB과 짝을 이루는 외부 독자용 소개 문서. 블로그·스토어·SNS에 바로 쓸 수 있도록 logline, 책 설명, 대상 독자, 핵심 약속, 차례, 저자 소개, 책 정보로 구성된다. 파일명은 EPUB과 같은 stem (`{책-제목}-v{version}.md`). 작성 규약은 `epub-builder` 에이전트 정의의 "책 소개 markdown" 섹션을 따른다.

## 에러 핸들링

| 시나리오 | 대응 |
|---------|------|
| 리서치 에이전트 하나가 실패 | 1회 재시도, 재실패 시 해당 섹션 누락 명시하고 진행 |
| 스타일 가디언과 챕터 저술가가 3회 왕복에도 합의 실패 | 저술가의 최종본을 채택하고 reviewlog에 기록 |
| 팩트체커와 저술가가 3회 왕복에도 사실 미합의 | 사실 오류는 덮지 않는다 — `factcheck_log.md`에 "미해소(위험)" 명시, editor·사용자에 에스컬레이션 (style 이견과 다른 처리) |
| fact-checker의 `editor 메모/재확인 권장` 에스컬레이션 또는 ❌·🕒 판정이 남음 | **BLOCKING (자문 아님)** — Phase 5 진행 전에 반드시 해소하거나 사용자에 에스컬레이션한다. 의심·검증 불가 인용은 정정·삭제·약화하거나 사용자 판단을 받는다. 절대 조용히 출간하지 않는다 |
| 레퍼런스가 빈약해 fact-checker가 핵심 주장 검증 불가 | Critical 주장만 웹 에스컬레이션, 나머지는 주장 약화/삭제 권고 + 리서치 보강 필요 보고 (해소 전엔 Phase 5 진행 차단) |
| continuity-keeper와 저술가가 3회 왕복에도 연속성 미합의 | 연속성 모순은 덮지 않는다 — `continuity_log.md`에 "미해소(모순 위험)" 명시, editor·사용자에 에스컬레이션 |
| 계획이 인물·설정을 충분히 명시 안 해 story_bible 시드 부실 | 1장 초안에서 캐논을 추출해 bible 초기화, 이후 챕터에서 누적 보강 |
| `04_manuscript.md`에 `(사실 확인 필요)`·`[리서치 공백]`·`[미완성]` 마커 잔존 | **Phase 5 진행 차단** — 해당 Phase로 되돌린다(`[리서치 공백]`→Phase 1, `(사실 확인 필요)`→fact-checker, `[미완성]`→chapter-writer) |
| Phase 4.5 manuscript-reviewer가 BLOCK 판정 | Phase 4로 되돌린다(최대 1회 라운드). 1회 후에도 BLOCK이면 Phase 5로 진행하지 않고 사용자에 하드 스톱·에스컬레이션 |
| 검수·저술 에이전트가 세션 한도·연결 끊김으로 중단 | **재시작보다 `SendMessage` 트랜스크립트 재개가 훨씬 싸다** — 이미 끝낸 측정·웹 조회 결과가 보존된다. 재개 실패 시에만 재시작. 즉시-append 규약 덕에 완료된 챕터 판정은 로그에 남아 있다 |
| 표지 생성 실패 | 플레이스홀더 이미지(검은 배경 + 제목 텍스트)로 대체, 사용자에게 알림 |
| EPUB 빌드 실패 | pandoc 에러 메시지 그대로 보고, 원고 마크다운은 보존 |
| mermaid 렌더 실패 (빌드는 성공) | 원고에 ```` ```mermaid ```` 블록이 있는데 빌드 리포트의 `mermaid:` 줄이 `rendered to ...`가 아니면 epub-builder가 경고를 반환값에 올린다 — 다이어그램이 코드 펜스로 실린 채 조용히 출간하지 않는다. 렌더 환경(mmdc·Chrome)을 고치거나 사용자에 알리고 재빌드한다 |

## 데이터 전달 프로토콜

| 전략 | 용도 |
|------|------|
| 파일 기반 (`{slug}/`) | 모든 Phase 간 산출물 전달, 감사 추적 |
| 메시지 기반 (SendMessage) | Phase 3·4의 팀 내 실시간 조율 |
| 태스크 기반 (TaskCreate) | Phase 4의 챕터 작업 할당 및 진행 추적 |
| 반환값 기반 | 서브 에이전트 모드(Phase 1·2·5)의 결과 수집 |

파일명 컨벤션: Phase 주요 산출물은 `{NN}_{artifact}.md` (NN=Phase 번호). 챕터는 `chapters/{NN}_draft.md`·`{NN}_final.md` (NN=챕터 번호). 로그·매니페스트·표지·리포트 등 부산물은 역할별 고정 파일명을 쓴다 (`style_log.md`·`factcheck_log.md`·`continuity_log.md`·`book_manifest.json`·`cover.png`·`length_report.md` 등 — 샤딩하지 않는다).

## 실행 후 피드백

모든 Phase 완료 및 EPUB 산출 후:
1. 사용자에게 EPUB 경로 + 책 소개 markdown 경로 + 요약 보고. 보고에 **설계 근거 요약**(`02_plan.md`의 "설계 근거" 섹션 — 구조적 선택과 기각한 대안)을 동봉한다
2. **운영자 학습 루프 (자문 전용):**
   - **설명 가능성 자문 한 줄** — "이 책의 핵심 논지를 남에게 한 문단으로 설명할 수 있는가? 막히는 지점이 직접 읽을 지점이다."
   - **직접 검수 표적 제안** — 로그 기반 표적화: `factcheck_log.md`의 ⚠️/🕒 밀집 챕터, `style_log.md`의 최다 왕복 챕터, `05_acceptance.md`의 아슬한 통과 기준 중에서 `production`은 1개, `learning`은 3개를 15~30분 크기로 제안한다. 수행을 추적하거나 강요하지 않는다
3. "개선할 부분이 있나요?"를 짧게 물어본다 (강요하지 않음)
4. 피드백이 오면 아래 **재실행 매트릭스**에 따라 해당 Phase만 재실행

## 재실행 매트릭스

후속 요청은 전체를 다시 돌리지 않고 해당 Phase만 재호출한다. 이미 확정된 산출물은 `{...}_v{N}.{ext}`로 백업한 뒤 갱신한다.

| 요청 유형 | 재실행 범위 |
|----------|------------|
| 리서치 보강 | Phase 1 (리서처 재호출, `01_reference.md` 갱신) |
| 구성·차례 변경 | Phase 2~3 (계획 재작성 + 리뷰 왕복) |
| 특정 챕터 수정 | Phase 4 (해당 챕터만 재저술, 나머지 유지) |
| 표지 변경 | Phase 5 — cover-designer만 재호출 |
| 메타데이터·라이선스 변경 | Phase 5 — epub-builder만 재호출 (재빌드) |

**장르는 `book_manifest.json`의 `genre`를 재사용한다** — 사용자가 장르 변경을 명시하지 않는 한 다시 감지하지 않는다 (재실행 결정성). 챕터·표지·메타 수정은 모두 같은 장르 프로필·같은 EPUB 식별자(`urn:uuid:*`)를 유지하고, 책 버전(매니페스트 `version`)과 발행일만 증가한다.

## 운영자 학습 루프 (자문 전용, 비블로킹)

하네스 학습 루프(아래)가 하네스 자신의 누적 메모리라면, 이것은 **운영자(인간)의 판단력**이 하네스 사용 중에 마모되지 않게 하는 설계다. 정전 스펙·근거는 `docs/learning-loop.md`. 세 겹:

1. **흐름 안 (항상):** Phase 3 선판단 후공개 + `02_plan.md`의 "설계 근거"(기각 대안 ≥2 포함) 동봉 + 완료 보고의 설명 가능성 자문
2. **흐름 밖 (완료 보고):** 로그 기반 직접 검수 표적 제안 (`production` 1개 / `learning` 3개)
3. **메타 (Phase 0):** 위임 다이얼 `delegation_mode: production|learning` — `learning`이면 Phase 3 초대 승격 + Phase 4 첫 챕터 직접 읽기 권유

**불변 원칙:** 모든 터치포인트는 자문 전용·비블로킹이다. 응답이 없으면 조용히 생략하고 진행한다. 질문은 기존 상호작용 지점(Phase 0 확인·Phase 3 승인·완료 보고)에만 편승하며 새 대기 지점을 만들지 않는다.

## 하네스 학습 루프 (append-only, 자문 전용)

하네스가 책을 누적하며 배우도록 가벼운 메모리를 둔다. **읽기 전용 자문이며 절대 블로킹하지 않는다** — 파일이 없으면 조용히 건너뛴다.

- **Phase 5 빌드 직후:** 오케스트레이터가 이번 책의 교훈 한 레코드를 메모리 파일(`{slug}/../book-lessons.md`, 없으면 `.omc/book-lessons.md`)에 **append** 한다 — `{topic, genre, 반복된 style/fact 이슈, 챕터 수, 분량 준수도}`.
- **Phase 0:** 같은 `genre`의 최근 N개 레코드를 읽어 "이전 책에서 배운 점" soft note를 만들어 `book-planner`·`style-guardian`에 전달한다. 강제하지 않는 참고 신호일 뿐이다.
- 파일 부재·읽기 실패는 무시하고 진행한다.

## 테스트 시나리오

**정상 흐름:** 주제 "효과적인 SQL 쿼리 튜닝", 대상 "백엔드 주니어 개발자", 분량 "150페이지" → 리서치 → 5~7개 챕터 계획 → 리뷰 반영 → 챕터 저술 → EPUB 생성

**에러 흐름:** community-researcher가 timeout → 웹/논문 결과만으로 reference.md 작성, 리서치 범위 제한 명시 → 이후 Phase 정상 진행
