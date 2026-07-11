# Book Writer Project

주제·주요 내용·대상 독자가 주어지면 완성된 EPUB을 산출하는 자동화 하네스가 구축되어 있다.

## 하네스: 책 저술 자동화

**목표:** 주제가 주어지면 리서치 → 저술 계획 → 계획 리뷰 → 챕터 저술(Toby 스타일) → EPUB 빌드까지 자동 수행한다. 저자명은 기본값 `Toby-AI`이며, 사용자가 프롬프트에 `저자: {이름}` 한 줄을 넣으면 그 값이 매니페스트·표지·EPUB 메타까지 그대로 전파된다.

**트리거:** 책/전자책/EPUB 저술 관련 작업 요청 시 `book-writing-orchestrator` 스킬을 사용하라. 특정 Phase만 재실행하거나 챕터 수정 요청도 동일 스킬이 처리한다. 단순 질문(예: "책 저술이 뭐야?")은 직접 응답 가능.

**스타일 가이드 (장르 프로필):** 하네스 v1.3.0부터 문체는 단일 가이드가 아니라 **장르별 프로필**(`profiles/{genre}/`)로 관리된다. 오케스트레이터가 Phase 0에서 장르(`tech-book`/`narrative`/`practical`/`essay`, 기본 `tech-book`)를 감지·확인하면, 그 프로필의 `voice.md`·`scaffolds.md`·`style-checklist.md`가 저술·검수의 제약 조건이 된다. 챕터 저술가와 스타일 가디언은 활성 프로필을 준수한다. 프로필 목록·선택 규칙은 `profiles/_registry.md`. 루트 `toby-book-writing-style.md`는 `tech-book` 프로필의 뿌리이자 하위호환 기준 문서로 유지된다. 확장 후속(장르별 fact-checker·구조화 EPUB·소설 연속성 추적)은 `docs/harness-roadmap.md` 참조.

**산출 경로:**
- 중간 산출물: `{book-slug}/`
- 최종 산출물(프로젝트 루트, 같은 폴더에 짝으로 산출):
  - `{책-제목}-v{version}.epub` — 본문 EPUB
  - `{책-제목}-v{version}.md` — 외부 독자용 책 소개 markdown (logline·대상 독자·차례·저자 소개)

**브랜치 운영 패턴:** 하네스 자체(에이전트·스킬·CLAUDE.md·README)는 `main` 브랜치에서 관리하고, **각 책은 자기 브랜치**(예: `rust-for-java-developer`, `french-cooking`, `worktree-sf`)에서 산출한다. 새 책을 시작할 때는 `main`에서 새 브랜치를 따고, 거기서 오케스트레이터를 돌린다. 이렇게 하면 하네스 변경과 책 산출물이 섞이지 않는다.

> **반드시 현재 `main`에서 분기하라.** 책 worktree는 분기 시점의 하네스 스펙(에이전트·스킬·프로필)을 자동 로드한다 — 오래된 브랜치나 worktree(예: `.claude/worktrees/team-five/...`의 스냅샷)에서 분기하면 자동 로드되는 스펙이 정전(canonical)과 어긋나 구버전 동작으로 산출된다. 새 책은 항상 최신 `main`에서 따서 시작한다.

**학습 루프 (두 개):** 하네스에는 방향이 다른 두 학습 루프가 있다 — 하네스 자신이 책 산출 교훈을 누적하는 **하네스 학습 루프**(`book-lessons.md`, v1.8.0)와, 운영자(인간)의 판단력이 완전 위임으로 마모되지 않게 상호작용 기본값(선판단 후공개·설계 근거 동봉)·로그 기반 직접 검수 표적·위임 다이얼(`delegation_mode: production|learning`)을 설계한 **운영자 학습 루프**(v1.9.0). 운영자 터치포인트는 전부 자문 전용·비블로킹이며 production 기본값은 기존 동작과 동일하다. 정전 스펙은 `docs/learning-loop.md`.

**하네스 버전:** 프로젝트 루트의 `VERSION` 파일이 단일 출처. 현재 `v1.9.1`. 책 매니페스트의 `version`(책의 판본)과 다른 개념이다 — 하네스는 도구의 진화, 책 매니페스트는 각 책의 개정을 추적한다. 매니페스트의 `harness_version` 필드를 통해 산출된 책의 콜로폰에도 노출된다.

**책 콘텐츠 라이선스:** 산출되는 책의 기본 라이선스는 `CC BY-NC-SA 4.0`(저작자 표시·비상업적 이용·동일조건 변경허락). 하네스 코드 라이선스(MIT)와 별개다 — `LICENSE` 파일은 하네스 자체에만 적용되고, 각 책의 라이선스는 EPUB의 콜로폰(`## 판권` 섹션)과 OPF의 `<dc:rights>`로 표기된다. 책별로 다른 라이선스를 쓰려면 `book_manifest.json`의 `license` 필드(예: `"CC BY 4.0"`, `"CC0"`, `"All rights reserved"`)에 명시한다.

## 변경 이력

| 날짜 | 하네스 버전 | 변경 내용 | 대상 | 사유 |
|------|-------------|----------|------|------|
| 2026-04-17 | 0.1.0 | 초기 구성 (에이전트 11 + 스킬 12 + 오케스트레이터) | 전체 | - |
| 2026-04-18 | 0.2.0 | `{slug}/` 루트 컨벤션 정착, EPUB을 프로젝트 루트로 산출 | 오케스트레이터, 에이전트, README | 책 폴더를 `_workspace/` 스크래치에서 프로모션 |
| 2026-04-18 | 0.2.0 | 저자명 매니페스트 기반으로 가변화 (기본값 `Toby-AI` 유지) | editor, cover-designer, epub-builder, build_epub.sh, README | 다른 사용자가 자기 이름으로 책을 낼 수 있도록 |
| 2026-04-18 | 0.2.0 | 라이선스를 MIT로 전환 | LICENSE | 오픈 소스 배포 정합성 |
| 2026-04-28 | **1.0.0** | EPUB과 짝을 이루는 책 소개 markdown 산출 추가 — feature-complete 베이스라인 (~12권 산출 검증) | epub-builder, epub-build, 오케스트레이터, README | 마케팅·공유용 외부 독자 카피 자동화 |
| 2026-05-04 | **1.1.0** | 정합성 정비 (CLAUDE.md 저자 가변 반영, 변경 이력 도입, 브랜치 운영 패턴 명시, 리서처/스타일 가디언 재실행 정책 보강) + `VERSION` 파일 도입 + README 버전 표시 | CLAUDE.md, README, VERSION, web/paper/community-researcher, style-guardian, plan-reviewer | 하네스 감사로 발견된 drift 보정 + 공식 버저닝 도입 (minor 업그레이드, breaking change 없음) |
| 2026-05-07 | **1.2.0** | 책 본문에 콜로폰(`## 판권`) 페이지 도입 — 책 버전·발행일·라이선스 명문화·CC 마크/링크·하네스 크레딧·식별자 노출. 기본 콘텐츠 라이선스 `CC BY-NC-SA 4.0` 채택 (매니페스트 `license` 필드로 책별 오버라이드 가능). `build_epub.sh`의 하드코딩된 `rights:` 줄을 매니페스트 기반으로 교체. | editor, book-editing, build_epub.sh, epub-builder, epub-build, orchestrator, VERSION, CLAUDE.md | 책 버전을 독자에게 노출 + CC 라이선스 정책 명문화 + `rights` drift 정리 |
| 2026-05-25 | **1.3.0** | **장르 추상화** — 단일 Toby 문체 고정을 장르별 프로필로 분리. `profiles/{genre}/`(voice·scaffolds·style-checklist) 신설: `tech-book`(기존 Toby + 신선도·사실 규율)·`narrative`·`practical`·`essay`. Phase 0에 장르 자동 감지+확인 추가, `genre`를 전 Phase로 전파. 매니페스트에 `genre` 필드(빌드 시 dc:subject로 노출). 후속 백로그 `docs/harness-roadmap.md`(P2 fact-checker·P3 구조화 EPUB·P4 소설 연속성). | profiles/*, orchestrator, book-planner, book-planning, chapter-writer, chapter-writing, style-guardian, style-review, community-researcher, editor, book-editing, build_epub.sh, VERSION, CLAUDE.md, README | IT 외 장르(소설·실용서·에세이) 지원 + 최신 기술서 신선도 강화 (minor, breaking 없음 — tech-book 기본값) |
| 2026-05-25 | **1.4.0** | **최신 기술서 fact-checker** (로드맵 P2) — `fact-checker` 에이전트 + `fact-check` 스킬 신설. tech-book 장르 한정으로 Phase 4 팀에 합류, style 합의 후 구체 사실 주장(수치·인용·버전·연도·API·단정)을 레퍼런스 대조로 판정(✅/❌/⚠️/🕒)하고 `(사실 확인 필요)` 주석 해소. `factcheck_log.md` 기록. 사실 오류는 저술가 재량으로 덮지 않음(에스컬레이션). 리서처(web/paper/lead)에 신선도 메타(발행일·"{버전}/{연도} 기준"·검색 시점) 추가. 비용 통제: 레퍼런스 1차 → Critical만 웹 2차. | fact-checker, fact-check, orchestrator, web/paper-researcher, research-lead, chapter-writer, editor, VERSION, CLAUDE.md, README, harness-roadmap | 빠르게 변하는 기술의 사실 정확성을 일급 역할로 분리 (minor, breaking 없음 — tech-book만 활성) |
| 2026-05-25 | **1.5.0** | **실용서 구조화 데이터 EPUB** (로드맵 P3) — 번들 스타일시트 `epub-build/styles/epub.css` 신설. 실용서(요리·여행) 챕터가 pandoc fenced div(`::: meta`·`::: ingredients`·`::: steps`·`::: tip`·`::: warning`·`::: itinerary`)로 메타 박스·재료·단계·콜아웃·일정표를 작성하면 EPUB에서 박스로 렌더. `build_epub.sh`가 스크립트 상대 경로로 CSS 자동 임베드(`--css`). 특정 클래스만 스타일 → 전 장르 안전 적용. practical 프로필 scaffolds·voice에 fenced div 규약 명문화. | epub.css, build_epub.sh, epub-build, profiles/practical, VERSION, CLAUDE.md, README, harness-roadmap | 실용서의 재료·단계·일정표를 산문이 아닌 구조화 블록으로 (minor, breaking 없음 — 클래스 스코프 CSS) |
| 2026-05-25 | **1.6.0** | **테크 리서치 소스 확장** — tech-book 리서치 커버리지를 대폭 넓힘. community: Lobsters·Dev.to·GitHub Issues/PR·Discord/Slack·X·Mastodon·GeekNews·커리어리 추가, 버전 민감 주제는 GitHub Issues/릴리스 토론 비중↑. web: 공식 1차 소스(릴리스 노트·체인지로그·RFC/스펙·GitHub 릴리스)·회사 엔지니어링 블로그(우아한형제들·카카오·토스·네이버 D2·LINE·Netflix·Cloudflare)·컨퍼런스 발표·기술 뉴스레터 추가, 버전·수치는 1차 소스 우선(fact-checker 대조). paper: Semantic Scholar·DBLP·USENIX·OpenReview·주요 학회 proceedings 추가. | community-researcher, community-research, web-researcher, web-research, paper-researcher, VERSION, CLAUDE.md | 리서치 소스가 좁다는 피드백 — 1차·권위 소스와 최신 변경 채널로 폭 확대 (minor, breaking 없음) |
| 2026-05-25 | **1.7.0** | **소설 연속성 추적** (로드맵 P4) — `continuity-keeper` 에이전트 + `continuity-check` 스킬 신설 (narrative 전용 Phase 4 멤버). `{slug}/story_bible.md`(인물 시트·관계·세계관·타임라인·복선 원장)를 계획에서 시드하고 챕터마다 대조·갱신. 모순(❌)·미회수 복선(⚠️)·새 정전(🆕) 판정, `continuity_log.md` 기록. 연속성 모순은 저술가 재량으로 덮지 않음(에스컬레이션). editor의 narrative 통합 검수를 story_bible 대조 + 복선 마감 점검으로 확장. 병렬 저술 풀 1~2 축소. writer-memory는 선택적 보조로만(의존 없음, self-contained). | continuity-keeper, continuity-check, orchestrator, chapter-writer, editor, profiles/narrative, VERSION, CLAUDE.md, README, harness-roadmap | 소설의 가장 흔한 실패(설정·복선·타임라인 모순)를 일급 역할로 분리 — 로드맵 4트랙 모두 완료 (minor, breaking 없음 — narrative만 활성) |
| 2026-05-31 | **1.8.0** | **하네스 품질·신뢰성 일괄 개선** — (1) EPUB 기본 타이포그래피(epub.css superset)·epubcheck 게이트·식별자 민팅/보존·슬러그 강건화·표지 alt·다크모드/CJK 폰트; (2) AI-slop 제거(오프닝 메뉴·tic 밴드/상한·통권 변주 점검); (3) 신뢰성(자기탐지 의심 인용 하드블록·단일 append 로그·research/* 보존·마커 종료 기준); (4) 신규 Phase 4.5 통권 수락 게이트(manuscript-reviewer + manuscript-acceptance, 신선 컨텍스트); (5) drift 정리(Phase 7-2 → 재실행 매트릭스·README/콜로폰 URL·명명 규칙·model 라우팅). 선택적 mermaid 그림 파이프라인·학습 루프 추가. | 전체 하네스 | 7각도 분석으로 발견한 책 품질·신뢰성·정합성 결함 일괄 보정 (minor, breaking 없음 — 기본값 동작 보존) |
| 2026-07-11 | **1.9.0** | **운영자 학습 루프** — 인간의 학습 환경을 하네스 설계 요소로 편입 (출처: Toby/AI, "에이전트의 실행 환경만이 아니라, 개발자의 학습 환경도 설계 대상이다"). 세 겹: (1) 흐름 안 — Phase 3 **선판단 후공개**(계획 공개 직전 운영자 예상 스케치 초대, 갈라진 지점 명시) + `02_plan.md` **"설계 근거" 섹션 의무화**(기각 대안 ≥2 + 사유) + 완료 보고 설명 가능성 자문; (2) 흐름 밖 — 완료 보고에 **로그 기반 직접 검수 표적** 제안(factcheck ⚠️/🕒 밀집 챕터·style 최다 왕복 챕터·acceptance 아슬 기준, production 1개/learning 3개); (3) 메타 — Phase 0 **위임 다이얼** `delegation_mode: production\|learning`(매니페스트 기록, learning이면 Phase 3 초대 승격 + 첫 챕터 직접 읽기 권유). 전 터치포인트 자문 전용·비블로킹, 질문은 기존 상호작용 지점 편승만. 정전 스펙 `docs/learning-loop.md` 신설. | orchestrator, book-planner, book-planning, editor, book-editing, docs/learning-loop.md, VERSION, CLAUDE.md, README | 하네스의 최종 품질 게이트인 운영자 판단력이 완전 위임 기본값으로 마모되는 설계 결함 보정 (minor, breaking 없음 — production 기본값은 현행 동작 보존) |
| 2026-07-12 | **1.9.1** | **하네스 정합성 감사 drift 보정** — (1) 오케스트레이터 Phase 1 계약 정비: 입력에 `genre`·슬러그 명시(리서처의 장르별 소스 세트 선택이 실제로 작동하도록), 산출물에 `research/*.md` 보존 명시, research-lead에 `genre` 수신·리서처 전파 추가; (2) Phase 4 산출물·Phase 4.5 입력에 `length_report.md`·`book_manifest.json` 명시; (3) 사실·연속성 판정 구속력을 저술가·편집자 측에도 명문화 — chapter-writer·editor에 "스타일 3회 왕복 후 저술가 최종본 채택" 규칙이 fact/continuity ❌·🕒 판정에는 적용되지 않음(에스컬레이션)을 추가; (4) book-planner에 팀 통신 프로토콜(plan-reviewer 왕복) 추가; (5) 변경 이력 시간순 재정렬; (6) 구버전(v1.2.0 시점) Codex 미러(AGENTS.md·.codex/agents·.agents/skills) 현행 스펙으로 재생성. | orchestrator, research-lead, chapter-writer, editor, book-planner, CLAUDE.md, VERSION, README, AGENTS.md, .codex/, .agents/ | 하네스 감사(오케스트레이터·에이전트·프로필/빌드 3각 대조)에서 발견한 스펙-구현 drift 보정 (patch, breaking 없음 — 기존 의도의 명문화) |
