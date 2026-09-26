---
name: continuity-check
description: Maintain a story bible and check narrative chapter drafts for continuity — character facts (appearance, voice, motive), relationships, world rules, timeline, and planted setups (복선). Seeds {slug}/story_bible.md from the plan, flags contradictions, and tracks setup→payoff. Also measures per-chapter tension/emotion and scene-level pacing (advisory {slug}/pacing_report.md). Use when keeping a novel consistent across chapters, building a story bible, validating character voice, tracking 복선, or reviewing pacing/emotion curve. Triggers on "연속성 확인", "스토리 바이블", "복선 추적", "캐릭터 일관성", "continuity check", "story bible", "페이싱 분석", "감정 곡선".
---

# Continuity Check

소설·서사물을 챕터를 건너뛰며 일관되게 유지한다. 인물·관계·세계관·타임라인·복선을 `story_bible.md`라는 단일 정전(canon)으로 잡고, 각 챕터를 그에 대조한다. 문체가 아니라 **연속성**만 본다.

> **narrative 장르 전용.** `genre`(오케스트레이터 → `{slug}/book_manifest.json`)가 narrative가 아니면 오케스트레이터가 이 단계를 생략한다.

## 절차

1. `story_bible.md`가 없으면 `02_plan.md`에서 인물·설정·타임라인·복선을 뽑아 시드한다 (부족하면 1장에서 캐논을 추출).
2. 장 원고에서 연속성에 걸리는 항목을 모아 bible과 대조한다 — 인물 외모·나이, 대사톤·말투, 관계 상태, 세계관 규칙, 시점·날짜, 고유명사 철자, 복선 심기·회수.
3. 모순은 해당 문장을 최소한으로 고쳐 반영한다. 서사상 의도일 수 있는 충돌은 고치지 않고 `미해소`로 남긴다.
4. 새 정전을 bible에 반영하고 복선 원장의 상태를 갱신한다.
5. 판정과 계측 한 줄(`계측: 긴장도 {1~5} · 지배 감정 {단어} · 씬 {N}개 · 아크 위치 {설정/상승/절정/하강}`)을 `continuity_log.md`에 장별 섹션으로 즉시 append한다.
6. 마지막 장을 마치면 `pacing_report.md`를 만든다 (아래).

## 무엇을 검증하나

| 유형 | 모순 예시 |
|------|----------|
| 인물 고정 사실 | 눈/머리 색, 나이, 키, 흉터 — 챕터마다 다름 |
| 대사톤·말투 | 1장 반말 캐릭터가 5장에서 존댓말 (의도 없이) |
| 관계 상태 | 아직 안 만난 두 인물이 구면처럼 행동 |
| 생사·소재 | 죽은 인물 재등장, 멀리 있던 인물이 갑자기 등장 |
| 세계관 규칙 | 1장에서 "마법은 밤에만"인데 3장에서 낮에 사용 |
| 타임라인 | 사건 순서 역행, 요일·계절 모순 |
| 고유명사 | 지명·인명 철자가 장마다 다름 |
| 복선 | 심은 떡밥(🌱)이 회수(🎯) 안 됨 / 회수가 심기보다 먼저 |

## 판정 라벨

- ❌ **모순** — bible과 충돌. 원고를 정정한다
- ⚠️ **미회수 복선** — 심은 복선이 아직 안 풀림. 의도면 OK, 잊었으면 표시
- 🆕 **새 정전** — 챕터가 도입한 새 인물·설정. bible에 추가
- ✅ **일관됨** — 캐논과 일치 (간단 확인)

## story_bible.md 템플릿

```markdown
# 스토리 바이블: {제목}
<!-- 갱신: {날짜} {요약} -->

## 인물
### {이름}
- 외모·나이: {고정 사실}
- 감정 궤도: {체념 → 욕망 자각 → 선택}
- 태도·성격:
- 대사톤·말투: {담백/직설/회피, 반말/존댓말/혼합}
- 핵심 단어·말버릇:
- 동기·비밀: {공개 시점}
- 첫 등장: {N장}

## 관계
- {A} ↔ {B}: {유형} — 변화: {N장에서 ~}

## 세계관·설정
- 시대·장소:
- 규칙·제약:
- 명칭 정전: {철자 고정}

## 타임라인
- {시점} — {사건} ({N장})

## 복선 원장
- 🌱 {N장}: {복선} → 🎯 {M장} 회수 예정/회수됨
```

## 로그 형식 (`continuity_log.md`)

```markdown
## {NN}장 (라운드 {N})

### ❌ 모순 → 정정
- "지수의 파란 눈이 빛났다" → "지수의 갈색 눈이…" — 근거: story_bible 인물>지수 (1장)

### ⚠️ 미회수 복선
- 3장 "낡은 회중시계" 아직 미회수 — 의도 확인 필요

### 🆕 새 정전 (bible 반영)
- 새 인물 "노인" — 인물 시트 추가

### 미해소
- (없음)
```

## 작업 원칙

- 연속성만 본다. 문체·플롯 평가는 하지 않는다.
- 먼저 정한 설정이 정전이다. 의도적 변경이 확인되면 bible을 갱신한다.
- 복선은 원장에서 심기→회수까지 닫는다. 마지막 장에서 미회수 목록을 보고한다.

## 페이싱 리포트 (`{slug}/pacing_report.md`, 자문 전용)

장별 계측을 모아 통권 리포트로 만든다. 판정이 아니라 editor의 참고 자료이며, 이 리포트로 BLOCK하지 않는다. 값은 `{NN}_final.md`를 직접 세어 얻는다.

````markdown
# 페이싱 리포트: {제목}

## 감정 곡선 (긴장도 1~5)

```mermaid
xychart-beta
  title "긴장도 곡선"
  x-axis [1장, 2장, 3장]
  y-axis "긴장도" 1 --> 5
  line [2, 3, 4]
```

| 장 | 긴장도 | 지배 감정 | 아크 위치 |
|----|--------|----------|----------|

## 씬 단위 페이싱

| 장 | 씬 수 | 씬당 평균 자수 | 대사 비중(추정) | 플래그 |
|----|-------|---------------|----------------|--------|

## 관찰 (플래그만)
- {예: 4~6장 긴장도가 3으로 평탄 — 2막 중간점이 곡선에 안 보임}
- {예: 7장 씬 2가 8,000자 — 앞뒤 씬(2,000자대) 대비 돌출}
````

mermaid 곡선은 내부 검토용이라 렌더 환경이 없어도 된다.
