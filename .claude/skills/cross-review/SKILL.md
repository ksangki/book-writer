---
name: cross-review
description: Phase 7 — cross-model review of a finished book. Ingests an external GPT/ChatGPT editorial review folder (편집검토.md, 문체-검토.md, generated illustrations, placement plan) and/or calls the local Codex CLI directly (read-only, with illustration images attached) to review the manuscript diff, illustrations and book rules; re-verifies every factual claim against research/primary sources before applying; then applies text fixes, illustrations (placement, caption, alt), colophon edition history, bumps the minor version and rebuilds EPUB/web. Triggers on "GPT 검토 반영", "편집 검토 반영", "삽화 반영", "Codex랑 같이 검토", "코덱스 검토", "교차 검토", or when the user pastes a path to a ChatGPT outputs folder.
---

# 교차 검토 (GPT · Codex)

책을 만든 모델과 다른 모델에게 원고를 한 번 더 읽힌다. 같은 모델의 수락 게이트(Phase 4.5)가 놓친 수치 해석, 번역투, 저자 경험의 과장이 다른 눈에서 매번 나왔다. 반대로 외부 검토서가 틀린 경우도 매번 나왔다. 그래서 이 단계의 핵심은 **받은 지적을 원문에 다시 대조한 뒤에만 반영하는 것**이다.

## 입력

- 책 폴더 `{slug}/`: `04_manuscript.md`(정본), `research/*.md`, `00_brief.md`(있으면), `book_manifest.json`
- GPT 결과 폴더(저자가 경로를 준다). 흔한 구성:
  - `편집검토.md` 또는 `문체-검토.md`: 고칠 곳 표(위치·원문·수정안)
  - `삽화/*.png` 또는 `media/illustrations/*.jpg`: 생성 삽화
  - `삽화-배치안.html` 또는 삽화가 들어간 `index.html`: 위치와 캡션
- 로컬 Codex CLI(`codex`). 없으면 Codex 단계만 건너뛴다.

## 1. 받은 폴더 확인

1. 폴더 안 파일 목록과 md5를 본다. 이름이 비슷한 폴더(`… 2`, zip 풀린 사본)가 이미 반영한 것과 같으면 저자에게 그렇다고 알리고, 같은 상위 폴더에 이번 책 이름의 새 폴더가 있는지 찾는다.
2. 삽화는 축소 접촉 시트(`magick … +append/-append`)로 한 번에 보고, 배치안에서 각 삽화의 앞 문단과 캡션을 뽑는다.
3. 표지 파일이 들어 있으면 지금 표지와 md5를 비교한다. 같으면 무시한다.

## 2. 순서

GPT 검토와 Codex 검토를 함께 하면 아래 순서로 한다. 반영한 결과를 다른 모델이 다시 보게 하기 위해서다.

1. **백업:** `{slug}/_v{이전}/`에 `04_manuscript.md`·`book_manifest.json`을 복사한다. 모든 diff의 기준이다.
2. **GPT 지적 재대조 → 반영** (3절·4절)
3. **diff 만들기:** `diff <(fold -w 2000 {slug}/_v{이전}/04_manuscript.md) <(fold -w 2000 {slug}/04_manuscript.md) > $REVIEW/v{새}.diff || true` (diff는 차이가 있으면 종료 코드 1을 낸다)
4. **Codex 검토** (아래)
5. **Codex 지적 재대조 → 반영** (3절·4절)
6. **판·빌드·기록** (5절)

저자가 Codex만 원하면 2를 건너뛰고, 3에서 diff 대신 원고 전체를 검토 폴더에 넣는다.

### Codex 검토

Codex에는 **검토 전용 폴더**(`$REVIEW`, 스크래치 아래 새 폴더)만 보여 준다. 프로젝트나 책 폴더 전체를 열어 주지 않는다.

- 넣는 것: 원고 사본(`04_manuscript.md`), 이번 판 diff, 수치 대조에 필요한 `research/*.md` 발췌, 전송 가능한 저자 사실 목록(`author_facts.md`).
- `author_facts.md`는 `00_brief.md`의 1인칭 허용 사실을 그대로 옮기되, 브리프의 금지 목록(회사·부서·인물 실명, 사내 용어, 미공개 수치, 개인정보, 인증정보)을 `grep`해 하나라도 남으면 그 줄을 일반화하거나 빼고, 일반화가 불가능하면 전송을 보류하고 저자에게 묻는다. 원고 사본도 같은 `grep`을 통과해야 넘긴다.
- 사실 목록을 빠뜨리면 Codex가 저자의 실제 생각까지 "지어낸 경험"으로 지적한다. 실제로 그랬다.

```bash
bash .claude/skills/cross-review/scripts/codex_review.sh $REVIEW $REVIEW/prompt.md $REVIEW/codex_review.md \
     $(ls {slug}/illustrations/*.{jpg,jpeg,png} 2>/dev/null)
```

`run_in_background: true`로 띄우고 완료 알림을 기다린다. 스크립트는 읽기 전용 샌드박스로 `$REVIEW`만 열고, 없는 이미지와 이미지가 아닌 파일은 건너뛴다. 종료 코드 3은 Codex 미설치(이 단계만 건너뛴다), 2는 인자 오류다.

지시문에 넣을 것:

- 검토 범위: 삽화(본문·캡션 일치, 위치, 로고·읽히는 글자·실존 인물처럼 보이는 요소, alt가 보이는 것만 묘사하는지), diff의 문장 수정(의미가 더 정확해졌는지, 새 오류), 수치 문단은 함께 넣은 연구 발췌와 대조, 책 규칙(엠대시, 대조 틀 장당 2회, 금지 단어, 저자 경험 창작). 저자 사실은 `author_facts.md`를 기준으로 하라고 적는다.
- 출력: 항목마다 `[필수 수정]/[권장]/[문제 없음]`, 원문 인용과 수정안, 근거 없는 지적 금지, 파일 수정 금지.

## 3. 재대조 (반영 전 필수)

받은 지적을 세 가지로 나눈다.

| 종류 | 처리 |
|---|---|
| 수치·인용·출처 해석 | `research/*.md`의 원문 인용과 1차 출처(WebFetch)로 다시 확인한다. 맞으면 반영, 틀리면 반영하지 않고 근거를 적는다 |
| 저자 경험·감정 | `00_brief.md` 허용 사실과 대조한다. 허용 사실이면 지적을 기각하고, 허용 밖이면 지운다 |
| 문장·번역투·구성 | 책 규칙(엠대시·대조 틀·금지 단어)을 지키는 선에서 반영한다. 수정안이 새 대조 틀이나 금지 단어를 만들면 다시 쓴다 |

검토서 수정안을 그대로 붙이지 말고, 앞뒤 문장과 이어지게 다시 쓴다. 수정안이 새 단정(예: "로그에 바로 뜬다")을 만들면 범위를 좁힌다.

## 4. 반영 방법

1. **스크립트로 치환:** 한 파일에 (원문, 수정문, 태그) 목록을 두고 원문이 정확히 1번 나올 때만 바꾼다. 0번이나 2번 이상이면 멈춘다. 정본이 장 final에서 재조립되는 책이면 같은 수정을 원천에도 넣는다.
2. **삽화:** `{slug}/illustrations/`에 복사하고, 배치안의 앞 문단 끝에 넣는다.

   ```markdown
   ![삽화. {캡션} 상상으로 그린 장면으로, 특정 인물이나 조직이 아니다.](illustrations/ch02.jpg){alt="{그림에 보이는 것만}"}
   ```

   alt에는 정지 화면에서 보이는 것만 쓴다("건네려다 멈춘다" 같은 행동 추정, "오류를 표시한다" 같은 해석을 넣지 않는다).

## 5. 판·빌드·기록

1. **판:** 문장·수치·삽화가 바뀌면 minor(v1.0.0 → v1.1.0), 오탈자·링크·마크다운만 고쳤으면 patch(`epub-build` 규칙과 같다). 판권 판본과 `**판 이력:**`(이번 판 내용 한 줄), 매니페스트 `version`·`edition_history`(이전 판 항목은 두고 새 항목 추가)를 맞춘다. 생성 이미지를 처음 쓰면 제작 고지에 "본문 삽화 N점은 이미지 생성 모델로 그린 상상 장면이다"를 넣고, 예전 "이미지 생성 도구 미사용" 문구가 있으면 고친다. 식별자(`urn:uuid`)는 유지한다.
2. **EPUB과 책 소개:** EPUB을 새 판으로 빌드하고 `epubcheck` 0건을 확인한다. 같은 stem의 책 소개 `{제목}-v{새}.md`도 만든다(이전 판 소개를 복사해 판본·바뀐 점을 고친다).
3. **웹·덱:** 새 EPUB을 `site/epub/`에, 새 책 소개를 `site/BOOK.md`에 복사하고 웹을 다시 빌드한다(`build_web.py`). 390px·1440px 넘침을 확인하고, 덱이 있으면 다시 빌드한다.
4. **기록:** `{slug}/07_cross_review.md`에 받은 지적 목록과 처리(반영/기각/수정 반영)와 근거를 남긴다. 기각한 지적은 이유를 꼭 적는다.
5. **멈춤:** 여기까지가 이 스킬의 범위다. 이미 공개된 책이라도 이번 판을 다시 올리는 것은 사용자가 이번 판의 공개를 요청할 때 `book-launch`로 한다.

## 6. 보고

저자에게는 표 하나로 보고한다: 지적, 출처(GPT/Codex), 처리, 근거. 기각한 것과 지시문 탓에 생긴 오판(예: 저자 사실 목록 누락)도 숨기지 않는다. 다른 책의 오류를 찾았으면 정오 후보로 따로 적는다.

## 주의

- push·재배포는 하지 않는다. 공개된 책이라도 이번 판의 공개 요청이 따로 있어야 한다.
- `site/` 안에 외부 도구가 직접 넣은 파일(예: GPT가 만든 `media/illustrations/`, `삽화본.epub`)이 있으면 지우지 말고 보고한다.
- Codex에는 검토 전용 폴더와 공개 예정 이미지만 넘긴다. 사내 문서·개인정보·인증정보가 섞인 파일은 넣지 않는다.
