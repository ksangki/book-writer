---
name: manuscript-acceptance
description: Whole-book acceptance gate run by a fresh-context reviewer before EPUB build (Phase 4.5). Cross-reads the integrated manuscript against the plan, research ledger, and logs, scans for forbidden leftover markers, checks terminology/voice/variation, cross-reference and promise integrity, and emits {slug}/05_acceptance.md with per-criterion PASS/BLOCK + owner-tagged fixes. Genre-agnostic; complements the per-chapter fact/continuity passes. Triggers on "수락 검수", "통권 검수", "manuscript acceptance", "최종 통과 게이트".
---

# Manuscript Acceptance

통합 원고(`04_manuscript.md`)가 Phase 5로 넘어가기 전 책 전체를 판정하는 게이트다. 원고를 만든 editor와 다른 새 컨텍스트가 수행한다. 챕터 단위 사실·연속성 패스를 다시 하지 않고, 잔여 미결과 통권 단위 문제만 본다. 기본 흐름에는 별도 스타일 검수가 없으므로 voice 이탈도 여기서 잡는다.

없는 로그가 대상인 기준(예: essay의 사실 로그)은 N/A PASS로 두고 이유를 한 줄 적는다.

교정 패스(Phase 4.4)의 `proofread_log.md`·`ci_report.md`가 있으면 함께 읽는다. 교정 패스가 사실이나 저자 장면을 바꾼 흔적이 있는지, 보류로 남긴 항목이 판정에 영향을 주는지 본다. 교정 패스를 건너뛰었다면 그 이유가 로그에 있는지 확인한다.

## 수락 기준

| ID | 기준 | 확인 방법 | BLOCK 시 담당 |
|----|------|----------|--------------|
| (a) | 챕터 완비·분량 균형 | 플랜의 챕터 목록 ↔ 원고 `# N장` 헤딩 1:1 대조. `length_report.py`로 분량을 직접 재고 70% 미만·150% 초과 장을 본다 | 해당 장 `chapter-writer` |
| (b) | 미해소 마커 0건 | 아래 grep | 사용자 (빌드 중단) |
| (c) | 사실 미결 해소 | `factcheck_log.md`의 `미해소`. (tech-book) 참고문헌 항목의 식별자·확인 등급 라벨을 `research/*.md`와 표본 대조하고, 같은 수치·버전이 장마다 다르게 쓰였는지 본다 | `fact-checker` / 해결 불가면 사용자 (빌드 중단) |
| (d) | 용어·voice·변주 | 핵심 용어 표기 흔들림. 여러 장을 표본으로 활성 `style-checklist.md`에 비춰 voice 이탈(번역투, 강압 어조, 과포화 말버릇, 메타 선언 오프닝)을 본다. `editor_notes.md`의 변주 표를 참고해 오프닝·클로징이 같은 틀로 반복되는지 본다 | 해당 장 `chapter-writer` 또는 `editor` |
| (e) | 상호 참조 무결성 | "앞서 N장에서 ~" 류 콜백이 실제로 그 장의 내용을 가리키는지 | `editor` |
| (f) | 약속 이행 | 매니페스트 `description`과 계획의 독자 여정이 약속한 범위를 원고가 다루는지 | `editor`, 본질적 미달이면 사용자 |
| (g) | 부속 자료 완비 | 서문·목차·콜로폰(`## 판권`)·에필로그·(tech-book/essay) 참고문헌 | `editor` |
| (i) | 그림·표 무결성 | 계획에 그림·표 배정이 없으면 N/A PASS. 있으면: `figures/fig-*.svg` 참조가 모두 실재하는지, 그림·표 번호가 장 안에서 나오는 순서대로 이어지는지, 계획에 배정된 그림·표가 들어갔는지, 그림 라벨이 원고가 말한 사실·저자 경험의 범위를 넘지 않는지, 남은 `<!-- 그림 … -->` 자리 표시가 없는지 | `figure-designer` 또는 `editor` |
| (h) | 연속성 (narrative) | `continuity_log.md`의 `미해소`, `story_bible.md` 복선 원장의 미회수 항목 | `chapter-writer` / 의도 확인은 사용자 |

## 절차

1. 금지 마커를 grep한다. 한 건이라도 있으면 (b) BLOCK이며 줄 번호와 원문을 기록한다.
   ```bash
   grep -nE "\(사실 확인 필요\)|\[리서치 공백\]|\[미완성\]" {slug}/04_manuscript.md
   ```
2. 챕터 완비와 분량을 확인한다.
   ```bash
   grep -nE "^# [0-9]+장" {slug}/04_manuscript.md
   python3 .claude/skills/book-editing/scripts/length_report.py {slug}
   ```
3. 콜백을 모아 가리키는 장이 맞는지 본다.
   ```bash
   grep -nE "앞서 [0-9]+장|[0-9]+장에서 (다룬|살펴본|본)" {slug}/04_manuscript.md
   ```
4. 로그의 잔여 미결을 본다.
   ```bash
   grep -nE "미해소" {slug}/factcheck_log.md {slug}/continuity_log.md 2>/dev/null
   ```
5. (c)의 참고문헌 표본 대조, (d)의 voice·변주, (f)(g)를 판정한다. 말버릇 반복 횟수는 grep으로 센다.
6. `05_acceptance.md`를 쓴다.

## 평결

- **ACCEPT** — 모든 기준 PASS.
- **BLOCK** — 하나 이상 BLOCK. 오케스트레이터가 조치를 담당자에게 한 번 보내고, 영향받은 기준만 재판정한다. 재판정 후에도 BLOCK이면 사용자가 판단한다.
- (b)(c)는 사용자가 명시적으로 승인하지 않는 한 PASS가 될 수 없다. 승인했으면 그 사실과 범위를 기록한다.

## 출력 형식

```markdown
# 수락 검수: {책 제목}

<!-- 검수: {날짜} · 라운드 {N} · manuscript-reviewer (fresh context) -->

## 기준 판정

| ID | 기준 | 판정 | 근거 |
|----|------|------|------|
| (a) | 챕터 완비·분량 균형 | PASS | 플랜 8장 = 원고 8장, 플래그 0 |
| (b) | 미해소 마커 0건 | PASS | grep 0건 |
| (c) | 사실 미결 해소 | PASS | 미해소 0건, 참고문헌 표본 6건 원장 일치 |
| (d) | 용어·voice·변주 | BLOCK | 4·5·6장 모두 '상황 가정' 오프닝, 6장 "기억해두자" 11회 |
| (e) | 상호 참조 무결성 | PASS | 콜백 6건 정합 |
| (f) | 약속 이행 | PASS | ... |
| (g) | 부속 자료 완비 | PASS | ... |
| (h) | 연속성 | N/A | tech-book |

## 평결

BLOCK

## 조치

| 기준 | 심각도 | 담당 | 조치 |
|------|--------|------|------|
| (d) | 중간 | chapter-writer 5장 | 오프닝을 '실패 장면'으로 교체 (계획 배정과 일치시킴) |
| (d) | 낮음 | chapter-writer 6장 | "기억해두자" 11회 → 4회 이하로, 나머지는 평어체 |
```

재검수면 새 라운드를 append하고, 이전 조치의 해소 여부를 먼저 적은 뒤 영향받은 기준만 다시 판정한다.
