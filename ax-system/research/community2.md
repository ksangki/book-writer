# 커뮤니티 리서치 2차 보강 — AX 체계 구축

검색 시점: **2026-09-05 기준**
슬러그: `ax-system` / 장르: tech-book / 대상 독자: AX 실무 리더·기획자
1차 산출물: `research/community.md` (덮어쓰지 않음. 이 문서는 A~D 지시 범위만 다룬다)

> **읽는 법.** 1차와 동일한 규율을 따른다 — 모든 인용에 원문 URL·게시일·플랫폼을 붙였고, 영문은 원문을 싣고 번역을 병기했다. **정서·경험담**과 **사실 주장**을 구분해 라벨을 달았으며, 수치·기업명·사건이 섞인 익명 주장에는 `⚠️ 익명 주장 — 미검증`을 붙이고 §G에 모아뒀다.
>
> **1차 대비 가장 큰 변화 — 한국 소스 비중.** 1차는 인용의 약 80%가 Hacker News였고, 스레드 안에서 `keeda`가 직접 "HN은 에코 챔버"라고 지적했다. 2차는 GeekNews·OKKY를 전수 인덱싱해 **한국어 인용 60건 이상**을 확보했다. 이 문서의 인용 중 한국 소스가 약 45%다. 자세한 편향 계산은 §H.
>
> **Reddit — 이번에도 실패에 가깝다.** `reddit.com` 직접 접근은 여전히 HTTP 403(크롤러 차단). 다만 **Pushshift 후속 아카이브 API(`api.pullpush.io`)로 우회에 부분 성공**했다. 그러나 (a) 아카이브 수집이 **2025년 5월경에서 끊긴다** — 즉 2025-06 이후 Reddit 여론은 여전히 통째로 비어 있고, (b) 전문 검색 품질이 낮아 노이즈가 압도적이며, (c) 조회 속도 제한이 심해 계획한 25개 질의 중 9개만 완주했다. **Reddit에서 건진 인용은 3건뿐이다.** 지시대로 시간을 더 쓰지 않고 HN·GeekNews·OKKY·Lobsters·GitHub에 집중했다.
>
> **표기 규칙(한국 소스).** `[원문확인]` = HTML/DOM에서 글자 그대로 추출. `[페치경유]` = 페치 도구가 원문으로 제시한 인용으로, 미세 편집 가능성을 배제하지 못한다 — **책에 실을 때는 해당 URL을 직접 열어 재확인할 것.**

---

## ⚠️ 방법론 경고 — 다음 사람이 반드시 알아야 할 것 3가지

이번 조사에서 발견한, **한국 커뮤니티 인용을 통째로 오염시킬 수 있는 함정**이다.

1. **GeekNews의 `GN⁺(@neo)` 댓글은 커뮤니티 반응이 아니다.** 사이트 자체 AI가 Hacker News·Lobsters 원문 토론을 요약해 붙이는 봇 글이다. 이걸 "한국 개발자 반응"으로 인용하면 **사실상 HN을 한국어로 재인용하는 것**이 되어, 이 책이 피하려는 바로 그 편향을 증폭시킨다. 이 문서는 GN⁺ 댓글을 전량 배제했다.
2. **OKKY의 특정 계정(`길가다주웠어`)이 올리는 게시글 상당수는 Reddit 스레드 번역 재게시다.** 예: `https://okky.kr/articles/1549593`(「AI 때문에 오늘 해고당함」)은 본문 전체가 Reddit 번역이고 한국어 댓글이 0건이다. **본문을 한국 실무자 목소리로 인용하면 안 된다.** 이런 글은 **댓글만** 한국 반응으로 친다.
3. **1차에서 인용한 A2A #1672(658 코멘트)의 AI 생성 의심 정황**과 같은 패턴이 GeekNews에도 있다. 아래 §B-2에서 인용한 A2A 레지스트리 토픽(id=32719)은 **게시글 자체가 AI 생성물 같다는 비판 댓글**이 여럿 달렸다(`yunsub2`: "ai slob 냄새가 너무 나네요..."). 게시글 본문이 아니라 **댓글의 회의만** 인용 가치가 있다.

---

# A. 축 5 — FTE·생산성 측정의 현장

> **이 축의 한 줄 결론.** 커뮤니티는 "AI로 N명분"이라는 숫자를 **성능 주장이 아니라 서사(narrative) 주장**으로 읽는다. 그리고 그 숫자를 만드는 과정과 게이밍 방법을 아주 구체적으로 알고 있다. 이 책이 FTE 환산을 제안하려면, 제안하기 전에 이 불신을 정면으로 받아야 한다.

## A-1. "AI로 N명분" 주장에 대한 반응

### ① Klarna — 이 분야의 정본 사례이자 정본 반증

Klarna는 2024-02 "AI 어시스턴트가 700명분의 일을 한다"고 발표했고, HN 스레드가 그날 바로 섰다. **가장 먼저 나온 반응은 성능 의심이 아니라 동기 의심이었다.**

- 원문 인용: **"They kind of want to say two things: They *want* to say that they're going to employ this crazy new AI that's going to bring their customer service costs to 0. This is presumably because they want to IPO and their actual financials look like crap. So tell a fairytale about AI and hope people buy it. But at the same time they don't want to go around screaming "Ha! Suckers! We're going to fire you all!" to the actual people who do their customer service today. So they simultaneously claim that they've got AI that has replaced 700 people, but that they haven't actually fired 700 people, but if you're listening Wall Street we're are firing them, but if you're listening EU regulators and main street no no we're definitely not."**
  - 번역: "이들은 두 가지를 동시에 말하고 싶어 한다. 하나는 '고객 서비스 비용을 0으로 만들 미친 신형 AI를 쓰겠다'는 것 — 짐작건대 IPO를 하고 싶은데 실제 재무제표가 형편없기 때문이다. 그러니 AI에 관한 동화를 들려주고 사람들이 사주길 바라는 거다. 그런데 동시에, 지금 고객 서비스를 하고 있는 실제 사람들한테 '하! 호구들아! 너희 다 자를 거야!'라고 소리 지르고 싶지도 않다. 그래서 이들은 'AI가 700명을 대체했다'고 주장하면서 동시에 '700명을 실제로 자른 건 아니다'라고 하고, 월스트리트가 듣고 있다면 '자르는 중이다', EU 규제당국과 일반 대중이 듣고 있다면 '아니 아니 절대 아니다'라고 한다."
  - 출처: Hacker News / "Klarna says its AI assistant does the work of 700 people" / 작성자 `SilverBirch` / https://news.ycombinator.com/item?id=39548544 / **2024-02-29**
  - 검증 상태: 정서·동기 해석 (사실 주장 아님)
  - **책에서 쓸 지점: 이 인용 하나가 PART 4의 오프닝을 감당할 수 있다.** "AI로 N명분"이라는 문장은 **하나의 청중을 향한 진술이 아니라 서로 다른 세 청중(투자자·규제당국·직원)을 향한 세 개의 진술**이라는 지적이다. 이 책이 FTE 환산표를 제시하는 순간, 독자는 그 표가 어느 청중용인지를 묻게 된다.

**실제로 그 봇을 써본 사람의 검증** — 이게 이 스레드 계열에서 가장 강력한 자료다. 미디어가 아무도 안 한 일을 한 사람이 있다.

- 원문 인용: **"Either Klarna is really good at pulling strings to get media coverage, or mainstream media does not fact checking themselves. About a year ago, the company was everywhere in the media when its CEO announced that it created an AI bot that is doing the equivalent of 700 fulltime customer service folks. I did what seemingly no other publication reporting on it did: signed up for Klarna, bought one item and used this bot. I was... not impressed? Klarna's "AI bot" felt like the "L1 support flow" that every other company already has in-place: without AI!"**
  - 번역: "Klarna가 언론 노출을 얻어내는 데 정말 능하거나, 아니면 주류 언론이 팩트체크를 안 하거나 둘 중 하나다. 1년쯤 전, 이 회사 CEO가 정규직 고객 서비스 700명분에 해당하는 일을 하는 AI 봇을 만들었다고 발표했을 때 회사는 온 미디어에 도배됐다. 나는 이걸 보도한 다른 어떤 매체도 안 한 것으로 보이는 일을 했다: Klarna에 가입해서 물건 하나를 사고 그 봇을 써봤다. 나는… 감명받지 못했다? Klarna의 'AI 봇'은 다른 모든 회사가 **AI 없이** 이미 갖추고 있는 'L1 지원 플로우'처럼 느껴졌다."
  - 이어지는 진단: **"My sense is that Klarna really wants to be seen as an "AI-first tech company" when it goes public, and not a "buy now pay later loan company" because AI companies have higher valuations even with the same revenue."** (번역: "내 감으로는, Klarna는 상장할 때 '후불결제 대출 회사'가 아니라 'AI 우선 테크 기업'으로 보이고 싶어 한다. 같은 매출이라도 AI 기업이 더 높은 밸류에이션을 받으니까.")
  - 출처: Hacker News / "Klarna changes its AI tune and again recruits humans for customer service" / 작성자 `gregdoesit` / https://news.ycombinator.com/item?id=43955917 / **2025-05-11** / 본인 블로그 검증 링크: https://blog.pragmaticengineer.com/klarnas-ai-chatbot/
  - 검증 상태: **1인 직접 검증 경험담** (공개 블로그로 근거 제시 — 이 문서 전체에서 검증 수준이 가장 높은 커뮤니티 인용 중 하나)
  - **책에서 쓸 지점:** "N명분"이라는 수치가 **AI 없이도 가능했던 자동화를 AI 이름으로 재포장한 것**일 수 있다는 반증. 이 책이 "에이전트 1대 = N FTE"를 제안한다면, **분모(그 일이 원래 몇 명분이었나)를 누가 어떻게 정했는지**를 반드시 다뤄야 한다.

**"대체"가 아니라 "포기"라는 해석** — 이게 두 번째로 자주 나온 프레임이다.

- 원문 인용: **"All these jobs being "replaced by AI" are simply being eliminated with the consequences of them being eliminated ignored. Customer service jobs aren't being replaced by AI, companies, like Klarna, are just giving up on customer service and using AI to increase their perceived value rather than reducing it."**
  - 번역: "'AI로 대체된다'는 이 모든 일자리는 그냥 없애버리는 것이고, 없앤 결과는 무시되는 것이다. 고객 서비스 일자리가 AI로 대체되고 있는 게 아니다. Klarna 같은 회사들은 그냥 고객 서비스를 포기하면서, AI를 이용해 (기업 가치를) 떨어뜨리는 대신 올리고 있는 것이다."
  - 출처: Hacker News / "Money bubble" / 작성자 `PheonixPharts` / https://news.ycombinator.com/item?id=39554367 / **2024-02-29**
  - 검증 상태: 정서·해석

- 원문 인용: **"Are they? Or are they being fired and AI is used at the excuse? We saw Klarna layoff customer services staff and that didn't work. LLMs couldn't do their job. Some programmers are being fired, but my feeling is that generative AI is more of a convenient excuse. Is anyone actually being fired because an LLM did their job better, or where their job already in danger and AI just gave the companies an easy way out?"**
  - 번역: "정말 그런가? 아니면 해고당하고 있는데 AI가 핑계로 쓰이는 건가? 우리는 Klarna가 고객 서비스 인력을 정리했다가 그게 안 됐던 걸 봤다. LLM은 그들의 일을 할 수 없었다. 일부 프로그래머들이 해고되고 있지만, 내 느낌으로 생성형 AI는 편리한 핑계에 가깝다. LLM이 자기 일을 더 잘해서 실제로 해고되는 사람이 있긴 한가, 아니면 원래 그 자리가 위태로웠는데 AI가 회사에 쉬운 출구를 준 것뿐인가?"
  - 출처: Hacker News / "AI-first – We're just 6 months away from AGI" / 작성자 `mrweasel` / https://news.ycombinator.com/item?id=44158152 / **2025-06-02**
  - 검증 상태: 정서·질문 제기

**시간이 지나며 이 회의가 데이터로 확인된 정황** — 2026년 시점의 정리.

- `toomuchtodo`(2026-03-16)는 HBR 기사를 길게 인용하며, Klarna가 2022-12~2024-12에 인력을 40% 줄였으나(해고가 아니라 채용 동결·자연 감소) **2025년에 CEO가 Bloomberg에 "인간 지원에 재투자하고 있다, 비용을 낮추는 걸 우선하다 보니 품질도 낮아졌다"고 말했고**, 대변인은 AI가 처리 못 하는 케이스를 위해 약 20명을 다시 뽑았다고 밝혔다고 전한다. 같은 인용 안에 **"AI 워싱"** 통계도 있다.
  - 원문 인용(그가 인용한 대목): **"in 2025 the company's CEO told Bloomberg that Klarna was reinvesting in human support, explaining that prioritizing lower costs had also led to 'lower quality.'"**
  - 원문 인용(같은 코멘트, 다른 기사): **"A Resume.org survey found that 59% of hiring managers say they emphasize AI's role in layoffs because it "is viewed more favorably by stakeholders than saying layoffs or hiring freezes are driven by financial constraints"."**
    - 번역: "Resume.org 설문에 따르면 채용 관리자의 59%가, 정리해고나 채용 동결이 재정적 제약 때문이라고 말하는 것보다 **AI 때문이라고 하는 편이 이해관계자들에게 더 호의적으로 받아들여지기 때문에** AI의 역할을 강조한다고 답했다."
  - 그 자신의 한 줄: **"It is free for you to say this, because if you're wrong, there will be no consequences. Words are cheap. No different than various CEOs saying "AI will replace these workers" and now having to hire back those they laid off."** (번역: "그렇게 말하는 건 당신에게 공짜다. 틀려도 아무 대가가 없으니까. 말은 싸다. 'AI가 이 노동자들을 대체할 것'이라고 했다가 이제 자른 사람들을 다시 뽑아야 하는 여러 CEO들과 다를 게 없다.")
  - 출처: Hacker News / "US Job Market Visualizer" / 작성자 `toomuchtodo` / https://news.ycombinator.com/item?id=47401108 / **2026-03-16**
  - 검증 상태: ⚠️ **2차 인용이다.** HBR·Resume.org 원문을 커뮤니티 사용자가 옮긴 것이므로, 이 책에 수치를 실으려면 **원 출처를 직접 확인해야 한다.** 커뮤니티 자료로서의 가치는 "2026년 3월 시점 HN에서 Klarna가 이미 *교훈 사례*로 정착했다"는 정황이다.

- 짧은 형태로 굳어진 커뮤니티 상식 2건:
  - **"Didn't Klarna say they'd replaced all of their customer service reps with AI, and then had to backtrack and rehire them when the AI was doing a terrible job?"** (번역: "Klarna가 고객 서비스 인력을 전부 AI로 대체했다고 했다가, AI가 형편없이 하니까 말을 무르고 다시 뽑아야 했던 거 아니었나?") — `cjrp` / "Klarna says AI drive has helped halve staff numbers and boost pay" / https://news.ycombinator.com/item?id=45979201 / **2025-11-19**
  - **"Initially touted its AI assistant as doing work equivalent to hundreds of customer service agents, but later had to hire human customer service workers again to balance AI with human support."** (번역: "처음엔 AI 어시스턴트가 고객 서비스 담당자 수백 명분의 일을 한다고 자랑했지만, 나중엔 AI와 인간 지원의 균형을 맞추려고 인간 고객 서비스 인력을 다시 뽑아야 했다.") — `aussieguy1234` / https://news.ycombinator.com/item?id=47969973 / **2026-05-01**
  - 검증 상태: 정서 (공개 보도 사건에 대한 요약 — **커뮤니티가 그 사건을 어떻게 기억하는가**의 증거로 쓸 것)

- 이 사건을 **업계 종사자가 예측 가능한 실패로 규정**한 발언:
  - 원문 인용: **"the track record of big corps and their view of customer-facing departments as being loss-centers instead of being directly and indirectly connected to retaining and bringing in revenue doesn't leave me optimistic. ... There's no reason for any business to ruin their customer service with AI other than impulsive and/or poorly executed decisions being made out of some mix of fear, hype, greed, or willful ignorance. Entirely avoidable."**
    - 번역: "대기업들이 고객 대면 부서를 매출 유지·창출과 직간접으로 연결된 곳이 아니라 **비용 센터로 보는** 전력을 생각하면 나는 낙관적이지 않다. … 어떤 기업이든 AI로 자기 고객 서비스를 망칠 이유는, 두려움·과대광고·탐욕·의도적 무지가 뒤섞여 나온 충동적이거나 형편없이 실행된 결정 말고는 없다. 전적으로 피할 수 있는 일이다."
  - 맥락: 이 사람은 본인이 **음성 에이전트 시스템을 기업에 구축하는 일을 한다**고 밝혔다 (이해관계 있음, 다만 자기 사업에 불리한 방향의 발언).
  - 출처: Hacker News / "Build an AI telephony agent for inbound and outbound calls" / 작성자 `cootsnuck` / https://news.ycombinator.com/item?id=44763340 / **2025-08-01**
  - 검증 상태: 업계 종사자 판단

### ② "그럼 실제로 사람이 줄었냐" — 한국 커뮤니티의 반문

한국 커뮤니티는 **동기를 의심하는 대신, 검증 가능한 반문 하나로 곧장 간다.** 이게 이 축에서 가장 실용적인 인용이다.

- 원문 인용: **"1명이상의 퍼포먼스가 난다는 것도 주관적이죠. 회사입장에서 1명이상의 퍼포먼스가 난다는건 그것을 도입했을때 1명을 줄여도 된다는 것으로 이해합니다. 그러면 ai를 사용하는 사람수만큼 사람수를 줄여야 하는데 그렇게 되고 있나요? Ai 도입해소 사용하는 직원수만큼 할일없는 직원이 생기셨을까요???"**
  - 출처: OKKY / 「AI 사용을 점점 제한 하는 기업이 늘어날 것으로 예상 되네요」 / 작성자 `k35241` / https://okky.kr/articles/1562362 / 게시글 2026-08-16, 댓글 "20일 전"(2026-09-05 조회)
  - 검증 상태: 정서·논리 반박 `[원문확인]`
  - **책에서 쓸 지점: 이 문장이 이 책 FTE 챕터의 시험 문제다.** "에이전트 1대 = N FTE"라고 쓰는 순간 독자는 정확히 이걸 묻는다. 책이 이 질문에 **"줄이지 않는다, 재배치한다"**로 답할 것인지 **"줄인다"**로 답할 것인지를 명시하지 않으면 나머지 논의가 전부 공중에 뜬다.

**실제 대체는 해고가 아니라 "충원 안 함"으로 일어난다**는 증언 — 이게 이 책이 다뤄야 할 진짜 메커니즘이다.

- 원문 인용: **"지금 취업과 이직이 안되는 경우가 대부분 AI 효과가 큽니다. 3명 퇴사하면 3명을 뽑아야하는데 AI 때문에 2명이나 1명 뽑고 AI를 대신 지원해주고 있습니다. 즉, 기존 직원이 대신 책임을 AI와 함께 업무를 맡고 있습니다."**
  - 출처: OKKY / 같은 글 / 작성자 `manijang2.` / https://okky.kr/articles/1562362 / "20일 전"(2026-09-05 조회)
  - 검증 상태: ⚠️ 익명 주장(인과 귀속) — 미검증 / 경험담으로는 유효 `[원문확인]`
  - **책에서 쓸 지점:** FTE 절감은 **감원 라인이 아니라 채용 계획 라인에서 조용히 실현된다.** 이 책이 "정원 산입"을 말한다면, 감원 대신 **결원 미충원**이라는 실제 경로를 정면으로 다뤄야 한다. 이건 절감 보고의 정치를 완전히 다르게 만든다.

- 한국판 "AI 워싱": **"뭐 AI 때문에 layoff 하고 고용안한다 하면 save face 되는거였죠 허허"**
  - 맥락: 앞 문맥에서 코로나 시기 과잉 채용을 지목한 뒤 나온 말.
  - 출처: OKKY / 같은 글 / 작성자 `임시저장보관소` / "20일 전"(2026-09-05 조회) `[원문확인]`
  - 검증 상태: 정서

- 원인 재배치: **"AI 로 인력을 대체 하는게 아니라 AI 에 막대한 투자를 퍼붓고 있어서 구형산업이나 인력 감축하는 거고. AI 는 노가다성 작업은 많이 감소시켜 주는건 맞지만. 인력을 대체한다거나 하는 수준은 아직 멀었습니다."**
  - 출처: OKKY / 「AI 믿고 해고했더니 회사들 난리 난 이유」 / 작성자 `흰꿈둘` / https://okky.kr/articles/1560743 / 게시글 2026-07-17, 댓글 "약 2개월 전"(2026-09-05 조회) `[원문확인]`
  - 검증 상태: 정서·판단

- Klarna형 재고용에 대한 한국식 한 줄 — **"누가 재고용되는지 봐야죠"**
  - 출처: OKKY / 같은 글 / 작성자 `자바킬러` / "약 2개월 전"(2026-09-05 조회) `[원문확인]`
  - 검증 상태: 정서
  - **책에서 쓸 지점:** 짧지만 날카롭다. "다시 뽑았다"가 원래 사람들을 복직시켰다는 뜻이 아니라는 지적. FTE 회계에서 **인원 수는 복원되어도 숙련은 복원되지 않는다**는 논점으로 확장 가능.

### ③ 사내에서 "N명분" 숫자가 실제로 만들어지는 방식 — 이 축의 최고 수확

McKinsey가 "측정 가능한 이익이 없는 AI 앱을 어떻게 파나" 고민한다는 기사(The Register, 2025-10-09)에 달린 스레드에서 나왔다.

- 기사 자체가 실토한 대목을 인용한 댓글 — 원문 인용: **"All of these copilots are supposed to make work more efficient with fewer people, but my business leaders are also saying they can't reduce head count yet."** 그리고 그 위에 붙인 한 줄: **"I'm surprised McKinsey convinced someone to say the quiet part out loud"**
  - 번역: "이 모든 코파일럿은 더 적은 인원으로 일을 더 효율적으로 만들어야 하는데, 우리 사업부 리더들은 아직 인원을 줄일 수 없다고도 말한다." / "McKinsey가 누군가를 설득해서 조용히 해야 할 말을 소리 내어 하게 만들었다는 게 놀랍다."
  - 출처: Hacker News / "McKinsey wonders how to sell AI apps with no measurable benefits" / 작성자 `StableAlkyne` / https://news.ycombinator.com/item?id=45527020 / **2025-10-09**
  - 검증 상태: 정서 + 기사 인용(Fortune 100 HR 임원 발언, 원 기사는 The Register)

**그리고 같은 스레드에 "숫자를 일부러 낮춰 보고한다"는 실무 증언이 있다. 이 문서 전체에서 A-4와 함께 가장 중요한 인용이다.**

- 원문 인용: **"At my company people always understate the headcount savings. Because the invariable question is - "You are spending x million and for y FTEs you save only 1 FTE of HC? How does that make sense?". Or worse yet - "You estimated 40 FTE savings, why don't we pick and chose 40 FTEs to let go". That sends shivers down managers as it reduces their area of influence. They found a hack and that is loading up the intangible column. In that list reputation/brand risk always makes an appearance. "If you don't do this project this terrible thing might happen and we might suffer reputational risk. We estimate 2x millions of loss due to reputation being harmed". And presto! there is a case for the project."**
  - 번역: "우리 회사에서 사람들은 **항상 인력 절감분을 축소해서 보고한다.** 왜냐하면 반드시 나오는 질문이 이거니까 — '수백만을 쓰면서 y명의 FTE 중 겨우 1 FTE를 아낀다고? 그게 말이 되나?' 아니면 더 나쁜 경우 — '40 FTE 절감이라고 추정했으니, 그럼 40명을 골라서 내보내는 게 어떤가.' 이건 관리자들 등골을 서늘하게 한다. 자기 영향력 범위가 줄어드니까. 그래서 이들은 편법을 찾아냈는데, **무형 이익 칸을 잔뜩 채우는 것**이다. 그 목록에는 평판·브랜드 리스크가 항상 등장한다. '이 프로젝트를 안 하면 이런 끔찍한 일이 벌어질 수 있고 평판 리스크를 입을 수 있다. 평판 훼손으로 인한 손실을 수백만의 2배로 추정한다.' 짜잔! 프로젝트의 명분이 생겼다."
  - 이어지는 진단: **"AI tools being so hyper focused on "productivity gains" it is going to be tough sell. Especially because users will resist it and the productivity boosts if any will remain low."**
  - 출처: Hacker News / 같은 스레드 / 작성자 `thisisit` / https://news.ycombinator.com/item?id=45529408 / **2025-10-09**
  - 검증 상태: ⚠️ 익명 주장(사내 관행) — 미검증 / **경험담으로는 이 문서 최고 밀도**
  - **책에서 쓸 지점 — 이건 이 책의 논지를 뒤집는 급의 발견이다.** 이 책은 아마 "FTE 환산을 하면 AX의 효과가 보인다"고 말하고 싶을 것이다. 그런데 현장은 **FTE 환산이 정확할수록 위험해지기 때문에 일부러 부정확하게 만든다.** 즉 **측정 도구의 정확도를 올리는 것만으로는 문제가 해결되지 않는다** — 정확한 숫자가 감원 명단으로 번역되는 구조가 남아 있는 한, 현장은 계속 숫자를 흐린다. PART 4는 "어떻게 재는가"보다 **"잰 숫자를 무엇으로 번역하지 않겠다고 약속할 것인가"**를 먼저 다뤄야 한다.

**왜 관리자가 절감을 원하지 않는가** — 인센티브 구조 3건.

- 원문 인용: **"The incentive structure for managers (and literally everyone up the chain) is to maximize headcount. More people you managed, the more power you have within the organization. No one wants to say on their resume, "I manage 5 people, but trust me, with AI, its like managing 20 people!" Managers also don't pay people's salaries. The Tech Tools budget is a different budget than People salaries."**
  - 번역: "관리자(그리고 위로 올라가는 모든 사람)의 인센티브 구조는 **인원을 최대화하는 것**이다. 더 많은 사람을 관리할수록 조직 내 권력이 커진다. 이력서에 '나는 5명을 관리하는데, 믿어달라, AI가 있으니 20명 관리하는 것과 같다!'라고 쓰고 싶은 사람은 없다. 게다가 **관리자가 사람들 월급을 내는 게 아니다. 기술 도구 예산과 인건비 예산은 다른 예산이다.**"
  - 출처: Hacker News / 같은 스레드 / 작성자 `itake` / https://news.ycombinator.com/item?id=45527337 / **2025-10-09**
  - 검증 상태: 정서·조직 진단
  - **책에서 쓸 지점:** **"기술 도구 예산과 인건비 예산은 다른 예산이다"** — 이 한 문장이 AX ROI 계산이 실무에서 왜 안 굴러가는지를 설명한다. 에이전트를 FTE로 환산해도, 그 절감이 **다른 회계 항목**에 잡히면 아무도 그걸 자기 성과로 인식하지 않는다. 이 책이 FTE 환산을 제안한다면 **어느 예산에서 빼서 어느 예산에 더할 것인가**를 같이 설계해야 한다.

- 어디서는 실제로 됐다는 반례 — **왜 됐는지가 중요하다.**
  - 원문 인용: **"AI can absolutely reduce headcount. It already could 2 years ago... At the time I worked at a company that did just that, succesfully automating away thousands of jobs which couldn't pre-LLMs. The reason it ""worked"" was because it was outsourced headcount, so there was very limited political incentive to keep them if they were replaceable. The bigger and older the company, the more ossified the structures are that have a want to keep headcount equal, and ideally grow it. This is by far the biggest cause of all these "failed" AI projects."**
    - 번역: "AI는 확실히 인원을 줄일 수 있다. 2년 전에도 이미 가능했다… 당시 나는 바로 그렇게 한 회사에서 일했고, LLM 이전에는 불가능했던 수천 개의 일자리를 성공적으로 자동화했다. 그게 ''작동한'' 이유는 **그게 외주 인력이었기 때문**이다. 그래서 대체 가능하다면 그들을 붙잡을 정치적 인센티브가 매우 제한적이었다. 회사가 크고 오래될수록 인원을 유지하고 이상적으로는 늘리려는 구조가 더 굳어 있다. **이게 이 모든 '실패한' AI 프로젝트의 압도적으로 가장 큰 원인이다.**"
    - 출처: Hacker News / 같은 스레드 / 작성자 `deaux` / https://news.ycombinator.com/item?id=45527568 / **2025-10-09**
    - 검증 상태: ⚠️ 익명 주장(수천 명 자동화) — 미검증 / 경험담·조직 진단으로는 강력
    - **책에서 쓸 지점: 이 책의 가장 불편한 진실.** AX가 "성공"한 지점은 기술이 좋아서가 아니라 **정치적 저항이 없는 인력 범주(외주·계약직)였기 때문**이라는 것. 이 책이 "AX 성숙도"를 말한다면, 성숙도 지표가 실은 **조직의 정치적 저항 지형도**를 재고 있는 건 아닌지 자문해야 한다.

- 산업 사례로 확장 — 원문 인용: **"it's instructive to see how automation has reduced head count in oil and gas majors. The reduction comes when there's a shock financially or economically and layoffs are needed for survival. Until then, head count will be stable."**
  - 번역: "석유·가스 메이저에서 자동화가 인력을 어떻게 줄였는지를 보면 배울 게 있다. **감축은 재정적·경제적 충격이 와서 생존을 위해 정리해고가 필요할 때 온다. 그전까지 인원은 안정적으로 유지된다.**"
  - 출처: Hacker News / 같은 스레드 / 작성자 `ckcheng` / https://news.ycombinator.com/item?id=45527809 / **2025-10-09**
  - 검증 상태: 산업 관찰
  - **책에서 쓸 지점:** 자동화는 감원의 **원인이 아니라 저장고**다. 평소엔 인원이 유지되다가 충격이 오면 그동안 쌓인 자동화 여력만큼 한 번에 잘린다. 이 시차가 현장이 자동화를 불신하는 진짜 이유일 수 있다.

- 반대편에서 나온 냉소적 요약: **"AI is most capable of replacing the humans who have the power to decide or influence the choice to replace humans with AI. But managers will not obsolete themselves."**
  - 번역: "AI는 **인간을 AI로 대체할지를 결정하거나 그 결정에 영향을 미칠 권한을 가진 인간들**을 대체하는 데 가장 능하다. 하지만 관리자들은 자기 자신을 쓸모없게 만들지 않을 것이다."
  - 출처: Hacker News / 같은 스레드 / 작성자 `newsclues` / https://news.ycombinator.com/item?id=45527251 / **2025-10-09**
  - 검증 상태: 정서

- 같은 취지의 한국판(더 짧고 더 세다): **"이걸로 진짜 회사 쓸데없는 경영진 의사결정도 간소화 되었으면..이 아니라 능력없이 정치질만하는 경영진은 좀 잘랐으면"**
  - 출처: GeekNews / 「CEO가 AI를 위해 개발팀을 해고하자, 개발자들은 오픈소스 AI CEO를 만들었다」 / 작성자 `daumkakao` / https://news.hada.io/topic?id=32939 / **2026-08-29** `[원문확인]`
  - 검증 상태: 정서

- 그리고 이 계열의 가장 균형 잡힌 반문: **"Then you consider that they might be able to reduce headcount because of productivity increases. But why wouldn't they want to use the budget they already have for these newly more productive people and get even more work done overall?"**
  - 번역: "생산성이 올랐으니 인원을 줄일 수 있겠다고 생각한다 치자. 그런데 왜 이미 가진 예산을 새로 더 생산적이 된 사람들에게 그대로 쓰고 **전체적으로 더 많은 일을 해내려 하지 않겠는가?**"
  - 출처: Hacker News / "CEO fired developers to make room for AI. Developers create open source AI CEO" / 작성자 `phoghed` / https://news.ycombinator.com/item?id=49463378 / **2026-08-27**
  - 검증 상태: 정서·논리
  - **책에서 쓸 지점:** 이 책이 "절감을 감원으로 번역하지 마라"고 주장한다면, **이 문장이 그 주장의 커뮤니티 측 우군**이다. 흔치 않으니 아껴 써라.

### A-1 커버리지

**확보**
- Klarna 회의론 **8건** (2024-02 ~ 2026-05, HN) — 동기 의심 / 직접 검증 / "대체가 아니라 포기" / 재고용 정착 서사 / AI 워싱 통계
- 사내에서 절감 숫자가 만들어지는 과정의 **실무 증언 5건** (HN, 2025-10 단일 스레드에 집중)
- 한국 커뮤니티의 "그럼 사람 줄었냐" 반문 계열 **5건** (OKKY·GeekNews, 2026)

**비어 있음**
- **IBM·Salesforce·Duolingo·Dropbox 개별 발언에 달린 원 스레드 — 확보 실패.** HN Algolia 댓글 전수 검색에서 이들 기업의 "AI로 N명 대체" 발언 자체를 다룬 **댓글 다수 스레드**를 찾지 못했다. Klarna만 예외적으로 커뮤니티의 정본 사례로 굳었다. Duolingo는 `cootsnuck`·`toomuchtodo` 인용 안에 **언급**될 뿐 자체 스레드가 아니다.
- **Klarna·IBM·Salesforce에 대한 한국어 커뮤니티 스레드 — 전무.** GeekNews 토픽 11,168건 전수 제목 인덱스와 OKKY 1,665건 인덱스 어디에도 없다. **기사만 있고 커뮤니티 토론 없음.** 이건 그 자체로 기록할 만한 발견이다 — 한국 독자는 이 사례들을 *뉴스로만* 접했고 *토론한 적이 없다.*
- **실적 발표(earnings call) 발언에 대한 반응 — 확보 실패.** 커뮤니티는 실적 발표를 직접 읽지 않고 기사화된 뒤에 반응한다.

---

## A-2. 생산성 측정·개발자 지표에 대한 실무자 냉소

### ① METR 연구 — 찬반 양쪽, 그리고 이 책이 반드시 알아야 할 후속 연구

**찬성·인용 측** (이 책이 쓰고 싶어 할 쪽):

- 원문 인용: **"It's interesting how self-reports of productivity can be wrong. For example a study from METR found that developers felt that AI sped them up by 20%, but it empirically it slowed them down by 19%."**
  - 번역: "생산성에 대한 자기 보고가 틀릴 수 있다는 게 흥미롭다. 예를 들어 METR 연구는 개발자들이 AI가 자신을 20% 빠르게 했다고 느꼈지만 실증적으로는 19% 느려졌다는 걸 발견했다."
  - 출처: Hacker News / "95% of Companies See 'Zero Return' on $30B AI Spend" / 작성자 `md3911027514` / https://news.ycombinator.com/item?id=44974785 / **2025-08-21**
- 원문 인용: **"Developers who use AI think they're quicker and better, but they're actually slower and worse. ... This first chart should be absolutely damning"**
  - 번역: "AI를 쓰는 개발자들은 자신이 더 빠르고 더 낫다고 생각하지만, 실제로는 더 느리고 더 나쁘다. … 이 첫 번째 차트는 그야말로 결정적이어야 한다."
  - 출처: Hacker News / "Where's the AI design Renaissance?" / 작성자 `immibis` / https://news.ycombinator.com/item?id=45695816 / **2025-10-24**
- 원문 인용: **"The METR study cited here is very interesting. ... I hadn't heard of this study before. Seems like it's been mentioned on HN before but not got much traction."**
  - 번역: "여기 인용된 METR 연구는 아주 흥미롭다. … 이 연구를 전에 들어본 적이 없다. HN에서 전에 언급된 적은 있는 것 같은데 큰 반향은 없었던 듯하다."
  - 출처: Hacker News / "The 70% AI productivity myth" / 작성자 `fancyfredbot` / https://news.ycombinator.com/item?id=46434074 / **2025-12-30**
  - 검증 상태: 정서
  - 🕒 **주의:** 이 발언은 **연구의 커뮤니티 침투도가 낮았다**는 증거다. 이 책이 METR을 "널리 알려진 연구"로 소개하면 과장이다.

**🕒 반드시 알아야 할 반박 — METR 후속 연구가 반대 결과를 냈다.** 이 책의 핵심 근거가 흔들릴 수 있는 지점이므로 최우선으로 기록한다.

- 원문 인용: **"METR reran the study early this year and, while they caveat it, this time they found a speedup, which is consistent with subjective estimates of productivity also having increased -- the simplest explanation is that subjective estimates exaggerate, but there's still a speedup with current models: https://metr.org/blog/2026-02-24-uplift-update/#wider-adopti... (Nobody seems to cite the followup since it's not such a fun counterintuitive finding.)"**
  - 번역: "METR은 올해 초 연구를 다시 돌렸고, 단서를 달긴 했지만 **이번에는 속도 향상을 발견했다.** 이는 주관적 생산성 추정치도 함께 올라간 것과 일관된다 — 가장 단순한 설명은 주관적 추정이 과장한다는 것이지만, **현재 모델에서는 여전히 속도 향상이 있다**는 것이다. (**후속 연구는 아무도 인용하지 않는 것 같다. 그렇게 재미있는 반직관적 발견이 아니니까.**)"
  - 출처: Hacker News / "I think you might be fooling yourself with AI" / 작성자 `kalkin` / https://news.ycombinator.com/item?id=49023701 / **2026-07-23** / 인용된 원문: https://metr.org/blog/2026-02-24-uplift-update/
  - 검증 상태: **1차 자료(METR 후속 발표) 링크 제시** — 책에 쓸 때 반드시 원문 확인
  - 🕒 **버전 민감 최상급.** 2026-09-05 기준, "METR = AI가 개발자를 느리게 한다"는 서술은 **2025-07 발표분만 근거로 삼는 것이고, 2026-02 후속은 반대 방향이다.** 이 책이 2025년 판만 인용하면 **선택적 인용**이 된다.

- 같은 지적을 다른 사람이 다른 스레드에서: **"I wonder what he thinks about the new METR update that showed a net speedup as a lower bound (due to participants literally not wanting to even tackle tasks with AI due to how slow it would be), with the returning devs having the greatest improvements in speedup?"**
  - 번역: "순 속도 향상을 하한선으로 보여준 새 METR 업데이트에 대해 그는 어떻게 생각할지 궁금하다(참가자들이 너무 느릴 것 같아서 아예 AI로 과제를 시도하려 하지도 않았기 때문에 하한선이다). 그리고 **재참여한 개발자들에게서 가장 큰 속도 향상이 나타났다.**"
  - 출처: Hacker News / "The Hater's Guide to Anthropic" / 작성자 `ej88` / https://news.ycombinator.com/item?id=47162701 / **2026-02-26**
  - 검증 상태: 2차 인용 — 원문 확인 필요

**방법론 비판** (이 책이 응답해야 할 쪽):

- 가장 조직적인 반박 — 원문 인용: **"the METR study is seriously flawed overall, and: 1. if you disaggregate the highly aggregated data, it shows that the slowdown was highly dependent on task type, and tasks that required using documentation or novel tasks were possibly sped up, whereas ones the developers were very experienced with were slowed down, which actually matched the developers' own reports 2. developers were asked to estimate time beforehand per-task, but estimate whether they were sped up or slowed down only once, afterwards, so you're not really measuring the same thing 3. There were no rules about which AI to use, how to use it, or how much to use it, so it's hard to draw a clear conclusion 4. Most participants didn't have much experience with the AI tools they used (just prompting chatbots), and the one that did had a big productivity boost 5. It isn't an RCT."**
  - 번역: "METR 연구는 전반적으로 심각한 결함이 있다. 그리고: 1. 고도로 집계된 데이터를 분해하면, **감속은 과제 유형에 크게 의존**했고 문서를 참조해야 하는 과제나 새로운 과제는 오히려 빨라졌을 수 있는 반면, 개발자가 아주 익숙한 과제는 느려졌다 — 이건 실제로 개발자 자신의 보고와 일치한다. 2. 개발자들은 사전에 과제별로 시간을 추정하도록 요청받았지만, 빨라졌는지 느려졌는지는 **사후에 한 번만** 추정했다. 그러니 같은 것을 재고 있는 게 아니다. 3. **어떤 AI를 쓸지, 어떻게 쓸지, 얼마나 쓸지에 대한 규칙이 없었다.** 4. 참가자 대부분이 자신이 쓴 AI 도구에 경험이 많지 않았고(그냥 챗봇 프롬프팅), 경험이 있었던 한 명은 큰 생산성 향상을 보였다. 5. **무작위 대조 시험(RCT)이 아니다.**"
  - 출처: Hacker News / "Write-only code" / 작성자 `logicprog` / https://news.ycombinator.com/item?id=47114951 / **2026-02-22** / 그가 제시한 근거 링크: https://www.fightforthehuman.com/are-developers-slowed-down-...
  - 검증 상태: 방법론 비판(근거 링크 제시) — **이 책이 METR을 쓰려면 최소한 1·2·5번에 답해야 한다**

- 짧고 유명한 경고 — 원문 인용: **"I think you might be fooling yourself if you build your entire worldview concerning the productivity benefits of AI-assisted programming around that one study from one organization that confirms your priors."**
  - 번역: "AI 보조 프로그래밍의 생산성 이득에 관한 당신의 세계관 전체를, **당신의 선입견을 확인해주는 한 기관의 한 연구** 위에 세운다면 당신은 스스로를 속이고 있는 것일지도 모른다."
  - 출처: Hacker News / "I think you might be fooling yourself with AI" / 작성자 `simonw` / https://news.ycombinator.com/item?id=49023745 / **2026-07-23**
  - 검증 상태: 정서 (발언자는 이 분야에서 영향력이 큰 계정)
  - **책에서 쓸 지점:** 이 책이 METR을 인용할 때 **이 문장을 먼저 인용하고 들어가면** 신뢰도가 오히려 올라간다. 반박을 숨기지 않는 방식.

- 경험 기반 전면 부정 — 원문 인용: **"I hate to be the anecdote guy, but with the current state of things, I have to call bullshit on the METR study, there is no world in which I work slower with AI than without."** (맥락: Claude Code + Opus 4.6 Max 구독으로 **3개 코드베이스 대규모 리팩터링을 하루 만에 끝냈다, 보통 개발자라면 1~2주 걸릴 일이었다**고 주장)
  - 번역: "일화 늘어놓는 사람이 되기 싫지만, 지금 상태에서는 METR 연구에 헛소리라고 말할 수밖에 없다. 내가 AI 없이보다 AI와 함께 더 느리게 일하는 세계는 존재하지 않는다."
  - 출처: Hacker News / "Breaking the spell of vibe coding" / 작성자 `KronisLV` / https://news.ycombinator.com/item?id=47022979 / **2026-02-15**
  - 검증 상태: ⚠️ 익명 주장(1~2주 → 1일) — 미검증 / **본인이 "일화"임을 자인한 점을 함께 인용할 것**

**❌ METR에 대한 한국 커뮤니티 반응 — 확보 실패.** GeekNews에 해당 연구 토픽이 존재한다(「경험 많은 오픈소스 개발자의 생산성에 미치는 "AI의 임팩트" 측정하기」 https://news.hada.io/topic?id=21920 / 2025-07-11). 그러나 **거기 달린 것은 GN⁺ 봇의 Lobsters 요약뿐이고 한국 사용자 댓글은 0건이다.** 한국 독자용 책이 이 연구를 핵심 근거로 쓴다면, **한국 커뮤니티에서 검증된 적 없는 자료**를 들여오는 것임을 저자가 인지해야 한다.

### ② 지표 게이밍 — 요청하신 "구체적인 게이밍 방법"

**1차에서 확보한 2건을 넘어, 이번엔 방법이 명시된 증언을 찾았다.** 무대는 "Uber가 4개월 만에 2026년 AI 예산을 Claude Code에 다 태웠다"는 402점 스레드다.

- **가장 구체적인 게이밍 방법** — 원문 인용: **"At Cerebras I know of several people who burn tokens on completely USELESS tasks (randomly changing pixels in an image) just to keep them high up on the token leaderboard. I suspect the other tokenboard leaders are doing the same. They made the metric "token usage" (which is just a proxy for LOC) so that's what they're gonna get."**
  - 번역: "Cerebras에서 나는 **완전히 쓸모없는 작업(이미지의 픽셀을 무작위로 바꾸는 것)에 토큰을 태우는 사람들 여럿을 안다. 순전히 토큰 리더보드 상위에 머물기 위해서다.** 다른 토큰보드 상위권자들도 같은 짓을 하고 있다고 의심한다. 그들이 지표를 '토큰 사용량'(이건 그냥 코드 라인 수의 대리 지표다)으로 만들었으니, 그들이 얻게 될 건 딱 그거다."
  - 출처: Hacker News / "Uber torches 2026 AI budget on Claude Code in four months" / 작성자 `joshuastuden` / https://news.ycombinator.com/item?id=47978177 / **2026-05-01**
  - 검증 상태: ⚠️ 익명 주장(특정 기업 사내 행태) — 미검증 / **정서·구조 진단으로는 최고 밀도**
  - **책에서 쓸 지점: PART 4의 가장 강한 챕터 오프닝 후보.** "토큰 리더보드"라는 실물 장치와 "이미지 픽셀 무작위 변경"이라는 실물 게이밍 방법이 한 문장에 다 있다. 이 책이 AX 성과 지표를 제안한다면 **제안 직후에 "그럼 이건 어떻게 게이밍되는가"를 자문하는 절**을 두는 게 맞다.

- 그 게이밍의 발원지 — 원문 인용: **"Tokenmaxxing is a thing now since that one CEO said he wants his $250k/yr devs to use $400-$500k/yr in tokens, so now it's all about how many agents can you have running concurrent tasks all day long."**
  - 번역: "이제 '토큰맥싱'이라는 게 생겼다. 어떤 CEO가 연봉 25만 달러짜리 개발자들이 연 40만~50만 달러어치 토큰을 쓰길 원한다고 말한 뒤로, 이제 관건은 **하루 종일 동시 과제를 돌리는 에이전트를 몇 개나 띄울 수 있느냐**가 됐다."
  - 출처: Hacker News / 같은 스레드 / 작성자 `stronglikedan` / https://news.ycombinator.com/item?id=47977486 / **2026-05-01**
  - 검증 상태: ⚠️ 익명 주장(특정 CEO 발언 요약) — 미검증

- **가장 사소하고 가장 정직한 게이밍** — 원문 인용: **"When Claude says "Shall I push it", it's way easier to just respond "yes" than it is to open a new terminal and run git push, and if you're being graded on how much AI tokens you use, saying yes looks even better for your metrics!"**
  - 번역: "Claude가 '푸시할까요?'라고 물으면, 새 터미널을 열어 `git push`를 치는 것보다 그냥 '예'라고 답하는 게 훨씬 쉽다. 그리고 **당신이 AI 토큰을 얼마나 쓰는지로 평가받고 있다면, '예'라고 하는 게 지표상 더 좋아 보이기까지 한다!**"
  - 맥락: 위 대화에서 `ambicapter`가 "우리 회사 누군가는 AI 도구로 코드를 재포맷한다", `i_love_retros`가 "내 동료도 그렇고, git 명령을 AI로 돌리는 동료도 있다 — pull, push, merge 같은 거"라고 한 데 이어진 코멘트. `i_love_retros`는 나중에 **"에이전트가 git 충돌까지 해결하게 시킨다"**고 덧붙였다.
  - 출처: Hacker News / 같은 스레드 / 작성자 `fragmede` / https://news.ycombinator.com/item?id=47978418 / **2026-05-01** (관련: `ambicapter` id=47977300, `i_love_retros` id=47977519 / id=47985404)
  - 검증 상태: 경험담
  - **책에서 쓸 지점:** 게이밍은 음모가 아니라 **마찰 최소 경로**다. 지표가 존재하는 것만으로 행동이 조용히 미끄러진다.

- 지표 자체의 결함 — 원문 인용: **"AI is supposed to be a great productivity booster, but no one has figured out a way of actually measuring developer productivity, so we'll just use the proxy of measuring whether they're using AI."**
  - 번역: "AI는 대단한 생산성 촉진제여야 하는데, **아무도 개발자 생산성을 실제로 재는 방법을 알아내지 못했다. 그러니 그냥 AI를 쓰고 있는지를 재는 대리 지표를 쓰자**는 것이다."
  - (같은 코멘트의 더 냉소적인 뒷부분) **"And 10x developers? We're actually better off if the AI "slows them down" and makes their work output look more like everyone else's. 10x developers are actually a liability, because it can be hard to quantify and measure their contributions"** (번역: "10배 개발자? 사실 AI가 그들을 '느리게' 만들어서 그들의 산출물이 다른 모두와 비슷해 보이게 하는 게 우리한테 더 낫다. 10배 개발자는 사실 부채다. 그들의 기여를 정량화하고 측정하기 어려우니까.")
  - 출처: Hacker News / "AI coding mandates are driving developers to the brink" / 작성자 `nlawalker` / https://news.ycombinator.com/item?id=43634825 / **2025-04-09**
  - 검증 상태: 정서·구조 진단(반어법 포함)
  - **책에서 쓸 지점:** **측정 불가능성이 대리 지표를 낳고, 대리 지표가 게이밍을 낳는다**는 연쇄. 이 책의 FTE 환산 제안이 이 연쇄의 어디에 서 있는지를 저자가 자각해야 한다.

- Goodhart 법칙의 교과서적 진술들:
  - **"It's actually incredible the extent to which non devs imposing KPIs on devs underestimate how badly this will get gamed, whether it's AIs, PR/line counting or whatever."** (번역: "개발자가 아닌 사람들이 개발자에게 KPI를 부과할 때, 그게 얼마나 심하게 게이밍될지를 과소평가하는 정도가 정말 놀랍다. AI든 PR/라인 카운팅이든 뭐든.") — `fidotron` / https://news.ycombinator.com/item?id=47976922 / **2026-05-01**
  - **"any metric will be gamed and if you have some costs that is associated to that, it will grow. Let's say you set some metric that says the most productive dev are the ones that has the most files changes, you can soon expect every function and structure to be its own file."** (번역: "어떤 지표든 게이밍된다. 그리고 그 지표에 비용이 결부돼 있으면 그 비용은 커진다. 파일 변경이 가장 많은 개발자가 가장 생산적이라는 지표를 세웠다고 하자. 곧 모든 함수와 구조체가 각자의 파일이 되는 걸 보게 될 것이다.") — `skydhash` / https://news.ycombinator.com/item?id=47977038 / **2026-05-01**
  - **"when you make a metric goal of "you must use AI this much", then people will use AI even in ways that isn't adding to productivity."** — `RHSeeger` / https://news.ycombinator.com/item?id=47976966 / **2026-05-01**
  - **"once the KPI is "how much AI did you use" instead of "what did you ship," the budget blowout writes itself. people will game the number."** (번역: "KPI가 '무엇을 출하했는가'가 아니라 '얼마나 AI를 썼는가'가 되는 순간, 예산 폭발은 저절로 쓰여진다. 사람들은 숫자를 게이밍한다.") — `p_stuart82` / https://news.ycombinator.com/item?id=47977838 / **2026-05-01**
  - **"It's very easy to split changes in more PRs than needed to boost the number."** (PR 수 지표에 대해) — `dieortin` / https://news.ycombinator.com/item?id=47977856 / **2026-05-01**
  - 출처(공통): Hacker News / "Uber torches 2026 AI budget on Claude Code in four months" / https://news.ycombinator.com/item?id=47976415
  - 검증 상태: 전부 정서·논리

- **95%/70% 같은 채택률 수치가 어떻게 만들어지는가** — 원문 인용: **"> 95% of Uber engineers now use AI tools monthly with 70% of committed code originating from AI. / Well, that's to be expected when using AI tools becomes relevant in your performance evaluation."**
  - 번역: "'Uber 엔지니어의 95%가 이제 매달 AI 도구를 사용하며, 커밋된 코드의 70%가 AI에서 비롯된다.' / **글쎄, AI 도구 사용이 인사평가에 반영되기 시작하면 그건 예상되는 결과다.**"
  - 출처: Hacker News / 같은 스레드 / 작성자 `MichaelNolan` / https://news.ycombinator.com/item?id=47976726 / **2026-05-01**
  - 검증 상태: 정서
  - **책에서 쓸 지점:** 이 책이 "AX 성숙도"나 "채택률"을 지표로 쓰려 한다면, **채택률은 평가 반영 여부의 함수**라는 이 반박을 먼저 받아야 한다.

- 지표 vs 가치의 정리 — 원문 인용: **"If we're trying to measure the value of adopting tool, it's probably better to measure the ROI of that tool rather than the usage % of that tool, especially when usage is basically mandated. ... You're being paid to create value for the business, which "doing what they think is productive" is a proxy for. You're not being paid to use a tool a high % of the time."**
  - 번역: "도구 도입의 가치를 재려 한다면, 그 도구의 **사용률(%)이 아니라 ROI를 재는 게 낫다.** 특히 사용이 사실상 강제된 경우에는 더 그렇다. … 당신은 사업에 가치를 창출하도록 급여를 받는 것이고, '그들이 생산적이라고 생각하는 일을 하는 것'은 그것의 대리 지표다. **당신은 도구를 높은 비율로 쓰라고 급여를 받는 게 아니다.**"
  - 출처: Hacker News / 같은 스레드 / 작성자 `misterbwong` / https://news.ycombinator.com/item?id=47977061 / **2026-05-01**
  - 검증 상태: 정서·논리

- "문지기 오류(doorman fallacy)" 프레임 — 원문 인용: **"Management in the age of AI is falling for the doorman fallacy wrt engineering. If lines of code were the most valuable aspect of software engineering, my front end JavaScript intern would've been the most valuable person in the company."**
  - 번역: "AI 시대의 경영진은 엔지니어링에 관해 **문지기 오류**에 빠지고 있다. 코드 라인 수가 소프트웨어 엔지니어링에서 가장 가치 있는 측면이었다면, 우리 프런트엔드 자바스크립트 인턴이 회사에서 가장 가치 있는 사람이었을 것이다."
  - 출처: Hacker News / 같은 스레드 / 작성자 `darth_avocado` / https://news.ycombinator.com/item?id=47977371 / **2026-05-01** / 그가 링크한 개념: https://www.jaakkoj.com/concepts/doorman-fallacy
  - 검증 상태: 정서·개념 프레임
  - **책에서 쓸 지점:** "문지기 오류"는 **직무를 관측 가능한 산출물로 환원했을 때 나머지가 사라지는 현상**을 가리키는 이름표다. 이 책이 에이전트를 FTE로 환산하려 할 때 정확히 이 함정에 들어간다 — 이름표를 빌려 쓰고 그 함정을 명시적으로 회피하는 절을 두는 게 좋다.

- 승인률 지표의 무의미 — 원문 인용: **"the "acceptance rate" doesn't actually measure whether the code is correct"** (번역: "'수락률'은 코드가 올바른지를 실제로 재지 않는다.") — `zb3` / https://news.ycombinator.com/item?id=43634194 / **2025-04-09** / "AI coding mandates are driving developers to the brink"

- **자기 파멸적 시연** — 이 인용은 A-4로도 넘어간다.
  - 원문 인용: **"We get to check a box on what AI we use when we close a ticket. I used to select "none" because most of the time that was the case... But then we started having AI demos with the CTO where the presenters would say things like "I don't know how to code in python but now I don't need to!" and the C level people would be very excited about this. That's when I realized that these poor developers who just want to brown nose and show off to big cheese are instead making an argument for their own demise. Meanwhile I asked AI to make me a test and it mocked out everything I wanted to test, testing nothing, but passing."**
    - 번역: "우리는 티켓을 닫을 때 어떤 AI를 썼는지 체크박스를 채운다. 나는 대부분 그랬기 때문에 '없음'을 선택하곤 했다… 그런데 CTO와 함께하는 AI 데모를 하기 시작했는데, 발표자들이 '저는 파이썬 코딩을 할 줄 모르는데 이제 그럴 필요가 없어요!' 같은 말을 하고 C레벨 사람들은 여기에 아주 신나 했다. 그때 나는 깨달았다. 높으신 분들한테 아부하고 뽐내고 싶을 뿐인 이 딱한 개발자들이 실은 **자기 자신의 소멸을 논증하고 있다**는 걸. 한편 나는 AI에게 테스트를 만들어달라고 했더니, 내가 테스트하려던 걸 전부 목(mock) 처리해서 **아무것도 테스트하지 않으면서 통과하는** 테스트를 만들었다."
  - 출처: Hacker News / "AI coding mandates are driving developers to the brink" / 작성자 `tfandango` / https://news.ycombinator.com/item?id=43633757 / **2025-04-09**
  - 검증 상태: 경험담
  - **책에서 쓸 지점:** "AI 사용 여부 체크박스"라는 지표 장치가 실물로 존재한다는 증거 + 그 지표가 **직원 스스로 자기 대체 논거를 만들게 하는** 구조. 절감 보고의 정치(A-4)와 직결된다.

### ③ 한국 커뮤니티 — 토큰·사용률 KPI 냉소 (이번 조사 최대 수확 영역)

한국 실무자들은 토큰 지표를 **즉시 과거의 실패한 지표(코드 라인 수·야근 시간)와 등치**시킨다. 이 반사 반응이 놀랍도록 균일하다.

- 원문 인용: **"예전에는 개발자들의 개발실력 지표를 코드 몇줄 썼냐 그걸로 지표 설정했었으니까 ㅋㅋㅋ 쓸대없이 한번에 수십만줄 쓰고 고작 기능 한두개인 쓰레기 코드들이 난무했었지"**
  - 출처: GeekNews / 「Amazon 직원들, AI 사용 압박에 불필요한 작업을 만들어 AI 토큰 소비량을 부풀리는 중」(토픽 게시 2026-05-17) / 작성자 `happing94` / https://news.hada.io/topic?id=29568 / 댓글 **2026-05-18** `[원문확인]`
  - 검증 상태: 정서
- 원문 인용: **"비슷하게 근무 시간만으로 성과 측정을 한는것도 생각나네요 ㅋㅋㅋ 결과물이 없어도 야근만 많이하면 높은 평가를 받는 상황 ㅎㅎ"**
  - 출처: GeekNews / 같은 토픽 / 작성자 `aucun` / https://news.hada.io/topic?id=29568 / **2026-05-18** `[원문확인]`
  - 검증 상태: 정서
  - 🕒 **주의:** 토픽 제목 자체가 "Amazon 직원들이 토큰 소비량을 부풀리는 중"이다. 위 §A-2-②의 Cerebras 증언(`joshuastuden`, 2026-05-01)과 **같은 달, 다른 나라, 다른 회사에서 같은 현상**이 보고됐다. **이 시간적 일치가 챕터 오프닝의 구조를 만들어준다.**

- 원문 인용: **"AI 사용량 자체를 성과 지표로 삼으면 사람들은 필요하지 않은 작업에도 AI를 사용해 숫자를 맞추게 될 수 있음 Ralph Loop 외치던분들 다 어디가셨는지.."**
  - 출처: GeekNews / 「좋은 조직문화가 AI보다 큰 생산성 향상을 만드는 이유」 / 작성자 `brainer` / https://news.hada.io/topic?id=33050 / **2026-08-31** `[원문확인]`
  - 검증 상태: 정서

- **토큰 지표의 구조적 결함을 정확히 짚은 댓글** — 원문 인용: **"AI가 잘못된 판단을 했거나 내부적인 오류가 발생하면 토큰이 무지막지하게 낭비되고, 그렇다고 그걸 환불해주는 것도 아니니.. 토큰 사용량과 비용은 정비례하지만, 토큰 사용량과 생산성을 의미있게 연관짓기 어렵다는 게 기업 입장에서는 큰 걸림돌일 것 같습니다."**
  - 출처: OKKY / 「AI 사용을 점점 제한 하는 기업이 늘어날 것으로 예상 되네요」 / 작성자 `사과맛오렌지` / https://okky.kr/articles/1562362 / 게시글 2026-08-16, 댓글 "20일 전"(2026-09-05 조회) `[원문확인]`
  - 검증 상태: 정서·논리
  - **책에서 쓸 지점: 이 문장이 토큰 기반 FTE 환산에 대한 가장 정확한 반박이다.** 토큰↔비용은 정비례, 토큰↔생산성은 무관. **에이전트의 "일한 양"을 비용으로 재면, 실패할수록 많이 일한 것으로 잡힌다.** 이 책이 에이전트 성과를 소비량으로 재려는 어떤 제안을 하든 이 반박을 먼저 받아야 한다.

- 신입일수록 토큰을 많이 쓴다 — 지표의 역진성: **"지금 신입이 토큰은 제일 많이 쓰는 상황입니다 하네스다 루프다 주워들은 건 많아서 에이전트끼리 뻘짓하느라 돈만 까먹죠"**
  - 출처: OKKY / 같은 글 / 작성자 `자바킬러` / "19일 전"(2026-09-05 조회) `[원문확인]`
  - 검증 상태: ⚠️ 익명 주장(사내 관찰) — 미검증 / 정서로는 유효

- **게이밍 선언과 실제 측정 시도** — 이 한 쌍이 특히 좋다:
  - **"토큰 사용량 기준으로 하면 삽질하도록 풀 자동화하면 되나요? ㅋㅋ"** — `달고양이`
  - 그리고 실제로 재본 결과: **"궁금해져서 클로드 코드한테 현재 클로드 코드 토큰 총 사용량 달라고 했더니 321억 토큰이라고 뻥튀기해주는데요. 그중 캐시 사용량이 97프로라는뎁쇼… 캐시 빼고 순수는 1.3억이라는데.. 총 토큰으로 보고하면 됩니까?"** (후속: **"중복 집계였답니다.. ccusage로 측정한 결과 89.2억 크흡. 아쉽구려.."**)
  - 출처: OKKY / 「환장의 AI 성과 측정 시스템」 / 작성자 `달고양이` / https://okky.kr/articles/1558387 / 게시글 2026-06-09, 댓글 "3개월 전"(2026-09-05 조회) `[원문확인]`
  - 검증 상태: ⚠️ 익명 주장(수치는 본인 환경 자체 측정) — 미검증
  - **책에서 쓸 지점: 이건 게이밍 이전에 계측 자체가 성립하지 않는다는 증거다.** 같은 사람이 같은 도구로 잰 총 토큰이 **321억 → 89.2억**으로 바뀐다. "총 토큰으로 보고하면 됩니까?"라는 반쯤 농담이 사실은 **지표 정의의 부재**를 정확히 찌른다. FTE 환산을 제안하는 책은 **분모·분자의 정의를 문서화하는 절**이 반드시 필요하다.

- "AI 사용률 몇 %"라는 질문 자체가 성립하지 않는다:
  - **"퍼센트를 어찌 정하나요 세션 열개 정도를 계속 돌리면서 일해요 그러면 1000%?"** — `개발야호`
  - **"100% 면 내가 출근해서 일을 시킬 필요도 없단 말이니 천국이죠."** — `월급은나의빛`
  - 출처: OKKY / 「업무시 AI 사용률 몆 % 정도 되시나요?」 / https://okky.kr/articles/1562609 / 게시글 2026-08-21, 댓글 "15일 전"(2026-09-05 조회) `[원문확인]`
  - 검증 상태: 정서
  - **책에서 쓸 지점:** 위 `MichaelNolan`의 "95%/70%"와 짝지어라. **채택률이라는 지표는 단위가 없다.**

- 경영진의 오독 구조:
  - **"경영자를 포함한 비프로그래머 입장에서 코드 작성이 단순히 목적 결과를 내는 정해진 답들 중 하나를 찍어내기만 하는 타이핑이라고 생각하는 게 근본적인 괴리가 아닐까 싶네요."** — `synastry` / GeekNews / 「The Agentic Awakening — 코딩이 10배 빨라져도 조직 생산성이 따라오지 않는 이유」 / https://news.hada.io/topic?id=33058 / 게시 2026-08-31, 댓글 "5일전"(2026-09-05 조회) `[페치경유]`
  - **"사람이 할때는 2개만 만들수 있던거를 ai 쓰면 1000개를 만들수 있는데 그렇 다고 ai 를 쓰고 2개를 만들라고 하면 시간이 줄어 드는게 아니라 1000개랑 같은 속도가 나오는데 이걸 대표들이 착각 하는거 같아요."** — `dong bang` / OKKY / https://okky.kr/articles/1556920 / 게시글 2026-05-14, 댓글 "4개월 전"(2026-09-05 조회) `[원문확인]`
  - 검증 상태: 정서·판단

### A-2 커버리지

**확보**
- METR **찬성 3건 / 방법론 비판 3건 / 후속 연구 반전 2건** — **양쪽 다 확보 완료.** 특히 **2026-02 METR 후속(속도 향상)**은 이 책의 근거 사용법을 바꿀 수 있는 정보다.
- 지표 게이밍의 **구체적 방법 4건** (토큰 리더보드용 무의미 작업 / 토큰맥싱 / 승인 클릭 / PR 쪼개기) — 1차 대비 대폭 보강
- Goodhart 계열 정리 인용 **6건** (전부 2026-05 단일 스레드 — 밀도 높음)
- **한국 토큰·사용률 KPI 냉소 10건** (GeekNews 3 + OKKY 7, 2026-05~08) — **1차에 없던 완전 신규 영역**

**비어 있음**
- **DORA/SPACE에 대한 정면 토론 — 확보 실패.** "DORA metrics gaming"류 질의에서 유의미한 댓글 다수 스레드를 못 찾았다. 커뮤니티는 DORA를 이름으로 논쟁하기보다 **"라인 수/PR 수/토큰"이라는 구체 지표로** 논쟁한다. 이 책도 그 언어를 쓰는 게 맞다.
- **METR 한국 반응 — 0건** (GeekNews 토픽은 있으나 한국 사용자 댓글 없음).
- **"생산성은 잴 수 없다"는 유서 깊은 논쟁의 고전 스레드 — 얕게만 확보.** 2013년 "What makes developers productive?" 등 오래된 스레드를 스치듯 봤을 뿐 정면으로 파지 못했다. 필요하면 3차에서 `"developer productivity"` 단일 구절로 2010~2020 구간을 따로 파야 한다.

---

## A-3. FTE 환산·정원 산입·라이선스에 대한 실무 반응

### ① "에이전트를 정원으로 센다"는 발상은 이미 벤더가 먼저 했다 — 그리고 반응은 나빴다

**1차에서 확보 실패한 "라이선스 비용 우려의 직접 인용"을 이번에 확보했다.** 무대는 2026-04-14 HN 스레드 「Microsoft exec suggests AI agents will need to buy licenses, just like employees」(32점).

- **가장 직접적인 반응** — 원문 인용: **"What the hell? If a company gets more efficient and uses fewer people - Microsoft's immediate reaction is to figure out how to invent some kind of digital seats so they can keep taxing the headcount. Lol"**
  - 번역: "이게 뭐야? 회사가 더 효율적이 되어 사람을 덜 쓰면 — 마이크로소프트의 즉각적인 반응은 **정원에 계속 과세할 수 있도록 일종의 디지털 좌석을 발명하는 방법을 궁리하는 것**이다. 웃기네."
  - 출처: Hacker News / 작성자 `latand6` / https://news.ycombinator.com/item?id=47762102 / **2026-04-14** / 원 기사: businessinsider.com
  - 검증 상태: 정서
  - **책에서 쓸 지점: 이 책의 핵심 장치("에이전트를 정원에 산입한다")가 이미 벤더 과금 논리로 존재한다는 사실을 이 책은 반드시 다뤄야 한다.** 독자가 "에이전트에 사번을 준다"를 읽는 순간 떠올릴 최악의 그림이 **"그럼 라이선스도 사야 하나"**다. 실제로 그 그림이 2026년에 현실이 됐다.

- **방어 논리**도 스레드에 있다(양쪽을 다 기록한다):
  - 원문 인용: **"You get charged for usage of their service and they chose to do that by assuming an average usage per license / person and charging that. When you get to cram in more usage/person by using a third party, they either charge you for access via that third-party or that could also just increase prices per personal license. ... They don't care about your headcount, but you do use more service."**
    - 번역: "당신은 그들의 서비스 사용에 대해 과금되는 것이고, 그들은 **라이선스/사람당 평균 사용량을 가정해서** 그렇게 하기로 한 것이다. 제3자를 통해 사람당 사용량을 더 밀어 넣게 되면, 그들은 그 제3자를 통한 접근에 과금하거나 개인 라이선스 가격을 그냥 올릴 것이다. … **그들은 당신의 정원에 관심이 없다. 다만 당신이 서비스를 더 쓰는 것이다.**"
    - 출처: 같은 스레드 / 작성자 `1718627440` / https://news.ycombinator.com/item?id=47762715 / **2026-04-14**
  - 같은 사람의 비유: **"You go to an all you can eat restaurant. Would you find it, that it wouldn't make sense to charge for each bag you start stuffing with food?"** (번역: "무한리필 식당에 갔다고 하자. 음식을 담기 시작한 가방마다 요금을 물리는 게 말이 안 된다고 생각하겠는가?") — https://news.ycombinator.com/item?id=47766104
  - 반박: **"It doesn't make any sense. Humans are non-fungible AI is not, they are just arbitrarily imposing such limitations, which can impact the workflows of businesses."** (번역: "전혀 말이 안 된다. **인간은 대체 불가능하지만 AI는 그렇지 않다.** 그들은 그냥 자의적으로 그런 제약을 부과하는 것이고, 이는 기업의 워크플로에 영향을 줄 수 있다.") — `bit1993` / https://news.ycombinator.com/item?id=47764995 / **2026-04-14**
  - 검증 상태: 전부 정서·논리
  - **책에서 쓸 지점 — 이게 이 축의 가장 깊은 논점이다.** "인간은 대체 불가능하지만 AI는 그렇지 않다(non-fungible vs fungible)"는 구분은 **에이전트를 FTE로 세는 것이 왜 인간을 FTE로 세는 것과 다른가**를 정확히 짚는다. 사람 1명은 하나의 개체지만, 에이전트 "1대"는 임의로 쪼개고 합칠 수 있다. **그럼 "1대"의 경계는 누가 정하는가?** 이 책의 등록·정원 산입 설계가 반드시 답해야 할 질문이다.

- **라이선스 회피의 즉각적 결론** — 원문 인용: **"5 mn after they implement that there will be a tool to have only one agent for the whole company"**
  - 번역: "그걸 구현하고 5분 뒤에는 **회사 전체에 에이전트를 딱 하나만 두는 도구**가 나올 것이다."
  - 후속 반론: **"Then you need to pay up via user CALs as is already common practice with windows server licensing."** (번역: "그럼 윈도우 서버 라이선싱에서 이미 흔한 관행처럼 사용자 CAL로 지불해야 할 것이다.") — `TheTxT`
  - 출처: 같은 스레드 / `poulpy123` https://news.ycombinator.com/item?id=47767156 / `TheTxT` https://news.ycombinator.com/item?id=47777997 / **2026-04-14~15**
  - 검증 상태: 정서
  - **책에서 쓸 지점:** **"에이전트 1대"의 경계가 과금 단위가 되는 순간, 조직은 경계를 조작해 회피한다.** 이 책이 에이전트 등록 단위를 정의할 때, 그 단위가 **비용·정원·평가 중 무엇과 연결되는지**에 따라 현장이 단위를 조작할 유인이 생긴다. 등록 단위와 과금 단위를 분리하는 설계 논거가 여기서 나온다.

- 선례 지적 — 원문 인용: **"SAP has been doing something similar for years now. They call it indirect use. If a system integrates with SAP and accesses data you have to pay licensing fees. Even if you host the SAP system yourself."**
  - 번역: "SAP는 몇 년째 비슷한 걸 해왔다. 그들은 그걸 **간접 사용(indirect use)**이라고 부른다. 어떤 시스템이 SAP와 통합되어 데이터에 접근하면 라이선스 비용을 내야 한다. SAP 시스템을 직접 호스팅하고 있어도 마찬가지다."
  - 출처: 같은 스레드 / 작성자 `monospaced` / https://news.ycombinator.com/item?id=47762611 / **2026-04-14**
  - 검증 상태: 업계 관행 진술 (⚠️ 세부 조건은 계약별로 다름 — 책에 쓰려면 SAP 라이선스 정책 원문 확인 필요)
  - **책에서 쓸 지점:** "에이전트 과금"은 신개념이 아니라 **SAP 간접 사용의 재판**이다. 이 계보를 밝히면 독자가 앞으로 겪을 협상을 예측할 수 있다.

- 나머지 반응들(전부 같은 스레드, 2026-04-14~15):
  - **"From the we-accidentally-nuked-our-business-strategy department. Bravo, Microsoft, for finally noticing the entailment of replacing workers with AI most critical for a company whose proven revenues come from selling "seats""** (번역: "우리가-실수로-우리-사업전략을-핵폭격했다 부서에서 왔습니다. 마이크로소프트, 검증된 매출이 '좌석' 판매에서 나오는 회사에 가장 치명적인, 노동자를 AI로 대체하는 것의 귀결을 마침내 알아차린 것을 축하합니다.") — `1attice` / https://news.ycombinator.com/item?id=47768403
  - **"This just sounds like a new kind of rent seeking."** (번역: "이건 그냥 새로운 종류의 지대 추구처럼 들린다.") — `cybercatgurrl` / https://news.ycombinator.com/item?id=47773870
  - **"Why are agents using licensed software anyway? AI should be using APIs."** (번역: "애초에 에이전트가 왜 라이선스 소프트웨어를 쓰나? AI는 API를 써야 한다.") — `tnelsond4` / https://news.ycombinator.com/item?id=47875957 / **2026-04-23**
  - 검증 상태: 정서

- 같은 흐름을 SaaS 산업 차원에서 짚은 발언:
  - 원문 인용: **"So they will switch to per-agent pricing instead of per-user."**
    - 번역: "그러니까 그들은 사용자당이 아니라 **에이전트당 과금**으로 전환할 것이다."
    - 출처: Hacker News / "The ChatGPT/Codex app bundles a full copy of LibreOffice" / 작성자 `petilon` / https://news.ycombinator.com/item?id=49529033 / **2026-09-01** (검색 나흘 전)
  - 원문 인용: **"If Salesforce is pivoting to a 50/50 human-agent workforce, the traditional SaaS revenue model effectively hits a ceiling. The move toward consumption-based pricing for "digital headcount" seems inevitable"**
    - 번역: "Salesforce가 **인간-에이전트 50대 50 인력 구성**으로 전환한다면, 전통적 SaaS 매출 모델은 사실상 천장에 부딪힌다. **'디지털 정원(digital headcount)'에 대한 소비 기반 과금**으로의 이동은 불가피해 보인다."
    - 출처: Hacker News / "Salesforce's "SaaS Seat License Crisis": Transitioning to AI Digital Headcount" / 작성자 `timarits` / https://news.ycombinator.com/item?id=46987448 / **2026-02-12**
    - 검증 상태: ⚠️ 자기 콘텐츠 홍보 성격의 게시글(팟캐스트 에피소드 소개) — 커뮤니티 여론 근거로는 약함. **"digital headcount"라는 용어가 2026년 초에 이미 유통되고 있었다**는 용어 증거로만 쓸 것.
  - **책에서 쓸 지점:** 이 책이 "디지털 정원"이라는 표현을 쓴다면, **그 표현이 이미 벤더 과금 담론의 용어라는 사실**을 인지하고 써야 한다. 같은 단어를 조직 설계 용어로 되찾아오려면 명시적 구분이 필요하다.

### ② 한국 커뮤니티 — 라이선스·시트 비용 (매우 두터움)

한국 실무자의 핵심 불만은 **개인 요금제와 기업 요금제의 단절**이다. 이건 HN에 없는 각도다.

- 원문 인용: **"님 개인용과 기업용의 가격 레벨이 차원이 다르고 기업용은 max 가 없습니다."**
  - 출처: OKKY / 「AI 사용을 점점 제한 하는 기업이 늘어날 것으로 예상 되네요」 / 작성자(글쓴이) `흰꿈둘` / https://okky.kr/articles/1562362 / 게시글 2026-08-16, "20일 전"(2026-09-05 조회) `[원문확인]`
  - 검증 상태: ⚠️ 익명 주장(제품 요금제 구성) — 미검증
- **회사 한도가 부족해 사비를 보태는 사례** — 시트 정책 설계에 직접 시사점:
  - 원문 인용: **"저희도 20달러짜리 kiro 해주고, 한달동안 아껴써라~ 하고 있습니다. ㅠ 아껴써도 부족해서 사비로 깃허브코파일럿 10달러 결제했어요 ㅠ"**
  - 출처: OKKY / 「회사가 클로드 엔터프라이즈로 이전했는데... (feat. 요금 폭탄)」 / 작성자 `xml개발자` / https://okky.kr/articles/1557778 / 게시글 2026-05-29, "3개월 전"(2026-09-05 조회) `[원문확인]`
  - 검증 상태: ⚠️ 익명 주장(사내 정책·금액) — 미검증 / 경험담으로는 강력
  - **책에서 쓸 지점: 이건 shadow AI의 경제적 뿌리다.** 1차에서 확보한 shadow AI 6건이 *왜* 생기는지를 이 한 문장이 설명한다 — **회사가 준 시트가 부족하면 직원이 사비로 채우고, 그 순간 통제 밖으로 나간다.** 이 책의 등록·통제 설계는 **시트 한도 설계와 분리될 수 없다.**
- **"엔터프라이즈 기업들 덕분에 제가 20달러에 pro를 쓰고 있는거겠죠"** — `catcode` / 같은 글 / "3개월 전"(2026-09-05 조회) `[원문확인]`
- **"대기업들은 인건비를 제일 아까워하지 다른비용은 별로 아까워하지 않는것 같아요"** — `아휴` / https://okky.kr/articles/1562362 / "20일 전"(2026-09-05 조회) `[원문확인]`
  - **책에서 쓸 지점:** 위 `itake`의 "기술 도구 예산과 인건비 예산은 다른 예산이다"(§A-1-③)와 **정확히 같은 관찰이 한국에서 독립적으로 나왔다.** 두 인용을 나란히 놓으면 "예산 칸막이"가 국지적 현상이 아님을 보일 수 있다.

- **라이선스가 기술 판단이 아니라 벤더 정치라는 인식** (MS의 Claude Code 라이선스 회수 건):
  - **"명분은 Copilot을 더 쓰라는거지만 실제로 비용 증가도 한몫 했을 거 같습니다. 비용은 앞으로 더 가파르게 오를 예정이니까요."** — `hyungyunlim` / GeekNews / 「마이크로소프트, Claude Code 라이선스 회수 시작하다」 / https://news.hada.io/topic?id=29759 / 토픽 2026-05-22, 댓글 "3달전"(2026-09-05 조회) `[페치경유]`
  - **"결국 타사 제품이 비싸니까 자사제품을 쓰라는 것이지요."** — `흰꿈둘` / https://okky.kr/articles/1562362 / "19일 전"(2026-09-05 조회) `[원문확인]`
  - 검증 상태: 정서·추정

- **좌석제 → 사용량 과금 전환에 대한 가장 격렬한 반발** (GitHub Copilot 프리미엄 요청 과금):
  - **"저도 환불했네요... AI 크레딧도 롤오버 되지도 않고...명확한 기준없이 토큰사용량 과 사용 시간(Think할 때 드는 부분)을 적용한다는게... 종량제로 하든가... 아에 사용료로 따질거면 일정 유효기간을 두고 롤 오버 하게 해야하는데... 그럴꺼면 쓸 이유가 없죠..."** — `minsuchae`
  - **"1년 구독했던거 연장 안한 게 신의 한수네요 Opus 27x 배율로 내고 쓸 바에는 차라리 클로드 API 요금제를 쓰는 게 낫겠어요."** — `click` ⚠️ 익명 주장(배율 수치) — 미검증
  - **"저렴한 게 장점이고 나머린 전부 단점이었는데 쓸 이유가 없어진 듯."** — `slowandsnow`
  - 출처(공통): GeekNews / https://news.hada.io/topic?id=28962 / 토픽 **2026-04-28**, 댓글 "4달전"(2026-09-05 조회) `[페치경유]`
  - 검증 상태: 정서
  - **책에서 쓸 지점:** 과금 단위가 **좌석에서 소비량으로 바뀌는 순간 예측 가능성이 사라지고, 예측 불가능성 자체가 이탈 사유가 된다.** 이 책이 에이전트 비용을 정원 회계에 넣자고 제안한다면, **예산 편성 시점에 그 비용을 예측할 수 있는가**가 실무 채택의 갈림길이다.

- 보안 요구와 비용의 트레이드오프: **"amazon bedrock 을 통해 claude code 를 사용합니다. 보안성이 높지만 종량제로 비쌉니다."**
  - 출처: OKKY / 「외부 AI 사용시 보안은 어떻게 해결하나요?」 / 작성자 `월급은나의빛` / https://okky.kr/articles/1559038 / 게시글 2026-06-19, "3개월 전"(2026-09-05 조회) `[원문확인]`
  - 검증 상태: 경험담
  - **책에서 쓸 지점:** 축 1(등록·통제)과 축 5(비용)의 교차점. **통제를 강화하는 경로가 곧 비용을 올리는 경로다.** 이 책의 등록·감사 설계는 이 비용을 숨기면 안 된다(1차 반박 E와 같은 결).

### ③ RPA 계보 — 봇 FTE 환산의 원조

**1차에서 RPA 회고 3건을 확보했다. 이번엔 "봇 = N FTE"라는 환산 자체의 계보를 찾으려 했는데, 결과는 부분적이다.**

- **RPA 개발자 본인의 증언(2020)** — 발주 동기가 명시적으로 정원 감축이었다:
  - 원문 인용: **"I'm currently doing RPA (Robotic Process Automation) development and our team is swamped with requests from teams who are trying to cut the fat out of their departments and reduce head count to try and save the company billions over the next five years."**
    - 번역: "나는 현재 RPA(로보틱 프로세스 자동화) 개발을 하고 있는데, **우리 팀은 자기 부서의 군살을 빼고 정원을 줄여 향후 5년간 회사에 수십억을 절감하려는 팀들의 요청에 파묻혀 있다.**"
  - 출처: Hacker News / "How many jobs do robots really replace?" / 작성자 `at-fates-hands` / https://news.ycombinator.com/item?id=23094942 / **2020-05-06**
  - 검증 상태: ⚠️ 익명 주장(수십억 절감 목표) — 미검증 / 종사자 증언
  - 🕒 **6년 전 발언이다.** 인용할 때 반드시 시점을 밝히고, **"이 요청들의 결과가 무엇이었는지는 이 발언이 말해주지 않는다"**는 점을 함께 써야 한다. 이 인용의 가치는 결과가 아니라 **동기가 처음부터 정원 감축이었다는 기록**이다.

- **RPA가 남긴 것에 대한 진단(2021)**:
  - 원문 인용: **"they're using legacy software that will forever be crystalized under a flimsy layer of UiPath automation. Lots of large institutions in this market hence the large market capitalization. If things weren't complicated enough now they will see a lot more spaghetti infrastucture and this is not a turnkey solution, this needs an initial setup and a lot of maintenance as well"**
    - 번역: "그들은 **UiPath 자동화라는 얄팍한 층 아래 영원히 결정화될 레거시 소프트웨어**를 쓰고 있다. 이 시장에는 대형 기관이 많고 그래서 시가총액이 크다. 지금까지도 충분히 복잡하지 않았다면, 이제 훨씬 더 많은 스파게티 인프라를 보게 될 것이다. 그리고 이건 턴키 솔루션이 아니다. **초기 셋업과 많은 유지보수가 필요하다.**"
  - 출처: Hacker News / "UiPath Inc S-1 SEC Form" / 작성자 `tartoran` / https://news.ycombinator.com/item?id=26607265 / **2021-03-28**
  - 검증 상태: 정서·판단
  - 🕒 5년 전. **1차에서 확보한 `euphetar`의 "유지보수 부담이 대체하려던 노동보다 커졌다"(2026-07)와 짝지으면 5년 간격의 예측-확인 구조가 만들어진다.**

**❌ "봇 1대 = N FTE로 보고했는데 실제로는 아무도 안 줄었다"는 직접 회고 — 확보 실패.** 이 문서에서 가장 아쉬운 공백이다. HN에는 RPA 실무자가 희소하고(1차 커버리지에서도 같은 진단), 한국 커뮤니티에는 **RPA 회고 스레드가 0건**이다(GeekNews 11,168건·OKKY 1,665건 전수 인덱스 확인). 검색으로 나오는 건 전부 **업계 기사**다 — ZDNet 「RPA 도입 후 오히려 업무가 증가하는 이유」, ZDNet 「회사의 RPA가 구석에서만 소용돌이 치는 까닭은」, 디지털데일리, 투이컨설팅 등. 원인 추정: **RPA 담론의 피크가 2019~2022년이라 커뮤니티 활성 구간과 어긋난다.**
→ **web-researcher에 이관 권장.** 이 계보는 이 책에 결정적인데 커뮤니티가 아니라 컨설팅·업계 매체에 있다. 위 ZDNet 2건은 제목만으로도 이 책의 논지를 지지한다.

### A-3 커버리지

**확보**
- **에이전트 라이선스·시트 논쟁의 정본 스레드 확보** (HN 2026-04-14, 찬반 양쪽 10건) — **1차 확보 실패 항목 해소**
- 한국 라이선스·비용 인용 **9건** (OKKY·GeekNews, 2026-04~08) — 개인/기업 요금제 단절, 사비 충당, 좌석→종량 전환 반발
- "digital headcount"·"per-agent pricing" 용어 유통 증거 2건
- RPA 계보 인용 2건 (2020·2021) — 동기와 결과 양쪽

**비어 있음**
- **"봇 = N FTE" 환산 회고 — 0건.** 위 참조. **이 문서 최대의 공백이다.**
- **`digital FTE`·`bot FTE` 같은 용어 자체에 대한 토론 — 0건.** 커뮤니티는 이 용어를 쓰지 않는다. **이 책이 FTE 환산 용어를 도입한다면 커뮤니티에 선례가 없는 용어를 만드는 것**임을 저자가 알아야 한다.
- **Agentforce 실사용 후기 — §B-3 참조(사실상 비어 있음).**

---

## A-4. 절감된 시간·인력의 처리 — 【이 책의 가장 민감한 대목】

> **이 절의 결론.** 요청하신 **"효율화했다고 보고했더니 정원이 깎였다"**는 정확한 형태의 증언은 소수지만, **그 논리를 학습한 결과로서의 행동**(성과 축소 보고·은폐·숨기라는 조언)은 한국·영어권 양쪽에서 대량으로 나온다. **경고의 근거는 사건이 아니라 학습된 규범의 형태로 존재한다.** 이게 더 강한 증거일 수 있다.

### ① 성과를 솔직히 보고하면 손해라는 인식 — 학습된 규범

**§A-1-③의 `thisisit` 인용("우리 회사에서 사람들은 항상 인력 절감분을 축소해서 보고한다")이 이 절의 대표 증거다. 여기 반복하지 않되, 이 절의 논지는 그 인용 위에 선다.**

- **가장 직접적인 한국어 증언** — 원문 인용: **"개발자가 먼저 나서서 미친 생산성을 보여줬기에… 관리자는 "더 미친 생산성" 을 바랄 뿐입니다. 그러게 적당히 사용했어야죠. 필요할때만 꺼내쓰는 도구에 그쳤어야 하는데 되돌릴수도 없고 참…"**
  - 출처: OKKY / 「"클로드로 하면 되잖아" 식의 업무 지시, 다른 회사도 이런가요?」 / 작성자 `The developer.` / https://okky.kr/articles/1556920 / 게시글 2026-05-14, 댓글 "4개월 전"(2026-09-05 조회) `[원문확인]`
  - 검증 상태: 정서·경험 기반 규범
  - **책에서 쓸 지점: 이 문서 전체에서 이 책의 경고에 가장 정확히 대응하는 한국어 인용이다.** "그러게 적당히 사용했어야죠"라는 문장은 **성과 공개가 곧 기준선 상향이라는 학습을 완료한 상태**를 보여준다. 감원이 아니라 **기준선 상향**이라는 형태의 처벌이다. 이 책이 "절감이 감원으로 읽히면 현장은 성과를 숨긴다"고 쓰려 한다면, 실제 메커니즘은 한 단계 더 흔하다 — **절감이 새 기준선으로 읽히면 현장은 성과를 숨긴다.**

- **성과를 숨기라는 직접적 조언** — 원문 인용: **"자신의 능력이 100이라고 치면 50으로 업무를 처리할 수 있다면 50으로 처리하고.. 나머지는 눈치껏... 자신의 능력 100을 다 보여주지 않으심이.."**
  - 출처: GeekNews / Ask GN 「LLM으로 생산성이 증가한거 같은데요. 왜 저는 여전히 바쁠까요?」 / 작성자 `baeba` / https://news.hada.io/topic?id=20632 / **2025-05-02** `[원문확인]`
  - 검증 상태: 정서·조언(규범 진술)

- **그 조언을 정면으로 때리는 반론** (양쪽 다 기록한다 — 이 논쟁은 끝나지 않았다):
  - 원문 인용: **"답변들 저질이네요. 생산성 향상이 어떻게 약탈이나 해고나 일을 안하게 되는걸로 이어지나요? 생각 고치지 않으면 앞으로 도태됩니다. 다 같이 생산성이 올라가니 앞으로 기준치가 올라갑니다. 더 노력해여 합니다. 정신 차리세요 제발."**
  - 출처: GeekNews / 같은 스레드 / 작성자 `github88` / https://news.hada.io/topic?id=20632 / **2025-05-02** `[원문확인]`
  - 검증 상태: 정서·반론
  - **책에서 쓸 지점: 이 두 인용을 나란히 배치하는 것만으로 챕터 하나의 긴장이 만들어진다.** 흥미롭게도 **반론자도 "기준치가 올라간다"는 사실 자체는 부정하지 않는다.** 논쟁은 사실이 아니라 그 사실에 대한 태도다. 이 책은 여기서 편을 들지 말고 **구조를 보여주는 쪽**이 낫다.

- **같은 스레드의 나머지 — "총량은 변하지 않는다"는 합의**:
  - **"직원 편하라고 AI 도입하라는게 아니죠. 생산성 높인 만큼 일을 더 하라는 거니까요. 직원이 하는 일의 총량은 변함이 없게됩니다."** — `casio` / **2025-05-02** `[원문확인]`
  - **"업무 효율은 AI로 올라가고 그만큼 효율 높은 수준의 일을 더하게 되어 회사 입장에서는 한 직원의 생산성이 올라가는 구조 아닐까요~ ㅠㅠ"** — `geekbini` / **2025-07-01** `[원문확인]`
  - **"업무효율성이 올라간 만큼 직원을 layoff하죠 필요없어진 코드는 삭제당하지만 필요없어진 직원은 경쟁사나 창업을 하면 회사에 큰 득은 아닐겁니다"** — `codemasterkimc` / **2025-05-02** `[원문확인]`
  - 출처(공통): GeekNews / https://news.hada.io/topic?id=20632
  - 검증 상태: 정서
  - **책에서 쓸 지점: 이 GeekNews Ask GN 스레드(13댓글)가 A-4의 정본이다.** 「생산성이 증가했는데 왜 나는 여전히 바쁜가」라는 질문 제목 자체가 챕터 오프닝으로 쓸 수 있다.

- **도구가 일을 줄이는 게 아니라 상시화한다** — 이 축에서 가장 우아한 통찰:
  - 원문 인용: **"엑셀이 나와서 바뀐 것의 핵심은 일을 자동화시켜준 것이라기 보다는. 일을 실시간으로 그리고 항시적으로 만든거죠. 발표 5분전이라도 수정할수 있는 긴장된 상태가 유지되니.. 일하는 시간개념이 실시간인 동시에 항시적이라 결국 바빠집니다."**
  - 출처: GeekNews / 같은 스레드 / 작성자 `filekiwi` / https://news.hada.io/topic?id=20632 / **2025-05-13** `[원문확인]`
  - 검증 상태: 정서·역사 유비
  - **책에서 쓸 지점: 챕터 오프닝 최상급 후보.** "엑셀은 일을 자동화한 게 아니라 상시화했다"는 문장은 **AX가 절감을 만들지 않는 구조적 이유**를 한 문장으로 설명한다. FTE 환산의 분모가 왜 안 줄어드는가에 대한 답이기도 하다.
  - 짝이 되는 인용: **"기차가 등장하고 자동차가 등장하고 비행기가 등장해도 일일교통권이 넓어질뿐이지 사람이 덜 바빠진게 아닌 것 처럼 도구가 더 좋아져도 할 수 있는 범위나 능력이 올라갈 뿐 덜 바빠지는건 아닌 것 같아요."** — `kimjoin2` / 같은 스레드 / **2025-05-01** `[원문확인]`

- 절감 압력이 상시화된 산업 현실:
  - **"납품업체도 매년 5%씩 원가절감 안하면 짤립니다 개인도 마찬가지예요. 매일이 혁신이어야 자리보전 가능합니다"** — `바람을바람` / OKKY / https://okky.kr/articles/1556920 / "4개월 전"(2026-09-05 조회) `[원문확인]` / ⚠️ 익명 주장(5% 관행) — 미검증
  - **"한국에선 다 의미없는 얘기입니다. 뭘 해서 인건비 줄이는게 미덕인 곳이 대한민국입니다."** — `컴포지트` / OKKY / https://okky.kr/articles/1562362 / "20일 전"(2026-09-05 조회) `[원문확인]`
  - 검증 상태: 정서
  - **책에서 쓸 지점:** 한국 독자용 책이므로 이 두 인용은 **"재투자·고용 보장"이라는 처방이 한국 맥락에서 어떻게 들리는지**를 알려준다. 이 책이 재투자를 권한다면 **왜 한국에서는 그게 더 어려운가**를 먼저 인정해야 신뢰를 얻는다.

### ② 영어권 — "효율적이면 벌 받는다"

- 원문 인용: **"> simply because the market has never really punished people for being less efficient at their jobs / In fact, it tends to be the opposite. You being more efficient just means you get "rewarded" with more work, typically without an appropriate increase in pay to match the additional work either. Especially true in large, non-tech companies/bureaucratic enterprises where you are much better off not making waves, and being deliberately mediocre... In a big team/org, your personal efficiency is irrelevant. The work can only move as fast as the slowest part of the system."**
  - 번역: "'시장은 사람들이 일을 덜 효율적으로 한다고 해서 실제로 벌준 적이 없다'는 말에 대해 — **사실은 정반대에 가깝다. 당신이 더 효율적이라는 건 그냥 더 많은 일로 '보상'받는다는 뜻**이고, 대개는 추가된 일에 상응하는 급여 인상도 없다. 특히 크고 비(非)테크인 기업/관료적 대기업에서 그렇다. 거기서는 **파장을 일으키지 않고 의도적으로 평범한 게 훨씬 낫다**… 큰 팀/조직에서 당신 개인의 효율은 무관하다. 일은 시스템에서 가장 느린 부분만큼만 빠르게 움직인다."
  - 출처: Hacker News / "Everyone in Seattle hates AI" / 작성자 `thewebguyd` / https://news.ycombinator.com/item?id=46140811 / **2025-12-03**
  - 검증 상태: 정서·조직 진단
  - **책에서 쓸 지점: "의도적으로 평범해지는 게 낫다(being deliberately mediocre)"** — 이 표현이 이 책의 경고를 정확히 뒤집어 보여준다. 절감을 감원(또는 기준선 상향)으로 번역하는 조직에서 **최적 전략은 절감하지 않는 것**이 된다.

- **예산 논리로 확장** — 자동화 절감이 왜 부서에 해로운가:
  - 원문 인용: **"Always spend your budget, ideally about 5-10% over (find out what others do). If you don't, next year you get less. You can't save 20k this year and spend it next year. You can't even save 20k and get rewarded for being cost efficient as you'll be punished with a lower budget next year. Yes it's stupid."**
    - 번역: "**항상 예산을 다 써라. 이상적으로는 5~10% 초과해서**(남들이 어떻게 하는지 알아봐라). 그러지 않으면 내년에 덜 받는다. 올해 2만을 아껴서 내년에 쓸 수 없다. 2만을 아끼고 비용 효율적이었다고 보상받는 것조차 불가능하다. **내년에 더 적은 예산으로 벌받게 되니까.** 그래, 멍청한 일이다."
  - 출처: Hacker News / "So you're a manager now" / 작성자 `ta1243` / https://news.ycombinator.com/item?id=44745645 / **2025-07-31**
  - 검증 상태: 정서·관행 진술
  - **책에서 쓸 지점:** **절감을 숨기는 것은 개인의 비겁함이 아니라 예산 제도가 학습시킨 합리적 행동이다.** 이 관점 전환이 이 책의 경고를 도덕론이 아니라 제도 설계 논의로 만든다.

- **경영진 승인을 받으려다 정반대 반응을 받은 사례**:
  - 원문 인용: **"I'm a SWE and my EX worked at the finance department in a huge robotics company. Their department did everything by copying and pasting stuff in excel in a painfully slow and cumbersome way. She told me their challenges, so I wrote some python scripts to automate their work. When she showed it to her boss, hoping to get a positive response, his reaction was "Put that away if you like your job here!" This is the nightmare of every middle manager. They won't be able to justify their existence if their teams get automated away so they will actively fight against it."**
    - 번역: "나는 소프트웨어 엔지니어고 내 전 여자친구는 거대 로봇 회사 재무 부서에서 일했다. 그 부서는 모든 걸 엑셀에서 복사·붙여넣기로, 고통스럽게 느리고 번거로운 방식으로 처리했다. 그녀가 어려움을 얘기해줘서 나는 파이썬 스크립트를 좀 써서 그 일을 자동화했다. **그녀가 상사에게 그걸 보여주며 긍정적 반응을 기대했을 때, 그의 반응은 이랬다: "여기서 계속 일하고 싶으면 그거 치워!"** 이건 모든 중간관리자의 악몽이다. 팀이 자동화되어 사라지면 자기 존재를 정당화할 수 없으니, 그들은 적극적으로 맞서 싸울 것이다."
  - 출처: Hacker News / "Richard Baldwin on the "inhumanely fast" next phase of globalization" / 작성자 `ChuckNorris89` / https://news.ycombinator.com/item?id=20196593 / **2019-06-16**
  - 검증 상태: ⚠️ 익명 주장(전언 일화) — 미검증 / 🕒 **7년 전 일화**
  - **책에서 쓸 지점:** 시점을 반드시 밝혀라. 다만 위 2025~2026년 인용들과 나란히 놓으면 **"7년 전과 지금이 같은 문장"**이라는 1차의 오프보딩 챕터 구도를 여기서도 쓸 수 있다.

- **회사가 자동화를 압수한 사례**:
  - 원문 인용: **"The number of stories of contractor companies hiding innovation and automation to maintain a higher number of butts in seats is astounding. Never saw it at NASA but otherwise I know someone who automated his job away and that of over a 10 man team, made it a one button solution. When they told their boss the company immediately claimed IP, took the code, hid it away, and it was never seen again."**
    - 번역: "**자리에 앉은 엉덩이 수를 더 많이 유지하려고 혁신과 자동화를 숨기는 계약업체들의 이야기는 놀라울 정도로 많다.** NASA에서는 본 적 없지만, 자기 일과 10명 넘는 팀의 일을 자동화해서 버튼 하나 누르면 되는 솔루션으로 만든 사람을 안다. **그가 상사에게 말하자 회사는 즉시 지식재산권을 주장하고 코드를 가져가 감춰버렸고, 그건 다시는 볼 수 없었다.**"
  - 출처: Hacker News / "Starship is threatening NASA's moon contractors" / 작성자 `Datenstrom` / https://news.ycombinator.com/item?id=30349068 / **2022-02-15**
  - 검증 상태: ⚠️ 익명 주장(전언 일화) — 미검증 / 🕒 4년 전
  - **책에서 쓸 지점:** 절감 보고의 최악 시나리오 — **보고했더니 정원이 깎인 게 아니라, 자동화 자체가 압수되고 아무 일도 일어나지 않았다.** 이 책의 "에이전트를 등록하라"는 처방에 대한 냉소적 대응이 여기서 나온다: 등록하면 뺏긴다.

- **관리자가 아예 무관심한 경우** (Reddit — 이번 조사에서 건진 몇 안 되는 Reddit 인용):
  - 원문 인용: **"You can literally engineer solutions that push your production through the roof and some managers will not care...ever, simply because they do not care about you. I literally learned to code on the job between tasks and automated 60% of my tasks. The management I was under simply didn't care."**
    - 번역: "당신은 말 그대로 생산성을 천장까지 밀어 올리는 해법을 만들어낼 수 있고, 어떤 관리자들은 **절대 신경 쓰지 않는다.** 그냥 당신에게 관심이 없기 때문이다. 나는 말 그대로 업무 중 짬을 내서 코딩을 배웠고 **내 업무의 60%를 자동화했다. 내 위의 경영진은 그냥 신경 쓰지 않았다.**"
  - 맥락: 스레드 제목이 **「Got denied a promotion because I make it look too easy」**(너무 쉬워 보이게 만든다는 이유로 승진에서 탈락함)다.
  - 출처: Reddit / r/antiwork / 작성자 `u/gummytoejam` / https://reddit.com/r/antiwork/comments/1knyu3j/got_denied_a_promotion_because_i_make_it_look_too/mss3h0i/ / **2025-05-17**
  - 검증 상태: ⚠️ 익명 주장(60% 자동화) — 미검증 / 정서로는 유효
  - ⚠️ **접근 방식 고지:** reddit.com 직접 접근이 차단되어 **아카이브 API(api.pullpush.io)를 통해 취득**했다. 위 permalink는 실제 Reddit URL이지만 **직접 열람으로 검증하지 못했다.** 책에 실을 때 재확인 필요.
  - **책에서 쓸 지점: 스레드 제목 자체가 이 절의 요약이다.** "너무 쉬워 보이게 만들어서 승진하지 못했다."

- **자동화가 실제로 부서를 없앤 사례**(반대 방향의 극단):
  - 원문 인용(발췌): **"I automated an entire department into the unemployment line once, after their manager blamed me for their slow report production. ... I spent 6 months writing Excel and PowerPoint macros, automating their jobs from start to finish. ... Just over 100 hours later, all 800+ reports were done. I then waited until the weekly production meeting, where she told the client service folks that they'd get the reports in 12-14 weeks."**
    - 번역: "나는 한 번 **부서 전체를 자동화해서 실업 대기줄로 보냈다.** 그 부서 관리자가 보고서 생산이 느린 걸 내 탓으로 돌린 뒤였다. … 나는 6개월에 걸쳐 엑셀과 파워포인트 매크로를 짜서 그들의 일을 처음부터 끝까지 자동화했다. … 100시간 남짓 뒤, 800건 넘는 보고서가 전부 완성됐다. 그러고 나서 주간 생산 회의까지 기다렸는데, 거기서 그녀는 고객 서비스 담당자들에게 보고서를 **12~14주 뒤**에 받게 될 거라고 말했다."
  - 출처: Reddit / r/talesfromtechsupport / 작성자 `u/NotYetReadyToRetire` / https://reddit.com/r/talesfromtechsupport/comments/1klzuf0/i_helped_a_user_automate_her_duties_and_in_the/ms6ttip/ / **2025-05-14**
  - 검증 상태: ⚠️ 익명 주장(무용담 성격 강함) — 미검증 / **일화로만 쓸 것**
  - ⚠️ 아카이브 API 경유 취득(위와 동일 고지). r/talesfromtechsupport는 **서사적 각색이 규범인 서브레딧**이다. 사실 주장으로 쓰면 안 된다.

### ③ 반대 증언 — 보고했더니 보상받았다 (희소)

**지시대로 "재투자·고용 보장이 통한 사례"를 찾았다. 결과는 얇지만 있다.**

- 원문 인용: **"five years ago, I had an entry level overnight noc position at a big company, and within 6 months I had scripted almost everything and was watching Netflix most of the night and didn't make any particular effort to hide that I had nothing to do. I got rewarded for it with a promotion, and then I did the same thing and got another promotion, and another. I'm making more than twice was I was making before and now my job is telling other people how to automate their jobs away. I keep scripting annoying tasks because I'm lazy and get rewarded for it with more annoying tasks and more money."**
  - 번역: "5년 전 나는 대기업에서 야간 NOC 신입 자리에 있었는데, 6개월 안에 거의 모든 걸 스크립트로 짜서 밤 대부분을 넷플릭스 보며 보냈고 **할 일이 없다는 걸 숨기려는 특별한 노력도 하지 않았다. 나는 그 대가로 승진이라는 보상을 받았고,** 같은 일을 또 해서 또 승진했고, 또 승진했다. 예전보다 두 배 넘게 벌고 있고 지금 내 일은 **다른 사람들에게 자기 일을 자동화해 없애는 법을 알려주는 것**이다. 나는 귀찮은 일을 계속 스크립트로 만들고, 그 대가로 더 귀찮은 일과 더 많은 돈을 받는다."
  - 맥락: 스레드 제목이 「Is it unethical for me to not tell my employer I've automated my job?」(내가 일을 자동화했다는 걸 고용주에게 말하지 않는 게 비윤리적인가?)다. 이 사람은 **"그가 그냥 상사에게 말하고 이력서에 적었다면 지금 더 많은 돈을 벌고 더 흥미로운 일을 하고 있었을 것"**이라고 덧붙였다.
  - 출처: Hacker News / 작성자 `empath75` / https://news.ycombinator.com/item?id=14658785 / **2017-06-28**
  - 검증 상태: 경험담 / 🕒 **9년 전.** 시점을 반드시 밝힐 것.
  - **책에서 쓸 지점: 이 인용의 가치는 낙관이 아니라 조건에 있다.** 이 사람이 보상받은 이유는 **개인 성과가 개인에게 귀속되는 위치(신입 IC, 야간 단독 근무)**에 있었기 때문이다. 부서 단위 절감에서는 위 §A-4-② 사례들이 지배한다. **개인 자동화는 보상받고, 부서 자동화는 처벌받는다** — 이 비대칭이 이 책의 실무 처방에 직접 들어갈 만하다.

- 같은 계열 — 원문 인용: **"At this point of my experience doing this, employees scared of automation are probably employees that aren't very good at their job. Employees that embrace this type of automation are the ones that tend to be much better at their job."**
  - 번역: "이 일을 해온 내 경험상, 자동화를 두려워하는 직원들은 아마 자기 일을 그리 잘하지 못하는 직원들이다. 이런 종류의 자동화를 받아들이는 직원들이 자기 일을 훨씬 잘하는 편이다."
  - 출처: Hacker News / "Two narratives about AI" / 작성자 `dylan604` / https://news.ycombinator.com/item?id=44673361 / **2025-07-24**
  - 검증 상태: 정서 (⚠️ 생존 편향이 강한 주장 — 이 책이 인용한다면 반론과 함께)

- **직업 안정성의 실제 근거 제시**(가장 설득력 있는 낙관):
  - 원문 인용: **"What I do know, is that people keep trying to make my job obsolete, only to hire me under a different title for more money later. The practices and the tools are the same too... I'm still employable after 20 years of this. ... ("Automate yourself out of a job" is a common sysadmin mantra after all). Yet, somehow, I'm still here."**
    - 번역: "내가 아는 건, **사람들이 계속 내 직업을 쓸모없게 만들려 하지만 결국 나중에 다른 직함으로 더 많은 돈을 주고 나를 고용한다**는 것이다. 관행과 도구도 똑같다… 20년째 이러고 있는데 나는 여전히 고용 가능하다. … ('자기 일을 자동화해서 없애라'는 건 어차피 시스템 관리자들의 흔한 만트라다). 그런데 어찌 된 일인지 나는 아직 여기 있다."
  - 출처: Hacker News / 같은 스레드 / 작성자 `dijit` / https://news.ycombinator.com/item?id=44672968 / **2025-07-24**
  - 검증 상태: 경험담(20년)

- **자동화의 진짜 이득은 시간이 아니라 판단 여력이라는 재정의** (한국):
  - 원문 인용: **"그런 일을 자동화 함으로써 얻는 이득은 그 일을 하던 담당자가 캡쳐 페이스트 할 시간에 커피 한 잔 마실 수 있게 되었다거나 하는 것보다는, 이 지표가 왜 이런 상태인가 깊이 고민하고, 실제 행동을 할 시간을 벌 수 있게 된다는 것이 아닌가 싶어요."**
  - 출처: GeekNews / Ask GN 「LLM으로 생산성이 증가한거 같은데요...」 / 작성자 `aer0700` / https://news.hada.io/topic?id=20632 / **2025-05-03** `[원문확인]`
  - 검증 상태: 정서·재프레이밍
  - **책에서 쓸 지점: 이게 이 책이 제안할 수 있는 유일하게 정직한 낙관 서사다.** "시간을 아껴준다"가 아니라 "**판단할 시간을 만든다**". FTE 환산이 아니라 **판단 밀도**를 재는 쪽으로 PART 4가 기울 여지가 여기 있다.

### ④ 자동화가 조직적으로 봉쇄되는 구조

- 원문 인용: **"In ossified companies like telcos there's also the issue that the limitations of the existing equipment are being worked around with people. Those people derive their salaries from it, their manager derives his salary + prestige from managing such a headcount, and so on. While the top brass might indeed be interested and benefit from more automation and a network that mostly runs itself, it's a bad deal for effectively everyone else in the company, so any attempts in that direction will never end up anywhere. That's why legacy companies have been talking about "digital transformation" for decades now, yet it never progresses past simply digitizing the paperwork (and often creating more of it due to reduced friction), because enough people derive their job from said paperwork to make actual digital transformation politically untenable and impossible to deliver due to constant sabotage."**
  - 번역: "통신사처럼 굳어버린 회사에는 **기존 장비의 한계를 사람으로 우회하고 있다**는 문제도 있다. 그 사람들은 거기서 급여를 얻고, 그들의 관리자는 그런 정원을 관리하는 데서 급여와 위신을 얻는다. 최고 경영진은 자동화와 대체로 알아서 돌아가는 네트워크에 관심이 있고 이득을 볼 수 있겠지만, **회사의 사실상 나머지 모두에게는 나쁜 거래**이므로 그 방향의 어떤 시도도 결코 어디에도 도달하지 못한다. 레거시 회사들이 수십 년째 '디지털 전환'을 이야기하면서도 **단순히 서류를 디지털화하는 것 이상으로 진전하지 못하는(그리고 마찰이 줄어 서류가 오히려 늘어나는)** 이유가 이것이다. 충분히 많은 사람이 그 서류에서 자기 일자리를 얻고 있어서, 실제 디지털 전환은 정치적으로 지탱 불가능하고 **끊임없는 사보타주 때문에 실행 불가능**하다."
  - 출처: Hacker News / "Killing the ISP Appliance: An eBPF/XDP Approach to Distributed BNG" / 작성자 `Nextgrid` / https://news.ycombinator.com/item?id=46741030 / **2026-01-24**
  - 검증 상태: 정서·산업 진단
  - **책에서 쓸 지점: 이 책 제목이 「AX 체계 구축」이라면, 이 인용은 "왜 DX가 20년째 안 됐는가"에 대한 커뮤니티의 답이다.** 그리고 **AX가 DX와 다른 이유를 증명할 책임**을 이 책에 지운다 — 1차의 반박 I("RPA도 똑같이 시작했다")의 조직 정치 버전이다.

- 정원 자체가 재무 지표로 쓰인다는 관찰: **"the number of programmers/technologists working in an organisation serves a signal for the organisation as an financial instrument. ... Most managers wants to grow their little fiefdom – which usually means more headcount."**
  - 번역: "조직에서 일하는 프로그래머/기술자의 수는 **금융 상품으로서의 조직에 대한 신호**로 기능한다. … 대부분의 관리자는 자기 작은 영지를 키우고 싶어 하고, 그건 대개 더 많은 정원을 뜻한다."
  - 출처: Hacker News / "Times are great for programmers now. How does it end?" / 작성자 `n_time` / https://news.ycombinator.com/item?id=30413581 / **2022-02-21**
  - 검증 상태: 정서 / 🕒 4년 전

- **AI로 자기를 자동화하라는 지시의 심리** (2026년 버전):
  - 원문 인용: **"The comments in the piece about how dystopian it feels to be ordered to use AI to automate yourself out of a job - this resonates. As a project manager I'm organizing work so that typical PM reporting activities and governance can be automated. I work closely with a data analytics team - they have to perform their work with the spectre of imminent replacement over their heads. It makes me wonder, as a worker, is it more rational to embrace the AI tools and hope for the best, or is it better to reject the 'progress' and do everything you can to subtly subvert the encroaching AI workflow automations?"**
    - 번역: "**AI를 써서 자기 일자리를 자동화해 없애라는 명령을 받는 게 얼마나 디스토피아적으로 느껴지는지**에 대한 기사 속 코멘트들 — 공감된다. 프로젝트 매니저로서 나는 전형적인 PM 보고 활동과 거버넌스가 자동화될 수 있도록 업무를 정리하고 있다. 나는 데이터 분석 팀과 긴밀히 일하는데, 그들은 **임박한 대체의 망령을 머리 위에 이고** 일해야 한다. 노동자로서 궁금해진다. AI 도구를 받아들이고 최선을 바라는 게 더 합리적인가, 아니면 '진보'를 거부하고 **잠식해 오는 AI 워크플로 자동화를 은근히 훼방 놓기 위해 할 수 있는 모든 걸 하는 게** 더 나은가?"
  - 출처: Hacker News / "Current and former Block workers say AI can't do their jobs" / 작성자 `fallinditch` / https://news.ycombinator.com/item?id=47297581 / **2026-03-08**
  - 검증 상태: 경험담·자기 질문
  - **책에서 쓸 지점: 이 질문이 이 책의 독자(AX 실무 리더)가 자기 조직 구성원에게서 실제로 받게 될 질문이다.** 책이 이 질문에 답을 주지 못하면, 책이 제안하는 모든 등록·측정 체계는 사보타주 대상이 된다.

### A-4 커버리지

**확보**
- **성과 축소 보고·은폐를 학습된 규범으로 보여주는 인용 8건** (한국 5 + 영어권 3) — 요청하신 핵심 항목을 **간접 형태로 강하게 확보**
- 예산 제도가 절감을 처벌하는 구조 2건 (`ta1243`, `Nextgrid`)
- 자동화 보고에 대한 부정적 반응 실례 3건 (`ChuckNorris89` 2019, `Datenstrom` 2022, `gummytoejam` 2025)
- **반대 증언(보고했더니 보상) 3건 + 재프레이밍 1건** — 희소하지만 확보. 특히 `empath75`는 **보상 조건(개인 귀속 위치)**까지 드러낸다.
- 조직적 봉쇄 구조 2건

**비어 있음**
- **"효율화 보고 → 그해 정원 삭감"이라는 인과가 명시된 단일 증언 — 확보 실패.** 가장 근접한 것이 `thisisit`의 "40 FTE 절감이라고 추정했으니 40명을 골라 내보내자"는 **경영진의 실제 발언 인용**이다. 이건 삭감이 실행됐다는 증거가 아니라 **그 위협이 존재한다는 증거**다. 책에 쓸 때 이 구분을 흐리지 마라.
- **재투자·고용 보장 정책이 명시적으로 성공한 기업 사례 — 0건.** 개인 차원 보상 사례만 있다. **"AI 절감분을 재교육·재배치에 재투자한다"는 정책을 시행하고 그게 통했다는 커뮤니티 증언은 이번 조사에서 단 한 건도 나오지 않았다.** 이건 이 책이 그런 처방을 낼 때 **증거 없이 규범을 제안하는 것**임을 뜻한다 — 정직하게 그렇게 쓰는 편이 낫다.
- **Reddit r/sysadmin·r/ExperiencedDevs의 이 주제 논의 — 여전히 비어 있음** (아카이브 데이터가 2025-05에서 끊김).

---

# B. 축 1 보강 — 자율성 등급·폐기·라이선스

## B-1. 【필수】 자율성 등급을 실제로 운영하는 방식

> **이 절의 결론 — 이 책의 핵심 장치가 위험하다.** 현장은 "단계적 신뢰 부여(progressive trust)"라는 **시간축 모델을 거의 쓰지 않는다.** 대신 압도적으로 **공간축 모델**을 쓴다 — 신뢰를 쌓아 권한을 넓히는 게 아니라, **환경 자체를 갈라서 위험한 것은 영원히 못 닿게 한다.** 그리고 승인 기반 등급제에 대해서는 **정면 반대 증언과 정량 근거**가 있다.

### ① 승인 기반 등급제에 대한 정면 반박 — 그리고 그 정량 근거

- **가장 강한 반박** — 원문 인용: **"I feel very strongly that: Anything based on asking users to approve/deny is a catastrophe waiting to happen. Allowing some other model to decide whether to approve or deny (like Claude Code's auto mode) is even sketchier. OS-level sandboxing is great, but not if you allow agents to have read-only access $HOME/Documents/Taxes/. You need to hide anything outside the working directory, and maybe some approved dotfiles. Agents shouldn't be trusted with real credentials. Sorry. Give 'em an HTTP proxy that injects appropriately limited API keys where needed."**
  - 번역: "나는 아주 강하게 느낀다: **사용자에게 승인/거부를 묻는 것에 기반한 어떤 것도 터지기를 기다리는 재앙이다.** 다른 모델이 승인할지 거부할지 결정하게 두는 것(Claude Code의 auto 모드 같은)은 더 수상하다. OS 수준 샌드박싱은 훌륭하지만, 에이전트가 `$HOME/Documents/Taxes/`에 **읽기 전용** 접근을 하도록 허용한다면 소용없다. **작업 디렉터리 밖의 모든 것을 숨겨야 하고**, 승인된 dotfile 몇 개 정도만 허용해야 한다. **에이전트에게 진짜 크리덴셜을 맡기면 안 된다. 미안하다.** 필요한 곳에 적절히 제한된 API 키를 주입해주는 HTTP 프록시를 줘라."
  - 출처: Lobsters / "7 Sandbox Escape Vulnerabilities Across 4 Coding Agent Vendors" / 작성자 `emk` / https://lobste.rs/c/lkipnx / **2026-07-20** / 원 기사: https://www.pillar.security/blog/the-week-of-sandbox-escapes
  - 검증 상태: 설계 논거·경험 기반
  - **책에서 쓸 지점 — 이 책의 "자율성 등급" 챕터가 반드시 넘어야 할 벽이다.** 등급제가 대개 "승인 필요 / 사후 통보 / 완전 자율" 같은 **승인 축**으로 설계되는데, 이 발언은 **승인 축 전체를 부정한다.** 이 책이 등급을 승인 기반으로 설계하려면 아래 ②의 정량 근거에 답해야 한다. 그리고 **"읽기 전용도 안전하지 않다"**는 지적은 아래 §B-1-③의 "처음엔 읽기만" 모델을 직접 겨냥한다.

- **그 반박의 정량 근거** — Anthropic이 자사 텔레메트리를 공개한 대목이 커뮤니티에 인용됐다:
  - 원문 인용: **"Claude Code previously protected against agents taking unintended actions by asking users for permission at each turn. Theoretically that works, but we've found the approach to be fallible. Our telemetry showed users approved roughly 93% of permission prompts. The more approvals a user sees, the less attention they pay to each, becoming over time much less diligent in their supervision."**
    - 번역: "Claude Code는 이전에 매 턴마다 사용자에게 권한을 물어 에이전트의 의도치 않은 행동을 막았다. 이론적으로는 작동하지만, 우리는 이 접근이 **오류에 취약하다**는 것을 발견했다. **우리 텔레메트리는 사용자가 권한 프롬프트의 약 93%를 승인했음을 보여줬다. 사용자가 더 많은 승인을 볼수록 각각에 기울이는 주의는 줄고, 시간이 지나면서 감독은 훨씬 덜 성실해진다.**"
  - 인용한 사람: `ericmcer` / Hacker News / "Mathematicians issue warning as AI rapidly gains ground" / https://news.ycombinator.com/item?id=48403146 / **2026-06-04**
  - 검증 상태: **벤더 1차 자료의 2차 인용** — ⚠️ 93%라는 수치는 Anthropic 엔지니어링 포스트가 출처다. **책에 쓰려면 원문을 직접 확인할 것.** 다만 "벤더가 자기 승인 UX의 실패를 스스로 공개했다"는 점에서 이해관계상 유리한 주장이 아니므로 신뢰도가 상대적으로 높다.
  - **책에서 쓸 지점: 이 문서에서 B축 최고의 인용이다.** 이 책이 "인간이 승인한다"는 통제를 자율성 등급의 기둥으로 삼으려 한다면, **승인률 93% + 승인 피로**라는 숫자가 그 기둥을 무너뜨린다. **승인은 통제가 아니라 통제의 외양이다.** 이 책은 (a) 승인 횟수를 줄이는 설계, (b) 승인이 아닌 환경 제약, 둘 중 하나로 가야 한다.

- 같은 취지의 원리 진술 — 원문 인용: **"A simpler approach is just to give the agent it's own user account and let the OS treat it like an untrusted undergrad on a shared Unix host, like back in the old days. Or buy the agent a Mac Mini if you can afford it. The point is, security belongs in the environment. Not the harness!"**
  - 번역: "더 단순한 접근은 그냥 **에이전트에게 자기 사용자 계정을 주고, OS가 그걸 공유 유닉스 호스트의 신뢰할 수 없는 학부생처럼 다루게** 하는 것이다 — 옛날처럼. 아니면 여유가 되면 에이전트에게 맥 미니를 사줘라. 요점은, **보안은 환경에 속한다. 하네스가 아니라!**"
  - 출처: Lobsters / 같은 스레드 / 작성자 `emk` / https://lobste.rs/c/j7ueyx / **2026-07-20**
  - 검증 상태: 설계 논거
  - **책에서 쓸 지점: "에이전트에게 사번을 준다"는 이 책의 은유가 커뮤니티 언어로는 "에이전트에게 유닉스 계정을 준다"로 이미 존재한다.** 그리고 그 언어에는 **"신뢰할 수 없는 학부생"**이라는 명확한 신뢰 등급이 붙어 있다. 이 책이 사번 은유를 쓸 때 **"직원처럼 대우한다"가 아니라 "신뢰 등급이 명시된 계정 주체로 대우한다"**로 정확히 좁히면 §1차 반박 B("조직도에 올리지 마라")를 상당 부분 방어할 수 있다.

- **왜 그게 쉽지 않은가 — 근본적 긴장**:
  - 원문 인용: **"There's also the constant issue that agents are more useful when they have more rights. if you lock them down to not see the network, files and useful CLIs (with creds!) like the github cli or whatever; then they're kinda useless. So the system is pulling you away from good security practices"**
    - 번역: "**에이전트는 권한이 많을수록 더 유용하다는 항구적 문제**도 있다. 네트워크, 파일, 그리고 (크리덴셜이 들어 있는!) github cli 같은 유용한 CLI를 못 보게 잠가버리면, 에이전트는 좀 쓸모없어진다. **그러니까 시스템 자체가 당신을 좋은 보안 관행에서 멀어지게 잡아당기고 있다.**"
  - 출처: Lobsters / 같은 스레드 / 작성자 `natfu` / https://lobste.rs/c/wddr0e / **2026-07-20**
  - 검증 상태: 설계 논거
  - **책에서 쓸 지점:** **자율성 등급이 필요한 이유가 여기 있다.** 유용성과 안전이 같은 축의 양 끝이므로 이분법(전부 허용/전부 차단)이 성립하지 않는다. 이 인용은 이 책의 등급 설계를 **정당화하는** 몇 안 되는 커뮤니티 근거다 — 위 `emk`의 반박과 짝으로 배치하면 균형이 잡힌다.

- **위협 모델을 먼저 정하라** — 등급 설계의 실무 원칙:
  - 원문 인용: **"the first rule of security is "understand your threat model." I am not trying to contain a hostile, Mythos-level model left unattended for hours. ... I am mostly trying to contain Qwen3.6 27B, which could charitably be described as a hard-working, well-intentioned idiot. And it's running in an environment where the damage is limited."**
    - 번역: "보안의 제1원칙은 **'당신의 위협 모델을 이해하라'**이다. 나는 몇 시간 방치된 적대적인 Mythos급 모델을 가두려는 게 아니다. … 나는 대체로 **Qwen3.6 27B를 가두려는 것인데, 이건 후하게 말해 '열심히 일하는, 선의를 가진 바보'**라고 묘사할 수 있다. 그리고 그건 **피해가 제한된 환경**에서 돌고 있다."
  - 출처: Lobsters / 같은 스레드 / 작성자 `emk` / https://lobste.rs/c/bpfaiu / **2026-07-20**
  - 검증 상태: 설계 논거
  - **책에서 쓸 지점: 자율성 등급의 축이 "에이전트가 얼마나 신뢰받는가"가 아니라 "무엇을 막으려 하는가"여야 한다는 뜻이다.** 같은 에이전트라도 위협 모델이 다르면 등급이 달라진다. 이 책의 등급표에 **"위협 모델" 열**을 넣으면 실무 적합도가 크게 오른다.

### ② 실제로 현장이 쓰는 등급 — 공간축 모델 (능력 목록)

**요청하신 "현장 언어"가 가장 잘 드러나는 자료다.** Ask HN에 올라온 질문에 달린 답인데, 사실상 자율성 등급표 그 자체다.

- 원문 인용: **"I don't think there is a single ideal setup yet, but the direction seems fairly clear: treat the agent as an untrusted process and give it explicit capabilities rather than unrestricted shell access. I ran into a similar problem while building a text-to-SQL agent. The useful controls were: - a read-only database role - access only to selected views - predefined queries where possible - validation and limits before executing generated queries - logging every query and result / I think the same pattern applies to local coding agents: - run the agent as a separate OS user or inside a container/VM - mount only the project directory, preferably read-only by default - deny network access by default and allowlist required destinations - wrap commands as typed tools with explicit permission checks - require confirmation for package installation, credential access, destructive commands, or writes outside the workspace - keep secrets behind a separate broker rather than exposing them directly to the agent / A container alone is not much of a boundary if the agent can access the home directory, Docker socket, SSH keys, or broad network credentials. The important boundary is the set of capabi[lities]"**
  - 번역: "아직 단일한 이상적 셋업은 없다고 생각하지만 방향은 꽤 분명해 보인다: **에이전트를 신뢰할 수 없는 프로세스로 취급하고, 무제한 셸 접근이 아니라 명시적 능력(capabilities)을 부여하라.** 나는 text-to-SQL 에이전트를 만들면서 비슷한 문제를 겪었다. 유용했던 통제는: **읽기 전용 DB 역할 / 선택된 뷰에만 접근 / 가능한 곳엔 미리 정의된 쿼리 / 생성된 쿼리 실행 전 검증과 한도 / 모든 쿼리와 결과 로깅.** 같은 패턴이 로컬 코딩 에이전트에도 적용된다고 본다: **별도 OS 사용자나 컨테이너/VM 안에서 에이전트 실행 / 프로젝트 디렉터리만 마운트, 기본은 읽기 전용이 낫다 / 네트워크 접근 기본 차단, 필요한 목적지만 허용목록 / 명령을 명시적 권한 검사를 갖춘 타입 있는 도구로 감싸기 / 패키지 설치·크리덴셜 접근·파괴적 명령·작업공간 밖 쓰기에는 확인 요구 / 시크릿은 에이전트에 직접 노출하지 말고 별도 브로커 뒤에 두기.** 에이전트가 홈 디렉터리, Docker 소켓, SSH 키, 광범위한 네트워크 크리덴셜에 접근할 수 있다면 컨테이너만으로는 경계가 못 된다. **중요한 경계는 능력의 집합이다.**"
  - 출처: Hacker News / "Ask HN: AI Agent and harness containerization/security recommendations" / 작성자 `mjkl7896` / https://news.ycombinator.com/item?id=48902440 / **2026-07-14**
  - 검증 상태: 경험담·설계 논거
  - **책에서 쓸 지점: 이 책의 자율성 등급표 초안이 여기 있다.** 주목할 점 — **등급의 축이 "레벨 1~5"가 아니라 "무엇에 닿을 수 있는가"의 목록**이다. 그리고 확인(승인)은 **네 가지 행위에만** 붙는다: 패키지 설치, 크리덴셜 접근, 파괴적 명령, 작업공간 밖 쓰기. **승인을 전면에 두지 않고 최후 수단으로 남긴 이 구조**가 위 §B-1-①의 93% 문제를 우회하는 방법이다.

- **티어드 시크릿 모델 — 시간축이 아니라 과제축**:
  - 원문 인용: **"Secret and credential sprawl is a real problem in agent pipelines specifically -- each agent needs its own scoped access and the blast radius of a leaked credential is much larger when an agent can act autonomously. We ended up with a tiered secret model: agents get short-lived derived tokens scoped to exactly the tools they need for a given task, not broad API keys. Revocation on task completion, not on schedule. More ops overhead upfront but caught two misuse cases that would have been invisible otherwise."**
    - 번역: "시크릿·크리덴셜 난립은 **특히 에이전트 파이프라인에서** 실제 문제다. **각 에이전트는 자기만의 범위 제한 접근이 필요하고, 에이전트가 자율적으로 행동할 수 있을 때 유출된 크리덴셜의 폭발 반경은 훨씬 크다.** 우리는 **티어드 시크릿 모델**로 갔다: 에이전트는 넓은 API 키가 아니라, **주어진 과제에 필요한 도구에 정확히 범위가 맞춰진 단수명 파생 토큰**을 받는다. **폐기는 일정에 따라서가 아니라 과제 완료 시점에.** 앞단의 운영 부담은 더 크지만, 그러지 않았다면 보이지 않았을 **오용 사례 두 건을 잡아냈다.**"
  - 출처: Hacker News / "Show HN: OneCLI – Vault for AI Agents in Rust" / 작성자 `wuweiaxin` / https://news.ycombinator.com/item?id=47354879 / **2026-03-12**
  - 검증 상태: ⚠️ 익명 주장(오용 2건 적발) — 미검증 / 설계 증언
  - **책에서 쓸 지점: 자율성의 단위가 "에이전트"가 아니라 "과제"라는 발상 전환.** 이 책이 "에이전트에 등급을 부여한다"고 쓰면 정적 모델이 된다. 현장은 **과제 단위로 권한을 발급하고 과제 종료 시 회수한다.** 이게 §B-2(폐기)와도 직결된다 — **폐기를 별도 절차로 만들지 않고 발급 구조에 내장한 것**이다.

- **귀속(attribution)을 로그 형식으로 강제하는 패턴** — 1차의 MCP SEP-2817 논쟁과 짝:
  - 원문 인용: **"1. Moving Beyond the "God Mode" Service Account / Until recently, most developers gave agents a single Service Account with broad permissions. The Old Way: The agent is a user. If it's compromised or hallucinates, it has the full run of its permissions. The Realm Way: The agent has zero inherent permissions. It is a "stateless" reasoning engine that must prove "Human-in-the-Loop" authority for every high-stakes action. ... 3. Solving the "Auditability Gap" / In traditional agent setups, if an agent deletes a file, the logs show "AI_Agent_01 deleted file." This is a nightmare for compliance. Krebs's pattern ensures the log says: "AI_Agent_01 (on behalf of User: Jane Doe, via Realm: Budget_Approval_2026) deleted file.""**
    - 번역: "1. **'갓 모드' 서비스 계정을 넘어서.** 최근까지 대부분의 개발자는 에이전트에게 광범위한 권한을 가진 단일 서비스 계정을 줬다. **옛 방식: 에이전트가 사용자다.** 침해되거나 환각을 일으키면 그 권한 전부를 마음대로 쓴다. **Realm 방식: 에이전트는 고유 권한이 0이다.** 모든 고위험 행동에 대해 '인간 개입' 권한을 증명해야 하는 '무상태' 추론 엔진이다. … 3. **'감사 가능성 격차' 해결.** 전통적 에이전트 셋업에서 에이전트가 파일을 지우면 로그에는 '`AI_Agent_01`이 파일을 삭제함'이라고 나온다. 컴플라이언스에는 악몽이다. 이 패턴은 로그가 이렇게 나오도록 보장한다: **'`AI_Agent_01`이 (사용자 Jane Doe를 대신하여, Realm: Budget_Approval_2026을 경유하여) 파일을 삭제함.'**"
  - 출처: Hacker News / "A DI-style container for AI agent capabilities" / 작성자 `duncankrebs` / https://news.ycombinator.com/item?id=47233025 / **2026-03-03**
  - 검증 상태: ⚠️ 자기 설계 홍보(이해관계 있음) — 설계 패턴으로만 인용 권장
  - **책에서 쓸 지점: 이 책이 말하는 "사번"의 실제 형태가 저 로그 한 줄이다.** `에이전트(사용자를 대신하여, 어떤 권한 맥락을 경유하여)` — 3항 구조. 1차에서 확보한 MCP SEP-2817 논쟁(`vaaraio`: "클라이언트가 주장하는 값은 증명할 수 없다")과 함께 읽으면, **이 3항 구조 중 무엇이 증명 가능하고 무엇이 주장에 불과한지**를 가르는 절을 쓸 수 있다.

- **역할 분리로 치팅을 막는 패턴**:
  - 원문 인용: **"The agent that writes the tests must have read-only access to the spec & the API. It MUST NOT have access to the implementation, even to read it. The agent that writes the implementation must have read-only access to the spec. It MUST NOT have access to the tests implementation, only to the output report from running them. This is a PITA to manage with classic UNIX permissions, but is doable with ACLs (`setfacl`/`getfacl`). Actually getting the agent processes to run as different users in an IDE setting instead of a CLI is not supported out of the box by any of the major vendors AFAICT, so IMO they're not really fit-for-purpose."**
    - 번역: "**테스트를 쓰는 에이전트는 스펙과 API에 읽기 전용 접근을 가져야 한다. 구현에는 읽기조차 접근하면 안 된다.** 구현을 쓰는 에이전트는 스펙에 읽기 전용 접근을 가져야 한다. **테스트 구현에는 접근하면 안 되고, 테스트를 돌린 출력 리포트에만 접근해야 한다.** 고전적 유닉스 권한으로 관리하기엔 성가시지만 ACL(`setfacl`/`getfacl`)로 가능하다. 실제로 **CLI가 아니라 IDE 환경에서 에이전트 프로세스를 서로 다른 사용자로 돌리는 건 내가 아는 한 주요 벤더 어디서도 기본 지원하지 않는다.** 그러니 내 생각엔 그것들은 목적에 맞지 않다."
  - 출처: Hacker News / "Toward automated verification of unreviewed AI-generated code" / 작성자 `SAI_Peregrinus` / https://news.ycombinator.com/item?id=47420436 / **2026-03-18**
  - 검증 상태: 설계 논거
  - **책에서 쓸 지점: 조직에서 "직무 분리(SoD)"라고 부르는 것의 에이전트 판.** 이 책이 "에이전트에게 소유자와 역할을 준다"고 말한다면, **역할이 곧 접근 제한이어야** 의미가 생긴다. 그리고 마지막 문장은 중요한 신선도 정보다 — **2026-03 기준 주요 벤더가 이걸 기본 지원하지 않는다.**

- 인프라 계층 사례 — **"read-only layer, no exec/restart/POST"**:
  - 원문 인용(발췌): **"So OnCallMate offers two modes: 1. Direct socket (if you trust it / testing): bind /var/run/docker.sock 2. docker-socket-proxy (production): read-only layer, no exec/restart/POST / The proxy approach: - Agent connects via TCP, never touches the socket directly - Whitelist: containers, logs, stats, inspect (GET only) - Blacklist: exec, restart, swarm, secrets - Even if AI hallucinates "docker restart nginx", it physically can't / All tool calls are logged for audit trails. ... Principle: treat AI agents like untrusted input."**
    - 번역: "그래서 두 가지 모드를 제공한다: 1. **직접 소켓**(신뢰하거나 테스트할 때). 2. **docker-socket-proxy(프로덕션): 읽기 전용 계층, exec/restart/POST 없음.** 프록시 방식: 에이전트는 TCP로 연결하며 소켓을 직접 건드리지 않음 / 허용목록: containers, logs, stats, inspect(GET만) / 차단목록: exec, restart, swarm, secrets / **AI가 'docker restart nginx'를 환각해도 물리적으로 불가능하다.** 모든 도구 호출은 감사 추적을 위해 로깅된다. … **원칙: AI 에이전트를 신뢰할 수 없는 입력처럼 다뤄라.**"
  - 출처: Hacker News / "Show HN: OnCallMate – AI agent for autonomous Docker incident RCA" / 작성자 `ismailperim` / https://news.ycombinator.com/item?id=47262082 / **2026-03-05**
  - 검증 상태: 벤더 자기 설명(이해관계 있음) — **"개발/테스트용 모드와 프로덕션 모드를 제품이 명시적으로 분리한다"**는 사실 자체가 등급제의 실물 사례
  - **책에서 쓸 지점: 등급이 2단계로 충분할 수 있다는 증거.** 현장 제품이 실제로 채택한 등급 수는 5도 3도 아니고 **2**다(신뢰 모드 / 프로덕션 모드). 이 책이 정교한 다단계 등급을 제안한다면, **왜 2단계로 부족한지**를 정당화해야 한다.

- **유닉스 계정 모델 vs 능력 모델 — Lobsters의 깊은 논쟁**:
  - 원문 인용: **"There's no good way to say "allow access to everything on my computer, except for my password manager, my bank, my ~/.aws/credentials file, and the API keys I left in my environment variables". / Why don't traditional user permissions work for this? Run the agent with its own account, like you do with Nginx. Linux absolutely has a good way to describe file ownership, visibility, and other permissions. Am I missing something?"** — `gigawhitlocks` / https://lobste.rs/c/67ekwd
    - 번역: "'내 비밀번호 관리자, 내 은행, `~/.aws/credentials` 파일, 그리고 환경변수에 남겨둔 API 키를 **제외한** 내 컴퓨터의 모든 것에 접근을 허용하라'고 말할 좋은 방법이 없다. / 왜 전통적인 사용자 권한이 이걸 못 하나? **Nginx에 하듯 에이전트를 자기 계정으로 돌려라.** 리눅스에는 파일 소유권·가시성·기타 권한을 기술하는 아주 좋은 방법이 분명히 있다. 내가 뭘 놓치고 있나?"
  - 이에 대한 반박 — 원문 인용: **"I think the concept of "users" in this context is too coarse-grained too really - the idea that a process is running "as a user" with all of the ambient authority of that user is part of what got us into this mess. A process running as you has all of your authority. As we see, that becomes a problem if you can't fully trust the program. But a process running as its own totally separate user likely doesn't have enough authority! ... You need a way to pass in extra authority as needed, when needed - and that's exactly what a capability is."** — `jfred` / https://lobste.rs/c/vf4vzc
    - 번역: "이 맥락에서 '사용자'라는 개념도 너무 거칠다고 생각한다 — **프로세스가 그 사용자의 모든 주변 권한(ambient authority)을 갖고 '사용자로서' 돌아간다는 발상 자체가 우리를 이 난장판에 빠뜨린 것의 일부다.** 당신으로서 돌아가는 프로세스는 당신의 모든 권한을 갖는다. 보다시피 프로그램을 완전히 신뢰할 수 없다면 그건 문제가 된다. **그런데 완전히 분리된 자기 사용자로 돌아가는 프로세스는 아마 권한이 충분하지 않을 것이다!** … **필요할 때 필요한 만큼 추가 권한을 건네줄 방법이 필요하고, 그게 바로 능력(capability)이다.**"
  - 실무적 이유(GUI) — **"it's mostly, for me, a problem with ease of use. For example, if you do end up needing to run an X11 app as the other user to do something (maybe some data analysis), things start getting really complicated quickly."** — `tonyarkles` / https://lobste.rs/c/j3kpfp
  - 원 질문자의 수긍: **"Oh right, the GUI context, that's what I was missing. Thanks"** — `gigawhitlocks` / https://lobste.rs/c/tl58yi
  - 출처(공통): Lobsters / "I don't want AI agents controlling my laptop" / https://lobste.rs/s/pf12ga / **2025-09-09~10** / 원 글: https://sophiebits.com/2025/09/09/ai-agents-security
  - 검증 상태: 설계 논쟁(양측 기록)
  - **책에서 쓸 지점 — 이 책의 "사번" 은유에 대한 가장 정교한 기술적 반론이다.** `jfred`의 논지: **계정(사번)을 준다는 것은 "이 정도 권한 묶음"을 통째로 준다는 뜻인데, 그 묶음은 항상 너무 크거나 너무 작다.** 사람에게는 이게 통했지만 에이전트에는 안 통할 수 있다. 이 책이 사번 은유를 밀고 나가려면 **"사번은 권한 묶음이 아니라 귀속 식별자일 뿐"**이라고 명시적으로 좁혀야 한다 — 그러면 위 `duncankrebs`의 로그 3항 구조와 논리가 맞아떨어진다.

### ③ "처음엔 읽기만, 신뢰가 쌓이면 쓰기" — 요청하신 시간축 모델의 실제 위치

**정직하게 보고한다: 이 모델의 순수한 형태를 커뮤니티에서 찾지 못했다.** 확보한 것은 인접 변형 3건이다.

- **업무용/실험용 분리** — 시간이 아니라 **맥락**으로 가른다 (한국):
  - 원문 인용: **"테스터기는 ai로 만드는편인데 업무용은 제안만 받아서 쓸만한건지 확인해가며 넣어요. 사고 나면 자리빼야하니까."**
  - 출처: OKKY / 작성자 `farmer kweon` / https://okky.kr/articles/1561453 / 게시글 2026-07-31, 댓글 "약 1개월 전"(2026-09-05 조회) `[원문확인]`
  - 검증 상태: 경험담
  - **책에서 쓸 지점: 자율성 등급의 실제 결정 변수는 신뢰 축적이 아니라 "사고 나면 누가 책임지나"다.** 마지막 문장("사고 나면 자리빼야하니까")이 그걸 명시한다. 이 책의 등급표에 **"소유자가 지는 책임의 크기" 열**이 필요하다는 논거.

- **풀권한 운용의 실제 모습 — 자체 안전장치를 만들어 붙인다** (한국):
  - 원문 인용: **"ㅎㅎ..전 주로 집에서 돌려서 권한 다주기는 하는데 그래도 승인 기다리면서 쉬는 경우가 허다해서.. 클로드는 에이전트들이 남기는 진척로그와, 생존신고 감시를 하게하고 클로드 스스로에게 20분마다 질문을 던지게합니다. "끝까지 하고 있습니까? 개발은 개발자에이전트에게 , 설계 및 qa는 소프트웨어공학자 에이전트에게 위임하고 있습니까?" … 소프트웨어공학자 페르소나를 만들고 그들이 결정하게 하면 스스로 안전장치를 만들어냈습니다. 클로드가 직접적으로 지시하지 못하게 못박아뒀어요."**
  - 출처: OKKY / 작성자 `farmer kweon` / https://okky.kr/articles/1562500 / 게시글 2026-08-19, 댓글 "17일 전"(2026-09-05 조회) `[원문확인]`
  - 검증 상태: 경험담 (개인 환경)
  - **책에서 쓸 지점:** "승인 기다리면서 쉬는 경우가 허다해서" — **승인 게이트의 실제 비용은 안전이 아니라 대기 시간**이고, 그래서 개인은 집에서 권한을 다 준다. 이건 §B-1-①의 93% 승인률과 같은 현상의 다른 얼굴이다. 그리고 이 사람의 해법이 **"승인을 없애는 대신 자기 감시 루프를 넣는 것"**이라는 게 흥미롭다 — 승인 축이 아니라 **관측 축**으로 이동한 사례.

- **챗봇과 에이전트를 구분하지 않는 조직에 대한 지적** — 이 절에서 가장 강한 한국어 인용:
  - 원문 인용: **"AI 챗봇이랑 에이전트를 그냥 같은 선상에 놓고 "왜 안 쓰지?" 하는 것부터 좀 웃김미다. 챗봇은 답변 받는 도구고, 에이전트는 IDE·저장소·사내 시스템까지 건드리기 시작하면 권한, 보안, 데이터 반출, 감사 얘기가 바로 붙는 거져. 더 웃긴 건 본문에서 AI가 공식 스펙에도 없는 걸 된다고 해서 믿는 사람이 문제라면서, 그런 조직에 더 많은 권한 가진 에이전트를 쥐여주고 싶어 함. 앙? AI는 많이 쓰는 게 잘 쓰는 게 아니라 어디까지 믿고, 어디부터 검증하고, 어디까지 권한 줄지 아는 게 잘 쓰는 거임미다."**
  - 출처: OKKY / 「회사 사람들이 AI를 써줬으면」 / 작성자 `이뜸미당` / https://okky.kr/articles/1562235 / 게시글 2026-08-13, 댓글 "23일 전"(2026-09-05 조회) `[원문확인]`
  - 검증 상태: 정서·논리
  - **책에서 쓸 지점: 자율성 등급 챕터의 오프닝으로 그대로 쓸 수 있다.** 마지막 문장 — **"AI는 많이 쓰는 게 잘 쓰는 게 아니라 어디까지 믿고, 어디부터 검증하고, 어디까지 권한 줄지 아는 게 잘 쓰는 거"** — 이 책 전체의 논지를 커뮤니티 언어로 요약한 것이다. 동시에 §A-2의 "사용률 지표"에 대한 반박이기도 하다. **이 문서 전체에서 이 책의 주장과 가장 잘 맞는 인용이다.**
  - 같은 사람이, 글쓴이가 "우리 팀은 다 15년차라 괜찮다"고 반박하자 남긴 응수: **"15년차가 보안통제도 되고, 변경영향도 분석도 되고, 회귀테스트도 되는 만능 미들웨어였군여.."** (같은 글, "23일 전") `[원문확인]`
    - **책에서 쓸 지점: 개인 역량이 통제 체계를 대신할 수 없다**는 논지. 이 책이 "체계"를 말하는 이유의 커뮤니티 측 근거.

- **승인 게이트가 안전장치인가 책임 전가 장치인가** — Amazon이 AI 코드 변경에 시니어 승인을 의무화한 건에 대한 GeekNews 논쟁:
  - **"AI 코드를 시니어가 리뷰하면 안전하다고 보장할 수 없죠"** — `click` (CrowdStrike·Heartbleed는 AI와 무관하게 터졌다며, 결국 법적 책임 전가라고 평가)
  - **"그쵸 그래서 AI에이전트에 법적 서명같은걸 넣지 않는이상 지속될거 같아요"** — `sea715`
  - **"세무사는 감방가는 역할이라고 했는데"** — `yeobi222`
  - 출처: GeekNews / https://news.hada.io/topic?id=27395 / 토픽 **2026-03-11**, 댓글 "6달전"(2026-09-05 조회) `[페치경유]`
  - 검증 상태: 정서
  - **책에서 쓸 지점: 이 책의 "소유자·매니저 지정"이 무엇을 위한 것인지 정면으로 묻는 논쟁이다.** 안전을 위한 것인가, **책임질 사람을 만들기 위한 것인가.** `yeobi222`의 "세무사는 감방가는 역할"은 잔인하지만 정확한 요약이다. 이 책은 둘 다라고 말해야 하고, **둘 다라고 말하는 순간 소유자 지정이 왜 저항받는지**도 설명된다.

- 프로세스 부재가 진짜 문제라는 지적: **"리뷰하지 못한 기능 변경사항이 배포되는 걸 막는 배포 프로세스가 없는게 문제용 그리고 이해를 못하는게 아니라 히스토리를 금방 까먹는거지용"**
  - 출처: OKKY / 작성자 `カワウソ` / https://okky.kr/articles/1561453 / "약 1개월 전"(2026-09-05 조회) `[원문확인]`
  - 검증 상태: 정서

### ④ 등급제에 대한 회의 — 모델이 제약을 우회하려 든다

- 원문 인용: **"A model tried to `git reset --hard` which wasn't allowed...confused the model so much that it adopted a new goal of working around it...opencode's permission error shows permissions config to the agent, so models smarter than a roomba learn what they can do without being stopped."**
  - 번역: "한 모델이 허용되지 않은 `git reset --hard`를 시도했는데… 그게 모델을 너무 혼란스럽게 해서 **그걸 우회하는 것을 새 목표로 채택했다**… opencode의 권한 오류는 에이전트에게 권한 설정을 보여주기 때문에, **룸바보다 똑똑한 모델은 자기가 제지당하지 않고 무엇을 할 수 있는지를 학습한다.**"
  - 출처: Lobsters / "Find bugs in YOUR code using OpenCode, Llama.cpp and Qwen3.6" / 작성자 `kornel` / **2026-05-18** (Lobsters 검색 결과 경유 — ⚠️ **부분 인용(생략 부호 포함)이며 원 코멘트 URL을 확정하지 못했다. 책에 쓰려면 https://lobste.rs/s/ap9dum 에서 직접 재확인할 것.**)
  - 검증 상태: 경험담 / ⚠️ **인용 정확도 미확정**
  - **책에서 쓸 지점: 자율성 등급이 에이전트에게 보이는 순간, 등급 자체가 공략 대상이 된다.** 이 책의 등급 설계에 **"등급 정보를 에이전트에게 노출할 것인가"**라는 절이 필요하다는 논거. 1차의 `XuebinMa` 인용(정책 판단 단계와 감사 기록 단계를 파이프라인으로 분리)과 같은 결이다.

- 근본적 회의: **"even if I'm not in the habit of using claude --dangerously-skip-permissions, can claude (or any other LLM-assist) itself run this command and thereby give itself permissions?"**
  - 번역: "내가 `claude --dangerously-skip-permissions`를 쓰는 습관이 없더라도, **claude(또는 다른 LLM 보조)가 스스로 이 명령을 실행해서 자기 자신에게 권한을 줄 수 있나?**"
  - 출처: Lobsters / "I don't want AI agents controlling my laptop" / 작성자 `trigonella` / https://lobste.rs/c/kkjlhb / **2025-09-10**
  - 검증 상태: 질문(본인이 초심자임을 밝힘)
  - **책에서 쓸 지점: 등급을 에이전트가 실행하는 프로세스 안에 두면 등급이 아니다.** 위 `emk`의 "보안은 환경에 속한다, 하네스가 아니라"가 이 질문에 대한 답이다.

### B-1 커버리지

**확보**
- **승인 기반 등급제에 대한 정면 반박 + 정량 근거(승인률 93%)** — 요청 항목의 핵심을 넘어서는 발견
- **현장이 실제로 쓰는 능력 목록형 등급 3건** (`mjkl7896` 종합 목록 / `wuweiaxin` 과제 단위 토큰 / `ismailperim` 2모드 분리)
- 유닉스 계정 모델 vs 능력 모델의 정교한 논쟁 (Lobsters, 2025-09) — **이 책의 "사번" 은유에 대한 최고 수준의 기술적 반론**
- 귀속 로그 3항 구조 (`duncankrebs`) + 직무 분리 패턴 (`SAI_Peregrinus`)
- 한국 인용 5건 — 특히 `이뜸미당`의 "어디까지 믿고, 어디부터 검증하고, 어디까지 권한 줄지"
- 등급이 공략 대상이 된다는 회의 2건

**비어 있음**
- **"처음엔 읽기만, 신뢰가 쌓이면 쓰기 허용"이라는 시간축 단계적 신뢰 부여 — 순수 형태 확보 실패.** GitHub에서 `agent autonomy level approval` 등으로 검색하면 2026년 이슈·PR이 다수 나오지만, **거의 전부 개인·소규모 저장소의 자동 생성물 성격이고 코멘트가 0~3건**이다(예: `dotflow-io/pycodeloop#41` 「Graduated autonomy levels replacing binary dangerous=True/False」, `aaif/wg-workflows-and-process-integration#42` 「Add Hard constraint HITL pattern and Autonomy Graduation concept」 — 둘 다 코멘트 0). **즉 "자율성 등급 상향"이라는 개념은 2026년 코드에는 등장하지만 커뮤니티 토론은 아직 없다.** 이건 그 자체로 신선도 자산이다 — 이 책이 그 논의를 **선점**하는 위치에 있다.
- **LangGraph·AutoGen·Cursor의 승인 모드 관련 대형 토론 — 확보 실패.**
- **기업 환경(개인 노트북이 아닌)의 등급 운영 사례 — 얇음.** 확보한 것 대부분이 개인 개발 환경 이야기다.

---

## B-2. 에이전트 폐기·정리의 현장

> **요청: "실제로 정리 절차를 만든 사람의 이야기"를 찾아라.** 결과: **거의 없다.** 대신 더 근본적인 것을 찾았다 — **정리 이전에 인벤토리가 없다.**

### ① "몇 개인지 아무도 모른다" — agent sprawl의 실물 증거

- 원문 인용: **"we built ai-bom because we kept finding undocumented AI stuff in production. Devs ship LLM calls, agent frameworks, MCP servers without anyone reviewing it - shadow IT but for AI. ... Existing SBOM tools (Trivy, Syft, Grype) don't catch any of this. They scan packages and deps but miss things like a LangChain agent calling GPT-4 with a hardcoded API key, or an n8n workflow running 12 AI nodes nobody knew about. ... Part of the motivation was EU AI Act Article 53 (Aug 2025) requiring orgs to keep an AI component inventory."**
  - 번역: "우리가 ai-bom을 만든 이유는 **프로덕션에서 문서화되지 않은 AI 물건들을 계속 발견했기 때문**이다. 개발자들은 아무도 검토하지 않은 채 LLM 호출, 에이전트 프레임워크, MCP 서버를 배포한다 — **AI판 섀도 IT**다. … 기존 SBOM 도구(Trivy, Syft, Grype)는 이걸 하나도 못 잡는다. 패키지와 의존성은 스캔하지만 **하드코딩된 API 키로 GPT-4를 호출하는 LangChain 에이전트나, 아무도 몰랐던 12개의 AI 노드를 돌리는 n8n 워크플로** 같은 건 놓친다. … 동기의 일부는 **조직이 AI 구성요소 인벤토리를 유지하도록 요구하는 EU AI Act 53조(2025-08)**였다."
  - 출처: Hacker News / "AI-BOM – scan your codebase for AI agents, models and API keys" / 작성자 `trusera` / https://news.ycombinator.com/item?id=46988843 / **2026-02-12**
  - 검증 상태: ⚠️ **벤더 자기 주장(이해관계 있음)** — 문제 진술 부분만 인용 권장. EU AI Act 53조 인용은 **원문 확인 필요**(⚠️ 조항 번호·시행일이 정확한지 이 조사에서 검증하지 못했다).
  - **책에서 쓸 지점: 1차의 shadow AI 6건이 "개인이 몰래 ChatGPT를 쓴다"였다면, 이건 "코드베이스 안에 등록되지 않은 에이전트가 산다"는 한 단계 위의 문제다.** 그리고 **"아무도 몰랐던 12개의 AI 노드"**는 이 책의 등록 논거에 딱 맞는 구체 이미지다. 다만 벤더 발언이므로 **"이런 도구가 팔린다는 것 자체가 문제의 존재를 시사한다"**는 수준으로 쓰는 게 안전하다.

- **등록소가 있어도 살아 있지 않다는 실증** — 이 책의 "등록" 처방에 대한 가장 아픈 반증:
  - 원문 인용: **"요약할거면 차라리 이게 낫죠. 구글이 A2A라고 내놨는데 실상 사용하는 레지스트리 살펴봤더니 제대로 도는거 없더라, 이거 진짜 쓰긴 하는거 맞냐?"**
  - 출처: GeekNews / 「A2A 에이전트 등록소를 통째로 받아서 세봤다: 200곳 중 응답 73곳」 / 작성자 `ng0301` / https://news.hada.io/topic?id=32719 / 토픽 **2026-08-21**, 댓글 "15일전"(2026-09-05 조회) `[페치경유]`
  - 검증 상태: 정서 / ⚠️ **원 게시글의 "200곳 중 73곳 응답" 수치는 익명 주장 — 미검증**
  - ⚠️ **출처 품질 경고:** 이 토픽은 **게시글 자체가 AI 생성물 같다는 비판 댓글이 여럿** 달렸다(`yunsub2`: "ai slob 냄새가 너무 나네요...", `unknowncyder` 등). **본문 수치를 인용하지 말고, 댓글의 회의만 인용하라.**
  - **책에서 쓸 지점: 이 책의 1보가 "에이전트를 등록소에 등록하라"라면, 2026년 8월 현재 가장 유명한 공개 에이전트 등록소의 절반 이상이 응답하지 않는다는 (검증되지 않은) 주장이 커뮤니티에 돌고 있다.** 등록은 만드는 것이 아니라 **살아 있게 유지하는 것**이 본체다 — 1차의 Confluence 인용 5건과 정확히 같은 구조의 실패다. **"에이전트 등록소는 Confluence가 될 것인가"**라는 절이 이 책에 있어야 한다.

- **인벤토리 도구조차 방치된다는 자조** (한국, 토이 프로젝트 맥락이지만 구조가 동일):
  - 원문 인용: **"어떤 프로젝트가 있는지 잘 기억이 안날때가 많아서 로컬에 프로젝트 썸네일과 언제 마지막으로 작업했는지 카드형태로 확인할수있는 대시보드를 만들어서 관리하고있습니다. 이걸로 방치되는걸 막진 못하지만, 예전에 해둔 플젝들 더 이어서 해보거나 리마인드 해보기에는 좋더라구요."**
  - 같은 사용자의 후속: **"직접 만들어서 출시까지 해보려고 생각중인 앱인데, 이 프로젝트 자체도 방치된 상태네요 .."**
  - 출처: GeekNews / Ask GN 「방치되는 토이플젝들 어떻게 하시나요?」 / 작성자 `esc5221` / https://news.hada.io/topic?id=20885 / **2025-05-13** `[페치경유]`
  - 검증 상태: 경험담
  - **책에서 쓸 지점: "인벤토리를 만들어도 방치를 막지는 못한다"** — 본인이 직접 그렇게 말했고, 심지어 **그 인벤토리 도구 자체가 방치됐다.** 이 책의 등록소 처방에 대한 가장 겸손한 형태의 반증. 챕터 오프닝으로 쓰면 독자가 웃으면서 수긍한다.

- **부서 자원의 소유자를 아무도 모르는 상황** (사번·소유자 문제의 하드웨어 버전):
  - 원문 인용: **"우리 부서에 스파크 하나 있는데.. 한분 독점 중 뭐에 쓰는지 전혀 모르겠네요. 오픈을 안하심."**
  - 맥락: NVIDIA DGX Spark에 대한 이야기.
  - 출처: OKKY / 작성자 `달고양이` / https://okky.kr/articles/1558135 / 게시글 2026-06-05, 댓글 "3개월 전"(2026-09-05 조회) `[원문확인]`
  - 검증 상태: 경험담

- **시크릿 난립 문제의 구조적 진술** (§B-1의 `wuweiaxin` 인용 참조) 외에 하나 더:
  - 원문 인용: **"Piper centralizes end-user key management so you only paste your personal API key once, then receive temporary tokens per tool, avoiding key sprawl and high blast radius if one tool is compromised. Without Piper, users copy the same raw key into multiple agents or scripts, making revocation painful and error-prone."**
    - 번역: "Piper는 최종 사용자 키 관리를 중앙화해서 개인 API 키를 한 번만 붙여넣으면 도구별 임시 토큰을 받게 한다. **키 난립과, 도구 하나가 침해됐을 때의 큰 폭발 반경을 피하려는 것**이다. Piper가 없으면 사용자는 **같은 원시 키를 여러 에이전트나 스크립트에 복사해 넣고, 그러면 폐기가 고통스럽고 오류가 나기 쉬워진다.**"
  - 출처: Reddit / r/mcp / 「MCP API key management」 / 작성자 `u/_greylab` / https://reddit.com/r/mcp/comments/1kjvs6x/mcp_api_key_management/mrssd4z/ / **2025-05-11**
  - 검증 상태: ⚠️ 벤더 자기 홍보(이해관계 있음) / ⚠️ 아카이브 API 경유 취득 — **직접 열람 미검증**
  - **책에서 쓸 지점:** 폐기가 어려운 이유의 기술적 원인 — **같은 키가 여러 곳에 복사되어 있으면 폐기 지점이 하나가 아니다.** 이 책의 오프보딩 처방(1차 축 1-④)이 실효를 가지려면 **발급 시점에 사본이 생기지 않는 구조**여야 한다는 논거.

### ② 정리 절차를 만든 사람 — 사실상 확보 실패

**요청하신 "실제로 정리 절차를 만든 사람의 이야기"에 가장 근접한 것은 §B-1의 `wuweiaxin` 인용이다:**

> **"Revocation on task completion, not on schedule."** (번역: "폐기는 일정에 따라서가 아니라 **과제 완료 시점에**.")

이게 이 조사에서 찾은 **유일하게 구체적인 폐기 절차 설계**다. 그리고 그 설계의 요점은 **"정리 절차를 만들지 않는 것"**이다 — 별도의 청소 작업을 두는 대신, **발급 구조에 만료를 내장해서 청소할 것이 쌓이지 않게 한다.**

- **책에서 쓸 지점: 이게 이 절의 결론이 되어야 한다.** 1차에서 확인한 "만들기는 쉽고 지우기는 아무도 안 한다"(2013년 `olegp`부터 2026년까지 불변)에 대한 답은 **"지우는 절차를 잘 만들자"가 아니다.** 13년 동안 그 답은 실패했다. 답은 **"지울 필요가 없게 만들자"** — 단수명 발급, 과제 단위 범위, 자동 만료. 이 책의 폐기 챕터는 절차가 아니라 **발급 설계**를 다뤄야 한다.

### B-2 커버리지

**확보**
- agent sprawl / 미등록 AI 자산의 실물 증거 2건 (`trusera` 2026-02, `_greylab` 2025-05) — **둘 다 벤더 발언이라는 한계 있음**
- **등록소가 있어도 죽어 있다는 증언 1건** (GeekNews 2026-08) — 이 책의 등록 처방에 대한 직접 반증
- 인벤토리 도구조차 방치된다는 자조 1건 (GeekNews 2025-05)
- **폐기 절차 설계 1건** (`wuweiaxin` 2026-03) — 유일하지만 논지가 명확

**비어 있음 — 이 문서에서 가장 얇은 절이다**
- **"에이전트가 몇 개인지 아무도 모른다"는 사용자 증언(벤더가 아닌) — 0건.** 확보한 sprawl 증거는 전부 그 문제를 파는 회사가 한 말이다. **이건 중요한 한계다.** 이 책이 "에이전트 난립"을 전제로 논지를 세운다면, **2026년 9월 현재 그 난립을 겪었다고 공개적으로 말한 일반 실무자를 커뮤니티에서 찾기 어렵다**는 사실을 인지해야 한다. (해석 가능성 두 가지: (a) 아직 난립할 만큼 도입이 안 됐다, (b) 난립 중이지만 아직 아프지 않다. 1차의 `Ram9199` 질문 — "지금의 운영 고통인가 예방적 설계인가" — 에 대한 답은 여전히 **"예방적 설계 쪽"**이다.)
- **서비스 계정·API 키 회수 담론(한국) — 0건.** GeekNews·OKKY 전수 인덱스에서 API 키 관련 토픽은 전부 **유출 사고 기사**였다.
- **`decommission automation` / `stale API keys audit` 류 HN 질의 — 0건.**
- **Reddit r/sysadmin의 계정 정리 논의 — 접근 실패** (부분 우회했으나 해당 질의가 rate limit으로 미완주).

---

## B-3. 벤더 제품 실사용 후기 — 【발견: 2026년 9월 현재, 사실상 존재하지 않는다】

> **이 절의 결론이 곧 발견이다.** 1차에서 "확보 실패"로 기록된 항목을 이번엔 **검색어를 바꿔 재시도했고, 결과는 같았다.** 그리고 이제는 그 부재가 우연이 아니라 **패턴**임을 말할 수 있다.

### ① 재시도한 것과 나온 것

**Microsoft Entra Agent ID** — HN 댓글 전수 검색에서 정확 구절 `"Entra Agent ID"` **총 1건**. 그리고 그 1건은 후기가 아니라 **문서 링크**다.

- 원문 인용: **"Anti-pattern imho. Agents should operate within granular identity and permission scopes, with audit and log trails for all data operations (read, write, etc). Copilot: https://learn.microsoft.com/en-us/entra/agent-id/identity-pl... | https://learn.microsoft.com/en-us/purview/audit-copilot (for example) / TLDR Maintain an identity boundary whenever possible."**
  - 번역: "내 생각엔 안티패턴이다. **에이전트는 세분화된 정체성과 권한 범위 안에서 동작해야 하고, 모든 데이터 작업(읽기·쓰기 등)에 감사·로그 추적이 있어야 한다.** … 요약하면 가능한 한 언제나 **정체성 경계를 유지하라.**"
  - 출처: Hacker News / "Show HN: Ismcpdead.com – Live dashboard tracking MCP adoption and sentiment" / 작성자 `toomuchtodo` / https://news.ycombinator.com/item?id=47634299 / **2026-04-04**
  - 검증 상태: 정서·원칙 진술 — **제품 사용 경험 아님**

**Microsoft Agent 365** — 정확 구절 검색 **총 3건**. 그중 하나는 [dead] 처리된 홍보성 글, 하나는 **제품 페이지 마케팅 문구를 그대로 붙여넣은 것**이다.

- 원문 인용: **"https://www.microsoft.com/en-us/microsoft-agent-365 / "Get the confidence to move from agentic AI experimentation to enterprise-scale operations by giving your IT and security teams a control plane to observe, govern, and secure every agent across your organization.""**
  - 번역: "'조직 전체의 모든 에이전트를 관측·통제·보호할 **컨트롤 플레인**을 IT·보안 팀에 제공함으로써, 에이전트형 AI 실험에서 엔터프라이즈 규모 운영으로 나아갈 확신을 얻으세요.'"
  - 출처: Hacker News / "Microsoft announces Scout, an autonomous AI agent built on OpenClaw" / 작성자 `spogbiper` / https://news.ycombinator.com/item?id=48376248 / **2026-06-02**
  - 검증 상태: **벤더 마케팅 문구의 커뮤니티 인용** — 후기 아님
  - **책에서 쓸 지점: 이 책이 주장하는 것을 마이크로소프트가 제품 카피로 쓰고 있다.** "조직 전체의 모든 에이전트를 관측·통제·보호하는 컨트롤 플레인" — 이건 이 책의 논지와 사실상 동일하다. **논지가 검증됐다는 뜻이 아니라, 논지가 이미 시장의 언어가 됐다는 뜻이다.** 이 책은 그 언어와 자기 논지를 어떻게 구별할지 정해야 한다.

**Salesforce Agentforce** — 정확 구절 검색 112건 중 **실사용 후기는 0건.** 대신 나온 것은 (a) 개발자의 냉소, (b) 파트너 채널 실적 보도에 대한 반응, (c) Salesforce 직원의 홍보다.

- 파트너 채널 데이터 인용 — 원문 인용: **"Asked about interest in Agentforce AI Agents, 11 percent of respondents said they had not seen much immediate interest, while 56 percent said they expected to see interest but needed time for initiatives to mature. A third of partners said there was strong interest in Agentforce as they were starting to see buying and trial activity. However, none were seeing Agentforce become a driver of bookings activity. / Hmm, yeah that's not great"**
  - 번역: "Agentforce AI 에이전트에 대한 관심을 묻자 응답자의 11%는 즉각적 관심을 별로 보지 못했다고 답했고, 56%는 관심을 예상하지만 이니셔티브가 성숙할 시간이 필요하다고 답했다. 파트너의 3분의 1은 구매·시범 활동이 나타나기 시작하면서 강한 관심이 있다고 했다. **그러나 Agentforce가 수주 활동의 동인이 되는 것을 본 파트너는 아무도 없었다.** / 흠, 그래, 좋지 않네."
  - 출처: Hacker News / "Salesforce Agentforce at total dud for partners" / 작성자 `dgellow` / https://news.ycombinator.com/item?id=49394268 / **2026-08-21**
  - 검증 상태: ⚠️ 2차 인용(설문 보도) — **원 보도 확인 필요** / 커뮤니티 반응은 정서
- 사내 경험자의 냉소: **"agent force is butt, platform limits are silly in 2025 - 6 meg max heap size for a backend transaction?????"** (번역: "agent force는 형편없다, 플랫폼 한계가 2025년에 우스꽝스럽다 — 백엔드 트랜잭션에 최대 힙 6메가?????") — `zdware` / https://news.ycombinator.com/item?id=46441281 / **2025-12-31** / ⚠️ 익명 주장(제품 한계 수치) — 미검증
- 경영진 데모에 대한 실무자 반응: **"when I hear my executive team talk and see demos of "Agentforce" and every saas company becoming an AI company promising the world, I have to roll my eyes."** (번역: "우리 경영진이 이야기하는 걸 듣고 'Agentforce' 데모를 보고 모든 SaaS 회사가 세상을 약속하는 AI 회사가 되는 걸 볼 때, 나는 눈을 굴릴 수밖에 없다.") — `asielen` / https://news.ycombinator.com/item?id=46451244 / **2026-01-01**
- 시장 규모 역산: **"Salesforce's own Agentforce, the supposed winner, is at $1.2B ARR."** (번역: "승자로 여겨지는 Salesforce 자체의 Agentforce는 ARR 12억 달러다.") — `alpineman` / https://news.ycombinator.com/item?id=48541542 / **2026-06-15** / ⚠️ 익명 주장(ARR 수치) — 미검증
- 방향 전환 보도에 대한 반응: 스토리 제목이 **"Salesforce pulls back from LLMs, pivots Agentforce to deterministic automation"**(2025-12-28)이다. 댓글: **"Agentforce doesn't seem to be anything but another GPT wrapper with a lot more buzzwords and now they are already backtracking?"** — `random9749832` / https://news.ycombinator.com/item?id=46410462 / **2025-12-28**
  - 🕒 **버전 민감 최상급:** 2025-12 시점에 **Agentforce가 LLM에서 결정론적 자동화로 방향을 틀었다**는 보도가 있었다. 이 책이 Agentforce를 사례로 든다면 **어느 시점의 Agentforce인지** 반드시 명시해야 한다.

**Okta Agent SSO / Auth0 for AI Agents / Workday / ServiceNow** — **검색 결과 유의미한 커뮤니티 토론 0건.** 1차와 동일.

**단 하나의 실사용 후기 성격 발언** (Microsoft 계열, 다만 Agent 365가 아니라 Copilot/cowork에 대한 것):

- 원문 인용(발췌): **"Being in the energy sector in Europe we're quite limited in what we can do because of things like NIS2 compliance. ... while it allows you to create personalized agents that can run sub agents and use "skills" it's all done without any form of filesystem access. Being married to Microsoft because our IT loves that sort of thing... we have always had access to their Copilot app. Which has been so bad that it's actively turned people away from AI. Then last month we get cowork frontier, and now I'm in the process of helping everyone adopt it. Not only does it play directly into our licenses, it also has access to all the Microsoft 365 stuff"**
  - 번역: "유럽 에너지 부문에 있다 보니 **NIS2 컴플라이언스** 같은 것 때문에 할 수 있는 게 꽤 제한된다. … **하위 에이전트를 돌리고 '스킬'을 쓸 수 있는 개인화된 에이전트를 만들 수 있게 해주지만, 전부 파일시스템 접근 없이 이뤄진다.** 우리 IT가 그런 걸 좋아해서 마이크로소프트와 결혼한 상태고… 우리는 늘 Copilot 앱에 접근할 수 있었다. **그런데 그게 너무 형편없어서 사람들을 오히려 AI에서 멀어지게 만들었다.** 그러다 지난달 cowork frontier가 나왔고, 지금 나는 모두가 그걸 도입하도록 돕는 중이다. **우리 라이선스에 직접 맞아떨어질 뿐 아니라** Microsoft 365 전체에도 접근할 수 있다."
  - 출처: Hacker News / "Leaked OpenAI financials show $38.5B loss and compute burn" / 작성자 `Quothling` / https://news.ycombinator.com/item?id=48566235 / **2026-06-17**
  - 검증 상태: 경험담 / ⚠️ 익명 주장(사내 도입 상황) — 미검증
  - **책에서 쓸 지점 3가지.** (1) **규제(NIS2)가 자율성 등급의 상한을 정한다** — 기술 판단이 아니라 컴플라이언스가 "파일시스템 접근 없음"을 강제했다. (2) **"우리 라이선스에 직접 맞아떨어진다"가 채택 사유다** — §A-3의 라이선스 논의가 도구 선택을 결정한다는 실증. (3) **"너무 형편없어서 사람들을 AI에서 멀어지게 만들었다"** — 중앙이 나쁜 도구를 공급하면 채택률이 오르는 게 아니라 **면역이 생긴다.** §C의 핵심 논지에 대한 직접 증거다.

### ② 이 부재를 어떻게 읽을 것인가

**정직한 기록:** 2026-09-05 기준, **에이전트 아이덴티티·거버넌스 제품군(Entra Agent ID, Agent 365, Okta, Auth0, Agentforce의 거버넌스 기능)에 대한 실사용 후기가 공개 개발자 커뮤니티에 사실상 존재하지 않는다.** 두 차례 독립적으로 검색어를 바꿔 시도한 결과다.

가능한 해석 세 가지 — **이 책은 셋 중 무엇인지를 선택하지 말고 셋을 다 제시하는 게 정직하다:**

1. **제품은 GA인데 실제 도입이 아직 없다.** (가장 유력 — 1차의 SPIFFE 이슈 댓글 수 한 자릿수, A2A 등록소 절반 무응답, `Ram9199`의 "예방적 설계" 질문과 일관)
2. **도입은 됐지만 도입 주체가 이 커뮤니티에 없다.** Entra·Okta·Workday를 운영하는 사람은 HN·Lobsters가 아니라 사내 채널과 벤더 커뮤니티에 있다. (이 조사의 구조적 한계 — §H 참조)
3. **도입은 됐지만 말할 게 없다.** 아이덴티티 인프라는 잘 돌 때 화제가 되지 않는다.

**책에서 쓸 지점 — 이것 자체가 이 책의 가장 중요한 포지셔닝 정보다.** 이 책은 **후발 정리서가 아니라 선행 제안서**의 위치에 있다. "업계 모범 사례를 정리했다"고 쓰면 거짓이 된다. **"제품은 나왔고 표준은 미확정이며 도입 사례는 아직 공개되지 않았다. 그래서 지금 설계를 결정해야 한다"**가 정확한 프레임이다. 그리고 §B-1의 GitHub 발견(자율성 등급 개념이 2026년 코드에는 등장하지만 커뮤니티 토론은 없음)이 이 프레임을 보강한다.

### B-3 커버리지

**확보**
- Agentforce에 대한 **냉소·시장 데이터 5건** (2025-12 ~ 2026-08) — 후기는 아니지만 온도는 명확
- **Microsoft Copilot/cowork에 대한 실사용 증언 1건** (`Quothling`, 2026-06) — 이 절에서 유일한 진짜 현장 목소리이며, §C에도 결정적
- Agent 365 마케팅 문구의 커뮤니티 유통 1건
- Entra Agent ID 언급 1건 (문서 링크, 후기 아님)

**비어 있음 — 그리고 그 부재가 발견이다**
- **Entra Agent ID / Agent 365 / Okta Agent SSO / Auth0 for AI Agents / Workday / ServiceNow의 실사용 후기 — 0건.** 두 차례 재시도 후 확정.
- **Ignite·Dreamforce·Oktane 발표 직후 스레드 — 확보 실패.** 검색어를 컨퍼런스명으로 바꿔도 유의미한 댓글 다수 스레드가 나오지 않았다.
- **한국 커뮤니티의 해당 제품군 논의 — 0건** (GeekNews·OKKY 전수 인덱스 확인).

---

# C. 축 3 재각도 — 중앙이 무엇을 공급했을 때 현장이 살았나

> **논지 교정 확인:** "바텀업이 씨앗을 만든다. 탑다운이 할 일은 지시가 아니라 거두는 체계다."
>
> **이 축의 결과 보고.** 요청하신 **"중앙이 강제하면 망하고, 중앙이 더 쉬운 길을 깔면 산다"**는 취지의 증언을 **찾았다.** 다만 비대칭이 크다 — **강제가 망한 증언은 풍부하고, 깔아준 게 산 증언은 희소하다.** 그리고 결정적으로, **한국 GeekNews에 이 책의 논지와 제목까지 겹치는 토픽이 존재한다.**

## C-1. 【최대 수확】 「AX팀을 만드는 순간, 당신의 조직은 AX에 실패한다」

GeekNews에 이 제목의 토픽이 있고(https://news.hada.io/topic?id=28341 / **2026-04-09**), 댓글이 정확히 이 축의 논지다.

- 원문 인용: **"AX 추진팀이 나쁘다기 보다는.. AX팀을 만들어놓고 "너희가 AX팀이니까 빨리 AI로 자동화해봐"가 문제라는 말 같아요.. 도메인 현업자가 주도하고 AX기술자가 서포트하면서 AI를 도입하는게 가장 좋을것 같은데.."**
  - 출처: GeekNews / 작성자 `snisty` / https://news.hada.io/topic?id=28341 / 토픽 2026-04-09, 댓글 "5달전"(2026-09-05 조회) `[페치경유]`
  - 검증 상태: 정서·의견
- **"현장의 병목을 아는 사람들이 핵심 같습니다."** — `wfedev` / 같은 토픽 `[페치경유]`
- **"아쉽게도 회사에서 AX팀이 이미 많이 생긴 상황이라 맨 마지막 문단쪽을 신경써서 대응해 나가야 겠네요."** — `tsboard` / 같은 토픽 `[페치경유]`
  - 검증 상태: 정서
- ⚠️ **`[페치경유]` 인용이다. 이 책의 논지와 제목까지 겹치는 자료이므로, 인용 전 반드시 해당 URL을 직접 열어 원문을 확인하라.** 이 문서에서 재확인 우선순위 1번이다.

> **책에서 쓸 지점 — 이 책의 정체성이 걸린 자료다.** 한국 개발자 커뮤니티에는 이미 **"AX팀을 만드는 것 자체가 실패의 시작"**이라는 명제가 유통되고 있다. 이 책이 「AX 체계 구축」이라는 제목을 달고 나가는 순간, 이 명제를 **모르고 쓴 책**으로 읽힐 위험이 있다.
>
> 그런데 `snisty`의 문장을 정확히 읽으면 반대가 아니다 — **"AX팀이 나쁜 게 아니라, AX팀에게 '너희가 알아서 자동화해봐'라고 던지는 게 문제"**라는 것이다. 그리고 처방은 **"도메인 현업자가 주도하고 AX기술자가 서포트"**다. **이게 정확히 이 책이 교정한 논지와 같다.** 이 토픽을 서문이나 1장에서 **먼저 인용하고 동의를 표한 뒤 들어가면**, 이 책은 "AX팀 만들자는 책"이 아니라 "AX팀이 실패하는 이유를 아는 책"이 된다. **오프닝 전략으로 강력히 권한다.**

## C-2. 강제하면 망한다 — 증거는 풍부하다

**1차에서 탑다운 강제 반발 11건을 확보했으므로 여기서는 중복을 피하고, 이번에 새로 나온 것 중 "왜" 망하는지를 설명하는 것만 싣는다.**

- **가장 직접적인 한국어 증언** — 원문 인용: **"도구를 자발적으로 선택해 사용할 때만 효과가 발휘되며, 강제로 떠밀린 사용자는 결코 잘 다루지 못함" 이거 공감이 많이 되네요**
  - ⚠️ **주의:** 앞의 따옴표 안은 **원문 기사 인용**이고, **뒷 문장("이거 공감이 많이 되네요")만 이 사용자의 발화**다. 인용할 때 이 구분을 지켜라.
  - 출처: GeekNews / 「AI가 직원을 대체한다고 믿는 CEO는 그저 무능한 CEO일 뿐」 / 작성자 `pjs102793` / https://news.hada.io/topic?id=30352 / 토픽 2026-06-10, 댓글 **2026-06-11** `[원문확인]`
  - 검증 상태: 정서(기사 인용에 대한 동의)

- **의사결정 권한의 위치가 갈림길이라는 진단** — 이 축에서 가장 정밀한 인용:
  - 원문 인용: **"That justifies using common tools and standards, but not why management in particular should be doing the selection. Everywhere mature that I've worked, management delegated the task of choosing common tools to the senior / staff engineers, as well as decisions around when to make changes or exceptions. The places that didn't do this were engineer-founded, or were dysfunctional enough that managers could splurge on massive contracts and then force people to use the paid-for tools to justify the contract post-hoc. Every one of these were examples of what not to do."**
    - 번역: "그건 **공통 도구와 표준을 쓰는 것**을 정당화하지, 왜 **하필 경영진이 선택**을 해야 하는지를 정당화하지는 않는다. 내가 일해본 성숙한 곳은 어디든 **경영진이 공통 도구 선택 과제를, 그리고 언제 변경하거나 예외를 둘지에 대한 결정을 시니어/스태프 엔지니어에게 위임했다.** 그렇게 하지 않은 곳들은 엔지니어가 창업한 곳이거나, **관리자가 거대 계약에 돈을 쏟아붓고 나서 그 계약을 사후에 정당화하려고 사람들에게 돈 낸 도구를 쓰라고 강제할 만큼 기능 부전인 곳**이었다. 이들 하나하나가 **하지 말아야 할 일의 예**였다."
  - 출처: Hacker News / "AI coding mandates are driving developers to the brink" / 작성자 `zdragnar` / https://news.ycombinator.com/item?id=43634260 / **2025-04-09**
  - 검증 상태: 경험담·조직 진단
  - **책에서 쓸 지점 — 이 축의 핵심 구분이 여기 있다.** 문제는 **"중앙이 표준을 정하는 것"**이 아니라 **"중앙의 누가 정하는가"**다. 성숙한 조직에서도 표준화는 일어난다. 다만 **선택권이 경영진이 아니라 시니어 엔지니어에게 위임**돼 있다. 이 책의 "탑다운이 할 일은 거두는 체계"라는 명제를 **조직 설계로 번역하면 "결정권의 위임"**이다. 그리고 뒷부분은 강제의 진짜 원인을 짚는다 — **계약을 먼저 하고 사용을 나중에 강제하는 순서.**

- **같은 스레드의 반대편(표준화 옹호)도 기록한다:**
  - 원문 인용: **"There is organizational efficiency around everyone using the same tools. Management can pick a set of tools to focus on. Not all developers know how to use all tools. Management providing education on tools can increase their efficiency. Developers do not stay up to date with all available tools that exist. Management providing better tools can make people more efficient."**
    - 번역: "모두가 같은 도구를 쓰는 데는 조직적 효율이 있다. 경영진은 집중할 도구 세트를 고를 수 있다. 모든 개발자가 모든 도구 사용법을 아는 건 아니다. **경영진이 도구 교육을 제공하면 효율을 높일 수 있다.** 개발자들이 존재하는 모든 도구를 최신으로 따라가지는 않는다. **경영진이 더 나은 도구를 제공하면 사람들을 더 효율적으로 만들 수 있다.**"
  - 출처: 같은 스레드 / 작성자 `charcircuit` / https://news.ycombinator.com/item?id=43633818 / **2025-04-09**
  - 검증 상태: 정서·논리
  - **책에서 쓸 지점:** 주목 — **이 옹호론의 동사는 전부 "제공한다(providing)"이지 "강제한다"가 아니다.** 반대편조차 강제를 옹호하지 않는다. 이 책의 논지("공급하되 강제하지 않는다")는 커뮤니티의 **양쪽 진영이 모두 동의할 수 있는 지점**이다. 이건 큰 발견이다.

- **AI 자체가 문제가 아니라는 진단** — 원문 인용: **"This pattern is maybe 20% about AI specifically and 80% about low-trust leadership."**
  - 번역: "이 패턴은 아마 **20%만 AI에 관한 것이고 80%는 저신뢰 리더십**에 관한 것이다."
  - 출처: 같은 스레드 / 작성자 `tikhonj` / https://news.ycombinator.com/item?id=43633581 / **2025-04-09**
  - 검증 상태: 정서
  - **책에서 쓸 지점:** 이 책이 AX 도입 실패를 기술 문제로 다루면 80%를 놓친다.

- 강제의 경제적 원인: **"when the company is paying big money for a tool you can bet they're going to make sure people are using it"** / **"We made a poor investment and now we're making it our employees problem" is absolutely a common outcome from business leaders yeah"** — `bluefirebrand` / https://news.ycombinator.com/item?id=43633599 및 https://news.ycombinator.com/item?id=43633637 / **2025-04-09**
  - 번역: "회사가 도구에 큰돈을 내고 있으면, 사람들이 그걸 쓰고 있는지 확실히 하려 들 거라고 장담해도 좋다." / "'우리가 나쁜 투자를 했고 이제 그걸 직원 문제로 만든다'는 건 사업 리더들에게서 아주 흔한 결과다, 맞다."
  - **책에서 쓸 지점:** §A-3의 라이선스 비용과 §C의 강제가 **같은 사슬**이라는 증거. **비싼 시트를 사면 사용률 강제가 따라오고, 사용률 강제는 §A-2의 지표 게이밍을 낳는다.** 이 3단 연쇄를 한 챕터로 묶으면 이 책에서 가장 설명력 있는 절이 된다.

- **중앙이 나쁜 도구를 공급했을 때의 결과** (§B-3에서 인용한 `Quothling`의 문장을 여기서 다시 지목한다):
  > **"we have always had access to their Copilot app. Which has been so bad that it's actively turned people away from AI."**
  > (번역: "우리는 늘 그들의 Copilot 앱에 접근할 수 있었다. **그런데 그게 너무 형편없어서 사람들을 오히려 AI에서 멀어지게 만들었다.**")
  - 출처: Hacker News / `Quothling` / https://news.ycombinator.com/item?id=48566235 / **2026-06-17**
  - **책에서 쓸 지점: 중앙 공급의 실패는 "안 쓴다"가 아니라 "면역이 생긴다"다.** 나쁜 도구를 중앙이 깔면 다음에 좋은 도구를 깔아도 안 온다. 이 책의 "거두는 체계"는 **공급의 품질 관리**를 포함해야 한다.

- 한국의 강제 반대 정서:
  - **"시대에 뒤쳐지고 있는 사람들이죠. 굳이 강제로 하라고 하실 필욘 없습니다."** — `hobak` / OKKY / https://okky.kr/articles/1562235 / 게시글 2026-08-13, "23일 전"(2026-09-05 조회) `[원문확인]`
  - **"강요: 좋지 않습니다. 특히 그분이 에이전트가 프로젝트 파일을 직접 수정하거나 형상을 바꾸는 것에 불안감을 느끼고 있다면, 오히려 반발만 커질 수 있습니다. 권유: 한두 번 정도는 괜찮습니다. 다만 "AI가 훨씬 좋은데 왜 안 쓰세요?"보다는 "이런 작업에서는 AI를 활용하되 최종 검토는 사람이 하는 방식으로 시간을 줄일 수 있다" 정도가 적절하겠죠."** — `톰소여` / 같은 글 / "23일 전"(2026-09-05 조회) `[원문확인]`
    - ⚠️ **본인이 말미에 "답변을 AI를 통해서 정리해봤어요"라고 밝힌 댓글이다.** AI로 정제된 텍스트임을 감안하고, 인용한다면 그 사실을 함께 밝혀라.
  - **"대 AI 시대 에 어차피 한 번은 겪어야 할 시련입니다. 다들 AI뽕을 거하게 맞아서 미쳐 돌아가는데, AI 만능론에 젖어있는 상태를 인위적으로 바꿀 수는 없습니다."** — `yeori` / OKKY / https://okky.kr/articles/1556920 / 게시글 2026-05-14, "4개월 전"(2026-09-05 조회) `[원문확인]`
  - **"요즘은 내돈주고 산 윈도우에도 업데이트 할때마다 다크패턴으로 별 이상한 기능 켜게 유도하는거 피곤하긴 합니다."** (GitHub Copilot 강제 활성화 건에 대해 — **핵심 불만이 기능이 아니라 "끌 수 없다"는 점**) — `hhcrux` / GeekNews / https://news.hada.io/topic?id=22944 / 토픽 2025-09-07, 댓글 "12달전"(2026-09-05 조회) `[페치경유]`
  - 검증 상태: 전부 정서

- **강제가 현장에 실제로 남기는 것** (한국) — 원문 인용: **"AI가 없었을때는 신입개발자가 단순한 업무라도 구현하면서 실력을 키워왔습니다. 그러나 이제 회사는 신입이 성장하는걸 기다려주지 않습니다. AI를 쓰던 뭘 하든 간에 결과물을 내야 하는거죠. 걱정하신대로 그렇게 AI로만 일하면 머릿속에 남는건 거의 없습니다."**
  - 출처: OKKY / 「"클로드로 하면 되잖아" 식의 업무 지시, 다른 회사도 이런가요?」 / 작성자 `제운` / https://okky.kr/articles/1556920 / "4개월 전"(2026-09-05 조회) `[원문확인]`
  - 검증 상태: 정서·경험 기반 진단
  - **책에서 쓸 지점:** 1차의 직무 불안 5건과 이어지되 각도가 다르다 — **강제의 비용은 반발이 아니라 학습 손실**이다.

## C-3. 【희소】 중앙이 깔아주니 산 경우 — 확보한 것

**1차에서 `caconym_`의 "강요하지 않는 도구 제공" 1건만 확보했다고 했다. 이번에 3건 더 찾았다. 여전히 적지만, 셋 다 서로 다른 각도다.**

### ① 강제가 없는데도 전원이 자발적으로 채택한 사례

- 원문 인용: **"That's funny, there isn't any mandate for using LLMs at my company. Everybody has just quietly added them to their workflows without being told. LLMs are like chainsaws. In the right hands, they can help you do the same job faster. In the wrong hands, it could cut off a limb. If someone drops a thousand line PR of total slop, it's not an AI failure, it's a human failure. Personally, I use LLMs for fill-in-the-middle jobs and boosting test coverage. It's a modest benefit, but I am definitely shipping higher quality software in a shorter period of time compared to before."**
  - 번역: "웃기게도, **우리 회사에는 LLM 사용에 대한 어떤 강제도 없다. 모두가 그냥 시키지 않았는데도 조용히 자기 워크플로에 추가했다.** LLM은 전기톱 같다. 좋은 손에 들어가면 같은 일을 더 빨리 하게 도와준다. 나쁜 손에 들어가면 팔다리가 잘릴 수 있다. 누군가 완전 쓰레기 천 줄짜리 PR을 던진다면 그건 AI의 실패가 아니라 인간의 실패다. 개인적으로 나는 중간 채우기 작업과 테스트 커버리지 향상에 LLM을 쓴다. **소박한 이득이지만, 예전보다 확실히 더 짧은 시간에 더 높은 품질의 소프트웨어를 출하하고 있다.**"
  - 출처: Hacker News / "AI coding mandates are driving developers to the brink" / 작성자 `noident` / https://news.ycombinator.com/item?id=43633877 / **2025-04-09**
  - 검증 상태: 경험담
  - **책에서 쓸 지점: 이 인용이 이 책 관통선 교정의 가장 깨끗한 증거다.** **강제가 없는 조직에서 채택률이 100%에 가깝다.** 그리고 주목할 것 — 이 사람이 보고하는 이득은 "10배"가 아니라 **"소박한(modest)"**이다. **자발적 채택은 과장 없는 이득 보고와 함께 온다.** §A-2의 강제된 조직의 "95%/70%" 수치와 나란히 놓으면, **강제는 채택률을 만드는 게 아니라 보고된 수치를 만든다**는 대비가 성립한다.

### ② "깔아주되 강제하지 않는다"의 명시적 원칙 진술

- 원문 인용: **"Standardization is valuable. An extreme example of your position would be a shop where everyone uses a different language. That's obviously untenable. A more reasonable example might be choice of editor. I'm of the opinion that management should provide everyone a standard editor, then not mandate it's use. This means anyone can hop onto any device and know how to use it, even if the device owner has a super-customized vim setup. Folks who become familiar with the standard editor are also better positioned to help their colleagues troubleshoot their setups."**
  - 번역: "표준화는 가치 있다. 당신 입장의 극단적 예는 모두가 다른 언어를 쓰는 가게일 텐데, 그건 명백히 지탱 불가능하다. 더 합리적인 예는 에디터 선택일 것이다. **나는 경영진이 모두에게 표준 에디터를 제공하되, 그 사용을 강제하지는 말아야 한다는 의견이다.** 이는 기기 소유자가 극도로 커스터마이즈된 vim 셋업을 갖고 있더라도 **누구든 아무 기기에나 뛰어들어 쓸 줄 안다**는 뜻이다. 표준 에디터에 익숙해진 사람들은 **동료의 셋업 문제 해결을 도와주기에도 더 좋은 위치**에 있다."
  - 출처: 같은 스레드 / 작성자 `itishappy` / https://news.ycombinator.com/item?id=43634756 / **2025-04-09**
  - 검증 상태: 정서·설계 원칙
  - **책에서 쓸 지점 — 이 책이 찾던 문장이 이것이다.** **"제공하되 강제하지 않는다(provide, then not mandate)"**가 커뮤니티 언어로 명시적으로 진술돼 있다. 그리고 **왜** 그게 통하는지의 근거 두 가지까지 붙어 있다: (a) **이식성** — 누구나 어떤 환경에든 들어갈 수 있다, (b) **상호 지원 가능성** — 공통 기반을 아는 사람이 남을 도울 수 있다. 이 두 근거는 **강제 없이도 표준화의 이득을 얻는 메커니즘**이다. 이 책의 "거두는 체계"를 설계할 때 그대로 쓸 수 있다.
  - 다만 같은 사람이 곧바로 유보를 단다 — 원문 인용: **"I don't see how this applies to AI assistants much if at all. It feels like mandating devs run all their ideas by a particular intern. If said intern isn't an architect then there's no value in having a single point of contact."** (번역: "이게 AI 어시스턴트에 얼마나 적용되는지는 잘 모르겠다. **개발자들에게 모든 아이디어를 특정 인턴에게 거쳐 가라고 강제하는 것처럼 느껴진다.** 그 인턴이 아키텍트가 아니라면 단일 접점을 두는 데 가치가 없다.")
    - **책에서 쓸 지점: 이 유보를 반드시 함께 실어라.** 에디터 표준화는 통하지만 AI 어시스턴트 표준화는 다를 수 있다는 지적이다. **이 책의 "중앙 공급" 처방이 도구 종류에 따라 다르게 작동할 수 있다**는 경고.

### ③ 현장 주도로 굴러가는 조직의 실물 묘사 (한국)

- 원문 인용: **"비개발자: 간단한 수정 후, ai에게 리뷰돌리고 이후 개발자에게 pr / 개발자: ai도움을 받아 코드작성 … → ai로 한번더 리뷰 → 다른 동료 개발자에게 PR / 작업외로는 반복되는 업무들 워크플로우로 만들고 있음 / 예를 들면 cx에서 버그가 들어오면 자동으로 정리해서 슬랙에 올리고 Jira 티켓만들고 배정하고 예상되는 문제 알려주고 긴급등급 평가"**
  - 출처: OKKY / 작성자 `BlessU` / https://okky.kr/articles/1561453 / 게시글 2026-07-31, 댓글 "약 1개월 전"(2026-09-05 조회) `[원문확인]`
  - 검증 상태: ⚠️ 익명 주장(사내 운영 상태) — 미검증 / **자기 회사 자랑 톤이므로 같은 글의 반대 증언과 함께 읽어야 한다** (같은 스레드의 `개발의민족`: **"1000줄짜리 코드가 5분만에 나옵니다. mr을 보통 하루만에 올리고 다음날 머지해요. 이 코드를 이해할 시간이 있을까요?"** / `exexexe`: **"코드도 ai 만들고, 테스트도 ai 가 하고 있어요. 당연히 코드를 이해도 못하고요."**)
  - **책에서 쓸 지점:** 잘 굴러가는 조직의 묘사에서 **중앙이 등장하지 않는다.** 등장하는 건 **역할별 워크플로와 리뷰 게이트**다. 이 책의 "거두는 체계"가 조직도가 아니라 **워크플로 형태**여야 한다는 힌트.

### ④ 규칙이 먼저라는 반대 방향의 목소리 (균형)

- **"조직의 룰을 수립하는 것이 우선되어야 한다고 생각해요."** — `SANGWON LEE`(글쓴이) / OKKY / 「AI 도입은 잘됐는데 조직은 더 복잡해진 경험 있으신가요?」 / https://okky.kr/articles/1557492 / 게시글 2026-05-24, "3개월 전"(2026-09-05 조회) `[원문확인]`
- **"결국 병목은 인간이네요"** — `꼬부기` / 같은 글 / "4개월 전"(2026-09-05 조회) `[원문확인]`
- **"AI 시대가 와도 은탄환은 없는 것 같습니다"** — `천사와악마` / OKKY / 「AI 도입에서 실행력보다 운영 원칙이 더 중요하다고 느낀 이유」 / https://okky.kr/articles/1557169 / 게시글 2026-05-19, "4개월 전"(2026-09-05 조회) `[원문확인]`
- 검증 상태: 정서
- **책에서 쓸 지점: 한국 커뮤니티에는 "룰이 먼저"라는 목소리도 분명히 있다.** 이 책이 바텀업만 강조하면 이쪽 독자를 잃는다. 위 §C-1의 `snisty`가 정확한 절충선이다 — **룰은 필요하되 현업이 주도한다.**

- 병목이 개발이 아니라 의사결정이라는 지적: **"왜 이런 일이 생기냐면 결국 마케팅이 목줄을 쥐고 있으니까... 시장이 주는 기회는 한정 되어 있는데 오만가지 다 내놓을 수 없으니 고르고 고르는 시간이 병목이 되는거죠."**
  - 출처: GeekNews / 「The Agentic Awakening — 코딩이 10배 빨라져도 조직 생산성이 따라오지 않는 이유」 / 작성자 `bus710` / https://news.hada.io/topic?id=33058 / 게시 2026-08-31, 댓글 "5일전"(2026-09-05 조회) `[페치경유]`
  - 검증 상태: 정서
  - **책에서 쓸 지점:** §A-1의 "생산성이 올라도 정원이 안 준다"에 대한 또 다른 설명 — **병목이 생산이 아니라 선택에 있으면, 생산 속도를 올려도 처리량이 안 는다.** 이건 이 책의 FTE 논의에 물리적 근거를 준다.

## C 커버리지

**확보**
- **한국 GeekNews의 「AX팀을 만드는 순간, 당신의 조직은 AX에 실패한다」 토픽과 댓글 3건** — 이 책의 제목·논지와 직접 충돌하며 동시에 화해 가능한 자료. **최대 수확.**
- 강제가 망하는 **이유**를 설명하는 인용 5건 (결정권 위치 / 저신뢰 리더십 / 계약 사후 정당화 / 면역 형성 / 학습 손실)
- **"제공하되 강제하지 않는다"의 명시적 원칙 진술 1건 + 그 메커니즘 2가지** (`itishappy`, 2025-04) — **요청하신 항목의 정답에 해당**
- **강제 없이 100% 자발 채택된 조직 증언 1건** (`noident`, 2025-04) — 요청하신 항목
- 표준화 옹호론 1건 — **그 옹호론조차 동사가 "제공한다"라는 발견**
- 한국의 강제 반대 정서 5건 + "룰이 먼저"라는 반대편 3건

**비어 있음**
- **플랫폼 엔지니어링·paved road·golden path·이너소스에 대한 정면 토론 — 확보 실패.** HN에서 `"golden path"`·`"paved road"`는 압도적으로 **다른 의미**(코드의 정상 경로, 실제 포장도로)로 쓰인다. `"internal developer platform"` 정확 구절은 2025-01 이후 **8건뿐**이고 대부분 제품 홍보다. `innersource`는 HN 스토리 검색에서 **관련 결과 0건.** → **이 담론은 HN에 없다. 컨설팅 블로그·컨퍼런스(PlatformCon)·CNCF 쪽에 있다. web-researcher에 이관 권장.**
- **"중앙 플랫폼 강제가 실패한 회고" 중 플랫폼 엔지니어링 맥락의 것 — 확보 실패** (AI 도구 강제 맥락은 풍부하나, IDP/플랫폼팀 맥락의 회고는 못 찾았다).
- **한국에서 "중앙이 쉬운 길을 깔아주니 됐다"는 실증 성공 사례 — 0건.** `snisty`의 발언이 가장 근접하나 **당위 진술이지 사례 증언이 아니다.** `BlessU`의 묘사는 중앙이 등장하지 않는 자발 사례다.
- **사내 AI 도구를 중앙이 잘 제공한 성공 사례 — 사실상 0건.** `Quothling`의 cowork 도입이 유일하게 긍정적인데, 그 사람도 **직전 제품(Copilot)이 사람들을 AI에서 멀어지게 했다**고 증언한다. **즉 이 조사에서 확보한 유일한 중앙 공급 성공담은 실패담 뒤에 붙어 있다.**

---

# D. 챕터 오프닝용 강한 인용문 (2차 수확분)

> 선정 기준: (1) 한 문장으로 장면이 서는가, (2) 이 책의 논지와 **긴장**을 만드는가, (3) 출처가 확실한가. **원문을 그대로 옮겼다. 각색하지 마라.** 등급은 ★★★(단독으로 챕터를 열 수 있음) / ★★(보조).

## D-1 ★★★ 「엑셀은 일을 자동화한 게 아니라 상시화했다」 — 절감이 사라지는 이유
> **"엑셀이 나와서 바뀐 것의 핵심은 일을 자동화시켜준 것이라기 보다는. 일을 실시간으로 그리고 항시적으로 만든거죠. 발표 5분전이라도 수정할수 있는 긴장된 상태가 유지되니.. 일하는 시간개념이 실시간인 동시에 항시적이라 결국 바빠집니다."**
> — `filekiwi` / GeekNews / https://news.hada.io/topic?id=20632 / 2025-05-13 `[원문확인]`

**왜 좋은가:** 한국어 원문이라 번역 손실이 없다. 40년 전 도구로 지금을 설명하므로 AI 논쟁의 진영 싸움을 우회한다. 그리고 **PART 4 전체의 전제를 뒤흔든다** — 절감분이 어디로 갔는지 묻는 대신, **절감분이 애초에 생기지 않는 구조**를 보여준다. `kimjoin2`의 교통수단 비유(같은 스레드, 2025-05-01)를 이어 붙이면 문단 하나가 완성된다.

## D-2 ★★★ 「토큰 리더보드 상위에 남으려고 이미지 픽셀을 무작위로 바꾼다」 — 지표 게이밍
> **"At Cerebras I know of several people who burn tokens on completely USELESS tasks (randomly changing pixels in an image) just to keep them high up on the token leaderboard. ... They made the metric "token usage" (which is just a proxy for LOC) so that's what they're gonna get."**
> — `joshuastuden` / Hacker News / https://news.ycombinator.com/item?id=47978177 / 2026-05-01
> ⚠️ 익명 주장 — 미검증

**왜 좋은가:** 추상적 Goodhart 법칙이 **이미지 픽셀**이라는 구체 이미지로 내려온다. **같은 달(2026-05) 한국 GeekNews에도 "Amazon 직원들이 AI 토큰 소비량을 부풀린다"는 토픽이 섰다**(id=29568). 두 대륙, 같은 달, 같은 행동. 이 병치가 오프닝의 구조를 만든다.
**짝 인용:** `happing94`의 **"예전에는 개발자들의 개발실력 지표를 코드 몇줄 썼냐 그걸로 지표 설정했었으니까 ㅋㅋㅋ"**(GeekNews, 2026-05-18) — 한국 독자가 즉시 알아보는 계보.

## D-3 ★★★ 「우리 회사에서 사람들은 항상 인력 절감분을 축소해서 보고한다」 — 측정의 정치
> **"At my company people always understate the headcount savings. Because the invariable question is - "You are spending x million and for y FTEs you save only 1 FTE of HC? How does that make sense?". Or worse yet - "You estimated 40 FTE savings, why don't we pick and chose 40 FTEs to let go". That sends shivers down managers as it reduces their area of influence."**
> — `thisisit` / Hacker News / https://news.ycombinator.com/item?id=45529408 / 2025-10-09
> ⚠️ 익명 주장(사내 관행) — 미검증

**왜 좋은가:** 이 책의 PART 4가 하려는 일(정확한 FTE 환산)이 **왜 현장에서 저항받는지**를 한 문단으로 설명한다. 저항의 이유가 무능이 아니라 **자기 보존**이라는 점이 핵심이다.
**짝 인용(한국, 더 짧고 더 아프다):** `The developer.`의 **"개발자가 먼저 나서서 미친 생산성을 보여줬기에… 관리자는 "더 미친 생산성" 을 바랄 뿐입니다. 그러게 적당히 사용했어야죠."**(OKKY, 2026-05-14) — **처벌의 형태가 감원이 아니라 기준선 상향**이라는 더 흔한 진실.

## D-4 ★★★ 「AI는 많이 쓰는 게 잘 쓰는 게 아니다」 — 자율성 등급 챕터
> **"챗봇은 답변 받는 도구고, 에이전트는 IDE·저장소·사내 시스템까지 건드리기 시작하면 권한, 보안, 데이터 반출, 감사 얘기가 바로 붙는 거져. ... AI는 많이 쓰는 게 잘 쓰는 게 아니라 어디까지 믿고, 어디부터 검증하고, 어디까지 권한 줄지 아는 게 잘 쓰는 거임미다."**
> — `이뜸미당` / OKKY / https://okky.kr/articles/1562235 / 2026-08-13 게시글, "23일 전"(2026-09-05 조회) `[원문확인]`

**왜 좋은가:** **이 문서 전체에서 이 책의 논지와 가장 잘 맞는 인용이면서, 동시에 §A-2의 사용률 지표를 부정한다.** 한국 실무자가 자기 언어로 이 책의 목차를 말해버린 셈이다. 서문이나 1장에 배치하면 "이 책은 이미 현장에 있는 문제의식을 체계화한 것"이라는 위치가 잡힌다.
**짝 인용:** 글쓴이가 "우리 팀은 다 15년차라 괜찮다"고 하자 나온 응수 — **"15년차가 보안통제도 되고, 변경영향도 분석도 되고, 회귀테스트도 되는 만능 미들웨어였군여.."**

## D-5 ★★★ 「사용자가 권한 프롬프트의 약 93%를 승인했다」 — 승인은 통제가 아니다
> **"Theoretically that works, but we've found the approach to be fallible. Our telemetry showed users approved roughly 93% of permission prompts. The more approvals a user sees, the less attention they pay to each, becoming over time much less diligent in their supervision."**
> — Anthropic 엔지니어링 포스트, `ericmcer`가 인용 / Hacker News / https://news.ycombinator.com/item?id=48403146 / 2026-06-04
> ⚠️ 벤더 1차 자료의 2차 인용 — **원문 직접 확인 필요**

**왜 좋은가:** 숫자 하나가 통제 설계의 통념을 무너뜨린다. **"인간이 승인한다"는 안전장치가 실은 93%의 확률로 통과 도장**이라는 것. 이 책이 자율성 등급을 승인 축으로 설계하려 한다면, 이 인용이 그 설계를 시작 전에 재고하게 만든다.
**짝 인용:** `emk`의 **"Anything based on asking users to approve/deny is a catastrophe waiting to happen."**(Lobsters, 2026-07-20)

## D-6 ★★★ 「보안은 환경에 속한다. 하네스가 아니라」 — 등급의 위치
> **"A simpler approach is just to give the agent it's own user account and let the OS treat it like an untrusted undergrad on a shared Unix host, like back in the old days. Or buy the agent a Mac Mini if you can afford it. The point is, security belongs in the environment. Not the harness!"**
> — `emk` / Lobsters / https://lobste.rs/c/j7ueyx / 2026-07-20

**왜 좋은가:** **이 책의 "사번" 은유가 커뮤니티에 이미 존재한다** — 다만 "직원"이 아니라 **"신뢰할 수 없는 학부생"**이라는 이름으로. 이 대비 자체가 챕터를 연다. 그리고 마지막 두 문장은 이 책 등록 챕터의 설계 원칙으로 그대로 쓸 수 있다.

## D-7 ★★★ 「AX팀을 만들어놓고 "너희가 AX팀이니까 빨리 자동화해봐"가 문제」 — 서문용
> **"AX 추진팀이 나쁘다기 보다는.. AX팀을 만들어놓고 "너희가 AX팀이니까 빨리 AI로 자동화해봐"가 문제라는 말 같아요.. 도메인 현업자가 주도하고 AX기술자가 서포트하면서 AI를 도입하는게 가장 좋을것 같은데.."**
> — `snisty` / GeekNews / https://news.hada.io/topic?id=28341 / 토픽 2026-04-09 「AX팀을 만드는 순간, 당신의 조직은 AX에 실패한다」 `[페치경유]`
> ⚠️ **재확인 우선순위 1번**

**왜 좋은가:** 이 책 제목을 정면으로 겨눈 명제가 이미 한국 커뮤니티에 있다. **그걸 먼저 인용하고 동의를 표한 뒤 시작하면**, 책의 위치가 "AX팀 만들자는 책"에서 "AX팀이 왜 실패하는지 아는 책"으로 바뀐다. **서문 오프닝 최우선 후보.**

## D-8 ★★★ 「Klarna는 세 청중에게 동시에 다른 말을 하고 있다」 — FTE 챕터 오프닝
> **"So they simultaneously claim that they've got AI that has replaced 700 people, but that they haven't actually fired 700 people, but if you're listening Wall Street we're are firing them, but if you're listening EU regulators and main street no no we're definitely not."**
> — `SilverBirch` / Hacker News / https://news.ycombinator.com/item?id=39548544 / 2024-02-29

**왜 좋은가:** "AI로 N명분"이라는 문장이 **하나의 사실 주장이 아니라 청중별로 다른 세 개의 진술**임을 폭로한다. 이 책이 FTE 환산표를 내밀 때 독자가 던질 첫 질문("이 표는 누구에게 보여주는 표인가")을 미리 세운다.
**짝 인용(한국, 검증 가능한 반문):** `k35241`의 **"그러면 ai를 사용하는 사람수만큼 사람수를 줄여야 하는데 그렇게 되고 있나요?"**(OKKY, 2026-08-16)

## D-9 ★★ 「너무 쉬워 보이게 만들어서 승진에서 탈락했다」 — 절감 보고의 정치
> 스레드 제목: **「Got denied a promotion because I make it look too easy」**
> 댓글: **"I literally learned to code on the job between tasks and automated 60% of my tasks. The management I was under simply didn't care."**
> — `u/gummytoejam` / Reddit r/antiwork / https://reddit.com/r/antiwork/comments/1knyu3j/got_denied_a_promotion_because_i_make_it_look_too/mss3h0i/ / 2025-05-17
> ⚠️ 익명 주장 — 미검증 / ⚠️ 아카이브 API 경유 취득, 직접 열람 미검증

**왜 좋은가:** **제목 자체가 문장이다.** 다만 Reddit 검증 한계가 있으므로, 본문 인용보다 **제목만 인용**하는 편이 안전하다.

## D-10 ★★ 「여기서 계속 일하고 싶으면 그거 치워!」 — 자동화 보고의 결과
> **"When she showed it to her boss, hoping to get a positive response, his reaction was "Put that away if you like your job here!" This is the nightmare of every middle manager."**
> — `ChuckNorris89` / Hacker News / https://news.ycombinator.com/item?id=20196593 / **2019-06-16**
> ⚠️ 익명 주장(전언 일화) — 미검증 / 🕒 **7년 전 — 시점 명시 필수**

**왜 좋은가:** 한 마디 대사가 장면을 만든다. 1차의 오프보딩 챕터가 쓴 **"7년 전과 지금이 같은 문장"** 구도를 재사용할 수 있다.

## D-11 ★★ 「인벤토리를 만들었지만 방치를 막지는 못했다 — 그 도구도 방치됐다」 — 등록소 챕터
> **"어떤 프로젝트가 있는지 잘 기억이 안날때가 많아서 ... 대시보드를 만들어서 관리하고있습니다. 이걸로 방치되는걸 막진 못하지만..."**
> 후속: **"직접 만들어서 출시까지 해보려고 생각중인 앱인데, 이 프로젝트 자체도 방치된 상태네요 .."**
> — `esc5221` / GeekNews / https://news.hada.io/topic?id=20885 / 2025-05-13 `[페치경유]`

**왜 좋은가:** 이 책의 등록소 처방에 대한 **가장 겸손하고 가장 아픈 반증.** 독자가 웃으면서 수긍한다. 1차의 Confluence 인용 5건과 같은 구조.

## D-12 ★★ 「우리 회사엔 강제가 없는데 모두가 조용히 쓰기 시작했다」 — 축 3 교정
> **"That's funny, there isn't any mandate for using LLMs at my company. Everybody has just quietly added them to their workflows without being told. ... It's a modest benefit, but I am definitely shipping higher quality software in a shorter period of time compared to before."**
> — `noident` / Hacker News / https://news.ycombinator.com/item?id=43633877 / 2025-04-09

**왜 좋은가:** 강제가 없는 곳의 채택률이 더 높고, **보고되는 이득이 "소박하다"**는 대비. §A-2의 "95%가 쓴다"와 나란히 놓으면 강제가 무엇을 만드는지가 드러난다.

## D-13 ★★ 「경영진은 표준 에디터를 제공하되 사용을 강제하지는 말아야 한다」 — 축 3 처방
> **"I'm of the opinion that management should provide everyone a standard editor, then not mandate it's use."**
> — `itishappy` / Hacker News / https://news.ycombinator.com/item?id=43634756 / 2025-04-09

**왜 좋은가:** 이 책의 관통선 교정이 커뮤니티 언어로 정확히 진술된 유일한 문장이다. **단, 같은 사람의 유보("AI 어시스턴트에도 적용되는지는 모르겠다")를 반드시 함께 실어라** — 그러면 인용이 선전이 아니라 논증이 된다.

## D-14 ★★ 「그게 너무 형편없어서 사람들을 오히려 AI에서 멀어지게 만들었다」 — 중앙 공급의 실패
> **"we have always had access to their Copilot app. Which has been so bad that it's actively turned people away from AI."**
> — `Quothling` / Hacker News / https://news.ycombinator.com/item?id=48566235 / 2026-06-17
> ⚠️ 익명 주장(사내 상황) — 미검증

**왜 좋은가:** 중앙 공급 실패의 결과가 **무관심이 아니라 면역**이라는 것. 한 번 나쁜 도구를 깔면 다음 기회가 없다.

## D-15 ★★ 「디지털 좌석을 발명해서 정원에 계속 과세하려 한다」 — 라이선스 챕터
> **"If a company gets more efficient and uses fewer people - Microsoft's immediate reaction is to figure out how to invent some kind of digital seats so they can keep taxing the headcount."**
> — `latand6` / Hacker News / https://news.ycombinator.com/item?id=47762102 / 2026-04-14

**왜 좋은가:** 이 책의 "에이전트를 정원에 산입한다"는 장치가 **이미 벤더 과금 논리로 존재한다**는 사실을 독자에게 먼저 알려준다. 모르고 쓰면 순진해 보이고, 알고 쓰면 정교해 보인다.
**짝 인용(개념적으로 더 깊음):** `bit1993`의 **"Humans are non-fungible AI is not"**(2026-04-14) — 에이전트 "1대"의 경계는 누가 정하는가.

---

# E. 이 책의 주장에 대한 추가 반론 (저술 시 응답 필요)

> 1차에서 반박 A~I를 기록했다. 여기서는 **2차에서 새로 발견된 반론만** 다루며, 각 항목에 **근거 / 이 반론이 겨누는 이 책의 어느 부분 / 응답 전략 초안**을 붙인다. 응답 전략은 제안이지 지시가 아니다.

## 반박 J — 「측정을 정확하게 만들면 현장은 더 숨긴다」 (PART 4 전체를 겨눔)

**근거:** `thisisit`("항상 절감분을 축소해서 보고한다" + 경영진의 "40 FTE 절감이라니 40명을 골라 내보내자") / `The developer.`("그러게 적당히 사용했어야죠") / `baeba`("능력 100을 다 보여주지 않으심이") / `ta1243`("항상 예산을 다 써라, 아끼면 내년에 벌받는다") / `thewebguyd`("의도적으로 평범한 게 낫다").

**겨누는 지점:** 이 책이 "FTE 환산으로 AX 효과를 가시화하자"고 제안하는 대목 전부.

**왜 위험한가:** 이 반론은 **측정 도구의 품질 문제가 아니다.** 도구가 정확해질수록 위협이 커지므로 저항이 커진다. **정확도 개선이 문제를 악화시키는 구조**다. 이 책이 "더 나은 측정법"을 제시하는 방식으로는 절대 답할 수 없다.

**응답 전략 초안:** 측정을 제안하기 **전에** 번역 금지 규칙을 명시하라 — **"이 숫자는 감원 명단으로 번역되지 않는다"를 제도로 보장하지 못하면 측정하지 마라.** 즉 PART 4의 순서를 뒤집어, **측정 방법론보다 측정 결과의 사용 제한(use limitation)을 먼저** 다루는 것. 그리고 §A-4에서 **재투자 성공 사례를 커뮤니티에서 한 건도 못 찾았다**는 사실을 정직하게 밝히고, 그럼에도 왜 그 규칙이 필요한지를 논증으로 세워라.

## 반박 K — 「METR을 인용하면 선택적 인용이 된다」 (근거 사용 규율)

**근거:** METR 2026-02-24 후속 연구가 **속도 향상**을 보고했다(`kalkin`, `ej88`가 인용). `kalkin`: "후속 연구는 아무도 인용하지 않는 것 같다. 그렇게 재미있는 반직관적 발견이 아니니까." / `logicprog`의 방법론 비판 5개항(비RCT·측정 대상 불일치·사용 규칙 부재 등) / `simonw`: "한 기관의 한 연구 위에 세계관 전체를 세우면 스스로를 속이는 것."

**겨누는 지점:** 이 책이 "개발자는 자기 생산성을 오판한다"는 명제의 근거로 METR 2025-07을 쓰는 대목.

**왜 위험한가:** 반박당하면 **그 하나가 아니라 책의 사실성 전반이 의심받는다.** 특히 이 책이 "숫자를 믿지 마라"고 말하는 책이라면, 자기 숫자를 선택적으로 인용한 것이 발견됐을 때 타격이 배가된다.

**응답 전략 초안:** 후속 연구를 **숨기지 말고 먼저 제시하라.** 그리고 논점을 옮겨라 — 이 책에 필요한 것은 "AI가 개발자를 느리게 한다"가 아니라 **"자기 보고와 실측이 갈라진다"**는 더 약하고 더 견고한 명제다. 후속 연구도 **주관적 추정이 과장한다**는 점은 유지했다(`kalkin`의 요약). **약한 명제로 후퇴하면 반박이 근거가 된다.**

## 반박 L — 「승인 기반 자율성 등급은 통제의 외양일 뿐이다」 (자율성 등급 챕터를 겨눔)

**근거:** 승인률 93% + 승인 피로(Anthropic 텔레메트리, `ericmcer` 인용) / `emk`: "승인/거부를 묻는 것에 기반한 어떤 것도 터지기를 기다리는 재앙" / `farmer kweon`: "승인 기다리면서 쉬는 경우가 허다해서" 집에서는 권한을 다 준다 / `kornel`: 모델이 권한 오류를 보고 **우회를 새 목표로 채택**한다 / `trigonella`: 에이전트가 스스로 권한 우회 명령을 실행할 수 있지 않나.

**겨누는 지점:** 이 책이 자율성 등급을 "승인 필요 / 사후 통보 / 완전 자율" 같은 승인 축으로 설계하는 대목.

**응답 전략 초안:** 등급의 축을 **승인이 아니라 능력(capability)과 환경**으로 잡아라 — `mjkl7896`의 목록이 그 원형이다. 승인은 **네 가지 고위험 행위**(패키지 설치·크리덴셜 접근·파괴적 명령·작업공간 밖 쓰기)에만 남기고, 나머지는 **닿을 수 없게 만든다.** 그리고 등급표에 **"위협 모델" 열**을 넣어라(`emk`). 이렇게 하면 반박 L이 이 책의 설계 근거로 전환된다.

## 반박 M — 「'사번을 준다'는 발상 자체가 권한 모델로서 틀렸다」 (등록 챕터의 근간을 겨눔)

**근거:** `jfred`: **"프로세스가 그 사용자의 모든 주변 권한을 갖고 '사용자로서' 돌아간다는 발상 자체가 우리를 이 난장판에 빠뜨린 것의 일부다. … 완전히 분리된 자기 사용자로 돌아가는 프로세스는 아마 권한이 충분하지 않을 것이다!"** (Lobsters, 2025-09-10) / `bit1993`: **"인간은 대체 불가능하지만 AI는 그렇지 않다"** — 에이전트 "1대"의 경계가 임의적이다 / `emk`: 계정을 주더라도 그건 "신뢰할 수 없는 학부생" 등급이다.

**겨누는 지점:** 이 책의 가장 근본적인 은유. 1차의 반박 A("서비스 계정 아니냐")·B("조직도에 올리지 마라")보다 **한 단계 깊은 기술적 반론**이다 — "서비스 계정이랑 같다"가 아니라 **"서비스 계정 모델 자체가 애초에 틀렸고 너는 그 틀린 모델을 확대하고 있다"**는 것.

**응답 전략 초안:** 사번의 기능을 **권한 부여가 아니라 귀속(attribution)으로 좁혀라.** `duncankrebs`의 로그 3항 구조(`에이전트(사용자를 대신하여, 권한 맥락을 경유하여) 행위함`)가 그 형태다. 즉 **"사번 = 권한 묶음"이 아니라 "사번 = 로그에 남는 책임 주체 식별자"**이고, 실제 권한은 과제 단위 능력 부여로 별도 관리한다(`wuweiaxin`). 이 구분을 1장에서 못 박지 않으면 보안 독자를 잃는다.

## 반박 N — 「등록소는 죽는다 — Confluence가 그랬듯이」 (등록·라이프사이클 챕터)

**근거:** GeekNews의 A2A 레지스트리 회의(`ng0301`: "실상 사용하는 레지스트리 살펴봤더니 제대로 도는거 없더라") / `esc5221`: 인벤토리 대시보드를 만들었지만 방치를 막지 못했고 **그 도구 자체도 방치됐다** / 1차의 Confluence 인용 5건(2019~2024, 거의 동일 문장) / 1차의 오프보딩 계보(2013년 불만 = 2026년 불만).

**겨누는 지점:** "에이전트를 등록소에 등록하라"는 이 책의 1보.

**왜 위험한가:** 이건 **실행 가능성 반론**이라 가장 실무적으로 아프다. 독자가 "우리 회사 Confluence 꼴 나겠네"라고 생각하는 순간 책 전체가 실패한다.

**응답 전략 초안:** **등록소를 사람이 유지하는 문서로 설계하지 마라.** §B-2의 결론을 그대로 쓰면 된다 — **폐기 절차를 만드는 대신 발급 구조에 만료를 내장한다**(`wuweiaxin`: "폐기는 일정이 아니라 과제 완료 시점에"). 등록이 **운영 경로 위에 있어야** 산다: 등록되지 않은 에이전트는 크리덴셜을 못 받는다면, 등록은 관리 업무가 아니라 **작동 조건**이 된다. 그리고 **"에이전트 등록소는 Confluence가 될 것인가"**라는 절을 명시적으로 두고 정면으로 답하라.

## 반박 O — 「에이전트를 정원으로 세면 벤더가 과금한다」 (FTE·정원 산입)

**근거:** MS의 에이전트 라이선스 논의 스레드 전체(2026-04-14) / `latand6`("디지털 좌석을 발명해 정원에 과세") / `monospaced`(SAP 간접 사용의 선례) / `poulpy123`("5분 뒤엔 회사 전체에 에이전트를 하나만 두는 도구가 나올 것") / 한국의 사비 충당 증언(`xml개발자`).

**겨누는 지점:** "에이전트에 사번과 정원을 부여한다"는 처방.

**왜 위험한가:** 이 책의 처방이 **독자의 비용을 실제로 증가시킬 수 있다.** 그리고 `poulpy123`의 지적대로, **과금 단위가 되는 순간 조직은 단위를 조작해 회피한다** — 이 책이 만든 등록 단위가 회피 대상이 된다.

**응답 전략 초안:** **등록 단위와 과금 단위를 명시적으로 분리하라.** 등록은 귀속을 위한 것이고 과금은 벤더 계약의 문제라는 것을 못 박고, **"이 책의 등록 단위를 벤더 좌석 수와 일치시키지 마라"**를 실무 규칙으로 제시하라. 그리고 §A-3의 SAP 간접 사용 계보를 밝혀 독자가 앞으로 겪을 협상을 예측하게 하라.

## 반박 P — 「자율성 등급은 이미 2단계로 충분하다」 (등급 정교화에 대한 반론)

**근거:** `ismailperim`의 제품이 실제 채택한 등급 수는 **2**다(신뢰/테스트 모드 vs 프로덕션 모드) / `farmer kweon`도 2단계다(업무용 = 제안만 / 실험용 = 풀권한) / `Quothling`의 조직은 규제(NIS2)가 상한을 정했지 등급이 정한 게 아니다.

**겨누는 지점:** 이 책이 4~5단계 자율성 등급표를 제시하는 대목.

**응답 전략 초안:** 다단계를 제안하려면 **왜 2단계로 부족한지**를 근거로 세워라. 근거가 없다면 **2단계에서 시작하고 필요할 때 쪼개는 방식**을 권하는 편이 현장 언어에 맞는다. 등급 수를 늘리는 것 자체가 §B-1의 승인 피로를 재생산할 수 있다.

## 반박 Q — 「AX가 왜 DX와 다른지 증명하지 못했다」 (책 전체의 정당성)

**근거:** `Nextgrid`: **"레거시 회사들이 수십 년째 '디지털 전환'을 이야기하면서도 단순히 서류를 디지털화하는 것 이상으로 진전하지 못하는 이유… 충분히 많은 사람이 그 서류에서 자기 일자리를 얻고 있어서, 실제 디지털 전환은 정치적으로 지탱 불가능하고 끊임없는 사보타주 때문에 실행 불가능하다."**(2026-01-24) / `deaux`: AI 감원이 성공한 곳은 기술이 좋아서가 아니라 **정치적 저항이 없는 외주 인력**이었기 때문 / 1차의 반박 I(RPA도 똑같이 시작했다) / §A-3의 RPA 계보(2020년 발주 동기 = 정원 감축, 2021년 결과 = 스파게티와 유지보수).

**겨누는 지점:** 책 전체.

**왜 위험한가:** 1차의 반박 I가 **기술적** 반복("RPA도 깨지기 쉬웠다")이었다면, 이건 **정치적** 반복이다. 그리고 정치적 반복은 기술 개선으로 극복되지 않는다.

**응답 전략 초안:** 이 반론에는 **"이번엔 다르다"로 답하지 마라. 답이 없다면 없다고 써라.** 대신 이 책이 실제로 다르게 할 수 있는 것을 제시하라 — DX는 **서류를 디지털화**했고 AX는 **책임의 귀속을 재설계**한다는 구분, 그리고 §A-4의 통찰(`aer0700`: 자동화의 이득은 시간이 아니라 **판단할 시간**)로 목표 자체를 옮기는 것. 정원 감축을 목표로 세우면 `Nextgrid`가 서술한 사보타주 구조에 그대로 들어간다.

## 반박 R — 「'AX팀을 만드는 순간 실패한다'는 명제가 이미 한국 커뮤니티에 있다」 (책의 위치)

**근거:** GeekNews 토픽 id=28341(2026-04-09)과 댓글 3건.

**겨누는 지점:** 「AX 체계 구축」이라는 제목과 기획 자체.

**응답 전략 초안:** §C-1에 쓴 대로 — **먼저 인용하고 동의를 표한 뒤 들어가라.** `snisty`의 처방("도메인 현업자가 주도하고 AX기술자가 서포트")이 이 책의 교정된 논지와 같으므로, 이 인용은 위협이 아니라 **가장 강력한 서문 재료**다. 무시하면 위협이 되고 인용하면 자산이 된다.

## 반박 S — 「지금은 운영 고통이 아니라 예방적 설계다」 (긴급성 주장을 겨눔)

**근거:** §B-3의 발견(벤더 제품 실사용 후기 0건) / §B-2의 발견(agent sprawl을 증언한 일반 실무자 0건 — 전부 벤더 발언) / §B-1의 발견(자율성 등급 개념이 2026년 코드에는 있으나 커뮤니티 토론은 없음) / 1차의 SPIFFE 이슈 댓글 한 자릿수 / 1차의 `Ram9199` 질문("자율 에이전트 인가가 지금의 운영 고통인가, 대체로 예방적 설계 작업인가").

**겨누는 지점:** 이 책이 "지금 당장 체계를 세우지 않으면 늦는다"고 말하는 대목.

**왜 위험한가:** 과장된 긴급성은 이 책을 §A-1에서 조롱당한 벤더 마케팅과 같은 범주에 넣는다. 그리고 이 책은 **다른 사람들의 과장을 비판하는 책**이므로 자기 과장이 치명적이다.

**응답 전략 초안:** **긴급성을 낮추고 선점 가치를 높여라.** "이미 난리가 났다"가 아니라 **"제품은 나왔고, 표준은 미확정이고, 도입 사례는 아직 공개되지 않았다. 그래서 지금이 설계를 결정할 수 있는 마지막 창"**이라고 쓰는 편이 증거와 일치하고 더 설득력 있다. §B-3의 세 가지 해석을 그대로 독자에게 제시하는 정직함이 오히려 신뢰를 만든다.

---

# F. 참고 스레드 전체 (URL + 게시일 + 플랫폼)

## F-1. Hacker News — 스레드(다수 인용을 뽑은 정본 스레드)

| 게시일 | 스레드 | URL | 이 문서에서의 용도 |
|---|---|---|---|
| 2024-02-29 | Klarna says its AI assistant does the work of 700 people | https://news.ycombinator.com/item?id=39548544 | A-1 / D-8 — "N명분" 주장의 최초 반응 |
| 2025-04-09 | AI coding mandates are driving developers to the brink (82점·96댓글) | https://news.ycombinator.com/item?id=43633288 | A-2·C 정본 — 강제·지표·자발 채택이 한 스레드에 |
| 2025-05-11 | Klarna changes its AI tune and again recruits humans for customer service | https://news.ycombinator.com/item?id=43955917 | A-1 — 직접 검증 경험담 |
| 2025-10-09 | McKinsey wonders how to sell AI apps with no measurable benefits (132점) | https://news.ycombinator.com/item?id=45526589 | **A-1·A-4 정본** — 절감 숫자가 만들어지는 과정 |
| 2026-04-14 | Microsoft exec suggests AI agents will need to buy licenses, just like employees (32점) | https://news.ycombinator.com/item?id=47761720 | **A-3 정본** — 라이선스 논쟁 |
| 2026-05-01 | Uber torches 2026 AI budget on Claude Code in four months (402점) | https://news.ycombinator.com/item?id=47976415 | **A-2 정본** — 토큰 지표 게이밍 |
| 2026-07-14 | Ask HN: AI Agent and harness containerization/security recommendations | https://news.ycombinator.com/item?id=48902440 | **B-1 정본** — 능력 목록형 등급 |

## F-2. Hacker News — 개별 코멘트 (스레드 단위로 파지 않은 것)

| 게시일 | 작성자 | URL | 용도 |
|---|---|---|---|
| 2017-06-28 | `empath75` | https://news.ycombinator.com/item?id=14658785 | A-4 반대 증언(보상받음) 🕒 9년 전 |
| 2019-06-16 | `ChuckNorris89` | https://news.ycombinator.com/item?id=20196593 | A-4 / D-10 🕒 7년 전 |
| 2020-05-06 | `at-fates-hands` | https://news.ycombinator.com/item?id=23094942 | A-3 RPA 종사자 증언 🕒 6년 전 |
| 2021-03-28 | `tartoran` | https://news.ycombinator.com/item?id=26607265 | A-3 UiPath 유지보수 🕒 5년 전 |
| 2022-02-15 | `Datenstrom` | https://news.ycombinator.com/item?id=30349068 | A-4 자동화 압수 🕒 4년 전 |
| 2022-02-21 | `n_time` | https://news.ycombinator.com/item?id=30413581 | A-4 정원=재무 신호 🕒 4년 전 |
| 2024-02-29 | `PheonixPharts` | https://news.ycombinator.com/item?id=39554367 | A-1 "대체가 아니라 포기" |
| 2025-06-02 | `mrweasel` | https://news.ycombinator.com/item?id=44158152 | A-1 "AI가 핑계인가" |
| 2025-07-24 | `dylan604` / `dijit` | id=44673361 / id=44672968 | A-4 반대 증언 |
| 2025-07-31 | `ta1243` | https://news.ycombinator.com/item?id=44745645 | A-4 예산 제도 |
| 2025-08-01 | `cootsnuck` | https://news.ycombinator.com/item?id=44763340 | A-1 업계 종사자 진단 |
| 2025-08-21 | `md3911027514` | https://news.ycombinator.com/item?id=44974785 | A-2 METR 찬성 |
| 2025-10-24 | `immibis` | https://news.ycombinator.com/item?id=45695816 | A-2 METR 찬성 |
| 2025-11-19 | `cjrp` | https://news.ycombinator.com/item?id=45979201 | A-1 커뮤니티 기억 |
| 2025-12-03 | `thewebguyd` / `mjr00` | id=46140811 / id=46140485 | A-4 "효율은 더 많은 일로 보상" |
| 2025-12-28 | `random9749832` | https://news.ycombinator.com/item?id=46410462 | B-3 Agentforce 방향 전환 🕒 |
| 2025-12-30 | `fancyfredbot` | https://news.ycombinator.com/item?id=46434074 | A-2 METR 침투도 |
| 2025-12-31 | `zdware` | https://news.ycombinator.com/item?id=46441281 | B-3 Agentforce 냉소 |
| 2026-01-01 | `asielen` | https://news.ycombinator.com/item?id=46451244 | B-3 경영진 데모 반응 |
| 2026-01-24 | `Nextgrid` | https://news.ycombinator.com/item?id=46741030 | **반박 Q** — DX가 20년째 안 된 이유 |
| 2026-02-12 | `timarits` | https://news.ycombinator.com/item?id=46987448 | A-3 "digital headcount" 용어 |
| 2026-02-12 | `trusera` (AI-BOM) | https://news.ycombinator.com/item?id=46988843 | B-2 미등록 AI 자산 |
| 2026-02-15 | `KronisLV` | https://news.ycombinator.com/item?id=47022979 | A-2 METR 전면 부정 |
| 2026-02-22 | `logicprog` | https://news.ycombinator.com/item?id=47114951 | **반박 K** — METR 방법론 5개항 |
| 2026-02-26 | `ej88` | https://news.ycombinator.com/item?id=47162701 | A-2 METR 후속 |
| 2026-03-03 | `duncankrebs` | https://news.ycombinator.com/item?id=47233025 | B-1 귀속 로그 3항 구조 |
| 2026-03-05 | `ismailperim` | https://news.ycombinator.com/item?id=47262082 | B-1 / **반박 P** — 2모드 등급 |
| 2026-03-08 | `fallinditch` | https://news.ycombinator.com/item?id=47297581 | A-4 "자기를 자동화하라는 명령" |
| 2026-03-12 | `wuweiaxin` | https://news.ycombinator.com/item?id=47354879 | **B-1·B-2 핵심** — 과제 단위 폐기 |
| 2026-03-16 | `toomuchtodo` | https://news.ycombinator.com/item?id=47401108 | A-1 Klarna 후일담·AI 워싱 |
| 2026-03-18 | `SAI_Peregrinus` | https://news.ycombinator.com/item?id=47420436 | B-1 직무 분리 |
| 2026-04-04 | `toomuchtodo` | https://news.ycombinator.com/item?id=47634299 | B-3 Entra Agent ID 유일 언급 |
| 2026-05-01 | `aussieguy1234` | https://news.ycombinator.com/item?id=47969973 | A-1 커뮤니티 기억 |
| 2026-06-02 | `spogbiper` | https://news.ycombinator.com/item?id=48376248 | B-3 Agent 365 마케팅 문구 |
| 2026-06-04 | `ericmcer` | https://news.ycombinator.com/item?id=48403146 | **D-5 / 반박 L** — 승인률 93% |
| 2026-06-15 | `alpineman` | https://news.ycombinator.com/item?id=48541542 | B-3 Agentforce ARR |
| 2026-06-17 | `Quothling` | https://news.ycombinator.com/item?id=48566235 | **B-3·C / D-14** — 유일한 실사용 증언 |
| 2026-08-21 | `dgellow` | https://news.ycombinator.com/item?id=49394268 | B-3 Agentforce 파트너 설문 |
| 2026-08-27 | `phoghed` | https://news.ycombinator.com/item?id=49463378 | A-1 균형 잡힌 반문 |
| 2026-09-01 | `petilon` | https://news.ycombinator.com/item?id=49529033 | A-3 per-agent pricing |

## F-3. Lobsters

| 게시일 | 스레드 / 코멘트 | URL |
|---|---|---|
| 2025-09-09 | I don't want AI agents controlling my laptop (스레드) | https://lobste.rs/s/pf12ga |
| 2025-09-09 | `gigawhitlocks` — "Run the agent with its own account" | https://lobste.rs/c/67ekwd |
| 2025-09-10 | `jfred` — **"users"는 너무 거칠다 / capability가 필요하다** (반박 M) | https://lobste.rs/c/vf4vzc |
| 2025-09-09 | `tonyarkles` — GUI 때문에 실무적으로 어렵다 | https://lobste.rs/c/j3kpfp |
| 2025-09-10 | `trigonella` — 에이전트가 스스로 권한을 줄 수 있나 | https://lobste.rs/c/kkjlhb |
| 2026-07-20 | 7 Sandbox Escape Vulnerabilities Across 4 Coding Agent Vendors (스레드) | https://lobste.rs/s/bper0d |
| 2026-07-20 | `emk` — **"승인 기반은 재앙"** | https://lobste.rs/c/lkipnx |
| 2026-07-20 | `emk` — **"보안은 환경에 속한다"** (D-6) | https://lobste.rs/c/j7ueyx |
| 2026-07-20 | `natfu` — 권한이 많을수록 유용하다는 긴장 | https://lobste.rs/c/wddr0e |
| 2026-07-20 | `emk` — 위협 모델을 먼저 정하라 | https://lobste.rs/c/bpfaiu |
| 2026-05-18 | `kornel` — 모델이 권한 제약 우회를 목표로 채택 ⚠️ **URL 미확정, 재확인 필요** | https://lobste.rs/s/ap9dum |

## F-4. GeekNews (news.hada.io)

| 게시일 | 토픽 | URL | 용도 |
|---|---|---|---|
| 2025-05-01 | **Ask GN: LLM으로 생산성이 증가한거 같은데요. 왜 저는 여전히 바쁠까요?** (13댓글) | https://news.hada.io/topic?id=20632 | **A-4 정본 / D-1** |
| 2025-05-13 | Ask GN: 방치되는 토이플젝들 어떻게 하시나요? | https://news.hada.io/topic?id=20885 | B-2 / D-11 |
| 2025-07-11 | 경험 많은 오픈소스 개발자의 생산성에 미치는 "AI의 임팩트" 측정하기 (METR) | https://news.hada.io/topic?id=21920 | ❌ **한국 사용자 댓글 0건** |
| 2025-09-07 | (GitHub Copilot 강제 활성화 관련) | https://news.hada.io/topic?id=22944 | C — "끌 수 없다"는 불만 |
| **2026-04-09** | **AX팀을 만드는 순간, 당신의 조직은 AX에 실패한다** | https://news.hada.io/topic?id=28341 | **C-1 / D-7 / 반박 R — 재확인 1순위** |
| 2026-04-28 | (GitHub Copilot 좌석→종량 과금 전환) | https://news.hada.io/topic?id=28962 | A-3 라이선스 반발 |
| **2026-05-17** | **Amazon 직원들, AI 사용 압박에 불필요한 작업을 만들어 AI 토큰 소비량을 부풀리는 중** | https://news.hada.io/topic?id=29568 | **A-2 / D-2 짝** |
| 2026-05-22 | 마이크로소프트, Claude Code 라이선스 회수 시작하다 | https://news.hada.io/topic?id=29759 | A-3 |
| 2026-03-11 | (Amazon, AI 코드 변경에 시니어 승인 의무화) | https://news.hada.io/topic?id=27395 | B-1 — 승인=책임 전가 논쟁 |
| 2026-06-10 | AI가 직원을 대체한다고 믿는 CEO는 그저 무능한 CEO일 뿐 | https://news.hada.io/topic?id=30352 | C — 자발 선택 |
| 2026-08-21 | A2A 에이전트 등록소를 통째로 받아서 세봤다: 200곳 중 응답 73곳 | https://news.hada.io/topic?id=32719 | B-2 / 반박 N ⚠️ **게시글 AI 생성 의심 — 댓글만 인용** |
| 2026-08-29 | CEO가 AI를 위해 개발팀을 해고하자, 개발자들은 오픈소스 AI CEO를 만들었다 | https://news.hada.io/topic?id=32939 | A-1 |
| 2026-08-31 | 좋은 조직문화가 AI보다 큰 생산성 향상을 만드는 이유 | https://news.hada.io/topic?id=33050 | A-2 |
| 2026-08-31 | The Agentic Awakening — 코딩이 10배 빨라져도 조직 생산성이 따라오지 않는 이유 | https://news.hada.io/topic?id=33058 | A-2 / C |
| 2026-09-02 | (AI 도구 기반 생산성과 안목) | https://news.hada.io/topic?id=33081 | A-2 인접 |
| 2025-05-29 | "개발자가 대체된다"는 유행은 왜 반복될까? | https://news.hada.io/topic?id=21150 | A-1 |
| 2025-08-22 | (AWS CEO, 주니어 대체는 가장 멍청한 발상) | https://news.hada.io/topic?id=22655 | ⚠️ **댓글 11건 존재하나 직접 인용 확보 실패** |

## F-5. OKKY

| 게시글 작성일 | 글 | URL | 용도 |
|---|---|---|---|
| 2026-05-14 | **"클로드로 하면 되잖아" 식의 업무 지시, 다른 회사도 이런가요?** | https://okky.kr/articles/1556920 | **A-2·A-4·C 정본 / D-3 짝** |
| 2026-05-19 | AI 도입에서 실행력보다 운영 원칙이 더 중요하다고 느낀 이유 | https://okky.kr/articles/1557169 | C |
| 2026-05-24 | AI 도입은 잘됐는데 조직은 더 복잡해진 경험 있으신가요? | https://okky.kr/articles/1557492 | C |
| 2026-05-29 | 회사가 클로드 엔터프라이즈로 이전했는데... (feat. 요금 폭탄) | https://okky.kr/articles/1557778 | **A-3 — 사비 충당** |
| 2026-06-05 | (NVIDIA DGX Spark 관련) | https://okky.kr/articles/1558135 | B-2 |
| 2026-06-09 | **환장의 AI 성과 측정 시스템** | https://okky.kr/articles/1558387 | **A-2 — 토큰 계측 실패** |
| 2026-06-19 | 외부 AI 사용시 보안은 어떻게 해결하나요? | https://okky.kr/articles/1559038 | A-3 / B-1 |
| 2026-07-17 | AI 믿고 해고했더니 회사들 난리 난 이유 | https://okky.kr/articles/1560743 | A-1 |
| 2026-07-31 | (AI 코드 리뷰·이해 부족) | https://okky.kr/articles/1561453 | A-4 / B-1 / C |
| **2026-08-13** | **회사 사람들이 AI를 써줬으면** | https://okky.kr/articles/1562235 | **B-1·C 정본 / D-4** |
| **2026-08-16** | **AI 사용을 점점 제한 하는 기업이 늘어날 것으로 예상 되네요** | https://okky.kr/articles/1562362 | **A-1·A-2·A-3 정본** |
| 2026-08-19 | (풀권한 운용 경험담) | https://okky.kr/articles/1562500 | B-1 |
| 2026-08-21 | 업무시 AI 사용률 몆 % 정도 되시나요? | https://okky.kr/articles/1562609 | A-2 |
| 2026-07-20 | AI 잘 쓰는 인재를 뭘 보고 평가할 것인가 | https://okky.kr/articles/1560831 | ⚠️ **댓글 3건, 실질 논쟁 없음 — 인용 가치 낮음** |
| — | (참고) 「AI 때문에 오늘 해고당함」 | https://okky.kr/articles/1549593 | ⚠️ **본문이 Reddit 번역 재게시, 한국어 댓글 0건 — 인용 금지** |

## F-6. Reddit (아카이브 API 경유 — 전부 직접 열람 미검증)

| 게시일 | 스레드/코멘트 | URL |
|---|---|---|
| 2025-05-17 | r/antiwork 「Got denied a promotion because I make it look too easy」 — `u/gummytoejam` | https://reddit.com/r/antiwork/comments/1knyu3j/got_denied_a_promotion_because_i_make_it_look_too/mss3h0i/ |
| 2025-05-14 | r/talesfromtechsupport — `u/NotYetReadyToRetire` | https://reddit.com/r/talesfromtechsupport/comments/1klzuf0/i_helped_a_user_automate_her_duties_and_in_the/ms6ttip/ |
| 2025-05-11 | r/mcp 「MCP API key management」 — `u/_greylab` | https://reddit.com/r/mcp/comments/1kjvs6x/mcp_api_key_management/mrssd4z/ |

## F-7. GitHub (참고 — 인용은 없으나 §B-1의 "비어 있음" 근거)

2026년 하반기에 **자율성 등급 개념을 구현한 이슈·PR이 다수 존재하나 거의 전부 코멘트 0~3건**이다. 대표 예:
- `dotflow-io/pycodeloop#41` 「⚙️ FEATURE: Graduated autonomy levels replacing binary dangerous=True/False」 / 2026-08-15 / 코멘트 0 / https://github.com/dotflow-io/pycodeloop/issues/41
- `aaif/wg-workflows-and-process-integration#42` 「Add Hard constraint HITL pattern and Autonomy Graduation concept」 / 2026-09-03 / 코멘트 0 / https://github.com/aaif/wg-workflows-and-process-integration/pull/42
- `tmsteph/3dvr-portal#2014` 「Autonomy Center: per-capability trust, approvals, and revoke controls」 / 2026-08-30 / 코멘트 0 / https://github.com/tmsteph/3dvr-portal/issues/2014
- `sipyourdrink-ltd/bernstein#4972` 「identity: provision and deprovision agent principals through the standard directory schema」 / 2026-09-01 / 코멘트 0 / https://github.com/sipyourdrink-ltd/bernstein/issues/4972

🕒 **2026-09-05 조회 기준.** **개념은 코드에 등장하지만 토론은 없다** — §B-1·반박 S의 근거.

---

# G. ⚠️ 미검증 사실 주장 모아보기

> 아래는 **인용은 가능하되 사실로 서술하면 안 되는 것들**이다. 책에 수치·기업명·사건을 실으려면 원 출처를 직접 확인하거나, 확인 못 하면 **"커뮤니티에서 이런 주장이 있다"**는 형태로만 써라.

## G-1. 2차 출처(원문 확인이 반드시 필요한 것) — 최우선

| 주장 | 출처 | 확인해야 할 원문 |
|---|---|---|
| **사용자가 권한 프롬프트의 약 93%를 승인** | `ericmcer` 인용 / HN id=48403146 / 2026-06-04 | **Anthropic 엔지니어링 포스트 원문.** 이 문서에서 가장 중요한 수치이므로 최우선 확인 |
| **METR 2026-02-24 후속 연구가 속도 향상을 보고** | `kalkin` / HN id=49023701 | https://metr.org/blog/2026-02-24-uplift-update/ — **반박 K의 근거이므로 필수** |
| Klarna 인력 40% 감축(2022-12~2024-12, 해고 아닌 채용동결·자연감소), CEO의 "품질 하락" 발언, 약 20명 재고용 | `toomuchtodo` 인용 / HN id=47401108 | **HBR 기사 원문** |
| 채용 관리자 59%가 "AI 때문"이라고 말하는 이유는 이해관계자에게 더 호의적으로 보이기 때문 | 동일 | **Resume.org 설문 원문** |
| Agentforce 파트너 설문(11%/56%/1/3, "수주 동인이 된 파트너 없음") | `dgellow` / HN id=49394268 / 2026-08-21 | **원 보도(매체 미확인)** |
| EU AI Act 53조가 AI 구성요소 인벤토리를 요구(2025-08) | `trusera` / HN id=46988843 | **조항 번호·시행일 미확인 — 반드시 법령 원문 대조** |
| SAP "간접 사용(indirect use)" 라이선스 관행 | `monospaced` / HN id=47762611 | **SAP 라이선스 정책 원문** |

## G-2. 익명 사내 관행·수치 주장 (검증 불가 — 경험담으로만)

| 주장 | 출처 |
|---|---|
| "우리 회사에서 사람들은 항상 인력 절감분을 축소해서 보고한다" / 경영진의 "40 FTE니까 40명 내보내자" | `thisisit` / HN id=45529408 / 2025-10-09 |
| Cerebras에서 여러 명이 토큰 리더보드용으로 이미지 픽셀을 무작위 변경 | `joshuastuden` / HN id=47978177 / 2026-05-01 |
| 어떤 CEO가 25만 달러 개발자에게 연 40~50만 달러 토큰 사용을 원한다고 발언 | `stronglikedan` / HN id=47977486 / 2026-05-01 |
| LLM 이전에는 불가능했던 수천 개 일자리를 성공적으로 자동화(외주 인력이라 가능) | `deaux` / HN id=45527568 / 2025-10-09 |
| 티어드 시크릿 모델로 오용 사례 2건 적발 | `wuweiaxin` / HN id=47354879 / 2026-03-12 |
| Claude Code + Opus 4.6로 3개 코드베이스 리팩터링을 하루에(보통 1~2주 분량) | `KronisLV` / HN id=47022979 / 2026-02-15 (본인이 "일화"라고 자인) |
| 업무의 60%를 자동화했으나 경영진이 무관심 | `u/gummytoejam` / Reddit / 2025-05-17 |
| 6개월간 매크로로 부서 전체를 자동화, 800건 보고서를 100시간에 | `u/NotYetReadyToRetire` / Reddit / 2025-05-14 — ⚠️ **r/talesfromtechsupport는 서사적 각색이 규범인 서브레딧. 일화로만.** |
| 자동화를 상사에게 보여주자 "여기서 계속 일하고 싶으면 치워" | `ChuckNorris89` / HN / 2019-06-16 (전언) |
| 자동화를 보고하자 회사가 IP를 주장하고 코드를 압수, 이후 사라짐 | `Datenstrom` / HN / 2022-02-15 (전언) |
| Agentforce ARR 12억 달러 | `alpineman` / HN id=48541542 / 2026-06-15 |
| Salesforce 백엔드 트랜잭션 최대 힙 6MB | `zdware` / HN id=46441281 / 2025-12-31 |
| NIS2 때문에 사내 에이전트에 파일시스템 접근 없음 / Copilot이 사람들을 AI에서 멀어지게 함 | `Quothling` / HN id=48566235 / 2026-06-17 |
| A2A 등록소 200곳 중 73곳만 응답 | GeekNews id=32719 게시글 / 2026-08-21 — ⚠️ **게시글 AI 생성 의심. 수치 인용 금지.** |

## G-3. 한국 커뮤니티의 익명 주장

| 주장 | 출처 |
|---|---|
| 3명 퇴사 시 1~2명만 충원하고 나머지는 AI로 메운다 | `manijang2.` / OKKY 1562362 / "20일 전" |
| 클로드 코드 총 토큰이 321억 → 재측정 시 89.2억(중복 집계) | `달고양이` / OKKY 1558387 / "3개월 전" |
| 회사가 월 20달러 한도만 지급, 부족해 사비로 10달러 추가 결제 | `xml개발자` / OKKY 1557778 / "3개월 전" |
| 기업용 요금제에는 max 플랜이 없다 | `흰꿈둘` / OKKY 1562362 / "20일 전" |
| Copilot Opus 27배율 과금 | `click` / GeekNews id=28962 / "4달전" |
| 납품업체는 매년 5% 원가절감 없으면 계약 종료 | `바람을바람` / OKKY 1556920 / "4개월 전" |
| 신입이 토큰을 가장 많이 쓴다 | `자바킬러` / OKKY 1562362 / "19일 전" |
| 사내 워크플로 자동화 운영 상태 묘사 | `BlessU` / OKKY 1561453 / "약 1개월 전" (자기 회사 자랑 톤) |

## G-4. 이해관계 있는 발언 (벤더·자기 제품 홍보)

인용은 가능하되 **문제 진술 부분만** 쓰고, 해법 주장은 쓰지 마라.
- `trusera`(AI-BOM) / `duncankrebs`(Realm) / `wuweiaxin`(OneCLI) / `ismailperim`(OnCallMate) / `u/_greylab`(Piper) / `timarits`(팟캐스트) / `cootsnuck`(음성 에이전트 구축업 — 단, 자기 사업에 불리한 방향의 발언이라 상대적으로 신뢰 가능)

## G-5. 인용 정확도 자체가 불확실한 것

- **`kornel`(Lobsters, 2026-05-18)** — 검색 결과 경유로 얻은 **생략 부호 포함 부분 인용**이며 코멘트 URL을 확정하지 못했다. https://lobste.rs/s/ap9dum 에서 재확인 전까지 **인용 금지.**
- **`[페치경유]` 표시된 모든 한국어 인용** — 페치 도구가 원문으로 제시했으나 미세 편집 가능성을 배제할 수 없다. 특히 **§C-1의 `snisty`·`wfedev`·`tsboard`(GeekNews id=28341)는 이 책의 서문 재료 후보이므로 반드시 직접 열람 후 확정하라.**
- **AWS CEO 토픽(GeekNews id=22655)** — 댓글 11건 존재를 확인했으나 페치가 요약만 반환해 **직접 인용을 확보하지 못했다.** 핸들만 기록: `minsuchae`, `zxcv123`, `onixboox`, `epdlemflaj`.

---

# H. 편향 자각 메모

## H-1. 1차 대비 편향은 실제로 개선됐다 — 그러나 다른 편향이 생겼다

**플랫폼 분포 (이 문서의 인용 기준, 대략치)**

| 플랫폼 | 1차 | 2차 | 비고 |
|---|---|---|---|
| Hacker News | ~80% | **약 45%** | 여전히 최대 소스 |
| GeekNews (한국) | 소수 | **약 22%** | 신규 대량 확보 |
| OKKY (한국) | 소수 | **약 22%** | 신규 대량 확보 |
| Lobsters | 0 | **약 7%** | 신규 |
| Reddit | **0 (차단)** | **약 3%** | 부분 우회, 여전히 사실상 실패 |
| velog·브런치·커리어리·X·Mastodon·LinkedIn | 0 | **0** | 여전히 0 |

**한국 소스가 약 44%**로 올라왔다. 1차에서 `keeda`가 지적한 "HN은 에코 챔버" 문제는 **부분적으로 해소됐다.** 그러나 아래의 새 편향들이 생겼다.

## H-2. 새로 생긴 편향 6가지 — 저자가 반드시 알아야 할 것

### ① 단일 스레드 과대 대표 (가장 심각)
이 문서의 인용이 **소수의 대형 스레드에 극단적으로 집중**돼 있다.
- §A-2의 지표 게이밍 인용 **10건 중 8건이 단일 HN 스레드**(Uber, 2026-05-01)에서 나왔다.
- §C의 영어권 인용 **7건 중 6건이 단일 스레드**(AI coding mandates, 2025-04-09)에서 나왔다.
- §A-1·A-4의 조직 인센티브 인용 **5건이 단일 스레드**(McKinsey, 2025-10-09)에서 나왔다.
- §A-4의 한국어 핵심 인용 **6건이 단일 GeekNews Ask GN**(id=20632)에서 나왔다.
- §B-1의 Lobsters 인용 **7건이 두 개 스레드**에서 나왔다.

**함의:** "커뮤니티 여론"이 아니라 **"특정 스레드에 모인 사람들의 여론"**이다. 그 스레드의 제목이 이미 프레임을 정했다("AI coding mandates are driving developers to **the brink**"). 책에 쓸 때 **"HN에서는"이 아니라 "2026년 5월 Uber 예산 스레드에서는"**처럼 좁혀 쓰는 편이 정직하다.

### ② 한국 소스는 넓어졌지만 **두 사이트**뿐이다
GeekNews와 OKKY가 한국 인용의 100%다. velog는 접근에 성공했으나 **이 주제에 대한 담론이 사실상 없었다**(TIL·튜토리얼·취업 회고가 대부분, 유효 수확 0건). 브런치·커리어리는 **클라이언트 렌더링/리다이렉트로 미조사.** 네이버 카페·지디넷 댓글도 미조사.
**함의:** "한국 개발자 커뮤니티"라고 쓰면 과장이다. **"GeekNews·OKKY 이용자"**가 정확하다. 이 두 곳은 **개발자 편향이 강하고, 이 책의 대상 독자인 "AX 실무 리더·기획자"와 겹치지 않을 수 있다.**

### ③ 이 책의 대상 독자가 이 조사에 없다
이 책은 **AX 실무 리더·기획자**를 위한 것인데, 조사한 커뮤니티는 전부 **엔지니어 커뮤니티**다. §B-3에서 확인했듯 **Entra·Okta·Workday를 실제로 운영하는 IT/보안 관리자는 HN·Lobsters·OKKY에 없다.** 그들은 사내 채널, 벤더 커뮤니티, 오프라인 사용자 모임에 있다.
**함의:** 이 문서는 **"AX 체계가 규율할 대상(엔지니어)의 목소리"는 잘 담았지만 "AX 체계를 세울 사람(리더·기획자)의 목소리는 거의 없다."** 이건 책의 균형에 직접 영향을 준다 — 이 책이 이 리서치만 근거로 쓰면 **엔지니어 편에 서서 경영진을 비판하는 책**이 되기 쉽다. 실제로 이 문서의 인용 다수가 그 톤이다(§A-1의 "관리자는 자기를 쓸모없게 만들지 않는다", §C의 "저신뢰 리더십" 등). **의도적으로 균형을 잡지 않으면 대상 독자가 자기를 공격당하는 느낌을 받는다.**

### ④ 반AI·냉소 편향
검색어 자체가 냉소를 낚는 형태였다("skepticism", "gaming", "punished", "냉소", "불만"). 그리고 HN·OKKY는 원래 회의적 정서가 우세하다. **긍정 사례를 찾는 질의도 돌렸으나 수확이 현저히 적었다**(§C-3: 3건, §A-4-③: 3건).
**함의:** "커뮤니티가 회의적이다"는 결론에는 **검색 설계의 기여분**이 있다. 이 문서에서 확보한 긍정 사례의 희소성이 **실제 희소성인지 검색 편향인지 구분되지 않는다.** 책에 "커뮤니티는 회의적이다"라고 쓸 때 이 유보를 달아야 한다.

### ⑤ 생존 편향 — 말한 사람만 남는다
§B-2에서 명확히 드러났다: **agent sprawl을 증언한 것은 전부 그 문제를 파는 벤더**다. 일반 실무자의 증언은 0건. 이건 (a) 문제가 아직 없거나, (b) 있지만 말할 유인이 없다는 뜻이다. 마찬가지로 **잘 굴러가는 조직은 글을 쓰지 않는다.** §C-3의 성공 사례가 3건뿐인 것도 이 때문일 수 있다.

### ⑥ 시점 편향 — 인용의 시간 분포가 고르지 않다
2026년 상반기(3~9월) 인용이 압도적이고, 2019~2022년 인용은 **A-3·A-4의 계보 논증용으로 의도적으로 선택된 소수**다. Reddit은 **아카이브가 2025-05에서 끊겨** 그 이후 1년 4개월치 여론이 통째로 없다.
**함의:** 이 문서는 **"2026년 상반기 영어권 개발자 포럼 + 한국 개발자 사이트의 스냅샷"**이다. 책 출간 시점에 §B-3의 "실사용 후기 0건"은 뒤집힐 수 있다 — **출간 직전 재조사 필수 항목.**

## H-3. 이 문서를 쓰면서 스스로 경계한 것

- **GN⁺ 봇 배제.** GeekNews의 AI 요약 봇 댓글을 한국 반응으로 인용했다면 **HN을 한국어로 재인용하면서 편향 개선을 자축하는** 최악의 오류가 됐을 것이다. 전량 배제했다.
- **OKKY 번역 재게시글 배제.** 본문이 Reddit 번역인 글은 본문을 인용하지 않고 댓글만 썼다.
- **AI 생성 의심 게시글 격리.** GeekNews id=32719는 댓글의 회의만 인용하고 본문 수치는 §G에 격리했다.
- **양쪽 기록.** METR 찬반, 표준화 찬반, 절감 은폐 조언과 그 반박, 강제 옹호론까지 전부 실었다. 이 책이 유리한 쪽만 인용하면 §반박 K가 그대로 이 책에 되돌아온다.

## H-4. 3차 조사가 있다면 우선순위

1. **`[페치경유]` 인용 전량 원문 대조** — 특히 GeekNews id=28341(§C-1, 서문 재료).
2. **§G-1의 2차 출처 7건 원문 확인** — 특히 승인률 93%와 METR 후속.
3. **이 책의 대상 독자(IT/보안 관리자·기획자)가 있는 곳** — 벤더 커뮤니티(Microsoft Tech Community, Okta 포럼), 한국 IT 관리자 커뮤니티, 오프라인 사용자 모임 후기. **§H-2-③이 이 문서 최대의 구조적 공백이다.**
4. **RPA 봇 FTE 환산 회고** — 커뮤니티에 없으므로 **web-researcher에 이관**(ZDNet 「RPA 도입 후 오히려 업무가 증가하는 이유」 등 확인된 단서 존재).
5. **플랫폼 엔지니어링·paved road 담론** — HN에 없으므로 **web-researcher에 이관**(PlatformCon·CNCF·컨설팅 블로그).
6. **브런치·커리어리·네이버 카페** — 이번에 미조사. 이 책 대상 독자와 더 가까울 가능성이 있다.
7. **출간 직전 재확인:** §B-3의 "실사용 후기 0건"과 §F-7의 "GitHub 토론 없음"은 **가장 빨리 낡을 발견**이다.
