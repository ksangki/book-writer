# 5장. 'R'의 수단이 바뀌었다 — 콘텐츠·커뮤니티·퍼널 다시 배선하기

2026년 1월 7일, GitHub의 한 풀 리퀘스트 댓글창. 제목은 "feat: add llms.txt endpoint for LLM-optimized documentation"이었다. 2025년 11월 외부 기여자가 연 PR이다. Tailwind CSS 문서 사이트에 LLM이 읽기 좋은 문서 엔드포인트를 추가하자는, 겉으로는 평범한 제안이었다. 전날 이 제안에 난색을 보였던 Tailwind Labs의 창업자 Adam Wathan이 다시 댓글을 달았다.

"the reality is that 75% of the people on our engineering team lost their jobs here yesterday because of the brutal impact AI has had on our business."

AI가 사업에 준 타격 때문에 어제 엔지니어링 팀의 75%가 일자리를 잃었다는 고백이다. 문서를 에이전트가 읽기 쉽게 만들자는 PR 아래에서 이 말이 나왔다. 문서를 만드는 회사의 엔지니어 넷 중 셋이 전날 일자리를 잃은 것이다. 이 장면에는 이 장이 붙들 질문이 모두 들어 있다. 문서는 누구를 위한 것인가. 관계는 어디서 맺어지는가. 그리고 그 관계에서 나오던 돈은 어디로 갔는가.

## Tailwind의 역설

Wathan의 설명을 조금 더 들어보자. 같은 날 그는 이렇게 썼다. "Traffic to our docs is down about 40% from early 2023 despite Tailwind being more popular than ever. The docs are the only way people find out about our commercial products, and without customers we can't afford to maintain the framework." 문서 트래픽이 2023년 초보다 약 40% 줄었고, 문서가 유료 제품을 알리는 유일한 통로였다는 말이다. 고객이 없으면 프레임워크를 유지할 수 없다는 말도 덧붙였다.

그는 한 문장을 더 붙였다. "our revenue is down close to 80%." 매출이 80% 가까이 줄었다는 뜻이다.

숫자를 차분히 정리해두자. 문서 트래픽은 2023년 초 대비 약 40% 줄었다. 매출은 80% 가까이 줄었다. 엔지니어링 팀 넷 중 셋이 일자리를 잃었다. 75%는 엔지니어 4명 중 3명이다. HN 토론의 한 사용자가 이 점을 짚었고, Business Insider 기사 제목도 같은 사실을 전했다. 이 수치들은 모두 회사 창업자의 1차 증언이다(집계 방법 미공개). 회사 자체 수치라는 라벨을 붙여 읽자.

역설은 Wathan 자신의 문장 안에 있다. 그는 스스로 "more popular than ever", 곧 그 어느 때보다 인기 있다고 했다. 그런 프레임워크의 문서 트래픽이 40% 줄었다. Wathan은 원인을 AI가 사업에 준 타격이라고 불렀다. 그 영향이 어떤 경로로 왔는지는 이렇게 읽어볼 수 있다. 개발자가 문서를 열기 전에 코딩 에이전트가 이미 Tailwind 클래스를 써준다. 문서를 읽는 주체가 사람에서 모델로 옮겨가면 방문 기록은 남지 않는다. 문제는 Tailwind의 사업 모델이 바로 그 방문 위에 서 있었다는 점이다. 문서가 유료 제품을 알리는 유일한 입구였기 때문이다.

![그림 5-1. 문서가 유료 제품의 입구였던 Tailwind의 퍼널에 코딩 에이전트가 끼어든 자리](figures/fig-5-1.svg)

전날 그가 PR에 남긴 댓글은 이 사정을 더 날카롭게 보여준다. "making it easier for LLMs to read our docs just means less traffic to our docs which means less people learning about our paid products and the business being even less sustainable." LLM이 문서를 읽기 쉽게 만들수록 문서 트래픽이 줄고, 유료 제품을 알게 되는 사람도 줄어든다는 말이다. 에이전트가 읽기 좋은 문서를 만들수록 입구는 더 좁아진다. 문서 담당자라면 참으로 난감한 처지다.

4장에서 본 Supabase는 말 한 번 나눈 적 없는 빌더들에게 에이전트를 통해 채택되었다. Tailwind는 같은 흐름의 반대편 끝에 선 사례다. 두 이야기는 한 현상의 양면으로 읽을 수 있다. 채택과 수익이 서로 따로 움직이기 시작한 것, 이른바 채택과 수익의 탈동조화다.

HN 토론의 한 사용자는 이 현상을 자기 경험으로 설명했다. Claude 같은 모델이 Tailwind를 설치하지도 않은 프로젝트에 Tailwind 클래스를 넣으려 한 적이 여러 번 있다고 했다. 그리고 "LLMs has a bias toward tailwind css"라고 썼다. LLM이 Tailwind 쪽으로 기운다는 말이다. 그는 이것이 사업 모델의 문제라고 덧붙였다(원문 "a business model issue"). 개인의 체감이지만, 모델이 좋아하는 것과 회사가 돈을 버는 것 사이에 연결 고리가 끊겼다는 진단으로는 정확하다.

> **반론:** 트래픽이 줄었다는 사실만으로 AI를 원인으로 단정할 수 있을까? HN 토론에서 zdragnar는 "The real signal is conversions."라고 반박했다. 진짜 신호는 전환율이라는 말이다. 방문자 가운데 구매·가입으로 이어지는 비율이 그대로인데 트래픽만 줄었다면 LLM이 원인 중 하나라고 볼 수 있다. 하지만 전환율을 보지 않고서는 알 수 없다는 지적이다. 해고를 AI 탓으로 돌리는 서사 자체를 의심하는 댓글도 있었다. Tailwind가 방법을 공개하지 않은 이상 이 반론은 유효하다.

이 이야기에는 후일담이 있다. HN에서 이 소식이 크게 퍼진 다음 날, Google AI Studio가 Tailwind CSS를 후원한다는 소식이 이어졌다. 문서가 퍼널의 입구 노릇을 하던 모델이 깨졌다면, 관계는 이제 어디서 시작될까?

## Stack Overflow 이후, 개발자는 어디서 묻나

관계가 맺어지던 또 하나의 통로가 있다. 개발자들이 서로 묻고 답하던 공간이다. DevRel에게 이런 공간은 오랫동안 무대였다. 자기 제품에 관한 질문에 답을 달고, 태그를 지켜보며 어디서 사람들이 막히는지 읽었다. 그 무대는 지금 어떻게 되었을까?

연구가 그린 그림부터 보자. del Rio-Chanona, Laurentsyeva, Wachs는 2024년 *PNAS Nexus*에 논문을 실었다. ChatGPT 출시 후 6개월 동안 Stack Overflow의 활동이 비교 대상 플랫폼 대비 약 25% 줄었다는 추정이다. 비교군은 ChatGPT 접근이 제한된 러시아어·중국어 개발자 Q&A와, ChatGPT가 상대적으로 약했던 수학 포럼이었다. 차분의 차분이라는 방법으로 얻은 추정치다. 저자들은 이 값을 실제 영향의 하한으로 해석했다.

Burtch, Lee, Chen이 같은 해 *Scientific Reports*에 발표한 연구는 다른 각도에서 비슷한 결과를 보였다. Stack Overflow의 일일 웹 트래픽이 하루 약 100만 명 줄었다는 추정이다. ChatGPT 출시 직전 트래픽의 약 12%에 해당한다. 여기서 두 가지 발견을 눈여겨보자. 하나는 감소가 신규·주니어 사용자에게 집중되었다는 점이다. 다른 하나는 같은 기간 Reddit의 개발자 커뮤니티에서는 감소의 증거가 보이지 않았다는 점이다. 저자들은 이를 이렇게 해석했다. "suggesting the importance of social fabric as a buffer against the community-degrading effects of LLMs." 사람들 사이의 사회적 결속이 완충재 역할을 했다는 뜻이다.

2026년 9월에 나온 Ibrahim과 Zaki의 논문도 같은 방향을 가리킨다(동료 검토 전 논문, 프리프린트). Reddit의 정보성 커뮤니티에서 도움 요청 게시물이 3.4%보다 크게 줄었을 가능성을 배제했다고 보고했다. 공개된 지 몇 주 되지 않은 논문이다. 앞의 두 연구와 방향이 같다는 정도로만 읽어두자.

사람들은 왜 떠났을까? 답의 질이 이유였다면 이야기가 단순했을 것이다. 그런데 Kabir 등이 CHI 2024에서 발표한 연구는 다른 그림을 보여준다. 2023년 당시 ChatGPT가 Stack Overflow 질문 517개에 내놓은 답 가운데 52%가 부정확했고 77%가 장황했다. 2023년 모델 기준의 결과이니 지금 모델에 그대로 적용할 수는 없다.

그 시점에 사람들을 움직인 요인은 Hasan 등의 2024년 연구가 짚는다(동료 검토 전 논문). Stack Overflow가 "often suffers from unpleasant comments, reactions, and long waiting times" 한다는 것이다. 불친절한 댓글과 반응, 긴 대기 시간을 자주 겪는다는 말이다. 커뮤니티 경험의 실패가 이동을 부추겼다는 해석이다.

현장의 체감도 비슷하다. 2026년 5월 HN 토론에서 한 사용자는 이렇게 썼다. "SO was clearly on the decline ... It peaked around 2017 ... ChatGPT just pushed it off the cliff." Stack Overflow는 2017년 무렵 정점을 찍고 기울던 중이었고, ChatGPT가 벼랑 끝에서 밀어버렸다는 말이다.

같은 토론에서 나온 다른 댓글은 더 멀리 내다본다. Stack Overflow가 커진 이유 가운데 하나는 Android API 문서 같은 공식 문서가 부족했기 때문이라는 것이다. 누군가 직접 방법을 알아내 답으로 올리기 전까지 그 지식은 어디에도 없었다. 또 다른 사용자는 이렇게 썼다. "In the LLM era there won't be a new Stack Overflow to train LLMs on going forward." LLM 시대에는 LLM을 학습시킬 새 Stack Overflow가 나오지 않으리라는 말이다. 공개된 자리에서 새 지식을 만들어내던 사람들이 떠나면, 다음 세대 모델은 무엇을 배울까? 이 질문은 DevRel에게 남의 일이 아니다. 새 기능이 나온 첫날, 그 기능에 대한 공개된 답을 누가 처음 쓰느냐의 문제이기 때문이다.

이 연구들을 한데 놓으면 윤곽이 잡힌다. 줄어든 것은 정답 하나를 얻으려고 모르는 사람에게 묻는 정보 교환형 공간이었다. 사람들이 서로를 알아보고 머무는 공간은 적어도 측정된 범위 안에서는 버텼다. DevRel의 R, 관계라는 글자가 왜 여전히 의미가 있는지를 짐작하게 하는 대목이다.

## 채널이 바뀌었다는 진단

DevRel 실무자들도 이 변화를 나름대로 읽고 있다. 2026년 6월 r/devrel에 올라온 글 하나가 흥미로운 진단을 내놓았다(커뮤니티 의견, 글 말미에 AI 작성 표기). 제목부터가 주장이다. "I think DevRel has a channel problem, not a content problem." 문제의 자리를 콘텐츠가 닿는 채널에서 찾는 진단이다.

작성자는 개발자가 콘텐츠에 반응하지 않는다는 불평이 잘못된 진단이라고 봤다. 블로그든 튜토리얼이든 모든 형식이 멈춰 앉아 읽는 개발자를 요구한다는 것이다. 그리고 이렇게 썼다. "that slot barely exists anymore." 앉아서 읽는 시간이라는 자리 자체가 거의 사라졌다는 말이다.

댓글에서 나온 한 줄은 더 직접적이었다. "Another channel is agents." 에이전트가 또 하나의 채널이라는 말이다.

또 다른 댓글은 체인지로그를 예로 들었다. "Developers do not consume changelogs narratively, they consume them by search, at the moment of breakage, six months after publication." 체인지로그가 읽히는 때는 무언가 깨진 순간, 발행 반년 뒤, 검색창 앞이라는 것이다. 그 검색을 하는 주체가 점점 에이전트가 되고 있다.

DevRel을 했던 사람으로서 이 글에서 가장 오래 남는 것은 진단의 순서다. 독자가 그 콘텐츠를 읽을 자리가 아직 있는지를 맨 먼저 묻는다는 점이다.

Block의 Angie Jones도 2025년 10월 글에서 비슷한 이야기를 했다. "SEO is basically dead (sorry). ... Views and clicks will decline. But that doesn't mean the content isn't impactful. Check your referrers and you'll see ChatGPT is bringing you your future community members." 유입 경로를 보면 ChatGPT가 미래의 커뮤니티 구성원을 데려오고 있다는 말이다. 콘텐츠의 영향력이 도착하는 경로가 달라졌다는 이야기이기도 하다.

국내 DevRel 실무자의 기록에서도 같은 장면이 보인다. 스스로를 SK플래닛 DevRel Manager라고 소개한 josephyang은 2025년 10월 20일 데보션에 기술 블로그 개선 실험을 정리했다. 그 글의 문장이다. "이제는 개발자뿐만 아니라 AI가 나와 회사의 글을 검색하고 읽는 시대가 되었고…" 개발자와 함께 AI도 회사의 글을 찾아 읽는 독자가 되었다는 말이다. 그는 사람의 조회수가 높지 않은 글이라도 AEO/AIO 전략에 맞춰 발행하면 AI가 잘 검색하는 사례가 있다고 적었다(필자 한 사람의 관찰).

1장에서 본 Salma Alam-Naylor가 작별 글에 적었듯 "The Internet and its communities have fragmented." 인터넷과 그 커뮤니티들이 조각났다는 뜻이다. 흩어진 곳이 어디인지도 짐작할 수 있다.

2025년 5월 HN의 한 사용자는 LLM이 새롭고 빠르게 변하는 도구에는 약하다고 지적했다. 그 빈틈을 여기저기 쪼개진 Slack 채널 같은 커뮤니티가 채운다고 했다. 그리고 이렇게 덧붙였다. "those aren't search-indexed" 그런 곳은 검색 색인에 잡히지 않는다는 말이다. 지식이 색인되지 않는 Discord와 Slack 채널로 조각나고 있다. 검색으로도, 모델 학습으로도 닿지 않는 곳에 새로운 지식이 쌓인다. 찜찜한 구조다.

형식 쪽에서도 변화가 있다. Rizèl Scarlett은 2025년 9월 글에서 바이브 코딩 대회 이야기를 했다. Block에서 오픈소스 DevRel을 이끌던 시절에 연 대회다. 처음에는 에이전트가 틀린 결과를 내도 지켜보는 재미가 있었다. 그런데 "once models improved, it felt like an outdated trick to watch agents generate a tool." 모델이 좋아지자 에이전트가 도구를 만들어내는 장면은 금세 낡은 묘기가 되어버렸다는 말이다. AI 데모 콘텐츠에는 유통기한이 있다. 그것도 모델의 발전 속도만큼 짧은 유통기한이다.

지금까지 살펴본 통로들을 한 표로 정리해두자.

| 통로 | 이 장이 본 변화 | 근거의 성격 |
|---|---|---|
| 문서 사이트 | Tailwind 문서 트래픽 2023년 초 대비 약 40% 감소 | 회사 창업자의 1차 증언, 방법 미공개 |
| 공개 Q&A (Stack Overflow) | 출시 6개월 활동 약 25% 상대 감소 / 일일 웹 트래픽 약 12% 감소 | 동료 검토 논문 2편 |
| 관계형 커뮤니티 (Reddit) | 감소 증거 없음 / 정보성 요청 3.4% 초과 감소 배제 | 동료 검토 논문 / 프리프린트 |
| 검색 | "SEO is basically dead", 챗봇이 새 구성원을 데려옴 | 실무자 블로그 |
| 비색인 채널 (Discord·Slack) | 새 도구의 지식이 검색되지 않는 방으로 흩어짐 | Hacker News 댓글 |
| 에이전트 | "Another channel is agents" | r/devrel 댓글 |
| AI 데모 콘텐츠 | 모델이 좋아지자 금세 낡은 묘기가 됨 | 실무자 블로그 |

표 5-1. 관계의 통로별로 본 변화와 그 근거

이 진단들을 모으면 한 문장이 된다. 콘텐츠가 도착하던 통로가 바뀌었다.

## 두 개의 퍼널, 세 개의 표면

통로가 바뀌었다면 콘텐츠도 통로에 맞게 다시 짜야 한다. 이 문제를 구체적으로 정리한 두 사람의 틀을 살펴보자.

Dewan Ahmed는 2026년 8월 갱신한 글에서 DevRel의 퍼널을 둘로 나눴다. 하나는 machine funnel이다. 문서, 구조화된 콘텐츠, MCP 서버처럼 정확성과 검색 가능성이 핵심인 경로다. 다른 하나는 human funnel이다. 영상, 워크숍, 서사와 의견처럼 신뢰를 쌓는 경로다. 그리고 그는 한 문장으로 권고했다. "Stop trying to make one piece of content serve both." 콘텐츠 한 편으로 두 퍼널을 다 채우려 하지 말라는 말이다.

왜 하나로는 안 될까? 두 경로가 요구하는 것이 다르기 때문이다. 에이전트가 가져가는 문서는 짧고 정확하고 조각마다 독립적일수록 쓸모가 있고, 서사나 농담은 잡음이 된다. 신뢰를 쌓는 콘텐츠에는 그 반대로 판단의 과정과 실패담이 필요하다. 한 편의 블로그 글로 두 가지를 다 하려 들면 어느 쪽에도 충분하지 않은 글이 나오기 쉽다.

Joe Karlsson은 2026년 4월 글에서 이 구도를 셋으로 늘렸다. "In 2026 there are three distribution surfaces to own, not one: human developers, search crawlers, and LLMs. Each breaks differently." 사람 개발자, 검색 크롤러, 그리고 LLM이라는 세 유통 표면을 모두 챙겨야 한다는 말이다. 세 표면은 각기 다른 방식으로 고장 난다.

그는 여기서 한 걸음 더 나간다. "your README, your examples directory, your API reference, and your SDK docs are your LLM marketing. Not your blog posts. Not your conference talks." LLM이라는 표면에서는 README와 예제 디렉터리, API 레퍼런스, SDK 문서가 곧 마케팅이라는 것이다.

![그림 5-2. 개발자·검색 크롤러·LLM — 세 유통 표면과 두 퍼널](figures/fig-5-2.svg)

그림 5-2처럼 세 표면을 두 퍼널에 이어보면 설계의 기준이 조금 선명해진다. 독자의 질문이 "이 함수의 인자가 무엇인가"처럼 정확성을 요구한다면, 그 답은 machine funnel에 두는 편이 낫다. 에이전트가 가져가기 좋은 레퍼런스와 예제로, 버전과 날짜를 분명히 해서. 독자의 질문이 "이 도구를 우리 팀에 들여도 될까"처럼 신뢰를 요구한다면, 그 답은 사람이 만든 이야기와 라이브 시연, 실패담이 담긴 자리에 두는 편이 낫다. 검색 크롤러는 그 사이에서 양쪽 모두로 사람을 보낸다.

조금 더 구체적으로 생각해보자. 당신이 SDK의 새 메이저 버전 릴리스를 맡았다고 해보자. 예전이라면 긴 블로그 글 한 편에 변경 사항과 개발 배경, 마이그레이션 방법을 모두 담았을 것이다. 두 퍼널로 나눠 보면 할 일이 달라진다. machine funnel 쪽에는 버전 번호가 붙은 체인지로그가 간다. 옛 코드와 새 코드를 나란히 둔 마이그레이션 예제, 폐기된 API를 명시한 레퍼런스도 간다. 에이전트가 이 조각들을 가져가 옛 버전 코드를 새 버전으로 옮길 수 있게. human funnel 쪽에는 왜 이 버전을 만들었는지, 어떤 선택을 버렸는지, 팀이 어디서 헤맸는지를 담은 이야기와 라이브 세션이 간다. 도구를 팀에 들일지 고민하는 사람이 판단할 수 있게. 한 편에 섞여 있던 것을 제자리에 나눠 놓는 일이다.

Karlsson의 문장 가운데 하나를 더 기억해두자. "Answering a developer question well in public is both community work and corpus work." 공개된 자리에서 질문에 잘 답하는 일은 커뮤니티 작업인 동시에, 다음 세대 모델이 배울 코퍼스를 만드는 작업이다. 한 번의 답변이 세 표면 모두에 닿을 수 있다.

다만 Karlsson 자신도 인정했듯, LLM 표면에서 무엇이 먹히는지 재는 방법은 아직 거의 풀리지 않았다(원문 "largely unsolved"). 그가 권하는 최선은 수동 점검이다. 분기마다 실제 고객의 질문으로 여러 모델에 직접 물어보고 결과를 기록하는 방식이다. 계기판은 아직 없는 셈이다.

## 슬롭과 치어리딩 — 신뢰를 잃는 가장 빠른 길

통로를 다시 배선하는 동안 더 빨리 무너질 수 있는 것이 있다. human funnel의 연료, 신뢰다.

2026년 9월 22일, Rachel Andrew는 Bluesky에 이런 글을 남겼다. Google DevRel 사이트에 실을 콘텐츠를 제안하는 메일이 개인 메일함으로 온다고 했다. 그것들이 "obvious AI slop (and all follow the same template)"이라는 것이다. 한눈에 보이는 AI 슬롭, 그것도 모두 같은 틀로 찍어낸 제안들이다.

같은 해 4월 Jake Archibald는 한 공식 개발자 계정을 두고 글을 썼다. 말이 되지 않는 AI 풍 답변을 쏟아낸다는 지적이었다. 그리고 이렇게 덧붙였다. "These accounts used to be run by DevRel. Now they're run by marketing." 그 계정들을 이제 마케팅이 운영한다는 주장이다(운영 주체는 작성자의 주장). 개발자들이 그 변화를 어떻게 받아들이는지는 분명히 보여준다.

DevRel 스스로도 불편함을 드러낸다. 2025년 9월 Bluesky의 한 글은 "every devrel position includes AI cheerleading at this point"라고 자조했다. 모든 DevRel 자리에 AI 응원단 역할이 딸려 온다는 것이다.

2025년 12월 Jen Looper는 동료들에게 이렇게 권했다. "push back on demands to use AI for all the things, especially in DevRel" 모든 일에 AI를 쓰라는 요구에 맞서자는 말이다.

왜 이것이 신뢰를 잃는 가장 빠른 길일까? 2장에서 본 경계 역할을 떠올려보자. DevRel이 개발자에게 신뢰를 얻는 근거는 "이 사람은 회사의 말을 그대로 옮기지 않는다"는 믿음이다. 회사를 대변하는 동시에 개발자를 대변한다는 양방향성이 곧 이 일의 신용이다. 그런데 DevRel이 AI 응원단이 되고 공식 채널이 슬롭으로 채워지면, 그 믿음이 가장 먼저 무너진다. 개발자 입장에서는 경계에 서 있던 사람이 회사 쪽으로 넘어가버린 것처럼 보인다.

Karlsson은 같은 글에서 신뢰가 무너지는 또 다른 경로를 짚었다. 영업 조직이 Discord 커뮤니티의 명단을 달라고 할 때다. "And if you just hand over a list, you've poisoned the well. Developers feel the room shift." 명단을 넘기는 순간 우물에 독을 푼 셈이 되고, 개발자들은 방의 공기가 바뀐 것을 알아챈다는 말이다. 커뮤니티를 퍼널의 한 단계로 취급하는 유혹은 측정 압박이 커질수록 강해진다. 2장에서 본 "Communities aren't funnels"라는 선언이 이 대목에서 다시 무게를 얻는다.

여기에 근본적인 한계도 하나 짚어둬야 한다. Dewan Ahmed는 이렇게 썼다. "A great DevRel team still cannot save a bad product." 뛰어난 DevRel 팀도 나쁜 제품을 살릴 수는 없다는 말이다. 2장에서 본 Windows Phone의 교훈과 같은 이야기다. 통로를 아무리 잘 다시 배선해도 흘려보낼 제품이 매력적이지 않으면 소용이 없다.

Karlsson은 그래서 무엇을 만들기 전에 진단부터 하자고 권한다. 지금 겪는 문제가 콘텐츠 문제인가, 제품 문제인가, 유통 문제인가. 제품 문제를 가진 회사가 DevRel을 뽑아 튜토리얼을 찍어낼 수 있다. 그러면 돈을 쓰고 나서 DevRel은 효과가 없다고 결론 내리게 된다. 그리고 그 이유를 잘못 짚는다.

신뢰를 지키는 방법은 새롭지 않다. 콘텐츠를 늘리기 전에 진단하고, 제품의 한계를 숨기지 않는 일이다. 회사가 원하는 메시지와 개발자가 겪는 현실이 어긋날 때, 개발자 쪽의 목소리를 회사 안으로 들고 들어가는 일이다. 경계 역할이 원래 하던 일이다.

## 커뮤니티에 새 기여자가 들어왔다, 그리고 무엇을 셀 것인가

커뮤니티 쪽에서도 낯선 변화가 있다. 이제 기여자 가운데 에이전트가 있다.

Watanabe 등의 연구는 Claude Code로 만든 GitHub 풀 리퀘스트 567개를 분석했다(동료 검토 전 논문, 프리프린트). 그중 83.8%가 최종적으로 머지되었고, 머지된 것 가운데 54.9%는 추가 수정 없이 들어갔다. 한 도구, 한 시점의 표본이니 에이전트 PR 전체로 넓혀 읽지는 말자.

Peralta 등의 연구는 닫힌 에이전트 PR 1만여 개를 살펴봤다(MSR 2026 승인). 결론은 거절 결과만 보면 에이전트의 실패를 크게 과장하게 된다는 것이다. 원문 표현은 이렇다. "rejection outcomes substantially overstate agent error." 거절의 상당수는 워크플로 제약이나 관찰할 수 없는 사유 때문이었다는 것이다.

커뮤니티 운영자에게 이 발견은 새 숙제를 준다. Steinmacher 등이 2015년 CSCW에서 정리했듯, 오픈소스의 신규 참여자는 첫 기여 무렵 여러 장벽에 부딪힌다. 사회적 장벽도 있고 기술적 장벽도 있으며, 이 시기에 이탈이 잦다. 온보딩은 오랫동안 커뮤니티 운영의 핵심 과제였다. 이제는 그 온보딩 문서를 사람과 에이전트가 함께 읽는다. 기여 가이드와 에이전트용 지시문을 따로 두어야 할지, 하나로 써야 할지부터가 새로운 설계 질문이다.

Steinmacher 등이 2018년 ICSE에서 다룬 준기여자의 문제도 다시 볼 필요가 있다. 준기여자는 PR을 보냈지만 한 번도 받아들여지지 않은 외부 개발자다. 거절의 경험은 사람을 커뮤니티에서 떠나게 만든다. 에이전트가 쏟아내는 PR을 걸러내는 규칙을 만들 때도 이 점을 챙기는 편이 낫다. 그 규칙이 에이전트를 쓰는 사람 기여자에게 어떤 거절의 경험으로 닿을지까지 설계하자.

기여자가 늘어나는 곳에는 늘 허영 지표의 유혹이 따른다. Guo 등의 연구는 MCP 서버 마켓플레이스 여섯 곳을 수집해 분석했다(프리프린트). 그리고 제목에 가까운 질문을 던졌다. "Are MCP marketplaces truly growing, or merely inflated by placeholders and abandoned prototypes?" MCP 마켓플레이스가 정말 크는 것인지, 자리만 채운 항목과 버려진 시제품으로 부풀려진 것인지 묻는 말이다. 등록된 항목의 수가 늘어나는 것만으로는 생태계가 건강하다고 말할 수 없다는 경고다. 2장에서 본 CHAOSS와 SPACE가 오래전부터 한 말, 활동량은 건강을 말해주지 않는다는 말과 같은 이야기다.

그렇다면 무엇을 세야 할까? 2026년 7월 DevRelCon NYC 참관기가 좋은 출발점이 된다. 참관기에 따르면 1장에서 본 Joey deVilla의 세션은 설명 압박을 다뤘다. DevRel의 일이 채택·매출·유지 같은 결과에 어떻게 기여하는지 설명하라는 압박이다. Sean Keegan의 세션은 교육 지표를 예로 들어, 소비 지표 옆에 만든 흔적을 함께 보자고 했다. 참관기를 쓴 Ayodeji Ogundare는 두 세션을 정리한 뒤 이렇게 물었다. "What changed because this DevRel work existed?" 이 DevRel 활동이 있었기 때문에 무엇이 달라졌는가. 누군가 실제로 배포하고, API 호출에 성공하고, 포크하고, PR을 보낸 흔적이 그 답이 된다. 이 책은 이것을 '만든 증거'라고 부르려 한다. 참관기 작성자의 정리이니 발표 원문의 맥락은 따로 확인해두자.

국내에서도 비슷한 문장이 나왔다. 2026년 3월 GeekNews Weekly #350은 이렇게 썼다(편집자 미표기). "과거에는 Developer Evangelist가 컨퍼런스와 블로그, 샘플 코드를 통해 생태계를 키웠다면, 지금은 그 역할이 제품 안으로 더 깊이 들어와 핵심 레이어로 이동했습니다."

국내 커뮤니티 활동에서도 두 장면이 눈에 띈다. 2025년 8월 velog에 올라온 한 후기가 첫 장면이다. 필자는 스스로를 DevRel을 꿈꾸는 비개발 마케터라고 소개했다. 그가 처음 맡은 일은 "비개발자를 위한 바이브코딩 온라인 세미나" 기획이었다(커뮤니티 이름은 글에 나오지 않음). 그보다 앞선 2025년 6월에는 OKKY가 "AI시대 IT업계 일자리 위기 끝장토론회"를 열었다. 참관기에 따르면 패널들은 채용 감소를 두고 두 경우를 구분했다. AI 때문에 사람을 안 뽑는 것과 AI로 대체되었기 때문에 안 뽑는 것이다. 두 장면이 추세를 말해주지는 않는다. 다만 국내 개발자 커뮤니티의 대화 주제가 어디를 향하는지는 엿볼 수 있다.

관계의 통로는 이제 에이전트가 읽는 문서, 색인되지 않는 작은 방, 사람과 에이전트가 섞인 기여자 명단까지 넓어졌다. D와 R이 함께 움직였다는 진단은 여기까지다. 그렇다면 이 일을 하는 사람은 이제 뭐라고 불리나?

### 이 장의 한 줄

관계를 맺는 수단, 곧 무엇으로(R)의 무게가 에이전트가 읽는 정확한 문서와 측정된 범위에서 버틴 관계형 커뮤니티로 옮겨가고, 셀 것은 '만든 증거'가 된다.
