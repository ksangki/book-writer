---
name: site-build
description: Phase 6 — turn the finished book into its public companions every time, the same way. Builds the web edition from the EPUB, writes and builds a one-hour presentation deck (every content slide gets a plain-language "쉽게 말하면" analogy), visually checks both with headless Chrome, and prepares the site folder the brag launch video is made from. Triggers on "웹 버전", "발표자료", "덱 만들어", "사이트 빌드", "홍보 영상 소스".
---

# Site build (웹 · 발표자료)

EPUB이 나온 뒤 Phase 6에서 돈다. 모든 책이 같은 모양의 동반 산출물을 갖게 하는 것이 목적이다. 웹 버전으로 바로 읽히고, 1시간 발표자료로 소개되고, 그 둘을 소스로 홍보 영상이 만들어진다. 책마다 달라지는 것은 발표 내용(`{slug}/deck/slides.py`)과 색(`book_manifest.json`의 `theme`)뿐이다.

## 산출 구조

```text
{slug}/site/                  ← 공개 저장소에 그대로 올라가는 폴더
  index.html                  웹 버전 (EPUB → pandoc HTML)
  cover.png                   {slug}/cover.png 복사본
  BOOK.md                     책 소개 md 복사본
  epub/{책-제목}-v{version}.epub
  figures/fig-*.svg           본문 그림 (덱이 ../figures로 참조)
  media/                      웹 버전이 추출한 그림
  presentation/index.html     발표자료
{slug}/deck/slides.py         발표 내용 (엔진: scripts/deck.py)
{slug}/deck/shots/            화면 확인용 캡처 (공개하지 않음)
{slug}/brag-output/           홍보 영상 (Phase 6-3, 공개 폴더 밖)
```

`site/`에는 `.gitignore`를 둔다. 공개 저장소는 `site/`를 따로 만들기 때문에 하네스 루트의 `.gitignore`가 적용되지 않는다. `site/` 밖의 것은 공개하지 않는다. 특히 `brag-output/`의 작업 폴더(node_modules 등)와 `.omc/` 같은 세션 상태 파일을 `site/`나 공개 저장소에 두지 않는다. 공개 저장소에 올릴 때는 `git add -A`를 쓰지 말고 파일을 이름으로 지정한다.

## 1. 폴더 준비와 웹 버전

```bash
S={slug}/site; mkdir -p $S/epub $S/figures $S/presentation
cp {책-제목}-v{version}.epub $S/epub/; cp {책-제목}-v{version}.md $S/BOOK.md; cp {slug}/cover.png $S/
cp {slug}/figures/*.svg $S/figures/
printf '.omc/\nbrag-output*/\nnode_modules/\n.shot_*\n*.log\n.DS_Store\n' > $S/.gitignore   # 공개 저장소에 따라가는 방어선
python3 .claude/skills/site-build/scripts/build_web.py {slug} $S/epub/{책-제목}-v{version}.epub $S
```

- `build_web.py`는 제목·부제·표지 alt를 매니페스트에서 읽는다. 매니페스트에 `repo_url`이 있으면 GitHub 링크를 단다.
- 색은 `theme.light_accent`·`theme.dark_accent`에서 가져온다. 없으면 기본값을 쓴다. 매니페스트에 `theme`이 없으면 site-builder가 표지(`cover.png`)의 바탕색과 강조색을 보고 한 번 채운다. 형식은 아래와 같다. 그러면 웹·덱·영상이 같은 색을 쓴다.

  ```json
  "theme": {"light_accent": "#9a6b1c", "dark_accent": "#e3b35a",
            "deck": {"bg": "#0f1a26", "panel": "#16222f", "line": "#2a3a4c", "accent": "#e3b35a", "accent_d": "#b8862f", "glow": "#1a2a3c"}}
  ```
- 출력 끝의 "그림 N · 표 캡션 M"이 원고의 그림·표 수와 맞는지 본다.

## 2. 발표자료

`{slug}/deck/slides.py`를 쓴다. 엔진은 `scripts/deck.py`이고, 사용법은 파일 머리의 예시를 따른다. 슬라이드 함수는 다음과 같다.

- `cover`, `end_cover`
- `divider` (부 구분면)
- `quote`, `cards`, `table`, `stat`, `bullets`, `figure`
- `ez` (직전 슬라이드에 '쉽게 말하면' 한 줄)

**구성 규약** — 모든 책에 같게 쓴다. 청중이 책을 읽지 않았다는 전제다.

1. **여는 순서:** 표지(표지 그림) → 먼저 질문 하나 → 결론부터(책 전체를 한 표나 한 문장으로) → 이 책을 읽는 법 또는 순서.
2. **본론:** 부(PART)마다 구분면 하나, 그 뒤에 부의 핵심을 4~8장으로 싣는다. 슬라이드 종류는 다섯 가지다.
   - 저자 장면(quote)
   - 핵심 수치(stat, 출처·날짜·[자체 보고] 라벨 포함)
   - 본문 그림(figure)
   - 세 갈래 정리(cards)
   - 표(table)
3. **닫는 순서:** 결론 한 문장으로 되돌아가기 → 가져갈 것(도구·실천 한 가지) → 감사 표지.
4. **비유 한 줄:** 모든 내용 슬라이드에 `ez()`로 '쉽게 말하면' 비유를 하나씩 단다. 일상의 장면(요리, 이사, 등산, 도서관 같은 것)으로 그 슬라이드의 요지를 한 문장에 옮긴다. 빠진 슬라이드가 있으면 엔진이 WARNING으로 알린다.
5. **분량:** 30~45장이다. 1시간 발표에 슬라이드당 1~2분 기준이다.
6. **내용의 출처는 수락된 `04_manuscript.md`뿐이다.** 원고에 없는 사실·수치·저자 장면을 넣지 않는다. 수치는 원고의 문장 그대로 옮기고, 출처 라벨도 따라 붙인다. 원고의 근거 표지가 '하'인 장은 슬라이드 foot에도 그 한계를 한 줄 적는다.
7. **금지어·비식별:** 원고의 용어 규칙(`00_direction.md`·`02_plan.md`의 용어 표기)을 그대로 따른다.

빌드:

```bash
python3 {slug}/deck/slides.py .claude/skills/site-build/scripts {slug}/site/presentation/index.html
```

## 3. 화면 확인

눈으로 보지 않은 슬라이드는 끝난 것이 아니다. 헤드리스 Chrome으로 찍어 직접 본다.

```bash
SH=.claude/skills/site-build/scripts/shot.sh
$SH {slug}/site/index.html {slug}/deck/shots/web.png 1100x1400
for n in 1 2 3 <그림 슬라이드 번호들> <마지막>; do $SH {slug}/site/presentation/index.html {slug}/deck/shots/s$n.png 1440x900 $n; done
```

- 표지, 결론, 그림 슬라이드 전부, 표 슬라이드 하나, 마지막 장을 본다.
- 볼 것은 네 가지다: 글자가 상자를 넘치는지, 그림이 한 화면에 들어오는지, '쉽게 말하면' 상자가 화면 밖으로 밀리는지, 색이 표지와 맞는지.
- 휴대폰 폭 확인은 헤드리스 창의 최소 폭 때문에 캡처가 실제보다 넓게 찍힌다. 그래서 캡처로 판단하지 말고, 390px iframe 안에서 `scrollWidth`를 재서 가로 넘침이 없는지 확인한다.

## 4. 홍보 영상 소스 넘기기

오케스트레이터가 `site/`를 소스로 brag 스킬을 부른다. site-build는 `site/index.html`, `site/cover.png`, 그림이 제자리에 있고 영상에 쓸 만한 장면이 무엇인지 반환값으로 짧게 넘긴다. 예를 들면 대표 그림 2~3개, 결론 문장, 핵심 수치 하나다.

## 반환

짧게 돌려준다.

- site 경로
- 웹의 그림·표 수
- 덱 장수
- '쉽게 말하면' 누락 수(0이어야 함)
- 캡처로 확인한 슬라이드 번호와 고친 것
- 영상 소스로 추천하는 장면
