---
name: book-launch
description: Phase 8 — publish a finished book and promote it, only when the author asks. Creates or updates the book's public GitHub repo from {slug}/site (named-file commits, never `git add -A` or `rsync --delete`), enables GitHub Pages, verifies the live site (cover, opening video, illustrations, EPUB download, new-window links), writes the repo README, then drafts a short LinkedIn post centered on the book's conclusion/epilogue and renders a LinkedIn document carousel (1080×1350 PNGs + PDF). Triggers on "공개해줘", "배포해줘", "github page에 올려", "링크드인 글", "링크드인 캐러셀", "소개 문구", "홍보".
---

# 공개와 홍보

책을 공개 저장소로 내보내고 알리는 단계다. **저자가 공개를 요청할 때만** 한다. 이미 공개된 책도 새 판을 올리려면 그 판에 대한 공개 요청이 있어야 한다. 첫 공개는 1 → 2 → 4, 재배포는 1 → 3 → 4 순서이고, 1(공개 전 점검)은 어느 경우에도 건너뛰지 않는다. 링크드인(5~6)은 공개 뒤에 하거나 따로 요청받았을 때 한다. 저자 부재 자율 모드로 만든 책은 저자가 돌아와 원고·비식별을 확인하기 전까지 push하지 않는다.

## 1. 공개 전 점검

- 원고에 회사·부서·인물 실명, 사내 시스템·사내 용어, 미공개 수치, 개인정보, 인증정보가 없는지 `grep`으로 한 번 더 본다(`00_brief.md`의 금지 목록 기준).
- 판권의 판본·발행일·판 이력과 매니페스트 `version`이 같고, EPUB 파일명이 그 판본인지 본다.
- `{slug}/site/`에 `index.html`·`presentation/`·`epub/{새 EPUB}`·`cover.png`·`BOOK.md`·`media/`(영상·삽화)·`figures/`가 있는지 본다. 외부 도구가 넣은 낯선 파일이 있으면 공개 대상에서 빼고 저자에게 알린다.

## 2. 새 공개 저장소 (첫 공개)

```bash
gh repo create ksangki/{repo} --public --description "{제목}: {부제}"
git clone https://github.com/ksangki/{repo}.git ~/source/github/{repo}
# site/의 허용 목록만 이름으로 복사한다
cp -R {slug}/site/{index.html,presentation,epub,figures,media,cover.png,BOOK.md,.gitignore} ~/source/github/{repo}/
mkdir -p ~/source/github/{repo}/deck && cp {slug}/deck/slides.py ~/source/github/{repo}/deck/   # 덱 원천을 공개할 때만, slides.py 하나 (shots/는 공개하지 않는다)
```

- README에는 초안 판본 표시(저자 검토 전이면), 한 문단 소개, 읽기 링크(웹·EPUB·책 소개·발표 자료·오프닝 영상), 차례, 라이선스를 둔다.
- 커밋은 파일을 이름으로 지정한다. `git status --short`의 목록이 허용 목록(`index.html`·`presentation/`·`epub/`·`figures/`·`media/`·`cover.png`·`BOOK.md`·`README.md`·`.gitignore`·`deck/slides.py`)과 맞는지 대조한 뒤 커밋한다.
- Pages: `gh api -X POST repos/ksangki/{repo}/pages -f 'source[branch]=main' -f 'source[path]=/'`. 주소는 `https://ksangki.github.io/{repo}/`, EPUB은 `…/epub/{파일}`.

## 3. 재배포 (판 올림)

- 먼저 `git -C ~/source/github/{repo} log --oneline -5`와 `git status --short`를 본다. 저자가 다른 세션에서 넣은 커밋·파일(오프닝 영상, 작업 폴더)이 있으면 그대로 둔다.
- `rsync --delete`를 쓰지 않는다. 바뀐 파일만 복사하고, 지울 파일은 `git rm`으로 이름을 지정한다. 이전 판 EPUB은 이미 나간 링크가 죽지 않게 남겨 둔다.
- `build_web.py`는 저장소 폴더에 직접 출력해도 된다. 그래야 저장소에만 있는 `media/opening.mp4` 블록이 살아남는다.

## 4. 라이브 확인

push 후 1~2분 기다린 뒤 공개 주소에서 확인한다(WebFetch 또는 headless Chrome).

- 표지, 오프닝 영상(재생·포스터), 삽화, 본문 그림이 뜨는가
- EPUB 내려받기 링크가 200인가(`curl -sI`)
- 바깥 링크가 새 창으로 열리는가(`target="_blank"` 수), 맨 주소가 링크로 바뀌었는가
- 390px 폭에서 가로 넘침이 없는가
- 발표 자료가 열리는가

확인한 것과 확인하지 못한 것을 나눠 보고한다.

## 5. 링크드인 글

- **재료:** 에필로그나 결론 장의 문장. 원고에 없는 주장·수치·과장된 카피는 쓰지 않는다.
- **모양:** 첫 두 줄에 책이 던지는 질문이나 결론(피드에서 "더 보기" 전에 보이는 부분), 본문 5~8줄(핵심 3가지를 한 줄씩), 웹 주소 1개, 해시태그 3~5개.
- **형식 고르기:** 영상 하나만 붙인 게시물보다 문서형 캐러셀(PDF)이나 여러 장 이미지가 넘겨 보는 동안 머무는 시간이 길어 노출이 잘 되는 편이다. 기본은 캐러셀이고, 오프닝 영상은 댓글이나 다음 게시물로 돌린다.
- writing-deslop 규칙(엠대시 금지, 대조 틀·세 개 나열 남용 금지)을 적용한 뒤 저자에게 붙여 넣을 수 있는 텍스트로 준다.

## 6. 캐러셀

1. `{slug}/linkedin/src/`에 `templates/carousel.html`을 복사하고, `cover.png`와 삽화(`ill1.jpg`…)를 같은 폴더에 둔다.
2. 6~10장으로 채운다: 표지 → 질문 → 핵심 3장(삽화 위 한 문장 + 근거 한두 문장) → 다음 주에 해 볼 도구 하나 → 읽는 곳(웹 주소). 쪽 번호(`n / N`)를 맞춘다.
3. 찍는다. 넘침이 있으면 종료 코드 1이다.

   ```bash
   node .claude/skills/book-launch/scripts/carousel_shot.js $PWD/{slug}/linkedin/src $PWD/{slug}/linkedin
   ```

   스크립트는 출력 폴더의 예전 `NN.png`를 먼저 지우고, 이번에 찍은 페이지만으로 `carousel.pdf`를 만든다(ImageMagick 필요). 종료 코드 1은 넘침·크기 오류, 2는 `.s` 페이지 없음이다.

4. 결과를 접촉 시트로 한 번 보고, 저자에게 폴더를 열어 준다(`open {slug}/linkedin`).

## 주의

- 링크드인·SNS에 직접 게시하지 않는다. 글과 이미지를 만들어 저자에게 넘길 뿐이다.
- 책 브랜치(`{slug}` 작업 브랜치)는 로컬에 둔다. 공개는 `ksangki/{repo}` 저장소로만 한다.
- 커밋 메시지 끝에는 세션이 지정한 공동 저자 줄을 붙인다.
