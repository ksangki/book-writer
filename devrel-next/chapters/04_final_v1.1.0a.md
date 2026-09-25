# 4장. 새 독자, 에이전트 — 문서를 가장 많이 읽는 것은 누구인가

당신이 Supabase의 DevRel이라고 해보자. 어느 분기부터 가입 그래프가 가파르게 솟는다. 반가운 일이다. 그런데 새로 들어온 사용자들이 어디서 왔는지 따라가 보니 이상하다. 당신이 발표한 컨퍼런스에서 온 사람도, 당신이 쓴 튜토리얼을 읽고 온 사람도 잘 보이지 않는다. 그들 가운데 상당수는 AI로 앱을 만들어주는 서비스를 거쳐 들어왔다. 그 서비스들은 당신 팀에 한 번도 연락한 적이 없다. 통합 가이드를 요청한 적도, 파트너십을 제안한 적도 없다. 그냥 어느 날부터 당신의 제품을 쓰고 있었다.

반가우면서도 어딘가 찜찜하지 않은가? 채택은 일어났는데, 그 채택 과정에 당신이 없었다. 누가 당신의 제품을 골랐을까?

## Supabase를 고른 것은 누구였나

이 장면은 2025년 7월 DevRelCon New York에서 Thor Schaeff가 "DX for Humans and Machines"라는 발표로 들려준 일화를 독자 자리로 옮겨본 것이다. Stripe와 Supabase를 거쳐 발표 당시 ElevenLabs에서 개발자 경험을 맡고 있던 그는, Bolt나 Lovable 같은 AI 빌더 서비스가 Supabase를 통합한 과정을 이렇게 전했다. 그들은 Supabase를 "without ever talking to us" 통합했다. 사전에 흐름을 알아채지도 못했다. 이유는 단순했다. LLM에게 데이터를 저장해야 하는데 무엇을 쓰면 되느냐고 물으면, LLM이 Supabase를 쓰라고 답했다는 것이다.

Schaeff는 지금 자기 팀에 정한 목표를 "developer experience for machines"라는 말로 설명했다. 그리고 그 배경을 이렇게 요약했다. "Hey, actually now machines are writing the code." 코드를 쓰는 주체가 바뀌었으니, 개발자 경험을 설계할 대상도 바뀌어야 한다는 것이다.

발표에는 이 시기 가입자 수가 폭발적으로 늘었다는 주장도 나오지만, 그것은 발표자가 무대에서 한 말이고 Supabase가 공개한 수치로는 확인되지 않는다. 회사 쪽의 말로는 CEO의 인터뷰가 있다. Paul Copplestone은 2025년 4월 22일 Fortune 인터뷰에서 이렇게 말했다. "Our sign-up rate just doubled in the past three months because of vibe coding—Bolt, Lovable, Cursor, all those." 석 달 사이 가입 속도가 두 배가 됐다는 CEO의 발언이다. 이 장에서 붙잡을 것은 경로다. 개발자가 제품을 고르던 자리에 LLM의 추천이 끼어들었고, 그 추천은 DevRel과의 대화 없이 일어났다. 3장 끝에서 본 비개발 게임 개발자가 AI가 알려주는 대로 Supabase를 붙였던 장면과 같은 모양이다.

왜 하필 Supabase였을까? 발표에서 제시된 가설은 전 스택이 오픈소스이고 기반이 30년 된 Postgres라는 점이었다. LLM이 학습하는 동안 이미 충분히 읽어둔 기술이라는 뜻이다. 가설일 뿐이지만 방향은 분명하다. 에이전트가 당신의 제품을 추천할지는 에이전트가 당신의 제품에 대해 무엇을 읽었는지에 달려 있다.

2026년 4월 20일, Joe Karlsson은 같은 현상을 한 문장으로 정리했다. 검색창 앞의 개발자는 도구를 적극적으로 찾는 중이다. 하지만 AI 코딩 도구 안에서는 사정이 다르다. "In an AI coding assistant, the AI is solving a problem directly. It's not shopping. You have to already be there." AI는 곧장 문제를 풀러 가고, 그 순간 쓸 수 있는 것은 이미 알고 있는 도구뿐이다. 그러니 그 순간이 오기 전에 이미 거기 있어야 한다.

이 문장이 DevRel에게 난감한 이유는 분명하다. DevRel의 오래된 기술은 대부분 '쇼핑하는 개발자'를 겨냥했다. 비교 글, 시작 가이드, 컨퍼런스 부스, 데모가 모두 고르는 사람의 눈앞에 제품을 놓는 일이었다. 2026년 7월 DevRelCon에서 처음 발표한 Danielle Washington도 dev.to 회고(2026-07-28)에서 같은 과제를 적었다. "As developers begin using AI tools to discover products, evaluate options, and solve problems, our existing approaches to content and discoverability may need to change." 그렇다면 고르는 순간이 사람의 눈앞에서 사라지면, 그 기술들은 어디에 쓰여야 할까? 이 질문을 쥐고, 에이전트라는 독자가 어떻게 등장했는지부터 따라가보자.

## 에이전트를 위한 표준이 생긴 15개월

에이전트를 위한 문서와 인터페이스는 생각보다 짧은 시간에 한꺼번에 등장했다. 2024년 9월 3일부터 2025년 12월 9일까지, 15개월 남짓의 일이다.

```mermaid
timeline
    title 에이전트를 위한 표준·제품 타임라인
    2024-09 : llms.txt 제안 (Jeremy Howard)
    2024-11 : MCP 발표 (Anthropic)
    2025-01 : Agent Experience 명명 (Mathias Biilmann)
    2025-04 : GitHub 공식 MCP 서버 퍼블릭 프리뷰 : Cloudflare 원격 MCP 서버
    2025-08 : Vercel MCP 퍼블릭 베타 : 카카오 PlayMCP 베타
    2025-12 : Agentic AI Foundation 결성 (Linux Foundation)
```
그림 1. 에이전트를 위한 표준·제품 타임라인(2024-09~2025-12)

출발점은 2024년 9월 3일 Answer.AI의 Jeremy Howard가 낸 llms.txt 제안이다. 제안서는 스스로를 이렇게 소개한다. "A proposal to standardise on using an `/llms.txt` file to provide information to help agents use a website." 웹사이트 루트에 마크다운 파일 하나를 두고, 에이전트가 사이트를 쓰는 데 필요한 정보와 링크를 모아두자는 생각이다. 어디까지나 제안이라는 점을 기억해두자. 이 파일이 실제로 얼마나 읽히는지는 이 장 마지막에서 따로 따진다.

두 달여 뒤인 2024년 11월 25일, Anthropic이 Model Context Protocol(MCP)을 발표했다. AI 어시스턴트를 데이터가 있는 시스템, 곧 콘텐츠 저장소와 업무 도구와 개발 환경에 연결하는 새 표준이라는 설명이었다. 초기 도입 기업으로 Block, Apollo가, 개발 도구로 Zed, Replit, Codeium, Sourcegraph가 이름을 올렸다.

2025년 1월 28일에는 Netlify CEO Mathias Biilmann이 Agent Experience라는 말을 붙였다. 이 개념은 바로 다음 절에서 자세히 보자.

그다음은 제품이 따라왔다. 2025년 4월 4일 GitHub이 공식 MCP 서버를 퍼블릭 프리뷰로 내놓았고, 사흘 뒤인 4월 7일 Cloudflare가 원격 MCP 서버를 발표했다. Cloudflare는 이를 업계 최초라고 불렀다(회사 발표). 8월 6일에는 Vercel이 MCP를 퍼블릭 베타로 열었다. 처음에는 읽기 전용이었고, 연결할 때마다 OAuth 동의를 거치게 했다. 같은 8월 국내에서는 카카오가 PlayMCP를 베타로 열며 "국내 최초 MCP 실험 공간"이라고 소개했다. 이것 역시 회사의 자기 소개다.

마지막 장면은 2025년 12월 9일이다. Linux Foundation 산하에 Agentic AI Foundation(AAIF)이 결성됐고, MCP(Anthropic), goose(Block), AGENTS.md(OpenAI)가 창립 프로젝트로 들어갔다. 결성 발표는 MCP의 1년 성과로 월 SDK 다운로드 9,700만 건 이상, 활성 서버 1만 개 이상을 제시했다. 재단이 스스로 발표한 수치라는 점은 염두에 두자.

15개월을 이렇게 늘어놓으면 흐름이 보인다. 에이전트가 웹을 읽는 방법에 대한 제안이 먼저 나오고, 에이전트를 시스템에 연결하는 프로토콜이 뒤따르고, 그것에 이름이 붙고, 플랫폼 회사들이 제품으로 응답하고, 마지막에 중립 재단이 그 표준을 맡았다. 한 기술이 제안에서 제도로 옮겨 가는 과정이 이례적으로 압축돼 있다.

## Agent Experience — 에이전트도 사용자다

Biilmann이 2025년 1월 28일 개인 블로그에 쓴 글의 정의부터 보자. Agent Experience(AX)는 "the holistic experience AI agents will have as the user of a product or platform", 곧 AI 에이전트가 제품이나 플랫폼의 사용자로서 겪는 경험 전체다.

그는 이 말을 계보 위에 놓았다. 1993년 인지심리학자이자 디자이너인 Don Norman이 사용자 경험(UX)이라는 말을 만들었고, 2011년 Jeremiah Lee가 개발자 경험(DX)이라는 말을 만들었다. 이제 에이전트가 우리 제품과 자율적으로 상호작용하는 시대에 들어서니, 제품 경험을 에이전트를 위해 따로 설계하기 시작해야 한다는 것이다. 그는 모든 소프트웨어 회사가 제품의 AX를 의식적으로 설계하지 않으면 대체될 위험이 있다고까지 썼다.

Biilmann은 반년쯤 뒤 X에 올린 글에서 실제 사례를 하나 들었다. Bolt가 사용자가 로그인하기도 전에 Netlify 사이트를 먼저 배포해두는 방식, 이른바 "Deploy first, claim later"다. 배포를 가입 앞에 두어, 에이전트가 먼저 일을 끝낼 수 있게 순서를 바꾼 셈이다. 에이전트가 사용자라면 온보딩도 에이전트의 순서에 맞춰 다시 짜야 한다.

그렇다면 AX와 DX는 어떤 관계일까? Netlify의 AX 페이지에 실린 Resend의 Zeno Rocha 말은 이 개념이 DX를 넓히는 쪽임을 보여준다. "AX doesn't replace DX, it extends it." Netlify CTO Dana Lawson은 2026년 6월 The New Stack 인터뷰에서 한 걸음 더 나갔다. 기사는 그의 정의를 이렇게 요약한다. "agent experience is a combination of developer experience and user experience." 그리고 그가 든 실제 변화가 흥미롭다. 에이전트용 오류 메시지를 더 분명하게 다듬고, 빌드 출력을 기계가 읽기 좋게 구조화하고, 불필요한 마찰을 걷어냈더니 사람 개발자도 덕을 봤다는 것이다. "Every human assumption we removed made the platform better for everyone."

이 대목이 중요하다. 에이전트를 위한 설계와 사람을 위한 설계는 상당 부분 겹친다. 같은 오류 메시지를 사람과 에이전트가 함께 읽고, 같은 빌드 로그를 둘 다 해석한다. 에이전트가 헤매는 자리는 대개 사람도 헤매던 자리이고, 그 자리를 고치면 둘 다 편해진다.

학계에는 이 개념의 가장 가까운 친척이 있다. 2024년 NeurIPS에 발표된 SWE-agent 논문(Yang et al., 동료 검토 학회 논문)은 에이전트-컴퓨터 인터페이스(ACI)라는 개념을 내놓으며 이렇게 썼다. "we posit that LM agents represent a new category of end users with their own needs and abilities, and would benefit from specially-built interfaces to the software they use." 언어 모델 에이전트는 자기만의 필요와 능력을 가진 새로운 범주의 최종 사용자이고, 그들이 쓰는 소프트웨어에 특별히 만든 인터페이스가 있으면 도움이 된다는 것이다. 에이전트가 쓰는 인터페이스도 설계 대상에 들어간다는 뜻이다. 'Agent Experience'라는 이름 자체를 다룬 학술 문헌은 아직 찾기 어렵지만, 생각의 뿌리는 이렇게 이어져 있다.

한 가지만 덧붙여두자. 이 책의 뒤쪽에서 'AX'라는 약어를 다른 뜻으로 다시 만나게 된다. 조직 안에 AI를 퍼뜨리는 일, 곧 AI 전환(AI Transformation)이다. 두 AX가 같은 글자를 쓰는 것이 무엇을 가리키는지는 8장에서 따져보기로 하고, 이 장에서 AX는 에이전트 경험만을 뜻한다.

## 트래픽은 정말 옮겨갔나 — 벤더 데이터 읽는 법

에이전트가 새 사용자라는 말은 그럴듯하다. 그런데 실제로 얼마나 읽고 있을까? 이 질문에 가장 구체적인 숫자를 내놓은 곳은 문서 호스팅 회사 Mintlify다.

Mintlify가 2026년 7월 29일 발표한 "The state of docs traffic: a 2026 midyear report"는 자사가 호스팅하는 문서 사이트 전체의 2026년 1~7월 트래픽을 집계했다. 결론은 이렇다. "Agents now account for 66% of measured web-traffic." 2026년 7월 한 달 동안 에이전트의 웹 요청은 2억 1,300만 건, 사람의 페이지 로드는 1억 500만 건이었다. 연초에 에이전트 비중은 15.2%였다. 반년 사이에 비중이 네 배 넘게 뛴 셈이다.

인상적인 숫자다. 그러나 이 숫자를 "문서 독자의 3분의 2가 에이전트"라고 옮기는 순간 곤란해진다. 세 가지를 함께 읽어야 하기 때문이다.

첫째, 단위가 다르다. 에이전트 쪽은 '요청' 수이고, 사람 쪽은 '페이지 로드' 수다. 보고서의 방법론에 따르면 에이전트는 알려진 AI 클라이언트 시그니처나 기계 판독용 경로로 들어온 요청으로 세고, 사람은 브라우저에서 일어난 페이지 로드로 센다. 에이전트는 문서 하나를 읽으려고 여러 번 요청을 보낼 수 있고, 사람은 한 페이지를 한 번 열어 오래 읽을 수 있다. 서로 다른 잣대로 잰 두 양을 한 분모에 넣으면 비율이 무엇을 뜻하는지 흐려진다.

둘째, 식별에 한계가 있다. 보고서도 스스로 인정한다. 정체가 드러나지 않는 중개자가 있고, MCP 대화를 구분할 식별자가 없으며, 에이전트가 문서를 가져가는 경로가 바뀌는 것만으로도 실제 작업량이 변한 것처럼 보일 수 있다.

셋째, 이해관계가 있다. Mintlify는 에이전트 친화 문서를 파는 회사다. 에이전트 트래픽이 크다는 결론은 이 회사의 사업에 유리하다. 그렇다고 데이터가 틀렸다는 뜻은 아니다. 다만 한 회사가 자사 고객의 문서에서 집계한 숫자이고, 사이트 수도 공개되지 않았다는 사실을 함께 적어야 한다.

이 숫자에서는 비율 자체를 조심스럽게 두고 방향을 가져가자. 적어도 Mintlify가 보는 문서들에서는 2026년 상반기 동안 기계가 보내는 요청이 빠르게 늘었고, 그 규모가 사람의 페이지 로드를 넘어섰다. 당신의 문서 서버 로그에서도 같은 일이 일어나고 있는지는 직접 확인해볼 수 있다. 벤더의 숫자를 인용하기 전에 자기 로그부터 열어보자. Mintlify가 보고서에 밝힌 식별 방법을 참고하면 시작은 어렵지 않다. 요청에 선언된 클라이언트 이름(GPTBot, ChatGPT-User, ClaudeBot, Claude-User, PerplexityBot, Google-Extended 등)을 찾고, `.md`나 llms.txt나 일반 텍스트처럼 기계가 주로 찾는 경로로 들어온 요청을 따로 모아보자. 정체를 밝히지 않는 에이전트는 이 방법으로 잡히지 않으니, 여기서 얻는 숫자는 하한으로 읽어두자.

## Stripe 문서가 보여주는 것 — 두 독자가 함께 읽는 문서

에이전트를 독자로 받아들인 문서는 실제로 어떤 모양일까? 2026년 9월 시점 Stripe 문서의 AI 빌드 안내 페이지(docs.stripe.com/building-with-ai)가 좋은 예다. 첫 줄부터 방향이 분명하다. "Give an AI agent access to Stripe, and build products that agents can use." 사람 개발자에게 건네는 이 첫 문장이 곧장 에이전트를 위한 장치들로 이어진다.

하나씩 살펴보자. 먼저 모든 docs.stripe.com 주소 뒤에 `.md`를 붙이면 같은 페이지를 마크다운으로 돌려준다. 같은 내용을 에이전트가 군더더기 없이 읽을 수 있는 텍스트로 받는 셈이다. 다음으로 OAuth로 연결하는 원격 MCP 서버(mcp.stripe.com)와 로컬에서 띄우는 MCP 서버가 함께 있어 에이전트가 Stripe에 직접 연결할 수 있고, Python과 TypeScript용 Agent Toolkit이 여러 에이전트 프레임워크를 지원한다. 그리고 에이전트 스킬 모음과 함께, 기계가 읽을 수 있는 스킬 카탈로그를 `/.well-known/skills/index.json`에 둔다.

```text
https://docs.stripe.com/{문서 경로}        # 사람이 여는 페이지
https://docs.stripe.com/{문서 경로}.md     # 같은 내용을 마크다운으로
https://docs.stripe.com/.well-known/skills/index.json  # 에이전트용 스킬 카탈로그
```

더 흥미로운 것은 문서가 에이전트에게 직접 지시를 내리는 방식이다. 한 블로그(Apideck, 2026-02-23)가 전하는 바에 따르면 Stripe의 llms.txt에는 에이전트용 지시문이 들어 있다. 예를 들면 이런 문장이다. "Always use the Checkout Sessions API over the legacy Charges API." 이 인용은 2차 자료를 거친 것이니 원문과 함께 확인하는 편이 낫다. 그래도 의도는 읽힌다. 모델이 학습한 옛 자료에는 구식 API를 쓰는 예제가 잔뜩 남아 있다. 모델은 그것을 그럴듯하게 추천할 것이다. 문서 쪽에서 "지금은 이것을 쓰라"고 말해주면 그 오래된 기억을 교정할 수 있다.

같은 흐름은 Google Cloud에서도 보인다. 2026년 8월 4일 Google Cloud 블로그에서 Lead Developer Relations Engineer인 Remigiusz Samborski는 Developer Advocate와 테크니컬 라이터가 이끈 태스크포스가 Google의 Agent Skills를 만든 과정을 소개했다. 그가 강조한 교훈은 이것이다. "a skill is a living product, not a one-off document." 스킬을 계속 고치고 가꿔야 하는 제품으로 다루라는 뜻이다. 그는 이렇게도 썼다. "AI agents are only as good as the instructions and context you give them."

두 사례를 겹쳐 보면 DevRel의 산출물 목록에 마크다운 엔드포인트, MCP 서버, 스킬, 에이전트용 지시문이 더해지고 있다. 그 목록을 만드는 사람으로 Developer Advocate와 테크니컬 라이터가 이름을 올렸다는 점도 눈여겨보자.

## 연구는 무엇을 말하나

벤더의 사례는 인상적이지만 효과를 증명하지는 않는다. 에이전트용 문서가 정말 도움이 되는지는 연구 쪽에서 따져봐야 한다. 아직 초기 연구가 대부분이고 상당수가 동료 검토 전 논문(프리프린트)이라는 점을 먼저 밝혀두자. 그래도 세 갈래의 발견은 짚어둘 만하다.

첫째, 문서 자체가 힘을 가진다. Hsieh 등(2023, 프리프린트)은 언어 모델에게 도구를 쓰는 시범 예제를 보여주는 대신 도구 문서만 줬을 때의 성능을 비교했다. 문서만 준 조건이 예제를 준 조건과 비슷하거나 더 나았고, 수백 개의 API가 있는 현실적인 과제에서는 문서만 준 쪽이 문서 없이 예제만 준 쪽을 크게 앞섰다. 저자들은 이렇게 썼다. "We advocate the use of tool documentation ... over demonstrations." 2023년 모델 기준의 결과이지만, 예제를 쌓는 것만큼 정확한 레퍼런스가 중요하다는 방향을 준다.

둘째, 에이전트를 위한 문서는 지금 꽤 엉성하다. Hasan 등(2026, 프리프린트)은 MCP 서버 103개에 들어 있는 도구 856개의 설명을 분석했다. 도구 설명의 97.1%에서 결함, 곧 '스멜'이 하나 이상 나왔고, 56%는 도구의 목적조차 분명히 밝히지 않았다. 여기서 단위를 잊지 말자. 서버의 97%가 불량이라는 뜻이 아니고, 도구 설명의 97.1%다. 설명을 보강하면 과제 성공률 중앙값은 5.85%p 올랐지만, 실행 단계 수가 67.46% 늘었다. 많이 쓴다고 꼭 좋아지지는 않는다는 신호다. 연구진이 왜 이 문제에 매달렸는지는 그들의 문장에 드러난다. 모델은 자연어로 된 도구 설명에 기대어 어떤 도구를 고를지, 어떤 인자를 넘길지 정한다. 도구 설명이 곧 에이전트의 사용 설명서라는 뜻이다. 사람을 위한 API 레퍼런스를 다듬던 테크니컬 라이팅의 기술이 여기서 그대로 쓰인다.

셋째, 무엇을 적느냐가 관건이다. Gloaguen 등(2026, 프리프린트)은 AGENTS.md 같은 저장소 수준의 컨텍스트 파일이 코딩 에이전트에게 도움이 되는지 평가했다. 결과는 기대와 달랐다. 컨텍스트 파일은 과제 성공률을 일반적으로 개선하지 않았고, 추론 비용은 평균 20% 넘게 늘렸다. 모델 제공사가 권하는 '저장소 개요'는 도움이 되지 않았다. 그런데 한 가지 예외가 있었다. 그 저장소만의 비표준 코딩 관행을 적어줄 때는 유용했다. 요컨대 컨텍스트 파일의 값은 모델이 모르는 정보에서 나왔다. Stripe가 구식 API 대신 새 API를 쓰라고 적어둔 지시문이 바로 그런 종류의 정보다.

빈 곳도 있다. Chatlatanagulchai 등(2025, 프리프린트)이 컨텍스트 파일 2,303개를 분석해보니 보안 요구를 명시한 파일은 14.8%에 그쳤고, Hasan 등의 다른 연구(2026년 4월 개정판, 프리프린트)는 오픈소스 MCP 서버 1,899개 가운데 7.2%에서 일반 취약점을, 5.5%에서 MCP 특유의 도구 오염(tool poisoning)을 찾았다. 에이전트용 산출물을 내는 순간 보안과 유지보수의 책임도 함께 따라온다.

이 모든 것이 완전히 새로운 이야기는 아니다. 2009년 Robillard가 Microsoft 개발자를 설문한 연구(IEEE Software, 동료 검토 논문, 응답자 83명·유효 80명)에서 API를 배우는 방법으로 문서를 읽는다고 답한 사람은 78%였다. 사람도 오래전부터 문서를 가장 먼저 읽었다. 이제 그 문서를 에이전트도 함께 읽는다.

## 반론 — llms.txt는 아무도 읽지 않는다?

여기까지 읽으면 에이전트용 문서를 서둘러 만들어야 할 것 같다. 잠시 멈추고 반대편 목소리를 들어보자. 이 논쟁은 생각보다 뜨겁다.

> **반론:** Google의 John Mueller는 2025년 llms.txt에 대해 "FWIW no AI system currently uses llms.txt."라고 말했고, 이 파일을 예전의 keywords 메타 태그에 견줬다(언론 인용). 블로그 약 8만 개를 운영한다고 밝힌 HermanMartinus는 2026년 6월 Hacker News에서 "/llms.txt is not requested by anything"이라고 썼다. 일반 페이지는 공격적으로 긁어가면서 llms.txt는 요청조차 없다는 것이다. MCP를 두고도 비슷한 말이 나온다. 2026년 3월 한 HN 사용자는 회사들이 'AI 우선'임을 증명하려고 MCP 서버를 서둘러 냈다며 "MCP adoption is a marketing signal not a technical one."이라고 했다.

이 반론에는 다시 반박이 따라붙었다. 같은 HN 토론에서 주요 AI 회사들도 자사 llms.txt를 게시한다는 지적이 나왔고, 한 사용자는 자기 회사 GitBook 문서에서 이 파일 요청이 꽤 보인다고 전했다. 그러자 또 다른 사용자가 선을 그었다. 원래 주장은 AI 회사들이 남의 사이트를 긁을 때 llms.txt를 읽지 않는다는 뜻이었다는 것이다. 게시하는 것과 소비되는 것은 다르다는 지적이다. 또 다른 사용자는 llms.txt보다 요청 헤더에 `Accept: text/markdown`을 보내면 마크다운을 돌려주는 방식이 더 널리 합의된 관행이라고 했다. Stripe의 `.md` 주소도 같은 계열이다.

MCP 쪽에서도 반박이 나왔다. 같은 2026년 3월 토론에서 한 사용자는 기업의 디자인 시스템 문서나 특정 UI 라이브러리처럼 방대한 문서를 에이전트에게 통째로 읽히면 컨텍스트가 금세 차버린다며, 이런 경우에는 MCP가 가장 낫다고 했다. 또 다른 사용자는 AI를 쓰는 사람이 개발자만이 아니라는 점을 짚었다. 마케팅이나 영업 도구를 ChatGPT나 Claude에 연결하려는 회사라면 MCP가 딱 맞는다는 것이다. 3장에서 본 넓어진 'D'가 여기서도 등장한다.

이 논쟁은 어떻게 정리하면 좋을까? 두 맥락을 나눠서 보는 편이 낫다. 하나는 검색 가시성 신호로서의 llms.txt다. 크롤러가 이 파일을 읽고 검색이나 답변 노출을 바꾸느냐는 질문이라면, 지금까지의 증언은 회의적이다. 다른 하나는 코딩 에이전트가 개발자 문서를 직접 가져가는 맥락이다. 개발자가 에이전트에게 특정 라이브러리 문서를 읽혀 작업하는 경우라면, 마크다운 제공과 정확한 레퍼런스와 비표준 규칙의 명시가 효과를 낼 여지가 크다. 앞 절의 연구가 가리킨 것도 이쪽이다. 어느 경우든 "llms.txt가 표준이 됐다"고 말하기는 이르다. 2026년 9월 시점에 이 파일은 여전히 제안이고, 관련 관행은 빠르게 바뀌고 있으니 공식 문서를 함께 확인해두자.

그리고 이 장을 닫기 전에 들어둘 목소리가 하나 더 있다. 에이전트가 제품을 쓸 수 있는지 점검해주는 도구 ax-check가 Hacker News에 소개된 스레드에, 2026년 9월 18일 xena라는 사용자가 이런 댓글을 남겼다. "As someone that works for a company that gets a 100% score on ax-check, all the effort I've put into making it accessible for agents has not 10xed the growth numbers like I was told it would." 같은 계정이 2024년 7월에는 막 DevRel에 들어왔다며 불안을 털어놓았던 사람이다. 2년 사이 그는 에이전트를 위한 일을 했고, 점수는 만점을 받았고, 약속받은 성장은 오지 않았다.

한 사람의 댓글로 AX 전체를 판정할 수는 없다. 하지만 이 문장은 이 장의 모든 내용 위에 물음표를 하나 얹는다. 에이전트가 문서를 읽는다는 것과, 그 독해가 제품의 성장으로 이어진다는 것 사이에는 아직 아무도 다리를 놓지 못했다. 그 다리가 어디에 놓여야 하는지는, 관계의 통로 전체를 다시 봐야 보인다.

### 이 장의 핵심

- AI 빌더와 코딩 에이전트는 DevRel과 대화하지 않고도 제품을 고른다(Supabase 일화). 추천의 순간에 에이전트가 기대는 것은 이미 읽어둔 문서와 학습 자료이니, 그 안에 먼저 있어야 한다.
- 2024년 9월부터 2025년 12월까지 15개월 사이 llms.txt 제안, MCP, Agent Experience 명명, 플랫폼들의 MCP 서버, AAIF 결성이 이어졌다.
- Agent Experience는 DX와 UX를 넓히는 개념이며, 에이전트를 위해 걷어낸 마찰은 사람에게도 이롭다.
- 에이전트 트래픽 수치는 벤더 자사 데이터이고 단위(요청과 페이지 로드)가 다르다. 방향으로 읽고, 자기 로그로 확인하자.
- 연구가 가리키는 원칙은 모델이 모르는 것(비표준 규칙, 최신 API)을 간결하게 적는 것이다. 에이전트 친화 문서의 실전 점검 항목은 부록 B에 모아두었다.
