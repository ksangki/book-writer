# 하네스 로드맵 — 장르 확장 후속 작업

장르 추상화(P1, harness v1.3.0)에서 의도적으로 범위 밖으로 둔 항목들의 백로그다. P1은 "장르별 프로필로 voice·스캐폴드·체크리스트·리서치 소스를 갈아끼우는" 골격을 만든다. 아래는 그 골격 위에서 각 장르의 품질을 끌어올리는 후속 트랙이다.

| 트랙 | 제목 | 의존 | 상태 |
|------|------|------|------|
| P2 | 최신 기술서: 전용 fact-checker | P1 tech-book 프로필 | ✅ 완료 (하네스 v1.4.0) |
| P3 | 실용서: 구조화 데이터 EPUB 템플릿 | P1 practical 프로필 | ✅ 완료 (하네스 v1.5.0) |
| P4 | 소설: 캐릭터·플롯 연속성 추적 | P1 narrative 프로필 | ✅ 완료 (하네스 v1.7.0) |
| P2-ext | 실용서 안전·식품 사실 검증 (fact-checker 확대) | P2 | ✅ 완료 (하네스 v1.11.0) |
| P3-ext | 이미지 임베드 파이프라인 + 영양표·환산표 partial | P3 | ✅ 완료 (하네스 v1.11.0) |
| P4-ext | 감정 곡선 시각화 + 씬 단위 페이싱 분석 | P4 | ✅ 완료 (하네스 v1.11.0) |

---

## P2 — 최신 기술서: 전용 fact-checker ✅ 완료 (v1.4.0)

**왜:** P1은 tech-book 프로필의 `style-checklist.md`에 사실/버전 점검 항목을 넣는 선에서 멈췄다. 즉 style-guardian이 부차적으로 사실을 살폈다. 최신 기술서는 수치·API·버전·릴리스 연도가 6개월이면 낡고, 틀리면 책 신뢰를 통째로 깎는다. 사실 검증을 일급 역할로 분리했다.

**한 일:**
- ✅ `fact-checker` 에이전트 + `fact-check` 스킬 신설 — style 합의 후, 구체 주장(수치·인용·버전·연도·API·단정)을 레퍼런스 대조로 판정(✅확인/❌정정/⚠️출처없음/🕒신선도). `{slug}/factcheck_log.md` 기록.
- ✅ chapter-writer의 `(사실 확인 필요)` 주석을 fact-checker가 소비·해소하는 프로토콜. final에 미해소 주석 금지.
- ✅ 리서치 신선도 메타: web-researcher/paper-researcher/research-lead가 발행일·"{버전}/{연도} 기준"·"검색 시점" 라벨 기록.
- ✅ Phase 4 팀에 fact-checker를 tech-book일 때만 합류시키는 옵션 멤버로 배선. 사실 오류는 저술가 재량으로 덮지 않음(style 이견과 다른 에스컬레이션).

**구현된 비용 통제:** 1차 레퍼런스 대조 → Critical 주장만 2차 웹 에스컬레이션(WebSearch/WebFetch) → 확정 불가 시 주장 약화/삭제 권고. 장르 ≠ tech-book이면 단계 자체를 생략.

**남은 확장:** ✅ P2-ext로 완료 (v1.11.0) — 아래 참조.

---

## P3 — 실용서: 구조화 데이터 EPUB 템플릿 ✅ 완료 (v1.5.0)

**왜:** 요리·여행 실용서는 산문보다 구조화 블록(재료·분량·조리 단계·일정표·준비물 체크리스트)이 핵심이다. P1 practical 프로필의 scaffolds가 구조를 글로 안내했지만, EPUB 빌드는 이를 일반 markdown으로만 처리했다.

**한 일:**
- ✅ 번들 스타일시트 `.claude/skills/epub-build/styles/epub.css` — 메타 박스·재료·단계·팁/주의 콜아웃·여행 일정표·체크리스트 블록 스타일. 특정 클래스만 스타일하므로 전 장르 안전 적용.
- ✅ `build_epub.sh`가 스크립트 상대 경로로 CSS를 자동 임베드(`--css`), 빌드 로그에 기록.
- ✅ practical scaffolds·voice에 fenced div 규약 정의: `::: meta` / `::: ingredients` / `::: steps` / `::: tip` / `::: warning` / `::: itinerary` + 태스크 체크리스트.
- ✅ 요리(분량·시간·난이도 메타)·여행(일정표) 구조 커버.

**범위 밖:** ✅ P3-ext로 완료 (v1.11.0) — 아래 참조.

---

## P4 — 소설: 캐릭터·플롯 연속성 추적 ✅ 완료 (v1.7.0)

**왜:** P1 narrative 프로필은 씬·시퀀스·캐릭터아크 스캐폴드를 제공했지만, 여러 챕터를 쓸 때 캐릭터 설정·복선·타임라인이 어긋나는 게 소설의 핵심 실패 지점이다. 기술서의 "용어 일관성"보다 훨씬 무겁다.

**한 일:**
- ✅ `continuity-keeper` 에이전트 + `continuity-check` 스킬 신설 (narrative 전용 Phase 4 멤버, fact-checker의 소설판).
- ✅ 연속성 추적 아티팩트 `{slug}/story_bible.md` — 인물 시트(외모·감정궤도·대사톤·동기)·관계·세계관 규칙·타임라인·복선 원장. Phase 4 시작 전 계획에서 시드, 챕터마다 새 캐논 누적.
- ✅ 각 챕터 초안을 bible 대조로 검수(❌모순/⚠️미회수 복선/🆕새 정전/✅일관)하고 `continuity_log.md` 기록. 모순은 저술가 재량으로 덮지 않음(에스컬레이션).
- ✅ editor의 narrative 일관성 점검을 story_bible 대조 + 미회수 복선 마감 점검으로 확장.
- ✅ 병렬 저술 시 풀 크기 1~2 축소·순차 우선(P1에서 명시, P4에서 keeper 전제로 강화).
- `oh-my-claudecode:writer-memory`는 **선택적 보조**로만 언급 — 하네스는 그것에 의존하지 않고 `story_bible.md`가 단일 출처(self-contained).

**범위 밖:** ✅ P4-ext로 완료 (v1.11.0) — 아래 참조.

---

## 후속 확장 3트랙 ✅ 완료 (v1.11.0)

P2~P4가 각각 남겨둔 후속 후보를 한 릴리스로 반영했다.

### P2-ext — 실용서 안전·식품 사실 검증

- ✅ fact-checker 활성 장르를 `tech-book` + `practical`로 확대. practical은 **안전·건강·법규 사실 한정** — 식품 안전(조리 심부 온도·보관 기간·해동), 알레르겐·독성 재료, 응급 대처, 여행 법규·비자·안전 수칙, "안전하다" 단정.
- ✅ practical의 안전 주장은 **기본 Critical** — 레퍼런스 확정 불가 시 웹 2차 대상, 1차 출처는 공공 보건·식품 안전 기관(식약처·FDA·USDA)·정부 여행 공지 우선.
- ✅ style-guardian과 분업 명문화 (practical style-checklist): guardian은 경고의 존재·위치·형식, fact-checker는 값의 진위.
- ✅ 오케스트레이터 Phase 4 팀 배선·chapter-writer 통신 프로토콜·editor 입력에 반영. `factcheck_log.md`는 tech-book·practical 공용.

### P3-ext — 이미지 임베드 파이프라인 + 영양표·환산표 partial

- ✅ `build_epub.sh` **이미지 pre-flight**: 본문(mermaid 치환 결과 포함)이 참조하는 로컬 이미지의 실재를 pandoc 전에 일괄 검증, 누락은 stderr WARNING + 빌드 로그 `images:` 줄 기록. epub-builder 필수 확인 항목화 (pandoc은 누락 이미지를 조용히 빼고 빌드하므로).
- ✅ **puppeteer 브라우저 자동 탐지**: `PUPPETEER_EXECUTABLE_PATH` 미설정 시 Chrome/Chromium/Edge 표준 경로를 스크립트가 자동 탐지 (v1.10.0 스펙이 광고했으나 스크립트에 없던 drift 해소).
- ✅ 이미지 소싱 규칙 (practical scaffolds): 사용자 제공 우선 → 생성/mermaid 대체 → **라이선스 불명 웹 이미지 임베드 금지** → 미준비 이미지는 `[이미지 예정: {설명}]` 마커.
- ✅ `epub.css`에 `::: nutrition`(영양표)·`::: conversion`(환산표) 블록 클래스 + 구조화 블록 다크 모드 대비 보정.
- ✅ 재사용 partial `profiles/practical/partials/conversion-tables.md` — 부피·무게·오븐 온도 표준 환산표 (요리 계열 부록에 복사) + 영양표 템플릿 (값은 책별, 출처 의무).

### P4-ext — 감정 곡선 시각화 + 씬 단위 페이싱 분석

- ✅ continuity-keeper에 **계측 역할** 추가 (자문 전용·비블로킹): 챕터 검수 마감마다 `continuity_log.md`에 긴장도(1~5)·지배 감정·씬 수·아크 위치 한 줄 기록.
- ✅ 통합 대조 시 `{slug}/pacing_report.md` 산출 — 감정 곡선(mermaid `xychart-beta` + 표), 씬 단위 페이싱 표(씬 수·씬당 자수·대사 비중·돌출/요약 구간 플래그), 관찰 노트.
- ✅ 역할 경계 유지: 계측은 판정이 아니다 — keeper는 수치·플래그만, 해석·수정 결정은 editor. 리포트는 BLOCK 사유가 아니며 저술 왕복을 만들지 않는다. 값은 `{NN}_final.md` 직접 계측 (기억·요약 금지).

**남은 후속 후보:** 지도·사진의 자동 생성 파이프라인 고도화(현재는 사용자 제공/생성 대체 규약), 페이싱 계측의 공용 계측기 스크립트화.

---

## 갱신 규칙

각 트랙 착수 시 이 문서의 상태 칼럼을 갱신하고, 완료 시 `CLAUDE.md` 변경 이력 테이블에 하네스 버전 행을 추가한다.
