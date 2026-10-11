# 수락 검수: 「디지털 워커의 시대」 v1.7.0 개정판

<!-- 검수: 2026-10-10 · v1.7.0 라운드 1 · 검수자: manuscript-reviewer (fresh context) -->

- **판정 대상:** `04_manuscript.md` — sha256 **`646b9fca677b109717786e95b70e4a08d473b781713d14d2bfc332c80624f1d3`** (직접 계측, coordinator 통지 `646b9fca677b…`와 일치), 228,118자(파이썬 `len`), 3,314줄
- 이전 판정: v1.6.0 ACCEPT, 발간 전 조치 마감 뒤 최종 sha `11b1beaac02f…`(218,321자). `04_manuscript_v1.6.0.md`의 sha256이 `11b1beaac02f2adf…`임을 직접 확인함. 이전 판정 기록은 `05_acceptance_v1.6.0.md`에 있음(덮어쓰기 전에 `cmp`로 현재 `05_acceptance.md`와 같은 파일임을 확인)
- 장르 `tech-book` · 슬러그 `ax-system` · 위임 모드 `production` · 매니페스트 `version 1.7.0` / `pub_date 2026-10-10` / `harness_version 1.11.0` / `license CC BY-NC-SA 4.0`
- **범위:** v1.7.0 변경분만 본다. 상자 밖 본문과 부록 A·B는 재판정하지 않고 v1.6.0의 PASS를 유지한다. 이 전제는 아래 diff로 직접 확인했다.

## 전제 확인: v1.6.0 수락본 대비 diff

`diff 04_manuscript_v1.6.0.md 04_manuscript.md` 결과 변경 hunk는 아래 10개뿐이다. 통지된 변경 목록과 정확히 같고, 그 밖의 변경은 0이다.

| 위치 | 변경 |
|---|---|
| L7, L15 | 판본 v1.6.0 → v1.7.0 (본문 상단 판본 줄, 판권) |
| L77 | "저장소 주소는 각 상자 끝과 부록 B-7에, 직접 돌려 보는 방법은 부록 C에 적었다" |
| L87 | 「둘째, 시점」에 "v1.7.0의 부록 C" 추가 |
| L128 | 목차에 "부록 C. 예제 직접 돌려 보기" 추가 |
| L627·1058·1834·2147·2618 | 상자 ①~⑤에 "직접 돌려 보기: `python run.py aN` — … 부록 C." 한 줄씩 (④만 "①~③의 실행 기록을 환산한다" 추가) |
| L3121–3314 | `# 부록 C. 예제 직접 돌려 보기` (C-1~C-7) 신설 |

L55 괄호는 style 검수 Nice 3에 따라 v1.6.0 문장으로 되돌아가 있다(diff 0). 상자 다섯의 `::: {.case}` 5개는 그대로이고, 부록 C의 코드 펜스 30개(15블록)는 짝이 맞는다.

## 직접 세기: 부록 C를 예제 저장소 코드·실행과 대조

순환 논증을 피하려고 factcheck_log v1.7.0 절의 ✅ 판정은 근거로 쓰지 않았다. `/home/user/ax-system/examples/digital-workers/`의 코드를 직접 읽고, 원본 파일을 파싱해 세고, 스크래치 복사본에서 실행했다. API는 호출하지 않았다. 복사본은 끝난 뒤 리터럴 경로로 삭제했다.

| 부록 C 주장 | 대조 대상 | 결과 |
|---|---|---|
| `python run.py a1~a5`, `all`, `--approve ask\|yes\|no`(기본 ask) | `run.py` argparse(`choices=[*AGENTS,"all"]`, `default="ask"`) | ✅ |
| 키 없을 때 문장 `ANTHROPIC_API_KEY 환경 변수가 없습니다. 키는 코드나 파일에 적지 말고 환경 변수로 넘기세요.` | 복사본에서 키 없이 `python run.py a1` 실행 → 글자 단위로 같음 | ✅ |
| `requirements.txt` 세 가지(anthropic·ruamel.yaml·PyYAML), Python 3.10 이상 | `requirements.txt` 3줄, README L41 | ✅ |
| clone URL `github.com/ksangki/ax-system`, `examples/digital-workers` | `git remote -v` origin. 기록본 `logs/*.jsonl`·`outputs/*`·`registry.yaml`은 `.gitignore` 예외로 git 추적됨(`git ls-files`) → `git checkout -- logs outputs registry.yaml`이 작동함 | ✅ |
| **`python tests/dry_run.py` 마지막 줄 `점검 통과: 등록부 상태 retired, 자격 증명 회수, 묘비 기록 확인`** | 복사본에서 키 없이 실행 → 마지막 줄이 글자 단위로 같고 종료 코드 0. 실행 뒤 `registry.yaml` sha256, `logs/`, `outputs/`가 원본과 같음(`diff -r` 0) → "스스로 되돌린다" ✅ | ✅ |
| C-3 화면 문장: S0 → `형식 오류로 저장하지 않았습니다`, 공지 → `'send_customer_notice'은 제안만 허용됩니다.`, 폐기안 없이 폐기 → 거부, 일곱 항목 미달 → 저장 안 됨 | dry_run 출력: "형식 오류로 저장하지 않았습니다: severity='S0'…", "'send_customer_notice'은 제안만 허용됩니다. …", "폐기안이 없습니다. …", "저장하지 않았습니다: ②③④⑤⑥⑦ 항목이 없습니다." | ✅ |
| C-3 점검 범위 "세 갈래(auto·approve·suggest)와 읽기 범위 밖 거부", 미등록은 실험 2 | dry_run `SCRIPTS`: a2의 `registry.yaml` 읽기(→`read_denied`), 미등록 행위 호출 없음 | ✅ |
| C-4 승인 프롬프트 3줄 모양, 승인 입력 `y`·`yes`·`예`·`ㅇ`, 나머지 거절 | `runtime._ask_human()` 출력 형식·`answer in ("y","yes","예","ㅇ")`. summary `{id} {name} — {reason}`(a5) | ✅ |
| `approve` 수준은 ⑤의 `retire_agent` 하나뿐 | `registry.yaml` 전체 8개 항목의 `actions` | ✅ |
| ③ `절차서: …` 출력, outputs → fallback 순서 | `a3.load_sop()`. dry_run 출력 `절차서: outputs/sop_incident_triage.md` | ✅ |
| ④ "`AGT-001의 실행 기록이 없습니다. 먼저 그 에이전트를 실행하세요.`", 기준값은 AGT-001~003뿐 | `a4_performance.py` L93, `baselines.yaml`. dry_run에서 AGT-005 → "기준값이 없어 환산하지 않습니다" | ✅ |
| ⑤ `이미 retired 상태입니다.` (모델이 요청하지 않을 수도 있음) | `a5.retire_agent()` — `plans` 확인 → status 확인 순서. 단서 문장이 이 순서와 맞음 | ✅ |
| C-4 ① 요약 한 줄 "처리 18건 · 사람 개입 0회 · 토큰 입력 17,110 / 출력 9,119 · 약 $0.241" | `logs/usage.jsonl` AGT-001: items 18, human_touches 0, input+cache_read+cache_write 17,110, output 9,119, cost 0.241. 출력 형식은 `runtime.run()` 끝 print와 같음 | ✅ |
| C-5 사건 표: run_start/run_end 5/5, read 19, action_auto 69, handoff 1, approved 1, retired 1 | `logs/audit.jsonl` 직접 집계: 같음. 나머지 사건 0 | ✅ |
| "`action_auto` 69건 가운데 22건은 `read` 수준" | action별 집계: list_projects 1 + read_document 1 + list_open_tickets 1 + read_ticket_log 8 + read_usage 1 + read_baselines 1 + list_registry 1 + get_activity 8 = 22 | ✅ |
| `grep handoff_to_human` → T-1008 한 줄 | audit L65 한 줄, `ticket_id: T-1008` | ✅ |
| C-5: `hold` 보류 2건, 열린 질문 9개, `assigned` 확인, `suggestions.jsonl` 없음 | `a1_verdicts.jsonl` hold=true 2 · audit `record_open_question` 9 · `a3_triage.jsonl` assigned=false 8/8 · `outputs/suggestions.jsonl` 없음 | ✅ |
| C-6 실험 1: `assign_ticket: suggest` → `'assign_ticket'은 제안만 허용됩니다.` / `send_customer_notice: auto` → `발송했습니다.` | 복사본 등록부를 고쳐 dry_run 실행 → 두 문장 모두 실측과 같음 | ✅ |
| C-6 실험 2: 줄 삭제 → `거부됨: 'assign_ticket'은 등록부에 없는 행위입니다. 실행하지 않았습니다.` / `status: paused` → `[AGT-003] 등록부 상태가 'paused'라 실행하지 않습니다.`, 점검 전체가 ③에서 멈춤 | 복사본 실측: 두 문장 같음. paused면 a3에서 `sys.exit`, "점검 통과" 줄 없음 | ✅ (관찰 1 참조) |
| C-6 실험 3: `action_rejected`, `담당자가 'retire_agent'을 승인하지 않았습니다. 실행하지 않았습니다.` | `runtime.authorize()` approve 분기 문자열 | ✅ (API 필요, 코드로만 확인) |
| C-6 실험 4: `projects.csv` 열 일곱 `id,name,team,description,status,touches,users` | `data/projects.csv` 헤더 | ✅ |
| C-7 합계 127,330 / 36,413 / 약 1.004달러, 한 번 0.06~0.29달러 | usage 5줄 합: 127,330 / 36,413 / 1.0037. 최소 0.0587, 최대 0.2934 | ✅ |
| C-7 단가 입력 4·출력 20·캐시 쓰기 5·캐시 읽기 0.20달러 | `runtime.PRICE` | ✅ |

**결론:** 부록 C의 명령·파일명·화면 문장·건수·금액이 코드와 실행 결과에 맞는다. `python tests/dry_run.py`의 통과 문장도 실측과 같다.

## 기준 판정

| ID | 기준 | 판정 | 근거 / 조치 |
|----|------|------|------------|
| (a) | 챕터 완비·분량 균형 | **PASS** | `# N장` 10개, PART 5개, 부록 A·B·C. 장 구성은 v1.6.0과 같다(위 diff에서 본문 변경 0). H1 grep에 잡히는 `# 1단 —`·`# 2단 —`(L2128·2131)은 상자 ④의 python 코드 블록 안 주석이라 헤딩이 아니다. 부록 C 9,479자는 상한 9,000자를 +479자(+5.3%) 넘는다. 수용 근거(코드 리터럴 때문에 과대 계측됨, 순수 산문 약 7,900자)가 length_report v1.7.0 절과 style_log에 적혀 있어 받아들인다. 뒷부속이라 본문 장 균형에는 들어가지 않는다 |
| (b) | 미해소 마커 0건 | **PASS** | `(사실 확인 필요)`·`[리서치 공백]`·`[미완성]`·`[이미지 예정]`·TODO·TBD를 원고 전체에서 grep → **0건** |
| (c) | 사실 미결 해소 | **PASS** | factcheck_log v1.7.0 1차: ❌2(C-3 '네 갈래' 과장, `action_auto`의 뜻)·⚠️2·🕒0. 재확인 라운드: 넷 모두 ✅, 새 ⚠️1(YAML 들여쓰기 과잉 일반화). **원고에서 닫혔는지 직접 확인함:** ❌-1 → L3181 "세 갈래(`auto`·`approve`·`suggest`)와 읽기 범위 밖 거부 … 등록부에 없는 행위는 C-6 실험 2에서" ✅ / ❌-2 → 사건 표 "`auto`·`read` 수준 행위 … (`read` 수준도 이 이름으로 남는다)" + "69건 가운데 22건은 `read` 수준" ✅(직접 집계 22) / ⚠️-1 → "모델이 이미 폐기된 것을 보고 요청하지 않을 수도 있다" ✅ / ⚠️-2 → "점검으로 돌리면 ③에서 이 문장을 남기고 점검 전체가 멈춘다" ✅ / YAML ⚠️ → "실행이 영어 오류로 멈추거나, 멈추지 않고 뜻이 바뀐다" ✅. 의심 식별자(arXiv·URL) 신규 0. 신규 URL은 저장소 1개(B-7과 같은 주소)뿐이다. 보안 규약: 부록 C의 조직 이름은 예제 등록부의 가상 이름을 그대로 인용한 것이다. C-6 실험 4는 실제 조직·고객·개인정보를 넣지 말라고 명시한다 |
| (d) | 용어 통일 + 챕터 간 변주 | **PASS** | '등록부'·'절차서(SOP)'·'사람 개입'·'판정 보류'·'묘비'·'자격 증명'·'실행 런타임'이 본문·상자와 같은 표기다. 풀이가 필요한 말(터미널·Python·git·패키지·pip·API 키·환경 변수·옵션·토큰·YAML·grep·프록시·FTE)은 첫 등장에서 한 번씩 풀었다(plain_language_rules). 상자 다섯의 새 줄은 같은 틀을 일부러 쓴 안내 줄이다. ④만 내용(앞 상자 기록을 환산)을 덧붙였다. 부속 형식이라 tic으로 보지 않는다 |
| (e) | 상호 참조 무결성 | **PASS** | 부록 C 안: "예제 저장소(B-7)"(L3114 절) · "(10장)" 자격 증명 회수 · "10장 상자가 정직하게 적었듯"(L2614) · "8장 자율성 계수의 재료"(L1153·1826) · "2장 상자의 보류 2건" · "질문 9개(4장 상자)" · "7장 상자의 '배정 0건'·'공지 제안 0건'"(L1830) · "(7장)" 되돌릴 수 없는 대외 발송 · "(5장)" 등록부 스위치 · "(10장 체크리스트 ①)"(L2525 ① 공식 폐기 워크플로·승인자) · "8장의 분자·분모" · C-1 표의 상자↔장(①2·②4·③7·④8·⑤10)이 상자 위치와 같다. 상자 다섯의 "부록 C" → L3124. 앞부속 L77·목차 → 부록 C 제목과 같다. 끊긴 참조 0 |
| (f) | 약속 이행 | **PASS** | 매니페스트 description "각 장은 다음 주에 쓸 수 있는 도구를 하나씩 남긴다"를 부록 C가 더 단단하게 한다. 도구 다섯을 독자가 직접 돌려 볼 수 있는 절차가 생겼다. 앞부속 "본문에는 코드가 나오지 않는다"는 여전히 맞다. 새 코드 펜스는 상자 밖이지만 모두 뒷부속 부록 C 안에 있다. 범위·대상 독자는 바뀌지 않았다 |
| (g) | front/back matter 완비·정합 | **PASS** | 판권 "v1.7.0 / 2026-10-10", 본문 상단 판본 줄, 매니페스트 `1.7.0`·`2026-10-10`이 같다. 식별자 `urn:uuid:5cef80ff…` 유지, 라이선스 `CC BY-NC-SA 4.0`, 하네스 v1.11.0. 「둘째, 시점」이 부록 C를 포함하도록 넓혀졌고, 부록 C 서두가 "2026년 10월 10일 기준"을 따로 밝힌다(v1.5.0 BLOCK-1과 같은 종류의 어긋남 없음). C-7 단가에도 "2026년 10월 기준"이 적혀 있다. 목차에 부록 A·B·C. 서문·목차·판권·에필로그(10장 마지막 절)·부록 A·B·C 모두 있음 |

## 평결

# ✅ ACCEPT (sha256 `646b9fca677b109717786e95b70e4a08d473b781713d14d2bfc332c80624f1d3`)

7개 기준 모두 PASS다. v1.7.0 개정판은 Phase 5(EPUB·웹 빌드)로 넘어갈 수 있다. 빌드는 이 sha의 원고로 한다. 아래 관찰 1을 반영하면 sha가 바뀐다. 그때는 그 한 줄과 sha 변화만 다시 확인한다.

## 차단 항목별 조치

- (없음)

## 발간 전 확인 (배포 게이트, 비차단)

### P-1 (권고) 예제 저장소 `main`에 dry_run docstring 정정 커밋 반영 — 담당: 저자/coordinator

- **사실:** 검수 지시는 로컬 예제 폴더가 "ax-system main과 동일"하다고 했지만 정확히는 그렇지 않다. 로컬은 `claude/loving-sagan-1a7tpu` 브랜치 HEAD `460b55b`다. `origin/main`은 `89ee9d0`(`git ls-remote`로 확인)이다. 둘의 차이는 `tests/dry_run.py` docstring 2줄뿐이다(`auto·approve·suggest·미등록` → `auto·approve·suggest)와 읽기 범위 밖 거부` + "미등록은 기본 스크립트에 없다"). 동작은 같다.
- **영향:** 부록 C의 명령·화면 문장은 main 코드에서도 그대로 나온다. 다만 main에서 받은 독자가 `dry_run.py`를 열면 옛 docstring이 "미등록"도 점검한다고 적고 있다. 이것이 C-3의 "등록부에 없는 행위는 C-6 실험 2에서" 문장과 어긋난다(factcheck ❌-1이 지적한 과장이 저장소 쪽에 남아 있는 상태).
- **조치:** 외부 배포 전에 `460b55b`를 main에 병합한다. 원고 수정은 필요 없다.

## 관찰 (판정 대상 아님)

1. **C-6 실험 2 "감사 로그에는 `action_denied`가 남는다"(점검으로 돌릴 때).** 런타임은 실행 중에 `action_denied`를 기록한다. 하지만 C-3이 적었듯 dry_run은 끝나면서 `logs/`를 되돌린다. 복사본 실측에서 점검이 끝난 뒤 `logs/audit.jsonl`의 `action_denied`는 **0건**이었다. 독자가 점검 뒤에 그 줄을 찾으면 찾을 수 없다. 사실이 틀린 것은 아니다(실행 중에는 기록된다). 하지만 따라 하는 절차로 읽으면 오해할 수 있다. editor 선택 사항: 예) "감사 로그에도 `action_denied`가 적힌다(점검이 끝나면 로그는 되돌려진다)". 반영하면 sha가 바뀌므로 그 줄만 재확인한다.
2. **dry_run의 통과 문장과 단언 범위 (원고 밖).** `점검 통과: … 묘비 기록 확인`을 찍기 전의 `assert`는 `status == "retired"`와 `credentials == []`만 확인한다. `tombstone` 존재는 확인하지 않는다. 부록 C는 코드가 찍는 문장을 정확히 인용했으므로 원고 문제는 아니다. 저장소 쪽에서 assert에 `"tombstone" in retired`를 더하면 문장과 검사 범위가 맞는다.
3. **로그 판정과의 대조.** factcheck_log v1.7.0의 ✅ 판정과 이 검수의 직접 세기 결과가 어긋나는 곳은 없다. 관찰 1은 fact-checker가 다루지 않은 지점이다.

## 수락 후 조치 — 2026-10-10 (orchestrator)
- **관찰 1 반영:** C-6 실험 2 문장에 "(점검이 끝나면 로그도 되돌려지므로, 화면에서 확인하자)"를 덧붙여 재조립. 수락본(646b9fca677b) 대비 diff는 이 한 줄뿐. 새 원고 sha256 `770c8ddb092a7ebb8f5a85e89d5d5f52ae817a99ac2ce6c4a6f311fa86418685`. 금지 마커 0. ACCEPT 유지 — 이 sha로 빌드한다.
- **관찰 2 (원고 밖) 반영:** ax-system `tests/dry_run.py`에 묘비(tombstone.reason) assert 추가 — 통과 문장 "묘비 기록 확인"이 실제 검사가 됨(ax-system 브랜치 0526f78, dry_run 통과 확인).
- **P-1:** ax-system 브랜치 `claude/loving-sagan-1a7tpu`의 dry_run.py 커밋 2건(460b55b docstring, 0526f78 assert)을 main에 병합해야 부록 C-3과 저장소가 완전히 맞는다 — 저자 병합 대기.
