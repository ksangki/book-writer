---
name: book-figures
description: Phase 4.2 — draws the book's figures as clean SVG diagrams (1–2 per chapter, assigned in the plan) with the shared figlib, inserts them into the chapter finals with a caption and a short reading sentence, numbers them in order of appearance, and screenshot-checks every one. Also checks that each chapter's assigned tables exist with "표 N-k." captions. Triggers on "그림 넣어", "도식", "figure", "표랑 그림", "다이어그램 다시".
---

# Book figures (그림 · 표)

사실 검증이 끝난 `chapters/{NN}_final.md`에 본문 그림을 넣는 단계다. 계획에 그림 배정이 있는 장만 대상이다. 장르별 기준은 `book-planning`의 그림·표 배정 표를 따른다. tech-book·practical은 필수, essay는 선택, narrative는 기본 없음이다. 배정이 하나도 없으면 이 단계 전체를 건너뛴다. 모든 책이 같은 모양의 그림을 갖게 한다. 형식은 SVG, 색은 표지와 같은 theme, 글꼴은 한글 산세리프다. 그림은 EPUB·웹·발표자료가 같은 파일을 함께 쓴다. mermaid는 EPUB 렌더가 불안정하고 모양을 제어하기 어려워 기본으로 쓰지 않는다. 원고에 mermaid 블록이 있으면 같은 내용의 SVG로 바꾼다.

## 입력

- `02_plan.md`의 장별 **그림·표 배정**. 그림마다 번호, 무엇을 보여 주는지, 어느 절 근처인지가 적혀 있다.
- `chapters/{NN}_final.md` 전부. 저술가가 남긴 자리 표시 `<!-- 그림 N-k -->`가 있으면 그 자리에 넣는다.
- `book_manifest.json`의 `theme.figures`(있으면)
- 용어 규칙(`02_plan.md` 용어 표기, `00_direction.md`가 있으면 그것도)

## 만드는 법

1. `.claude/skills/book-figures/scripts/figlib.py`와 `figures_template.py`를 `{slug}/figures/`에 복사한다. 템플릿은 `figures.py`로 이름을 바꿔 그림 함수를 채운다.
   - 흐름은 `chain`, 격자는 `grid`, 순환은 `cycle` 헬퍼를 쓴다.
   - 그 밖의 모양(연표·2축 사분면·자리 지도 등)은 `Fig`의 `box`·`arrow`·`line`·`dot`·`text`로 그린다.
2. 렌더: `BOOK_MANIFEST={slug}/book_manifest.json python3 {slug}/figures/figures.py` → `{slug}/figures/fig-N-k.svg`
3. 규칙
   - SVG 안에 그림 번호를 쓰지 않는다. 번호는 원고 캡션이 맡는다. 번호를 고칠 때 SVG를 다시 그리지 않아도 되게 하기 위해서다.
   - `<foreignObject>`를 쓰지 않는다. epubcheck가 XHTML 오류로 막는다. `<text>`/`<tspan>`만 쓴다.
   - 줄바꿈은 figlib의 `wrap()`에 맡긴다. 라벨에 `\n`을 넣지 않는다.
   - 그림 안의 사실(수치·회사명·연도·인용)은 그 장 원고에 이미 있는 것만 쓴다. 그림은 검증을 한 번 더 거치지 않는 경로라, 새 사실을 넣으면 확인되지 않은 채 책에 실린다.
   - 저자 경험을 다루는 라벨은 원고가 말한 범위를 넘지 않는다. 예를 들어 원고가 "위에서 시작했다"까지만 말했으면, 그림에 "아래로 이관" 같은 방향을 덧붙이지 않는다.
   - 용어 규칙과 금지어를 원고와 똑같이 지킨다.

## 원고에 넣기

- 넣는 위치: 그 구조를 설명하는 문단 바로 뒤, 또는 자리 표시 `<!-- 그림 N-k -->`를 바꿔서.
- 형식:

  ```markdown
  ![그림 N-k. 캡션 — 무엇을 보여 주는지 한 구절](figures/fig-N-k.svg)

  그림을 읽는 한두 문장. 본문 문체로, 그림의 어디를 먼저 보면 되는지.
  ```
- **번호는 장 안에서 나오는 순서대로** 1부터 매긴다. 계획의 배정 번호와 실제 위치가 다르면 위치를 따른다. 번호를 바꿨으면 `figures.py`의 등록 번호, SVG 파일명, 원고의 캡션과 참조를 함께 바꾼다.
- 기존 문장·사실은 바꾸지 않는다. 늘어나는 것은 이미지 줄과 읽는 문장뿐이다.

## 표 확인

그림을 넣으며 장마다 표도 확인한다.

- 계획에 배정된 표가 있는가.
- 표 바로 위 캡션이 `**표 N-k. 제목**` 형식인가. 번호는 장 안에서 나오는 순서다.
- 장 끝 `### 가져갈 도구:` 표도 캡션을 단다.

빠진 표는 만들지 않고, 장과 표 번호를 반환값에 올린다. 표 내용은 저술가가 정할 몫이다.

## 화면 확인

그림을 모두 찍어서 직접 본다.

```bash
for f in {slug}/figures/fig-*.svg; do .claude/skills/site-build/scripts/shot.sh "$f" "{slug}/figures/shots/$(basename "$f" .svg).png" 1000x640; done
```

- 볼 것: 글자가 상자를 넘치지 않는가, 화살표가 글자를 가리지 않는가, 빈 여백이 너무 크지 않은가(viewBox 높이를 내용에 맞춘다), 색이 표지와 맞는가.
- 캡처는 공개 폴더에 두지 않는다. `figures/shots/`는 공개하지 않는다.
- Chrome이 없으면 캡처를 건너뛰고 그 사실을 반환값에 적는다.

## 반환

짧게 돌려준다.

- 그림 목록(번호·제목·장)
- 고친 원고 파일
- 번호를 바꾼 곳
- 빠진 표 목록
- 캡처로 고친 것
