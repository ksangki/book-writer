# fact_rules_active — 사실 규율 누적 파일 (fact-checker 전용 기록)

> `devrel-next` · tech-book · 기준 시점 2026-09-25 · 작성 fact-checker (라운드 0, 저술 전 선제 검증)
> **저술가 필독.** 저술 전에 읽고, 파가 끝날 때마다 아래 "실패 패턴 누적"을 다시 확인한다.
> 우선순위: 이 파일 > `02_plan.md` 사실·수치 규율 > `01_reference.md` §6·§7. 이 파일이 원장과 다르면 **이 파일이 맞다**(원 데이터·1차 출처로 다시 확인한 결과다).
> 판정 표기: **쓸 수 있음** / **약화해서**(라벨·조건 필수) / **쓰지 말 것**. 배치(어느 장에 쓰나)는 계획서가 정한다 — 이 파일은 사실 여부만 정한다. 계획서가 금지한 자리는 이 파일이 "쓸 수 있음"이어도 쓰지 않는다.

---

## 1. 미해결 4건 (research-lead 자기 검증 부록) — 해소 결과

| 항목 | 검증 방법 | 결과 | 판정 | 본문에 쓰는 방식 |
|---|---|---|---|---|
| Block "All 12,000 employees ... have access to goose" | Angie Jones 원문 재조회(2025-10-20 게시, 문장 일치) + Block 10-K(FY2024) 대조 | 10-K: **2024-12-31 기준 정규직 11,372명**. 12,000은 작성자의 어림 수치로 Block 공식 인원과 맞지 않는다 | **약화해서** | "Angie Jones에 따르면 전 직원 1만 2천 명이 goose에 접근할 수 있게 됐다(2025년 10월 글)"처럼 **그녀의 문장으로만**. "Block의 직원 1만 2천 명" 같은 회사 사실 단정 금지. Block의 현재 인원 언급 금지 |
| Supabase "last quarter ... same amount of signups as in the last four years" (Thor Schaeff) | DevRelCon NY 2025(2025-07-17~18) 전사본 재조회 — 문장 존재 확인. Supabase 1차 자료 검색 | 발표자 구두 주장. Supabase 1차 확인 불가. 대신 **CEO 1차 발언**을 찾았다(아래 F1) | 4년치 수치는 **약화해서**("발표자에 따르면", 전사본 라벨) 또는 생략. **권장:** 수치가 필요하면 F1을 쓴다 | 두 수치를 한 문장에 겹쳐 쓰지 않는다(규모 주장이 서로 다르다) |
| Stack Overflow 월 질문 수("약 300건"·"월 2.5만 건") | Stack Exchange 공개 API 직접 집계(2026-09-25, 현존 질문 기준) | "약 300건"·"2.5만"은 원 데이터와 불일치 | **쓰지 말 것 — 월 질문 수는 어떤 값도 쓰지 않는다**(team-lead 결정, F2) | SO 감소는 N21·N22 논문으로만 |
| CJ올리브영 DevRel 공고 | career.oliveyoung.com/ko/o/220176 재조회 | **HTTP 404**(2026-09-25). 원문 확보 불가 | **쓰지 말 것** | 계획서대로 전면 미사용 |

> **team-lead 결정 반영(2026-09-25):** SO 월 질문 수 = 계속 금지 / State of DevRel "영향력 증명 60.7%" = 조건부 허용(F3). 계획서 7-3의 "영향력 증명 수치는 어디에도 쓰지 않는다"는 이 결정으로 대체된다.

---

## 2. fact-checker가 새로 확인한 값 (F 목록 — N·E와 같은 지위, 라벨째만)

| # | 값 | 출처·라벨 | 비고 |
|---|---|---|---|
| F1 | "Our sign-up rate just doubled in the past three months because of vibe coding—Bolt, Lovable, Cursor, all those." — Paul Copplestone(Supabase CEO). 같은 기사: 개발자 약 200만 명, DB 350만 개+ | Fortune 2025-04-22 Series D 단독 보도 [언론 인터뷰, CEO 발언] | 4-1에서 Supabase 수치가 필요하면 이것. "가입 속도가 두 배"는 **속도** 주장이다 — "가입자가 두 배"로 바꾸지 않는다 |
| F2 | ~~Stack Overflow 월 신규 질문 재집계값~~ | **team-lead 결정(2026-09-25): 계속 금지.** 집계 방식(현존 질문만·삭제/폐쇄 제외)을 독자가 검증할 수 있게 설명하기 어렵다 | **쓰지 말 것.** SO 감소는 동료 검토 논문 2편(N21 del Rio-Chanona·N22 Burtch)으로만 서술 |
| F3 | "Proving impact with data and metrics (60.7%)" — DevRel 실무자가 꼽은 최대 과제 | State of DevRel 2024 리포트 원문 [설문] | **team-lead 결정(2026-09-25): 허용.** 조건 ① 원문 값 **60.7%** 그대로(61%로 반올림 금지) ② 라벨 **"State of DevRel 2024, n=310, 실무자 설문"** 동반 ③ N4(커리어 경로 없음 61%)와 같은 문단에 두지 않는다(숫자 혼동 방지) |
| F4 | OpenAI 공개 목록에 "Forward Deployed Engineer - Seoul" 1건 | Ashby 공개 API(2026-09-25) [1차 스냅샷] | 6-6 서울 근무지 절에 쓸 수 있다(스냅샷·일반화 금지 라벨) |
| F5 | Mintlify 에이전트 식별 방법: 선언된 클라이언트 이름(GPTBot, ChatGPT-User, ClaudeBot, Claude-User, PerplexityBot, Google-Extended 등) + 기계용 경로(.md·llms.txt·plain text) + 알려진 AI IP/UA 패턴 | Mintlify midyear report 원문 [벤더 방법론 서술] | 4-4에서 쓸 수 있음. 원문의 한계 문장(중개자 식별 불가, 경로 변경만으로 비율 상승, MCP 대화 식별자 없음)을 함께 |

---

## 3. 원장(N·§2)의 틀리거나 오해를 부르는 부분 — 정정

| 원장 위치 | 원장 서술 | 정정 | 판정 |
|---|---|---|---|
| N42·§2 축 5 공고 표 "Replit / Lovable / ElevenLabs / Stripe = FDE 1 / CM·SA / DX Engineer 1 / DevRel 0" | ElevenLabs가 DX Engineer 1건만 있는 것처럼 읽힌다 | 2026-09-25 API 재집계: **ElevenLabs(218건) — FDE 계열 16건 + DX Engineer 1**, **Stripe(695건) — "Forward Deployed" 제목 5건**(FDE Privy, Forward Deployed Security Engineer, Forward Deployed AI Accelerator 2 등), DevRel 제목 0. Replit — FDE 1 확인 | 표를 쓸 때 **ElevenLabs·Stripe의 FDE 계열을 빠뜨리지 말 것**(빠뜨리면 논지에 유리한 방향의 누락이 된다) |
| N42 전체 공고 수 | Anthropic 627 / OpenAI 827 | 같은 날 재조회 628 / 825 — 당일 변동 | 원장 값 사용 가능. 단 "약 630건"·"약 830건"처럼 **어림**으로 쓰거나 "2026-09-25 조회 기준" 라벨 필수 |
| N42 Anthropic | FDE 4 + 매니저 2 + Pre-Sales 1, DevRel 1, Education Lead 1 | **일치**. 추가로 "Staff+ Software Engineer, Developer Experience" 1건(사내 DX 직무로 보임) 존재 | 쓸 수 있음 |
| §1-1·N45 "a lack of role clarity and difficulty in measuring impact" | 결성(2025-08-25) 배경처럼 기술 | 이 문장은 **2024-09-16 결성 의향 발표문**에 있다. 2025-08-25 결성 발표문의 표현은 "uphill battles with perception and clarity of purpose" | 1-4에서 인용할 때 **"2024년 9월 결성 의향을 밝히며"** 로 귀속 |
| N35 Robillard | "응답 80명" (§2는 83명, §7은 83명) | 원 파일: **설문 응답 83명, 유효 80명** | "응답자 83명"으로 쓰고 괄호에 유효 80. "80명" 단독 표기 금지 |
| N40 카카오 설문 라벨 "사내 참여자 ≈100명 설문" | 응답자 약 100명처럼 읽힌다 | 원문(tech.kakao.com/posts/762, 2025-09-19): 시범 참여 "100여명·30여개 조직·40여개 과제" 확인, 68.4/31.6/0% 확인. **설문 응답 수는 공개되지 않았다** | 라벨을 **"카카오 자체 운영 시범(참여 100여 명)의 3개월 차 사내 설문, 응답 수 미공개"** 로 |
| §2 축 6 Salma "The forums are dead, the new Discord is quiet." | "익명 동료 재인용(확인 필요)" | 원문 확인: **Salma 본인의 문장**(2026-07-02 글) | Salma 인용으로 쓸 수 있음 |
| §2 축 5 Supabase 공고 "350,000+ developers" | 공고 내 자기 서술 | 공고 문구는 맞다. 그러나 CEO가 2025-04에 "약 200만 명"이라 말했다(F1) — 공고 문구가 낡았거나 다른 모수 | **쓰지 말 것**(Supabase 규모 수치로 오해됨) |
| §2 축 5 Rizèl Scarlett "작성 당시 Block goose DevRel 리드" | goose 팀 리드처럼 읽힌다 | 원문(dev.to 2025-09-16) 본인 서술: **"I was promoted to lead Open Source Developer Relations at Block"**. goose 저장소에 직접 기여(CLI·데스크톱 앱 수정)는 원문에 있다 | "Block에서 오픈소스 DevRel을 이끌던 시기" — "goose 팀을 이끌던" 금지 |
| Tailwind 날짜 | "2026-01-07" | 두 댓글: "less traffic to our docs" = **2026-01-06**(UTC), "75% ... lost their jobs here yesterday"·"down about 40%"·"down close to 80%" = **2026-01-07 03:55 UTC 한 댓글** | 5장 오프닝은 "2026년 1월 7일" 가능(UTC). "yesterday"를 풀어 "1월 6일에 해고"라 쓰지 말 것(시간대 모호) |

---

## 4. 확인 완료 — 그대로 쓸 수 있음 (원문·1차 대조)

### 4-1. 계획서 E1~E6

| # | 판정 | 근거 |
|---|---|---|
| E1 Hasan 2026 +5.85%p / 단계 +67.46% / 퇴행 16.67% / 목적 불명 56% | **쓸 수 있음**(프리프린트 라벨) | papers.md P-19 abstract 수치 일치, arXiv:2602.14878 실재(제목 "MCP Tool Descriptions Are Smelly!") |
| E2 LF DRF Persona Library 24 / Tools Catalog 36 | **쓸 수 있음** + 🕒 | LF 결성 발표문(2025-08-25, Amsterdam OSS Europe) "24 definitions / 36 definitions" 확인. **"결성 시점(2025년 8월) 기준"** 명기 필수(이후 늘었을 수 있다) |
| E3 카카오 1K — 1시간(실개발 35분)·MVP 99개·비개발자 참가 허용 | **쓸 수 있음**(회사 발표) | tech.kakao.com/posts/784 원문 확인 |
| E4 MCP Player 10 — 10명·총 2,100만 원 | **쓸 수 있음**(회사 발표) | web.md W-8-2(카카오 발표) — 원문 재조회는 안 함, 원 파일 일치 |
| E5 Windows Phone SO 질문 46,030개 | **쓸 수 있음** | papers.md P-25 표본 기술 일치 |
| E6 프런티어 밖 84.5% → 60%/70.6% | **쓸 수 있음**, **N29 "약 19%p"와 함께만** | papers.md P-35 본문 대조 일치. "19%"(퍼센트) 금지, "19%p" |

### 4-2. 1차 공고 원문 (Greenhouse·Ashby 공개 API, 2026-09-25 전문 조회 — 문자열 일치 확인)

- Anthropic Developer Relations(updated 2026-08-21): "help developers discover, onboard, and get the most out of Claude Code, Claude Tag, and future developer products" / "Help define what world-class AI developer relations looks like in this emerging field" / "from individual hobbyists to enterprise engineering teams" / "Build frameworks and mechanisms for measuring developer success" / "Act as an advocate for developer needs at Anthropic, translating developer feedback into concrete product and content initiatives" — **전부 일치**.
- N41 연봉 "$290,000 — $435,000 USD" **일치**, 공고가 "the range includes both the sales commissions/sales bonuses target and annual base salary"라고 명시 → **OTE 라벨 필수**, "기본급"으로 쓰지 말 것.
- Developer Education Lead(updated 2026-09-21): 세 인용 모두 일치. (참고: 이 공고의 연봉은 $290,000 — $365,000. 쓰지 않는 것을 권장)
- FDE(updated 2026-08-21): 세 인용 일치. Copywriter, Developer(updated 2026-09-16): 두 인용 일치.
- Vercel DevRel Engineer, Agentic Infrastructure(updated 2026-09-17): 인용 전부 일치. "Applications without one will not be considered."의 "one" = **"a link to something you made that taught developers something, a talk, a repo, a post, a video"**. 보고 라인 "Head of AI Infrastructure" 일치. 공고에 "people and agents"와 "agents and people"이 둘 다 나온다.
- Supabase DevRel Engineer(published 2026-08-21): "Our users are builders, startup founders, weekend hackers, and engineers scaling to millions of users." 일치. 공고 3건(SF·NY·런던) 일치.
- OpenAI Developer Experience Engineer, Cyber(2026-09-11): 두 인용 일치.
- Cloudflare VoidZero DevRel Engineer(updated 2026-09-15): "someone who identifies as a builder, teacher, mentor, and communicator" 일치. 근무지 후보 "Singapore, Sydney, Tokyo, Seoul, Lisbon, or London" — 서울 포함 확인.
- Anthropic 서울: "Applied AI Architect"·"Manager, Applied AI Architect" 서울 근무지 확인. Applied AI 제목 공고 총 38건.

### 4-3. 기타 원문 확인

- Angie Jones(2025-10-20): "plot twist: we're not dead. We're standing on the biggest stage of our careers." / "Guess who our CEO asked to lead this? DevRel." / "We treated them like any other community of builders." / "We help them move from fear to curiosity." / "They want to see the full, messy, real process." — 일치.
- Salma Alam-Naylor(2026-07-02, 페이지 time 태그 확인): 제목·섹션 "AI is killing developer education"·"If DevRel is to survive, I think it will need to look entirely different from how it functioned during the last ten years."·"made redundant in 2023 from a DevRel role at a company that was moving away from a community-centred approach to an enterprise-based strategy"·"People aren't seeking information in the ways we once knew; The Internet and its communities have fragmented." — 일치. **주의:** 글 부제가 "why I'm not telling you what's next"다 — 새 회사명을 추정해 쓰지 말 것. "Staff Engineer"는 프로필 문구로만 확인.
- Tailwind PR #2388: 세 인용 원문 일치(§3 날짜 주의). PR 자체는 2025-11-18 제3자(quantizor)가 연 **llms.txt 엔드포인트 추가 PR**이다 — "Tailwind가 연 PR"이라 쓰지 말 것.
- Anthropic Claude Code $1B: 게시 **2025-12-03**, "just six months after becoming available to the public, it reached $1 billion in run-rate revenue" 일치(GA 2025-05 → 6개월 산술 맞음).
- 카카오 Sue: 697(2025-04-22) "다르게 표현하자면, 저는 비개발자입니다." / MVK 원어는 **"최소한의 필수 지식(Minimum Viable Knowledge)"** / "기다리는 것이 배우는 것보다 빠르다" 일치. 700(2025-04-24) "필요한 도구를 찾는 것보다 내가 직접 만들어서 쓰는 것이 더 빠르다" 일치. 저자 소개 "DevRel 담당자 Sue" 확인. 762: "원숭이 꽃신"·"숫자로 보여드리는 것 이상의 실체가 필요했습니다. 그것은 바로 개발자들의 실제 사례가 모이는 것"·"'코더'에서 ... '코치'까지 확장" 일치. 783(2025-10-30): 1·2차 실험, "일하는 방식과 조직문화를 함께 바꾸는 여정" 일치.
- LF DRF: 결성 2025-08-25 Amsterdam(OSS Europe), 미션 문장 일치. 의향 2024-09-16(Vienna).
- Ibrahim & Zaki arXiv:2609.12447 — **실재**(2026-09-11 제출, 제목 "Informational Help-Seeking on Reddit Did Not Decline After ChatGPT"), 3.4%·"Humans still ask humans for help" 일치. 프리프린트 라벨 필수.
- arXiv ID 22건(원장 §8 논문 목록의 2023~2026 프리프린트 전부) arXiv API 일괄 조회 — **전부 실재, 제목·제1저자 일치, 미래 YYMM 없음.**
- State of DevRel 2024: 14.6%(2023 15.1%), 27/18.1/22.1%, 중위 기본급 $150,000(2023 $175,000, -14.3%), 커리어 경로 없음 61%(2023 54%), 33개국, AI 미사용 21.8% — 리포트 원문 일치.

### 4-4. 날짜 산술 (계획서 요구 항목)

- 4-2 "15개월": llms.txt 2024-09-03 → AAIF 2025-12-09 = **15개월 6일** — "15개월" 맞음. (MCP 발표 2024-11-25부터 세면 12개월 남짓 — 기점을 바꾸면 숫자도 바꾼다)
- Claude Code "6개월 만에": 2025-05 GA → 2025-11 달성 → 2025-12-03 발표. 맞음.
- Octoverse 2025 "신규 3,600만+"의 기간: 2024-09~2025-08(12개월).
- Rizèl Scarlett 글: **2025-09-16**(2026 아님).

---

## 5. 쓰지 말 것 (원장 §7 + 라운드 0 추가)

원장 §7 전 항목 유지. 라운드 0 추가:
- "Stack Overflow 월 질문 약 300건" / "월 2.5만 건" — 원 데이터와 불일치.
- "Block 직원 1만 2천 명"(회사 사실로) — 10-K와 불일치.
- Supabase 공고의 "350,000+ developers"를 Supabase 규모로.
- CJ올리브영 공고 — 404.
- 영향력 증명 **"61%"** — 원문은 60.7%. 60.7%는 F3 조건부 허용.
- Stack Overflow 월 질문 수 — 어떤 값이든(재집계값 포함) 금지.
- LF DRF "lack of role clarity"를 **2025-08 결성문** 인용으로 귀속.

---

## 6. 실패 패턴 누적 (파마다 갱신)

### 라운드 0 (저술 전)에서 본 패턴
1. **요약 수치의 전파:** 2차 보도·댓글의 수치(SO 월 300건)가 원 데이터와 한 자릿수 이상 틀렸다. 수치는 원 데이터에서 다시 센다.
2. **어림수의 사실화:** 1인칭 글의 어림수(Block 12,000)가 공시 수치와 다르다. 개인 글의 숫자는 그 사람의 문장으로만 옮긴다.
3. **요약표의 누락 편향:** 공고 스냅샷 요약표가 ElevenLabs·Stripe의 FDE 공고를 빠뜨렸다. 표를 옮길 때 논지에 유리한 쪽으로 줄어든 항목이 없는지 본다.
4. **인용의 문서 귀속 혼동:** 같은 기관의 두 발표문(LF DRF 2024 의향 / 2025 결성) 사이에서 인용 출처가 섞였다. 인용마다 "어느 문서, 어느 날짜"를 붙인다.
5. **라벨의 과장:** "참여자 100여 명" 프로그램이 "100명 설문"으로 바뀌었다. 표본 라벨은 원문이 밝힌 것까지만.

### 1파 (1·2·4·7장 판정)에서 본 패턴
6. **근거 없는 평판 수식어:** "DevRel을 잘하는 회사로 자주 거론되던"(Twilio)처럼 회사·인물에 붙이는 평판 수식어는 출처가 없으면 쓰지 않는다. 평판이 필요하면 원장에 있는 사실(예: 미션이 인용된 사례)로 대신한다.
7. **목소리의 진단을 사실로 격상:** 여러 인용이 가리키는 진단을 저자 문장으로 요약하면서 "먼저 흔들린 것은 ~였다"처럼 데이터가 필요한 사실 단정으로 바꾸지 않는다. "이 목소리들이 공통으로 가리키는 것은"처럼 귀속을 남긴다.
8. **상황 가정 속 수량어:** 실제 일화를 독자 자리로 옮긴 가정 장면에서도 "대부분"·"모두" 같은 수량어는 일화의 사실 범위를 넘으면 안 된다.
9. **직함은 본인 서술 그대로:** 인물의 당시 직함·소속은 원장 요약이 아니라 본인 글의 표현("lead Open Source Developer Relations at Block")을 따른다.
10. **최상급 "처음으로":** "처음으로"·"유일한"·"가장" 같은 최상급은 근거가 없으면 빼고, 책의 다른 장 논지(3장 "새 이야기가 아니다")와 부딪히지 않는지 본다.
11. **따옴표 안의 변형:** 직접 인용 안에서 괄호·단어를 말없이 빼지 않는다. 줄이려면 줄임표를 쓰거나 간접 인용으로 바꾼다.

### 2파 (3·5·6·8·9·10장 판정)에서 본 패턴
12. **부분 인용의 기울기:** 한 문장의 앞 절("개발자 수요는 줄 것 같은데")을 빼고 뒤 절만 옮기면 원래 말이 한쪽으로 기운다. 조건절·양보절은 함께 옮긴다.
13. **해석의 당사자 귀속:** "그의 설명을 따라가면"이라고 쓴 뒤 당사자가 말하지 않은 기제를 붙이지 않는다. 저자 해석은 저자 해석으로 표시한다.
14. **후일담의 과잉 결론:** 후속 사건(후원 발표)을 "위기는 일단락됐다" 같은 결과 판정으로 바꾸지 않는다. 일어난 사건까지만 쓴다.
15. **표의 분류 규칙과 내용의 일치:** 본문이 "나머지는 넷째 열로 돌렸다"처럼 규칙을 밝혔다면 그 규칙에 해당하는 항목을 모두 넣는다. 제목 키워드로 셌다고 했으면 셈에 쓴 키워드도 정확히 적는다('Developer Relations' vs 'DevRel').
16. **"같은 토론" 귀속:** 댓글을 "같은 토론장에서"로 이을 때는 실제로 같은 스레드인지 원 파일의 URL·item 번호로 확인한다.
17. **상대 날짜의 어림:** "1년 전"·"반년 뒤" 같은 상대 표현은 원문 날짜로 계산한다("Last May" → 발표 10개월 전). 원문이 날짜를 주면 날짜를 쓴다.
