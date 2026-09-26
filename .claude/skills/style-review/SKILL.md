---
name: style-review
description: Review chapter drafts against the active genre profile's style checklist (defaults to tech-book = Toby's voice) — detects voice deviations and applies or proposes concrete before/after rewrites. Use when reviewing a chapter for style consistency, enforcing the genre voice, or polishing prose.
---

# Style Review

챕터를 활성 장르 프로필의 문체 기준으로 점검하고 구체적 대체 문장으로 고친다. 기준은 `profiles/{genre}/style-checklist.md`와 `voice.md`다 (`genre`는 오케스트레이터 전달값 → `{slug}/book_manifest.json` → 기본 `tech-book`). 체크리스트 항목과 우선순위는 프로필에만 있다 — 여기에 복사하지 않는다.

## 점검 방식

- 빈도 항목은 하한이 아니라 범위로 본다. 부족함만큼 과포화(같은 말버릇이 한 장에 과다하거나 모든 장에 기계적으로 반복)도 결함이다. 반복 횟수는 grep으로 센다.
- 고칠 곳마다 원문을 인용하고, 대체 문장과 짧은 이유를 적는다. "청유형이 부족하다"가 아니라 "3.2절 두 번째 문단의 '~이다'를 '~해보자'로".
- 장당 5~10곳, 톤을 가장 크게 흔드는 곳부터. 저술가의 의도적 변주(리듬·강조)는 인정한다.
- 사실 주장·출처 단서의 내용은 바꾸지 않는다.

## 로그 형식 (`{slug}/style_log.md`)

```markdown
## {NN}장 (라운드 {N})

### Critical
1. [원문] "..." → [수정] "..." — 이유: {짧게}
### Should
1. ...
### Nice
1. ...

전체 톤: {한 줄 — "토비 목소리가 살아 있지만 2.3절 중반이 딱딱함" 등}
```

장마다 끝나는 즉시 append한다.

## 통합 원고 점검

`04_manuscript.md`를 대상으로 하면 장 경계의 톤 단절, 서문·에필로그와 본문의 어울림, 그리고 장별 오프닝·클로징·최다 말버릇 표로 통권 반복을 함께 본다. 결과는 `## 통합 원고` 섹션으로 같은 로그에 남긴다.
