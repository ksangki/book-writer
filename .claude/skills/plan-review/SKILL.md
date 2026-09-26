---
name: plan-review
description: Critically review a book plan against the reference document and audience fit. Check coverage, narrative flow, audience alignment, chapter balance, and redundancy. Use when reviewing a book outline, auditing a chapter structure, or giving structured feedback on a writing plan. Triggers on "계획 리뷰", "아웃라인 평가", "review the plan", "critique the outline".
---

# Plan Review

저술 계획을 다섯 축으로 비판하고, 구체적 수정 제안을 우선순위와 함께 돌려준다. 칭찬으로 채우지 않고, 근거 없는 취향 비판도 하지 않는다.

## 다섯 축

| 축 | 질문 | 빨간불 신호 |
|----|------|------------|
| 커버리지 | 주제의 핵심 쟁점 중 빠진 게 있는가? | 레퍼런스의 한 챕터 분량 내용이 한 단락으로 축소됨 |
| 내러티브 흐름 | 챕터 순서가 자연스러운가? | 난이도 급등·급감, 맥락 없는 주제 점프 |
| 독자 적합도 | 대상 독자 수준에 맞는가? | 입문자용인데 2장부터 고급 개념을 가정 |
| 챕터 균형 | 분량·밀도가 고른가? | 한 챕터가 다른 챕터의 3배 이상 |
| 중복·공백 | 같은 내용이 여러 장에 퍼져 있는가? | 인접 장의 주요 내용이 대부분 겹침 |

레퍼런스의 각 섹션이 계획의 어느 장에 매핑되는지부터 대조하면 커버리지와 중복이 빨리 보인다.

## 형식 (`{slug}/03_review_log.md`에 append)

```markdown
## 리뷰 라운드 {N}

### Critical (반드시 반영)
- [챕터 {NN}] 문제: {...}
  - 근거: {레퍼런스 섹션 또는 독자 관점}
  - 제안: {구체적 수정 방향}

### Should (반영 권장)
- ...

### Nice (여유 있으면)
- ...

### 전체 평
{한 단락 — 강점과 전반적 방향}
```
