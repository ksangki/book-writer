---
name: book-writing-orchestrator
description: Orchestrate a full book-writing workflow from topic to finished EPUB with cover image. Use when the user asks to "write a book", "draft a book", "author a book", "책 쓰기", "책 저술해줘", "책 만들어줘", "전자책 만들어줘", "EPUB 생성", provides a topic/audience/outline and asks to turn it into a book, or says "~에 대한 책을 써줘". Also triggers on follow-ups like "다시 저술", "계획 수정", "챕터 다시 써줘", "표지 바꿔", "책 업데이트", "특정 챕터 보완", "이전 책 개선", "리서치만 다시". Coordinates research, planning, chapter writing in the active genre voice (auto-detected; defaults to tech-book = Toby's style), fact/continuity checks, editing, a proofreading pass (manuscript-ci + writing-deslop), cover design, EPUB assembly, and — every time — the web edition, a one-hour presentation deck, and a brag launch video. Author defaults to Toby-AI (overridable via user prompt — include "저자: {이름}").
---

# Book Writing Orchestrator

주제·주요 내용·대상 독자를 받아 완성된 EPUB과 그 동반 산출물(웹 버전·발표자료·홍보 영상)을 산출한다. 각 Phase에서 전문 에이전트를 호출하고, 중간 산출물을 `{slug}/`에 쌓은 뒤 최종 EPUB과 책 소개 markdown을 프로젝트 루트에 만든다.

## 흐름 한눈에

| Phase | 누가 | 산출물 |
|-------|------|--------|
| 0. 컨텍스트 | 오케스트레이터 | 장르·저자·라이선스·슬러그·위임 모드 확정 |
| 1. 리서치 | 리서처 2~3명 병렬 → `research-lead`(합성) | `research/*.md`, `01_reference.md` |
| 2. 계획 | `book-planner` | `02_plan.md` (+ narrative면 `story_bible.md` 시드) |
| 3. 계획 승인 | 사용자 | 승인된 `02_plan.md` |
| 4. 저술 | `chapter-writer` 최대 4명 병렬 → 묶음별 `fact-checker`/`continuity-keeper` | `chapters/*`, (narrative) `pacing_report.md` |
| 4.2. 그림 | `figure-designer` (`book-figures`) | `figures/fig-N-k.svg`, 그림이 들어간 `chapters/{NN}_final.md` |
| 4.3. 통합 | `editor` | `04_manuscript.md`, `book_manifest.json`, `length_report.md` |
| 4.4. 교정 패스 | `editor` + `manuscript-qa` (원고 CI · writing-deslop) | `ci_report.md`, `proofread_log.md`, 교정된 `04_manuscript.md` |
| 4.5. 수락 게이트 | `manuscript-reviewer` (신선 컨텍스트) | `05_acceptance.md` |
| 5. 표지 + EPUB | `cover-designer`(백그라운드) + `epub-builder` → 빌드 CI | `{책-제목}-v{version}.epub`·`.md` |
| 6. 웹 · 발표자료 · 홍보 영상 | `site-builder` → brag 스킬 | `{slug}/site/`(웹·발표자료), `{slug}/brag-output/brag.mp4` |

독립 검수는 두 곳에만 둔다 — 챕터 묶음마다 한 번의 사실/연속성 패스, 그리고 통권 수락 게이트 한 번. 그 사이에 기계 점검과 문형 교정을 하는 교정 패스(4.4)가 한 번 돈다. 교정 패스는 사실을 판정하지 않고, 기계가 잡는 결함과 AI 글 문형만 걷어낸다. 저술가는 활성 프로필의 체크리스트를 자기 품질 기준으로 삼아 쓰므로 별도의 스타일 왕복 검수는 기본 흐름에 없다(요청 시 `style-guardian`을 쓴다).

## 서브에이전트 운용

- 에이전트는 `Agent` 도구로 호출하고, 서로 독립인 호출(리서처들, 저술가들)은 한 메시지에 모아 병렬로 띄운다. 팀 도구(`TeamCreate`·`SendMessage`)에 의존하지 않는다 — 모든 조율은 `{slug}/`의 파일과 반환값으로 한다.
- 첫 브리프에 필요한 것을 다 담는다: `genre`, 슬러그, 담당 범위(챕터 번호 등), 읽을 파일 경로, 쓸 파일 경로, 저자·라이선스처럼 이 Phase에 필요한 사용자 지정값. 파일 내용을 프롬프트에 붙여넣지 말고 경로를 준다.
- 각 에이전트에게 반환값은 짧게 요청한다 — 쓴 파일 경로, 미해소 항목, 사용자 판단이 필요한 것. 반환된 결과를 오케스트레이터가 다시 검증하거나 다시 쓰지 않는다.
- 모델은 지정하지 않는다. 모든 에이전트가 현재 세션의 모델 설정을 그대로 상속한다 (frontmatter에도 `model`을 두지 않는다).
- 에이전트가 중단되면 이미 쓴 파일(로그는 챕터마다 즉시 append된다)을 확인하고, 남은 범위만 담아 다시 호출한다.

## Phase 0: 컨텍스트 확인

1. 사용자 입력에서 주제·주요 내용·대상 독자를 뽑는다. 하나라도 불명확하면 `AskUserQuestion`으로 짧게 묻는다. `저자: {이름}`이 있으면 그 값, 없으면 `Toby-AI`. `라이선스: {값}`이 있으면 그 값, 없으면 매니페스트 `license`를 비워 빌드 스크립트 기본값(`CC BY-NC-SA 4.0`)을 쓴다.
2. 장르를 정한다. `장르: {값}`이 있으면 그대로 쓴다. 없으면 `profiles/_registry.md`의 감지 규칙으로 추정하고, 신호가 분명하면 알리고 진행하며, 애매하면 `AskUserQuestion`으로 추정값을 첫 옵션으로 제시해 확인받는다.
3. 위임 모드를 정한다. `모드: 학습`이나 "이 주제를 공부하려고" 같은 명확한 학습 신호가 있으면 `learning`, 없으면 묻지 않고 `production`. 어차피 질문할 일이 있으면 거기에 함께 묻는다 (`docs/learning-loop.md`).
4. 같은 `genre`의 교훈이 `book-lessons.md`(없으면 `.omc/book-lessons.md`)에 있으면 최근 몇 건을 읽어 planner·writer 브리프에 참고 메모로 넣는다. 파일이 없으면 건너뛴다.
5. 제목 후보와 슬러그를 만든다 (예: `AI 시대의 개발자 철학` → `ai-developer-philosophy`). `{slug}/`가 없으면 새 실행, 있고 부분 수정 요청이면 재실행 매트릭스를 따르고, 있는데 완전히 새 입력이면 기존 폴더를 `{slug}_prev-{timestamp}/`로 옮긴 뒤 새로 시작한다. 재실행에서는 `book_manifest.json`의 `genre`·`delegation_mode`를 그대로 쓴다.

## Phase 1: 리서치

장르에 맞는 리서처를 한 메시지에서 병렬로 띄운다. 각자 `{slug}/research/`에 자기 파일을 쓴다.

| genre | 리서처 |
|-------|--------|
| `tech-book` | `web-researcher`, `paper-researcher`, `community-researcher` |
| `essay` | `web-researcher`, `community-researcher` (학술 근거가 중요한 주제면 `paper-researcher` 추가) |
| `practical`·`narrative` | `web-researcher`, `community-researcher` |

모두 끝나면 `research-lead`를 호출해 `research/*.md`를 `{slug}/01_reference.md`로 합성한다. `research/*.md`는 합성 후에도 보존한다 — `fact-checker`의 1차 대조 근거다. 리서처 하나가 실패하면 한 번 다시 띄우고, 또 실패하면 그 소스 없이 진행하며 레퍼런스의 "리서치 한계"에 적는다.

## Phase 2: 저술 계획

`book-planner`에게 `genre`, 주제·주요 내용·대상 독자, `01_reference.md`, 활성 `profiles/{genre}/scaffolds.md`, (있으면) 교훈 메모를 준다. 산출물은 `{slug}/02_plan.md` — 제목 후보 3개, 책 특성, 내러티브 아크, 설계 근거(기각한 대안 2개 이상), 챕터 목록, 챕터별 오프닝·클로징·스캐폴드 배정. `narrative`면 planner가 `{slug}/story_bible.md`도 시드한다.

## Phase 3: 계획 승인

사용자에게 계획을 보여주고 승인을 받는다. 보여주기 직전, 운영자에게 "이 주제·독자라면 어떤 챕터 흐름을 기대하시나요? (한두 줄, 건너뛰어도 됩니다)"를 초대한다 — `learning`에서는 별도 단계로, `production`에서는 승인 요청에 한 줄로 붙인다. 스케치가 오면 계획과 갈라진 지점을 짚어준다. 계획 제시에는 `02_plan.md`의 설계 근거를 포함한다. 피드백이 있으면 `book-planner`를 한 번 더 호출해 반영한다.

사용자가 계획의 비판적 검토를 원하면 그때 `plan-reviewer`를 한 번 호출해 `03_review_log.md`를 받고, planner가 반영한다.

## Phase 4: 저술

**저술.** 챕터를 연속된 묶음으로 나눠 `chapter-writer`에게 맡긴다 — 한 명이 2~4장, 최대 4명, 한 메시지에서 병렬로. 연속 묶음이어야 저술가가 자기 묶음 안의 전환을 직접 다듬을 수 있다. 묶음마다 끝나는 시점에 검수를 붙이려면 `run_in_background: true`로 띄워 완료 알림을 하나씩 받는다. `narrative`는 서사가 갈라지지 않도록 저술가 1명(길면 2명)이 순서대로 쓴다. 브리프에는 담당 장 번호, `02_plan.md`, `01_reference.md`, 활성 프로필(`voice.md`·`scaffolds.md`·`style-checklist.md`), (narrative) `story_bible.md`, 교훈 메모를 준다.

저술가는 검수자가 있는 장르(`tech-book`·`practical`·`narrative`)에서는 `chapters/{NN}_draft.md`를, 없는 장르(`essay`)에서는 바로 `chapters/{NN}_final.md`를 쓴다.

**묶음별 검수 (파이프라인).** 저술가 하나가 끝나는 즉시 그 묶음의 검수자를 띄운다 — 다른 묶음을 기다리지 않는다.
- `tech-book` → `fact-checker`: 구체 사실 주장과 `(사실 확인 필요)` 주석을 `01_reference.md`·`research/*.md`와 대조하고, 정정·약화·삭제를 draft에 직접 반영해 `{NN}_final.md`로 저장한다. `factcheck_log.md`에 장별로 기록한다.
- `practical` → `fact-checker`: 안전·건강·법규 사실만 본다 — 식품 안전 온도·보관 기간·알레르겐·응급 대처·여행 법규, "~해도 안전하다"류 단정. 틀리면 독자가 실제로 다치는 영역이라서다. 맛·취향·팁은 대상이 아니다.
- `narrative` → `continuity-keeper`: `story_bible.md`와 대조해 모순을 직접 고치고 `{NN}_final.md`로 저장하며, 새 정전을 bible에 반영한다. narrative는 순차 저술이므로 저술가가 장을 끝낼 때마다 이어서 검수하고, 장마다 긴장도·지배 감정·씬 수·아크 위치를 한 줄 계측한다. 마지막 장을 마치면 `pacing_report.md`(감정 곡선·씬 페이싱, 자문 전용)를 만든다 — editor가 참고할 뿐 BLOCK 사유가 아니다.

검수자가 스스로 고칠 수 없는 항목(고치면 장의 논지가 무너지는 사실 오류, 저자 의도를 알아야 하는 설정 충돌)만 로그에 `미해소`로 남기고 반환값에 올린다. 오케스트레이터는 이를 사용자에게 묻는다.

## Phase 4.2: 그림

모든 묶음의 사실/연속성 검수가 끝나 `{NN}_final.md`가 모이면, editor 통합 전에 `figure-designer`를 호출한다(`book-figures` 스킬). 계획에 그림 배정이 있으면 매번 돈다. 장르 기준은 `book-planning`의 배정 표를 따른다. tech-book·practical은 필수, essay는 선택, narrative는 기본 없음이다. 배정이 하나도 없으면 건너뛴다.

- 계획의 장별 그림 배정(장마다 1~2개)을 공용 `figlib`으로 SVG로 그린다. 색은 매니페스트 `theme`이다.
- 저술가가 남긴 `<!-- 그림 N-k -->` 자리에 캡션과 함께 넣고, 그림을 읽는 한두 문장을 붙인다.
- 번호를 나오는 순서로 맞추고, 모든 그림을 캡처해 확인한다.
- 표는 저술가가 쓴다. figure-designer는 배정된 표와 `**표 N-k.**` 캡션이 있는지만 확인하고, 빠진 것은 반환값에 올린다. 오케스트레이터는 빠진 표를 해당 장 `chapter-writer`에게 한 번 보낸다.

## Phase 4.3: 통합

그림까지 들어간 `{NN}_final.md`가 모이면 `editor`를 호출한다. editor는 전환부·용어·콜백을 다듬고, 통권 변주(오프닝·클로징·말버릇이 여러 장에 같은 틀로 반복되는지)를 바로잡고, 서문·에필로그·참고문헌·콜로폰(`## 판권`)을 쓰고, `04_manuscript.md`·`book_manifest.json`·`length_report.md`를 만든다. `practical` 요리 계열이면 `profiles/practical/partials/conversion-tables.md`의 환산표를 부록에 싣고, `narrative`면 `pacing_report.md`를 참고해 평탄한 긴장 구간·돌출 씬을 손볼지 정한다. 매니페스트에는 `genre`, `delegation_mode`, 저자, (지정됐으면) 라이선스, 루트 `VERSION`의 `harness_version`을 넣는다.

`learning` 모드에서는 첫 `{NN}_final.md`가 나오면 운영자에게 알리고 `style-checklist.md`와 함께 직접 읽어보길 권한다. 저술은 멈추지 않는다.

## Phase 4.4: 교정 패스 (원고 CI · writing-deslop)

그림이 들어간 뒤 editor 통합이 끝나면, 수락 게이트 전에 `editor`를 한 번 더 호출해 `manuscript-qa` 스킬을 수행하게 한다. 모든 책에서 매번 돈다.

1. **원고 CI 정적 점검:** `.claude/skills/manuscript-qa/scripts/run_ci.sh check {slug}/04_manuscript.md` → `{slug}/ci_report.md`. 중복 문단은 정리하고, 과한 단정어는 근거가 받치지 못하는 문장만 고친다. 건수를 0으로 만드는 것이 목표가 아니다.
2. **writing-deslop 11개 패턴:** writing-deslop 스킬(Skill 도구로 부르거나, `~/.claude/skills/`·플러그인 캐시에서 SKILL.md를 찾는다)의 정의로 원고를 훑고, 확정한 것만 활성 프로필의 문체로 고친다. 기본은 외부 전송 없는 직접 점검이다. 문단을 외부 API로 보내는 `--jev`는 기본으로 쓰지 않는다. 두 조건이 모두 맞을 때만 쓴다. 첫째, 사용자가 이 세션에서 외부 전송을 명시적으로 허락했다. 둘째, 원고의 비식별 검토가 끝났다. 쓰면 `proofread_log.md`에 "Jev 사용: 사용자 허락 {날짜}"를 남긴다. 기밀·미공개 내용이 섞일 수 있는 원고를 외부 서비스로 보내지 않기 위해서다.
3. 고친 곳은 `04_manuscript.md`와 그 원천(`chapters/{NN}_final.md` 또는 부속 원고) 양쪽에 반영하고, `{slug}/proofread_log.md`에 기록한다.

도구가 설치돼 있지 않으면 건너뛴다. manuscript-ci가 없으면 `run_ci.sh`가 종료 코드 3을 낸다. writing-deslop 스킬이 없으면 스킬 파일을 찾을 수 없다. 어느 쪽이든 건너뛴 사실을 로그와 완료 보고에 적는다. 교정 패스는 사실을 바꾸지 않는다. 문형을 고치다 주장이 달라질 것 같으면 "보류"로 남긴다.

## Phase 4.5: 통권 수락 게이트

`manuscript-reviewer`를 새 컨텍스트로 호출한다 — 원고를 만든 editor가 스스로 승인하지 않게 하기 위해서다. 입력은 `04_manuscript.md`, `02_plan.md`, `book_manifest.json`, `length_report.md`, `editor_notes.md`, 존재하는 로그(`factcheck_log.md`·`continuity_log.md`·`proofread_log.md`·`ci_report.md`), (narrative) `story_bible.md`, (tech-book) `research/*.md`, 활성 `style-checklist.md`. 산출물은 `05_acceptance.md`. 기본 흐름에 별도 스타일 검수가 없으므로 voice 이탈도 이 게이트가 본다 — 여러 장에 걸친 이탈이면 해당 장들에 `style-guardian`을 한 번 보낸다.

- **ACCEPT** → Phase 5.
- **BLOCK** → 판정문의 조치를 담당자(해당 장 `chapter-writer`·`fact-checker`·`editor`)에게 한 번 보낸 뒤, 영향받은 기준만 다시 판정받는다. 그래도 BLOCK이면 빌드하지 않고 사용자에게 판단을 구한다.
- 미해소 마커(`(사실 확인 필요)`·`[리서치 공백]`·`[미완성]`)나 미해소 사실 오류가 남은 원고는 사용자가 명시적으로 승인하지 않는 한 빌드하지 않는다. 틀린 사실이 담긴 책이 조용히 나가는 것이 이 하네스에서 가장 비싼 실패다.

## Phase 5: 표지 + EPUB

`cover-designer`를 백그라운드로 먼저 띄우고(`{slug}/cover.png`), 동시에 `epub-builder`를 호출한다. epub-builder는 매니페스트·콜로폰 정합성 확인과 책 소개 초안처럼 표지와 무관한 일을 먼저 하고, `cover.png`가 생긴 뒤 빌드한다. 산출물은 프로젝트 루트의 `{책-제목}-v{version}.epub`과 같은 stem의 책 소개 `{책-제목}-v{version}.md`.

EPUB 메타데이터: 저자(기본 `Toby-AI`), Phase 2에서 확정된 제목, 버전(첫 실행 `1.0.0`, 재실행 시 증가), 언어 `ko`, 라이선스(기본 `CC BY-NC-SA 4.0`), `genre`, `harness_version`. epub-builder가 mermaid 미렌더나 epubcheck 문제를 보고하면 그대로 사용자에게 전한다.

빌드가 끝나면 `manuscript-qa`의 빌드 점검을 돌린다: `.claude/skills/manuscript-qa/scripts/run_ci.sh check-build {책-제목}-v{version}.epub`. 기준은 `No build findings.`다. 결함이 나오면 `editor`가 원인을 고친다. 원인은 대개 원고의 마크다운이다. 예를 들어 `[라벨](날짜)`처럼 붙어 링크로 해석된 괄호가 있다. 이 단계에서 허용되는 수정은 마크다운 구문뿐이고 문장은 바꾸지 않는다. 문장이 바뀌면 수락 게이트를 우회하게 된다. 수정은 `proofread_log.md`에 append하고, 같은 버전으로 다시 빌드해 덮어쓴다(이 루프에서는 `_prev/` 이동을 하지 않는다). 두 번 고쳐도 결함이 남으면 사용자에게 묻는다.

## Phase 6: 웹 · 발표자료 · 홍보 영상

EPUB과 책 소개가 나오면 매번, 같은 방식으로 동반 산출물을 만든다. 책을 소개하고 나누는 일이 책 한 권마다 즉흥으로 달라지지 않게 하기 위해서다.

1. **웹·발표자료:** `site-builder`를 호출한다(`site-build` 스킬).
   - 산출물: `{slug}/site/`(웹 `index.html`, `presentation/index.html`, `epub/`, `figures/`, `media/`, `cover.png`, `BOOK.md`, `.gitignore`)과 `{slug}/deck/slides.py`
   - 덱은 수락된 원고에서만 내용을 가져온다. 모든 내용 슬라이드에 '쉽게 말하면' 비유 한 줄을 단다.
2. **홍보 영상:** site-builder가 끝나면 오케스트레이터가 brag 스킬을 부른다(`/brag` — 모델별 분기는 brag가 처리한다).
   - 소스는 `{slug}/site/`이고, 출력 위치는 `{slug}/brag-output/`이다. 호출 지시에 두 경로를 모두 적는다. 영상 작업물(node_modules·프레임·세션 상태)이 공개 폴더에 섞이지 않게 하기 위해서다.
   - 호출 뒤 `ls -a {slug}/site | grep -E 'brag|\.omc|node_modules'`가 비어 있는지 확인한다. 무엇이 나오면 `{slug}/brag-output/`으로 옮기거나 지운다.
   - 매번 같은 지시로 부른다:
     > 책 「{제목} — {부제}」의 소개 영상을 만든다. 소스는 `{slug}/site/`(웹 버전·표지·그림), 결과물과 작업 파일은 전부 `{slug}/brag-output/`에 쓴다. 톤은 polished, 가로형, 약 20초. 화면 텍스트는 한국어. 색은 표지와 웹 버전을 따른다. 책의 결론 문장, site-builder가 추천한 대표 그림 2~3개, 핵심 수치 하나(출처 라벨 그대로), 마지막 장면에 표지와 "웹에서 읽기" 주소(공개 주소가 있을 때만)를 넣는다. 원고에 없는 주장·수치·과장된 카피는 쓰지 않는다.
   - 산출물: `{slug}/brag-output/brag.mp4`, `brag.jpg`(포스터), `share-copy.txt`
   - brag 플러그인이 설치돼 있지 않거나 렌더에 필요한 도구가 없으면 영상은 건너뛰고, 그 사실과 설치 방법을 완료 보고에 적는다. 영상이 없다고 책 산출을 실패로 보지 않는다.
3. **공개하지 않는다.** 공개 저장소 생성·푸시는 사용자가 원고와 비식별을 확인한 뒤 요청할 때 한다. 올릴 때는 `{slug}/site/`의 파일을 이름으로 지정해 커밋한다(`git add -A` 금지). 커밋 전에 `git status --short`의 목록이 허용 목록과 맞는지 대조한다. 허용 목록은 `index.html`·`presentation/`·`epub/`·`figures/`·`media/`·`cover.png`·`BOOK.md`·`README.md`·`.gitignore`다. `brag-output/`·`.omc/`·`deck/shots/`·`figures/shots/`는 공개 저장소에 두지 않는다.

## 완료 보고

1. EPUB 경로, 책 소개 md 경로, 웹 버전·발표자료(`{slug}/site/`)·홍보 영상(`{slug}/brag-output/brag.mp4`) 경로, 짧은 요약, `02_plan.md` 설계 근거 요약. 교정 패스와 빌드 CI 결과(고친 건수, 건너뛴 도구)도 한 줄로.
2. 설명 가능성 자문 한 줄: "이 책의 핵심 논지를 남에게 한 문단으로 설명할 수 있는가? 막히는 지점이 직접 읽을 지점이다."
3. 직접 검수 표적 제안 — `production`은 1개, `learning`은 3개, 각 15~30분 크기. 로그에서 고른다: `factcheck_log.md`에서 약화·삭제가 몰린 장, `continuity_log.md`의 미해소, `05_acceptance.md`에서 아슬하게 통과한 기준. 수행을 강요하거나 추적하지 않는다.
4. 교훈 한 레코드를 `book-lessons.md`(없으면 `.omc/book-lessons.md`)에 append한다 — `{topic, genre, 반복된 사실/연속성 이슈, 수락 게이트 BLOCK 사유, 챕터 수, 분량 준수도}`.
5. "개선할 부분이 있나요?"를 짧게 묻는다.

학습 루프 터치포인트는 모두 자문이며 응답이 없으면 그대로 진행한다. 새 대기 지점을 만들지 않는다.

## 재실행 매트릭스

후속 요청은 해당 Phase만 다시 돌린다. 덮어쓸 산출물은 `{name}_v{N}.{ext}`로 백업한다. 장르·식별자(`urn:uuid:*`)는 유지하고 책 버전과 발행일만 올린다.

| 요청 | 재실행 범위 |
|------|------------|
| 리서치 보강 | Phase 1 (해당 리서처 + 합성) |
| 구성·차례 변경 | Phase 2~3 |
| 특정 챕터 수정 | Phase 4 해당 장(저술 → 검수) → 4.2 해당 장(그림 자리·번호) → 4.3 editor 부분 갱신 → 4.4 → 4.5 → 5 → 6 |
| 표지 변경 | Phase 5 `cover-designer` → 재빌드 → 빌드 CI → Phase 6(site 복사·웹 재빌드·덱 재빌드, 영상은 선택) |
| 메타데이터·라이선스 변경 | Phase 5 `epub-builder` → 빌드 CI → Phase 6(site 복사·웹 재빌드. 판번호가 바뀌면 EPUB 파일명이 달라지므로 덱도 재빌드) |
| 그림만 다시 | Phase 4.2 해당 그림 → editor 부분 갱신 → 4.5의 (i) → 5 → 6 |
| 문체 점검 요청 | `style-guardian`을 지정 장에 한 번 |
| 교정만 다시(CI·deslop) | Phase 4.4 → 원고가 바뀌면 4.5의 영향받은 기준 → 5 → 6 |
| 발표자료·웹만 다시 | Phase 6 `site-builder` (덱 내용만이면 `deck/slides.py` 수정 후 재빌드) |
| 홍보 영상만 다시 | Phase 6 brag 호출만 |
| 페이싱 분석 요청 (narrative) | `continuity-keeper`로 `pacing_report.md`만 재산출 |

## 에러 대응

| 상황 | 대응 |
|------|------|
| 저술가가 `[리서치 공백]`으로 장이 계획 분량의 절반 아래로 줄었다고 보고 | 해당 주제로 리서처를 한 번 보강 호출한 뒤 그 장만 다시 쓴다 |
| 레퍼런스가 빈약해 fact-checker가 핵심 주장을 확인하지 못함 | 확인 못 한 주장은 약화·삭제하고, 핵심 주장이라 그럴 수 없으면 사용자에게 알린다 |
| narrative 계획이 인물·설정을 충분히 정하지 않음 | continuity-keeper가 1장 final에서 캐논을 뽑아 bible을 채운다 |
| 표지 생성 실패 | ImageMagick 타이포 표지로 대체하고 알린다 |
| EPUB 빌드 실패 | 에러 메시지를 그대로 보고하고 원고는 보존한다 |
| 선택 도구가 없음 (manuscript-ci 종료 코드 3 · writing-deslop 스킬 없음 · Chrome 없음(shot.sh 종료 코드 2) · brag 플러그인 없음) | 해당 단계만 건너뛰고 흐름은 계속한다. 건너뛴 도구와 설치 방법을 완료 보고에 적는다 |
| 덱 빌드가 종료 코드 1 (`'쉽게 말하면'` 누락 또는 참조 파일 없음) | 누락 슬라이드에 `ez()`를 달거나 site에 그림·표지를 복사한 뒤 다시 빌드한다 |

## 파일 규칙

Phase 산출물은 `{NN}_{artifact}.md`(NN = Phase 번호), 챕터는 `chapters/{NN}_draft.md`·`{NN}_final.md`(NN = 챕터 번호). 로그는 역할별 단일 파일(`factcheck_log.md`·`continuity_log.md`)에 `## {NN}장` 섹션으로 append하고, 한 장의 판정이 끝날 때마다 바로 쓴다 — 중단돼도 끝낸 판정은 남는다.
