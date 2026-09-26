---
name: fact-check
description: Verify concrete factual claims in a chapter draft — numbers, statistics, benchmarks, quotes, version numbers, release years, API signatures, superlatives, citations (tech-book), and safety/health/legal claims like food-safety temperatures, storage limits, allergens, local regulations (practical) — against the reference document, resolve "(사실 확인 필요)" markers, and apply the corrections. Use when checking a chapter for factual accuracy, validating version/API claims in fast-moving tech content, verifying safety facts in practical guides, or resolving fact-check annotations. Triggers on "팩트체크", "사실 확인", "fact check", "출처 검증", "버전 맞는지 확인", "안전 사실 확인".
---

# Fact Check

원고의 구체적 사실 주장을 검증하고 정정한다. 문체가 아니라 정확성만 본다. 범위는 장르가 정한다 — `tech-book`은 구체 주장 전반(빠르게 변하는 기술일수록 시점 명기와 출처 대조가 핵심), `practical`은 안전·건강·법규 사실만(틀리면 독자가 다친다). 다른 장르에서는 이 단계가 없다.

## 검증 대상

구체적이고 확인 가능한 주장만 본다. 의견·비유·일반 서술은 대상이 아니다.

**tech-book — 구체 주장 전반:**

| 유형 | 예시 |
|------|------|
| 수치·통계·벤치마크 | "응답이 3배 빨라진다", "메모리 40% 절감" |
| 인용·귀속 | "Dijkstra가 말했듯이", "공식 문서에 따르면" |
| 버전 번호 | "React 18", "Python 3.12" |
| 릴리스 연도·시점 | "2023년에 도입된", "최신 버전에서는" |
| API·시그니처 | 함수명·플래그·옵션명·기본값 |
| 단정 | "최초의", "유일한", "가장 빠른" |
| 참고문헌 식별자·등급 | DOI·arXiv ID·URL, 항목별 확인 등급 라벨 |

**practical — 안전·건강·법규 사실만:**

| 유형 | 예시 |
|------|------|
| 식품 안전 수치 | 조리 심부 온도("닭고기 75℃"), 보관 기간, 해동 규칙 |
| 알레르겐·독성 | 익혀야 하는 재료, 교차 오염, 알레르기 유발 표시 |
| 응급·부상 대처 | 화상·베임 등 사고 시 대처 서술 |
| 여행 법규·안전 | 비자·통관 규정, 현지 법, 안전 수칙 |
| 안전 단정 | "~해도 안전하다", "괜찮다"류 단정 |

맛·취향·팁·모호한 분량은 대상이 아니다. 안전 경고가 있는지·어디 있는지는 문체 체크리스트 소관이고, 여기서는 그 값이 맞는지를 본다. 안전 주장은 레퍼런스로 확정되지 않으면 모두 웹으로 확인하며, 공공 보건·식품 안전 기관(식약처·FDA·USDA 등)과 정부 여행 안전 공지를 1차 출처로 삼는다.

`(사실 확인 필요)` 주석이 달린 지점을 먼저 본다.

## 판정과 처리

| 라벨 | 의미 | 원고에 반영할 것 |
|------|------|-----------------|
| ✅ 확인됨 | 레퍼런스와 일치 | 그대로 둔다 |
| ❌ 정정 | 레퍼런스와 불일치 | 맞는 값·표현으로 고친다 |
| ⚠️ 출처 없음 | 근거를 찾지 못함 | 약화("더 빠르다")하거나 삭제한다 |
| 🕒 신선도 | 시점 미명기·곧 바뀔 내용 | "{버전}/{연도} 기준" 또는 휘발성 문구를 붙인다 |

대조 순서: `01_reference.md`와 `research/*.md`로 먼저 판정한다. 거기서 판정할 수 없는 핵심 주장, 그리고 의심스러운 식별자(형식이 이상하거나 빌드 날짜보다 미래 YYMM인 arXiv ID, 열리지 않는 DOI·URL, 출처가 한 곳뿐이고 확인되지 않는 인용)는 WebSearch·WebFetch로 공식 문서·1차 출처를 확인한다. 확인되지 않은 의심 식별자는 ✅가 될 수 없다 — 원고에서 빼거나 출처 없는 일반 서술로 바꾼다.

정정은 원고의 voice를 유지하는 최소 수정으로 한다. 약화·삭제로도 처리할 수 없는 경우(그 주장이 장의 논지를 떠받치고 있어서 빼면 장이 무너지는 경우)만 `미해소`로 남기고 보고한다.

## 로그 (`{slug}/factcheck_log.md`)

로그는 단일 파일이다. 장마다 판정이 끝나는 즉시 섹션을 append한다 — 중단돼도 끝낸 판정이 남는다.

```markdown
## {NN}장 (라운드 {N})

### ❌ 정정
- "React 18에서 도입된 Server Actions" → "React 19에서 안정화된 Server Actions" — 근거: research/web.md 자료 4 (공식 릴리스 노트)
### ⚠️ 약화·삭제
- "이 방식이 3배 빠르다" → "더 빠르다" — 레퍼런스에 근거 없음
### 🕒 신선도
- "최신 버전에서는" → "PostgreSQL 16 기준으로는"
### ✅ 확인 (요약)
- 수치 4건, 버전 3건 — research/web.md·papers.md와 일치
### 미해소
- (없음)
```

## 통합 원고 재확인 (수락 게이트가 되돌렸을 때)

`05_acceptance.md`가 지목한 항목만 본다 — 대개 장 간 사실 충돌(같은 수치·버전을 장마다 다르게 씀)이나 참고문헌 항목의 등급 라벨·식별자가 `research/*.md` 원장과 어긋난 경우다. 수정은 `04_manuscript.md`와 해당 `{NN}_final.md`에 함께 반영하고, 로그에 `## 통합 원고` 섹션으로 남긴다.
