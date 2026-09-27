---
name: manuscript-qa
description: Proofreading pass for the integrated manuscript — runs manuscript-ci static checks and the writing-deslop 11-pattern AI-slop review, fixes what they confirm without touching facts or the author's voice, and logs every change. Also runs manuscript-ci check-build on the built EPUB. Invoked by the orchestrator after editor integration (before the Phase 4.5 gate) and again after the EPUB build. Triggers on "교정 패스", "CI 돌려", "deslop", "슬롭 점검", "원고 교정".
---

# Manuscript QA (교정 패스)

editor가 `04_manuscript.md`를 만든 뒤, 수락 게이트(4.5)로 넘기기 전에 한 번 돈다. 목적은 두 가지다. 기계가 잡을 수 있는 결함(중복 문단, 과한 단정어, 빌드 결함)을 사람 눈보다 먼저 잡고, AI가 쓴 글에 흔히 남는 문형(인질 협상식 반전, "X가 아니다. Y다.", 원룸 문장 등)을 걷어낸다. 사실·인용·수치·저자 장면은 이 패스의 대상이 아니다. 그건 fact-checker와 수락 게이트가 본다.

## 1. 원고 CI 정적 점검

```bash
.claude/skills/manuscript-qa/scripts/run_ci.sh check {slug}/04_manuscript.md
```

- 결과는 `{slug}/ci_report.md`에 저장된다. 종료 코드 3은 manuscript-ci가 설치돼 있지 않다는 뜻이다. 그러면 건너뛰고, 건너뛰었다는 사실을 `proofread_log.md`와 완료 보고에 적는다.
- 규칙별로 처리한다.
  - `duplicate-within-file`: 같은 문장·문단이 되풀이된 곳이다. 콜백이나 의도한 반복이 아니면 한쪽을 줄인다.
  - `strong-claim-word`("모두·반드시·유일한·전부·저절로" 등): 권고성 표시다. 근거가 그 강도를 받치지 못하는 문장만 고친다. 표·체크리스트·원문 인용·"~는 아니다" 같은 부정 문맥은 그대로 둔다. 건수를 0으로 만드는 것이 목표가 아니다.
  - 그 밖의 규칙은 메시지를 읽고 판단한다. 오탐이면 로그에 이유를 한 줄 적는다.

## 2. writing-deslop — AI 글 문형 11가지

writing-deslop 스킬을 Skill 도구로 부르거나 그 `SKILL.md`를 찾아 읽는다. 위치는 `~/.claude/skills/writing-deslop/` 또는 플러그인 캐시다. 거기 정의된 11가지 패턴으로 원고 전체를 훑는다. 보통은 장 단위로 끊어 읽는다.

- **기본은 직접 점검이다.** 원고를 외부로 보내지 않는다.
- **`--jev`(TypeSafe 트리아지)는 기본으로 쓰지 않는다.** `--jev`는 문단을 외부 API로 보낸다. 두 조건이 모두 맞을 때만 쓴다. 첫째, 사용자가 이 세션에서 외부 전송을 명시적으로 허락했다. 둘째, 원고의 비식별 검토가 끝났다. 여기에 `TYPESAFE_API_KEY`가 이미 환경에 있어야 한다. 쓰면 로그에 "Jev 사용: 사용자 허락 {날짜}"를 남긴다. 기밀·미공개 내용이 섞일 수 있는 원고를 외부 서비스로 보내지 않기 위해서다. 키는 파일이나 대화에 쓰지 않는다.
- 찾은 것은 후보로 다루고, 판결로 삼지 않는다. 잘 다듬어진 책 원고에서는 대부분이 오탐이다. 흔한 오탐은 세 가지다.
  - 요약 문장에 걸린 p5
  - 원문 인용 안의 문형
  - 진짜 질문 뒤에 실제 분석이 이어지는 경우
- 고칠 때는 활성 프로필(`profiles/{genre}/voice.md`)의 문체를 지킨다. tech-book의 평어체, 질문으로 열고 바로 답하는 구성, 장당 대구 상한처럼 프로필이 허용한 장치는 슬롭으로 보지 않는다.
- 고치는 곳은 두 군데다.
  - `04_manuscript.md`
  - 그 문장의 원천: `chapters/{NN}_final.md`, 또는 editor가 부속 원고를 따로 둔 경우 그 파일
  
  둘 다 고쳐야 재통합 때 수정이 사라지지 않는다.

## 3. 기록

`{slug}/proofread_log.md`에 한 파일로 append한다.

```markdown
## 교정 패스 — {날짜} (04_manuscript.md sha256 앞 12자리: 전 → 후)
- CI: {규칙별 건수} → 고친 곳 N, 그대로 둔 곳 M(이유 요약)
- deslop: 후보 N(직접 점검 / Jev), 확정 K — 장·패턴·전후 한 줄씩
- 건너뛴 도구와 이유
```

수정이 끝나면 수락 게이트가 이 로그를 읽는다. 교정 패스는 사실을 바꾸지 않는다. 문형을 고치다가 문장의 주장이 달라질 것 같으면 고치지 말고 로그에 "보류"로 남긴다.

## 4. 빌드 뒤 점검 (Phase 5)

EPUB을 빌드한 뒤 한 번 더 돌린다.

```bash
.claude/skills/manuscript-qa/scripts/run_ci.sh check-build {책-제목}-v{version}.epub
```

- `No build findings.`가 기준이다. 결함이 나오면 editor가 원인(원고의 마크다운이나 빌드 설정)을 고치고 같은 버전으로 다시 빌드한다. 이 단계의 수정은 마크다운 구문으로 한정하고 문장은 바꾸지 않는다. 수정은 `proofread_log.md`에 append한다. 두 번 고쳐도 남으면 사용자에게 묻는다.
- 흔한 원인은 `[라벨](날짜 문구)`처럼 대괄호 바로 뒤에 괄호가 붙어 링크로 해석되는 경우다. 대괄호와 괄호 사이를 한 칸 띄우면 된다.
