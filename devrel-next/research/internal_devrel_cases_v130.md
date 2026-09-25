<!-- 검색 시점: 2026-09-25 기준 -->
<!-- 용도: 「DevRel Next」 8장 보강 (v1.3.0) — DevRel 또는 DevRel 방식이 '회사 안' AI 도입·확산에 쓰인 공개 사례 -->
<!-- 제외(이미 책에 있음): Block "How DevRel Is Leading AI Adoption"(2025-10-20), Anthropic 개발자 교육 공고, 카카오 DevRel 사내 AI 도구 지원 -->

# 웹 리서치: 사내 AI 확산에 쓰인 DevRel과 DevRel의 방식

## 확인 표기 규칙

- **확인(원문 대조)**: 페이지를 직접 받아 인용문을 원문 텍스트에서 문자열로 찾아 맞춰 봄
- **확인(요약 경유)**: WebFetch로 페이지는 열었지만 인용문은 요약 모델을 거쳐 나옴. 책에 넣기 전에 원문 대조가 필요함
- **미확인**: 페이지를 열지 못함(403 등). 검색 결과 스니펫만 있음

## 사례 분류

- **A. DevRel 조직이나 직함이 직접 맡은 사례**: ING, Intuit, Block(보강)
- **B. DevRel이 아닌 조직이 DevRel 방식을 사내에 옮긴 사례**: GitHub, Microsoft, Zapier, Duolingo, Atlassian, Canva, Intercom, Carta, LINE Plus, 당근, 토스, 우아한형제들
- **C. 대조 사례(명령·계측 중심)**: Coinbase, Shopify, Cloudflare

---

## 자료 1: ING — "AI Developer Advocate" 채용 공고 (DevRel 팀이 사내 AI 채택 책임)
- 출처: https://ing.talent-community.com/projects/ai-developer-advocate/63822
- 저자·날짜: ING 채용 공고(Randstad Sourceright 채용 커뮤니티가 호스팅), Project ID REQ-10108589, 암스테르담. 게시일은 페이지에 없음. 현재 마감됨. 페이지 푸터 © 2026
- 출처 성격: 회사 공식 채용 공고(제3자 호스팅)
- 신뢰성: 중 (공식 공고이지만 게시일을 모름)
- 확인 여부: **확인(원문 대조)**
- 누가: ING Developer Relations 팀의 AI Developer Advocate
- 무엇을: 엔지니어링 조직 안의 AI 채택에 책임을 짐. GenAI Community of Practice 운영, 블로그·튜토리얼·발표 같은 기술 콘텐츠 제작, 업무 시간의 20~40%는 직접 엔지니어링. 스택은 GitHub Copilot, Spaces, Copilot CLI, Azure DevOps
- 인용 가능한 구절:
  - "We are seeking an AI Developer Advocate to join our developer relations team at ING." (ING 개발자 관계 팀에 합류할 AI 개발자 애드버킷을 찾는다.)
  - "We are responsible for the success of the adoption of AI inside the engineering organization." (우리는 엔지니어링 조직 안에서 AI 채택이 성공하도록 책임진다.)
  - "You help generate adoption for GenAI tooling inside the company. You help drive the GenAi Community of practise" (사내 GenAI 도구 채택을 만들어 내고, GenAI 실천 공동체를 이끈다. 원문 철자 'practise', 'GenAi' 그대로)
  - "You spend 20 to 40% of your time engineering (this does not only mean coding)." (시간의 20~40%는 엔지니어링에 쓴다. 코딩만 뜻하지는 않는다.)
- 바깥→안 대응: 외부 개발자 커뮤니티 운영과 기술 콘텐츠 제작이 사내 GenAI Community of Practice와 사내 튜토리얼·발표로 옮겨감
- 관련 섹션: 8장 "DevRel 직함이 안으로 향한다"를 보여 주는 가장 직접적인 증거

## 자료 2: Intuit — Senior Developer Advocate (사내 엔지니어 대상 GenAI 활성화)
- 출처: https://jobs.anitab.org/companies/intuit/jobs/43338937-senior-developer-advocate
- 저자·날짜: Intuit 채용 공고(AnitaB.org 잡보드에 재게시), Job ID 2024-63460. ID로 보면 2024년 공고로 추정됨. 페이지에는 "Posted 6+ months ago", 현재 마감 상태
- 출처 성격: 회사 채용 공고(제3자 잡보드)
- 신뢰성: 중
- 확인 여부: **확인(원문 대조)**
- 누가: Intuit Developer Advocacy 팀
- 무엇을: 사내 엔지니어링 팀의 GenAI·데이터 활용 지원. 사내 워크숍, 기술 교육, 온보딩 자료, FAQ·튜토리얼 같은 지식 베이스 제작
- 인용 가능한 구절:
  - "We're seeking a Senior Developer Advocate to play a pivotal role in enabling our internal engineering teams to harness the full power of Gen AI" (사내 엔지니어링 팀이 생성형 AI를 제대로 쓰게 하는 데 핵심 역할을 할 시니어 개발자 애드버킷을 찾는다.)
  - "Internal Enablement & Education : Deliver internal workshops, technical training sessions, and onboarding materials" (사내 활성화·교육: 사내 워크숍, 기술 교육 세션, 온보딩 자료를 제공한다.)
- 바깥→안 대응: 외부용 워크숍·튜토리얼·온보딩 문서가 사내 워크숍·사내 지식 베이스로 옮겨감
- 관련 섹션: ING와 짝을 이루는 두 번째 공고 증거. 2024년 공고로 추정되므로 "AI 붐 초기부터"라는 시점 서술에 쓸 수 있음(단, 날짜는 추정)

## 자료 3: Block — AI Champions 프로그램과 사내 DevRel의 Repo Quest (기존 Block 사례의 후속 글)
- 출처: https://engineering.block.xyz/blog/ai-assisted-development-at-block
- 저자·날짜: Angie Jones("I lead AI Enablement for Engineering at Block."), Block Engineering Blog, 2026-01-18
- 출처 성격: 당사자가 회사 공식 엔지니어링 블로그에 씀
- 신뢰성: 최상
- 확인 여부: **확인(원문 대조)**
- 비고: 책에 이미 있는 2025-10-20 글과는 **다른 글**. 새로 더할 내용은 챔피언 프로그램의 구조와 사내 DevRel 팀이 만든 게임화 장치
- 무엇을:
  - 2025년 8월에 AI Champions 프로그램 시작. 여러 팀의 개발자 50명이 업무 시간의 30%를 리포지토리 단위 AI 활성화에 씀
  - 사내 DevRel 팀이 **Repo Quest**(RPG식 퀘스트, Locked → Novice → Adept → Artisan 네 단계)를 만들어 AGENTS.md 같은 컨텍스트 파일 작성과 리포 준비 작업을 게임으로 바꿈
  - 챔피언과 DevRel이 함께 브라운백, 데모, "agent battles", 오피스아워, 온보딩 키트, 리포 템플릿, 프롬프트 라이브러리를 운영함
- 효과 수치(Block이 스스로 보고함): 챔피언 프로그램 시작 3개월 안에 AI 작성 코드 +69%, 보고된 시간 절감 +37%, 자동 PR 21배. 측정 방법은 글에 없음
- 인용 가능한 구절:
  - "Our internal Developer Relations team developed Repo Quest, an RPG-style game where developers complete quests to collect companions." (사내 DevRel 팀이 Repo Quest를 만들었다. 개발자가 퀘스트를 깨며 동료 캐릭터를 모으는 RPG식 게임이다.)
  - "AI Champions, along with Developer Relations, didn't just learn these tools, they taught them to all of Engineering. They ran brownbags, demos, agent battles, and office hours." (AI 챔피언과 DevRel은 도구를 배우는 데서 멈추지 않고 엔지니어링 전체에 가르쳤다. 브라운백, 데모, 에이전트 배틀, 오피스아워를 열었다.)
  - "When an engineer on your team shows you how they used an agent to knock out a tedious migration in an afternoon, it hits different than a generic tutorial." (옆자리 엔지니어가 지루한 마이그레이션을 에이전트로 한나절 만에 끝낸 방법을 보여 주면, 일반 튜토리얼과는 와닿는 정도가 다르다.)
- 바깥→안 대응: 외부 앰배서더 프로그램과 게임화된 온보딩 퀘스트가 사내 챔피언 50명과 Repo Quest로, 컨퍼런스 데모가 사내 브라운백과 agent battles로 옮겨감
- 관련 섹션: 기존 Block 서술 바로 뒤에 "3개월 뒤"로 이어 붙이기

## 자료 4: GitHub — 사내 "AI Advocates" 자원봉사 네트워크 플레이북
- 출처: https://github.com/resources/insights/activating-internal-ai-champions
- 저자·날짜: Matt Nigh(Program Manager Director of AI for Everyone, GitHub), 2025-08-29
- 출처 성격: 회사 공식 자료. 고객용 플레이북이면서 사내 경험을 공개한 글(벤더 자료 성격도 있음)
- 신뢰성: 상 (GitHub 제품 판매와 이해관계가 있음)
- 확인 여부: **확인(원문 대조)**
- 무엇을: 자원봉사 AI Advocates 네트워크. 전용 Slack 커뮤니티, 월간 체크인, 애드버킷이 여는 워크숍·오피스아워·학습 세션, 지역별·주제별 리드. 권장 시간은 주 30~60분이고 "choose your own adventure" 방식으로 운영
- 효과 수치: 없음. 측정 지표만 제시함(커뮤니티 채널 활동, 애드버킷 주최 행사 수와 참석자 수, 직원 설문에서 프로그램이 언급되는지)
- 인용 가능한 구절:
  - "AI advocates are volunteer champions. They're part coach, part translator, and part feedback loop." (AI 애드버킷은 자원한 챔피언이다. 코치이자 통역사이고 피드백 고리다.)
  - "Your advocates are on the front lines, discovering novel, practical use cases that solve real problems." (애드버킷은 최전선에서 실제 문제를 푸는 새롭고 실용적인 사례를 찾아낸다.)
  - "Volunteers are often passionate but also busy." (자원자는 열정적이지만 바쁘기도 하다.)
- 바깥→안 대응: DevRel의 세 역할(코치, 번역자, 제품 피드백 루프)을 사내 자원봉사 애드버킷에게 그대로 옮김. 외부 커뮤니티 Slack이 사내 advocate Slack으로 바뀜
- 관련 섹션: "part coach, part translator, part feedback loop"는 DevRel 정의와 거의 같아서 8장 핵심 인용 후보

## 자료 5: Microsoft — Copilot Champs Community (약 1만 명)
- 출처: https://www.microsoft.com/insidetrack/blog/driving-copilot-for-microsoft-365-adoption-with-our-copilot-champs-community/
- 저자·날짜: Alex Fleck, Microsoft Inside Track 블로그, 2024-08-01
- 출처 성격: 회사 공식 블로그(Microsoft Digital, 즉 사내 IT 조직). 자사 제품 도입기라서 벤더 자료 성격도 있음
- 신뢰성: 상
- 확인 여부: **확인(원문 대조)**
- 무엇을: 허브 앤 스포크 구조. 중앙 변화관리 팀이 자료 창구를 맡고 챔프들이 현장을 지원함. Viva Engage 커뮤니티, 전용 Teams 채널, train-the-trainer 세션(챔프가 자기 팀에서 lunch-and-learn이나 power hour를 열 수 있게 훈련), 정기 커뮤니티 콜
- 효과 수치: "nearly 10,000 champs and counting". 참여자 수이며 효과 측정은 아님
- 인용 가능한 구절:
  - "At Microsoft Digital, the company's IT organization, we understand that peer-to-peer support is one of the most powerful levers for driving excitement, engagement, education, and action for employees." (사내 IT 조직인 Microsoft Digital은 동료 간 지원이 직원의 흥미, 참여, 교육, 실행을 끌어내는 가장 강력한 지렛대 가운데 하나라고 본다.)
  - "The way to get people to really adopt a change is to make it relevant to their roles, and you achieve that by showing them the value of that change." — Lisa Fryc (사람들이 변화를 진짜 받아들이게 하려면 그 변화를 각자 역할에 맞닿게 해야 하고, 그러려면 그 가치를 보여 줘야 한다.)
- 바깥→안 대응: 외부 MVP·커뮤니티 리더 프로그램과 train-the-trainer 방식이 사내 챔프 1만 명과 팀별 lunch-and-learn으로 옮겨감
- 관련 섹션: 규모의 극단 사례. DevRel 조직이 아니라 IT 변화관리 조직이 DevRel 방식을 쓴 예

## 자료 6: Zapier — 전사 "Code Red" 해커톤에서 97% 채택까지
- 출처: https://zapier.com/blog/how-zapier-rolled-out-ai/
- 저자·날짜: Wade Foster(CEO), Zapier 공식 블로그. 페이지 표기는 2026-01-08(검색 스니펫에는 2025년 4월 초판으로 나옴. 초판 날짜는 미확인)
- 출처 성격: 당사자(CEO)가 회사 공식 블로그에 씀
- 신뢰성: 상 (자사 홍보 성격이 섞임)
- 확인 여부: **확인(원문 대조)**
- 무엇을: 2023년 3월 GPT-4 출시 뒤 첫 "Code Red"를 선언하고 전사 해커톤을 엶. 중앙 AI Enablement 지식 허브, 공동창업자가 녹화한 개발자용 Loom 영상, 챔피언(공동창업자 2인과 AI 전담으로 옮긴 전 PM), #fun-ai 채널, AI 워킹그룹, 라이브 데모, 사내 Q&A, 올핸즈·해크위크·데모 세션에서 메시지를 되풀이함
- 효과 수치(Zapier가 스스로 보고함): 제목과 본문에 97% 채택. 검색 요약에는 63%(2023년 말), 77%(2024년 말)도 나오지만 이 두 수치는 원문 대조를 못 함
- 인용 가능한 구절:
  - "The message was "Everyone, let's get hands on keyboards. Build something real to develop a sense of what is possible with AI. Learn together."" (메시지는 이것이었다. "모두 키보드에 손을 얹자. 진짜로 뭔가를 만들어 보며 AI로 무엇이 가능한지 감을 잡자. 함께 배우자.")
  - "Channels like #fun-ai became hubs of shared learning. We spun up AI working groups, ran live demos, and hosted internal Q&As." (#fun-ai 같은 채널이 함께 배우는 거점이 됐다. AI 워킹그룹을 꾸리고, 라이브 데모를 하고, 사내 Q&A를 열었다.)
  - "Repetition > announcements" (공지보다 반복)
- 바깥→안 대응: 해커톤, 라이브 데모, 커뮤니티 채널, 녹화 튜토리얼이 모두 사내 버전으로 옮겨감. 전 PM이 "빌드하면서 가르치는" 전담자가 된 점은 사내 애드버킷 역할과 겹침
- 관련 섹션: 해커톤을 사내 확산의 기폭제로 쓴 대표 사례

## 자료 7: Duolingo — AI 리터러시 워크숍, 15분 오피스아워, 격주 밋업
- 출처: https://www.infoq.com/presentations/duolingo-ai-literacy-code-review/
- 저자·날짜: Sarah Deitke(Software Engineer, Duolingo), QCon London 2026 발표. InfoQ 페이지 표기 "Recorded at: Sep 16, 2026"(InfoQ 게시 날짜로 보임)
- 출처 성격: 발표 영상과 트랜스크립트(당사자)
- 신뢰성: 최상
- 확인 여부: **확인(원문 대조)**
- 무엇을: 실습형 AI 리터러시 랩 워크숍, AI 사용 관측 대시보드, 누구나 예약하는 15분짜리 라이브 AI 지원 오피스아워, Slack 채널, 격주 "engineering building with AI" 밋업(실패 공유도 권장하고 부담을 낮춤)
- 효과 수치(발표자 팀이 측정함): 올핸즈 설문에서 엔지니어링 조직의 95%가 새로 배운 것이 있다고 답함. PR 중앙 머지 시간이 약 18시간에서 약 12시간으로 줄었고, 같은 기간 자동 승인 봇으로 머지된 PR 비중은 0%에서 약 10%로 늘어남. 발표자는 이를 상관관계로 제시함
- 인용 가능한 구절:
  - "Another thing my team does is live office hours for AI support. This is just a 15-minute time slot that different people in our organization can book." (우리 팀이 하는 또 하나는 AI 지원 라이브 오피스아워다. 조직 안 누구나 예약할 수 있는 15분짜리 시간대다.)
  - "We have a Slack channel for engineering building with AI, and then in parallel we have a biweekly engineering building with AI meetup." (AI로 만드는 엔지니어링 Slack 채널이 있고, 나란히 격주 밋업도 연다.)
  - 관찰: 오피스아워를 주로 쓰는 사람은 엔지니어가 아니라 러닝 디자이너처럼 엔지니어링 가장자리에 있는 직군이라고 함("it's not necessarily used by engineers, but it is used by these fringe parts of people")
- 바깥→안 대응: DevRel의 오피스아워와 밋업이 사내 15분 예약 오피스아워와 격주 사내 밋업으로 옮겨감
- 관련 섹션: 오피스아워를 사내에 옮긴 가장 구체적인 사례. "가장자리 직군이 온다"는 관찰은 Block이 비개발 직군으로 확장한 흐름과 이어짐

## 자료 8: Atlassian — AI Builders Week (PM·디자인 조직)
- 출처: https://www.atlassian.com/blog/how-we-build/behind-the-scenes-atlassian-ai-builders-week
- 저자·날짜: Kathleen De Lara, Inside Atlassian 블로그, 2026-04-13
- 출처 성격: 회사 공식 블로그
- 신뢰성: 상
- 확인 여부: **확인(원문 대조)**
- 무엇을: 4일짜리 프로그램(Inspire, Hands-on Skills, Build Day, Demo Day). 프로그램 매니저, 크래프트 전문가, 멘토, 고객, 외부 AI 리더, IT가 함께 설계함. 가상 멘토링과 기술 지원을 붙이고, 데모데이는 Loom 제출과 시상으로 진행. 외부 공개용 "AI Builders Week in a Box" 템플릿도 냄
- 효과 수치(Atlassian이 스스로 보고함): PM 조직 77%, 디자인 조직 80%가 참석. 에이전트 298개 제작. 슈퍼유저 사용량 +147%, 평균 사용자 +175%. Rovo Dev 일간 사용량 15~20배
- 인용 가능한 구절:
  - "298 Agents were built. We saw a jump in AI intensity with super users increasing usage by 147% and average users by 175%." (에이전트 298개가 만들어졌다. 슈퍼유저 사용량은 147%, 평균 사용자는 175% 늘었다.)
- 바깥→안 대응: 외부 개발자 해커톤과 데모데이가 사내 빌더 위크와 데모데이로 옮겨감. 멘토와 기술 지원을 붙이는 방식은 DevRel이 해커톤 멘토로 참여하던 모습 그대로임
- 관련 섹션: 해커톤 기반 사례. Zapier, Canva와 묶어서 쓰기 좋음

## 자료 9: Canva — AI Discovery Week (전 직원 1주)
- 출처(확인): https://fortune.com/2026/05/28/canva-ai-discovery-week-human-behavior-change-giglio/
- 출처(미확인, 403): https://www.canva.com/newsroom/news/ai-discovery-week-2026/ , https://www.canva.com/newsroom/news/ai-discovery-week/
- 저자·날짜: Rob Giglio(Chief Customer Officer, Canva), Fortune 기고, 2026-05-28
- 출처 성격: 당사자가 언론에 쓴 기고
- 신뢰성: 상
- 확인 여부: Fortune 기고는 **확인(원문 대조)**, Canva 뉴스룸은 **미확인**
- 무엇을: 약 5,000명에게 일주일을 통째로 줘 AI를 배우게 함. 직무별 워크숍, 리더십 패널, Anthropic·OpenAI·Google 팀 초청 실습을 하고, 이틀짜리 해커톤으로 마무리함. 좋은 아이디어는 팀 회의에서 축하하고 전사에 공유함
- 효과 수치(Canva가 스스로 보고함): "over 90% of Canva employees are weekly if not daily users of AI assistants". 검색 스니펫의 "5,300명, 25,000시간 학습, 해커톤 아이디어 330개 이상"은 뉴스룸 페이지 수치로 미확인
- 인용 가능한 구절:
  - "The entire program was designed around one idea: meet people where they are." (프로그램 전체가 하나의 생각에서 설계됐다. 사람들이 있는 곳으로 찾아간다.)
  - "Second: community accelerates adoption faster than formal enablement ever will." (둘째, 공식 교육보다 커뮤니티가 채택을 더 빨리 끌어올린다.)
- 바깥→안 대응: 벤더 초청 실습 세션(외부 DevRel이 고객사에 와서 하는 워크숍)과 해커톤을 사내 AI 주간으로 묶음. "meet people where they are"는 DevRel의 오래된 원칙과 같은 말
- 관련 섹션: 외부 벤더 DevRel이 고객사 사내 행사에 들어오는 장면. Anthropic 교육 공고 사례와 짝을 이룸

## 자료 10: Intercom — Claude Code를 전 직원에게 (동료가 동료를 온보딩)
- 출처: https://ideas.fin.ai/p/we-gave-claude-code-to-everyone-at
- 저자·날짜: Andrii Yakovenko(게스트 포스트, 바이라인 "Shaping the data behind Fin and driving AI transformation of Intercom using Claude"), 2026-03-23
- 출처 성격: 당사자가 회사 관련 뉴스레터(Substack)에 씀
- 신뢰성: 중상
- 확인 여부: **확인(원문 대조)**
- 무엇을: 원클릭 설치와 사내 시스템 연결, 도메인 스킬 자동 로드, 결과물을 사내에 게시하는 플랫폼. 공식 챔피언 프로그램이 있다는 서술은 없음. 동료 간 온보딩이 저절로 퍼졌다고 씀
- 효과 수치(글쓴이 팀 집계): 접근 권한자 1,000명 이상, 주간 활성 300명 이상, 한 주에 게시 페이지 330개, 한 주 조회 2,500회 이상, 디렉터급 이상의 60%가 활성 사용
- 인용 가능한 구절:
  - "And people started onboarding their own teammates without us being involved - they just showed a colleague and said "you need to try this."" (사람들이 우리가 끼지 않았는데도 동료를 직접 온보딩하기 시작했다. 옆 사람에게 보여 주며 "이거 꼭 써 봐"라고 했다.)
  - "It has unlocked an army of high-agency individuals." (주도적으로 움직이는 사람들의 군단을 풀어놓았다. 사내 직원 발언을 인용한 것)
- 바깥→안 대응: "show-and-tell"과 사례 공유가 사내 게시 플랫폼이 되고, 사용자가 사용자를 끌어오는 커뮤니티 플라이휠이 됨
- 관련 섹션: 공식 장치 없이 게시 공간만 열어도 DevRel식 확산이 일어난다는 반례에 가까운 사례
- 참고(미확인): Brian Scanlan(Intercom)의 "2x" 사례는 해커톤, enablement day, 전담 지원 팀을 언급함 — https://newsletter.getdx.com/p/doubling-the-productivity-of-your (열지 않음)

## 자료 11: Carta (LeadDev 기사) — 믿는 동료의 시연, 주간 오피스아워, show-and-tell
- 출처: https://leaddev.com/ai/ai-champions-are-the-key-to-engineering-adoption
- 저자·날짜: Sage Lazzaro, LeadDev, 2026-02-09
- 출처 성격: 업계 매체 기사
- 신뢰성: 상
- 확인 여부: **확인(원문 대조)**
- 무엇을: Carta에서는 파워유저가 일찍 나타나 공유의 순환을 만들었다고 함. 주간 오피스아워, 같은 도메인 엔지니어끼리 하는 "show-and-tell"과 페어 프로그래밍, 도구별 Slack 채널(Claude Code, Windsurf)을 운영함. 기사 문맥상 이 장치들은 Carta의 것으로 읽히지만, 기사 본문을 한 번 더 확인할 것
- 인용 가능한 구절:
  - "You can't tell them a better way; you need to show them. And the person showing them needs to be an existing trusted peer." — Tyler McConnell, staff software engineer, Carta (더 나은 방법을 말로 알려 줄 수는 없다. 보여 줘야 한다. 그리고 보여 주는 사람은 이미 믿는 동료여야 한다.)
- 바깥→안 대응: 데모와 show-and-tell, 그리고 신뢰받는 동료가 목소리를 내는 앰배서더 방식이 사내 주간 오피스아워와 도구별 채널로 옮겨감
- 관련 섹션: 8장 "보여 주기(show, don't tell)" 원칙의 인용 후보

## 자료 12: LINE Plus (LY Corporation) — 조직별 AI Evangelist
- 출처: https://techblog.lycorp.co.jp/ko/tech-verse-2026-ai-driven-development-review
- 저자·날짜: LINE Plus와 ABC Studio의 서버 개발자 2인(블로그 바이라인에 공개됨), LY Corporation Tech Blog, Tech-Verse 2026 참관기. 게시일은 본문에서 못 찾음(2026년)
- 출처 성격: 당사자가 회사 공식 기술블로그에 씀
- 신뢰성: 상
- 확인 여부: **확인(원문 대조)**
- 무엇을: 글쓴이 두 사람이 "사내에서 조직별로 구성된 AI Evangelist"로 활동한다고 밝힘. Tech-Verse 2026 패널에서 LINE Plus가 "조직별 에반젤리스트를 통한 현장 중심(bottom-up) 확산 전략"을 소개했다고 전함. 에반젤리스트는 팀 안 AI 표준과 공통 가이드를 만드는 역할을 함
- 효과 수치(발표 인용): LINE Plus 백엔드 팀이 10개월 동안 측정해 인당·시간당 생산성 9.24배. 1주 차에 CLAUDE.md 10~15줄을 쓰는 것부터 시작하는 "4주 도입 플랜"
- 인용 가능한 구절:
  - "저희는 사내에서 조직별로 구성된 AI Evangelist로 활동 중이며 이번 Tech-Verse 2026에 참관자로 참여했습니다."
  - "LINE Plus의 사례로는 안건당 90%를 AI가 개발하고 사람은 10%만 검수하는 피처 파이프라인, 그리고 조직별 에반젤리스트를 통한 현장 중심(bottom-up) 확산 전략이 소개되었습니다."
  - 에반젤리스트의 고민: "공통화가 개개인의 업무 상상력을 제한하고, 이미 앞서 달리는 누군가에게는 오히려 모래주머니가 될 수도 있겠다는 생각이 들었기 때문입니다."
- 바깥→안 대응: 'Evangelist'라는 DevRel 직함을 그대로 사내 조직별 AI 확산 담당자에게 붙임. 사내 컨퍼런스(Tech-Verse)가 외부 컨퍼런스 역할을 함
- 관련 섹션: 국내 사례 가운데 DevRel 어휘가 가장 직접 드러나는 사례. "표준화 대 개인 상상력" 긴장은 8장 논점으로 쓸 수 있음

## 자료 13: 당근 — 매주 AI Show & Tell, 해커톤, 피처톤, 월요일 데모 사이클
- 출처(확인): https://careers.daangn.com/blog/post/%EB%8B%B9%EA%B7%BC-ai-%ED%94%84%EB%A1%9C%EB%8D%95%ED%8A%B8-%EC%A1%B0%EC%A7%81%EB%AC%B8%ED%99%94-%EC%82%AC%EC%9A%A9%EC%9E%90%EA%B2%BD%ED%97%98/ ("AI가 만든 파도 위에서 당근이 서핑하는 법". about.daangn.com 주소에서 리다이렉트됨)
- 출처(미확인, Medium 403): https://medium.com/daangn/ai-%ED%88%B4-%EA%B0%9C%EB%B0%9C%EC%9D%80-%EC%B2%98%EC%9D%8C%EC%9D%B4%EB%9D%BC-%EB%8B%B9%EA%B7%BC-%EB%B9%84%EA%B0%9C%EB%B0%9C%EC%9E%90-%EA%B5%AC%EC%84%B1%EC%9B%90%EB%93%A4%EC%9D%98-ai-%EB%8F%84%EC%A0%84%EA%B8%B0-fb62d2a6c2f3 ("당근 AI Show & Tell #1", 비개발자 사례). 2회 요약본은 https://eopla.net/magazines/28600 (미확인)
- 저자·날짜: 당근 공식 채용 블로그, 2025-05-15(요약 모델이 추출한 날짜)
- 출처 성격: 회사 공식 블로그
- 신뢰성: 상
- 확인 여부: **확인(요약 경유)**. 인용문은 원문 대조가 필요함
- 무엇을: 매주 AI Show & Tell(팀별 실행 과정과 레슨런 공유. 검색 스니펫상 매주 화요일), 팀 단위 4일 해커톤, 월간 피처톤 데이(부동산팀), 운영실은 매주 월요일에 그룹별로 AI 기능 데모를 하고 한 주 동안 피드백을 반영하는 사이클을 돌림. 앞서 Gen AI 해커톤(1회)도 열었음(당근 블로그 별도 글, 미확인)
- 인용 가능한 구절(요약 경유이므로 원문 대조 필요):
  - "매주 열리는 AI Show & Tell 세션에서는 각 팀의 실행 과정과 레슨런을 생생하게 나누고 있죠"
  - "매주 월요일마다 각 그룹이 담당 AI 기능을 데모로 공유하고, 한 주 동안 피드백을 반영해 다시 개선하는 사이클이 자리 잡았어요"
- 바깥→안 대응: 밋업의 라이트닝 토크와 사례 공유가 매주 사내 Show & Tell로 옮겨가고, 외부 기술블로그와 Medium 연재로 다시 바깥에 공개됨(안팎 순환)
- 관련 섹션: 국내 "사례 공유 세션" 대표. 비개발자 발표 회차가 따로 있다는 점이 Block이 비개발 직군으로 넓힌 흐름과 대응함

## 자료 14: 토스 — 매주 금요일 'AI 서프 데이'와 OpenAI 공동 세션
- 출처: https://www.industrynews.co.kr/news/articleView.html?idxno=81391
- 저자·날짜: 인더스트리뉴스, 2026-05-25
- 출처 성격: 언론(회사 보도자료를 바탕으로 한 기사로 추정)
- 신뢰성: 중
- 확인 여부: **확인(요약 경유)**
- 무엇을: 토스가 매주 운영하는 실습 중심 사내 AI 학습 프로그램 'AI 서프 데이(Surf Day)'(요약상 금요일). 특별 회차로 OpenAI와 'AI 협업 세션'을 열어 OpenAI 전문가 강연과 미니 해커톤(AI 도구 설계 트랙, 업무 프로세스 적용 트랙)을 진행함
- 효과 수치(회사 발표를 기사가 전함): 약 400명 참여(온·오프라인), 만족도 4.7/5
- 인용 가능한 구절(요약 경유):
  - "이어 열린 미니 해커톤은 △AI 도구 자체를 설계하는 트랙 △실제 업무 프로세스에 AI를 적용하는 트랙 등 두 분야로 운영됐다."
- 바깥→안 대응: 벤더 DevRel(OpenAI)의 강연과 해커톤이 고객사 사내 정례 학습 프로그램 안으로 들어옴
- 관련 섹션: Canva와 짝을 이룸. 외부 벤더 DevRel이 고객사 사내 확산 장치의 일부가 되는 흐름

## 자료 15: 우아한형제들 — 우아톤 2026 (AI 활용 12시간 해커톤, AI 예선 평가)
- 출처: http://www.newsworker.co.kr/news/articleView.html?idxno=432492
- 저자·날짜: 뉴스워커. 행사 2026-06-22(기사 게시일은 확인 못 함)
- 출처 성격: 언론
- 신뢰성: 중
- 확인 여부: **확인(요약 경유)**
- 무엇을: "AI와 함께 업무는 더 스마트하게, 서비스는 더 새롭게"라는 슬로건 아래 기획, 구현, 발표자료까지 전 과정에 AI를 쓰는 12시간 해커톤. 개발자, 기획자, 디자이너가 참가함. 예선은 AI가 코드·문서·데모를 분석한 평가에 동료 평가를 더해 결선 10팀을 뽑음. 결선은 대표, CTO, CPO가 심사함
- 인용 가능한 구절(요약 경유):
  - "AI가 참가팀의 코드와 문서, 데모 등을 분석해 평가한 결과와 동료 평가 점수를 합산해 결선 진출 10개 팀을 선발했다."
- 바깥→안 대응: 외부 해커톤 형식을 사내로 옮기고, 심사 자체에도 AI를 넣음
- 관련 섹션: 국내 해커톤 사례. 경영진이 심사에 참여한 점은 Zapier의 "리더가 해커톤에 직접 참여" 원칙과 대응함

---

## 대조 사례 (DevRel 방식이 아닌 명령·계측 중심)

## 자료 16: Coinbase — 일주일 안 온보딩 명령과 해고, 이후 월간 공유 모임
- 출처: https://techcrunch.com/2025/08/22/coinbase-ceo-explains-why-he-fired-engineers-who-didnt-try-ai-immediately
- 저자·날짜: Julie Bort, TechCrunch, 2025-08-22. 원 발언은 John Collison의 팟캐스트 "Cheeky Pint"
- 출처 성격: 언론
- 신뢰성: 상
- 확인 여부: **확인(요약 경유)**
- 무엇을: CEO가 엔지니어링 Slack에 "이번 주 안에 Copilot·Cursor 온보딩"을 지시함. 따르지 않은 사람은 토요일 미팅에 부르고 일부는 해고함. 이후 팀들이 AI 활용법을 공유하는 월간 모임을 도입했다고 함
- 인용 가능한 구절(요약 경유): "AI is important. We need you to all learn it and at least onboard." (AI는 중요하다. 모두 배우고, 최소한 온보딩은 하라.)
- 대응: 명령으로 시작했지만 결국 공유 모임(DevRel식 장치)을 붙였다는 점이 대조 포인트

## 자료 17: Shopify — "기본값은 yes", 토큰 리더보드
- 출처: https://www.firstround.com/ai/shopify
- 저자·날짜: First Round Review, 2025-07-15(요약 모델이 추출한 날짜). Farhan Thawar(VP & Head of Engineering) 인터뷰
- 출처 성격: VC 매체 인터뷰
- 신뢰성: 상
- 확인 여부: **확인(원문 대조)**
- 무엇을: 2021년 말부터 Copilot을 도입해 채택률 80%. Cursor 라이선스 1,500개를 주문했다가 1,500개를 더 조달함. 법무가 기본값으로 "yes"를 말하게 함. 사내 토큰 사용 리더보드를 둠(쿼터는 없음)
- 인용 가능한 구절:
  - "If you don't default to 'yes,' you're defaulting to 'no.'" — Farhan Thawar (기본값이 'yes'가 아니면 'no'를 기본값으로 둔 것이다.)
  - "I know folks who are proud to show up on the top 10 token spend leaderboard due to valuable work being done." (가치 있는 일을 해서 토큰 사용 상위 10위에 오른 걸 자랑스러워하는 사람들을 안다.)
- 대응: 접근 장벽 제거와 사용량 계측이 중심이고, 커뮤니티 장치는 이 글에 드러나지 않음. 참고로 cryptobriefing 기사는 Shopify 엔지니어링 책임자가 나중에 토큰 리더보드를 실수라고 불렀다고 전함(미확인: https://cryptobriefing.com/shopify-token-leaderboard-mistake-ai/)

## 자료 18: Cloudflare — iMARS 태스크포스, AGENTS.md 3,900개 리포
- 출처: https://blog.cloudflare.com/internal-ai-engineering-stack/
- 저자·날짜: Ayush Thakur, Scott Roemeschke, Rajesh Bhatia, Cloudflare Blog, 2026-04-20(검색 결과 미러 기준)
- 출처 성격: 회사 공식 엔지니어링 블로그
- 신뢰성: 최상
- 확인 여부: **확인(원문 대조)**
- 무엇을: 전사 엔지니어로 꾸린 tiger team iMARS(Internal MCP Agent/Server Rollout Squad). 이후 지속 업무는 Dev Productivity 팀이 맡음. AI Gateway, MCP Portal, 수천 개 리포에 AGENTS.md 생성, AI Code Reviewer
- 효과 수치(Cloudflare 집계, 최근 30일): 사내 사용자 3,683명(전사 60%, R&D 93%), 전체 직원 약 6,100명
- 인용 가능한 구절:
  - "In the last 30 days, 93% of Cloudflare's R&D organization used AI coding tools powered by infrastructure we built on our own platform." (최근 30일 동안 Cloudflare R&D 조직의 93%가 자사 플랫폼 위에 만든 인프라로 돌아가는 AI 코딩 도구를 썼다.)
- 대응: 플랫폼 엔지니어링과 Dev Productivity 경로. 사람 네트워크가 아니라 인프라·컨텍스트 파일로 확산시킴. Block의 Repo Quest(AGENTS.md를 게임으로 채우게 함)와 대비됨

---

## 교차 관찰 (8장 서술 힌트)

1. **DevRel 직함 자체가 안으로 향하는 증거는 채용 공고에 있다.** ING("adoption of AI inside the engineering organization"를 DevRel 팀이 책임짐)와 Intuit(Developer Advocacy 팀이 사내 GenAI를 활성화함). LINE Plus는 'Evangelist' 직함을 사내 조직별 담당자에게 붙임.
2. **옮겨간 장치 목록**: 오피스아워(Duolingo 15분 예약, GitHub, Block, Carta), 밋업·Show & Tell(Duolingo 격주, 당근 매주, Carta), 해커톤(Zapier, Atlassian, Canva, 토스, 우아한형제들), 챔피언·앰배서더 네트워크(GitHub, Microsoft 약 1만 명, Block 50명), 게임화 온보딩(Block Repo Quest), 커뮤니티 채널(Zapier #fun-ai, Duolingo, Carta), 녹화 튜토리얼·지식 허브(Zapier, Intuit).
3. **GitHub의 정의 "part coach, part translator, part feedback loop"는 DevRel 정의를 사내로 옮긴 문장이다.** 8장 핵심 인용 후보.
4. **벤더 DevRel이 고객사 안으로 들어온다**: Canva(Anthropic·OpenAI·Google 팀 초청), 토스(OpenAI 공동 세션). 기존 Anthropic 교육 공고 사례와 한 흐름.
5. **대조**: Coinbase(명령)와 Shopify(접근·계측), Cloudflare(인프라). 명령으로 시작한 Coinbase도 결국 공유 모임을 붙였다는 점이 서술에 쓸 만함.
6. **수치는 모두 당사자가 스스로 보고한 것이다.** 제3자가 검증한 효과 수치는 이번 수집에서 찾지 못함. 이 점을 본문에 밝혀야 함.

## 수집 한계

- Canva 뉴스룸(403)과 당근 Medium(Cloudflare 차단)은 열지 못함. Fortune 기고와 당근 채용 블로그로 대체함.
- 당근, 토스, 우아한형제들, Coinbase의 인용문은 요약 모델을 거쳤으므로 fact-checker가 원문과 대조해야 함.
- ING 공고는 게시일이 없음. Intuit 공고 연도(2024)는 Job ID로 추정한 것임.
- Halliburton "Senior Developer Advocate"(사내 AI 코딩 활성화) 공고는 검색 스니펫에만 있고 URL은 404라 제외함.
- 후보 가운데 Stripe, Vercel, Twilio, Postman, MongoDB, Notion, Moderna, Morgan Stanley, Klarna, Accenture/Deloitte는 이번 라운드에서 DevRel 방식이 드러나는 공개 1차 자료를 찾지 못해 제외함(찾지 않은 것이 아니라 시간 안에 확인하지 못한 것).
- 네이버·우아한형제들 기술블로그에서 DevRel 조직이 사내 AI 확산을 맡았다는 1차 글은 찾지 못함.
