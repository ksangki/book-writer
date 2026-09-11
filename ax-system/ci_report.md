# Manuscript CI 결과 — 「거두는 체계」 v1.0.0

- 실행: 2026-09-11, manuscript-ci (로컬 src, PYTHONPATH 실행)
- 대상: `거두는-체계-v1.0.0.epub` (check-build) / `04_manuscript.md` (check)

## check-build (빌드 산출물 게이트) — ✅ PASS

```
No build findings.
```

epub-responsive-img · epub-image-missing · svg-stretched-corner 등 독자 단 렌더 결함 **0건**.

## check (정적 프로즈 린트) — 자문 133건, 차단 0건 판정

| 규칙 | 건수 | 판정 |
|---|---|---|
| `strong-claim-word` (항상·반드시·전부·모두·유일한 등) | 127 | **자문 — 조치 없음.** 일반 단어 목록 린트. 이 원고의 단정 표현은 Phase 4 fact-checker가 약 200건 주장 검증(출처 라벨·완충 규율 R0-1·R0-12)에서 개별 심사했고, 잔존 사용처의 다수는 워크시트의 절차 명령형("반드시 확인하라")이다. Phase 4.5 라운드 2 ACCEPT 상태의 텍스트를 단어 목록 기준으로 재수정하지 않는다 |
| `duplicate-within-file` | 6 | **의도된 설계 — 조치 없음.** 전건이 본문 장 도구(판별 프레임·스키마 표·신뢰도 등급·사용 제한 선언 등)를 **부록 A 워크시트 모음에 재수록**한 것이다. 부록 A의 존재 이유가 그 재수록이다 (계획서 명세) |

## 종합

**게이트 통과.** 차단 결함 0건 — 발행 진행.
