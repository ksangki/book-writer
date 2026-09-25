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

## v1.1.0

### 참고문헌 커뮤니티 절 재구성 (2026-09-25, tools/editor/biblio.md — fact-checker 단독 수정, 수정 전 사본은 스크래치패드 보관)
- 기준: 04_manuscript.md 본문에서 실제로 인용된 게시물·토론만. research/community.md 표를 파싱해 인용 문자열·작성자 핸들로 원고와 대조한 뒤, "한 사용자"로만 인용된 댓글은 요지 문구로 개별 확인.
- 형식: `- 작성자. "제목 또는 설명." 플랫폼, 날짜. <URL> [커뮤니티 의견]`, HN·Reddit·GeekNews는 스레드 단위 + 본문 인용 댓글 작성자 병기.
- HN 메타데이터: research/hn_threads.txt 12개 + 공식 API 추가 조회 6개(47167931 itunpredictable 2026-02-26 "Will vibe coding end like the maker movement?" / 45166388·47146362·48270456·48124504·48869038은 댓글 ID로 확인, 상위 스레드 제목을 API로 조회해 표기).
- 제외(본문 미인용 확인): HN 45571058(swyx "DevRel Is -Unbelievably- Back" 토론 — 글 자체는 블로그 절에 있음), 41439983(Llms.txt 2024), 48095550(Software engineering may no longer be a lifetime career).
- 결과(현 원고 기준): 커뮤니티 항목 40개(Bluesky 11·Hacker News 18·Reddit 3·GeekNews/velog 6·X 2), 링크 없는 항목 0개. Salma Bluesky 인사는 기존대로 블로그 절 Salma 항목에 둠.
- 새 15건(research/community_devrel_voices.md) 중 본문에 들어간 글은 개정 장 판정 후 추가한다.

### 재조회 중 발견한 본문 오류 (04장, 라운드 1에서 놓친 항목)
**❌ 정정 필요 (1, 경미)**
- 04_final.md(원고 L626) "2026년 9월 18일, ... ax-check가 Hacker News에 소개되자 xena라는 사용자가 이런 댓글을 남겼다" — HN API: 스레드 49744416 게시 2026-09-17 18:08 UTC, Algolia: xena 댓글 2026-09-18 19:03 UTC. 소개된 날은 9월 17일, 댓글은 이튿날이다. → "ax-check가 Hacker News에 소개된 스레드에, 2026년 9월 18일 xena라는 사용자가 이런 댓글을 남겼다." (10장 "2026년 9월 18일 ax-check를 소개한 Hacker News 스레드에서"는 댓글 날짜 귀속이라 맞음)

### 04장 ax-check 날짜 반영 확인 (2026-09-25, 04_final.md 디스크 wc -m 13688 — 통보값 13,691과 다름)
- ✅ L125 "ax-check가 Hacker News에 소개된 스레드에, 2026년 9월 18일 xena라는 사용자가" — 반영 확인. 이 판에는 v1.1.0 새 목소리 삽입이 진행 중이라 나머지 변경분은 별도 요청 시 판정.

### ax-check 날짜 패턴 전수 점검 (2026-09-25, team-lead 요청)
- 검색 범위: 04_manuscript.md, chapters/10_final.md, tools/editor/front.md·back.md·biblio.md — "9월 18일"·"09-18"·"9월 17일"·"ax-check"·"xena"
- **10장 ❌ (경미, 모호성):** 10_final.md L39(원고 L1311) "2026년 9월 18일 ax-check를 소개한 Hacker News 스레드에서 한 사용자는 ..." — cyanydeez 댓글은 2026-09-18 18:54 UTC(Algolia)로 날짜는 맞지만, 문장 구조상 날짜가 "소개한"(스레드 게시, 실제 09-17)에 붙어 읽힌다. → "ax-check를 소개한 Hacker News 스레드에서 한 사용자는 2026년 9월 18일, 에이전트라는 새 중개자에 투자해 ..."
- 10장 L45 aspleenic "2026년 9월 18일" — Reddit 댓글 날짜(C-2-5), 스레드 게시일과 무관 ✅
- **원고 L626(4장):** 04_final.md는 이미 수정됐으나 04_manuscript.md는 재조립 전 옛 문장("2026년 9월 18일, ... 소개되자")이 남아 있다 → editor 재조립 시 반영 확인 필요
- 서문·에필로그(back.md L7)·부록 B(back.md L127): xena를 "4장 끝에서 본 xena의 댓글"로만 지칭, 날짜 표기 없음 ✅
- biblio.md L163: "2026-09-17(인용 댓글은 2026-09-18)" ✅

### 01·04장 v1.1.0 개정분 (2026-09-25, 01_final.md wc -m 11994 / 04_final.md 13689, *_final_v1.0.1.md 대비 diff 11곳만)
**❌ 정정 필요 (2, 경미 — 따옴표 안 문장 절단)**
- 01 1-4 Joey deVilla(2026-07-06) 인용 ""DevRel ROI" means something specific now that it didn't mean in the zero-interest 2010s" — 원문 문장은 "... in the zero-interest 2010s or the Great Resignation era of a couple of years ago."로 이어진다. 문장 중간에서 끊고 줄임표가 없다. → 끝에 " …"를 붙이거나 뒤 절까지 인용.
- 01 1-5 Marcos Placona 인용 "... Companies will hire fewer people who can actually prove ROI" — 원문은 "... prove ROI and pay them 2x what they paid for teams that couldn't measure impact."로 이어진다. → " …" 표시, 또는 뒤 절까지 인용(뒤 절이 "salaries will rise"의 근거라 포함을 권장).

**⚠️ · 🕒:** 없음

**✅ 확인됨 (원문 직접 대조)**
- Joey deVilla, Global Nerdy 2024-02-05: "I was laid off ... Okta, along with around 400 others (a 7% reduction in the company's size)." 일치 / 해고 대비 추가 작업 풀이("In anticipation of possible upcoming layoffs, I'd been doing a little extra work") 일치
- Liz Acosta, dev.to datePublished 2024-10-30: 인용 일치, "다음 자리 없이"(= "without anything else lined up") 일치, 프로필 Developer Advocate
- Justin Poehnelt, X 2026-06-23 18:06 UTC(fxtwitter): 인용 일치 / 직함: justin.poehnelt.com/about "Senior Developer Relations Engineer at Google on the Google Workspace and Google Maps Platform teams"(전직) 일치 / "Two months ago" = 사이트 "Google fired me in April 2026"과 일치 / 사유 "I think the cause was ..." → "본인의 추정·Google 입장 미확인" 표기 적절
- "이 편지들 대부분에서" — Poehnelt 사례(도구 제작 이유의 해고)를 포괄하려는 한정어로 적절
- Daniel Bryant, Substack 2024-02-09: "I think this is overblown."·"a lack of clarity between DevRel efforts and business impact."(원문 문장 끝 일치)·overhiring 인정·"product advocates"/"community building" 분기 일치 / Ambassador Labs(~6년) 퇴사·dev/ops 도구 스타트업 자문 — 2024-01-16 회고글 일치
- Alexander Reelsen, spinscale.de 2023-11-28: "After almost four years of developer advocacy as my main job"·"cost center" 인용 전문 일치
- Sam Julien, X 2024-03-07 22:25 UTC: 첫 트윗 "#DevRel isn't dead, it's just evolving." 일치 / 후속 트윗 "lay off devrel because there's no attributable ROI" phase·"it's really hard to measure when the role is so poorly defined" — codetv.dev 임베드 원문 일치
- Joey deVilla 2026-07-06 DevRelCon NYC 2026 초록·"2024년 Okta 해고"(2024 글과 동일인) — 원문 일치(인용 절단만 ❌)
- Marcos Placona LinkedIn: datePublished 2026-01-05(활동 ID 디코딩 2026-01-05 21:01 UTC와 일치 → "2026년 1월 초" 적절)·헤드라인 "Former DevRel leader at Twilio & Circle"·[예측] 라벨 일치(인용 절단만 ❌)
- Danielle Washington, dev.to datePublished 2026-07-28·첫 발표·인용 전문 일치
- 04 L125 ax-check 날짜 — 앞서 확인
- 삭제 5곳(Salma "cry for help"·DRF 미션·swyx 부연·HN 문단 끝·"네 가지 이야기와 겹쳐 읽어도") — 삭제만, 새 사실 주장 없음 확인

### 참고문헌 추가 — 1·4장 새 목소리 9건 (2026-09-25, biblio.md "블로그·의견·언론" 절, 알파벳순 삽입)
- Acosta 2024-10-30 / Bryant 2024-02-09(+경력 회고 2024-01-16) / deVilla 2024-02-05 / deVilla 2026-07-06 / Julien 2024-03-07(+codetv 임베드) / Placona 2026-01-05 / Poehnelt 2026-06-23(+about 직함 출처) / Reelsen 2023-11-28 / Washington 2026-07-28
- 제목은 각 페이지 <title>로 확인해 원제로 적었다. Placona는 URL("15-devrel-predictions")과 페이지 요약("14 predictions")이 달라 원제를 지어내지 않고 설명으로 적음. Julien·Poehnelt는 X 게시물이라 첫 문장/설명으로 적음.
- 전 항목 링크 있음. 2장(writer-b) 새 목소리는 판정 후 추가 예정.

### 01·04·10장 v1.1.0 반영 확인 (2026-09-25)
- ✅ 01_final.md(디스크 wc -m 12076) L88 deVilla 인용 끝 "…in the zero-interest 2010s …" 절단 표시 / L100 Placona 뒤 절까지 인용("… and pay them 2x what they paid for teams that couldn't measure impact.") / style Nice "물론 r/devrel의 이 절충안도" — 지시어 명확화, 사실 변경 없음
- ✅ 04_final.md(13689) — 앞서 판정한 판 그대로
- ✅ 10_final.md(11358) L39 "ax-check를 소개한 Hacker News 스레드에서 한 사용자는 2026년 9월 18일, ..." — v1.0.1 대비 이 문장 외 변경 없음(diff 확인)
- **01·04·10장 v1.1.0 사실 검증 통과.** 미해소 없음.

### 02장 v1.1.0 개정분 (2026-09-25, 02_final.md wc -m 12920, 02_final_v1.0.1.md 대비 추가 5곳)
**❌ 정정 필요 (1, 경미 — 따옴표 안 문장 절단)**
- 2-4 Xe Iaso 인용 "At its heart, when you are DevRel, you are the bridge between the company and the community of developers" — 원문 문장은 "... community of developers that may or may not use the company's products."로 이어진다. 끝에 " …"를 붙이거나 뒤 절까지 인용.

**⚠️ · 🕒:** 없음

**✅ 확인됨 (원문 직접 대조, 따옴표 안 문자열 일치)**
- Catalin Pit, catalins.tech datePublished 2023-10-31: "In the last 2 years, I worked ... as a Developer Advocate (DA)."(= "2년 동안 Developer Advocate") / "A DA represents the company to the community and the community to the company." / "You don't know how to measure your performance." / 앞 요지 "most companies don't have clear expectations, personal metrics, and a progression track" 일치
- Ashley Willis, ashley.dev datePublished 2025-04-25: "we represent the voice of the developer inside the organization, and we represent the product to the developer community outside of it." / "We gather feedback, surface pain points, advocate for improvements, and translate between worlds." 일치, 직함 생략 준수
- Xe Iaso, xeiaso.net 2023-10-24: 경력 전환 본인 서술("pivot my career from being a software developer towards ... Developer Relations") / "you can start to observe (but not count) the results of the work." 일치 (첫 인용 절단만 ❌)
- Una Kravets, X 2024-03-08 17:52 UTC(fxtwitter): "Chrome DevRel (not true of all Google DevRel)"·"We're" → "Chrome DevRel 팀을 두고"·"자기 팀의 방식" 적절, 직함 미기재 준수 / "Ideally, DevRel should work closely with Eng and Product as a liaison for user needs, architect of the solution, test user to provide feedback, and only then a GTM strategist." / "metrics are focused around ecosystem impact and not vanity metrics like video views." / "(Which yes, can be quite hard to quantify 😂)" 전부 한 글자까지 일치
- 기존 문장 수정 없음(diff상 기존 문장은 추가 인용을 끼워 넣은 줄뿐, 원래 문구 보존 확인)

### 참고문헌 추가 — 2장 새 목소리 4건 (biblio.md "블로그·의견·언론")
- Iaso, Xe 2023-10-24 / Kravets, Una X 2024-03-08 / Pit, Catalin 2023-10-31 / Willis, Ashley 2025-04-25 — 제목은 페이지 <title>로 확인

### 02장 v1.1.0 반영 확인 (2026-09-25, 02_final.md wc -m 12922)
- ✅ 2-4 Xe Iaso 인용 끝 "… the community of developers …" 절단 표시
- **02장 v1.1.0 사실 검증 통과.** 미해소 없음.

### v1.1.0 새 목소리·참고문헌 종합
- 본문 새 목소리: 1장 8건·2장 4건·4장 1건 — 전부 원문 직접 대조 통과(❌ 3건 모두 따옴표 안 절단, 반영 확인). 4·10장 ax-check 날짜 귀속 ❌ 2건 반영 확인.
- biblio.md: 커뮤니티 절 40항목(링크 없음 0) / 블로그·의견 절에 새 출처 13건 추가(1·4장 9 + 2장 4, 링크 없음 0). 원문 주소 없는 언론 보도 묶음 1줄(사유 명기)은 기존대로 유지.

### v1.1.0 표·그림 사양 — writer-c (3·6·9장, 2026-09-25)
**❌ 0 · ⚠️ 0 · 🕒 0 — 통과**
- 표 3-2(03_final L117~123): 다섯 연구의 대상·문헌 유형·결과가 같은 절 본문(Sarkar & Drosos PPIG 2025 / Chou 영상 20개·FSE 2026 승인 / Thorgeirsson 대학생 100명·CHI 2026 / Feldman & Anderson 67명·CHIWORK '24 / Virk & Liu VL/HCC 2025)과 일치, 새 수치 없음
- 표 9-1(09_final L25~31): Shopify(성과·동료평가 설문, 인력 요청 조건, "share what you learned", 두 채널)·Coinbase(TechCrunch 2025-08 보도, 해고)·Zapier(2026-03-31, 모든 채용, "what they've actually built") 칸 전부 본문과 일치. 본문에 없는 칸 "이 장에서 다루지 않음" 처리 적절
- 표 9-2: 사실 주장 없음(본문 네 줄 양식과 일치)
- 그림 3-1: 2005 Scaffidi(N36 수치·2012 전망)·2011 Ko·2025-02-02 Karpathy·2025-11-06 Collins·2026-01 HN mjburgess(2026-01-19) — 날짜·수치 본문·원장과 일치
- 그림 3-2: 띠의 네 점과 양 끝 도구 목록(빌더 도구 표 3-1 / Claude Code·Cursor·Copilot)이 본문과 일치, 수치 없음
- 그림 6-1: 다섯 갈래와 인물 배정(cameron.stream MTS·Salma Staff Engineer / Briggs SE / Robinson Cursor 교육 / Fly.io 공고 / Dona Sarkar AI Power Users)이 6장 L78 분류와 일치, 대표성 고지 포함
- 그림 6-2: 한 축 위 세 점이 6장 스펙트럼 서술과 일치. FDE 끝에 Applied AI를 함께 둔 것은 6-6 "고객 곁으로 가는 이름(Applied AI, FDE)" 서술로 뒷받침됨
- 그림 9-1: 세 다이얼 눈금이 9장 L15(권유~성과평가)·Coinbase(해고, 강도 끝)·Zapier(채용)·9-6(만든 결과·달라진 것)·공유 장치와 일치
- 그림 9-2: 경로 a→e와 점선 x가 9장 L39·L41 서술과 일치

### 참고문헌 전부 링크화 — 언론 보도·단행본·공고 (2026-09-25, team-lead 요청)
- "원문 주소 없는 언론 보도" 묶음 줄 삭제 → 항목별 11개로 분리(블로그·의견·언론 절, 알파벳순): 9to5Google(2023-01-20) · Business Insider(2026-01-08, 원제 "Tailwind Cuts 3 of Its 4 Engineers, Cites 'Brutal Impact' of AI") · CNBC Twilio 2건(2023-02-13·2023-12-04) · CFR Amodei 대담 X + Yahoo Finance · Dealroom Cursor(2026-06-09) · FT(2025-11-02) · Andrew Ng(Yahoo Tech·AOL/BI) · TechCrunch Coinbase(2025-08-22)·Replit(2025-09-10)·Twilio(2022-09-14) · The Register(2026-02-27)
- 새로 찾은 1차 출처: Claude Code run-rate $2.5B+ — Anthropic Series G 발표(2026-02-12) 원문 "Claude Code's run-rate revenue has grown to over $2.5 billion; this figure has more than doubled since the beginning of 2026." / "The number of weekly active Claude Code users has also doubled since January 1." → 1차·공식 절에 추가. Reuters 보도 대신 1차로 인용 가능(N12 라벨 [언론] → [1차] 승격 가능)
- 새로 찾은 원문: 우아한형제들 공고 — 비즈니스피플 게재본, "Posted 2022-11-21", 현재 마감. "[2차 게재본, 현재 상태 미확인]" → 주소·게시일 확정, "현재 조직 상태 미확인"만 유지
- 단행본: Rogers 5판 ISBN 978-0-7432-2209-9(Open Library) / Wenger 1998 doi:10.1017/CBO9780511803932 / Wenger·McDermott·Snyder 2002 ISBN 978-1-57851-330-7 / Wenger-Trayner 2015 소개문 URL
- 제목 확인: 9to5Google·TechCrunch 2건·BI·Dealroom은 페이지 <title>로 원제 표기. CNBC는 봇 차단으로 제목 미확인 → 제목 대신 설명으로 표기(주소는 검색 결과·HTTP 200 확인)
- **링크 없는 항목: 0 / 전체 173.** 링크는 있으나 본문을 직접 읽지 못한 항목: FT(페이월·403, 제목·주소는 HN 제출 기록으로 확인) 1건, Andrew Ng(원 LinkedIn 게시물 주소 미확인, 2차 보도 링크) 1건

### 링크 작업 중 발견한 본문 문제
**07장 ❌ (경미, 2건 — 원문 게재본 확인으로 드러남)**
- L67 "하는 일은 "대내외 개발자들과의 관계를 바탕으로 우아한형제들의 기술 조직을 알리는" 활동" — 원문은 "대내외 개발자들과의 관계(Relations)를 바탕으로 우아한형제들의 기술 조직을 알리는"이다. 따옴표 안에서 "(Relations)"가 빠졌다. → 원문대로 복원.
- L67 "2022년 무렵으로 추정되는" — 게재본에 "Posted 2022-11-21"이 있다. → "2022년 11월 채용 플랫폼(비즈니스피플)에 게재된". "2차 게재본으로만 확인했고, 지금 이 조직이 어떤 형태인지는 알 수 없다"는 유지.
**03장 🕒 (갱신 권고)**
- "2026년 2월에는 25억 달러 이상이라는 Reuters 보도가 이어졌다(언론 보도, Anthropic 원문 문장은 미대조)" — Anthropic 원문을 찾았다(2026-02-12 Series G 발표). "미대조" 고지는 이제 사실과 다르다. → "2026년 2월 12일 Anthropic은 Claude Code의 연환산 매출이 25억 달러를 넘었다고 밝혔다(1차 발표)."

### v1.1.0 표·그림 사양 — writer-a (1·4·7·10장, 2026-09-25)
**표 5개: ❌ 0 · ⚠️ 0 — 통과**
- 표 1-1: 6명 날짜·플랫폼·떠난 방식이 본문·원문과 일치(Neal 직무 폐지 / deVilla Okta Senior Developer Advocate / Acosta dev.to 프로필·번아웃 / Camden 구조조정 해고 / Poehnelt 전 직함 본인 사이트·사유 본인 추정 / Salma 스스로 이탈·현 프로필 Staff Engineer), 날짜순 맞음
- 표 1-2: 14.6%·18.1%·22.1%(State of DevRel 2024, 유효 310, 자기선택)·26.1%(Common Room 2023, 136명, 팀 단위)·Google 약 6%(보도, DevRel 단독 아님) 단위·출처 일치
- 표 1-3: 기존 표 + 캡션 "(2024~2025)" 맞음
- 표 4-1: 연구 여섯 편 문헌 유형·대상·수치가 4-6 본문과 일치(Robillard 83명·유효 80명·78%)
- 표 7-2: 7-5 서술 요약과 일치 / 표 10-1: 10-2~10-5 출발점·반대 의견·관찰 지표와 일치
**그림 사양 7점:** 4-2 캡션만 ⚠️(아래 렌더 검증과 같은 건). 나머지(1-1·1-2·4-1·7-1·7-2·10-1) 통과

## 그림 렌더 검증 (2026-09-25, figures/fig-*.svg 13점 — tools/figures.py 렌더본, <text> 추출 대조)
**❌ 0 · ⚠️ 2 · 🕒 0**
- ⚠️ fig-4-2 제목 "Biilmann이 그린 사용자 경험의 계보" — Biilmann이 그린 것은 UX(1993 Norman)→DX(2011 Jeremiah Lee)→AX(2025)까지다. 그림에 함께 들어간 "DX와 UX의 결합(Lawson)"과 "ACI(2024, SWE-agent 논문)"는 Biilmann의 계보가 아니다(4장 본문도 Lawson·SWE-agent를 별개 출처로 서술). 제목이 전체를 Biilmann에게 귀속한다. → figures.py L171·L174 및 04_final L45 캡션: "사용자 경험의 계보 — Biilmann의 UX·DX·AX에 Lawson의 정의와 가장 가까운 학술 개념을 더해"
- ⚠️ fig-6-2 공통 띠 "세 자리 모두 되돌려준다 — 제품·엔지니어링 팀으로 피드백" — 표 6-2 되돌려주기 행은 Anthropic DevRel·Anthropic FDE 두 공고만 싣는다. Vercel(본문 "make sure they get fixed before launch")은 본문에 근거가 있지만 DX Engineer 쪽 피드백 문구는 6장 본문에 없다(공고 원문 "inform product priorities"는 있으나 본문 미인용). 그림이 본문에 없는 주장을 더한다. → figures.py L226: "되돌려주기 — 제품·엔지니어링 팀으로 피드백(표 6-2)"
- ✅ fig-1-1: 16개 날짜·인물·요지가 1장 본문·표 1-1과 일치. **분류(작별/진단·예측/반론) 16건 모두 본문 서술과 부합**: 작별 = Neal·Reelsen(DevRel을 떠나며)·deVilla 2024·Acosta·Camden·Poehnelt·Salma / 진단·예측 = swyx 2024-07·Casey·Briggs·Placona([예측])·deVilla 2026(ROI 의미 변화)·r/devrel 절충 / 반론 = Bryant("overblown")·Julien("isn't dead")·swyx 2025-10(부활론). Bryant는 본문이 진단(과잉 채용·비즈니스 영향 불명확)도 함께 싣지만 요지 라벨이 "overblown"이라 반론 분류와 일치. Camden 2026-05-27 "해고"(Webflow 구조조정 해고 — 원문 "laid off as part of the restructuring") ✓, Neal 2023-07-25 ✓
- ✅ fig-1-2: 네 단계·화살표 근거 인물(Julien 2024·DRF 2024-09 / Casey 2024·Reddington 13명 중 2명 / Reelsen 2023)과 하단 고지 "인과를 입증한 자료는 아니다"가 1장 L115 결론과 일치
- ✅ fig-3-1(다섯 시점·N36)·fig-3-2(띠·도구 목록)·fig-4-1(8개 날짜, 4장 본문 일치)·fig-6-1(다섯 갈래·대표성 고지)·fig-7-2(세 질문·예시 배치·예시 증거)·fig-9-1(세 다이얼·고지)·fig-9-2(경로·"biggest AI champion"·점선)·fig-10-1(출발점 다섯·전망 넷·흡수 라벨)
- ✅ fig-7-1 하단 "먼저 가보기가 나머지 셋을 떠받친다" — 7장 L45의 저자 판단 문장("이 네 번째 기능이 나머지 셋을 떠받친다는 생각이 든다")과 L133 핵심 박스("먼저 가보기가 나머지 셋의 재료를 만든다")와 일치
- 참고(요청 범위 밖, 간이 대조): fig-2-1·2-2·5-1·5-2·8-1·8-2도 라벨을 훑었다 — 2-2 날짜(2012·2016·2019-11·2019-12·2021·2021·2021·2023·2024-04-11)·5-1 Wathan 인용과 "이 책의 해석" 고지·8-1 "효과를 비교한 연구는 없다" 고지 모두 본문과 맞음. 옛 fig-01~05.svg(v1.0 mermaid)는 별도 파일로 남아 있음 — 사용 여부는 team-lead 판단

### 그림 렌더 검증 — 추가 6점(writer-b 사양: fig-2-1·2-2·5-1·5-2·8-1·8-2, 2026-09-25)
**❌ 1(경미) · ⚠️ 0**
- ❌ fig-5-1 하단 인용 'Wathan: "The docs are the only way people find out about our commercial products"'(figures.py L411) — 문자열 자체는 원문과 일치하지만 원문 문장은 ", and without customers we can't afford to maintain the framework."로 이어진다. 문장 중간 절단 표시 없음(fact_rules 11). → 'Wathan: "The docs are the only way people find out about our commercial products …"'
- ✅ fig-5-1 하단 고지 "에이전트 경로는 이 책의 해석 — Wathan은 원인을 AI의 영향으로만 말했다" — 05_final 5-1절 L15(저자 해석 귀속)와 일치, 퍼널 네 단계·우회 경로·점선("방문 기록이 남지 않음") 사양과 일치, 수치 미기재
- ✅ fig-2-1: 다섯 노드·네 선 라벨이 사양·본문과 일치, 네 선 모두 양방향 화살표(marker-start·end 각 4)
- ✅ fig-2-2: 9개 연도·인물(2012 Fagerholm & Münch / 2016 Leggetter DevRelCon London / 2019-11 Orbit "Communities aren't funnels"·Love × Reach / 2019-12 Thengvall DRL / 2021 Lewko & Parton / 2021 SPACE Forsgren 외 잡지 기고 / 2021 CHAOSS Goggins 외 / 2023 DevEx Noda 외 잡지 기고 / 2024-04-11 Orbit·Postman 인수 발표)이 2장 2-5절·원장(N44)과 일치
- ✅ fig-5-2: 세 표면·두 퍼널·"양쪽 퍼널로 보낸다"(5장 L83)
- ✅ fig-8-1: 대응 5행과 출처 표기(Block ×3 — 8장 L21 / Anthropic 공고 문구 — 8-3 "a demo that raises awareness and one that creates champions" / 카카오 — 8-2 "사례를 공유하는 장") 일치, 대응선만(화살표 없음) 사양 준수, 하단 "공개 사례 세 건과 이론에 기댄 대응 — 효과를 비교한 연구는 없다(8장 6절)" = 8-6의 Block·카카오·Anthropic 공고 세 건과 일치
- ✅ fig-8-2: 네 동사 순환(화살표 4)·주석 세 줄·"(Rogers)" 일치

### 07·03장 링크 작업 후속 반영 확인 (2026-09-25)
- ✅ 07_final.md(12442) L67 "관계(Relations)를 바탕으로 …" 원문 복원·"2022년 11월 채용 플랫폼(비즈니스피플)에 게재된"
- ✅ 03_final.md(14096) L85 "2026년 2월 12일 Anthropic은 Claude Code의 연환산 매출이 25억 달러를 넘었다고 밝혔다(1차 발표)." — Series G 원문과 일치, "Reuters"·"미대조" 잔존 0건
- **07·03장 통과.** 미해소 없음.

### 그림 재렌더·캡션 반영 확인 (2026-09-25)
- ✅ fig-4-2: 제목 "사용자 경험의 계보" + 부제 "Biilmann의 UX·DX·AX에 Lawson의 정의와 가장 가까운 학술 개념을 더해", SVG <title> 전체 문구 / 04_final.md L45·figure_specs.md 캡션 동일 문구
- ✅ fig-6-2: 띠 "되돌려주기 — 제품·엔지니어링 팀으로 피드백" — "(표 6-2)" 제외는 연번 치환 문제로 수용(사실 문제는 "세 자리 모두" 삭제로 해소)
- ✅ fig-5-1: Wathan 인용 끝 "…" 절단 표시
- ✅ 옛 문구("Biilmann이 그린"·"세 자리 모두") 잔존 0건(figures/*.svg·figures.py·04_final·figure_specs), 옛 fig-01~05.svg 삭제 확인
- ✅ 07_final L67 우아한형제들 정정 2건 재확인
- **그림 19점·v1.1.0 표·캡션 사실 검증 통과.** 미해소 없음.

### v1.1.0 표·그림 — writer-b (2·5·8장, 2026-09-25; 02_final 13388 / 05_final 13355 / 08_final 13593)
**❌ 0 · ⚠️ 0 · 🕒 0 — 통과**
- 표 2-1: 캡션만 추가("회사·연구자·블로그가 내놓은 DevRel의 정의") — 기존 표 구성(Google·Twilio·Fontão·Massanori·kt cloud)과 맞음
- 표 2-2: 원문 조각 4개가 원문과 일치(Pit "represents the company to the community and the community to the company" / Xe Iaso "… community of developers …" 절단 표시 / Willis "translate between worlds" / Kravets "a liaison for user needs, … and only then a GTM strategist"), 날짜·플랫폼(2023-10-31 블로그·2023-10-24 블로그·2025-04-25 블로그·2024-03-08 X) 일치
- 2-5 도입 축약 "이 일을 하는 사람들의 말도 기록으로 남았다." — 사실 주장 없음
- 표 5-1: 일곱 통로의 변화·근거 성격이 5장 본문과 일치(Tailwind 약 40%·창업자 1차 증언·방법 미공개 / N21 약 25%·N22 약 12% 동료 검토 2편 / Reddit 감소 증거 없음·3.4% 논문·프리프린트 / Angie Jones 실무자 블로그 / bloppe HN 댓글 / uncertainschrodinger r/devrel 댓글 / Rizèl 실무자 블로그)
- 표 8-1: 두 AX의 뜻·다룬 곳(4장 Biilmann 2025-01-28 / 8장 저자)·겹치는 일이 8-5와 일치
- 표 8-2: Block(Angie Jones 2025-10-20, 인원은 작성자 서술)·카카오(2025-09-19·2025-10-30, 응답 수 미공개)·Anthropic(2026-09-21 갱신, 2026-09-25 확인)이 8장 본문·fact_rules와 일치
- 그림 줄: 5-1·5-2·2-1·2-2·8-1·8-2 삽입과 "그림 N-M처럼" 지시어 변경 — 렌더 검증(앞 섹션)과 동일 그림, 캡션이 사양과 일치

## v1.1.0 재조립본 검증 (2026-09-25, 04_manuscript.md sha256 f064ad351144…)
- ✅ ax-check 날짜: 4장(원고 L698) "ax-check가 Hacker News에 소개된 스레드에, 2026년 9월 18일 xena라는 사용자가" / 10장(원고 L1440) "ax-check를 소개한 Hacker News 스레드에서 한 사용자는 2026년 9월 18일," — 옛 문장 잔존 0건
- ✅ 6장(원고 L905 부근) "표 10의 22건" — 원고 표 10 = 2026-09-25 공개 채용 목록 스냅샷(원래 표 6-1), 연번 치환 맞음
- ✅ 5장 editor 수정 "1장에서 본 Joey deVilla" — 동일인 확인: 참관기 표기 "🪗 Joey de Villa", LinkedIn "Joey de Villa – Developer Advocate @ NetFoundry", 본인 블로그 2026-07-06 "I'm speaking at DevRelCon NYC 2026"·"my own developer relations work at NetFoundry". 표기 통일 자체는 문제없음

**❌ 정정 필요 (1 — 원 참관기 대조로 새로 드러난 인용 오귀속, 라운드 1에서 놓친 항목)**
- 05_final L115(원고 L824) "2026년 7월 DevRelCon NYC의 한 세션 제목이 좋은 출발점이 된다. 참관기에 따르면 Joey de Villa와 Sean Keegan은 이렇게 물었다. "What changed because this DevRel work existed?"" — 참관기 원문(Ogundare, LinkedIn 2026-07-25 "Activity is not the same as impact" 절): Joey de Villa의 세션과 Sean Keegan의 세션은 **별개**이고, 질문은 **참관기 작성자가 두 세션을 정리한 뒤 던진 것**이다("The more strategic question is: What changed because this DevRel work existed?"). 세션 제목도 아니고, 두 발표자가 한 질문도 아니다. 원장 C-5-1("Joey de Villa·Sean Keegan 'What changed…'")과 community.md L140 요약이 원문을 합쳐 적은 데서 전파됐다.
  → 5장 교체안: "그렇다면 무엇을 세야 할까? 2026년 7월 DevRelCon NYC 참관기가 좋은 출발점이 된다. 참관기에 따르면 1장에서 본 Joey deVilla의 세션은 DevRel의 일이 채택·매출·유지 같은 결과에 어떻게 기여하는지 설명하라는 압박을 다뤘고, Sean Keegan의 세션은 교육 지표를 예로 들어 소비 지표 옆에 만든 흔적을 함께 보자고 했다. 참관기를 쓴 Ayodeji Ogundare는 두 세션을 정리한 뒤 이렇게 물었다. "What changed because this DevRel work existed?"" + 끝 문장 "참관기 요약에서 나온 문장이니 …" → "참관기 작성자의 정리이니 발표 원문의 맥락은 따로 확인해두자."
- 콜백 2곳(같은 오귀속의 전파, 🕒 표현 갱신): 09_final L119(원고 L1363)·10_final L49(원고 L1450) "5장에서 본 DevRelCon NYC 2026의 질문" → "5장에서 본 DevRelCon NYC 2026 참관기의 질문"
- 에필로그(back.md L13)·표 9-2 "무엇이 달라졌는가" — 귀속 없음, 수정 불필요

### DevRelCon 오귀속 정정 반영 확인 (2026-09-25)
- ✅ 05_final.md(13490) L115: 두 세션 분리 서술(deVilla — 결과 기여 설명 압박 / Keegan — 교육 지표 예시, 소비 지표 옆 만든 흔적) + 질문을 참관기 작성자 Ayodeji Ogundare에게 귀속 + 끝 문장 "참관기 작성자의 정리이니 …" — 참관기 원문과 일치, "한 세션 제목"·"Keegan은 이렇게 물었다" 잔존 0
- ✅ 09_final.md(13169) L119 "5장에서 본 DevRelCon NYC 2026 참관기의 질문"
- ⏳ 10_final.md(11589) L49 — 아직 "DevRelCon NYC 2026의 질문"(writer-a 반영 대기)

- ✅ 10_final.md(11593) L49 "5장에서 본 DevRelCon NYC 2026 참관기의 질문" — 전 장 옛 표현 잔존 0건. **DevRelCon 오귀속 정정 3장 모두 통과.** 재조립본 재grep 대기

### 01장 L113 지시어 수정 확인 (2026-09-25, 01_final.md)
- ✅ "2년 뒤 Joey deVilla의 후속 기록도 있다. 2024년 Okta에서 해고됐던 그는 …" — 주어 명시만, 날짜·인용·사실 변경 없음

### 재조립본 재grep (2026-09-25, 04_manuscript.md sha256 f5abf4ea4212…)
- ✅ 5장 L824: 두 세션 분리·Ogundare 귀속 / 9장 L1363·10장 L1450: "DevRelCon NYC 2026 참관기의 질문" / 옛 표현("DevRelCon NYC 2026의 질문"·"한 세션 제목"·"Keegan은 이렇게 물었다") 0건
- ✅ ax-check L698·L1440 새 표현 유지, 옛 문장 0건
- ⚠️(사실 문제 아님, 동기화) 1장 L113 writer-a 지시어 수정("2년 뒤 Joey deVilla의 후속 기록도 있다")이 이 재조립본에 없다 — 원고는 옛 문장 "2년 뒤 같은 사람에게서 후속 기록이 나왔다". 사실 내용은 같으므로 판정에는 영향 없음, 다음 재조립 때 반영 필요

### 재조립본 동기화 확인 (2026-09-25, 04_manuscript.md sha256 b7c2c388c3f8…)
- ✅ L236 "2년 뒤 Joey deVilla의 후속 기록도 있다" 반영, 옛 문장 0건. DevRelCon·ax-check 정정 유지. **v1.1.0 통합 원고 사실 검증 미해소 0.**

## 발표자료 (2026-09-25, tools/build_deck.py 51장 — 04_manuscript.md sha b7c2c388… 대조)
**❌ 0 · ⚠️ 4 · 🕒 0 (+권고 1)**
- ⚠️ L222(그림 5 foot) "바이브 코딩은 그 오래된 흐름의 가속이다" — 원고에 없는 새 규정. 3장 L29는 "이번 물결에서 새로운 것은 … 규모와 산출물이다"라고 쓴다. → "바이브 코딩은 그 흐름의 새 물결이고, 달라진 것은 규모와 산출물이다."
- ⚠️ L226(그림 6 foot) "독립 기관이 검증한 수치는 없다(표 6)" — 표 6 캡션은 "이 표에 없다"로 범위를 한정한다. 절대 단정이 된다. → "독립 기관이 검증한 수치는 표 6에 없다."
- ⚠️ L268(표 9 foot) "약해진 것은 익명의 공개 Q&A, 버틴 것은 관계형 커뮤니티." — 5장 L39는 "정답 하나를 얻으려고 모르는 사람에게 묻는 정보 교환형 공간"이고 "적어도 측정된 범위 안에서는 버텼다"로 한정한다. "익명의"는 원고에 없는 성격 규정(SO는 익명 공간으로 규정된 적 없음)이고, 측정 범위 한정이 빠졌다. → "줄어든 것은 모르는 사람에게 정답을 묻는 정보 교환형 공간, 측정된 범위에서 버틴 것은 관계형 커뮤니티."
- ⚠️ L351(카드 "인과 실증이 없다") "AI 챔피언 프로그램의 효과를 정량화한 동료 검토 연구는 아직 없다." — 8-6은 "2026년 9월 시점에 이 책의 리서치가 닿은 범위 안에서는 … 찾지 못했다"로 한정한다. → "AI 챔피언 프로그램의 효과를 정량화한 동료 검토 연구는 2026년 9월 시점 이 책의 조사 범위에서 찾지 못했다."
- 권고 L249 "연초 15.2%에서 반년 사이 네 배" — 4장은 "네 배 넘게"(66/15.2=4.3). → "네 배 넘게"
- ✅ team-lead 지정 문장: "2011년 서베이도 이미 '대부분의 프로그램은 전문 개발자가 쓰지 않는다'"(Ko 2011 초록의 번역, 그림 3-1 라벨과 동일) / "Anthropic FDE 계열 7" = 원고 표 10의 FDE 4 + 매니저 2 + Pre-Sales(FDE) 1 합산 맞음 / "경계 역할의 신뢰는 '회사의 말을 그대로 옮기지 않는다'는 데서 나온다" = 5장 L91 서술과 일치 / "Rogers의 관찰 가능성·시험 가능성은 DevRel의 데모·핸즈온과 같은 자리" = 8장 L59(데모→관찰 가능성, 핸즈온→시험 가능성) 대응 맞음 / 표 10 발췌 6행(Anthropic·OpenAI·Vercel·Supabase·Cursor·ElevenLabs) 셀 전부 원고 표 10과 일치
- ✅ 그 밖: 표·그림 번호 19개·18개가 원고 연번과 일치(표 3·5·9·10·12·13·14·17·18, 그림 1~19) / Salma·Angie Jones·Thor Schaeff·Mueller·HermanMartinus·zdragnar·cheeseplus·Jen Looper·Daily Context·Shopify 인용 문자열·날짜 일치 / State of DevRel 14.6%·18.1%·60.7%·61%·Common Room 26.1%·Google 약 6%·SO 84%·46%/33%·66%·Mintlify 66%·2억 1,300만·1억 500만 라벨 일치 / Julien 2024-03·Bryant 2024-02 / 서문 인용 "하는 일을 동사로 적어보면 두 일의 목록은 꽤 겹친다" 원고 일치 / 9장 "비교 연구는 없다"는 원고 문장 그대로
- 범위 밖(원고 사실 아님, 미검증): 마지막 표지 "ksangki.github.io/devrel-next"·"저장소 epub/ 폴더" — 배포 주소는 team-lead 확인 사항

## v1.2.0 front/back matter (2026-09-25, tools/editor/front.md·back.md, 기준 thesis.md·각 장 final)
**❌ 1 · ⚠️ 2 · 🕒 0**
- ❌ 서문 "책의 구성" 6장 "'DevRel'이라는 이름이 **줄어드는** 자리에서도" / PART 3 끝 "'DevRel'이라는 이름이 **줄어드는** 자리에서도 이어지는 네 가지 기능" — 추세 단정이다. 6장 본문은 "'DevRel이 줄고 FDE가 늘었다'고 … 그 문장은 이 표로는 쓸 수 없다. 어제의 목록이 없으니 늘었는지 줄었는지 알 수 없고"라고 쓰며, 원장 §7도 "공고 건수 비교로 DevRel 직무 감소 단정"을 금지한다. 출처는 thesis.md 장별 기여 6행("이름은 줄어도")이다.
  → 서문: "**6장**은 2026년 9월 25일 하루치 공고에서 'DevRel' 제목은 적었지만, 잇는 일이 다른 직함 속에 들어 있음을 공고 문구로 확인한다." / PART 3: "결론의 '남는 것' 칸이다. 'DevRel' 제목이 적은 하루치 공고에서도 되풀이되는 네 가지 기능, 곧 번역·피드백 루프·신뢰·먼저 가보기를 공고의 문장으로 확인한다."
- ⚠️ 서문 "책의 구성" 9장 "강요보다 공유를, 사용량보다 만든 증거를 본다" — "강요보다 공유"는 근거 강도를 넘는다. 9장은 "커뮤니티형 확산이 의무화보다 효과적이라는 것을 보여주는 비교 연구는 없다" "어떤 조합이 더 낫다고 말할 근거는 아직 없다"고 쓰고, Shopify 메모가 의무와 공유를 한 문서에 함께 담았다는 점을 들어 둘을 양자택일로 보지 않는다(세 다이얼). "사용량보다 만든 증거"는 9-6의 제안과 일치한다. 출처는 thesis.md 9행.
  → "**9장**은 회사 안에서 같은 원칙을 쓰는 설계를 다룬다. 강도·측정·공유 장치를 세 다이얼로 놓고, 사용량보다 만든 증거를 세자고 제안한다. 어느 조합이 더 나은지는 아직 증명 전이다."
- ⚠️(경미, 개념) 서문 5장 요약 "에이전트가 읽는 정확한 문서, 서로 알아보는 커뮤니티, **만든 증거가 새 통로다**" — 5장에서 만든 증거는 통로가 아니라 "무엇을 셀 것인가"의 측정 기준이다(5-6). 5장이 새 통로로 든 것은 에이전트가 읽는 문서·색인되지 않는 작은 방·사람과 에이전트가 섞인 기여자 명단이다(L113). → "에이전트가 읽는 정확한 문서와 서로 알아보는 커뮤니티가 새 통로이고, 셀 것은 만든 증거로 옮겨간다." 결론 박스·PART 2 끝·에필로그 첫 문단의 "무엇으로(R) … 만든 증거로 옮겨간다"는 저자가 확정한 thesis 문장이라 판정 대상에서 제외하고 권고로만 남긴다(R을 "통로와 셀 것"으로 읽으면 성립).
- 확인 요청(사실 아님): 부록 C-3 "9장 표 9-2" — 조립본 연번(v1.1.0에서 표 17)으로 치환되는지 확인 필요
- ✅ 서문 결론 박스·1장 "잇는 일 자체가 사라졌다는 증거는 부고 속에 없다"(1장 "누구도 개발자와 관계를 맺는 일이 필요 없어졌다고 쓰지 않았다"와 일치)·2·3·7·8장 요약("효과는 아직 증명 전")·10장 요약 / 4장 "에이전트는 문서를 읽고 제품을 고른다"(4장 핵심 박스 "DevRel과 대화하지 않고도 제품을 고른다(Supabase 일화)"와 일치)
- ✅ PART 1·2·4 끝 "이 PART가 결론에 보태는 것" — PART 4 "아직 증명 전" 한계 유지
- ✅ 에필로그 첫 문단(공인 결론 문장 원문·"회사 안의 동료를 향한 부분은 아직 증명 전")·둘째 질문("견준 연구는 없었다")·상한론 풀이·Lewko & Parton 설명(2장 Developer Journey Map Discover→Scale과 일치)·추천 도서 서지 불변
- ✅ 새 우리말 풀이: A-3 공고 문구 풀이 4개(원문 뜻과 일치) / B-3 "a skill is a living product…" 풀이 / B-4 "largely unsolved = 대부분 풀리지 않았다"·로그 숫자 "최소치"(하한) / C-1 Rogers 속성 설명(8장 "혁신이 얼마나 빨리 채택되는지에 영향을 주는 속성"과 일치) / C-4 허영 지표 정의 / 용어집 경계 역할·MCP("약속(프로토콜)")·llms.txt("맨 위 경로")·ACI·바이브 코딩("사람의 말로 지시한 AI")·FDE·DX·AX — 날짜(2024-11·2024-09·2025-01·2025-02·2025-12)·출처 불변, 뜻 일치
- ✅ 서문 약속 4항·AX 두 뜻·공저 문구 불변

### v1.2.0 front/back matter 반영 확인 (2026-09-25)
- ✅ 서문 5·6·9장 줄, PART 3 끝 한 줄 교체 문구 반영 / "줄어드"·"강요보다 공유"·"만든 증거가 새 통로" front·back 0건
- ✅ 부록 C-3 표 번호는 assemble.py 캡션 매핑 치환(v1.1.0 "표 17" 확인) — v1.2.0 재조립본에서 재확인 예정
- **v1.2.0 앞뒤 부속 통과.**

### v1.2.0 front/back matter — style R1 반영분 재확인 (2026-09-25)
**❌ 0 · ⚠️ 0 — 통과**
- ✅ 서문 6장 줄 "하루치 채용 공고를 읽는다. 제품 팀에 되돌려주고 만들어 보여주는 일이 FDE 같은 다른 직함의 공고 문구에도 적혀 있다" — 원고 표 11(기능별 공고 문구 대조) 되돌려주기·만들어 보여주기 행의 FDE 칸과 일치, 추세 단정 없음
- ✅ 서문 9장 줄 — 세 다이얼, 공유 장치(9장 "동료의 팁이 올라올 자리 … 부터 만들자"·부록 C-2), 만든 증거(9-6) 제안 + "어느 조합이 더 나은지는 아직 증명 전" 한계 유지
- ✅ 서문 7장 줄·PART 3 끝 한 줄("하루치 공고의 문장에서") / 1장 줄 둘째 문장 삭제 — 삭제만
- ✅ 에필로그 첫 문단 — 공인 결론 문장 원문 유지, "3장부터 7장까지 … 상대와 통로 … 네 가지 기능" 요약이 각 장과 맞음, "아직 증명 전" 한계 유지
- ✅ 결론 박스 라벨 "남는 것"→"잇는 일" — 내용(네 기능) 불변
- 옛 표현("줄어드"·"강요보다 공유") 0건

## v1.2.0 풀어쓰기 — 03·06·09장 (2026-09-25, *_final_v1.1.0.md 대비, 03 14776 / 06 14091 / 09 13641)
**❌ 0 · ⚠️ 3**
- ⚠️ 03 Octoverse 풀이 "개발자가 1억 8천만 명이 넘는다는 뜻이다" — 바로 뒤에서 "1억 8천만은 GitHub에 가입한 계정의 수다"라고 바로잡지만, 풀이 문장이 먼저 사실처럼 단정한다. → "개발자가 1억 8천만 명이 넘는다고 적은 것이다(2025-10-28 발행, 데이터 2024-09~2025-08)."
- ⚠️ 03 `### 이 장의 한 줄` "…돕는 일이 DevRel의 새 몫이 된다" — 3장 본문 끝은 "그 사이의 간격을 메우는 일이 누구의 몫인지, 아직 정해지지 않았다"이고, Pimenova는 커뮤니티가 먼저 그 자리를 채운다고 본다. 한 줄이 본문 결론보다 강하다. → "스스로를 개발자라 부르지 않는 빌더까지 'D'에 들어오면서, 그들이 막히는 명세·검증·기술적 의사소통은 DevRel이 오래 가르쳐온 일과 겹친다(그 몫을 누가 맡을지는 아직 정해지지 않았다)."
- ⚠️ 06 `### 이 장의 한 줄` "…FDE·Applied AI·DX Engineer 같은 여러 직함의 문장에 나뉘어 적혀 있었다" — 6장이 되돌려주기·만들어 보여주기 문구를 원문으로 보인 것은 Anthropic DevRel·Vercel DevRel Engineer·Anthropic FDE 공고다(표 6-2). Applied AI 공고 문구는 인용하지 않았고, DX Engineer(Cyber)는 예제 만들기만 서술했을 뿐 되돌려주기 문구는 없다. → "그날의 공고에서 개발자의 말을 제품으로 되돌려주고 만든 것으로 보여주는 일은 DevRel 공고뿐 아니라 FDE 공고의 문장에도 적혀 있었다."
- ✅ 영어 인용 풀이(지정 항목 포함): Octoverse Copilot "새로 들어온 개발자의 80% 가까이가 첫 주에 Copilot을 쓴다"(원문 "nearly 80% of new developers on GitHub … in their first week" 일치) / ivcatcher 두 인용 / "not toys"·"gate keeping" / Lovable 두 문구 / Masad 두 문구 / v0 "anyone" / Virk & Liu / BetterToBest / roxolotl("c++" 대목 생략 풀이는 뜻 유지) / Daily Context "fail at integration, not awareness" → "실패하는 지점은 제품을 연결하고 붙이는 단계"(대비항 생략이나 뜻 유지) / OpenAI DX 팀 "전 세계 개발자에게 힘을 싣는 것 하나에 집중" / Fly.io(저널리스트·이야기꾼) / Weinmeister 제목 "규모를 키운 FDE가 곧 DevRel Engineering" / VoidZero·Supabase·Vercel·Anthropic DevRel·FDE·Copywriter·FT 제목·a16z "rebranded" 풀이 / N41 "연 29만~43만 5천 달러" + OTE 라벨 유지 / hluska·Armstrong 대화 / Zapier Adoptive·Transformative / Shopify "Everyone means everyone" / Angie "nondeterministic" → "같은 요청에도 매번 다른 결과"
- ✅ 분할 서술: 03 Scaffidi "실측이 아닌 추정·전망치다"(라벨 "추정·전망치" 유지) / 03 Peng·METR·Daniotti 조건 라벨 세 문장으로 분리 유지 / 09 Coinbase 두 문장(TechCrunch 제목과 일치) / 09 Dell'Acqua "범위 안의 과제와 밖의 과제를 나눠 골랐다"(원 설계와 일치)
- ✅ 라벨·숫자·인용 누락 검사(스크립트): 3·6·9장 라벨 괄호·숫자·영어 인용 문자열 모두 유지. 6장 Robinson 인용은 3장 콜백으로 대체(의도된 변경), 3장 "developers" 따옴표 해제(의도된 변경)
- ✅ 09 `### 이 장의 한 줄` — "(이 설계의 효과는 아직 비교 연구로 증명되지 않았다)" 한계 유지, 9장 본문과 일치

### 03·06장 v1.2.0 반영 확인 (2026-09-25)
- ✅ 03 Octoverse 풀이 "…넘는다고 적은 것이다" / 03 한 줄 한계 괄호 포함 / 06 한 줄 "DevRel 공고와 FDE 공고의 문장에 함께 적혀 있었다"(뜻 동일) — 옛 표현 0건
- **03·06·09장 v1.2.0 통과.** 미해소 없음.

## v1.2.0 풀어쓰기 — 02·05·08장 (2026-09-25, *_final_v1.1.0.md 대비, 02 13545 / 05 14344 / 08 14037)
**❌ 0 · ⚠️ 2**
- ⚠️ 05 "문서를 만드는 회사의 엔지니어 넷 중 셋이 전날 **회사를 떠난** 것이다" — v1.1.0은 "전날 일자리를 잃었다"였고 원문은 "lost their jobs"(해고)다. "회사를 떠난"은 자발적 이탈로도 읽혀 뜻이 약해진다. → "…엔지니어 넷 중 셋이 전날 일자리를 잃은 것이다."
- ⚠️ 05 `### 이 장의 한 줄` "무엇으로(R)가 에이전트가 읽는 정확한 문서와 사람이 머무는 관계형 커뮤니티, 그리고 '만든 증거'로 옮겨갔다" — 5장에서 만든 증거는 통로가 아니라 무엇을 셀지의 기준(5-6)이고, 관계형 커뮤니티는 "적어도 측정된 범위 안에서는 버텼다"(5-2)이지 수단이 그쪽으로 옮겨갔다는 근거가 아니다(앞뒤 부속 서문 5장 줄 판정과 같은 건). → "관계를 맺는 수단, 곧 무엇으로(R)의 무게가 에이전트가 읽는 정확한 문서와, 측정된 범위에서 버틴 관계형 커뮤니티로 옮겨가고, 셀 것은 '만든 증거'가 된다."
- ✅ 02: KT Cloud 행·문단 삭제, "네 정의"(Google·Twilio·Fontão·Massanori 4행)·표 2-1 캡션 "회사와 연구자가 내놓은 DevRel의 정의" 일치 / 새 풀이 Kawasaki 위키·Boich("시작했고 자신을 뽑았다")·Briggs("쉽게 정의되지 않는 일")·Pit·Willis 2건·Xe Iaso 2건·Kravets·Journey Map "Is this of use to me?"·Fagerholm & Münch·CHAOSS — 원문 뜻과 일치 / Tushman·Massanori(46,030·SBES)·Parker·DevEx·SPACE·Lewko & Parton 분할 서술 사실 불변 / DevEx·SPACE "(둘 다 동료 검토 논문이 아닌 잡지 기고)"·Orbit "(2차 정리 자료)" 라벨 유지 / 한 줄 — 본문과 일치
- ✅ 05: 75%·40%(유일한 통로)·80%·"less traffic" 풀이, Wathan 원인 서술(두 번째 언급 우리말화), "창업자의 1차 증언(집계 방법 미공개)" 라벨, csomar "(원문 "a business model issue")"(대비항 생략이나 요지 유지), zdragnar, N21~N24(Kabir "2023년 모델 기준" 유지), Ibrahim & Zaki·Hasan·Watanabe·Guo 프리프린트 라벨, Peralta "(MSR 2026 승인)", SO 2017 정점·jmyeet·r/devrel 세 인용·Angie SEO·Salma "조각났다"·bloppe 풀이+"those aren't search-indexed"·Rizèl·Dewan 2건·Karlsson 세 표면·README·"largely unsolved"(괄호 원문)·Rachel Andrew·Archibald(운영 주체 라벨 유지)·Jen Looper·Guo·GeekNews·velog·OKKY, DevRelCon(Ogundare 귀속 유지) — 모두 원문·v1.1.0과 뜻 일치
- ✅ 08: 12,000명 "(Block 공개 자료로는 미확인)"·카카오 설문 괄호 라벨·Education Lead 갱신일 괄호 / 새 풀이 "We didn't know…"·"Guess who our CEO…"·"So overnight…"·"AI Monolingual"·"You're an engineer who teaches"·"You know the difference…"·Wenger 정의(2015 Wenger-Trayner 귀속 유지) / Angie 전망 귀속("그는 같은 글에서 … 내다봤다") 유지 / Rogers·Howell & Higgins·동질성 가설("잘 건너갔다고 해보자") / 8-6 "2026년 9월 시점, 이 책의 리서치가 닿은 범위 기준" / 한 줄 "효과는 아직 증명 전" — 근거 강도 준수
- 라벨·숫자·영어 인용 누락 검사(스크립트): 라벨·숫자 누락 0. 빠진 영어 인용은 의도된 변경(KT Cloud 행, csomar 뒤 절, "a developer who stops, sits, and reads"→우리말, bloppe "balkanized…"→우리말)뿐

### biblio.md kt cloud 항목 제거 (2026-09-25, fact-checker)
- "kt cloud 기술블로그. "DevRel 톺아보기." 2024-11-04" 1줄 삭제 → biblio.md 잔존 0, 전체 172항목. (04_manuscript.md의 3건은 v1.2.0 재조립 전 잔존 — 재조립본에서 0건 확인 예정)

## v1.2.0 풀어쓰기 — 04장 (2026-09-25, 04_final_v1.1.0.md 대비, 04 14912)
**❌ 1(경미, 풀이 주어 반전) · ⚠️ 0**
- ❌ 반론 박스 HermanMartinus 풀이 "일반 페이지는 공격적으로 긁어가면서, llms.txt는 무엇도 요청하지 않는다는 것이다("/llms.txt is not requested by anything")" — 원문은 수동태로 "llms.txt를 요청하는 것이 아무것도 없다"는 뜻이다. 풀이는 llms.txt가 요청하는 주체처럼 읽힌다. → "일반 페이지는 공격적으로 긁어가면서, llms.txt를 요청하는 것은 아무것도 없다는 것이다("/llms.txt is not requested by anything")."
- ✅ 지정 풀이: Copplestone "석 달 사이 가입 속도가 두 배"(속도 표현 유지, F1) / Karlsson "You have to already be there" / Washington / llms.txt 제안서 / Lawson "Every human assumption…"(사람을 전제로 한 가정을 걷어낼 때마다 모두에게 더 나은 플랫폼) / Mintlify "측정된 웹 트래픽의 66%" / Stripe 첫 줄 / Checkout Sessions 지시문(2차 인용 라벨 유지) / Samborski "only as good as the instructions and context" / Hsieh "시범 예제보다 도구 문서를 쓰자" / Mueller "지금 llms.txt를 쓰는 AI 시스템은 없다" / MCP "마케팅 신호에 가깝다" / xena "성장을 열 배로 키우지는 않았다"(10xed) — 원문 뜻과 일치
- ✅ 분할 서술: Schaeff 일화 귀속("실제 일화를 독자 자리로 옮겨본 것")·"미리 알아채지 못했다"(didn't realise beforehand)·가입 수치 "(Supabase 공개 수치로는 미확인)" / 타임라인 날짜·"사흘 뒤" / 카카오 "(회사 소개)"·AAIF "(재단 자체 발표)" / Biilmann 계보 / Mintlify 수치·단위·"네 배 넘게"·식별 한계·F5 목록 / Stripe 장치 / 연구 여섯 편 수치·프리프린트 라벨 / Robillard 83명(유효 80) / 반론·재반박 / ax-check 날짜 귀속(댓글 2026-09-18)
- ✅ 라벨·숫자 누락 0, 영어 인용 문자열 유지(Lawson 정의는 괄호 원문으로 이동)
- ✅ 이 장의 한 줄 "에이전트는 이미 읽어둔 문서로 제품을 고른다" — 4장 핵심 박스("추천의 순간에 에이전트가 기대는 것은 이미 읽어둔 문서와 학습 자료")와 일치

### 05장 v1.2.0 반영 확인 (2026-09-25)
- ✅ "전날 일자리를 잃은 것이다" 복원 / 이 장의 한 줄 교체 — 옛 표현 0건. **02·05·08장 v1.2.0 통과.**

## v1.2.0 풀어쓰기 — 01·07·10장 (2026-09-25, *_final_v1.1.0.md 대비, 01 14093 / 07 12755 / 10 13245)
**❌ 0 · ⚠️ 4**
- ⚠️ 01 Salma 풀이 "회사가 커뮤니티 중심에서 **엔터프라이즈 영업 중심**으로 전략을 틀었고" — 원문 "enterprise-based strategy"에 '영업'이 없고, v1.1.0도 "엔터프라이즈 중심"이었다. → "…커뮤니티 중심에서 엔터프라이즈 중심으로 전략을 틀었고, 그러자 그 자리가 사라졌다는 것이다."
- ⚠️ 01 `### 이 장의 한 줄` "부고들이 잘라낸 것은 숫자로 설명되지 않던 자리와, …한 시대의 운영 방식이었다." — 1장 본문은 이를 "이 목소리들이 공통으로 가리키는 것은 하나의 진단이다"로 당사자들의 진단에 귀속한다(fact_rules 7). 한 줄이 사실 단정으로 격상한다. → "부고들이 공통으로 가리킨 것은, 잘려나간 것이 숫자로 설명되지 않던 자리와 튜토리얼·검색·포럼에 기대던 한 시대의 운영 방식이었다는 진단이다."
- ⚠️ 10 결론 절 "8장은 이 축이 회사 담장 안까지 닿을 수 있다고 봤다. 회사 안의 동료도 **만드는 사람이 됐기 때문이다**." — 8-5는 "사내의 거의 모든 직원이 DevRel의 'D' 자리에 **설 수 있게** 되었다"로 가능성을 말한다. → "회사 안의 동료도 만드는 사람이 될 수 있게 됐기 때문이다."
- ⚠️ 10 결론 절 "공개 사례와 이론이 있을 뿐, 인과를 보여준 연구는 2026년 9월 시점에 **없다**." — 8-6은 "이 책의 리서치가 닿은 범위 안에서는 … 찾지 못했다"로 한정한다(발표자료 L351과 같은 건). → "공개 사례와 이론이 있을 뿐, 인과를 보여준 연구는 2026년 9월 시점 이 책의 조사 범위에서 찾지 못했다."
- 권고(판정 제외): 10 결론 R축 "그 자리에 세 가지가 들어온다 … 셋째는 … 셀 수 있는 '만든 증거'다" — 저자 확정 thesis 배치 문장이라 제외. "셀 수 있는"으로 성격을 밝혀 5장과 모순되지 않음
- ✅ 01 지정 풀이: 제목 "아마도 영원히, 안녕" / Bluesky 인사 / 소제목 우리말+괄호 원문 / HN "모호한 연결, 연출된 솔직함, 조율자끼리의 조율"(비꼼) / Neal / Camden / deVilla(약 400명·7%) / Acosta / Poehnelt "(Google 쪽 입장은 미확인)" / Common Room 73.9% / Briggs "money printer"·"neither fish nor fowl"(이도 저도 아닌 존재)·Measurability / Reelsen / Casey(주어·연준 서술 유지) / Julien "귀속할 ROI가 없으니 DevRel을 해고하는 국면" / deVilla 2026 / Placona "두 배"·[예측] / swyx 부활론 "그 일에 대한 욕구가 … 강하다" — 원문 뜻과 일치. 라벨(자기선택·n=310·벤더 주관 소표본·진단 귀속) 유지
- ✅ 07: 카카오 담당자 "사내 AI 도구 지원 프로그램의 경험을 공개했다"(8·10장·08_final 서술과 일치) / VoidZero·Kruczek("커뮤니티 전체가 필요로 하던")·Rizèl 조찬("4만 달러짜리") 풀이 / 우아한형제들 2022-11·E4·N4 61%·E2 24/36(2025-08 기준) / 한 줄
- ✅ 10: 결론 절 — 공인 결론 문장 원문, 표 10-2(thesis 세 축, "잇는 일"), 장별 근거 연결, 8장 한계 고지 포함, 새 사실 주장 없음(위 두 표현만 ⚠️) / [이 책의 전망] 반증 조건 3개 유지 / a16z "rebranded"·Huang·Ng(원 게시물 미확인 라벨)·DevRelCon "약 10억 명"(참관기)·Biilmann·Chanezon 세 방향·Liran Tal·roxolotl·a1o·aspleenic 풀이 일치 / 한 줄
- ✅ 라벨·숫자 누락 0(스크립트). 빠진 영어 인용 4건은 괄호 원문으로 옮기며 마침표만 빠진 것

## v1.2.0 풀어쓰기 — 라운드 2 (04 ❌1 · 01·10 ⚠️4 · 05 보충)

디스크 기준 확인 (`chapters/{NN}_final.md`).

- ✅ 04장 L136 HermanMartinus 풀이 — "일반 페이지는 공격적으로 긁어가면서, llms.txt를 요청하는 것은 아무것도 없다는 것이다("/llms.txt is not requested by anything")." 주어 복원, 원문과 일치. ❌ 해소.
- ✅ 01장 L15 Salma 풀이 — "엔터프라이즈 중심" (원문 "enterprise-based strategy"). ⚠️ 해소.
- ✅ 01장 L161 이 장의 한 줄 — "…였다는 진단이다" 귀속 유지. ⚠️ 해소.
- ✅ 10장 L130 결론 절 — "될 수 있게 됐기 때문이다" (8장 서술 강도와 일치). ⚠️ 해소.
- ✅ 10장 L130 결론 절 — "2026년 9월 시점 이 책의 조사 범위에서 찾지 못했다" (8장 6절 한정과 일치). ⚠️ 해소.
- ✅ 05장 L15 (writer-b 보충) — "엔지니어링 팀 넷 중 셋이 일자리를 잃었다." 원문 "lost their jobs"와 일치, L7과 통일. v1.1.0 "회사를 떠났다"의 약화 보정.
- 참고: 01·04·07·10장은 `_draft.md`와 `_final.md`가 다르다. 판정은 final 기준이며, 조립은 final에서 한다.

v1.2.0 풀어쓰기 10장 전체: 미해소 ❌0 ⚠️0.

## v1.2.0 재조립본 검증 (04_manuscript.md sha256 8268e653bb7e, wc -m 187,549, 2,221줄)

- ✅ kt cloud 흔적 0건 (kt cloud / kt클라우드 / 케이티).
- ✅ 이전 문구 "강요보다 공유"·"줄어드" 흔적 0건.
- ✅ 연번: `{장}-{k}` 흔적 0건. 부록 C-3 L1969 "9장 표 17"은 L1632 "표 17. 사례 수집 네 줄 양식"(9장 L1487~1655 범위)과 일치. 새 표 19(L1783 "결론을 읽는 세 개의 축")는 10장 안에 있다.
- ✅ 결론 문장 세 곳: L73 서문 결론 상자 / L1773 10장 결론 절 / L1807 에필로그 첫 문단. 원문 그대로.
- ✅ ax-check 날짜 표현 유지: L812 "ax-check가 Hacker News에 소개된 스레드가 있다. 거기에 2026년 9월 18일 xena라는 사용자가" / L1702 "한 사용자는 2026년 9월 18일,". 이전 문장 0건.
- ✅ 실패 패턴 #19: L974·L1613·L1714 모두 질문을 "참관기의 질문"(Ogundare)에 귀속. 발표자에게 귀속한 곳 0건.
- ✅ roxolotl 콜백 L1702 "그 토론(Hacker News, 2026-02-26)에서 roxolotl은 참여자가 두 배로 늘어도 소수에 머물 것이라고 봤다". 3장 L633 원문 인용("a small fraction of people")과 일치. "without an audience"는 같은 토론의 다른 사용자(a1o)에게 귀속 유지.
- ✅ xena 콜백 L1702: 4장 L812 풀이("약속받은 것처럼 성장을 열 배로 키우지는 않았다")와 일치.
- ⚠️ a16z 콜백 L1680 "그 일을 맡는 인력이 FDE 같은 새 이름을 얻는다고도 봤다" — 원문 "sometimes rebranded"의 '때로'가 빠져 단정이 강해졌다(6장 L1085 풀이는 "때로는 … 새 이름을 단다"). → "그 일을 맡는 인력이 때로 FDE 같은 새 이름을 얻는다고도 봤다." 6장 L1083의 투자사 에세이 라벨은 콜백에도 유지돼 있다.
- ✅ 콜백 참조 장 번호: a16z → 6장(L1083, 6장 L1002~1162 범위), 메이커 운동 → 3장(L631, 3장 L479~664 범위), xena → 4장(L812).
- ✅ (재확인, sha256 8a1e05552a39, wc -m 187,552) L1680 "그 일을 맡는 인력이 때로 FDE 같은 새 이름을 얻는다고도 봤다." 반영 확인. assemble.py L47의 교체 문구도 같다. 10_final.md L25는 원문 인용과 풀이가 그대로 있어 고칠 것이 없다. ⚠️ 해소. **v1.2.0 재조립본 사실 검증: 미해소 0건.**

## v1.2.0 데보션(DEVOCEAN) — 사전 검증 (2026-09-25)

- 저자 결정 (3)(4)(`00_direction.md` L58~)을 확인했다. `01_reference.md` 머리말 L7에 익명화 예외 한 줄을 추가했다(team-lead 요청).
- ✅ `research/devocean.md`의 원문 인용 9편(164693·168336·167940·167931·167950·167964·167590·166794·167611)을 원 페이지와 직접 대조했다. 표의 인용 문자열이 모두 글자 그대로 있다. 제목과 게시일(YY.MM.DD) 표기도 일치한다.
- 현재 디스크 상태(chapters/*_final.md, tools/editor/*.md, 04_manuscript.md sha 8a1e05552a39): 데보션 관련 서술 0건. 저술 반영 전이다.
- 서문 약속 문구: front.md L63 / 원고 L129 "내 경험을 사례로 쓰지는 않았다"가 그대로다. 저자 글을 반영할 때 함께 고쳐야 한다(고치지 않으면 ❌).
- 판정 규칙은 `fact_rules_active.md` §7에 올렸다.
- biblio.md: 새 절 "### 저자 본인 공개 기록 (저자 승인 예외)"에 164693·168336 두 항목을 링크와 함께 추가했다(라벨 [저자 본인 공개 기록], 회사명은 이 절에만 있다). 외부 필자 글은 본문 인용이 확정되면 커뮤니티 절에 "**DEVOCEAN (국내)**" 묶음으로 추가한다.
- 필자 자기소개의 회사명 권고(team-lead 위임): 외부 필자 글은 본문 자기소개 표기 그대로, 귀속을 붙이는 경우에만 허용한다. 저자 본인 글은 본문에 회사명을 쓰지 않는다.

## v1.2.0 데보션 — 03·09장 (writer-c 요청)

원문 대조: 원 페이지 HTML에서 본문 텍스트를 뽑아 문자열 포함 여부를 검사했다. 판정은 chapters/{03,09}_final.md 기준이다.

**03장**
- ✅ L127 데보션 소개 "국내 개발자 커뮤니티 블로그 데보션(DEVOCEAN)". 운영사 표기 없음(요청 메시지의 "SK텔레콤이 운영하는" 문구는 디스크에 없다). 03·09장 전체에 SK텔레콤·SKT 0건.
- ✅ L127 Felix(167590, 2025-07-07): 자기소개 "웹 프론트엔드 개발자 Felix" 일치. "처음에는 … 부정적이었는데 생각이 좀 바뀌었다" 풀이 일치. 인용 "바이브 코딩 시대는 … 제한될 수 있습니다."는 원문과 글자 그대로다. "(커뮤니티 의견)" 라벨이 붙어 있고, 연구 결과와 "겹친다"는 표현으로 강도를 한정했다.
- ✅ L181~185 Todd(167940, 2025-10-02): 용도 풀이(업무에 직접 쓰지 않음, 상상력 시각화, 능동적 학습)가 원문과 맞다. 인용 블록과 한계 인용 두 개는 글자 그대로다. 권고: 본문 제목 「…방법: Vibe-coding 도구」는 원제가 「…방법 : Vibe-coding 도구」(콜론 앞 공백)다. 표기 정규화로 보고 판정에는 넣지 않았다. biblio는 원제로 적었다.

**09장**
- ✅ L77 게시일 2025-10-01·제목 일치. 자기소개 인용 "저는 회사에서 … 고민하고 있습니다"는 글자 그대로다(원문 뒤의 "ㅎㅎ"는 문장 밖이라 생략해도 된다). 실명 노재헌은 본문 자기소개 표기다. 회사명(SK 하이닉스)은 본문에 쓰지 않았다.
- ✅ L81 인용 "\"나만 잘 쓰는 AI\"가 아니라, 동료가 쉽게 따라올 수 있는 경험 설계" 일치. L79 장치 풀이(재사용 가능한 형태로 정리, 팀 코드 리뷰·기술 공유 세션) 일치.
- ✅ L85 단계 모델 "학습 → 개인 PoC → 팀 체감 → 조직 리듬 결합 → 제도화 → 문화적 내재화" 원문 순서 일치. "(필자 의견, 효과 검증 전)" 라벨 적절. MIT 95% 0건.
- ⚠️ L77 "국내 현업의 확산 담당자도" — 필자는 자신을 "구성원들이 AI를 활용하여 일하는 문화를 만들기 위해 고민하고 있"다고 소개했을 뿐, 확산 담당자라는 직함은 원문에 없다. → "국내 현업에서 사내 AI 활용 문화를 고민하는 사람도 비슷한 장치를 적어두었다."
- ⚠️ L79 "그가 제안한 장치는 이렇다." — 원문에서 이 장치들은 "1. 이미 AI를 잘 사용하는 개발자"에게 준 접근 방법이다. 그 과제는 "개인 단위의 활용을 넘어서, 팀과 조직으로 확산하는 역할"이다. 대상 한정이 빠져 일반 제안처럼 읽힌다. → "그는 이미 AI를 잘 쓰는 개발자에게 개인 활용을 넘어 팀과 조직으로 퍼뜨리는 역할을 주문하며, 이런 방법을 들었다."
- biblio.md: 커뮤니티 절에 "DEVOCEAN (국내 개발자 커뮤니티 블로그)" 묶음을 새로 만들고 167590·167931·167940 세 항목을 추가했다. 운영사 표기는 저자 공개 기록 절에서도 뺐다(team-lead 보강 규칙). URL과 164693의 원제에만 남는다.
- ✅ (라운드 2, 디스크 기준) 09장 L77 "국내 현업에서 사내 AI 활용 문화를 고민하는 사람도" / L79 "그는 이미 AI를 잘 쓰는 개발자에게 … 이런 방법을 들었다." 반영 확인. ⚠️2 해소. L77의 필자 소개 "필자 노재헌은 자신의 일을 이렇게 소개했다."는 소속 표기를 뺐고 자기소개 인용은 원문 그대로다. 03장 L181 Todd 원제는 콜론 앞 공백까지 원제와 같다. 03·09장 SK텔레콤·SKT·하이닉스 0건. **03·09장 데보션 미해소 0건.**
- team-lead 결정: biblio 164693은 원제 「… (Feat. SKT 사옥)」를 유지한다. "운영사는 URL로만"은 본문 규칙이고, 참고문헌은 저자 결정 (4)의 허용 범위다. 현행 유지.

## v1.2.0 데보션 — 04·10장 (writer-a 요청)

- ✅ 04장 L117 인용 두 개(167950)는 원문과 글자 그대로다(안쪽 따옴표와 띄어쓰기 "라고 지시하니"까지 같다). 게시일 2025-10-15, 필자 인절미 일치. Chroma DB 재인용 0건. 운영사 표기 없음.
- ⚠️ 04장 L117 "후기는 필자가 전한 발표 내용으로 이런 경험을 적는다." — 원문에서 "고쳐줘" 문단은 발표 내용이 아니다. 필자 자신의 과제 경험이다("올해 진행한 과제 중 하나는 3개월동안 기획 / 디자인 / 개발이 모두 진행되었습니다. 모든 이슈는 빠르게 처리되어야 했고 LLM에게 …"). 발표자의 경험으로 읽히게 귀속이 옮겨졌다. CLAUDE.md 문장은 세미나에서 정리한 내용 쪽이다(바로 앞 "컨벤션이나 지켜야 할 팀의 관습이 있다면, 미리 지침으로 제공하자."). → "필자는 먼저 자기 과제에서 겪은 일을 이렇게 적었다." … "후기가 세미나에서 옮겨 온 해법은 지침 파일이다. 팀의 컨벤션이나 관습을 미리 지침으로 주자는 것이다."
- ✅ 04장 맺음 "그 저장소만의 규칙을 적은 짧은 문서가 현장에서 쓰이는 한 장면" — 원문의 "컨벤션이나 지켜야 할 팀의 관습"과 맞다. 앞 문단 연구의 예외(비표준 코딩 관행)와 이어진다.
- ✅ 10장 L144 "8장에서 본 저자의 공개 기록이 그 이동의 한 장면을 적어두었다." — 8장 L120에 2026-06-30 저자 공개 기록 서술이 있다. 새 사실 주장이 없고, 회사명과 운영사 표기도 없다.
- 참고(판정 요청 전): 8장 L120 인용 "진짜 신호는 검증된 결과입니다."는 원문이 "검증된 결과 입니다."(띄어쓰기)다. 8장 판정 때 다룬다.
- 참고: 데보션 첫 소개는 2장 L58이다("국내 개발자 커뮤니티 블로그인 데보션(DEVOCEAN)"). 03장 L127은 "2장에서 본"으로 이미 맞춰져 있다.
- biblio.md DEVOCEAN 묶음에 166794·167964(josephyang, 5·8장 인용), 167950(인절미, 4장)을 추가했다. 외부 필자 6편, 항목 수 180개.
- ✅ (04장 라운드 2) L117 "필자는 먼저 자기 과제에서 겪은 일을 이렇게 적었다." / "후기가 세미나에서 옮겨 온 해법은 지침 파일이다. 팀의 컨벤션이나 관습을 미리 지침으로 주자는 것이다." 반영 확인(wc -m 15,335). 콜백 "2장에서 본 데보션"은 2장 L58과 맞다. ⚠️ 해소. 10장(13,305)은 바뀐 곳 없음. **04·10장 데보션 미해소 0건.**

## v1.2.0 데보션 — 02·05·08장 (writer-b 요청)

원 페이지 원문 대조. writer-b의 조회 도구가 164693·166794 요약을 거부해, 이 두 편은 fact-checker가 원문을 직접 대조했다.

- ✅ 02장 L58 저자 공개 글(164693, 2023-04-03): 인용 "굳이 남들이 한다고 다해야하는 거 아님 (블로그 개설? 컨퍼런스 개최? ) → 회사의 목적에 맞게 꼭 해야하는 것만 하는게 좋음"은 공백까지 원문 그대로다. "DevRel 커뮤니티 모임에 참여한 뒤 올린 기록"은 원문과 맞다. "이 책을 쓰는 나도 … 공개로 남긴" 문장으로 저자 기록임을 밝혔다. 제목(회사명 포함)은 본문에 쓰지 않았다. 원문 바로 뒤의 "(하지만 보통 Top-down으로 할 일이 지정되는 경우가 많음)"은 인용 밖이라 생략해도 된다.
- ✅ 05장 L65 167964: 자기소개 "SK플래닛 DevRel Manager"는 원문 표기 그대로이고, 필자에게 귀속해 썼다. AEO 서술 "사람의 조회수가 높지 않은 글이라도 … 사례가 있다고 적었다(필자 한 사람의 관찰)"은 원문("때로는 … 사례를 보여주고 있습니다", Perplexity 검색 1건)의 강도와 맞다. PV 수치 0건.
- ⚠️ 05장 L65 인용 "이제는 개발자뿐만 아니라 AI가 나와 회사의 글을 검색하고 읽는 시대가 되었고" — 원문 문장이 "되었고 (정확하게는 …)"로 이어지는데 끊은 표시가 없다(실패 패턴 #1). → "…읽는 시대가 되었고…"로 끊김을 표시한다.
- ✅ 08장 L55 166794: 인용 두 개는 원문 그대로다(첫 인용 뒤 원문의 "(주제: …, 연사: …)"는 인용 밖). "세미나로 시작해 사용자 그룹이 사례를 나누는 순서" 요약이 맞다. 40%·55%·30명 0건.
- ⚠️ 08장 166794의 역할 귀속 — 이 글은 회사 목소리("당사는 2024년 4월부터 8월까지 … 진행하였습니다")로 쓰였다. 필자가 DevRel 매니저로서 프로그램을 맡았다는 서술은 원문에 없다. DevRel 매니저 자기소개는 2025년 글(167611·167964)에만 있고, 2024년 당시 역할도 이 글에 없다(실패 패턴 #20). 해당 지점:
  · L57 "세 기록 모두에서 개발자와 관계를 맺던 사람이 회사 안의 AI 확산을 맡았다." (v1.1.0은 "두 곳 모두") → "세 기록 모두 회사 안의 AI 확산을 사례를 나누는 커뮤니티를 운영하는 방식으로 풀어갔다. Block과 카카오의 기록에서는 개발자와 관계를 맺던 사람이 그 일을 맡았다."
  · 표 8-2 SK플래닛 행 "DevRel 매니저가 … 운영" / "담당자의 1인칭 공개 글" → "회사가 사내 AI 코딩 도구 도입을 세미나·킥오프·사용자 그룹 순으로 진행(필자는 2025년 글에서 자신을 DevRel 매니저로 소개)" / "회사 활동을 정리한 필자의 공개 글, 필자의 당시 역할은 글에 없음"
  · 8-6 둘째 "SK플래닛의 기록도 담당자 한 사람의 공개 글이다." → "SK플래닛의 기록도 회사 활동을 필자 한 사람이 정리한 공개 글이다."
- ✅ 08장 L120 저자 공개 글(168336, 2026-06-30): 인용 두 개는 원문과 같다. HTML 원문이 "<strong>검증된 결과</strong>입니다"라서 붙여 쓴 "검증된 결과입니다"가 맞다. 앞서 적은 "결과 입니다" 참고 메모는 태그를 벗길 때 생긴 공백이었다. "AX를 코드로 구현한 6개월을 정리한 글"은 원제와 맞다. 1인칭 "나는 … 공개로 남겼다"로 밝혔다.
- ✅ 08장 L141 "저자가 공개로 남긴 기록도 … 효과의 증거로 셀 수는 없다" — 한계 고지로 적절하다.
- ✅ 02·05·08장 SK텔레콤·SKT 0건. biblio에는 요청된 4편(164693·167964·166794·168336)이 이미 있다.
- ✅ (02·05·08장 라운드 2, 디스크 기준, final과 draft 동일) 05장 L65 인용 끝이 "…읽는 시대가 되었고…"로 바뀌었다. 08장 L57 "세 기록 모두 회사 안의 AI 확산을 … 풀어갔다. Block과 카카오의 기록에서는 개발자와 관계를 맺던 사람이 그 일을 맡았다." 같은 문단 첫 문장 "회사나 필자가"도 원문과 맞다(카카오는 회사, SK플래닛은 필자). 표 8-2 SK플래닛 행과 L128 "SK플래닛의 기록도 회사 활동을 필자 한 사람이 정리한 공개 글이다." 반영 확인. 옛 문구("DevRel 매니저가 사내", "담당자의 1인칭", "담당자 한 사람의") 0건, SK텔레콤·SKT 0건. ⚠️2 해소. **02·05·08장 데보션 미해소 0건.**
- 데보션 본문 반영(2·3·4·5·8·9·10장) 판정 완료. 미해소 0건. 남은 것은 서문 약속 문구와 재조립본이다.
- ✅ 서문 약속 문구 front.md L63 "저자의 경험은 공개로 남긴 기록 두 편에서만 가져왔다(2장·8장). 그 밖의 1인칭은 …" — 저자 결정 (4)와 맞다. 저자 글은 2장 L58(164693)과 8장 L120(168336) 두 곳에만 있고, 10장 L144는 8장을 가리키는 콜백일 뿐이다. 옛 문구 "사례로 쓰지" 0건(front·back·chapters). front/back의 SK텔레콤·SKT 0건. **v1.2.0 데보션 본문·서문 미해소 0건.** 남은 것은 재조립본 grep이다.
- ✅ 10장 L144 콜백 조정 "2장과 8장에서 본 저자의 공개 기록 두 편이 그 이동의 앞과 뒤를 적어두었다." (디스크 wc -m 13,313, 보고값 13,314와 1자 차이. 판정은 디스크 기준) — 2장 L58(2023-04-03, DevRel 커뮤니티 모임 참관)과 8장 L120(2026-06-30, AX 6개월)이 DevRel에서 AX로의 이동의 시간 순서와 맞다. 서문 "(2장·8장)"과도 일치한다. 새 사실 주장과 회사명은 없다.

## v1.2.0 데보션 재조립본 검증 (04_manuscript.md sha256 ec2da969ad7e, wc -m 192,250)

- ✅ 본문(L1~2044)에 SK텔레콤·SKT·꼬마집사·저자 글 제목·kt cloud·"사례로 쓰지"·MIT 95% 0건. 참고문헌의 164693 원제 "(Feat. SKT 사옥)"만 남는다(team-lead 결정대로 허용).
- ✅ SK플래닛은 본문에 4곳 나온다. L908은 외부 필자 자기소개 귀속, L1479는 8-6 둘째, L1486은 표, L1490은 8-6 셋째 사례 나열이다. 모두 허용 범위다. 하이닉스 0건.
- ✅ 데보션 인용 8곳(L372·607·661·793·908·1406·1471·1582)이 참고문헌 DEVOCEAN 8항목(외부 6편, 저자 2편, L2045 이하)과 1:1로 대응한다. 조립 편집 L1582의 "2장에서 본 개발자 커뮤니티 데보션"은 첫 소개(L372, 2장)와 맞다.
- ✅ 라운드 2 정정 문구가 모두 원고에 들어갔다. 옛 문구("확산 담당자도", "그가 제안한 장치", "DevRel 매니저가 사내", "담당자 한 사람의", "필자가 전한 발표 내용", 끊김 표시 없는 josephyang 인용) 0건.
- ✅ 서문 L129 "저자의 경험은 공개로 남긴 기록 두 편에서만 가져왔다(2장·8장)", 저자 기록 L372(2장)·L1471(8장), 10장 콜백 L1828 "2장과 8장에서 본 저자의 공개 기록 두 편"이 서로 맞다. assemble.py L35의 8장 편집("AX를 하는 사람으로서," 삭제)은 L1471의 저자 기록 문장을 건드리지 않는다.
- ✅ 결론 문장 L73·L1802·L1836 세 곳, 원문 그대로.
- **v1.2.0 사실 검증 전체 미해소 0건.**

## v1.2.0 발표자료 (tools/build_deck.py, 39장) — 원고 sha ec2da969ad7e 대조

**❌ 1 · ⚠️ 7 · 🕒 0**

- ❌ PART 4 "솔직하게" 카드 "공개 사례는 Block·카카오·Anthropic 공고 세 건, 대부분 당사자의 기록이다." — v1.2.0 원고 8-6(L1479·L1490)과 표 8-2(L1486)는 SK플래닛 기록을 더해 네 건이다("Block·카카오·SK플래닛의 기록과 Anthropic 공고"). → "공개 사례는 Block·카카오·SK플래닛의 기록과 Anthropic 공고 한 건, 대부분 당사자의 기록이다." (그림 15 자체의 "공개 사례 세 건"은 그림이 대응시킨 사례 범위라 그대로 둔다.)
- ⚠️ "왜 이 이야기를" 인용 슬라이드 — "— 서문에서"라고 출처를 달았지만 서문 원문이 아니다. "DevRel은 회사 밖 개발자에게 제품을 알리고 돕는 일이었다"에는 서문(L79)의 되돌려주는 방향("그들이 부딪힌 벽은 회사 안의 제품 팀에 전한다")이 빠졌다. after "청중만 바뀌었다."는 서문이 질문으로 둔 것("…바뀌면, 그 일은 무엇이 될까?")을 단정으로 바꿨고, '무엇으로(R)'도 바뀌었다는 책의 결론과 어긋난다. → 인용문은 서문 원문 "DevRel은 … 회사 바깥의 개발자와 관계를 맺는 일이다. … 그들이 부딪힌 벽은 회사 안의 제품 팀에 전한다.<br>지금 내가 하는 AX는 … 조직 안에 AI를 퍼뜨리는 일이다. 두 일을 동사로 적어보면 목록이 꽤 겹친다." / after "먼저 써보고, 가르치고, 보여주고, 막힌 곳을 모아 되돌려준다. 그 동사가 향하는 사람이 회사 안의 동료로 바뀌면, 그 일은 무엇이 될까?"
- ⚠️ "에이전트" 슬라이드 제목 "제품을 고른 것은 사람이 아니었다" + after "…Supabase라고 답했기 때문이다." — 원고는 절 제목을 질문으로 두었고("Supabase를 고른 것은 누구였나", L683), 이유도 Schaeff의 전언으로 귀속했다("…답했다는 것이다", L685). → 제목 "Supabase를 고른 것은 누구였나", after "…Supabase라고 답했기 때문이라고 그는 전했다."
- ⚠️ Mintlify 카드 제목 "\"문서 방문의 66%가 에이전트\"" — 원문은 "66% of measured web-traffic"이다(L743). '방문'은 카드 자신이 지적한 단위 문제(요청과 페이지 로드)를 다시 흐린다. 따옴표 안이 원문처럼 읽히는 문제도 있다. → "\"측정된 웹 트래픽의 66%가 에이전트\" — 이렇게 읽는다"
- ⚠️ josephyang 슬라이드 after "…실험(AEO)을 했다. 개발자와 함께 <b>AI도 회사의 글을 읽는 독자</b>가 됐다." — 원고(L908)는 "(필자 한 사람의 관찰)" 라벨과 "~는 말이다" 귀속을 붙였다. 슬라이드는 이를 단정으로 옮겼다. → "사람의 조회수가 높지 않은 글도 AEO/AIO 전략에 맞춰 발행하면 AI가 잘 찾는 사례가 있다고 적었다(필자 한 사람의 관찰). 개발자와 함께 AI도 회사의 글을 읽는 독자가 됐다는 말이다."
- ⚠️ 그림 19 foot "넷 모두 '만드는 사람과의 관계'로 넓어지는 한 흐름의 다른 면이다." — 원고 결론 절(L1814~1818)은 네 전망을 세 축에 나눠 배치한다. 교정론은 '무엇으로'의 숙제를 묻고, 해체론은 '잇는 일'이 어느 직무로 옮겨가느냐를 묻는다. '넓어지는 흐름'으로 묶지 않았다. → "넷은 결론의 세 축에 자리를 잡는다 — 확장·내향은 '누구와', 교정은 '무엇으로', 해체는 '잇는 일'의 질문이다."
- ⚠️ "측정 압박" 그림 슬라이드 foot "(60.7%) — State of DevRel 2024." — F3 라벨 규칙("State of DevRel 2024, n=310, 실무자 설문")이 빠졌다. → "— State of DevRel 2024, 310명 실무자 설문."
- ⚠️(경미) "당사자의 말" after "\"두 세계 사이를 통역한다\"(Ashley Willis)" — 원고(L388)의 풀이는 "서로 다른 세계 사이를 번역한다"다(원문 "translate between worlds"). 따옴표 안이므로 원고 풀이와 맞추고, 책의 핵심어 '번역'도 살린다. → "\"서로 다른 세계 사이를 번역한다\"(Ashley Willis)"
- 권고(판정 제외): Salma 출처 줄 "지금은 Staff Engineer" → 원고 표현 "프로필 직함은 Staff Engineer". Stack Overflow foot에 "자기선택 표본" 추가.
- ✅ 저자 결정 규칙: 발표자료에 SK텔레콤·SKT·꼬마집사·저자 글 제목 0건. 저자 기록 출처 줄 "저자가 2026-06-30 데보션에 공개로 남긴, AX를 코드로 구현한 6개월의 기록"은 8장 L1471 표기와 같다. 두 인용은 원문 그대로다("결과입니다" 붙여쓰기 포함). "한 사람의 기록이지 효과의 증거는 아니다"는 8장 L1492의 한계 고지와 맞다. SK플래닛은 외부 필자 자기소개로만 나오고, 데보션 운영사 표기는 없다.
- ✅ 결론 문장 2곳(결론부터 표, CLOSING)은 원문 그대로다. 세 줄 표는 표 19(L1808~1810)와 같다.
- ✅ PART 1: Salma 제목·날짜(2026-07-02)·소제목, 14.6%(응답자 본인, 310명)·26.1%(팀, Common Room 2023, 136명, 벤더)·약 6%(Google 전체, 2023-01), 1984 에반젤리스트, Catalin Pit(2023-10-31) 인용, Xe Iaso "bridge", Julien의 "isn't dead, it's just evolving" 반론. 그림 3의 "모든 선이 양방향이다"는 SVG 화살표 4개가 모두 양방향이라 맞다.
- ✅ PART 2: Ko et al. 2011 취지, Stack Overflow 2025 84·46·33·66%·약 49,000명, Schaeff "without ever talking to us"·DevRelCon NY 2025-07, 15개월(2024-09~2025-12), Mintlify 벤더 집계·단위 차이·"네 배 넘게", josephyang 인용(끊김 표시 "…")·자기소개·날짜, Tailwind 약 40%(창업자 증언)과 경로 해석 표시, "측정된 범위에서 버텼다", 만든 증거(배포·호출·PR — 5장 L990), AI cheerleading 자조(Bluesky).
- ✅ PART 3: 표 10 발췌 값(Anthropic DevRel 1·Applied AI 38·FDE 계열 4+2+1=7 / OpenAI DX 1·FD 22 / Supabase 3 / ElevenLabs DX 1·FDE 16)과 "하루치, 추세 아님" 라벨, 네 기능, 커리어 표(7장 표와 일치), 61%(커리어 경로 항목, 60.7%와 다른 슬라이드 — F3 준수).
- ✅ PART 4: Angie Jones 인용·날짜·"Going first. Figuring stuff out. Guiding others." 풀이, 그림 15 foot의 대응 세 쌍(SVG 라벨과 일치), 효과 연구 없음(L1477), 비교 연구 없음(9장), 그림 18 경로.
- ✅ (발표자료 라운드 2, build_deck.py 디스크 기준) ❌1·⚠️7·권고 2 반영 확인. 새 문구 13곳 각 1건, 옛 문구 8종 0건, SK텔레콤·SKT·꼬마집사 0건. **발표자료 v1.2.0 미해소 0건.**

## R8 판권 문구 (04_manuscript.md L18, sha256 f2df26313c5e)

- ✅ "저자 피드백을 반영한 개정판"은 `00_direction.md` 저자 결정 기록 (v1.2.0, 2026-09-25)과 맞다. 판본 v1.2.0, 매니페스트 version 1.2.0 일치. 옛 문구 "1차 초고"·"저자 검토 전" 0건(원고·tools/editor). 뒤 문장은 그대로다.
- ⚠️(경미) 괄호 "(결론 세우기·쉽게 풀어쓰기)"는 반영 내용 전체처럼 읽힌다. 그런데 이 판의 저자 결정에는 데보션 공개 글 추가와 저자 공개 기록 두 편 사용(서문 약속 문구가 바뀐 항목), kt cloud 인용 제거도 있다. → "(결론 세우기·쉽게 풀어쓰기·공개 자료 보강)" 또는 괄호 삭제.
- ✅ (R8 라운드 2, sha256 b7f08463221c, wc -m 192,467) L18 "저자 피드백(결론 세우기·쉽게 풀어쓰기·공개 자료 보강)을 반영한 개정판이다." 반영 확인. ⚠️ 해소. **판권 미해소 0건.**
