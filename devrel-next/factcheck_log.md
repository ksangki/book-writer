# factcheck_log — devrel-next

> tech-book · 기준 시점 2026-09-25 · 기록자 fact-checker(단독 작성) · 판정 라벨 ✅ 확인됨 / ❌ 정정 필요 / ⚠️ 출처 없음 / 🕒 신선도 경고
> 장별 섹션 `## {NN}장`에 라운드마다 즉시 append한다.

## 00 라운드 0 — 저술 전 선제 검증 (2026-09-25)

- 산출: `fact_rules_active.md` (쓸 수 있음/약화해서/쓰지 말 것 표)
- 미해결 4건: Block 12,000 → 약화(10-K 2024-12-31 11,372명과 불일치, Angie Jones 발언으로만) / Supabase 4년치 가입 → 약화 또는 생략, 대체 F1(Fortune 2025-04-22 CEO "sign-up rate just doubled") / SO 월 질문 수 → 2차 수치 ❌, Stack Exchange API 재집계값 F2 / CJ올리브영 → 404, 사용 금지
- E1~E6 전부 원 파일·원문 일치(E2는 "2025-08 결성 시점 기준" 🕒)
- 원장 정정: N42 ElevenLabs(FDE 16)·Stripe(FDE 5) 누락, LF "lack of role clarity"는 2024-09-16 의향문 귀속, Robillard 83명(유효 80), N40 설문 응답 수 미공개, Salma "forums are dead"는 본인 문장, Supabase 공고 "350,000+" 사용 금지, State of DevRel "proving impact" = 60.7%(1차 확인)
- 공고 인용(Anthropic 4·Vercel·Supabase·OpenAI·Cloudflare) Greenhouse/Ashby API 전문 대조 전부 일치
- arXiv ID 22건 실재·제목·저자 일치, 미래 YYMM 없음

- team-lead 결정 반영(2026-09-25): F2(SO 월 질문 수) 계속 금지, F3(영향력 증명 60.7%) 조건부 허용 — 60.7% 그대로·"State of DevRel 2024, n=310, 실무자 설문" 라벨·N4와 다른 문단


## 01장

### 라운드 1 (2026-09-25, 대상 chapters/01_draft.md style R2 합의본, wc -m 10375)
**❌ 정정 필요:** 없음

**⚠️ 출처 없음 (2)**
- L37 "Twilio는 ... DevRel을 잘하는 회사로 자주 거론되던 곳이라 상징성이 컸다" — 레퍼런스·research 어디에도 근거가 없다(W-2-7은 감원 비율만). → 문장 삭제, 또는 근거가 있는 쪽으로 약화: "2장에서 볼 DevRel 정의에 미션이 인용될 만큼 개발자를 앞세워온 회사라" 정도(W-1-3 Leggetter가 Twilio 미션을 인용).
- L76 "2023~2024년의 감원기에 먼저 흔들린 것은, 기여를 숫자로 설명하지 못한 자리였다" — 어느 자리가 먼저 잘렸는지를 보여주는 데이터가 없다(State of DevRel은 직무별 해고 순서를 다루지 않는다). 앞의 목소리들(Casey·Briggs·Salma·r/devrel)의 공통 진단으로 귀속해 약화: "이 목소리들이 공통으로 가리키는 것은, 먼저 흔들린 자리가 기여를 숫자로 설명하지 못한 자리였다는 진단이다."

**🕒 신선도 경고:** 없음

**✅ 확인됨**
- Salma 글 제목·날짜(2026-07-02, 페이지 time 태그)·Bluesky 인사(2026-07-03 "I'm leaving DevRel, and I wrote a little bit about why.")·소제목·"If DevRel is to survive..."·"made redundant in 2023 ..."·"I have — all too often — ..."·"The forums are dead, the new Discord is quiet."(본인 문장)·"long game"·"most likely the 'wrong' success"·"a bit of a cry for help"·"traditional methods" 청중 문장 — 원문 대조(whitep4nth3r.com), Staff Engineer는 프로필 문구로만(새 회사명 없음)
- HN 토론 2026-07-03: zulux "vague connection, curated vulnerability, or coordinating other coordinators", fragmede 반박이 zulux 댓글의 **직접 답글**(HN API로 부모 id 확인) — "바로 아래" 맞음
- David Neal 2023-07-25 "My role has been eliminated"·creative content creator — C-9-2 / Raymond Camden 2026-05-27 Webflow·목록·"speak Developer" — C-5-2
- State of DevRel 2024(2024-09-10, 33개국, 유효 310): 14.6%·27/18.1/22.1%·$150,000(2023 $175,000) — 리포트 원문
- Common Room 2023(2023-08-31, n=136): 73.9% 원문 문장·26.1% 팀 단위·67.1% — W-2-6
- Google 2023-01 약 6%·1만 2천 명·증언 속 developer relations / Twilio 11%·약 17%·약 5% — W-2-7 / "DevRel 팀 전원 해고" 1차 미확인 고지 준수 / 2025판 부재 고지
- 네 이야기 표: swyx ZIRP(2024-07)·Casey 제목·날짜(2024-07-17)·Briggs 제목·날짜(2024-12-10)·swyx "DevRel Is -Unbelievably- Back"(2025-10) 인용 모두 원 파일 일치
- Casey "2022년 연준 금리 인상" — 원문 "Then we got into 2022 and the world changed with 7 Fed rate hikes making company valuations crater" 확인(caseysoftware.com), 처방 "Eliminate DevRel ... it's a bad approach"(구조 변경) 확인, "If Marketing can't measure ..."·"I did X ..." 일치
- Briggs "money printer"·"neither fish nor fowl"·"Measurability"·"The days of vague metrics ..."·Tailscale Sales Engineer — C-2-3·W-2-3
- swyx "out loud"·과잉에서 배울 것·"Bottom-Up Developer Adoption"·검색량 과장 단서 — W-2-1, C-2-4. "1년여 뒤"(2024-07 → 2025-10) 맞음
- Reddington 2026-03-11·Warwick MBA·13명 중 2명(약 15%)·"의견과 일화" — W-1-8
- F3 60.7%: 라벨 "State of DevRel 2024(n=310, 실무자 설문)" 준수, N4와 다른 장 — team-lead 조건 충족
- LF DRF 2024-09-16 의향 / 2025-08-25 Amsterdam OSS Europe 결성 / "lack of role clarity ..." 2024-09 의향문 귀속 / 미션 "a driver of business value" — LF 발표문 두 건 원문
- r/devrel Daria-Dovzhikova 2026-09-14 인용 전문 일치 — C-2-5

총평: 수치·인용·날짜 모두 원문과 맞는다. 근거 없는 평가 문장 두 곳만 약화하면 통과.

### 라운드 2 (2026-09-25, 01_final.md, wc -m 10418) — 반영 확인
- ✅ L37 Twilio 평판 수식어 → "2장에서 볼 DevRel 정의에 미션이 인용될 만큼 개발자를 앞세워온 회사"(W-1-3 근거)
- ✅ L76 목소리들의 진단으로 귀속
- **01장 사실 검증 통과.** 미해소 없음.

## 04장

### 사전 확인 (style-guardian 경고 대응, 2026-09-25, 04_draft.md L79)
- ✅ "GPTBot, ClaudeBot, PerplexityBot 같은 알려진 AI 클라이언트 이름" + "마크다운이나 llms.txt처럼 기계가 주로 찾는 경로" — Mintlify 원문(state-of-docs-traffic) 방법론에 그대로 있다: "GPTBot, ChatGPT-User, ClaudeBot, Claude-User, PerplexityBot, Google-Extended, and other declared sources", 경로 기준 ".md·llms.txt·plain text". Mintlify 방법론으로 읽혀도 사실이다. 레퍼런스에 없던 항목이므로 fact_rules F5로 등재. 원문 한계 문장("Known client signatures cannot prove whether a request originated in a product's built-in search, an intermediary...")도 L75 서술과 일치. 정식 판정은 style 합의 후 장 전체 라운드에서.


### 라운드 1 (2026-09-25, 대상 chapters/04_draft.md style R2 합의본, wc -m 13423)
**❌ 정정 필요:** 없음

**⚠️ 출처 없음 (1)**
- L3 "그들 **대부분**은 AI로 앱을 만들어주는 서비스를 거쳐 들어왔다" — L9에서 이 장면을 Schaeff 일화를 옮긴 것이라 밝히므로 일화의 사실 범위를 넘으면 안 된다. 전사본에는 비율 주장이 없다(가입 규모 주장만 있고 그것은 발표자 수치로 L13에서 이미 보류). → "그들 상당수는" 또는 "새 사용자를 따라가 보면 AI로 앱을 만들어주는 서비스가 보인다" 정도로.

**🕒 신선도 경고:** 없음 (Mintlify 2026-07·Stripe "2026년 9월 시점"·llms.txt "2026년 9월 시점 제안" 명기)

**✅ 확인됨**
- Thor Schaeff: DevRelCon New York 2025(2025-07-17~18), 발표 "DX for Humans and Machines", Stripe·Supabase 출신·발표 당시 ElevenLabs DX, "without ever talking to us", 사전에 추세를 몰랐다("didn't realise that beforehand"), "use Supabase", "developer experience for machines", "Hey, actually now machines are writing the code", 오픈소스·Postgres 30년+ 가설 — 전사본(developerrelations.com) 재조회 + C-5-1
- F1 Copplestone(Fortune 2025-04-22) 인용·"가입 속도" 표현 정확, 발표자 수치와 분리 — 원문 확인
- 3장 콜백(비개발 게임 개발자 Supabase) — 03_draft.md 마지막 절 L137~139에 실재
- Karlsson 2026-04-20 "It's not shopping ..." — C-6-4
- 타임라인: llms.txt 2024-09-03(제안문 원문 인용 일치)·MCP 2024-11-25(초기 도입 Block·Apollo, 개발 도구 Zed·Replit·Codeium·Sourcegraph)·"두 달여 뒤"·Biilmann 2025-01-28·GitHub MCP 2025-04-04·Cloudflare 2025-04-07 "업계 최초"(자기 주장 라벨)·"사흘 뒤" 산술·Vercel 2025-08-06 읽기 전용·매 연결 OAuth 동의·카카오 PlayMCP 2025-08 "국내 최초 MCP 실험 공간"(자기 소개 라벨)·AAIF 2025-12-09·9,700만+/1만+(주체 발표 라벨)·"15개월 남짓" — W-4-1~4-6, W-8-2, fact_rules §4-4
- Biilmann 정의·Norman 1993/Jeremiah Lee 2011 계보(Biilmann의 서술로 귀속)·"risk being replaced"·X 후속 "Six months after I coined Agent Experience"(= "반년쯤 뒤" 본인 표현)·"Deploy first, claim later" — W-4-6
- Zeno Rocha "AX doesn't replace DX, it extends it."(Netlify AX 페이지) / Lawson The New Stack 2026-06-06 요약 문장·오류 메시지·빌드 출력·"Every human assumption ..." — W-4-6, C-9-1
- SWE-agent NeurIPS 2024 인용 전문 — P-18
- Mintlify 2026-07-29 보고서 제목·66%·2억 1,300만/1억 500만·15.2%·"네 배 넘게"(66/15.2=4.3) 산술·단위·방법론·한계·사이트 수 비공개·F5 식별 방법 — 원문 재조회
- Stripe building-with-ai 첫 줄·`.md`·mcp.stripe.com OAuth·로컬 MCP·Agent Toolkit(Python·TS)·`/.well-known/skills/index.json`·URL 패턴(자리표시자 표기 적절)·Apideck 2026-02-23 2차 인용 라벨 — W-4-4
- Google Cloud 2026-08-04 Remigiusz Samborski(Lead Developer Relations Engineer)·두 인용 — W-5-6
- Hsieh 2023(프리프린트)·수백 API 과제 결과·인용 / Hasan 2026 103개·856개·97.1%·56%·+5.85%p·+67.46%·단위 고지·"rely on natural-language tool descriptions" 취지 / Gloaguen 2026 비용 20%+·저장소 개요 무익·비표준 관행 유용 / Chatlatanagulchai 2,303개·14.8% / Hasan v5(2026-04) 1,899개·7.2%·5.5% / Robillard 2009 83명(유효 80)·78% — P-17, P-19, P-20, P-22, P-23, P-30, arXiv 실재 확인
- 반론 박스: Mueller 2025 "FWIW no AI system currently uses llms.txt."·keywords 메타 태그(언론 인용 라벨) / HermanMartinus 2026-06 약 8만 블로그·"not requested by anything"·일반 페이지 aggressive scraping / umairnadeem123 2026-03-01 "MCP adoption is a marketing signal not a technical one."(앞 구절 "AI first"는 원글 인용을 받아 동의한 것 — 서술 허용 범위) — W-4-2, C-6-2, C-6-6
- 재반박: 0123456789ABCDE(주요 회사 게시)·nickserv GitBook·m4tthumphrey "게시와 소비"·solumos "Accept: text/markdown ... more agreed upon standard" / nvdnadj92 디자인 시스템 문서·tartieret 비개발 업무 도구 MCP(2026-03-02) — C-6-2, C-6-6
- xena 2026-09-18 ax-check Show HN 인용 전문·2024-07-08 "recently broken into DevRel ... really concerned"·"2년 사이" 산술 — C-9-1, C-2-3

총평: 사실 밀도가 높은 장인데 원문과 어긋난 곳이 없다. 오프닝 가정의 "대부분"만 약화하면 통과.

### 라운드 2 (2026-09-25, 04_final.md, wc -m 13427) — 반영 확인
- ✅ L3 "그들 가운데 상당수는"
- **04장 사실 검증 통과.** 미해소 없음.

## 02장

### 라운드 1 (2026-09-25, 대상 chapters/02_final.md 후보본, wc -m 11204)
**❌ 정정 필요 (1, 경미)**
- L41 kt cloud 인용 — 따옴표 안에서 원문의 괄호 풀이를 말없이 뺐다. 원문(tech.ktcloud.com, 2024-11-04, community.md C-8-3): "PR(Public Relations)이 일반인에게 기업을 알리는 활동이라면, DR(Developer Relations)은 개발자에게 기업을 알리는 활동". → 원문대로 복원하거나 따옴표를 풀고 간접 인용으로.

**⚠️ 출처 없음 (1)**
- L112 "2020년대 중반, 오랫동안 제자리에 있던 D가 **처음으로** 크게 흔들리기 시작했다" — "처음으로"는 근거 없는 최상급이다. 이 책 3장 계획(3-1 "새 이야기가 아니다" — Ko et al. 2011, Scaffidi 2005의 최종 사용자 프로그래머)과도 부딪힌다. → "처음으로"를 빼고 "크게 흔들리기 시작했다" 정도로.

**✅ 확인됨**
- Kawasaki 위키 요약 인용·"Mike Boich started evangelism and hired me"(부분 인용) — web.md W-1-1
- Parker·Van Alstyne·Jiang MISQ 41(1) 2017 두 인용·모형 요지 — papers.md P-33
- Microsoft DPE(Redmond Channel Partner 2012-10-04)·Cloud Developer Advocate·Soshnikov 2006 Academic Developer Evangelist·"10년 넘게" — W-1-2. Ramji 미귀속 준수
- Google·Twilio 미션 인용(Leggetter 2016-02-03) — W-1-3 원문 일치
- Fontão et al. JSEP 35(5) 2023(온라인 2021-10)·DevGo·keystone — P-24
- Massanori et al. SBES 2020 정의 인용, 「Death of a Software Ecosystem」, Symbian 2012·Firefox OS 2016·Windows Phone 2017, SO 질문 46,030개(E5), 정의와 붕괴 사례가 같은 논문이라는 서술 — P-25
- Thengvall 한국어판 2022(조은옥 옮김, 한빛미디어) — W-1-4
- Tushman ASQ 1977 제목·개념 일반 서술(직접 인용 없음, 확장은 "DevRel에 적용하면"으로 표시) — P-40
- AAARRRP DevRelCon London 2016·회사 유형별 목표 — W-1-3 / DRL 2019-12·영업 지표 반대 — W-1-5
- Orbit Model 2019-11·Gravity = Love × Reach·Dzielak "Communities aren't funnels"·Postman 인수 발표 2024-04-11·5-31/7-11(2차 라벨 명기) — W-1-6
- Lewko & Parton 2021 5단계·"Is this of use to me?" — W-1-7
- Fagerholm & Münch ICSSP 2012 정의·외부 개발자 포함 — P-26
- DevEx(Noda·Storey·Forsgren·Greiler, Queue 2023)·SPACE(Forsgren 외, Queue 2021) 잡지 기고 라벨 — P-27·P-28
- Goggins et al. 2021 CHAOSS 인용 — P-46

**🕒 신선도 경고:** 없음 (역사 서술 장, 연도 명기 충분)

총평: 수치·인용 귀속이 원장과 잘 맞는다. 경미한 두 건만 고치면 통과. ❌는 반영 확인 후 통과 처리한다.

### 라운드 2 (2026-09-25, 02_final.md, wc -m 11238) — 반영 확인
- ✅ L41 kt cloud 인용 원문 복원 확인
- ✅ L112 "처음으로" 삭제 확인
- **02장 사실 검증 통과.** 미해소 없음.


## 07장

### 라운드 1 (2026-09-25, 대상 chapters/07_draft.md style R2 합의본, wc -m 12028)
**❌ 정정 필요:** 없음

**⚠️ 출처 없음 (1)**
- L43 "Rizèl Scarlett는 2025년 9월 16일, **Block의 goose 팀에서 DevRel을 이끌던** 시기에 쓴 글에서" — 원문(dev.to, 2025-09-16) 본인 서술은 "I was promoted to lead Open Source Developer Relations at Block"이다. goose "팀"을 이끌었다는 근거는 없다(goose 저장소에 직접 기여한 것은 원문에 있음). → "Block에서 오픈소스 DevRel을 이끌던 시기"로. (원장 §2 축 5의 "Block goose DevRel 리드" 표기도 이 기준으로 fact_rules에 정정 등재)

**🕒 신선도 경고:** 없음 (공고 표 캡션 "2026-09-25 공개 목록 기준 예시", E2 "2025년 8월 기준" 명기)

**✅ 확인됨**
- 7-1 표 문구 7개 전부 공고 원문 문자열 일치(Greenhouse·Ashby API 2026-09-25 전문): Anthropic DevRel "translating developer feedback into concrete product and content initiatives"·"Act as an advocate for developer needs at Anthropic" / Anthropic FDE "contribute insights back to our Product and Engineering teams" / Vercel "include a link to something you made that taught developers something"·"hit the rough edges first and make sure they get fixed before launch"·"Build agents and applications on AI Gateway and Sandbox before they ship" / OpenAI DX Engineer Cyber "inspiring demos, developer tools, sample applications, and technical content"
- FDE "Identify and codify repeatable deployment patterns and contribute insights back ..."·"MCP servers, sub-agents, and agent skills" — 원문 일치
- Cloudflare VoidZero "someone who identifies as a builder, teacher, mentor, and communicator" / Supabase "You're equally comfortable writing a video script and TypeScript" — 원문 일치
- Vercel 지원서 결과물 링크 필수·Head of AI Infrastructure(제품 조직) / Anthropic "Build frameworks and mechanisms for measuring developer success" — 원문 일치
- Karlsson 2026-04-20 Dev Zero 인용 전문 — C-6-4
- Dewan Ahmed 2026-08-11 갱신 "Technical credibility ..."·"You are hired to remove a cost or a risk." — W-5-6
- Rizèl 2025-09-16: "Even though I was a leader, I continued to build."·"we need more content" 취지·goose 저장소 CLI·데스크톱 앱 수정·"genuine collaborators"·"Bringing internal engineers into community chats so they can see real-world edge cases"·"forty-thousand-dollar networking breakfasts ..." — dev.to 원문 + C-5-3, W-5-6
- State of DevRel 2024 N4 61% "no defined career path" 항목명 명기·22.1% 재편·표본 라벨 — 원문
- LF DRF: 2025-08 결성·Persona Library 24·Tools Catalog 36(결성 시점 기준 명기)·Events Directory·2024-09 의향문 귀속·Stacey Kruczek 인용(결성 발표 인용 구절) / AAIF 2025-12 MCP·AGENTS.md / "넉 달 사이"(08-25 → 12-09, 3개월 반) 산술 허용 범위 — W-2-8, LF 원문
- 국내: 공백 고지 / 우아한형제들 공고 2022 추정·"기술 조직 산하 Tech HR 실"·"대내외 개발자들과의 관계를 바탕으로 ... 기술 조직을 알리는"·2차 게재본·현재 미확인 / E4 MCP Player 10(회사 발표) / DevRel KR X 계정 / Thengvall 한국어판 2022-06·국내 인터뷰 추가 — W-8-2, W-8-4, W-1-4. CJ올리브영 미사용 준수
- 6장 이동 기록 콜백(SE·Staff Engineer·MTS·코딩 도구 교육) — 원장 §2 축 5 표

총평: 공고 문구가 전부 원문 문자열과 맞는다. Rizèl 직함 한 곳만 원문 표현으로 바꾸면 통과.

### 라운드 2 (2026-09-25, 07_final.md, wc -m 12024) — 반영 확인
- ✅ L43 "Block에서 오픈소스 DevRel을 이끌던 시기"
- **07장 사실 검증 통과.** 미해소 없음.

## 03장

### 라운드 1 (2026-09-25, 대상 chapters/03_draft.md style 합의본, wc -m 13369)
**❌ 정정 필요 (1, 경미)**
- L141 spilist2 댓글 부분 인용 — 원문 한 문장의 앞 절을 빼서 뜻이 한쪽으로 기운다. 원문(community.md C-8-4, GeekNews 2025-03-25): "저는 개별 기업에서는 개발자 수요는 어찌됐든 줄어들 것 같은데, '개발 업무'를 필요로 하는 기업 또는 그에 준하는 사업자/개인의 수는 훨씬 더 늘어날 것이니 개발자가 할 일은 여전히 많다고 생각했습니다." → 앞 절("개별 기업의 개발자 수요는 줄어들 것 같다")을 함께 옮기거나 서술에 반영.

**⚠️ 출처 없음:** 없음  **🕒 신선도 경고:** 없음

**✅ 확인됨**
- Scaffidi et al. VL/HCC 2005: 2012 미국 직장 추정·Census·BLS·자칭 1,300만+ vs 300만 미만·"네 배가 넘는다"(13/3=4.3, 300만 미만이므로 그 이상) 산술·Boehm 1995 "5,500만" 예측 구분 — P-13 본문
- Ko et al. 2011 초록 인용 전문·EUSE 서베이 내용(위험·보상·자기효능감·SE 원칙 교육)·"15년 전"·"ChatGPT 10년도 더 전" 산술 — P-12
- HN 2026-01-19 "I quit coding years ago. AI brought me back" ivcatcher(엔젤 펀드 투자 어소시에이트 자기소개)·두 인용·진위 의심 댓글·"not toys"/"Stop with the gate keeping" / mjburgess — C-3-1
- Karpathy 2025-02-02 인용·Cursor Composer·SuperWhisper / 1주년 회고 "shower of thoughts throwaway tweet" / Collins 2025-11-06 정의·후보 5개·"아홉 달 남짓" 산술 — W-3-1, W-3-2
- 표 1 N8·N9·N10(목표 굵게)·N14·N15 라벨, "수백 배"($80K→$40M=500배)·"폐업을 걱정하던"(CEO 발언 "폐업 직전") — W-3-3~3-8
- Lovable 1주년 글 제목·인용 / Masad Semafor 2025-01·2026-03 인용 / v0.app 2025-08 "anyone"(SiliconANGLE 2025-08-11) — W-3-3, W-3-4, W-3-8
- Claude Code N11(원문 대조 완료, 2025-12-03)·N12 Reuters 라벨·Cursor N13 / Octoverse 2025 N16·N17 계정 수 고지 / SO Survey 2025 N18 문구 "AI solutions that are almost right, but not quite" — W-3-5~3-11
- 생산성 한 문장: Peng(프리프린트)·METR(프리프린트)·Daniotti(Science 2026, 16만여 명=160,097) 조건 라벨 — P-5, P-6, P-52
- Sarkar & Drosos(Microsoft Research, PPIG 2025) 인용 전문 / Chou et al.(영상 20개, FSE 2026 승인) 인용·주사위 / Thorgeirsson(CHI 2026, 대학생 100명) / Feldman & Anderson(CHIWORK '24, 67명) / Virk & Liu(VL/HCC 2025) 절차·인용 — P-7, P-9, P-10, P-14, P-15
- Lee Robinson 2025-07-21 Substack 인용 전문 — C-5
- Lemkin(SaaStr) 2025-07-18 코드 동결 중 DB 삭제 / The Register 2026-02-27 Lovable 호스팅 앱 노출(인원 미기재) / carlgreene 댓글 — C-3-2
- ThailandJohn(2025-09-08, 줄임표로 "over 250 hours" 생략 — 표시 적절)·BetterToBest(2026-02-25)·roxolotl(2026-02-26) — C-3-3, C-3-2
- Pimenova 2025 프리프린트(인터뷰+Reddit+LinkedIn) — P-8
- 토스 SLASH 2021~·SLASH24 2024-09-12 첫 오프라인·TMC25 2025-07·메이커 범위 인용·인과 단정 금지·2026 미확인 고지 — W-8-1
- 카카오 697(2025-04-22) 인용·"DevRel 담당자 Sue" 자기소개·"기다리는 것이 배우는 것보다 빠르다" — tech.kakao.com 원문 대조
- sltyphoon 2025-06-17 일지·인용·구글플레이(06-20 "며칠 뒤")·"눈에 익긴"(06-24)·dooee 지인 댓글 / 자동차 문답 kgun9·hackerst 2025-08-02 — C-8-1, C-8-4

총평: 3장은 인용 밀도가 가장 높은 장인데 원문과 어긋난 문장이 없다. 부분 인용 한 곳만 고치면 통과.

### 라운드 2 (2026-09-25, 03_final.md, wc -m 13432) — 반영 확인
- ✅ L141 spilist2 원문 한 문장 전체 인용(앞 절 포함)
- **03장 사실 검증 통과.** 미해소 없음.

## 05장

### 라운드 1 (2026-09-25, 대상 chapters/05_final.md 후보본, wc -m 12921)
**❌ 정정 필요:** 없음

**⚠️ 출처 없음 (3)**
- L15 "그의 설명을 따라가면 이렇다. 개발자가 문서를 열기 전에 코딩 에이전트가 이미 Tailwind 클래스를 써준다..." — Wathan은 원인을 "the brutal impact AI has had on our business"로만 말했다. 에이전트가 클래스를 대신 써준다는 기제는 그의 설명이 아니다(가장 가까운 근거는 L19 csomar 댓글). → "이 사정을 이렇게 읽을 수 있다" 등 저자 해석으로 귀속을 바꾸기.
- L23 "한 회사의 위기는 이렇게 일단락됐다" — Google AI Studio 후원(HN 2026-01-08) 이후 위기가 해소됐다는 근거가 없다. → "후원 소식이 이어졌다"까지만.
- L51 "Block의 goose DevRel 리드로 일하던 시절" — 원문 본인 서술 "I was promoted to lead Open Source Developer Relations at Block"(fact_rules §3). → "Block에서 오픈소스 DevRel을 이끌던 시절".

**🕒 신선도 경고:** 없음

**✅ 확인됨**
- Tailwind PR #2388: 제목 "feat: add llms.txt endpoint for LLM-optimized documentation"·2025-11-18 외부 기여자(quantizor) 작성·2026-01-06 "less traffic ..." 댓글·2026-01-07(UTC) 75%·40%·80% 세 인용이 한 댓글 — GitHub API 원문 / 4명 중 3명(HN·BI) / 회사 자체 수치 라벨 / csomar 2026-01-08 두 인용 / zdragnar 2026-01-07 인용·전환율 논지 / Alex2037 AI 탓 서사 의심 / Google AI Studio 후원 HN 2026-01-08 — C-6-3
- N21 del Rio-Chanona(PNAS Nexus 2024, 6개월·약 25%·러시아어·중국어·수학 포럼·DiD·하한) / N22 Burtch(Sci. Rep. 2024, 약 100만 명/일·약 12%·신규·주니어·Reddit·"social fabric" 인용) / N23 Ibrahim & Zaki(arXiv:2609.12447 실재, 프리프린트 라벨) / N24 Kabir(CHI 2024, 517·52%·77%, 2023 모델 라벨) / Hasan 2024 프리프린트 인용 — P-1~P-3, P-50, P-51
- HN 2026-05-26 joshstrange "peaked around 2017"·nitwit005 Android 문서·jmyeet 인용(같은 스레드 확인) — C-6-1. SO 월 질문 수 미사용 준수
- r/devrel Deep_Ad1959 2026-06-07 제목·"that slot barely exists anymore"·AI 작성 표기 / uncertainschrodinger "Another channel is agents." / Competitive_Sir_8161 체인지로그 — C-2-5
- Angie Jones 2025-10-20 "SEO is basically dead ..." / Salma "fragmented"(1장 콜백) / bloppe 2025-05-15 — C-7-1, C-6-1
- Rizèl 바이브 코딩 대회(The Great Goose Off)·"outdated trick" 인용 — C-5-3 (직함만 ⚠️)
- Dewan Ahmed 2026-08-11 갱신 두 퍼널·"Stop trying ..." / Karlsson 2026-04-20 세 표면·README 인용·"community work and corpus work"·"largely unsolved"·분기별 수동 점검·"poisoned the well"·진단 3분법 — W-5-6, C-6-4
- Rachel Andrew 2026-09-22 / Jake Archibald 2026-04-07(운영 주체 라벨) / cheeseplus 2025-09-11 / Jen Looper 2025-12-21 / Dewan "cannot save a bad product" — C-5-2, W-5-6
- Watanabe(프리프린트, 567·83.8%·54.9%) / Peralta(MSR 2026 승인, 11,048개·"rejection outcomes substantially overstate agent error"·워크플로 제약 31.2%·관찰 불가 33.1%) / Steinmacher CSCW 2015·ICSE 2018 / Guo(프리프린트, 마켓 6곳, 인용) — P-44, P-45, P-21, P-47, P-48
- DevRelCon NYC 2026 Joey de Villa·Sean Keegan 질문(참관기 라벨) / GeekNews Weekly #350(2026-03) 인용·편집자 미표기 / velog jwclare95 2025-08-01(비개발 마케터·세미나·커뮤니티명 미기재) / OKKY 2025-06-01 토론회(참관기) — C-5-1, C-8-1, C-8-2

총평: 수치·인용 원문 일치. 저자 해석을 당사자 설명으로 귀속한 곳, 후일담의 과잉 결론, 직함 한 곳만 고치면 통과.

### 라운드 2 (2026-09-25, 05_final.md, wc -m 12912) — 반영 확인
- ✅ L15 기제를 저자 해석으로 귀속("그 영향이 어떤 경로로 왔는지는 이렇게 읽어볼 수 있다")
- ✅ L23 "일단락" 삭제, 후원 소식까지만
- ✅ L51 "Block에서 오픈소스 DevRel을 이끌던 시절"
- **05장 사실 검증 통과.** 미해소 없음.

## 06장

### 라운드 1 (2026-09-25, 대상 chapters/06_draft.md style 합의본, wc -m 13057)
**❌ 정정 필요 (2, 경미)**
- L32 "제목에 'Developer Relations'가 들어간 공고는 네 회사에 모두 여섯 건" — Vercel 공고 제목은 "DevRel Engineer, Agentic Infrastructure"로 'Developer Relations'가 들어 있지 않다. 여섯 건(Anthropic 1·Vercel 1·Supabase 3·Cloudflare 1) 산술은 맞다. → "제목에 'Developer Relations'나 'DevRel'이 들어간 공고는".
- L30·표 1 넷째 열 — 본문이 "표의 둘째 열에는 외부 개발자를 청중으로 삼는 공고만 넣고, 나머지는 넷째 열로 돌렸다"고 하지만 같은 기준의 공고가 넷째 열에서 빠졌다: Anthropic "Staff+ Software Engineer, Developer Experience", Lovable "Software Engineer, Platform (Developer Experience)", Stripe "Product Manager - Developer Experience, Bridge"·"Product Analytics - Developer Experience, Bridge"(2026-09-25 API). → 넷째 열에 넣거나, L30을 "나머지 가운데 일부를 넷째 열에 예로 적었다"로.

**⚠️ 출처 없음:** 없음  **🕒 신선도 경고:** 없음 (전 수치 "2026-09-25 공개 목록 기준 예시")

**✅ 확인됨**
- 표 1 전 행 API 재집계와 일치: Anthropic(628, 약 630)·DevRel 1·Applied AI 38·FDE 4+매니저 2+Pre-Sales 1·Education Lead·Copywriter / OpenAI(825, 약 830)·DX Cyber·"Forward Deployed" 22·TPM DX(Developer Velocity 팀 — "사내 개발 속도 조직" 맞음) / Vercel 87·FDE 1·SA 6 / Supabase 55·3건 / Cloudflare 382·FDE 계열 10 / Cursor 125·FDE 계열 7·SA 6·Startup Events & Community / Replit 75·FDE 1·SWE DX / Lovable 79·SA 1·CM 1 / ElevenLabs 218·DX 1·FDE 16 / Stripe 695·FD 5
- 공고 인용 전부 원문 문자열 일치: Anthropic DevRel 4개·N41 "$290,000 — $435,000 USD" OTE / Vercel 회사 소개·"work inside the product teams ..."·"hit the rough edges first"·결과물 링크·"Applications without one ..."·Head of AI Infrastructure·"demos, templates, and open source projects developers actually clone and run" / Supabase "Our users are builders ..."(published 2026-08-21) / VoidZero(updated 2026-09-15) / Anthropic FDE 3개 / OpenAI DX Cyber 두 인용·보안 도메인 / Copywriter 두 인용·DevRel 팀 매일 협업
- Cloudflare VoidZero 인수 2026-06-04 — W-5-5 원장
- FT 800% "FT 보도에 따르면" 라벨·원 데이터 미확인 고지 / a16z 2025-06-04 "services-led growth"·"sometimes rebranded ..."·N43 311건 중 22건·시점·기준 차이 고지 — W-5-2
- 이동 기록: Lee Robinson 2025-07-18 "I'm joining Cursor to teach the future of coding!"·Vercel 5년 / cameron.stream 2025-07-07 합류 → 2026-06-16 "1년이 채 안 된" 산술 맞음·인용 / Salma·Briggs 1장 콜백 / Dona Sarkar 2025-01-17 / Fly.io 2025-06-11 인용 전문 / Kelsey Hightower 2025-07-22 — C-5, C-5-2
- Daily Context 2026-07-02 세 인용·"Developer marketing aimed at engineers who read docs and deliberate" / Weinmeister 제목·1:many 요약(원문 미대조 라벨) — C-2-4, C-5
- 표 2 문구 6개 원문 일치, "가르치기" FDE 칸 미발견 서술 맞음
- 서울: Anthropic Applied AI Architect(서울 포함 6개 도시: 벵갈루루·뭄바이·서울·싱가포르·시드니·도쿄)·Manager 서울 / "런던"은 제목 변형(Applied AI Architect, Industries 등)으로 실재 — 계열 서술로 허용 / F4 OpenAI FDE Seoul / VoidZero 후보 도시 인용 / "서울 명시 DevRel 제목 공고 1건" 맞음

총평: 표와 공고 인용이 원 데이터와 맞는다. 제목 기준 표현 하나와 표 분류 기준의 일관성만 고치면 통과.

### 참고 (writer-c 자체 수정 통보, 2026-09-25)
- L84 "정면으로 답한 글로 ... 취재기가 있다", L120 "이 장을 닫기에 알맞은 문장은" — 평가어 제거, 사실 문제 없음. 라운드 1의 ❌ 2건(L32 제목 키워드, 표 1 넷째 열 규칙)은 아직 미반영.

### 라운드 2 (2026-09-25, 06_final.md, wc -m 13077) — 반영 확인
- ✅ L32 "'Developer Relations'나 'DevRel'이 들어간 공고는 ... 여섯 건"
- ✅ L30 "나머지 가운데 일부를 넷째 열에 예로 적었다" — 표와 본문 규칙 일치
- **06장 사실 검증 통과.** 미해소 없음.

## 08장

### 라운드 1 (2026-09-25, 대상 chapters/08_final.md 후보본, wc -m 12937)
**❌ 정정 필요:** 없음  **⚠️ 출처 없음:** 없음  **🕒 신선도 경고:** 없음 (Education Lead "2026년 9월 25일 확인" 명기)

**✅ 확인됨**
- Angie Jones 2025-10-20 「How DevRel Is Leading AI Adoption」(DevRelCon 발표 기반): "A couple years ago ... biggest stage of our careers."·제품 종료·goose 피벗·"We didn't know anything about AI agents."·"Going first. Figuring stuff out. Guiding others. ..."·12,000명 "Angie Jones에 따르면" + Block 공개 자료 미확인 고지(fact_rules §1 준수)·다른 팀 사용·교육 항목(프롬프트·LLM·MCP)·"Guess who our CEO ..."·"So overnight ... executive assistants."·주간 인에이블먼트·오프사이트·코드→결과·"any other community of builders"·"central ... cultural guides ... fear to curiosity"·데모 앱 범람·프로덕션·두려움 전망 — 원문 재조회 + C-7-1
- 카카오 697(2025-04-22) AI 전환 접목 문장 / 700(2025-04-24) "직접 만들어서 쓰는 것이 더 빠르다" / 762(2025-09-19) 기술전략 기획·코드 생성·디자인 프로토타이핑 AI 크레딧·약 3개월·100여 명·30여 조직·40여 과제·68.4/31.6/0%·라벨 "시범(참여 100여 명) 3개월 차 사내 설문, 응답 수 미공개"(fact_rules §3 준수)·'코더'→'코치'·시니어 인용·"사례를 공유하는 장" / 783(2025-10-30) 공동 필자(benedict.lee·sue.cream)·"한 달 남짓 뒤"(41일)·1차·2차 실험(50% 미기재 — 적절)·5~7월 시범·핵심 메시지 인용 — tech.kakao.com 원문 대조
- Anthropic Developer Education Lead(updated 2026-09-21): 세 인용·요건 3개(LLM API·에이전트/도구 사용·MCP·에이전트 프레임워크, AI 코딩 도구 일상 사용, 기술·비기술 청중 라이브 교육) 원문 일치·영업 인에이블먼트 계열 서술 수준 준수
- Rogers 5판 2003·초판 1962·5속성·오피니언 리더·변화 촉진자·동질성/이질성·채택자 범주 이론적 구분 고지 / Howell & Higgins ASQ 1990 「Champions of Technological Innovation」·짝 비교·세 행동(abstract 미확보 → 일반 서술) / Wenger 1998·2002·3요소·정의 인용의 2015 Wenger-Trayner 귀속 / Greenhalgh Milbank Quarterly 2004 — P-37~P-41
- Biilmann 2025-01-28(4장 콜백) / Ali et al.(arXiv:2606.17887 실재, 2026-06-16 프리프린트)·HR 검색→GenAI·로그·설문·인터뷰·적합도·신뢰 형성·인용 — P-43
- 8-6 학술 공백 서술 — 원장 §9와 일치

총평: 수정할 사실 문제가 없다. **08장 사실 검증 통과.**

## 09장

### 라운드 1 (2026-09-25, 대상 chapters/09_draft.md style 합의본, wc -m 12356)
**❌ 정정 필요 (1, 경미)**
- L21 Zapier "그는 1년 전 첫 판을 공개했는데" — 원문(2026-03-31) "Last May we open-sourced V1" = 2025년 5월, 발표 시점 기준 약 10개월 전이다. → "지난해 5월 첫 판을 공개했는데".

**⚠️ 출처 없음:** 없음  **🕒 신선도 경고:** 없음

**✅ 확인됨**
- Shopify Lütke 2025-04-07: 유출 중이라 직접 공개·제목·"carefully learned by… using it a lot. It's just too unlike everything else."·"too much of a suggestion"·성과·동료평가 설문·인력 요청 조건·"Everyone means everyone."·"Learning is self directed, but share what you learned."·"Ws (and Ls!)"·#revenue-ai-use-cases·#ai-centaurs — C-7-2 (fxtwitter 원문)
- Coinbase TechCrunch 2025-08-22·hluska 인용·biophysboy가 옮긴 기사 속 대화와 Armstrong "I agree." / serial_dev 2025-04-07 — C-7-2
- Zapier Wade Foster 2026-03-31: 모든 채용·Capable/Adoptive/Transformative·두 단계 인용·"the floor moved fast"·"focusing on what they've actually built" — C-7-2 (날짜 표현만 ❌)
- levhawk 2026-05-25·y0eswddl 2026-05-13("같은 달" 맞음)·esafak 2026-07-11 — C-7-3
- Sahni & Chilton(Columbia, 프리프린트 2025, M365 Copilot, 미국 경력 전문가 10명, 0/10·8/10·6/10, 인용) — P-42
- Brynjolfsson QJE 2025(5,172명, 시간당 해결 건수 15%, 저경험·저숙련 개선, 34%는 2023 WP 라벨) — P-34
- 카카오 697 MVK 인용 전문 / 700 두 인용·"이틀 뒤"(04-22→04-24) / 784 1K(E3, 2025-11-03) 진입장벽 판단·목적 인용·"복제(Clone)" 인용 — tech.kakao.com·C-8
- Dell'Acqua Org Sci 2026(BCG 758명, GPT-4, 2023 실험, 12.2%·25.1%·품질 유의 향상, 84.5%→60%/70.6%·약 19%p, "jagged frontier", 인용) — P-35 / Cybernetic Teammate(NBER WP 2025, P&G 776명, 2인 팀, 균형 잡힌 해법, 인용) — P-36
- Angie Jones "they don't trust your shiny demos ... full, messy, real process."·"AI is nondeterministic. People need to know this!!!"·"We didn't position ourselves ..." — C-7-1
- 카카오 762 두 인용("숫자로 보여드리는 것 이상의 실체", "원숭이 꽃신") 원문 일치. 동화 줄거리 요약은 일반 지식이고 762 본문 서술(꽃신에 익숙해진 뒤 ...)과도 부합
- 한계 문단 — 원장 §9 학술 공백과 일치

총평: 날짜 표현 한 곳만 고치면 통과.

### 라운드 2 (2026-09-25, 09_final.md, wc -m 12358) — 반영 확인
- ✅ L21 "지난해 5월 첫 판을 공개했는데"
- **09장 사실 검증 통과.** 미해소 없음.

## 10장

### 라운드 1 (2026-09-25, 대상 chapters/10_draft.md style R2 합의본, 디스크 wc -m 11334 — 요청서의 11,320과 다름, 디스크 기준 판정)
**❌ 정정 필요 (1, 경미)**
- L39 반론 박스 "2026년 9월 18일 **같은 토론장에서** 한 사용자는 ..." — 앞 문장의 토론은 2026-02-26 "Will vibe coding end like the maker movement?" 스레드다. cyanydeez 댓글(2026-09-18)은 **ax-check Show HN 스레드(item 49744416)** 에 달렸다(xena와 같은 스레드). → "2026년 9월 18일 ax-check를 소개한 Hacker News 스레드에서 한 사용자는".

**⚠️ 출처 없음:** 없음  **🕒 신선도 경고:** 없음 (전망마다 "2026년 9월 시점" 명기)

**✅ 확인됨**
- Amodei CFR 2025-03-10 인용 전문·단서 인용 / Gruber Daring Fireball 2026-03-13 해석(코드 총량 폭증·사람 몫 비중 감소, 서술형) / "1년 뒤" 산술 — W-9-1
- Huang WGS 2024-02-12 보도 인용·생물·화학·금융 취지·영상 미대조 고지 / Ng 2025 2차 인용·원 게시물 미확인 고지·'바이브 코딩' 명칭 비판 보도(AOL/Business Insider) — W-9-2, W-9-3
- a16z 2025-06-04 "services-led growth"·"sometimes rebranded ..."·"complex AI application companies" 취지·이해관계 고지 / HN hilariously 2026-07-03 "collapse"(Salma 글 토론) / cameron.stream 1년 미만 — W-5-2, C-2-1, C-5-2
- 반대: Anthropic·Vercel·Supabase DevRel 제목 공고(6장) — API 확인
- DevRelCon NYC 2026 Ogundare 참관기 2026-07-25·Jess Lee·Mike Swift 세션명·수천만→수억→"around a billion people ..." 인용·예측 라벨 / Biilmann "collaborators and extensions of humans" / Chanezon 2025-11-07·DevRel 20년·세 방향·"Will the model remember you?" / Liran Tal 2026 "code is cheap"·"building relationships, connecting and reaching developers"·DevRel Engineering — C-5-1, W-4-6, W-5-6, W-9-4
- roxolotl 2026-02-26·a1o "without an audience"·xena(4장 콜백) — C-3-2, C-9-1 (cyanydeez 스레드만 ❌)
- aspleenic: r/devrel 모더레이터·2026-09-18 "I made the switch about 17 years ago ... not a great time to attempt to get into DevRel" — C-2-5
- DRF 2024-09 결성 의향 귀속·Orbit 2024 Postman 인수 후 제품 종료·Salma '틀린 성공' 콜백 / N1 14.6%·N2 22.1% 기준선
- 콜백 대조: 1장(네 이야기·두 질문·r/devrel·틀린 성공)·4장 끝 xena·5장 DevRelCon 질문·6장 Daily Context·Anthropic 청중 문장·Supabase builders·7장 Dewan·세 질문·8장 끝 연구 공백·9장 다이얼 — 각 장 현재 파일(1·4·7 final, 5·8 final 후보, 2·3·6·9 draft/final)과 일치
- [이 책의 전망]: 사실 주장 없음, 본문 근거 참조·반증 조건 병기 확인

총평: 스레드 귀속 한 곳만 고치면 통과.

### 참고 (writer-a 통보)
- L55 카카오 콜백은 라운드 1 판정 대상 판(11,334자)에 이미 들어 있던 문장이며 08_final(기술전략 기획·필자 공개)과 일치 — ✅. 라운드 1 ❌ 1건(L39 스레드 귀속)은 미반영.

### 라운드 2 (2026-09-25, 10_final.md, wc -m 11357) — 반영 확인
- ✅ L39 "2026년 9월 18일 ax-check를 소개한 Hacker News 스레드에서"
- **10장 사실 검증 통과.** 미해소 없음.

## 본문 10장 종합 (2026-09-25)

| 장 | ❌ | ⚠️ | 🕒 | 최종 |
|---|---|---|---|---|
| 01 | 0 | 2 | 0 | 통과 (final 10418) |
| 02 | 1 | 1 | 0 | 통과 (final 11238) |
| 03 | 1 | 0 | 0 | 통과 (final 13432) |
| 04 | 0 | 1 | 0 | 통과 (final 13427) |
| 05 | 0 | 3 | 0 | 통과 (final 12912) |
| 06 | 2 | 0 | 0 | 통과 (final 13077) |
| 07 | 0 | 1 | 0 | 통과 (final 12024) |
| 08 | 0 | 0 | 0 | 통과 (final 12937) |
| 09 | 1 | 0 | 0 | 통과 (final 12358) |
| 10 | 1 | 0 | 0 | 통과 (final 11357) |
| 합계 | 6 | 8 | 0 | 미해소 0 |

- 10개 final 전부 `(사실 확인 필요)` 마커 0개.
- 수치 오류·날조 서술·의심 식별자 0건. ❌는 전부 인용 변형·귀속·산술 표현(경미).
- 다음: editor 앞뒤 부속(서문·PART 도입·에필로그·부록·참고문헌·콜로폰) 한정 검증 패스.

## front/back matter

### 라운드 1 (2026-09-25, 대상 04_manuscript.md 1,707줄 — 본문 10장 제외 범위 + editor 본문 수정 2곳)
**❌ 정정 필요 (3, 경미)**
- 참고문헌 "Virk, Y. & Liu, M." — 제2저자는 Dongyu Liu다(papers.md P-15). → "Virk, Y. & Liu, D."
- 참고문헌 "Tailwind Labs. "feat: add llms.txt endpoint ..." GitHub PR #2388" — 이 PR은 외부 기여자 quantizor가 2025-11-18에 열었다(GitHub API). Tailwind Labs를 PR의 저자로 적으면 5장 서술("외부 기여자가 연 PR")과 어긋난다. → "Wathan, Adam. tailwindlabs/tailwindcss.com PR #2388("feat: add llms.txt endpoint for LLM-optimized documentation", quantizor 작성 2025-11-18)에 단 댓글, 2026-01-06·07. https://github.com/tailwindlabs/tailwindcss.com/pull/2388 [1차 증언]"
- PART 1 도입 L114 "3년 가까이 쌓인 이 기록" — 가장 이른 작별 글이 2023-07-25(David Neal)이고 기준 시점이 2026-09이므로 3년 2개월이다. → "3년 넘게 쌓인".

**⚠️ 출처 없음 (1)**
- 부록 D 용어집 "에반젤리스트 — 1984년 매킨토시의 "software evangelist"에서 비롯한 직함" — 원장(W-1-1)은 에반젤리즘을 시작한 사람이 Mike Boich라고 적고 있어 "1984년 Kawasaki 직함에서 비롯했다"는 기원 단정은 근거가 없다(2장도 "처음 시작한 사람이 따로 있었다"고 썼다). → "1984년 매킨토시 시절 Apple의 "software evangelist"로 널리 알려진 직함."

**🕒 신선도 경고:** 없음 (판권·서문·참고문헌 머리말에 2026년 9월 시점·공고 조회일 명기)

**권고 (판정 아님, 서지 완결성)**
- 논문 원제 부제 누락: Robillard "What Makes APIs Hard to Learn? Answers from Developers" / Greenhalgh et al. "Diffusion of Innovations in Service Organizations: Systematic Review and Recommendations" / Lovable 글 전체 제목 "One year of Lovable: Welcome to the age of the builder"(web.md 3-3).
- editor_notes §4-4의 URL 없는 언론 보도 중 Fortune은 원문 주소를 fact-checker가 확인했다: https://fortune.com/2025/04/22/exclusive-supabase-raises-200-million-series-d-at-2-billion-valuation/
- Lee Robinson Substack은 2025-07-21로 일자까지 적을 수 있다(C-5).

**✅ 확인됨**
- 판권: 제목·부제·판본 1.0.0·발행일 2026-09-25·저자·식별자 urn:uuid:2e3ab927-… 가 book_manifest.json과 일치 / 라이선스 문자열 "CC BY-NC-SA 4.0"이 매니페스트 license와 문자 그대로 일치·CC 링크 / 하네스 v1.11.0(VERSION 파일)·저장소 URL(README와 일치)
- 목차: 10개 장 제목이 각 {NN}_final.md 첫 줄·매니페스트 chapters와 일치(10장 "네 갈래 전망")
- 서문: 2023년부터의 작별 글·"DevRel은 죽었다" 제목 글(Briggs·swyx)·Collins 2025 올해의 단어·공저 이력 문구(계획서 허용 문구 그대로)·'AX' 두 뜻과 4장·8장 배치·기준 시점·공고 조회일 2026-09-25
- PART 1~4 도입: 1·2장, 3·4·5장(범위 구분 포함), 6·7장(조회 실패 회사·스냅샷 고지·국내 장면), 8·9·10장(네 갈래 전망) 요약이 각 final과 일치. PART 2 "40년 가까이"(1984 → 2020년대 초) 허용 범위
- 에필로그: 다섯 질문의 장 참조(4장 xena, 8·9장 한계, 7장 국내 공백, 5·9장 만든 증거, 3·10장 상한론)·2장 밑줄 연습 회수 / 추천 도서 3권 서지: Thengvall 한국어판(조은옥 옮김, 한빛미디어, 2022)·Lewko & Parton(Apress, 2021)·Rogers 5판(Free Press, 2003) — W-1-4, W-1-7, P-38
- 부록 A: 네 기능×네 청중, 목적지 대응(7장), 공고 문구 3개 원문 일치, 리더 질문 3개(7-6)
- 부록 B: Gloaguen(비표준 관행·개요 무익·비용), Stripe 지시문(2차 인용 라벨), Hasan 56%·보강 트레이드오프, `.md`·Accept 헤더(커뮤니티 관행 라벨), llms.txt 제안 단계, MCP 맥락(커뮤니티 의견), `/.well-known/skills/index.json`, Chatlatanagulchai 14.8%, Hasan MCP 취약점, Google "living product" 인용, 로그 식별(F5)·단위, Karlsson "largely unsolved", xena
- 부록 C: Rogers 5속성과 9장 장치, 세 다이얼, 네 줄 양식, 허영 지표 목록(9장 levhawk·원숭이 꽃신)
- 부록 D: MCP 2024-11·AAIF 2025-12 창립 프로젝트 / llms.txt 2024-09·제안 단계 / Biilmann 2025-01 / Karpathy 2025-02·Collins 2025 / AGENTS.md AAIF / Fagerholm & Münch 2012 / DevEx 잡지 기고 / Tushman 1977 / ACI SWE-agent
- 참고문헌: 확인 등급 라벨이 원장·본문과 일치. DOI·arXiv 번호 전부 원장 §8과 일치(arXiv 22건은 라운드 0에서 실재 확인). 원장 §8에 없는 URL 8개(Karpathy 1주년·Biilmann X·Cloudflare VoidZero 발표·voidzero.dev·Apideck·FT X·velog OKKY·DevRel KR)도 research/*.md에 실재. 논문 제목 확인: Parker·Scaffidi·Ko·Burtch·del Rio-Chanona·Hsieh·Yang·Howell & Higgins·Brynjolfsson·Fagerholm & Münch·Massanori·Tushman·SPACE·DevEx 일치(Robillard·Greenhalgh은 부제 누락만). 블로그 제목 Casey·Briggs·swyx 2편 일치. 미확인 원제를 한국어 설명으로 둔 처리 적절(지어낸 제목 없음)
- editor 본문 수정: L1299(10장 a16z 콜백 — "services-led growth"·FDE 같은 새 이름, 6장 거처와 일치) / L1313(10장 roxolotl 콜백 — 3장 메이커 운동 비유, 2026-02-26, "소수에 머물 것" 요지 일치). 사실 주장 변경 없음

총평: 앞뒤 부속에서 수치 오류나 지어낸 서지는 없다. 저자명 이니셜 1곳, PR 저자 귀속 1곳, 기간 표현 1곳, 용어집 기원 단정 1곳만 고치면 통과.

### 라운드 2 (2026-09-25, 04_manuscript.md 재조립본) — 반영 확인
- ✅ L1679 "Virk, Y. & Liu, D."
- ✅ L1607 Wathan 댓글 항목(quantizor 작성 2025-11-18 명기)
- ✅ L114 "3년 넘게 쌓인 이 기록"
- ✅ L1559 용어집 에반젤리스트 "널리 알려진 직함"
- ✅ 권고 반영: L1595 Lovable 원제, L1623 Fortune 항목·URL(fact-checker 확인 주소와 일치), L1636 Lee Robinson 2025-07-21, L1664 Greenhalgh 부제, L1672 Robillard 부제
- 잔존 검사: "Liu, M." / "Tailwind Labs. \"feat" / "3년 가까이" / "에서 비롯한 직함" 0건
- **front/back matter 사실 검증 통과.** 미해소 없음. 본문 10장 + 앞뒤 부속 전 범위 미해소 0.

## 재제목

### 라운드 1 (2026-09-25, 04_manuscript.md 서문 "## 제목에 대하여" 두 문단 + 판권, v1.0.1)
**❌ 0 · ⚠️ 0 · 🕒 0 — 통과**
- ✅ "이 책 마지막 장의 제목 'DevRel 다음'" — 10장(마지막 장) 제목 "10장. DevRel 다음 — 네 갈래 전망과 그 반대편"의 주제목 부분과 일치(04_manuscript.md L1273, chapters/10_final.md 첫 줄)
- ✅ 공저 이력 문구 — 확정 문구 "데브챗 커뮤니티 출신 7인 공저 『코드 너머, 회사보다 오래 남을 개발자』(한빛미디어, 2025)"가 글자 그대로 유지됨. 뒤 서술만 "공저자 가운데 한 사람"→"저자 가운데 한 사람"으로 바뀌었고 사실 내용은 같다(7인 공저의 한 명)
- ✅ 판권 — 제목 "DevRel Next — 코드 너머의 관계"·판본 v1.0.1·발행일 2026-09-25·식별자 urn:uuid:2e3ab927-… 가 book_manifest.json(title "DevRel Next", subtitle "코드 너머의 관계", version "1.0.1")과 일치. 표제면 판본도 v1.0.1
- ✅ 잔존 검사 — 옛 부제 "AI 시대, DevRel은 누구와 무엇을 잇는가"·"v1.0.0" 원고 내 0건
