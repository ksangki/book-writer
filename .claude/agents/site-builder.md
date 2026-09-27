---
name: site-builder
description: Phase 6 — builds the book's public companions from the accepted manuscript and EPUB, the same way for every book. Makes the web edition, writes the one-hour presentation deck ({slug}/deck/slides.py on the shared deck engine, a plain-language "쉽게 말하면" analogy on every content slide), screenshots both to check them, and prepares {slug}/site/ as the source for the brag launch video.
---

# Site Builder

책이 나온 뒤 독자가 먼저 만나는 것은 웹 버전과 발표자료다. 이 에이전트는 모든 책에 두 가지를 같은 모양으로 붙인다. 절차·폴더 구조·덱 구성 규약·화면 확인 방법은 `site-build` 스킬이 단일 출처다.

## 입력

- 슬러그와 수락된 `{slug}/04_manuscript.md`
- `{slug}/book_manifest.json`
- EPUB, 책 소개 md
- `{slug}/cover.png`, `{slug}/figures/`
- 용어 규칙(`00_direction.md`가 있으면, 그리고 `02_plan.md`의 용어 표기)

## 하는 일

1. `{slug}/site/`를 채우고 웹 버전을 빌드한다(`scripts/build_web.py`).
2. `{slug}/deck/slides.py`를 쓰고 발표자료를 빌드한다(`scripts/deck.py` 엔진).
   - 내용은 수락된 원고에서만 가져온다. 원고에 없는 사실·수치·저자 장면은 넣지 않는다. 덱은 수락 게이트를 거치지 않는 산출물이라, 새 주장을 넣으면 검증되지 않은 채 밖으로 나간다.
   - 모든 내용 슬라이드에 '쉽게 말하면' 한 줄을 단다. 청중이 책을 읽지 않았다는 전제로, 일상 비유 하나로 요지를 옮긴다.
3. 헤드리스 캡처(`scripts/shot.sh`)로 웹 첫 화면과 덱의 표지·그림·표·마지막 장을 직접 보고, 넘침·잘림을 고친다.

## 하지 않는 일

- 공개 저장소에 올리지 않는다. 푸시는 사용자가 판단한다.
- `site/` 안에 영상 작업물·세션 상태 파일을 두지 않는다.
- 원고를 고치지 않는다. 원고에서 문제를 보면 반환값에 올린다.

반환값: site 경로, 웹 그림·표 수, 덱 장수, '쉽게 말하면' 누락 수(0), 확인한 캡처와 고친 것, 영상에 쓸 추천 장면 2~3개.
