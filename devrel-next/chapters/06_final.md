# 6장. 공고를 읽다 — 2026년 9월, DevRel 인접 직함 해부

2026년 9월 25일, AI·개발자 도구 회사 열세 곳의 채용 페이지를 같은 날 열어본다고 해보자. 대상은 Anthropic, OpenAI, Vercel, Supabase, Cloudflare, Cursor, Replit, Lovable, ElevenLabs, Stripe다. 여기에 Hugging Face, Google DeepMind, Mintlify를 더한다. 각 회사가 공개 채용 시스템(Greenhouse, Ashby)에 올려둔 목록을 하나씩 불러온다. 열 곳은 목록을 돌려준다. 세 곳(Hugging Face, Google DeepMind, Mintlify)은 같은 경로로 조회되지 않는다. 손에 남은 것은 열 개 회사의 그날 치 공고 목록이다.

이제 목록에서 DevRel이라는 단어를 찾아보자. 그리고 그 단어가 없는 공고들 가운데 DevRel이 하던 일을 적어둔 공고는 몇 건인지도 함께 세어보자. 어느 쪽이 더 많을까?

해부를 시작하기 전에 못 박아둘 것이 있다. 하루치 목록은 추세를 말해주지 않는다. 공고는 수시로 열리고 닫힌다. 제목 키워드로 센 숫자는 직무의 실제 내용과 어긋나기도 한다. 그래서 이 장의 숫자는 모두 **2026년 9월 25일 공개 목록 기준 예시**다. 그래도 하루치 목록으로 볼 수 있는 것이 있다. 회사가 이 일을 어떤 이름으로 부르고, 어떤 문장으로 설명하는지다.

## 같은 날 열어본 채용 페이지들

열 곳의 목록을 한 표에 모았다. 전체 공고 수는 같은 날에도 몇 건씩 오르내리므로 일부는 어림으로 적었다.

| 회사 (전체 공고, 약) | 외부 개발자 대상 DevRel·DX 제목 공고 | FDE·Applied AI·솔루션 계열 | 그 밖의 개발자 관련 공고 |
|---|---|---|---|
| Anthropic (약 630) | Developer Relations 1 | Applied AI 제목 38(서울 포함), FDE 4 + FDE 매니저 2 + Pre-Sales(FDE) 1 | Developer Education Lead 1(사내 영업 조직 대상), Copywriter, Developer 1 |
| OpenAI (약 830) | Developer Experience Engineer, Cyber 1 ("Developer Advocate" 제목 0) | "Forward Deployed" 제목 22 | TPM, Developer Experience 1(사내 개발 속도 조직) |
| Vercel (87) | DevRel Engineer, Agentic Infrastructure 1 | FDE 1, Solutions Architect 다수 | — |
| Supabase (55) | Developer Relations Engineer 3(SF·NY·런던) | — | — |
| Cloudflare (382) | VoidZero Developer Relations Engineer 1 | FDE 계열 10건 안팎 | — |
| Cursor (125) | 0 | FDE 계열 7~9, Solutions Architect 다수 | Startup Events & Community 1 |
| Replit (75) | 0 | FDE 1 | SWE, Developer Experience 1 |
| Lovable (79) | 0 | Solutions Architect | Community Manager 1 |
| ElevenLabs (약 220) | Developer Experience Engineer 1 | FDE 계열 16 | — |
| Stripe (약 690) | 0 | "Forward Deployed" 제목 5 | — |

표 6-1. 2026년 9월 25일 공개 채용 목록 스냅샷 (Greenhouse·Ashby 공개 API 조회, 제목 키워드 기준 — 추세 지표 아님. Hugging Face·Google DeepMind·Mintlify는 조회 실패)

표를 읽기 전에 두 가지를 짚자. 첫째, 이 열 곳을 모두 'AI 회사'라고 부르면 곤란하다. Anthropic과 OpenAI는 모델을 만드는 연구소다. Cursor·Replit·Lovable은 AI 코딩·빌더 도구를 만든다. Vercel·Supabase·Cloudflare·Stripe는 오래전부터 개발자를 고객으로 삼아온 플랫폼 회사다. 한 표에 모았다고 한 업종이 되는 것은 아니다.

둘째, 제목의 단어는 생각보다 미끄럽다. 'Developer Experience'라는 말이 좋은 예다. OpenAI의 Developer Experience Engineer, Cyber는 외부 개발자를 돕는 자리다. 그런데 같은 회사 목록에는 "Technical Program Manager, Developer Experience"도 있다. 사내 개발 속도를 다루는 자리다. Anthropic에는 사내 개발 환경을 다루는 것으로 보이는 Developer Experience 제목의 엔지니어 공고가 있다. Replit에도 같은 제목의 공고가 있는데, 성격이 분명하지 않다. 같은 단어가 가리키는 개발자가 공고마다 다르다. 그래서 표의 둘째 열에는 외부 개발자를 청중으로 삼는 공고만 넣었다. 나머지 가운데 일부는 넷째 열에 예로 적었다.

그렇다면 표에서 무엇이 보이는가? 제목에 'Developer Relations'나 'DevRel'이 들어간 공고는 모두 여섯 건이다. 네 회사(Anthropic·Vercel·Supabase·Cloudflare)에 나뉘어 있다. 'Forward Deployed'나 'Applied AI'가 들어간 공고는 여러 회사에 걸쳐 수십 건이다. 이 대비를 보고 "DevRel이 줄고 FDE가 늘었다"고 쓰고 싶어진다. 그 문장은 이 표로는 쓸 수 없다. 어제의 목록이 없으니 늘었는지 줄었는지 알 수 없다. 제목에 FDE가 붙은 자리가 DevRel의 일을 가져간 것인지도 제목만으로는 알 수 없다. 표가 허락하는 말은 이 정도다. 그날, 외부와 제품 사이에서 일할 사람을 찾는 공고 가운데 상당수가 DevRel 아닌 이름을 달고 있었다.

그 이름들 안에 무엇이 적혀 있는지 보려면 공고 본문을 열어야 한다. 먼저 여전히 DevRel이라는 이름을 쓰는 공고부터 읽어보자.

## 'DevRel'이라는 이름을 단 공고들

Anthropic의 Developer Relations 공고(2026-08-21 갱신)는 첫 문장에서 이 자리를 이렇게 설명한다. "help developers discover, onboard, and get the most out of Claude Code, Claude Tag, and future developer products." 개발자가 제품을 발견하고, 시작하고, 최대한 활용하도록 돕는 일이다.

여기에 청중의 폭을 적은 문장이 붙는다. 공고는 이해해야 할 개발자층을 "from individual hobbyists to enterprise engineering teams"로 적었다. 취미로 만드는 개인에서 기업 엔지니어링 팀까지라는 뜻이다. 3장에서 본 긴 띠가 공고 한 줄에 그대로 들어와 있다.

더 흥미로운 문장이 있다. "Help define what world-class AI developer relations looks like in this emerging field." 이 새로운 분야에서 세계 수준의 AI DevRel이 무엇인지 정의하는 일을 도와달라는 것이다. 채용 공고가 지원자에게 직무의 정의를 함께 만들자고 요청한다.

측정에 대한 문장도 있다. "Build frameworks and mechanisms for measuring developer success." 개발자의 성공을 측정할 틀을 만들라는 요구다. 전통적인 DevRel의 핵심 문장도 빠지지 않았다. "Act as an advocate for developer needs at Anthropic, translating developer feedback into concrete product and content initiatives." 회사 안에서 개발자의 필요를 대변하고, 개발자의 피드백을 구체적인 제품·콘텐츠 계획으로 옮기라는 것이다.

이 공고에는 보상 범위도 적혀 있다. "$290,000 — $435,000 USD." 연 29만~43만 5천 달러다. 다만 공고는 이 범위가 기본급과 영업 커미션·보너스 목표를 함께 포함한 금액이라고 밝혔다(OTE, 1차 공고, 2026-09-25 조회). 기본급으로 옮겨 적지 않도록 주의하자. DevRel 자리의 보상에 영업 성과 목표가 들어 있다는 점도 눈여겨볼 만하다. 이 자리의 성과가 어떤 식으로든 매출과 이어져 있다는 신호로 읽을 여지가 있다.

Vercel의 DevRel Engineer, Agentic Infrastructure 공고(2026-09-17 갱신)는 회사 소개부터 달라져 있다. "Vercel is the agentic infrastructure company, freeing people and agents to ship what's next." 회사가 스스로를 사람과 에이전트가 함께 쓰는 인프라라고 소개한다.

이 공고에서 가장 선명한 것은 배치다. "We're hiring a DevRel Engineer to work inside the product teams building Vercel's agentic infrastructure." DevRel Engineer가 에이전트 인프라를 만드는 제품 팀 안에서 일한다는 뜻이다. 보고 라인은 Head of AI Infrastructure다.

일의 순서도 적혀 있다. 먼저 출시 전에 직접 에이전트와 앱을 만들어본다. 그다음 배운 것을 데모·템플릿·오픈소스 프로젝트로 바꾼다. 개발자가 실제로 복제해 돌려보는 결과물이다. 공고는 이 일을 한 줄로 요약한다. "your job is to hit the rough edges first and make sure they get fixed before launch." 거친 모서리에 먼저 부딪히고, 출시 전에 고쳐지게 만드는 일이다.

지원 조건도 단호하다. 개발자에게 무언가를 가르친 결과물, 곧 발표·저장소·글·영상의 링크를 붙이라고 한다. 그리고 이렇게 못 박는다. "Applications without one will not be considered." 만든 것을 보여주지 못하면 지원서를 읽지 않겠다는 뜻이다.

Supabase는 같은 날 Developer Relations Engineer 공고 세 건을 열어두고 있었다(SF·NY·런던, 2026-08-21 게시). 청중을 설명하는 문장은 이렇다. "Our users are builders, startup founders, weekend hackers, and engineers scaling to millions of users." 사용자는 빌더, 스타트업 창업자, 주말 해커, 수백만 사용자를 감당하는 엔지니어라는 말이다. 문장의 첫 단어가 builders다.

Cloudflare의 VoidZero Developer Relations Engineer 공고도 있었다(2026-09-15 갱신). 찾는 사람은 "someone who identifies as a builder, teacher, mentor, and communicator"다. 스스로를 만드는 사람, 가르치는 사람, 멘토, 전달자로 여기는 사람이다. Cloudflare는 2026년 6월 4일 Vite·Vitest 등을 만든 VoidZero를 인수했다고 발표했다. 오픈소스 도구 생태계를 사들인 회사가 그 생태계를 돌볼 DevRel을 찾는 장면이다.

네 공고를 겹쳐 읽으면 공통점이 보인다. 청중을 넓게 잡는다(취미 개발자, 빌더, 에이전트). 만드는 사람을 원한다(결과물 링크, builder). 제품 가까이에 둔다(제품 팀, 피드백 번역). 이름 아래의 문장은 2장에서 본 에반젤리스트의 문장에서 꽤 멀리 와 있다.

## 이름을 바꾼 자리들

이제 DevRel이라는 이름을 달지 않은 공고를 열어보자. 가장 많이 보이던 FDE, 곧 Forward Deployed Engineer부터다.

Anthropic의 FDE 공고(2026-08-21 갱신)는 이 자리를 "embeds directly with our most strategic customers to drive transformational AI adoption"이라고 설명한다. 가장 전략적인 고객 안으로 직접 들어가 AI 도입을 이끄는 사람이다.

만드는 것도 구체적이다. "Deliver technical artifacts for customers like MCP servers, sub-agents, and agent skills that will be used in production workflows." 고객의 실제 업무에서 돌아갈 MCP 서버, 서브에이전트, 에이전트 스킬을 만들어 넘긴다는 뜻이다.

그리고 이런 문장이 이어진다. "Identify and codify repeatable deployment patterns and contribute insights back to our Product and Engineering teams." 반복되는 배포 패턴을 찾아 정리하고, 그 통찰을 제품·엔지니어링 팀에 되돌려준다는 것이다. 앞 절에서 본 DevRel 공고의 피드백 문장과 나란히 놓아보자. 되돌려주는 방향이 같다.

OpenAI에는 그날 'Developer Advocate' 제목의 공고가 없었다. 대신 Developer Experience Engineer, Cyber(2026-09-11 게시)가 있었다. 팀 소개는 이렇다. "The Developer Experience team at OpenAI has a singular focus: empowering developers globally." 전 세계 개발자에게 힘을 싣는 것 하나에 집중하는 팀이라는 말이다.

공고는 이 팀이 다루는 범위를 "the developer journey, from onboarding ... to first API call to production deployment"로 적었다. 시작부터 첫 API 호출, 실제 배포까지 개발자의 여정 전체다. 이 공고는 그 일을 보안이라는 한 도메인에 맞춘다. 사이버보안 역량을 개발자가 바로 실행해볼 수 있는 예제로 풀어내는 자리다. DevRel의 일이 도메인별로 쪼개지는 장면으로 읽을 수 있다.

Anthropic의 Copywriter, Developer 공고(2026-09-16 갱신)는 또 다른 분화를 보여준다. 공고는 청중을 "an audience that is notoriously allergic to being marketed to"라고 부른다. 마케팅에 알레르기가 있기로 악명 높은 청중이라는 뜻이다.

이 공고는 자리를 "the brand-led developer writing that sits between Dev Rel's technical content and pure marketing"이라고 설명한다. DevRel의 기술 콘텐츠와 순수 마케팅 사이에 놓인, 브랜드 중심의 개발자 대상 글쓰기다. 그리고 DevRel 팀에 붙어 매일 함께 일하라고 적었다. DevRel이 하던 콘텐츠 일 가운데 브랜드 쪽 글쓰기가 별도 직무로 떨어져 나온 것이다. 같은 회사에는 사내 영업 조직을 청중으로 한 개발자 교육 공고도 있었다. 그 이야기는 8장에서 따로 한다.

FDE라는 이름이 이렇게 흔해진 배경도 짚어두자. FT는 2025년 11월 무렵 "The new hot job in AI: forward-deployed engineers"라는 기사를 냈다. AI 업계의 새 인기 직업이 FDE라는 제목이다. FT 보도에 따르면 FDE 월간 채용 공고가 2025년 1월에서 9월 사이 800% 이상 늘었다(후속 기사들의 인용 기준). 다만 이 수치를 집계한 원 데이터 제공자는 확인하지 못했다.

그보다 앞서 a16z의 Joe Schmidt는 2025년 6월 4일 에세이 "Trading Margin for Moat"를 냈다. 이 글은 흐름을 "services-led growth"라고 불렀다. 구현 서비스를 제품에 붙여 파는 성장 방식이다.

그는 그 서비스를 맡는 사람이 "sometimes rebranded as a forward deployed engineer or an implementation/solutions specialist"라고 썼다. 때로는 FDE나 구현·솔루션 전문가라는 새 이름을 단다는 뜻이다. a16z의 집계로는 당시 OpenAI 공개 채용 311건 가운데 FDE·솔루션 직무가 22건이었다(2025년 6월 기준, VC 에세이). 표 6-1의 22건과는 시점도 집계 기준도 다르다. 투자사의 이해관계도 감안해 읽자.

a16z의 문장에서 'rebranded'라는 단어를 기억해두자. 오래된 직무가 새 이름을 얻었다는 뜻이다. 그렇다면 DevRel이라는 이름에서 떠난 사람들은 어떤 이름을 얻었을까?

## 사람들은 어디로 갔나

DevRel을 하던 사람들이 자기 직함이 바뀌었다고 공개적으로 밝힌 글도 있다.

Lee Robinson은 Vercel에서 5년을 일했다. 그리고 2025년 7월 18일 X에 이렇게 썼다. "I'm joining Cursor to teach the future of coding!" 코딩의 미래를 가르치러 Cursor에 간다는 소식이다. 3장에서 본 그의 인용은 바로 이 이동을 설명하는 글에서 나왔다. 그가 새로 맡은 일은 AI로 개발을 시작한 사람들을 가르치는 일이다.

cameron.stream은 2025년 7월 Letta에 "founding devrel engineer", 곧 창립 멤버 DevRel 엔지니어로 합류했다. 1년이 채 안 된 2026년 6월 16일, Bluesky에 이렇게 올렸다. "My title has changed from developer relations to Member of Technical Staff at @letta.com!" 직함이 developer relations에서 Member of Technical Staff로 바뀌었다는 소식이다. 같은 사람이 같은 회사에서 다른 직함을 얻었다.

1장에서 본 두 사람도 이 목록에 들어간다. Salma Alam-Naylor는 DevRel을 떠났고 프로필에 Staff Engineer를 적었다. Lee Briggs는 DevRel을 떠나 Tailscale의 Sales Engineer가 됐다.

청중을 새로 정의한 기록도 있다. Microsoft의 Dona Sarkar는 2025년 1월 17일 조직 개편 소식을 전했다. 그리고 "the newly announced AI Power Users DevRel team"을 맡게 됐다고 썼다. 새로 생긴 'AI 파워 유저 DevRel 팀'이다. DevRel의 청중이 개발자에서 AI를 깊이 쓰는 사용자로 넓어진 이름이다.

Fly.io의 채용 공지(2025-06-11, Bluesky)는 이렇게 시작한다. "Is it DevRel? Not exactly. It's closer to a journalist, specifically someone who will learn and share how companies are building and deploying AI agents. We're not asking for evangelists – we're looking for storytellers." DevRel이라기보다 저널리스트에 가깝다는 설명이다. 회사들이 AI 에이전트를 만들고 배포하는 방식을 배우고 전할 사람, 곧 이야기꾼을 찾는다는 공지다.

그리고 Kelsey Hightower는 2025년 7월 22일 공개적으로 연락을 청했다. 클라우드 네이티브 쪽 DevRel 가운데 AI 인프라로 옮기고 싶은 사람에게 좋은 기회가 있다는 내용이었다.

이 기록들을 어떻게 읽어야 할까? 저마다 사정이 다른 이직 소식이지만, 모아 놓으면 몇 가지 방향이 보인다. 첫째는 기술 직무로 흡수되는 방향이다(Member of Technical Staff, Staff Engineer). 둘째는 고객과 매출 쪽으로 가는 방향이다(Sales Engineer). 셋째는 가르치는 일로 초점을 좁히는 방향이다(Cursor의 AI 교육). 넷째는 이야기를 쓰는 일로 옮기는 방향이다(Fly.io). 다섯째는 청중을 새로 정의하는 방향이다(AI Power Users).

다만 이것은 스스로 공개한 사람들의 기록이다. 조용히 떠났거나 그대로 남은 사람은 이 목록에 없다. 대표성을 주장할 수 있는 표본이 아니라는 점을 잊지 말자.

![그림 6-1. DevRel이라는 이름을 떠난 공개 기록들 — 다섯 방향](figures/fig-6-1.svg)

남은 것은 가장 많이 보이던 이름, FDE와 DevRel의 관계다.

## FDE는 DevRel을 대체하는가

이 질문에 정면으로 답한 글이 있다. AI Engineer World's Fair 2026 취재기다(Daily Context, Dev.to 2026-07-02). 글은 이렇게 시작한다. "AI products fail at integration, not awareness." AI 제품이 실패하는 지점은 제품을 연결하고 붙이는 단계라는 진단이다. 그리고 글은 퍼널을 둘로 나눈다.

> "DevRel owns the top of the funnel: awareness, winning the customer's attention. FDE owns the bottom: converting that attention into real usage. What gets squeezed is the middle."

퍼널의 양 끝을 두 직무가 나눠 맡고, 그 사이의 가운데가 눌린다는 그림이다.

한 문장이 더 있다. "A conference talk earns applause, but a merged PR in the customer's repo earns a renewal." 신뢰의 근거가 발표장에서 고객의 저장소로 옮겨간다는 문장이다.

반대쪽 읽기도 있다. Google의 Karl Weinmeister는 "What does FDE at scale look like? DevRel Engineering."이라는 제목의 글을 썼다. 규모를 키운 FDE가 곧 DevRel Engineering이라는 제목이다. 원문은 확인하지 못했고 요약만 확보했다(요약 기반, 원문 미대조). 요지는 DevRel Engineering을 FDE의 일을 많은 사람에게 넓힌 형태로 보는 것이다.

두 읽기 가운데 무엇이 맞을까? 공고 문구로 직접 확인해보자. DevRel 계열 공고와 FDE 공고에서 같은 일을 가리키는 문장을 기능별로 나란히 놓았다.

| 기능 | DevRel 계열 공고 문구 | FDE 공고 문구 (Anthropic) |
|---|---|---|
| 되돌려주기 | "translating developer feedback into concrete product and content initiatives" (Anthropic DevRel) | "contribute insights back to our Product and Engineering teams" |
| 만들어 보여주기 | "turn what you learn into demos, templates, and open source projects developers actually clone and run" (Vercel) | "Deliver technical artifacts for customers like MCP servers, sub-agents, and agent skills" |
| 먼저 써보기 | "your job is to hit the rough edges first" (Vercel) | "Identify and codify repeatable deployment patterns" |
| 가르치기 | "a link to something you made that taught developers something" (Vercel 지원 조건) | 해당 문구를 찾지 못했다 |
| 누구에게 | "from individual hobbyists to enterprise engineering teams" (Anthropic DevRel) | "our most strategic customers" |

표 6-2. 기능별 공고 문구 대조 — 2026년 9월 25일 조회한 공고 원문

표를 따라 읽어보자. 되돌려주기 행에서 두 공고의 동사는 거의 같다. 이 FDE 공고의 문장은 DevRel을 했던 사람에게 낯설지 않다. 만들어 보여주기 행도 닮았다. 다만 결과물이 향하는 곳이 한쪽은 복제해서 돌려볼 불특정 다수의 개발자이고, 다른 쪽은 계약한 고객의 실제 업무다. 가르치기 행은 비어 있다. 적어도 이 FDE 공고에서 가르치는 일은 명시된 업무가 아니었다.

그래서 이 둘을 '대체'로 부르기는 어렵다. 같은 기능이 다른 규모로 배치된 것에 가깝다. 한 번에 닿는 사람의 수를 가로축으로 놓아보자. 한쪽 끝에는 고객 한 곳 안으로 깊이 들어가는 자리가 있다. 먼 쪽에는 공개 문서와 데모로 수많은 개발자와 에이전트에게 닿는 자리가 있다. FDE는 앞쪽에, 전통적인 DevRel은 뒤쪽에 놓인다. Vercel의 DevRel Engineer처럼 제품 팀 안에서 출시 전에 먼저 부딪히는 자리는 그 사이 어딘가다. 무엇이 어디에 놓이는지는 회사가 어떤 고객에게 무엇을 파는지에 따라 달라진다.

![그림 6-2. 한 번에 닿는 사람의 수로 놓아본 직함들 — 2026년 9월 25일 공고 문구 기준](figures/fig-6-2.svg)

> **반론:** 보완이라는 그림이 맞더라도 안심할 일은 아니다. Daily Context 취재기의 요점은 가운데가 눌린다는 것이다. 글은 가장 위험한 쪽을 "Developer marketing aimed at engineers who read docs and deliberate"라고 짚었다. 문서를 읽고 따져보는 엔지니어를 겨냥한 개발자 마케팅이다. 양 끝이 살아남아도, 그 사이에서 일하던 자리가 줄어들 수 있다. 하루치 공고로는 이 경고가 맞는지 확인할 수 없다.

이 표를 그대로 자기 이력에 대어 보는 것도 좋다. 당신이 해온 일 가운데 어느 행이 가장 굵은가? 그 행의 동사가 어떤 제목의 공고에 들어 있는지 찾아보자. 옮겨 갈 수 있는 자리가 보이기 시작한다.

## 서울이라는 근무지

마지막으로 같은 목록을 근무지로 걸러보자. 서울이 적힌 공고는 무엇이었을까?

Anthropic의 목록에는 서울 근무 공고가 있었다. Applied AI Architect와 Manager, Applied AI Architect다. Applied AI Architect는 도쿄·싱가포르·시드니·런던 등 여러 도시에 걸쳐 열려 있었고, 서울은 그중 하나였다. OpenAI의 목록에는 "Forward Deployed Engineer - Seoul" 공고가 한 건 있었다(Ashby 공개 API, 2026-09-25 조회). 서울 근무 FDE 자리다.

Cloudflare의 VoidZero Developer Relations Engineer 공고는 근무지 후보로 "Singapore, Sydney, Tokyo, Seoul, Lisbon, or London"을 적었다. 싱가포르, 시드니, 도쿄, 서울, 리스본, 런던 가운데 한 곳이다. 서울을 명시한 DevRel 제목 공고는 이 한 건이었다. 그것도 여러 후보 도시 가운데 하나였다.

그날의 목록만 놓고 보면, 서울을 근무지로 한 자리는 주로 고객 곁으로 가는 이름(Applied AI, FDE)을 달고 있었다. 이 관찰을 일반화하면 곤란하다. 열 개 회사, 하루치 목록, 제목 기준 집계일 뿐이다. 한국 회사들의 공고는 이 표에 들어 있지도 않다. 그래도 서울에서 이 공고들을 읽는 사람에게는 쓸모 있는 정보가 하나 남는다. 외부 개발자와 제품 사이에서 번역하고 되돌려주는 일을 찾는다고 하자. 검색창에 'DevRel'만 넣었다면 그날의 공고 대부분을 놓쳤을 것이다.

그날 열어본 공고들 가운데 이 장을 닫기에 알맞은 문장은 Anthropic의 이 한 줄이다. "Help define what world-class AI developer relations looks like in this emerging field." 이 일의 정의는 공고를 낸 쪽에서도 아직 쓰는 중이다.

### 이 장의 한 줄

그날의 공고에서 개발자의 말을 제품으로 되돌려주고 만든 것으로 보여주는 일은 DevRel 공고와 FDE 공고의 문장에 함께 적혀 있었다.
