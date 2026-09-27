---
name: book-editing
description: Integrate all finished chapters into a single book-ready manuscript — polish chapter transitions, unify terminology, insert cross-chapter callbacks, and write front/back matter (preface, epilogue, references). Produce a manuscript + book_manifest.json for EPUB build. Use when chapters are individually complete and need to become a coherent book.
---

# Book Editing

완성된 챕터들을 한 권의 책으로 직조한다. 내용을 새로 쓰지 않고 흐름과 일관성을 다듬는다. 병렬로 쓴 챕터들을 처음으로 한꺼번에 보는 단계라서, 묶음 경계의 전환과 통권 단조로움은 여기서 잡는다.

## 절차

1. 모든 `{NN}_final.md`가 있는지 확인한다. 빠진 장은 `[미완성]` 주석과 함께 자리만 두고 보고한다.
2. 1장부터 순서대로 읽으며 전환부를 다듬는다 — 끝-시작 연결이 갑작스럽지 않은지, 여러 장이 같은 이음말로 끝나지 않는지.
3. 용어를 `02_plan.md`의 "용어 표기"에 맞춰 통일하고, 뒤 장이 앞 개념을 쓸 때 "앞서 3장에서 살펴봤듯이 ~" 같은 콜백을 자연스럽게 넣는다. 콜백의 장 번호는 실제 그 내용이 있는 장이어야 한다.
4. 통권 변주를 점검하고 고친다 (아래).
4-1. 그림·표를 점검한다. 캡션은 `그림 N-k.`·`표 N-k.` 형식이고, 장 안에서 나오는 순서대로 번호가 이어져야 한다. 부록은 `표 A-1.`처럼 쓴다. `figures/fig-N-k.svg` 참조가 모두 실재해야 하고, 본문이 "그림 N-k"를 부르는 곳의 번호가 실제 그림과 맞아야 한다. 남은 `<!-- 그림 … -->` 자리 표시는 0개여야 한다.
5. 부속 자료(서문·목차·에필로그·참고문헌·콜로폰)를 장르에 맞게 쓴다. practical 요리 계열이면 `profiles/practical/partials/conversion-tables.md`의 환산표를 부록에 복사한다.
6. `04_manuscript.md`로 합본하고, `book_manifest.json`을 쓰고, 분량 리포트를 만든다.

## 통권 변주 점검

장마다 (a) 오프닝 기법, (b) 클로징 형태, (c) 최다 반복 말버릇을 한 줄씩 표로 만든다.

```
| 장 | 오프닝 기법 | 클로징 형태 | 최다 반복 말버릇 |
|----|------------|------------|-----------------|
| 1  | 상황 가정   | 적용 과제   | ~해보자 (9)      |
| 2  | 실패 장면   | 다음 장 예고 | 그렇다면 (6)     |
```

인접 장의 같은 오프닝, '상황 가정' 오프닝이 전체의 1/3 초과(tech-book), 같은 클로징 공식의 반복, 책 전반에 과포화된 말버릇을 찾아 해당 문단을 고친다. 반복 횟수는 grep으로 센다. 표는 `editor_notes.md`에 남긴다 — 수락 게이트가 참고한다.

## 용어 통일 원칙

- 기준은 `02_plan.md`의 "용어 표기"다. 거기 없는 용어가 여러 표기(영문/한글, 축약/풀)로 흔들리면 가장 많이 쓰인 표기로 맞춘다
- 예외: 장르가 기술서면 "사용자"보다 "유저"가 자연스러울 때도 있음 — 문맥 우선
- 결정 불가능 → 서문에 "이 책에서는 {A}를 {B}로 표기한다" 정의

## 서문 작성 지침

- 왜 이 책을 썼는가 (문제의식)
- 이 책을 누가 읽으면 좋은가 (대상 독자)
- 어떻게 읽으면 좋은가 (순서·선택 독서 가이드)
- 감사의 말 (선택)
- 길이: 2~4페이지 분량

## 에필로그 작성 지침

- 여정을 짧게 돌아봄
- 책이 답하지 못한 질문들
- 다음 걸음에 대한 제안 (추천 도서·실천 과제)
- 길이: 1~2페이지

## 참고문헌

- 챕터에서 인용한 출처를 모아 단일 목록으로 정렬하고 중복을 없앤다. 정렬 방식(인용 순서 또는 저자 가나다순)은 하나로 통일한다.
- 형식: `저자. 제목. 발행처/URL, 날짜.`
- 서지 정보·식별자·확인 등급 라벨은 `research/*.md`와 `factcheck_log.md`에서 그대로 옮긴다. 원장에 없는 항목은 넣지 않는다.

## 분량 균형 점검

글자 수는 눈대중이 아니라 스크립트로 센다:

```bash
python3 .claude/skills/book-editing/scripts/length_report.py {slug} > {slug}/length_report.md
```

스크립트는 표·코드·mermaid·`:::` 블록·인용·헤딩을 뺀 산문 글자 수(공백 포함)를 장별로 세고, 중앙값 대비 70% 미만이나 150% 초과인 장을 표시한다. `02_plan.md`의 예상 분량과 ±20% 넘게 어긋나는 장, 그리고 중앙값 아래로 떨어진 1장(첫인상을 만드는 장이다)도 리포트 끝에 적는다. 의도적으로 짧은 장(막간 등)은 사유를 적어 예외로 둔다. 플래그된 장은 반환값에 올린다 — 확장·축약 여부는 수락 게이트와 오케스트레이터가 정한다.

## 출력 형식

`04_manuscript.md`:

```markdown
# {책 제목}

## 저자
{author}

**판본:** v{version} · {pub_date}

---

## 판권

**{책 제목}**
**판본:** v{version}
**발행일:** {pub_date}
**저자:** {author}
**식별자:** {identifier}

### 라이선스

이 책은 **CC BY-NC-SA 4.0** 라이선스로 배포된다 — [Creative Commons 저작자표시-비영리-동일조건변경허락 4.0 국제](https://creativecommons.org/licenses/by-nc-sa/4.0/).

- **저작자 표시(BY):** 출처를 밝혀야 한다.
- **비상업적 이용(NC):** 상업적 목적으로 이용할 수 없다.
- **동일조건 변경허락(SA):** 변경·재배포 시 동일한 라이선스를 적용해야 한다.

매니페스트에 `license` 필드가 다른 값으로 명시되어 있으면 그 값으로 위 문장과 링크를 갈음한다. 어느 경우든 매니페스트 `license`의 정식 코드 문자열이 지면에 그대로 나와야 한다 — `epub-build`가 콜로폰과 매니페스트의 `license` 문자열 일치를 대조한다.

### 출처

이 책은 [book-writer](https://github.com/tobyilee/book-writer) 하네스 v{harness_version}로 자동 생성되었다.

---

## 서문
...

## 목차
- 1장. ...
- 2장. ...

---

# 1장. {제목}
(전환부 다듬어진 본문)

# 2장. ...

...

## 에필로그
...

## 참고문헌
...
```

`book_manifest.json`:

```json
{
  "title": "...",
  "subtitle": "...",
  "author": "Toby-AI",
  "language": "ko",
  "pub_date": "YYYY-MM-DD",
  "identifier": "urn:uuid:...",
  "description": "한 문단 소개",
  "cover_image": "cover.png",
  "cover_alt": "{title} 표지",
  "version": "1.0.0",
  "license": "CC BY-NC-SA 4.0",
  "genre": "tech-book",
  "delegation_mode": "production",
  "harness_version": "2.0.0",
  "rights": "© {year} {author} — Licensed under {license}"
}
```

`license`, `harness_version`, `rights`는 옵션 필드. 비우면 빌드 스크립트가 하네스 기본값(`CC BY-NC-SA 4.0` + 루트 `VERSION` + 자동 생성 rights)으로 채운다. `genre`는 오케스트레이터가 확정한 장르(`tech-book`/`narrative`/`practical`/`essay`)를 기록한다 — 재실행 시 활성 프로필을 결정적으로 재사용하는 출처다. 누락 시 `tech-book`. `delegation_mode`는 오케스트레이터가 Phase 0에서 확정한 위임 다이얼(`production`/`learning`)을 같은 취급으로 기록한다 — 재실행 시 학습 터치포인트를 결정적으로 재사용하는 출처다. 누락 시 `production` (`docs/learning-loop.md`).

`cover_alt`는 표지 이미지의 대체 텍스트로, 빌드 스크립트의 alt-text 주입이 이 값을 출처로 쓴다. 비우면 기본 패턴 `"{title} 표지"`를 적용한다.

**식별자(identifier) 발급 규칙:** `identifier`는 **신규 책일 때 한 번만** 생성한다 — `python3 -c "import uuid;print('urn:uuid:'+str(uuid.uuid4()))"`. 플레이스홀더 `"urn:uuid:..."`를 그대로 복사하지 않는다. 같은 책 재빌드 시 기존 `book_manifest.json`의 `identifier`를 **그대로 보존**하고 `version`만 올린다 (식별자는 책의 영구 ID — 재빌드마다 바뀌면 안 된다).

## 재편집 시

- 일부 챕터만 갱신 → 해당 섹션만 교체하고 전환부와 분량 리포트를 다시 만든다.
- 서문·에필로그 개선 요청 → 해당 섹션만 다시 쓴다.
- 구조·내용 변경 제안은 `editor_notes.md`에 적는다.
