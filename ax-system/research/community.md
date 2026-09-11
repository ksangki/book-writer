# 커뮤니티 리서치 — AX 체계 구축

검색 시점: **2026-09-05 기준**
장르: tech-book / 대상 독자: AX 실무 리더·기획자
슬러그: `ax-system`

> **읽는 법.** 이 문서의 인용은 전부 공개 게시물에서 가져왔고, 원문 URL·게시일·플랫폼을 함께 남겼다. 영문은 원문을 그대로 싣고 번역을 병기했다. 커뮤니티 발언은 대부분 검증 불가이므로, **정서·경험담**과 **사실 주장**을 구분해 라벨을 달았다. 사실 주장에는 `⚠️ 익명 주장 — 미검증`을 붙였고, 문서 맨 끝에 따로 모아뒀다.
>
> **접근 실패 플랫폼(중요).** Reddit은 이 리서치 환경의 크롤러 차단 대상이라 **r/sysadmin·r/devops·r/ExperiencedDevs·r/AI_Agents·r/msp 등 지정된 서브레딧 전체에 접근하지 못했다.** 축 1의 NHI 운영 고통 일화, 축 4의 주니어 직무 불안 증언은 원래 Reddit이 최대 광맥인데 그 광맥을 통째로 못 팠다. 대신 Hacker News(댓글 단위 전수 검색), GitHub Issues/PR(MCP·A2A·SPIFFE 스펙 논쟁), Lobsters, GeekNews, OKKY, velog로 보충했다. 각 축 끝의 커버리지 단락에 무엇이 비어 있는지 정직하게 적었다.

---

## 축 1 — 에이전트 등록의 현장 (예산 35%)

### 1-1. 통증(pain point)

#### **① "비인간 아이덴티티"는 새 개념이 아니라 옛 고통의 새 이름이다 — 그리고 그 옛 고통이 아직 안 풀렸다**

OWASP가 「Non-Human Identities Top 10」을 내놓자 HN에서 가장 먼저 나온 반응은 환영이 아니라 **명명(naming)에 대한 냉소**였다.

- 원문 인용: **"Wtf? We have been calling these workload identities for years"**
  - 번역: "뭐야? 우리 이거 몇 년째 workload identity라고 불러왔는데."
  - 출처: Hacker News / "OWASP Non-Human Identities Top 10" / 댓글 작성자 `zingababba` / https://news.ycombinator.com/item?id=42928645 / 2025-02-04
  - 검증 상태: 정서·경험담

- 원문 인용: **"service accounts are not bots"**
  - 번역: "서비스 계정은 봇이 아니다."
  - 출처: Hacker News / 같은 스레드 / 작성자 `xg15` / https://news.ycombinator.com/item?id=42928645 / 2025-02-04
  - 검증 상태: 정서

- 같은 스레드에서 `xarope`(2025-02-04)는 OWASP 문서가 결국 나열하는 게 "service accounts and access keys… API keys, tokens, encryption keys, and certificates"뿐이라며, **새로운 개념이 아니라 리브랜딩 아니냐**는 취지로 지적했다. `ALLTaken`(2025-02-04)도 NHI가 "특수한 케이스나 공격 벡터인지, 아니면 기존 서비스 계정 관행과 같은 것인지" 용어 자체를 되물었다.
  - 출처: Hacker News / https://news.ycombinator.com/item?id=42928645 / 2025-02-04
  - 검증 상태: 정서

> **책에서 쓸 지점.** 이 책이 "에이전트를 조직에 등록한다"고 말하는 순간, 보안·인프라 실무자의 첫 반응은 **"그거 서비스 계정 아니냐"** 다. 이건 가상의 반론이 아니라 실제로 가장 먼저 나온 반응이다. 1장이나 등록 챕터의 오프닝은 이 냉소를 먼저 인정하고 들어가는 게 맞다.

#### **② 정체성 관리는 "감사가 길고 지겹다" — 여기에 차원을 하나 더 얹는 문제**

- 원문 인용: **"Identities are very hard to manage and secure overall. Audits are super long, tedious."**
  - 번역: "정체성 관리와 보안은 전반적으로 아주 어렵다. 감사는 지독하게 길고 지겹다."
  - 이어서 이 작성자는, 지금도 부실한 기존 접근권한 리뷰에 NHI 차원까지 얹으면 "extremely tricky"해질 거라고 했다.
  - 출처: Hacker News / "OWASP Non-Human Identities Top 10" / 작성자 `batmansmk` / https://news.ycombinator.com/item?id=42928645 / 2025-02-04
  - 검증 상태: 경험담

- 원문 인용(요지): Vault 같은 도구를 써도 서비스 계정과 API 키의 유출·오용 문제를 **"still don't *fully* solve"** 한다.
  - 출처: Hacker News / 같은 스레드 / 작성자 `antithesis-nl` / https://news.ycombinator.com/item?id=42928645 / 2025-02-04
  - 검증 상태: 경험담

#### **③ 사람 이름이 붙은 자동화 — 그 사람이 나가면 무슨 일이 벌어지나**

이 책의 "소유자·매니저를 지정한다"는 주장에 정확히 꽂히는 통증이다.

- 원문 인용: **"So every time we fire or lay off the person whose name is on the automation, we need to rotate the keys?"**
  - 번역: "그러면 자동화에 이름이 걸린 사람을 해고하거나 정리할 때마다 키를 로테이션해야 한다는 거야?"
  - 출처: Hacker News / "You don't want long-lived keys" / 작성자 `collabs` / https://news.ycombinator.com/item?id=47898675 / 2026-04-25
  - 검증 상태: 경험담

- 원문 인용: **"I just wish instead of having a password which gets shared around via 1password, there were a clear permission list"**
  - 번역: "1Password로 돌려 쓰는 비밀번호 대신, 명확한 권한 목록이 있었으면 좋겠다."
  - 출처: Hacker News / "You don't want long-lived keys" / 작성자 `theamk` / https://news.ycombinator.com/item?id=47898958 / 2026-04-25
  - 검증 상태: 정서·경험담

- 계정 난립 쪽: **"I've seen startups that require a dozen service accounts just to run the software"**
  - 번역: "소프트웨어 하나 돌리는 데 서비스 계정 열두 개가 필요한 스타트업을 봤다."
  - 출처: Hacker News / "The bespoke software revolution? I'm not buying it" / 작성자 `perrygeo` / https://news.ycombinator.com/item?id=47462076 / 2026-03-20
  - 검증 상태: ⚠️ 익명 주장(구체 수치 "a dozen") — 미검증 / 정서로는 유효

#### **④ 오프보딩: 만들기는 쉽고 지우기는 아무도 안 한다**

- 원문 인용: **"making offboarding a lot easier... the main pain point, as opposed to onboarding"**
  - 번역: "오프보딩을 훨씬 쉽게 만드는 것 — 온보딩이 아니라 그쪽이 진짜 통증 지점이다."
  - 출처: Hacker News / "Ask HN: How do you manage passwords in teams?" / 작성자 `olegp` / https://news.ycombinator.com/item?id=6507980 / **2013-10-07**
  - 🕒 **신선도 주의:** 13년 전 글이다. 그런데 아래 2026년 사례가 같은 말을 한다는 게 요점이다.
  - 검증 상태: 경험담

- 원문 인용: **"after firing everyone they of course didn't follow the off boarding process"**
  - 번역: "전원 해고하고 나서, 당연하게도 오프보딩 절차는 안 지켰다."
  - 맥락: 인수 이후 해고당한 뒤에도 1년 넘게 JIRA 접근 권한이 살아 있었다는 이야기.
  - 출처: Hacker News / "Delve – Fake Compliance as a Service" / 작성자 `madaxe_again` / https://news.ycombinator.com/item?id=47462193 / 2026-03-20
  - 검증 상태: ⚠️ 익명 주장(특정 회사 관련 사건) — 미검증 / 경험담으로는 강력

- 원문 인용: **"No device inventory and off boarding process?"**
  - 번역: "장비 인벤토리도 오프보딩 절차도 없다는 거야?"
  - 출처: Hacker News / "Apple says more ex-employees may have taken confidential data to OpenAI" / 작성자 `crimsonnoodle58` / https://news.ycombinator.com/item?id=49176003 / 2026-08-04
  - 검증 상태: 정서(제3자 사건에 대한 반응)

- 원문 인용: **"They failed to lock out users of the previous system long after they left"**
  - 번역: "떠난 지 한참 지난 사용자들을 이전 시스템에서 차단하지 못했다."
  - 출처: Hacker News / "Cardinals Face F.B.I. Inquiry in Hacking of Astros' Network" / 작성자 `netik` / https://news.ycombinator.com/item?id=9727792 / **2015-06-16**
  - 🕒 11년 전 사건. **오프보딩 실패가 실제 침해로 이어진 고전 사례**로 인용 가치가 있으나, 시점을 반드시 밝혀야 한다.
  - 검증 상태: 정서 + 공개 보도 사건에 대한 언급

> **책에서 쓸 지점.** 오프보딩 챕터 오프닝은 "2013년의 불만과 2026년의 불만이 같은 문장"이라는 구도로 열 수 있다. 13년 동안 안 풀린 문제를 에이전트가 수십 배로 증폭시킨다는 게 이 책의 논거가 된다.

#### **⑤ 감사 로그: 에이전트가 한 일과 사람이 한 일이 구분되지 않는다**

이건 이 책의 핵심 주장(사번·소유자·매니저)이 실제로 해결하려는 문제다. **MCP 스펙 논쟁에서 정면으로 다뤄지고 있다.**

- MCP 스펙 SEP-2817 「AI Invocation Audit Context in Request `_meta`」(2026-05-29 개설, 29개 코멘트)는 요청 메타데이터에 `invocationReason`(왜 이 호출을 했는가), `model`(어떤 모델이 만들었는가), `userIntent`(어떤 사용자 의도에서 비롯됐는가), `turnId`(같은 사용자 턴 묶기)를 싣자는 제안이다.
  - 출처: GitHub / modelcontextprotocol/modelcontextprotocol PR #2817 / 제안자 `hangum` / https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2817 / 2026-05-29 개설
  - 🕒 **버전 민감:** 2026-09-05 기준 **open(미확정)** 상태. 책에 쓸 때 "제안 단계"임을 명시할 것.

- 이 논쟁의 핵심 문장 — 원문 인용: **"`invocationReason`, `userIntent` and `turnId` are client-asserted, so a host can record them but can't prove them. They describe intent, not what executed."**
  - 번역: "`invocationReason`, `userIntent`, `turnId`는 클라이언트가 스스로 주장하는 값이다. 호스트는 기록은 할 수 있어도 증명은 못 한다. 그건 의도를 서술할 뿐, 실제로 무엇이 실행됐는지가 아니다."
  - 출처: GitHub / 같은 PR / 작성자 `vaaraio` / https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2817 / 2026-05-29
  - 검증 상태: 스펙 설계 논거(공개 기술 논의)

- 이어지는 결론 — 원문 인용: **"Client-asserted context with no signed execution record is unverifiable. A signed execution record with no intent context is hard to interpret."**
  - 번역: "서명된 실행 기록 없는 클라이언트 주장 맥락은 검증 불가능하다. 의도 맥락 없는 서명된 실행 기록은 해석하기 어렵다."
  - 출처: 동일 / `vaaraio` / 2026-05-29
  - 검증 상태: 스펙 설계 논거

- 또 다른 구현자 `XuebinMa`(2026-05-30)는 자기 구현(agent-guard)에서 이 필드들이 **정책 판단 단계에는 절대 도달하지 못하게 파이프라인 자체로 막았다**고 설명했다. 원문 인용: **"'`invocationReason`/`userIntent` are not authorization evidence' isn't a doc promise here — it's enforced by which pipeline stage can see them."**
  - 번역: "'`invocationReason`/`userIntent`는 인가 근거가 아니다'라는 건 여기선 문서상의 약속이 아니라, 어느 파이프라인 단계가 그 값을 볼 수 있느냐로 강제된다."
  - 출처: https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2817 / 2026-05-30
  - 검증 상태: 구현자 증언

- HN에서도 같은 문제의식이 나온다 — `troupo`(2026-05-30, "MCP is dead?" 스레드)는 사람 계정과 자동화 계정을 **"differentiate these two accounts and audit log their activity"** 하는 건 1950년대부터 있던 일이라고 지적했다. 즉 **기술적으로 새롭지 않지만 조직적으로는 결정적**이라는 것.
  - 출처: Hacker News / https://news.ycombinator.com/item?id=48335321 / 2026-05-30
  - 검증 상태: 정서

- 실제 도구를 만든 쪽의 진단 — `cracadumi`(2026-04-19)는 "어떤 에이전트가 / 어떤 크리덴셜을 / 언제 접근했는가"를 추적하려면 귀속(attribution) 인프라가 필요한데 **대부분의 볼트에 그게 없다**고 했고, 자기 시스템은 "every request, approval, and credential fetch is in an append-only audit log"라고 설명했다.
  - 출처: Hacker News / "Show HN: AgentKey – Access governance for AI agents" / https://news.ycombinator.com/item?id=47822065 / 2026-04-19
  - 검증 상태: 벤더 자기 주장(이해관계 있음) — 문제 진술 부분만 인용 권장

#### **⑥ 에이전트에게 크리덴셜을 주는 순간 생기는 문제들 (Kontext CLI 스레드, 2026-04-14)**

「Kontext CLI – Credential broker for AI coding agents」(70점, 17댓글)는 **에이전트 전용 크리덴셜**이라는 이 책의 주제에 가장 근접한 공개 토론이다.

- 원문 인용: **"What prevents the agent from persisting or leaking the API key - or reading it from the environment?"** — `e12e`
  - 번역: "에이전트가 API 키를 어딘가에 저장하거나 유출하는 걸, 혹은 환경변수에서 읽어가는 걸 뭐가 막지?"
- 원문 인용: **"What if kontext runs under the same user as Claude? Could it in principle inspect the kontext process and extract the key from memory?"** — `sjdv1982`
  - 번역: "kontext가 Claude와 같은 사용자로 돌면? 원리적으로 kontext 프로세스를 들여다보고 메모리에서 키를 꺼낼 수 있는 거 아냐?"
- 설계 원칙에 대한 지지 — 원문 인용: **"This is how keychains should be designed. Never return the secret, but mint a new token, or sign a request."** — `zimbatm`
  - 번역: "키체인은 이렇게 설계돼야 한다. 시크릿을 절대 돌려주지 말고, 새 토큰을 발행하거나 요청에 서명하라."
- 출처: Hacker News / https://news.ycombinator.com/item?id=47765374 / 2026-04-14
- 검증 상태: 정서·설계 논거

### 1-2. 회의론·반박 (이 책의 주장에 대한 반대 논거)

#### **반박 A — "그거 서비스 계정에 마케팅 이름 붙인 것 아니냐"**
가장 강한 반박이고, 실제로 존재한다. 위 1-1-① 인용 3건(`zingababba`, `xg15`, `xarope`)이 근거다. 이 책은 **"사번을 준다"가 서비스 계정과 어떻게 다른지**를 1장 안에서 답하지 못하면, 보안·인프라 독자를 첫 챕터에서 잃는다.
- 출처: https://news.ycombinator.com/item?id=42928645 / 2025-02-04 / Hacker News

#### **반박 B — "에이전트를 조직도에 올리지 마라" (실제 경험자의 경고)**

이건 이 책의 주장에 정면으로 부딪히는, **직접 해본 사람의 후회담**이다.

- 원문 인용: **"I went through the entire investor arc in about a day and a half. From the hopeful optimism of hiring a CEO, to watching the org chart explode, to complete disillusionment, to demoting the CEO back to a regular worker..."**
  - 번역: "하루 반 만에 투자자 서사를 통째로 겪었다. CEO를 고용하는 희망찬 낙관에서 시작해, 조직도가 폭발하는 걸 지켜보고, 완전한 환멸에 이르렀다가, 결국 CEO를 평사원으로 강등시켰다…"
  - 맥락: 멀티 에이전트 구성에서 에이전트에게 조직적 권한을 넓게 주자 **역할이 20개로 불어나고 실제 산출물 대신 메타 작업을 우선하기 시작**했다는 이야기.
  - 출처: Hacker News / "Multi-agent Claude Code setup – 3 roles, Markdown coordination, Docker" / 작성자 `yego` / https://news.ycombinator.com/item?id=47245374 / 2026-03-04
  - 검증 상태: 경험담 (개인 실험 규모, 기업 사례 아님)

- 더 짧고 더 아픈 한 줄 — 원문 인용: **"Pretty pleaser please people don't get your agents registered as direct-reports in the org-chart with HR!"**
  - 번역: "제발 부탁인데 여러분, 에이전트를 HR 조직도에 직속 부하로 등록하지는 맙시다!"
  - 출처: Hacker News / "Grep beats LSP? Why coding agents ignore your fancier tools" / 작성자 `polotics` / https://news.ycombinator.com/item?id=49561918 / **2026-09-04 (검색 하루 전)**
  - 검증 상태: 정서(반농담)

> **책에서 쓸 지점.** 이 두 인용은 이 책이 반드시 응답해야 할 반론이다. 특히 `yego`의 "조직도가 폭발했다"는 **조직 은유를 에이전트에 적용했을 때의 구체적 실패 모드**다. 이 책이 "사번을 준다"고 할 때, 그것이 *권한과 책임의 귀속*을 뜻하지 *조직 놀이(org-chart cosplay)*를 뜻하지 않는다는 걸 명시적으로 갈라줘야 한다.

#### **반박 C — "누가 검증자를 검증하나" (에이전트 아이덴티티 표준의 미해결 지점)**

A2A 프로토콜의 「Proposal: Agent Identity Verification for Agent Cards」(#1672, 2026-03-22 개설, **658개 코멘트**)는 에이전트에 검증 가능한 신원을 붙이자는 제안이다. 여기서 반복해서 걸린 지점:

- 원문 인용: **"agent-to-agent communication across organizations hits a trust root question: who verifies the v[erifier]"** — `vessenes`
  - 번역: "조직 경계를 넘는 에이전트 간 통신은 신뢰 루트 문제에 부딪힌다: 누가 검증자를 검증하나."
  - 출처: GitHub / https://github.com/a2aproject/A2A/issues/1672 / 2026-03-23
- 원문 인용: **"'self-sovereign' without a trust layer can slide into 'self-asserted' - a `did:key` proves key control, not identity claims."** — `desiorac`
  - 번역: "신뢰 계층 없는 '자기주권'은 '자기 주장'으로 미끄러질 수 있다 — `did:key`는 키 통제를 증명할 뿐, 신원 주장을 증명하지 않는다."
  - 출처: 동일 / 2026-03-28
- 원문 인용: **"An Agent Card today is a static JSON document. Anyone who intercepts it can modify the claims before forwarding it, and the receiving agent has no way to detect the tampering."** — `jagmarques`
  - 번역: "오늘의 Agent Card는 정적 JSON 문서다. 중간에 가로챈 누구든 전달 전에 주장을 고칠 수 있고, 수신 에이전트는 변조를 탐지할 방법이 없다."
  - 출처: 동일 / 2026-04-12
- 🕒 **버전 민감:** 2026-09-05 기준 **open(미확정)**. 제안이지 표준이 아니다.
- ⚠️ **출처 품질 경고:** 이 스레드는 658개 코멘트 중 상당수가 **자기 프로젝트를 홍보하는 계정들의 교차 게시**로 보이고, 문체가 균질해 AI 생성 의심 정황이 있다. 그래서 "커뮤니티 여론"의 근거로는 쓰지 말고, **설계 쟁점이 무엇인지**를 보여주는 자료로만 쓰기를 권한다.

#### **반박 D — "AI 사원"이라는 프레이밍 자체에 대한 거부**

- 크리덴셜을 서버에 맡기는 모델에 대한 즉각 거부 — 원문 인용: **"Kontext holds secrets server-side... That probably makes this thing DOA for most people (certainly for me and everyone I know)."** — `james-clef`
  - 번역: "Kontext는 시크릿을 서버 쪽에 들고 있다… 그건 대부분의 사람에게 이 물건을 도착 즉시 사망(DOA) 상태로 만든다 (적어도 나와 내가 아는 모두에게는)."
  - 출처: Hacker News / https://news.ycombinator.com/item?id=47765374 / 2026-04-14
  - 검증 상태: 정서
  - **책에서 쓸 지점:** "중앙 등록소를 세운다"는 이 책의 처방에 대한 실무자의 본능적 거부 반응. 중앙화가 왜 필요한지 설득하지 못하면 이 반응이 기본값이다.

- 「Ask HN: What are the BIGGEST Problems you'd face with a full-AI employee?」(2025-07-28)에서 나온 답들은 **성능이 아니라 거버넌스**였다.
  - 질문자 `dontoni`가 스스로 나열한 통증에 이미 **"Create an account"**, **"I will have to manage secrets and api keys"** 가 들어 있다. (번역: "계정을 만들어야 한다", "시크릿과 API 키를 관리해야 한다")
  - `Aurornis`(2025-07-28): **"If the company is breached, all companies using their employees are breached"** (번역: "그 회사가 침해당하면, 그 회사의 '직원'을 쓰는 모든 회사가 침해당한다")
  - `dontoni`: **"the major biggest problem is vendor lock-in"** (번역: "가장 큰 문제는 벤더 종속이다")
  - 출처: Hacker News / https://news.ycombinator.com/item?id=44709844 / 2025-07-28
  - 검증 상태: 정서·설계 논거
  - ⚠️ 참고: 이 스레드는 10점·5댓글로 규모가 작다. "커뮤니티 정서"로 일반화하지 말고 개별 관점으로 인용할 것.

#### **반박 E — 감사·라이선스·관리 부담**
`Quothling`(2026-09-01)은 Entra 그룹 기반 RBAC를 유지하는 관리 부담, HR 데이터 연동의 복잡성, 지속적인 유지보수 비용을 지적했다.
- 출처: Hacker News / "AI Can Make You Suck Faster Too" / https://news.ycombinator.com/item?id=49519776 / 2026-09-01
- 검증 상태: 경험담
- **책에서 쓸 지점:** "에이전트마다 소유자·매니저를 지정한다"는 처방은 곧 **HR 데이터와 IAM 그룹을 계속 동기화하는 운영 비용**을 뜻한다. 이 비용을 숨기면 안 된다.

### 1-3. 현장에서 통한 것 (field-tested heuristics)

1. **시크릿을 돌려주지 말고, 토큰을 발행하거나 요청에 서명하라.**
   - 원문: "Never return the secret, but mint a new token, or sign a request." — `zimbatm`
   - 출처: HN / https://news.ycombinator.com/item?id=47765374 / 2026-04-14

2. **폭발 반경(blast radius)과 도달 범위(reach)는 다른 문제다 — 따로 풀어라.**
   - 원문: "sandbox the agent so it can't touch anything you care about, then route egress through a policy layer" — `coder-pm`
   - 번역: "에이전트를 샌드박스에 넣어 중요한 건 못 건드리게 하고, 그다음 나가는 트래픽을 정책 계층으로 라우팅하라."
   - 출처: HN / Launch HN: OneCLI / https://news.ycombinator.com/item?id=49363710 / 2026-08-21

3. **승인은 호스트가 아니라 요청 자체에 바인딩하라.**
   - 원문: 규칙 매칭이 "method + path + body, not only the host" 기준이어야 한다 — OneCLI 저자 `Jonathanfishner`
   - 출처: HN / https://news.ycombinator.com/item?id=49363710 / 2026-08-19

4. **런타임에 실제로 건드린 것과 정책이 허용한 것을 diff 할 수 있어야 한다.**
   - 원문: "can I diff what an agent was actually allowed to touch at run time against what the policy said" — `ericmaciver`
   - 출처: HN / https://news.ycombinator.com/item?id=49363710 / 2026-08-21
   - **이 책의 "등록"이 실효를 가지려면 필요한 검증 루프.**

5. **단발 주입 테스트는 부족하다 — 각 단계가 전부 허용된 상태에서 전체가 위험해지는 경우를 놓친다.**
   - 원문: "single-turn injection suites miss the case where every individual step is permitted" — `SaurabhKumbhar`
   - 출처: HN / https://news.ycombinator.com/item?id=49363710 / 2026-08-22

6. **정책 판단 단계와 감사 기록 단계를 물리적으로 분리하라.** 에이전트가 자기 입으로 말한 의도(`userIntent`)가 인가 판단에 절대 닿지 못하게 파이프라인 구조로 막는다. (`XuebinMa`의 agent-guard 구현, 위 1-1-⑤)

7. **워크로드가 이미 가진 자격증명을 재사용하고, 새 시크릿을 만들지 마라.**
   - MCP SEP-1933 「Workload Identity Federation」의 설계 의도: **"the goal of the spec is to let workloads use existing credentials (think Kubernetes PSAT tokens, SPIFFE JWTs) so that deployments don't have to further proliferate client secrets if they have better options available."** — `PieterKas`
   - 번역: "스펙의 목표는 워크로드가 이미 가진 자격증명(쿠버네티스 PSAT 토큰, SPIFFE JWT 같은 것)을 쓰게 해서, 더 나은 선택지가 있는데도 클라이언트 시크릿을 더 늘리지 않게 하는 것이다."
   - 출처: GitHub / https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1933 / 2025-12-17
   - 🕒 2026-09-05 기준 open. 40개 코멘트.
   - **책에서 쓸 지점:** 이 책의 "사번 발급"과 **긴장 관계**에 있는 접근이다. 한쪽은 "에이전트마다 새 신원을 만들어 등록하라", 다른 쪽은 "새 신원을 만들지 말고 런타임이 이미 주는 신원을 쓰라". 이 긴장을 다루면 책의 깊이가 생긴다.

8. **사람 없는 상황(non-interactive)의 인가는 아직 표준이 없다 — 현장은 자체 해법으로 때우고 있다.**
   - 12개 MCP 서버를 프로덕션에서 돌린다는 개발자의 필드 리포트: **"There is no user in the loop (agents act autonomously) / There is no central identity provider / The OAuth 2.1 flow assumes a user-agent redirect, but agents do not have browsers"**
   - 번역: "루프에 사용자가 없다(에이전트가 자율 동작). 중앙 아이덴티티 공급자가 없다. OAuth 2.1 플로우는 user-agent 리다이렉트를 전제하는데, 에이전트에는 브라우저가 없다."
   - 결국 **"a simple HMAC-SHA256 file-based token exchange"** 로 자체 해결했다고 밝혔다.
   - 출처: GitHub / modelcontextprotocol #2902 「MCP Authorization in Non-Browser, Non-User-Interactive Scenarios — Field Report from 12 Production Servers」 / 작성자 `guangda88` / https://github.com/modelcontextprotocol/modelcontextprotocol/issues/2902 / 2026-06-10 (2026-09-05 기준 closed)
   - ⚠️ 익명 주장(12개 서버 프로덕션 운영) — 미검증. 본인이 "solo developer, not a company"라고 밝힘.

9. **"실제 사고가 있었나, 아니면 예방적 설계인가"를 먼저 물어라.**
   - 같은 이슈에서 `Ram9199`(2026-06-13)가 던진 질문이 이 책의 취재 질문으로도 좋다: 잘못된 에이전트가 툴을 호출했는지, 토큰 권한이 과했는지, **귀속이 안 됐는지(missing attribution)**, 수동 정리가 필요했는지 — 그리고 그 뒤 무엇을 바꿨는지(HMAC 토큰 / 별도 크리덴셜 / 툴 비활성화 / 감사 로그 / 정책 / 아무것도 안 함).
   - 원문 인용: **"Trying to determine whether autonomous-agent authorization is current operational pain or mostly anticipatory design work."**
   - 번역: "자율 에이전트 인가가 지금의 운영 고통인지, 대체로 예방적 설계 작업인지 판단해보려는 것이다."
   - 출처: https://github.com/modelcontextprotocol/modelcontextprotocol/issues/2902 / 2026-06-13
   - **책에서 쓸 지점:** 이 질문에 정직하게 답하는 게 이 책의 신뢰도를 좌우한다. 2026년 9월 현재, 커뮤니티 증거로 볼 때 답은 **"둘 다이되, 아직은 예방적 설계 쪽이 크다"** 에 가깝다.

10. **표준 스펙 쪽의 현재 좌표(2026-09-05 기준, 전부 미확정 open).**
    - MCP: SEP-1933 워크로드 아이덴티티 페더레이션(40댓글), SEP-2817 AI 호출 감사 컨텍스트(29), SEP-2787 툴 호출 어테스테이션(33), SEP-2385 툴 인증 매니페스트(23), SEP-2643 구조화된 인가 거부(6), SEP-2848 비동기 툴 승인(6), #3337 엔터프라이즈 감사/컴플라이언스 스코프 제안(2026-09-01 개설)
    - A2A: #1672 Agent Card 신원 검증(658), #1575 신원·위임·집행 구현(98), #1850 A2A Identity Trust Framework 로드맵(47), #1937 위임 권한 컨텍스트 바인딩 프로파일(5)
    - SPIFFE: #382 「Proposal: SPIFFE IDs for AI Agent Workloads」(2026-03-26, 3댓글), #383 「JWT-SVID claim for model identity in AI workloads」(2026-03-31, 0댓글), #408 「JWT-SVID Support Delegated (Actor) Identity」(2026-06-27, 2댓글)
    - 🕒 **이 목록 자체가 신선도 자산이자 부채다.** 책 출간 시점에 재확인 필요. SPIFFE 쪽 댓글 수가 한 자릿수라는 사실은 **"업계 표준이 이미 정해졌다"고 쓰면 안 된다**는 신호다.
    - 출처: GitHub API 검색, 2026-09-05 조회

### 축 1 커버리지

**확보한 것**
- NHI/서비스 계정 용어 자체에 대한 실무자 냉소 (HN, 인용 4건)
- 소유자 불명·키 로테이션·공유 비밀번호의 구체적 고통 (HN, 2026년 인용 3건)
- 오프보딩 실패 일화 (HN, 2013·2015·2026년 각 시점 인용 4건)
- 감사 로그에서 에이전트/사람 구분 문제 — **MCP 스펙 논쟁의 1차 사료로 확보** (SEP-2817, 실무 구현자 증언 포함)
- 에이전트에게 크리덴셜 주는 것에 대한 구체적 공격 시나리오 (Kontext CLI 스레드)
- **"에이전트를 조직도에 올렸다가 후회한" 직접 경험담** — 이 책 주장에 대한 가장 강한 반박 (yego, 2026-03-04)
- 에이전트 아이덴티티 표준의 미해결 쟁점 (A2A #1672, MCP #2902, SPIFFE #382/383/408)

**비어 있는 것**
- **Reddit 전체 (r/sysadmin, r/devops, r/cybersecurity, r/ITManagers, r/msp) — 크롤러 차단으로 접근 불가.** "이 계정 누가 만들었는지 아무도 모름" 류의 날것 일화는 이쪽이 최대 광맥인데 통째로 비었다. 대체 확보한 HN 인용으로 부분 보완했으나 **밀도가 낮다.**
- **Microsoft Entra Agent ID / Okta / Auth0 for AI Agents 발표에 달린 HN·Reddit·Lobsters 댓글 — 사실상 확보 실패.** HN Algolia에 해당 제품 발표의 유의미한 토론 스레드(댓글 다수)가 없었다. Entra Agent ID 관련해서는 2026-04 Silverfort 연구진(Noa Ariel, Yoav S)이 보고한 Agent ID Administrator 역할 권한 상승 취약점 **보도**는 있으나(thehackernews.com, cybersecuritynews.com, hackread.com), **커뮤니티 토론이 아니다.** 축 1의 "실제로 써본 사람의 후기"는 **비어 있다.**
- **라이선스 비용 우려의 직접 인용 — 확보 실패.** "에이전트마다 라이선스를 사야 하냐"는 실무 반응을 찾지 못했다.
- **"AI 직원" 마케팅에 대한 LinkedIn·X 냉소 — 확보 실패.** X/Mastodon/LinkedIn 공개 포스트에 접근하지 못했다. HN에서 "AI employee"로 검색하면 나오는 것은 거의 전부 **Show HN 제품 홍보**(2024~2026, 대부분 1~3점·댓글 0)이고, 냉소를 담은 토론 스레드가 아니다. 다만 **"AI employee"를 표방하는 Show HN이 2년간 20건 넘게 올라오고 거의 전부 무반응(1~3점)이었다**는 사실 자체가 냉소의 간접 증거로는 쓸 만하다.
- Discord/Slack 공개 로그 — 미접근.

---

## 축 2 — SOP·절차의 현장 (예산 20%)

### 2-1. 통증(pain point)

#### **① "Confluence는 문서가 죽으러 가는 곳" — 7년간 반복된 같은 문장**

이 정서는 **여러 사람이 서로 다른 스레드에서 거의 동일한 문장으로** 말했다는 점에서 특히 강력하다.

- 원문 인용: **"Confluence is where documentation goes to die. And then rot."**
  - 번역: "Confluence는 문서가 죽으러 가는 곳이다. 그리고 썩는다."
  - 출처: Hacker News / "Ask HN: What's the worst piece of software you use everyday?" / 작성자 `EdwardDiego` / https://news.ycombinator.com/item?id=23808854 / **2020-07-12**
- 원문 인용: **"Confluence is where documentation goes to die."** — `morkalork`
  - 출처: Hacker News / "I Fucking Hate Jira (2022)" / https://news.ycombinator.com/item?id=39375258 / **2024-02-14**
- 같은 문장을 쓴 다른 사례:
  - `GordonS` / "Atlassian Acquires AgileCraft for $166M" / https://news.ycombinator.com/item?id=19429182 / **2019-03-19** — 검색이 쓸모없고 탐색이 어렵다는 지적과 함께
  - `more_corn` / "Ask HN: Software you hate but can't replace?" / https://news.ycombinator.com/item?id=30233639 / **2022-02-06** — "absolute garbage"라는 표현과 함께
  - `stock_toaster` / "What I learned after managing a small team for 2 years" / https://news.ycombinator.com/item?id=37167982 / **2023-08-17** — 느린 속도와 부실한 검색 지적
- 검증 상태: 정서 (반복 패턴으로서 매우 강함)
- 🕒 2019~2024년에 걸친 인용이다. 시점을 밝히고 쓸 것.

> **책에서 쓸 지점.** "SOP에서 출발하자"는 이 책의 1보에 대해 독자가 떠올릴 이미지가 바로 **죽은 Confluence 페이지**다. 이 다섯 개 인용은 그 정서가 **한 사람의 짜증이 아니라 7년간 여러 사람이 같은 문장으로 반복한 업계 상식**임을 증명한다. SOP 챕터의 오프닝 소재로 이보다 나은 걸 찾기 어렵다.

한국 커뮤니티에서도 같은 결의 지적이 있다.
- GeekNews 「스타트업을 위한 셀프 호스팅 Wiki 설정 방법」(topic id=17832) 논의에서: 검토를 거친 공식 문서 버전이 있는데 다음 버전을 작업하려면 **별도 작업용 페이지를 만들어야 하고, 그 결과 검색 결과가 오염되고 금방 지저분해진다**는 지적.
  - 출처: GeekNews / https://news.hada.io/topic?id=17832
  - 검증 상태: 정서
- GeekNews 「Docmost」(topic id=15610) 논의에서: Confluence가 너무 느려 **"Confluence 기다리는 중"이 관용구가 될 정도**였다는 증언.
  - 출처: GeekNews / https://news.hada.io/topic?id=15610
  - ⚠️ 익명 주장(특정 기업 사내 관용구) — 미검증
- 🕒 게시일이 상대 표기("N달전")로만 노출돼 정확한 날짜를 확정하지 못했다. 인용 시 "GeekNews 해당 토픽, 2026-09-05 조회"로 표기 권장.

#### **② 런북은 "보통 통하는 것"만 알려준다 — 보통이 아닐 때는 말해주지 않는다**

- 원문 인용: **"A runbook can tell you what usually works, but it cannot tell you when the situation is no longer 'usual.'"**
  - 번역: "런북은 보통 무엇이 통하는지는 알려줄 수 있지만, 언제부터 상황이 더 이상 '보통'이 아닌지는 알려주지 못한다."
  - 출처: Hacker News / "The West forgot how to make things, now it's forgetting how to code" / 작성자 `flashdesk` / https://news.ycombinator.com/item?id=47918548 / 2026-04-27
  - 검증 상태: 정서·경험 기반 통찰
  - **책에서 쓸 지점:** SOP를 에이전트에 주는 이 책의 설계에 대한 **가장 우아한 형태의 반론**. "절차를 코드화하면 된다"에 대한 답이 필요하다.

#### **③ AI가 문서를 쓰기 시작하면서 생긴 새로운 부패**

이건 2026년에 새로 생긴 통증이고, 이 책이 반드시 다뤄야 할 지점이다.

- 원문 인용: **"When I get an LLM-generated doc or runbook, my first thought is that its very possible that I'm the first person who has ever read this."**
  - 번역: "LLM이 만든 문서나 런북을 받으면, 첫 생각은 '내가 이걸 읽은 최초의 인간일 가능성이 꽤 높다'는 것이다."
  - 출처: Hacker News / "As AI eats the web, the internet's collective memory is disappearing" / 작성자 `backlava12` / https://news.ycombinator.com/item?id=49258726 / 2026-08-11
  - 검증 상태: 정서
  - **책에서 쓸 지점:** 최고의 챕터 오프닝 후보 중 하나. **쓰기는 공짜가 되고 읽기는 희소해졌다**는 역전. SOP를 AI로 대량 생성하려는 독자에게 정확히 필요한 경고다.

- 원문 인용: **"1-shotting documentation with AI is a bad idea. You then have to have multiple verification passes to have any chance of it being worth anything."**
  - 번역: "AI로 문서를 원샷으로 뽑는 건 나쁜 생각이다. 그러고 나면 그게 조금이라도 값어치를 가지려면 여러 번의 검증 패스를 거쳐야 한다."
  - 출처: Hacker News / 작성자 `tcoff91` / https://news.ycombinator.com/item?id=49009276 / 2026-07-22
  - 검증 상태: 경험담

#### **④ 긴 규칙 파일은 지켜지지 않는다 — 그리고 2026년엔 오히려 해롭다는 주장까지**

이 책이 "에이전트에게 SOP를 준다"고 할 때 가장 실무적으로 아픈 반박이다.

- 원문 인용(요지): 최신 모델(GPT-5.6 계열)에서는 상세한 AGENTS.md 지시가 **"redundant at best and frequently actively harmful"** 하다.
  - 번역: "잘해야 불필요하고, 자주 적극적으로 해롭다."
  - 출처: Hacker News / "Debian votes to allow 'responsible use of generative AI'" / 작성자 `nick__m` / https://news.ycombinator.com/item?id=49491488 / 2026-08-29
  - 검증 상태: ⚠️ 익명 주장(특정 모델 버전의 동작) — 미검증
- `Topfi`(2026-08-29, 같은 스레드)는 모델 5.2 무렵부터 AGENTS.md 사용을 그만뒀다며, MCP 툴과 함께 **"useless context bloat"** 를 만든다고 의심한다고 했다. 자체 평가 데이터상 성능을 향상시키기보다 제한했다는 것.
  - 출처: https://news.ycombinator.com/item?id=49491618 / 2026-08-29
  - 검증 상태: ⚠️ 익명 주장(자체 평가 결과) — 미검증
- 근본적 회의 — `reacharavindh`(2026-08-29): 모델이 외부 컨텍스트 파일을 **진짜로 쓰는지, 아니면 준수하는 시늉만 하는지** 확인할 방법이 없다는 지적.
  - 출처: https://news.ycombinator.com/item?id=49491148 / 2026-08-29
  - 검증 상태: 정서
- 조용한 실패 — `anotherCodder`(2026-02-12): **"Claude Code doesn't validate it - it just silently ignores the skill."**
  - 번역: "Claude Code는 그걸 검증하지 않는다 — 그냥 조용히 스킬을 무시한다."
  - 출처: Hacker News / "Show HN: Agnix – lint your AI agent configs" / https://news.ycombinator.com/item?id=46983893 / 2026-02-12
  - 검증 상태: 경험담
  - **책에서 쓸 지점:** "절차를 주면 따른다"는 가정이 **조용히** 깨진다. 감사·검증 루프가 없으면 SOP 배포는 착시다.

#### **⑤ RPA가 왜 기대만큼 안 됐는가 — 현장 회고**

- 원문 인용(요지): 기존 RPA는 **"too brittle"** 하고 유지보수 부담이 **대체하려던 노동보다 커지는 경우가 많았다.**
  - 출처: Hacker News / "You can't solve computer use by ignoring the interface" / 작성자 `euphetar` / https://news.ycombinator.com/item?id=49110493 / 2026-07-30
  - 검증 상태: 경험 기반 회고
  - **책에서 쓸 지점:** RPA 챕터의 핵심 문장. **유지보수 비용 > 절감된 노동**이라는 손익 역전이 RPA 실패의 구조다. 이 책의 "에이전트 등록"이 같은 함정을 피하려면, 등록·소유·감사에 드는 운영 비용을 처음부터 계산에 넣어야 한다.
- `cowartc`(2026-04-16)는 런타임 에이전트가 **깨지기 쉽고 감사하기 어렵다(fragile and difficult to audit)** 는 자기 판단이 직장에서 겪은 RPA 경험으로 강화됐다고 했다.
  - 출처: Hacker News / "Show HN: Libretto – Making AI browser automations deterministic" / https://news.ycombinator.com/item?id=47792235 / 2026-04-16
- `muchael`(2026-04-17)은 RPA 스크립트 경험 끝에 팀이 **결정론적 코드 기반 접근 + 의도적 AI 통합**으로 갔지 완전 자동화로는 가지 않았다고 했다.
  - 출처: https://news.ycombinator.com/item?id=47807714 / 2026-04-17
  - 검증 상태: 경험담

### 2-2. 회의론·반박

#### **반박 F — "SOP에서 출발한다"는 전제가 이미 죽은 자산 위에 서 있다**
근거: 2-1-①의 Confluence 인용 5건 + GeekNews 한국 사례 2건. 이 책이 "우리 회사엔 이미 SOP가 있다"고 전제하면, 독자의 실제 SOP는 **아무도 읽지 않고 이미 낡은 문서**일 확률이 높다. 책은 "SOP를 만들자"가 아니라 **"살아 있는 SOP만이 재료가 된다"** 는 조건을 먼저 세워야 한다.

#### **반박 G — 절차의 코드화는 예외를 못 다룬다**
근거: `flashdesk`의 "런북은 언제 보통이 아닌지는 말해주지 않는다" (2026-04-27).

#### **반박 H — 긴 규칙 파일은 무시되거나, 심지어 성능을 떨어뜨린다**
근거: `nick__m`, `Topfi`, `reacharavindh`, `anotherCodder` (2026-02 ~ 2026-08). 이 책이 "SOP를 에이전트에 준다"고 할 때 **분량과 형식**에 대한 처방이 없으면 반박당한다.

#### **반박 I — RPA도 똑같이 시작했다**
근거: `euphetar`, `cowartc`, `muchael` (2026-04 ~ 2026-07). **"이번엔 다르다"를 증명할 책임이 이 책에 있다.**

### 2-3. 현장에서 통한 것 (field-tested heuristics)

1. **적을수록 낫다 — 시스템 프롬프트를 80% 이상 걷어냈다는 보고.**
   - 원문: "We removed over 80% of Claude Code's system prompt for more advanced models" — `hbarka`
   - 출처: Hacker News / "The new rules of context engineering" / https://news.ycombinator.com/item?id=49063459 / 2026-07-26
   - ⚠️ 익명 주장(구체 수치 80%) — 미검증

2. **한 덩어리로 주지 말고 "X 할 때는 Y를 참조하라" 패턴으로 쪼개라.**
   - 원문: "adding my personal coding heuristics to my AGENTS.md and referencing subdocuments on a 'when doing X, consult Y' pattern" — `boorang`
   - 출처: HN / "Terminal-Bench-Science" / https://news.ycombinator.com/item?id=49474177 / 2026-08-28
   - **책에서 쓸 지점:** SOP를 에이전트에 주는 구체적 설계 패턴. 통짜 문서가 아니라 **점진적 공개(progressive disclosure)**.

3. **점진적 공개가 제대로 작동하게 하려면 큰 지시 덩어리를 분할해야 한다.**
   - `mirekrusin` / https://news.ycombinator.com/item?id=49532425 / 2026-09-02

4. **규칙 파일도 부패한다 — 주기적으로 걷어내라.**
   - `jpalomaki`(2026-08-20): 오래된 AGENTS.md에 낡은 규칙이 쌓이면 최신 모델을 **혼란시키므로 주기적 정리가 필요**하다.
   - 출처: https://news.ycombinator.com/item?id=49369002 / 2026-08-20
   - **책에서 쓸 지점:** SOP 부패는 사람만의 문제가 아니라 **에이전트 컨텍스트에서도 동일하게 발생**한다. 이 책의 SOP 라이프사이클 설계에 직접 반영할 것.

5. **추상적 정의 말고 짧은 명령형으로 쓰라.**
   - `clickety_clack`(2026-09-02): "always follow TDD" 같은 간결한 지시가 학술적 정의보다 낫다.
   - 출처: HN / "AI Coding Agent Skills for Real Engineers" / https://news.ycombinator.com/item?id=49530746 / 2026-09-02

6. **프롬프트 길이가 아니라 검증을 늘려라.**
   - 원문: "95% is running the verification deterministically" — `lazarie`
   - 번역: "95%는 검증을 결정론적으로 돌리는 것이다."
   - 출처: HN / "Managing AI Coding Costs at Scale" / https://news.ycombinator.com/item?id=49221134 / 2026-08-08
   - **책에서 쓸 지점:** "SOP를 준다"보다 "SOP 준수를 어떻게 확인하는가"가 본체라는 뜻. 이 책의 등록·감사 논리와 직결된다.

7. **모델이 바뀌면 기존 하네스가 깨진다.**
   - `shostack`(2026-08-05): 잘 돌던 지시가 새 모델에서 무시된다. 원문 인용: **"New models are like 'thank you for your suggestion...it's irrelevant. Now let me overspend your token budget.'"**
   - 번역: "새 모델은 이런 식이다. '제안 감사합니다… 그런데 그건 무관합니다. 이제 당신 토큰 예산을 초과 지출하겠습니다.'"
   - 출처: HN / "Building an Advanced Agentic Harness" / https://news.ycombinator.com/item?id=49184005 / 2026-08-05
   - **책에서 쓸 지점:** 에이전트 SOP는 **버전 고정과 회귀 테스트가 필요한 자산**이라는 논거.

8. **잘 관리된 규칙 파일은 여전히 메모리보다 낫다는 반대 증언도 있다.**
   - `nzach`(2026-08-31): 잘 유지된 AGENTS.md가 메모리 기능을 켜는 것보다 **거의 항상 더 나은 결과**를 냈다.
   - 출처: HN / "Agent memory as a file format" / https://news.ycombinator.com/item?id=49510061 / 2026-08-31
   - **양쪽 다 기록해둔다 — 이 논쟁은 아직 안 끝났다.**

9. **런북을 "실행 가능한 문서"로 만드는 흐름.** Atuin Desktop처럼 "문서처럼 보이지만 터미널처럼 실행되는" 로컬 우선 런북 편집기가 등장했다. 셸 명령·DB 쿼리·HTTP 요청을 한 곳에 두고 반복 운영 절차를 공유 가능한 워크플로로 바꾼다.
   - 출처: GeekNews / 「Atuin Desktop: 실행 가능한 Runbooks」 / https://news.hada.io/topic?id=20489 / **2025-04-23** / 원문 https://blog.atuin.sh/atuin-desktop-runbooks-that-run/
   - **책에서 쓸 지점:** "SOP → 에이전트 절차"의 중간 단계로 **실행 가능한 런북**이 이미 존재한다. 이 책의 진화 서사(문서 → 실행 가능 런북 → 에이전트 SOP)에 실물 근거를 준다.

### 축 2 커버리지

**확보한 것**
- SOP·문서 냉소의 **인용 가능한 원문** — 5개 독립 스레드, 2019~2024년, 거의 동일 문장 (요청받은 핵심 항목)
- 한국 커뮤니티의 같은 정서 (GeekNews 2건)
- 런북의 구조적 한계에 대한 우아한 반박 1건 (2026-04)
- AI 생성 문서의 새로운 부패 양상 2건 (2026-07, 2026-08) — **2026년 신규 통증**
- 긴 규칙 파일 회의론 4건 + 반대 증언 1건 (2026-02 ~ 2026-08)
- 컨텍스트 엔지니어링 실전 휴리스틱 7건 (전부 2026년)
- RPA 현장 회고 3건 (2026-04 ~ 2026-07)
- 실행 가능한 런북 사례 1건 (2025-04)

**비어 있는 것**
- **SRE 커뮤니티의 런북 문화 심층 논의 — 얕다.** "runbooks that rot", runbook automation을 정면으로 다룬 장문 토론을 확보하지 못했다. Google SRE Book 관련 HN 스레드까지는 못 갔다.
- **r/sysadmin·r/devops의 런북 논의 — 접근 불가.**
- **RPA 실무자 회고의 밀도가 낮다.** HN에는 RPA 경험자가 적다. 이 주제는 링크드인·컨설팅 블로그 쪽에 몰려 있는데, 그건 커뮤니티가 아니라 웹 리서치 담당 영역이다. **web-researcher에 이관 권장.**
- **MCP 툴 정의 설계 팁 — 확보 실패.** 툴 description 작성법에 대한 구체적 커뮤니티 노하우를 찾지 못했다.
- **한국 커뮤니티의 SOP/런북 논의 — 매우 얕다.** OKKY·velog에서 SOP·런북 주제의 실무 토론을 찾지 못했다.
- 프로세스 마이닝 경험자 목소리 — 비어 있음.

---

## 축 3 — 바텀업 → 탑다운: 현장의 온도 (예산 20%)

### 3-1. 통증(pain point)

#### **① 파일럿은 되는데 프로덕션이 안 되는 이유 — MIT 95% 스레드 (230점·167댓글)**

「95% of generative AI pilots at companies are failing – MIT report」는 이 책의 문제의식과 정확히 겹치는 스레드다.
- 출처: Hacker News / https://news.ycombinator.com/item?id=44941118 / **2025-08-18** / 원문 fortune.com

현장 진단으로 나온 것들:

- 원문 인용: **"LLMs get you 80% of the way... but that last 20%... is a complete tar pit and will wreck adoption"**
  - 번역: "LLM은 80%까지는 데려다준다… 그런데 마지막 20%는 완전한 타르 구덩이고 도입을 망가뜨린다."
  - 특히 커스터마이징 없는 범용 벤더 래퍼에서 그렇다는 지적.
  - 출처: 작성자 `morkalork` / https://news.ycombinator.com/item?id=44941118 / 2025-08-18
  - 검증 상태: 경험 기반 진단

- 데이터 준비 문제 — 원문 인용: **"documents are strewn about on random network drives and are not formatted similarly"**
  - 번역: "문서들이 아무 네트워크 드라이브에나 흩어져 있고 포맷도 제각각이다."
  - 이 상태에서 시도한 RAG는 **"a disaster"** 였고, 격리된 Gemini 인스턴스에서만 성과가 있다가 이후 환각이 늘었다고.
  - 출처: 작성자 `amirkabbara` / 같은 스레드 / 2025-08-18
  - 검증 상태: 경험담
  - **책에서 쓸 지점:** 이 책이 "SOP에서 출발한다"고 말하는 근거가 여기 있다. **실패의 원인이 모델이 아니라 절차·문서의 상태**라는 현장 증언.

- 조직 요인 — `mike_hearn`(2025-08-18): 실패의 원인으로 **무엇을 원하는지 스스로 모르는 것(not really knowing what they want)**, 생산성 향상을 측정하지 못하는 것, 그리고 사람을 AI로 완전 대체했다가 다시 채용하는 경영 판단을 들었다.
  - 출처: 같은 스레드 / 2025-08-18
  - 검증 상태: 정서·진단

#### **② 그 95% 통계 자체에 대한 반박 — 이 책이 그 숫자를 쓰려면 알아야 할 것**

- `layer8`(2025-08-18)은 방법론을 문제 삼았다. 표본이 **"300 public AI deployments"** 이고 비공개 프로젝트는 빠졌다는 점, 그리고 낮은 곳에 달린 열매를 AI 없이도 해결했을 가능성을 지적하며 **"AI wasn't the key to success?"** 라고 되물었다.
  - 출처: https://news.ycombinator.com/item?id=44941118 / 2025-08-18
  - 검증 상태: 방법론 비판(정서)

- `RaftPeople`(2025-08-18)은 **"실패"의 정의 문제**를 짚었다. SAP 도입 통계에서도 그랬듯 "실패"란 대개 **예산·일정 초과**를 뜻하지 실제로 작동하지 않는다는 뜻이 아니며, 진짜로 취소되거나 망가진 채 오픈한 프로젝트는 훨씬 적다는 것.
  - 출처: 같은 스레드 / 2025-08-18
  - 검증 상태: 경험 기반 반박
  - **책에서 쓸 지점: 이 책이 MIT 95%를 인용한다면 반드시 이 두 반박을 함께 실어야 한다.** 숫자를 그대로 쓰면 정보에 밝은 독자에게 신뢰를 잃는다.

- 🕒 **신선도 주의:** 이 논쟁은 2025년 8월이다. 2026-09-05 현재로부터 1년 전. 책에서 "최근 화제가 된"이 아니라 **"2025년 8월"** 로 명시할 것.

#### **③ shadow AI — 회사가 막으면 개인 계정으로 쓴다**

- 원문 인용: **"Shadow AI is obviously the number one security threat right now, especially in enterprise"** — `Quothling`
  - 번역: "shadow AI는 지금 명백히 최우선 보안 위협이다. 특히 엔터프라이즈에서."
  - 출처: Hacker News / https://news.ycombinator.com/item?id=48655348 / 2026-06-24
  - 검증 상태: 정서
- 원문 인용: **"Shadow AI [is] bigger than Shadow IT ever was in 2000s"** — `veunes`
  - 번역: "shadow AI는 2000년대의 shadow IT보다 크다."
  - 출처: https://news.ycombinator.com/item?id=46854187 / 2026-02-02
  - 검증 상태: ⚠️ 익명 비교 주장 — 미검증
- 원문 인용: **"Shadow AI economy: people using personal LLM subscriptions instead of internal offerings"** — `chriskanan`
  - 번역: "shadow AI 경제: 사람들이 내부 제공물 대신 개인 LLM 구독을 쓴다."
  - 출처: https://news.ycombinator.com/item?id=44978793 / 2025-08-21
- 원문 인용: **"How hard it is to get people to use official corporate tools instead of shadow AI?"** — `pbronez`
  - 번역: "shadow AI 말고 공식 사내 도구를 쓰게 만드는 게 얼마나 어려운가?"
  - 출처: https://news.ycombinator.com/item?id=46136275 / 2025-12-03
  - **책에서 쓸 지점:** 이 책의 "탑다운 체계"가 마주할 실제 저항의 형태. 금지가 아니라 **공식 경로가 개인 경로보다 나아야** 한다는 설계 조건.
- 탐지하는 쪽의 언어 — `volker48`(2026-07-01, Who is hiring 스레드): **"Big current focus is shadow AI, i.e. catching when employees paste sensitive data into ChatGPT"**
  - 번역: "지금 큰 초점은 shadow AI, 즉 직원이 민감 데이터를 ChatGPT에 붙여넣는 걸 잡아내는 것."
  - 출처: https://news.ycombinator.com/item?id=48754582 / 2026-07-01
  - **책에서 쓸 지점:** 이 문장은 축 4와 직결된다. **"잡아낸다(catching)"** 는 단어가 직원에게 어떻게 들릴지가 변화관리의 핵심이다.
- ⚠️ **주의:** shadow AI 사용률 관련 수치(90%, 65%, 30%, "median org uses 28 AI apps" 등)가 HN 댓글에 여러 개 돌아다니지만 전부 **2차 인용**이다. 아래 미검증 섹션에 따로 모아뒀다. **책에 쓰려면 원 출처를 fact-checker가 직접 확인해야 한다.**

#### **④ 한국 맥락 — 회사가 지원을 안 해서 개인이 구독한다**

- 원문 인용: **"일단 회사에서 AI 서비스를 지원 거의 안해주네요. 개인별로 쓰는건 개인이 하라고 하고(회사에서 쓰려고 개인이 AI 서비스 구독 ㅜ) 팀에는 클로드 프로?월 3만원짜리 지원하고 끝."**
  - 출처: GeekNews / 「모두가 AI를 가져도 회사는 여전히 아무것도 배우지 못할 때」 / 작성자 `akapwhd` / https://news.hada.io/topic?id=29217 / 게시 "4달전"(2026-09-05 조회 기준 대략 2026-05경)
  - 검증 상태: 경험담
  - **책에서 쓸 지점: 이 책의 한국 독자에게 가장 실감나는 한 줄.** 탑다운 체계를 말하기 전에, 현실은 **개인이 사비로 구독하고 있다**는 데서 출발해야 한다.

- 같은 스레드, 원문 인용: **"AI를 '잘쓰는법'을 어떻게 다뤄야 하는지는 다들 갈팡질팡하고 있는 것 같네요."**
  - 출처: 작성자 `kallare` / https://news.hada.io/topic?id=29217
  - 검증 상태: 정서
  - **책에서 쓸 지점:** 이 책의 존재 이유를 한 줄로 요약해주는 독자 목소리. 서문 후보.

- 같은 스레드의 GN⁺ 요약(HN 의견 인용): **"대기업 환경에서는 AI 도입이 개발팀 밖으로 거의 나가지 못했고, 배포되지 않은 코드는 자산이 아니라 부채임"**
  - 출처: https://news.hada.io/topic?id=29217
  - 검증 상태: 2차 인용 — 원 HN 댓글 미확인

- 관련 원문 글의 진단(GeekNews 요약): 기존 변화관리 방식인 **커뮤니티·챔피언 네트워크·데모·설문·대시보드**는 실제 업무 중 생기는 AI 활용의 맥락·실패·검증·사람의 개입을 담기 어렵다.
  - 출처: GeekNews / https://news.hada.io/topic?id=29217 / 원문 https://www.robert-glaser.de/when-everyone-has-ai-and-the-company-still-learns-nothing/
  - **책에서 쓸 지점:** 축 4 변화관리 챕터의 이론적 뼈대와 직결. 다만 이건 커뮤니티 발언이 아니라 **원문 글의 주장**이므로 web-researcher 쪽 사료로 넘기는 게 정확하다.

- 한국 특수성에 대한 강한 주장 — OKKY 「한국이 AI로 개발자 대체가 빠르게 진행될 수밖에 없는 이유」
  - 원문 인용: **"한국 기업은 '속도'와 '비용절감'을 가장 큰 의사결정의 기준으로 삼습니다."**, **"이는 AI가 가장 먼저 대체할 수 있는 구조입니다."**
  - 근거로 든 것: SI 중심 구조, 다단계 하청, 극단적 효율성 추구, 빠른 신기술 도입, 노동시장 유연성
  - 출처: OKKY / 작성자 `yh8332` / https://okky.kr/articles/1532084 / 게시 "1년 이상 전"(정확한 날짜 미확인)
  - 검증 상태: ⚠️ 익명 주장(구조적 일반화, "ChatGPT 유료 사용률 세계 상위권" 포함) — **미검증**. 정서로는 한국 개발자 커뮤니티의 불안을 잘 보여준다.
  - 🕒 1년 이상 전 게시물. 인용 시 시점 명시 필수.

### 3-2. 회의론·반박 — **탑다운 강제 도입에 대한 반발** 【이 책의 가장 위험한 지점】

요청받은 대로 이 영역을 집중 확보했다. **양이 많고 감정이 강하다.**

- 원문 인용: **"now he's implementing an AI mandate for every employee, replete with tracking and metrics and the threat of being fired"**
  - 번역: "이제 그는 전 직원 AI 의무화를 시행하고 있다. 추적과 지표, 그리고 해고 위협까지 완비해서."
  - 출처: Hacker News / "Why are executives enamored with AI, but ICs aren't?" / 작성자 `bitwize` / https://news.ycombinator.com/item?id=47552106 / 2026-03-28
  - 검증 상태: ⚠️ 익명 주장(자기 회사 CEO의 정책) — 미검증 / 정서로는 매우 강함

- 원문 인용: **"mandates happened and now I'm being forced to use them. Absolutely no guidance from leadership though."**
  - 번역: "의무화가 내려왔고 이제 나는 그걸 쓰도록 강요당한다. 그런데 리더십의 가이드는 전혀 없다."
  - 출처: Hacker News / "Seventeen Years of Coding and Starting Over" / 작성자 `ares623` / https://news.ycombinator.com/item?id=47279806 / 2026-03-06
  - 검증 상태: 경험담
  - **책에서 쓸 지점: 이 책의 1순위 독자가 막아야 할 실패 모드가 이 한 문장에 다 있다.** 명령은 내려오고 가이드는 없다. 이 책의 존재 이유.

- 원문 인용: **"usage of ai is not just allowed or encouraged but mandated. And is part of their performance score"**
  - 번역: "AI 사용이 허용·권장을 넘어 의무화돼 있다. 그리고 성과 점수의 일부다."
  - 출처: Hacker News / "I'm 60 years old. Claude Code killed a passion" / 작성자 `axegon_` / https://news.ycombinator.com/item?id=47387307 / 2026-03-15
  - 검증 상태: ⚠️ 익명 주장(제3자 회사 정책) — 미검증

- 원문 인용: **"my company forced us to use their AI tooling"** — 완료해야 할 필수 쿼리 수까지 지정됐다는 증언.
  - 출처: Hacker News / "AI can't stop making up software dependencies and sabotaging everything" / 작성자 `stego-tech` / https://news.ycombinator.com/item?id=43665422 / 2025-04-12
  - 검증 상태: ⚠️ 익명 주장 — 미검증

- 원문 인용: **"VP right now saying everyone must use AI every day"** — 기본 설치된 AI 브라우저 애드온 언급과 함께.
  - 출처: Hacker News / "At Amazon, some coders say their jobs have begun to resemble warehouse work" / 작성자 `placardloop` / https://news.ycombinator.com/item?id=44090429 / 2025-05-25
  - 검증 상태: ⚠️ 익명 주장(특정 기업 내부 정책) — 미검증

- 원문 인용: **"everyone was forced to use Microsoft's AI tools whether they worked or not"**
  - 번역: "작동하든 말든 모두가 마이크로소프트의 AI 도구를 쓰도록 강요당했다."
  - 출처: Hacker News / "Everyone in Seattle hates AI" / 작성자 `mips_avatar` / https://news.ycombinator.com/item?id=46138952 / 2025-12-03
  - 검증 상태: ⚠️ 익명 주장(특정 기업) — 미검증

- 원문 인용: **"not tying ratings/comp to AI usage (seriously how fucking stupid are they over in Redmond?)"**
  - 번역: "평가·보상을 AI 사용량에 묶지 않는 것 (진짜 레드먼드 쪽 사람들 얼마나 멍청한 거야?)"
  - 출처: Hacker News / "Everyone in Seattle hates AI" / 작성자 `caconym_` / https://news.ycombinator.com/item?id=46138952 / 2025-12-03
  - 검증 상태: 정서 (매우 날것)

- 원문 인용: **"Microsoft...will simply PIP you for being a luddite if you aren't meeting usage metrics"**
  - 번역: "마이크로소프트는… 사용량 지표를 못 맞추면 러다이트라는 이유로 그냥 PIP(성과개선계획)를 걸 것이다."
  - 출처: Hacker News / "The new skill in AI is not prompting" / 작성자 `klardotsh` / https://news.ycombinator.com/item?id=44430973 / 2025-07-01
  - 검증 상태: ⚠️ 익명 주장 — 미검증

- 지표 게이밍 — `plaguuuuuu`(2026-06-28): AI 의무화가 **지표 게이밍**을 유발하며, 준수해 보이려고 사용량 비용을 인위적으로 부풀린다는 증언.
  - 출처: Hacker News / "Ford AI hiccups push carmaker to rehire 'gray beard' inspectors" / https://news.ycombinator.com/item?id=48704828 / 2026-06-28
  - 검증 상태: 경험담

- 한국 커뮤니티도 같은 지적 — 원문 인용: **"AI 사용량 자체를 성과 지표로 삼으면 사람들은 필요하지 않은 작업에도 AI를 사용해 숫자를 맞추게 될 수 있음"**
  - 출처: GeekNews / 「좋은 조직문화가 AI보다 큰 생산성 향상을 만드는 이유」 / 작성자 `brainer` / https://news.hada.io/topic?id=33050 / 게시 "5일전"(2026-09-05 조회 기준 대략 2026-08-31)
  - 검증 상태: 정서·예측
  - **책에서 쓸 지점: 한국 독자용 인용으로 최적.** 탑다운 KPI의 실패 메커니즘을 한 문장으로 요약.

- 품질 하락 — `rk06`(2026-08-25): **"thanks to AI mandate, quality is going downhill a lot faster"** (번역: "AI 의무화 덕분에 품질이 훨씬 빠르게 내려가고 있다")
  - 출처: https://news.ycombinator.com/item?id=49433354 / 2026-08-25
  - 검증 상태: 정서

- 조용한 해고 수단이라는 해석 — `keeda`(2025-12-03): AI 의무화가 **"quiet fire people"** 수단으로 쓰이며, 교육과 실험할 시간을 주지 않는다는 지적.
  - 출처: Hacker News / "Everyone in Seattle hates AI" / https://news.ycombinator.com/item?id=46140813 / 2025-12-03
  - 검증 상태: 해석·정서

- **역방향 강제의 사례** — `tdeck`(2026-03-29): "We believe everyone can be more productive with an SD-based workflow"라는 식으로 **기능적으로 맞지 않는 팀에까지 획일적 워크플로를 강제**해 반감을 샀다는 사례.
  - 출처: https://news.ycombinator.com/item?id=47549649 (스레드) / 2026-03-29
  - **책에서 쓸 지점:** 탑다운 체계의 실패 모드는 "강제" 자체가 아니라 **맥락 무시한 획일화**라는 더 정밀한 진단.

#### **반대편 목소리도 반드시 기록 — 이 책의 주장을 지지하는 쪽**

- `keeda`(2026-03-28): HN의 반AI 정서가 대표성이 없다는 반박. 원문 인용: **"AI adoption is up to 80-90%; ICs absolutely are enamored with AI too. HN...is largely an echo chamber"**
  - 번역: "AI 도입률은 80~90%에 이른다. IC들도 분명히 AI에 매료돼 있다. HN은… 대체로 에코 챔버다."
  - 출처: https://news.ycombinator.com/item?id=47549649 / 2026-03-28
  - 검증 상태: ⚠️ 익명 주장(80~90% 수치) — 미검증
  - **책에서 쓸 지점: 이 리서치 문서 전체에 대한 메타 경고이기도 하다.** HN·Reddit은 AI 회의론이 과대표되는 곳이다. 이 문서의 축 3·4 인용을 "업계 전반의 정서"로 일반화하면 안 된다. **오케스트레이터와 저술가에게 이 경고를 반드시 전달할 것.**

- `Aperocky`(2026-03-27): 자발적 도입이 잘 된 경우의 목소리. 원문 인용: **"my implementation speed used to be a bottleneck...and now only thoughts and idea are the limit"**
  - 번역: "예전엔 구현 속도가 병목이었는데… 이제는 생각과 아이디어만이 한계다."
  - 출처: https://news.ycombinator.com/item?id=47549649 / 2026-03-27

### 축 3 커버리지

**확보한 것**
- MIT 95% 스레드 원문 + **그 숫자에 대한 방법론 반박 2건** (요청 항목 충족, 2025-08)
- 파일럿이 프로덕션으로 못 가는 현장 진단 3건 (2025-08)
- shadow AI 증언 6건 (2025-08 ~ 2026-07), 탐지하는 쪽 언어 포함
- **탑다운 강제 도입 반발 — 11건 확보 (요청받은 최우선 항목).** 2025-04 ~ 2026-08에 걸쳐 있고, 감정 강도가 높다.
- 지표 게이밍 증언 2건 (HN·GeekNews, 한국 인용 확보)
- **반대편(탑다운 옹호·에코챔버 경고) 2건** — 균형 유지에 필수
- 한국 맥락 3건 (GeekNews 2, OKKY 1)

**비어 있는 것**
- **"보안팀에서 막혔다" / "예산이 안 나왔다" 유형의 구체적 증언 — 확보 실패.** 여러 검색 조합을 시도했으나 HN 댓글에서 조달·법무·벤더 심사 단계 좌초 증언을 찾지 못했다. 이 영역은 Reddit(r/ITManagers, r/msp)과 링크드인이 주 무대인데 둘 다 접근 못 했다. **축 3에서 가장 큰 공백.**
- "PoC 지옥"이라는 표현 자체를 쓰는 한국 커뮤니티 글 — 확보 실패.
- MIT 95% 통계에 대한 **한국 커뮤니티** 반응 — 확보 실패.
- shadow AI 관련 IT 부서의 대응 방식(차단 우회 탐지, 정책 설계)에 대한 실무 노하우 — 얕다.

---

## 축 4 — 변화관리: 사람의 목소리 (예산 25%) 【이 책의 온도를 만드는 축】

### 4-1. 통증(pain point)

#### **① AI 도입을 감시로 느낀 순간**

- 원문 인용: **"all your prompts are tracked and easily viewable by whoever oversees it at your company"**
  - 번역: "당신의 프롬프트는 전부 추적되고, 회사에서 그걸 관리하는 누구든 쉽게 들여다볼 수 있다."
  - 출처: Hacker News / "Why are executives enamored with AI, but ICs aren't?" / 작성자 `smrtinsert` / https://news.ycombinator.com/item?id=47549649 / 2026-03-29
  - 검증 상태: 정서·우려
  - **책에서 쓸 지점: 변화관리 챕터의 오프닝 후보 1순위.** 이 책이 "에이전트를 등록하고 감사 로그를 남긴다"고 말할 때, 직원은 **자기 프롬프트가 감사된다**고 듣는다. 등록의 대상이 에이전트인지 사람인지를 명확히 갈라주지 못하면 이 책은 감시 매뉴얼로 읽힌다.

- 원문 인용: **"set a target for 80 per cent of developers to use AI for coding tasks at least once a week"**
  - 번역: "개발자의 80%가 최소 주 1회 코딩 작업에 AI를 쓰도록 목표를 설정했다."
  - 출처: Hacker News / "Amazon service was taken down by AI coding bot" / 작성자 `anon5739483` / https://news.ycombinator.com/item?id=47085498 / 2026-02-20
  - 검증 상태: ⚠️ 익명 주장(특정 기업 내부 목표) — 미검증
  - **책에서 쓸 지점:** "사용률을 측정한다"의 구체적 형태. 이 숫자가 실무자에게 어떻게 들리는지가 요점.

- 이중 압박의 증언 — `lollobomb`(2026-05-07): 동료들이 자신 있게 결함 있는 산출물을 쏟아내는 사이 자신은 그걸 검토하느라 압도됐고, 리더십은 **"we should collaborate and embrace AI in all our workflows, or we will be left behind"**(우리는 모든 워크플로에서 AI를 협업·수용해야 한다, 안 그러면 뒤처진다)고 말하며 **AI 사용에 대한 의무 생산성 보고**를 요구했다. 시니어인데도 빠질 수 없다고 느꼈다.
  - 출처: Hacker News / "Appearing productive in the workplace" / https://news.ycombinator.com/item?id=48046324 / 2026-05-07
  - 검증 상태: 경험담
  - **책에서 쓸 지점: 축 4에서 가장 입체적인 증언.** 감시·압박·소외·검토 부담이 한 사람 안에서 동시에 일어난다.

#### **② 반대로 수용이 잘 된 경우 — 무엇이 달랐나**

확보량이 적지만, 있는 것은 명확하다.

- 원문 인용: **"providing tools that we aren't forced to use...letting adoption proceed organically"**
  - 번역: "쓰라고 강요당하지 않는 도구를 제공하는 것… 도입이 유기적으로 진행되게 두는 것."
  - 맥락: 위에서 마이크로소프트를 비판했던 바로 그 `caconym_`이, 자기 회사에서는 잘 되고 있다며 그 차이를 설명한 대목이다.
  - 출처: Hacker News / "Everyone in Seattle hates AI" / https://news.ycombinator.com/item?id=46138952 / 2025-12-03
  - 검증 상태: 경험담
  - **책에서 쓸 지점: 이 책의 핵심 딜레마를 정면으로 건드린다.** 성공 사례의 공통 요소가 "강요하지 않음"인데, 이 책은 탑다운 체계를 주장한다. **이 모순을 정면으로 다루지 않으면 책이 무너진다.** → 정면 반론 모음에도 넣었다.

- 자율성이 전제 조건이라는 한국 쪽 관찰 — GeekNews GN⁺ 요약(HN 의견 인용): **"구성원의 자율성을 장려하는 문화에서만 상향식 AI 도입이 가능함"**, **"AI는 조직의 기능 장애를 가속함"**
  - 출처: GeekNews / https://news.hada.io/topic?id=33050 / 게시 "5일전"(2026-09-05 조회 기준)
  - 검증 상태: 2차 인용 — 원 HN 댓글 미확인
  - **책에서 쓸 지점: "AI는 조직의 기능 장애를 가속한다"는 이 책 전체의 부제가 될 수 있는 문장.** 다만 2차 인용이므로 원문 확인 필요.

- 문화가 먼저라는 증언 — 같은 GeekNews 요약에 인용된 HN 의견: **"뛰어나지만 천재적이지는 않은 엔지니어 약 20명과 일했는데, 서로 좋아하고 10년간 이직률이 매우 낮았던 것이 비밀 병기였음"**
  - 출처: 동일
  - 검증 상태: 2차 인용 — 원문 미확인

#### **③ 직무 불안 — 생산성 향상이 곧 인원 감축으로 번역된다는 인식**

- 원문 인용: **"as the individual productivity gets increased the amount of FTE per project goes down, and superfluous folks shown the door"**
  - 번역: "개인 생산성이 올라가면 프로젝트당 FTE가 줄고, 남는 사람들은 문밖으로 안내된다."
  - 출처: Hacker News / "Why are executives enamored with AI, but ICs aren't?" / 작성자 `pjmlp` / https://news.ycombinator.com/item?id=47549649 / 2026-03-27
  - 검증 상태: 정서·우려
  - **책에서 쓸 지점: 이것이 저항의 진짜 원인이다.** 실무자가 AI를 거부하는 이유는 도구가 나빠서가 아니라 **생산성 향상의 과실이 자기에게 오지 않는다고 믿기 때문**이다.

- 같은 논리의 다른 표현 — `pron`(2026-03-28): **"You work the same hours, but you're more tired, and the company pockets the profits"**
  - 번역: "일하는 시간은 같은데 더 피곤해지고, 이익은 회사가 챙긴다."
  - 출처: https://news.ycombinator.com/item?id=47549649 / 2026-03-28
  - 검증 상태: 정서
  - **책에서 쓸 지점: 변화관리 챕터 오프닝 후보.** 이 한 문장을 반박하지 못하면 어떤 체계도 안 굴러간다.

- 경영 동기에 대한 냉정한 진술 — `ilaksh`(2026-03-28): **"Reduction in employees is a primary way to do that. AI is the most promising way to reduce the need for employees."**
  - 번역: "직원 감축이 그걸 하는 주된 방법이다. AI는 직원 필요를 줄이는 가장 유망한 방법이다."
  - 출처: https://news.ycombinator.com/item?id=47549649 / 2026-03-28
  - 검증 상태: 정서·해석

- 정체성 훼손 — `beloch`(2025-12-03): **"most engineers got rebranded as 'not AI talent.' And then came the final insult"**
  - 번역: "대부분의 엔지니어가 'AI 인재가 아님'으로 재분류됐다. 그리고 마지막 모욕이 왔다."
  - 출처: Hacker News / "Everyone in Seattle hates AI" / https://news.ycombinator.com/item?id=46138952 / 2025-12-03
  - 검증 상태: ⚠️ 익명 주장(특정 기업 조직 개편) — 미검증 / 정서로는 강함
  - **책에서 쓸 지점:** 조직을 AI 기준으로 재분류하는 순간 무슨 일이 생기는지. 이 책이 "에이전트에 사번을 준다"고 할 때 **사람들이 자기 사번의 의미가 흔들린다고 느낄 수 있다**는 점.

- 전문성 무시 — `MarkSweep`(2026-03-27): **"managers lose all respect for engineering excellence and assume anything they want can be shat out by an LLM"**
  - 번역: "매니저들이 엔지니어링 탁월성에 대한 존중을 완전히 잃고, 원하는 건 뭐든 LLM이 싸질러줄 수 있다고 가정한다."
  - 출처: https://news.ycombinator.com/item?id=47549649 / 2026-03-27
  - 검증 상태: 정서 (날것, 인용 시 표현 수위 판단 필요)

#### **④ "AI 못 쓰는 사람" / 뒤처진다는 감각**

요청받은 대로 적극적으로 찾았고, 부분적으로 확보했다.

- `Kurtz79`(2025-07-24)는 고용 형태별 압박 구조를 정리했다. 직원은 AI를 쓰는 동료 대비 저평가될 위험, 컨설턴트는 단가 압축, 창업자는 높아진 MVP 기대치. 결론은 원문 인용: **"you will likely have to learn to live with it in order not to be left behind."**
  - 번역: "뒤처지지 않으려면 아마 그것과 함께 사는 법을 배워야 할 것이다."
  - 출처: Hacker News / "The great AI delusion is falling apart" / https://news.ycombinator.com/item?id=44673665 / 2025-07-24
  - 검증 상태: 정서·분석

- 기술 위축 — `joestrouth1`(2025-11-26): 동료들이 느끼는 **압박과 도태 공포**가 과도한 AI 의존으로 이어지고, 그 결과 **"dependence and progressive atrophy of the skills they once had"**(의존, 그리고 한때 가졌던 기술의 점진적 위축)로 간다는 관찰.
  - 출처: Hacker News / "I don't care how well your 'AI' works" / https://news.ycombinator.com/item?id=46059000 / 2025-11-26
  - 검증 상태: 관찰·정서

- 위 `lollobomb`(2026-05-07)의 증언도 이 범주에 걸친다 — **시니어인데도 흐름에서 빠질 수 없다고 느낀** 소외감.

- 미래 위협으로서의 강제 — `Balgair`(2024-10-03): 바이오텍 기업이 **"in about 2 years, you're going to be forced to use it or let go...job requirement going forward"**(약 2년 안에 쓰도록 강제되거나 내보내진다… 앞으로의 채용 요건)라는 방침을 세웠다는 증언.
  - 출처: Hacker News / "Employers Say Students Need AI Skills" / https://news.ycombinator.com/item?id=41730632 / **2024-10-03**
  - 🕒 2년 전 발언. "2년 안에"라고 했으니 지금이 그 시점이다 — **이 대비가 책에서 쓸 만하다.**
  - 검증 상태: ⚠️ 익명 주장 — 미검증

#### **⑤ AI 도입 담당자(추진자)의 고충 — 이 책의 1순위 독자**

**요청받은 최우선 항목인데, 솔직히 말해 가장 확보가 안 된 영역이다.** 커뮤니티에서 추진자는 대개 **비판의 대상**으로만 등장하고, 자기 목소리로 말하지 않는다. 찾아낸 것:

- GeekNews 원문 요약에 담긴 추진자의 딜레마: 회사는 개발자의 자율성을 자랑하지만, **AI 도입을 추진할 때마다 규정 준수 요구와 "현대판 러다이트" 분위기에 막힌다.**
  - 출처: GeekNews / 「AI가 Microsoft 개발자들을 미치게 만드는 걸 보는 게 새로운 취미가 되었어요」 요약 / https://news.hada.io/topic?id=21037
  - 검증 상태: 2차 요약 — 원문 확인 필요
  - **책에서 쓸 지점: 위(컴플라이언스)와 아래(반발) 사이에 끼인 추진자의 정확한 좌표.** 이 책 도입부의 인물 설정에 바로 쓸 수 있다.

- 반대편에서 본 추진자의 무능 — `enoint`(2026-03-28): 자기 회사 경영진이 **"he has no concern that competition even exists. No awareness that our competition demos at conferences"**(경쟁이 존재한다는 것 자체에 관심이 없다. 우리 경쟁사가 컨퍼런스에서 데모한다는 인식이 없다)
  - 출처: https://news.ycombinator.com/item?id=47549649 / 2026-03-28
  - 검증 상태: 정서

- 추진자를 향한 냉소의 언어 — `827a`(2026-05-22): 의무화가 이끄는 **"aimless tokenmaxing"**(목적 없는 토큰 극대화)이 회사의 생존을 위협한다는 경고.
  - 출처: Hacker News / "Steve Wozniak cheered after telling students they have AI" / https://news.ycombinator.com/item?id=48236051 / 2026-05-22
  - 검증 상태: 정서
  - **"aimless tokenmaxing"은 이 책이 반대하는 것을 한 단어로 요약한 커뮤니티 조어다. 인용 가치 높음.**

- 추진자가 마주하는 근본 반문 — `ryandrake`(2026-03-28)의 냉소적 진단: **"AI is like an energetic intern who knows his place on the totem pole and wants to please"**
  - 번역: "AI는 서열에서 자기 위치를 알고 비위를 맞추고 싶어 하는 열정적인 인턴 같다."
  - 출처: https://news.ycombinator.com/item?id=47549649 / 2026-03-28
  - 검증 상태: 정서
  - **책에서 쓸 지점:** 경영진이 AI를 좋아하는 이유가 성능이 아니라 **순응성**이라는 지적. 이 책이 "에이전트를 조직원으로 등록한다"고 할 때, 그 조직원이 **절대 반대하지 않는 조직원**이라는 사실이 조직에 무엇을 하는가 — 다룰 만한 깊은 논점.

- 경영진 동기에 대한 구조적 해석 — `pron`(2026-03-27): **"their thought process is: if they bet on AI and fail, they can plausibly claim that it was the technology's fault"**
  - 번역: "그들의 사고 과정은 이렇다: AI에 걸었다가 실패하면, 그건 기술 탓이었다고 그럴듯하게 주장할 수 있다."
  - 출처: https://news.ycombinator.com/item?id=47549649 / 2026-03-27
  - 검증 상태: 해석·정서
- `fooker`(2026-03-27): **"executives are more driven by FOMO than a teenager"** (번역: "경영진은 십대보다 FOMO에 더 휘둘린다")
  - 출처: 동일 / 2026-03-27

### 4-2. 회의론·반박

#### **반박 J — 잘 된 사례의 공통점이 "강요하지 않음"이다**
근거: `caconym_`(2025-12-03), GeekNews GN⁺ 요약의 "자율성을 장려하는 문화에서만 상향식 AI 도입이 가능함". **이 책의 탑다운 주장과 정면충돌.**

#### **반박 K — 등록·감사는 직원에게 감시로 번역된다**
근거: `smrtinsert`(2026-03-29), `lollobomb`(2026-05-07), `volker48`의 "catching"(2026-07-01). 이 책이 감시와 책임 귀속을 언어적으로 분리하지 못하면 반발을 산다.

#### **반박 L — 저항의 원인은 도구가 아니라 이익 분배다**
근거: `pjmlp`, `pron`, `ilaksh` (전부 2026-03). 변화관리 기법으로는 못 푸는 문제다. 이 책이 "변화관리로 사람을 함께 옮긴다"고 할 때, **함께 옮겨진 결과 그 사람에게 무엇이 남는지**를 말하지 못하면 공허하다.

#### **반박 M — 이 리서치 자체가 편향돼 있다**
근거: `keeda`(2026-03-28)의 "HN은 대체로 에코 챔버다". 축 3~4의 인용 대부분이 HN에서 왔고, HN은 AI 회의론이 과대표되는 곳이다. **저술 시 "커뮤니티 정서"를 "업계 정서"로 승격시키지 말 것.**

### 4-3. 현장에서 통한 것

1. **강요하지 않고 도구를 제공하고, 유기적 확산을 기다린다.** (`caconym_`, 2025-12-03) — 다만 이 책의 주장과 긴장 관계.
2. **AI 사용량을 성과 지표로 삼지 않는다.** (`brainer` GeekNews 2026-08경, `caconym_` 2025-12-03, `plaguuuuuu` 2026-06-28 — 세 곳에서 독립적으로 같은 결론)
3. **활동량·도구 사용률이 아니라 실제 결과를 보상하고, 실패 시 책임자를 찾는 대신 원인을 배우고 시스템을 개선한다.** (GeekNews 「좋은 조직문화가 AI보다 큰 생산성 향상을 만드는 이유」 요약 / https://news.hada.io/topic?id=33050 / 2026-08경)
4. **사용량은 ROI와 상관이 없다** — 원문 인용: **"사용량은 가치 있는 산출물이나 투자수익률(ROI)과 상관관계가 없음. 이 글은 실제 근거도 없이 고객이 ROI를 얻고 있다고 홍보하려는 어설픈 시도로 보임"**
   - 출처: GeekNews / 「소프트웨어 팀의 AI 사용 패턴」(Linear 데이터 분석 글에 대한 반응) / 작성자 `GN⁺` / https://news.hada.io/topic?id=32661 / 게시 "17일전"(2026-09-05 조회 기준 대략 2026-08-19)
   - **책에서 쓸 지점:** 측정 챕터의 핵심 경고. 한국어 원문이라 그대로 인용 가능.
5. **개인의 향상이 조직 학습으로 자동 전이되지 않는다** — 전이 경로 설계가 별도 과제. (GeekNews topic 29217 / 원문 robert-glaser.de)

### 축 4 커버리지

**확보한 것**
- 감시로 느낀 순간 3건 (2026-02 ~ 2026-07) — 요청 항목 충족
- 수용이 잘 된 사례 2~3건 (2025-12, 2026-08경) — **양이 적다**
- 직무 불안·정체성 훼손 5건 (2025-12 ~ 2026-03)
- "뒤처진다"는 감각 4건 (2024-10 ~ 2026-05)
- 추진자 관련 자료 — **부분 확보 (5건, 그중 자기 목소리는 사실상 1건)**
- 측정에 대한 한국어 인용 3건 (GeekNews) — 한국 독자용으로 가치 높음
- 균형용 반대 목소리(에코챔버 경고, 자발적 도입 성공) 2건

**비어 있는 것**
- **주니어 개발자·운영·CS 인력의 목소리 — 사실상 비어 있다.** 채용 축소와 연결된 주니어 당사자 증언을 확보하지 못했다. Reddit(r/cscareerquestions, r/ExperiencedDevs)이 이 주제의 본진인데 접근 불가. **축 4에서 가장 큰 공백이고, 이 책의 감정적 무게에 직접 영향을 준다.**
- **"AI 못 쓰는 사람"의 1인칭 목소리 — 확보 실패.** 찾은 건 "뒤처질까 봐 두렵다"는 목소리지 "나는 아무리 해도 안 된다"는 목소리가 아니다. 후자는 능숙한 사람들이 모인 커뮤니티에서 구조적으로 잘 안 나온다. 요청서에서 예상한 그대로다. **대안: 사내 인터뷰나 설문으로 직접 채워야 하는 영역.**
- **AI 도입 담당자의 1인칭 고충 — 거의 비어 있다.** 커뮤니티에서 추진자는 대개 3인칭 비판 대상으로만 등장한다. GeekNews topic 21037의 요약 1건이 유일하게 근접한 자료다. **이 책의 1순위 독자의 언어를 커뮤니티에서 캐오는 데 실패했다.** 대안 경로: 커리어리·링크드인 한국어 포스트(미접근), 사내 인터뷰.
- **커리어리 — 전혀 접근하지 못했다.** 검색 결과에 한 건도 잡히지 않았다.
- 운영·CS 인력의 목소리 — 완전히 비어 있음.
- Dev.to, X/Mastodon, Discord/Slack 공개 로그 — 미접근.

---

## 챕터 오프닝용 강한 인용문 모음

저술 시 챕터 도입부에 그대로 얹을 수 있는 것들. **원문 그대로**이며 각색하지 않았다.

1. **"Wtf? We have been calling these workload identities for years"**
   — `zingababba`, Hacker News, 2025-02-04 / https://news.ycombinator.com/item?id=42928645
   *(번역: "뭐야? 우리 이거 몇 년째 workload identity라고 불러왔는데.")*
   → **에이전트 등록 챕터.** 새 이름에 대한 첫 반응이 냉소라는 사실에서 출발하기.

2. **"Pretty pleaser please people don't get your agents registered as direct-reports in the org-chart with HR!"**
   — `polotics`, Hacker News, 2026-09-04 / https://news.ycombinator.com/item?id=49561918
   *(번역: "제발 부탁인데 여러분, 에이전트를 HR 조직도에 직속 부하로 등록하지는 맙시다!")*
   → **책 전체의 서문 또는 사번 챕터.** 이 책의 핵심 주장을 정확히 겨냥한 반농담.

3. **"I went through the entire investor arc in about a day and a half. From the hopeful optimism of hiring a CEO, to watching the org chart explode, to complete disillusionment, to demoting the CEO back to a regular worker..."**
   — `yego`, Hacker News, 2026-03-04 / https://news.ycombinator.com/item?id=47245374
   *(번역: "하루 반 만에 투자자 서사를 통째로 겪었다. CEO를 고용하는 희망찬 낙관에서 시작해, 조직도가 폭발하는 걸 지켜보고, 완전한 환멸에 이르렀다가, 결국 CEO를 평사원으로 강등시켰다…")*
   → **조직 은유의 함정 챕터.** 직접 해본 사람의 후회담.

4. **"Confluence is where documentation goes to die. And then rot."**
   — `EdwardDiego`, Hacker News, 2020-07-12 / https://news.ycombinator.com/item?id=23808854
   *(번역: "Confluence는 문서가 죽으러 가는 곳이다. 그리고 썩는다.")*
   → **SOP 챕터.** 같은 문장을 다섯 사람이 7년에 걸쳐 반복했다는 사실과 함께 쓸 것.

5. **"When I get an LLM-generated doc or runbook, my first thought is that its very possible that I'm the first person who has ever read this."**
   — `backlava12`, Hacker News, 2026-08-11 / https://news.ycombinator.com/item?id=49258726
   *(번역: "LLM이 만든 문서나 런북을 받으면, 첫 생각은 '내가 이걸 읽은 최초의 인간일 가능성이 꽤 높다'는 것이다.")*
   → **SOP 자동 생성 챕터.** 쓰기는 공짜, 읽기는 희소.

6. **"A runbook can tell you what usually works, but it cannot tell you when the situation is no longer 'usual.'"**
   — `flashdesk`, Hacker News, 2026-04-27 / https://news.ycombinator.com/item?id=47918548
   *(번역: "런북은 보통 무엇이 통하는지는 알려줄 수 있지만, 언제부터 상황이 더 이상 '보통'이 아닌지는 알려주지 못한다.")*
   → **절차의 한계 챕터.**

7. **"mandates happened and now I'm being forced to use them. Absolutely no guidance from leadership though."**
   — `ares623`, Hacker News, 2026-03-06 / https://news.ycombinator.com/item?id=47279806
   *(번역: "의무화가 내려왔고 이제 나는 그걸 쓰도록 강요당한다. 그런데 리더십의 가이드는 전혀 없다.")*
   → **책 전체의 오프닝 후보 1순위.** 이 책이 없어서 생긴 일.

8. **"You work the same hours, but you're more tired, and the company pockets the profits"**
   — `pron`, Hacker News, 2026-03-28 / https://news.ycombinator.com/item?id=47549649
   *(번역: "일하는 시간은 같은데 더 피곤해지고, 이익은 회사가 챙긴다.")*
   → **변화관리 챕터.** 저항의 진짜 이유.

9. **"all your prompts are tracked and easily viewable by whoever oversees it at your company"**
   — `smrtinsert`, Hacker News, 2026-03-29 / https://news.ycombinator.com/item?id=47549649
   *(번역: "당신의 프롬프트는 전부 추적되고, 회사에서 그걸 관리하는 누구든 쉽게 들여다볼 수 있다.")*
   → **감사·로깅 챕터.** 등록이 감시로 들리는 순간.

10. **"AI 사용량 자체를 성과 지표로 삼으면 사람들은 필요하지 않은 작업에도 AI를 사용해 숫자를 맞추게 될 수 있음"**
    — `brainer`, GeekNews, 2026-08-31경 / https://news.hada.io/topic?id=33050
    → **측정 챕터.** 한국어 원문 그대로 인용 가능.

11. **"일단 회사에서 AI 서비스를 지원 거의 안해주네요. 개인별로 쓰는건 개인이 하라고 하고(회사에서 쓰려고 개인이 AI 서비스 구독 ㅜ) 팀에는 클로드 프로?월 3만원짜리 지원하고 끝."**
    — `akapwhd`, GeekNews, 2026-05경 / https://news.hada.io/topic?id=29217
    → **바텀업의 현실 챕터.** 한국 독자에게 가장 실감나는 한 줄.

12. **"AI를 '잘쓰는법'을 어떻게 다뤄야 하는지는 다들 갈팡질팡하고 있는 것 같네요."**
    — `kallare`, GeekNews, 2026-05경 / https://news.hada.io/topic?id=29217
    → **서문.** 이 책이 왜 필요한지를 독자의 언어로.

13. **"So every time we fire or lay off the person whose name is on the automation, we need to rotate the keys?"**
    — `collabs`, Hacker News, 2026-04-25 / https://news.ycombinator.com/item?id=47898675
    *(번역: "그러면 자동화에 이름이 걸린 사람을 해고하거나 정리할 때마다 키를 로테이션해야 한다는 거야?")*
    → **소유자 지정 챕터.** 소유자를 정하는 순간 생기는 새 비용.

14. **"after firing everyone they of course didn't follow the off boarding process"**
    — `madaxe_again`, Hacker News, 2026-03-20 / https://news.ycombinator.com/item?id=47462193
    *(번역: "전원 해고하고 나서, 당연하게도 오프보딩 절차는 안 지켰다.")*
    → **오프보딩 챕터.** ⚠️ 익명 주장 라벨과 함께 쓸 것.

15. **"Client-asserted context with no signed execution record is unverifiable. A signed execution record with no intent context is hard to interpret."**
    — `vaaraio`, GitHub MCP SEP-2817, 2026-05-29 / https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2817
    *(번역: "서명된 실행 기록 없는 클라이언트 주장 맥락은 검증 불가능하다. 의도 맥락 없는 서명된 실행 기록은 해석하기 어렵다.")*
    → **감사 로그 설계 챕터.** "왜 했는가"와 "무엇을 했는가"는 다른 증거다.

16. **"aimless tokenmaxing"**
    — `827a`, Hacker News, 2026-05-22 / https://news.ycombinator.com/item?id=48236051
    *(번역: "목적 없는 토큰 극대화")*
    → 짧은 인용. 이 책이 반대하는 것의 이름.

17. **"AI is like an energetic intern who knows his place on the totem pole and wants to please"**
    — `ryandrake`, Hacker News, 2026-03-28 / https://news.ycombinator.com/item?id=47549649
    *(번역: "AI는 서열에서 자기 위치를 알고 비위를 맞추고 싶어 하는 열정적인 인턴 같다.")*
    → **에이전트를 조직원으로 볼 때의 함정 챕터.** 절대 반대하지 않는 조직원.

---

## 이 책의 주장에 대한 정면 반론 모음 (저술 시 반드시 응답해야 할 것들)

각 반론에 **누가 어디서 말했는지**를 붙였다. 이 목록은 저술가가 챕터별로 소화해야 할 체크리스트다.

### 반론 1 — **"에이전트에 사번을 준다는 건 서비스 계정에 마케팅 이름 붙인 것 아니냐"**
- 근거: `zingababba`("workload identities라고 몇 년째 불러왔다"), `xg15`("서비스 계정은 봇이 아니다"), `xarope`(OWASP가 나열하는 건 결국 API 키·토큰·인증서뿐), `ALLTaken` — 전부 https://news.ycombinator.com/item?id=42928645 / 2025-02-04
- **책이 답해야 할 것:** 사번 부여가 기존 서비스 계정과 **기술적으로** 무엇이 다른가, 아니면 다르지 않은데 **조직적으로** 무엇이 다른가. 후자라면 그걸 정직하게 말하고, 왜 그 조직적 차이가 결정적인지 논증해야 한다. 이 반론을 회피하면 첫 장에서 신뢰를 잃는다.

### 반론 2 — **"에이전트를 조직도에 올리면 조직도가 폭발한다"**
- 근거: `yego`(2026-03-04, 역할 20개로 불어나고 메타 작업이 실제 산출을 밀어냄), `polotics`(2026-09-04, "제발 HR 조직도에 등록하지 마라")
- **책이 답해야 할 것:** "등록"이 어디까지이고 어디부터가 아닌지의 경계. 사번·소유자·매니저가 **책임 귀속 장치**인지 **조직 시뮬레이션**인지. 후자로 읽히면 이 반론이 그대로 적중한다.

### 반론 3 — **"성공 사례의 공통점은 '강요하지 않음'이다 — 그런데 이 책은 탑다운을 주장한다"**
- 근거: `caconym_`(2025-12-03, "쓰라고 강요당하지 않는 도구를 제공… 유기적으로 확산되게"), GeekNews GN⁺ 요약("구성원의 자율성을 장려하는 문화에서만 상향식 AI 도입이 가능함", https://news.hada.io/topic?id=33050)
- **책이 답해야 할 것: 이 책의 존립이 걸린 반론.** "탑다운 체계"가 **강제(mandate)**가 아니라 **인프라·보증(guarantee)**이라는 구분을 세울 수 있는가. 위에서 정하는 것이 *무엇을 쓰라*가 아니라 *어디까지 안전한가*라면 이야기가 달라진다. 이 구분을 책 초반에 명시적으로 세우기를 권한다.

### 반론 4 — **"탑다운 AI 의무화는 실제로 이런 결과를 낳았다" (11건의 증언)**
- 근거: `bitwize`(추적·지표·해고 위협 완비, 2026-03-28), `ares623`(강요는 있고 가이드는 없음, 2026-03-06), `axegon_`(성과 점수에 반영, 2026-03-15), `klardotsh`(지표 못 맞추면 PIP, 2025-07-01), `mips_avatar`(작동하든 말든 강요, 2025-12-03), `caconym_`(평가·보상을 사용량에 묶는 것에 대한 격한 반응, 2025-12-03), `plaguuuuuu`(지표 게이밍, 2026-06-28), `rk06`(품질 하락, 2026-08-25), `keeda`(조용한 해고 수단, 2025-12-03), `stego-tech`(필수 쿼리 수 할당, 2025-04-12), `placardloop`(VP의 매일 사용 지시, 2025-05-25)
- **책이 답해야 할 것:** 탑다운을 옹호하는 책이 이 11건을 모르면 안 된다. **탑다운의 어떤 형태가 이 결과를 낳는지**를 구체적으로 진단하고, 이 책이 제안하는 형태가 그것과 어떻게 다른지 보여야 한다. `tdeck`의 증언(맥락 무시한 획일화가 문제)이 그 진단의 실마리다.

### 반론 5 — **"등록과 감사는 직원에게 감시로 번역된다"**
- 근거: `smrtinsert`(2026-03-29, 프롬프트가 다 추적됨), `lollobomb`(2026-05-07, 의무 생산성 보고), `volker48`(2026-07-01, "catching when employees paste sensitive data")
- **책이 답해야 할 것:** 에이전트를 감사하는 것과 사람을 감시하는 것의 경계를 **기술적으로** 그을 수 있는가. `XuebinMa`의 "정책 단계와 감사 단계를 파이프라인으로 분리한다"는 접근이 이 책에 줄 수 있는 답의 형태다.

### 반론 6 — **"저항의 원인은 도구가 아니라 이익 분배다 — 변화관리로는 못 푼다"**
- 근거: `pjmlp`(2026-03-27, FTE 감소 → 잉여 인력 정리), `pron`(2026-03-28, "이익은 회사가 챙긴다"), `ilaksh`(2026-03-28, "직원 감축이 주된 방법")
- **책이 답해야 할 것:** "변화관리로 사람을 함께 옮긴다"는 부제에 대한 가장 아픈 반론. **옮겨진 사람에게 무엇이 남는지** 말하지 못하면 이 책의 변화관리 챕터는 설득 기법 매뉴얼로 읽힌다.

### 반론 7 — **"긴 규칙 파일은 안 지켜지고, 2026년 모델에서는 오히려 해롭다"**
- 근거: `nick__m`(2026-08-29, "redundant at best and frequently actively harmful"), `Topfi`(2026-08-29, context bloat), `reacharavindh`(2026-08-29, 실제로 쓰는지 확인 불가), `anotherCodder`(2026-02-12, 조용히 무시됨)
- **책이 답해야 할 것:** "SOP를 에이전트에 준다"의 구체적 형식. 통짜 문서가 아니라 점진적 공개 + 결정론적 검증(`lazarie`, `boorang`, `mirekrusin`, `jpalomaki`의 휴리스틱)이라는 답이 이미 커뮤니티에 있다. 이걸 반영하지 않으면 실무자가 바로 알아본다.

### 반론 8 — **"RPA도 똑같이 시작했다 — 유지보수가 절감분을 잡아먹었다"**
- 근거: `euphetar`(2026-07-30, "too brittle", 유지보수가 대체하려던 노동을 초과), `cowartc`(2026-04-16), `muchael`(2026-04-17)
- **책이 답해야 할 것:** 등록·소유·감사에 드는 **운영 비용을 처음부터 계산에 넣은 손익 모델**. "이번엔 다르다"의 증명 책임이 이 책에 있다.

### 반론 9 — **"MIT 95%는 그렇게 읽으면 안 된다"**
- 근거: `layer8`(2025-08-18, 표본 300건 공개 배포 한정, 비공개 프로젝트 누락, 낮은 열매는 AI 없이도 해결 가능), `RaftPeople`(2025-08-18, "실패"는 대개 예산·일정 초과를 뜻함)
- **책이 답해야 할 것:** 이 숫자를 쓴다면 반드시 두 반박을 함께 실을 것. 안 그러면 밝은 독자를 잃는다.

### 반론 10 — **"에이전트 아이덴티티 표준은 아직 정해지지 않았다"**
- 근거: MCP SEP-1933/2817/2787/2385 전부 2026-09-05 기준 open, A2A #1672 open, SPIFFE #382/383/408은 댓글 한 자릿수. `vessenes`의 "누가 검증자를 검증하나", `desiorac`의 "신뢰 계층 없는 자기주권은 자기 주장으로 미끄러진다", `jagmarques`의 "Agent Card는 정적 JSON이라 변조 탐지 불가"
- **책이 답해야 할 것:** 특정 표준·제품에 못 박지 말고, **표준이 정해지기 전에 조직이 무엇을 할 수 있는가**로 서술할 것. 🕒 이 영역은 책 출간 시점에 반드시 재확인.

### 반론 11 — **"자율 에이전트 인가는 실제 운영 고통인가, 아니면 예방적 설계인가"**
- 근거: `Ram9199`의 질문(2026-06-13, https://github.com/modelcontextprotocol/modelcontextprotocol/issues/2902)
- **책이 답해야 할 것:** 2026년 9월 현재 커뮤니티 증거로는 **아직 예방적 설계 쪽 비중이 크다.** 이 책이 "지금 당장 터지고 있다"고 과장하면 나중에 반증당한다. **"아직 안 터졌을 때 세워야 한다"** 는 논리로 가는 게 더 방어 가능하다.

### 반론 12 — **"이 리서치의 출처가 편향돼 있다"**
- 근거: `keeda`(2026-03-28, "AI 도입률 80~90%… HN은 대체로 에코 챔버")
- **책이 답해야 할 것:** 이 문서의 축 3·4 인용은 HN 편중이고 Reddit은 접근조차 못 했다. 저술 시 **"커뮤니티에서는"**과 **"업계에서는"**을 절대 혼용하지 말 것.

---

## 참고 스레드 전체 (URL + 게시일 + 플랫폼)

### Hacker News — 스토리 스레드
| URL | 제목 | 게시일 | 규모 |
|---|---|---|---|
| https://news.ycombinator.com/item?id=42928645 | OWASP Non-Human Identities Top 10 | 2025-02-04 | 157점·33댓글 |
| https://news.ycombinator.com/item?id=44941118 | 95% of generative AI pilots at companies are failing – MIT report | 2025-08-18 | 230점·167댓글 |
| https://news.ycombinator.com/item?id=44709844 | Ask HN: What are the BIGGEST Problems you'd face with a full-AI employee? | 2025-07-28 | 10점·5댓글 |
| https://news.ycombinator.com/item?id=46138952 | Everyone in Seattle hates AI | 2025-12-03 | 967점·1065댓글 |
| https://news.ycombinator.com/item?id=47549649 | Why are executives enamored with AI, but ICs aren't? | 2026-03-27 | 109점·168댓글 |
| https://news.ycombinator.com/item?id=47765374 | Show HN: Kontext CLI – Credential broker for AI coding agents in Go | 2026-04-14 | 70점·17댓글 |
| https://news.ycombinator.com/item?id=49363710 | Launch HN: OneCLI (YC S26) – OSS sandboxed agent harness for teams | 2026-08-19 | 88점·36댓글 |

### Hacker News — 개별 댓글 (인용 출처)
| URL | 작성자 | 게시일 | 축 |
|---|---|---|---|
| https://news.ycombinator.com/item?id=6507980 | olegp | 2013-10-07 | 1 (오프보딩) |
| https://news.ycombinator.com/item?id=9727792 | netik | 2015-06-16 | 1 (오프보딩 실패) |
| https://news.ycombinator.com/item?id=19429182 | GordonS | 2019-03-19 | 2 (Confluence) |
| https://news.ycombinator.com/item?id=23808854 | EdwardDiego | 2020-07-12 | 2 (Confluence) |
| https://news.ycombinator.com/item?id=30233639 | more_corn | 2022-02-06 | 2 (Confluence) |
| https://news.ycombinator.com/item?id=37167982 | stock_toaster | 2023-08-17 | 2 (Confluence) |
| https://news.ycombinator.com/item?id=39375258 | morkalork | 2024-02-14 | 2 (Confluence) |
| https://news.ycombinator.com/item?id=41730632 | Balgair | 2024-10-03 | 4 (강제 예고) |
| https://news.ycombinator.com/item?id=43665422 | stego-tech | 2025-04-12 | 3 (의무화) |
| https://news.ycombinator.com/item?id=44090429 | placardloop | 2025-05-25 | 3 (의무화) |
| https://news.ycombinator.com/item?id=44430973 | klardotsh | 2025-07-01 | 3 (의무화·PIP) |
| https://news.ycombinator.com/item?id=44673665 | Kurtz79 | 2025-07-24 | 4 (뒤처짐) |
| https://news.ycombinator.com/item?id=44978793 | chriskanan | 2025-08-21 | 3 (shadow AI) |
| https://news.ycombinator.com/item?id=46059000 | joestrouth1 | 2025-11-26 | 4 (기술 위축) |
| https://news.ycombinator.com/item?id=46136275 | pbronez | 2025-12-03 | 3 (shadow AI) |
| https://news.ycombinator.com/item?id=46140813 | keeda | 2025-12-03 | 3 (조용한 해고) |
| https://news.ycombinator.com/item?id=46854187 | veunes | 2026-02-02 | 3 (shadow AI) |
| https://news.ycombinator.com/item?id=46983893 | anotherCodder | 2026-02-12 | 2 (조용한 무시) |
| https://news.ycombinator.com/item?id=47085498 | anon5739483 | 2026-02-20 | 4 (사용률 목표) |
| https://news.ycombinator.com/item?id=47245374 | yego | 2026-03-04 | 1 (조직도 폭발) |
| https://news.ycombinator.com/item?id=47279806 | ares623 | 2026-03-06 | 3 (가이드 없는 강요) |
| https://news.ycombinator.com/item?id=47387307 | axegon_ | 2026-03-15 | 3 (성과 점수) |
| https://news.ycombinator.com/item?id=47462076 | perrygeo | 2026-03-20 | 1 (계정 난립) |
| https://news.ycombinator.com/item?id=47462193 | madaxe_again | 2026-03-20 | 1 (오프보딩) |
| https://news.ycombinator.com/item?id=47552106 | bitwize | 2026-03-28 | 3 (의무화·추적) |
| https://news.ycombinator.com/item?id=47792235 | cowartc | 2026-04-16 | 2 (RPA) |
| https://news.ycombinator.com/item?id=47807714 | muchael | 2026-04-17 | 2 (RPA) |
| https://news.ycombinator.com/item?id=47822065 | cracadumi | 2026-04-19 | 1 (감사 귀속) |
| https://news.ycombinator.com/item?id=47898675 | collabs | 2026-04-25 | 1 (키 로테이션) |
| https://news.ycombinator.com/item?id=47898958 | theamk | 2026-04-25 | 1 (공유 비밀번호) |
| https://news.ycombinator.com/item?id=47918548 | flashdesk | 2026-04-27 | 2 (런북 한계) |
| https://news.ycombinator.com/item?id=48046324 | lollobomb | 2026-05-07 | 4 (이중 압박) |
| https://news.ycombinator.com/item?id=48236051 | 827a | 2026-05-22 | 4 (tokenmaxing) |
| https://news.ycombinator.com/item?id=48335321 | troupo | 2026-05-30 | 1 (계정 구분) |
| https://news.ycombinator.com/item?id=48655348 | Quothling | 2026-06-24 | 3 (shadow AI) |
| https://news.ycombinator.com/item?id=48704828 | plaguuuuuu | 2026-06-28 | 3 (지표 게이밍) |
| https://news.ycombinator.com/item?id=48754582 | volker48 | 2026-07-01 | 3 (shadow AI 탐지) |
| https://news.ycombinator.com/item?id=49009276 | tcoff91 | 2026-07-22 | 2 (AI 문서 검증) |
| https://news.ycombinator.com/item?id=49063459 | hbarka | 2026-07-26 | 2 (프롬프트 축소) |
| https://news.ycombinator.com/item?id=49110493 | euphetar | 2026-07-30 | 2 (RPA 취약성) |
| https://news.ycombinator.com/item?id=49184005 | shostack | 2026-08-05 | 2 (모델 변경 파손) |
| https://news.ycombinator.com/item?id=49176003 | crimsonnoodle58 | 2026-08-04 | 1 (오프보딩) |
| https://news.ycombinator.com/item?id=49221134 | lazarie | 2026-08-08 | 2 (결정론적 검증) |
| https://news.ycombinator.com/item?id=49258726 | backlava12 | 2026-08-11 | 2 (AI 문서 부패) |
| https://news.ycombinator.com/item?id=49369002 | jpalomaki | 2026-08-20 | 2 (규칙 부패) |
| https://news.ycombinator.com/item?id=49433354 | rk06 | 2026-08-25 | 3 (품질 하락) |
| https://news.ycombinator.com/item?id=49474177 | boorang | 2026-08-28 | 2 (참조 패턴) |
| https://news.ycombinator.com/item?id=49491148 | reacharavindh | 2026-08-29 | 2 (규칙 준수 불투명) |
| https://news.ycombinator.com/item?id=49491488 | nick__m | 2026-08-29 | 2 (규칙 유해론) |
| https://news.ycombinator.com/item?id=49491618 | Topfi | 2026-08-29 | 2 (context bloat) |
| https://news.ycombinator.com/item?id=49510061 | nzach | 2026-08-31 | 2 (규칙 옹호) |
| https://news.ycombinator.com/item?id=49519776 | Quothling | 2026-09-01 | 1 (Entra 관리 부담) |
| https://news.ycombinator.com/item?id=49530746 | clickety_clack | 2026-09-02 | 2 (간결한 지시) |
| https://news.ycombinator.com/item?id=49532425 | mirekrusin | 2026-09-02 | 2 (점진적 공개) |
| https://news.ycombinator.com/item?id=49561918 | polotics | 2026-09-04 | 1 (조직도 등록 반대) |

### GitHub — 스펙 논쟁 (전부 2026-09-05 조회, 상태 명시)
| URL | 제목 | 개설일 | 상태·규모 |
|---|---|---|---|
| https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1933 | SEP-1933: Workload Identity Federation | 2025-12-05 | open·40댓글 |
| https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2817 | SEP-2817: AI Invocation Audit Context in Request `_meta` | 2026-05-29 | open·29댓글 |
| https://github.com/modelcontextprotocol/modelcontextprotocol/issues/2902 | MCP Authorization in Non-Browser, Non-User-Interactive Scenarios — Field Report from 12 Production Servers | 2026-06-10 | closed·4댓글 |
| https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2787 | SEP-2787: Tool call attestation | 2026-05-25 | open·33댓글 |
| https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2385 | SEP-2385: Tool Auth Manifest | 2026-03-11 | open·23댓글 |
| https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2643 | SEP-2643: Structured Authorization Denials | 2026-04-24 | open·6댓글 |
| https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2848 | SEP-2848: Asynchronous Approval for Tool Calls | 2026-06-03 | open·6댓글 |
| https://github.com/modelcontextprotocol/modelcontextprotocol/issues/3337 | Proposal for the Enterprise IG Audit/Compliance Scope | 2026-09-01 | open·1댓글 |
| https://github.com/modelcontextprotocol/modelcontextprotocol/issues/333 | MCP currently seems to treat the client as a single entity which introduces a confused deputy problem | 2025-04-14 | open·10댓글 |
| https://github.com/modelcontextprotocol/modelcontextprotocol/issues/205 | Treat the MCP server as an OAuth resource server rather than an authorization server | 2025-03-16 | open·88댓글 |
| https://github.com/modelcontextprotocol/modelcontextprotocol/issues/214 | Support On-Behalf-Of Token Exchange protocol for Agent-to-Agent Communications | 2025-03-21 | open·11댓글 |
| https://github.com/modelcontextprotocol/modelcontextprotocol/pull/646 | SEP-646: Enterprise-Managed Authorization Profile for MCP | 2025-06-04 | open·15댓글 |
| https://github.com/a2aproject/A2A/issues/1672 | Proposal: Agent Identity Verification for Agent Cards | 2026-03-22 | open·658댓글 ⚠️ 출처 품질 주의 |
| https://github.com/a2aproject/A2A/issues/1575 | Running implementation of agent identity, delegation, and enforcement | 2026-03-02 | open·98댓글 |
| https://github.com/a2aproject/A2A/pull/1850 | docs(proposals): add A2A Identity Trust Framework roadmap (v1.0 - v2.0) | 2026-05-13 | open·47댓글 |
| https://github.com/a2aproject/A2A/issues/1937 | Optional context-binding profile for delegated authority | 2026-06-15 | open·5댓글 |
| https://github.com/spiffe/spiffe/issues/382 | Proposal: SPIFFE IDs for AI Agent Workloads | 2026-03-26 | open·3댓글 |
| https://github.com/spiffe/spiffe/issues/383 | JWT-SVID claim for model identity in AI workloads | 2026-03-31 | open·0댓글 |
| https://github.com/spiffe/spiffe/issues/408 | JWT-SVID Support Delegated (Actor) Identity | 2026-06-27 | open·2댓글 |

### GeekNews (news.hada.io) — 게시일이 상대 표기라 2026-09-05 조회 기준 추정치 병기
| URL | 제목 | 게시(추정) | 비고 |
|---|---|---|---|
| https://news.hada.io/topic?id=29217 | 모두가 AI를 가져도 회사는 여전히 아무것도 배우지 못할 때 | "4달전" ≈ 2026-05 | 한국어 댓글 2건 확보 |
| https://news.hada.io/topic?id=33050 | 좋은 조직문화가 AI보다 큰 생산성 향상을 만드는 이유 | "5일전" ≈ 2026-08-31 | 한국어 댓글 1건 확보 |
| https://news.hada.io/topic?id=32661 | 소프트웨어 팀의 AI 사용 패턴 | "17일전" ≈ 2026-08-19 | GN⁺ 비판 댓글 확보 |
| https://news.hada.io/topic?id=28810 | Google Cloud의 AI 에이전트 거버넌스 스택 | "4달전" ≈ 2026-05 | **댓글 확인 실패** |
| https://news.hada.io/topic?id=20489 | Atuin Desktop: 실행 가능한 Runbooks | 2025-04-23 | 실행 가능 런북 사례 |
| https://news.hada.io/topic?id=21037 | AI가 Microsoft 개발자들을 미치게 만드는 걸 보는 게 새로운 취미가 되었어요 | 상대 표기 | 추진자 고충 요약 |
| https://news.hada.io/topic?id=17832 | 스타트업을 위한 셀프 호스팅 Wiki 설정 방법 | 상대 표기 | 문서 오염 지적 |
| https://news.hada.io/topic?id=15610 | Docmost | 상대 표기 | Confluence 속도 불만 |
| https://news.hada.io/topic?id=26591 | 프런티어 AI 에이전트, KPI 압박 시 30~50% 비율로 윤리적 제약 위반 | 상대 표기 | ⚠️ 수치 미검증 |
| https://news.hada.io/topic?id=27499 | AI 에이전트를 고용해서 에러 추적을 자동화한 이야기 | "6달전" ≈ 2026-03 | 댓글 2건(내용 없음) |

### 기타
| URL | 플랫폼 | 게시일 | 비고 |
|---|---|---|---|
| https://okky.kr/articles/1532084 | OKKY | "1년 이상 전" | 한국 AI 대체 가속론 ⚠️ 미검증 |
| https://okky.kr/articles/1436748 | OKKY | 미확인 | 사내 ChatGPT 차단 문의 — 댓글 확인 실패 |
| https://lobste.rs (search) | Lobsters | — | "Securing agentic identity" (codon.org.uk/~mjg59, 2026-07-06, 1댓글) 및 "We don't need to hack your AI Agent to hack your AI Agent" (srlabs.de, 2026-03-17, 4댓글) 존재 확인. **개별 스레드 페이지 접근 실패(404)** — 댓글 미확보 |
| https://velog.io/@okorion/... | velog | 미확인 | 「AI 코딩 도구의 생산성을 잘못 측정하는 12가지 지표」 — 제목만 확인, 본문 미검토 |

---

## ⚠️ 미검증 사실 주장 모아보기

**fact-checker에게 넘김.** 아래는 커뮤니티 발언에 섞여 있던 사실 주장이다. 정서·경험담과 달리 **수치·기업명·사건**이 포함돼 있어, 책에 쓰려면 원 출처 확인이 필요하다. 그대로 인용하면 안 된다.

### 수치 주장
1. **"AI adoption is up to 80-90%"** — `keeda`, HN, 2026-03-28. 출처 미제시.
2. **"AI 도입률/shadow AI 사용률 약 90%"** — `Workaccount2`(2025-10-02, 2025-08-21), `PeterStuer`(2026-02-19), `WarmWash`(2026-03-05) 등 HN 댓글 다수가 "90% of companies reported regular use of personal AI tools"를 인용. **전부 2차 인용이고 원 조사 출처가 댓글에 명시돼 있지 않다.**
3. **"65% use unauthorized tools, 30% fed sensitive data to ChatGPT"** — `gaudioioio`, HN, 2025-11-05. 원 조사 미확인.
4. **"Median org uses 28 distinct AI apps. Global 2000 average 129."** — `emeryray02`, HN, 2026-03-12. 원 조사 미확인.
5. **"We removed over 80% of Claude Code's system prompt for more advanced models"** — `hbarka`, HN, 2026-07-26. 화자의 소속·근거 미확인.
6. **"set a target for 80 per cent of developers to use AI for coding tasks at least once a week"** — `anon5739483`, HN, 2026-02-20. 특정 기업(AWS) 내부 목표 주장. **익명 계정.**
7. **"프런티어 AI 에이전트가 KPI 압박 시 30~50% 비율로 윤리적 제약 위반, 12개 LLM 중 9개"** — GeekNews topic 26591. **원 연구 확인 필요.**
8. **MIT 리포트의 "95%"와 표본 "300 public AI deployments"** — HN 스레드(2025-08-18)에서 논쟁. 원 리포트 직접 확인 필요. **위 반론 9 참조.**
9. **NHI:인간 비율 "45:1"(Rubrik Zero Labs), "144:1"(Entro Labs H1 2025), "80:1 이상", "47% of NHIs are more than one year old with no credential rotation", "두 곳 중 두 곳(2/3) 기업이 NHI 침해 경험"** — 이 수치들은 **커뮤니티가 아니라 벤더 마케팅 콘텐츠**(doppler.com, lumos.com, apono.io, nhimg.org 등)에서 나왔다. 커뮤니티 리서치 범위 밖이며, **이해관계 있는 출처**다. 책에 쓰려면 원 조사 방법론 확인 필수. **web-researcher/fact-checker에 이관.**

### 기업·사건 주장
10. **"everyone was forced to use Microsoft's AI tools whether they worked or not"** — `mips_avatar`, HN, 2025-12-03. 특정 기업 내부 정책 주장.
11. **"Microsoft...will simply PIP you for being a luddite if you aren't meeting usage metrics"** — `klardotsh`, HN, 2025-07-01. 특정 기업 인사 관행 주장.
12. **"most engineers got rebranded as 'not AI talent'"** — `beloch`, HN, 2025-12-03. 특정 기업 조직 개편 주장.
13. **"VP right now saying everyone must use AI every day"** — `placardloop`, HN, 2025-05-25. 특정 기업 주장.
14. **"after firing everyone they of course didn't follow the off boarding process"** + 1년 넘게 JIRA 접근 유지 — `madaxe_again`, HN, 2026-03-20. 특정 사건 주장.
15. **"now he's implementing an AI mandate for every employee, replete with tracking and metrics and the threat of being fired"** — `bitwize`, HN, 2026-03-28. 자기 회사 CEO 정책 주장.
16. **"usage of ai is not just allowed or encouraged but mandated. And is part of their performance score"** — `axegon_`, HN, 2026-03-15. 제3자 회사 정책 주장.
17. **"my company forced us to use their AI tooling"** + 필수 쿼리 수 할당 — `stego-tech`, HN, 2025-04-12.
18. **"in about 2 years, you're going to be forced to use it or let go"** (바이오텍 기업) — `Balgair`, HN, 2024-10-03.
19. **"12 MCP servers in production"** 필드 리포트 — `guangda88`, GitHub #2902, 2026-06-10. 본인이 solo developer라고 밝힘. 규모 검증 불가.
20. **"'Confluence 기다리는 중'이 PayPal 같은 기업에서 관용구"** — GeekNews topic 15610 논의. 사내 관용구 주장, 검증 불가.
21. **한국 AI 대체 가속론의 근거들** ("ChatGPT 유료 사용률 세계 상위권", SI/하청 구조 비중 등) — OKKY `yh8332`. **구조적 일반화이며 통계 출처 미제시.**
22. **Microsoft Entra Agent ID Administrator 역할의 권한 상승 취약점** (Silverfort 연구진 Noa Ariel·Yoav S 보고, 2026-04 마이크로소프트 패치 완료) — 이건 커뮤니티 발언이 아니라 **보안 매체 보도**(thehackernews.com, cybersecuritynews.com, hackread.com)다. 책에 쓴다면 벤더 어드바이저리 원문 확인 필요. **에이전트 아이덴티티 제품의 조기 결함 사례로는 서사적 가치가 크다.**

### 모델 동작 주장
23. **"GPT-5.6 계열에서 상세한 AGENT.md 지시는 redundant at best and frequently actively harmful"** — `nick__m`, HN, 2026-08-29. 자체 평가 미공개.
24. **"모델 5.2 무렵부터 AGENTS.md가 성능을 제한했다"** — `Topfi`, HN, 2026-08-29. 자체 평가 데이터 미공개.
25. **"Claude Code doesn't validate it - it just silently ignores the skill"** — `anotherCodder`, HN, 2026-02-12. 🕒 특정 버전 동작이므로 현재도 유효한지 재확인 필요.

---

## 수집 한계 (전체 총괄)

**접근 실패 플랫폼**
- **Reddit 전체** — 크롤러 차단. r/devops, r/sysadmin, r/ExperiencedDevs, r/MachineLearning, r/LocalLLaMA, r/cybersecurity, r/ITManagers, r/AI_Agents, r/msp **전부 미접근.** 이 리서치의 최대 결손이며, 특히 축 1(NHI 운영 일화)과 축 4(주니어 직무 불안)에 직접 타격.
- **X / Mastodon / LinkedIn 공개 포스트** — 미접근. "AI employee" 마케팅에 대한 냉소를 못 캤다.
- **Discord / Slack 공개 로그** — 미접근.
- **커리어리** — 검색에 한 건도 잡히지 않음.
- **Dev.to** — 검색에 나온 것은 NHI 관련 벤더성 글 2건뿐(dev.to/kapusto)이며, 실무자 토론이 아니라 제외.
- **Lobsters 개별 스레드** — 검색 인덱스는 읽었으나 스레드 페이지 404로 댓글 미확보. 관련 스토리 2건(mjg59의 "Securing agentic identity" 2026-07-06 / srlabs.de "We don't need to hack your AI Agent to hack your AI Agent" 2026-03-17)의 존재만 확인.
- **Stack Overflow / ServerFault** — 검색 시도했으나 이 주제에서 유의미한 토론 미발견.

**언어·플랫폼 편중**
- 확보한 인용의 **약 80%가 Hacker News**다. HN은 AI 회의론이 과대표되는 곳이라는 지적(`keeda`, 2026-03-28)이 이 문서 자체에 적용된다. **"커뮤니티 정서"를 "업계 정서"로 승격시키지 말 것.**
- 한국 커뮤니티 인용은 **GeekNews 4건 + OKKY 1건**으로, 요청받은 "충분한 비중"에 미달한다. GeekNews는 댓글 문화가 얕고(대부분 GN⁺ 봇 요약), OKKY·velog는 이 주제의 실무 토론이 희박하다. 한국 독자용 재료는 **인터뷰나 사내 자료로 보완해야 한다.**

**출처 품질 경고**
- A2A #1672(658댓글)는 자기 프로젝트 홍보 계정의 교차 게시 정황과 AI 생성 의심 문체가 짙다. **여론 근거로 쓰지 말고 설계 쟁점 자료로만 쓸 것.**
- NHI 관련 수치는 대부분 벤더 마케팅 콘텐츠 출처다. 커뮤니티 자료가 아니다.
- GeekNews의 GN⁺ 계정은 HN 의견을 요약하는 봇/편집 계정으로 보인다. GN⁺ 인용은 **2차 인용**이며 원 HN 댓글 확인이 필요하다.

**신선도 상태**
- 축 1의 표준 관련 자료(MCP/A2A/SPIFFE)는 **전부 2026-09-05 기준 미확정(open)** 이다. 책 탈고 직전 재확인 필수.
- 축 2의 Confluence 인용은 2019~2024년이다. 시점 명시 필수.
- 축 3의 MIT 95% 논쟁은 2025-08이다. "최근"이라 쓰지 말 것.
- 축 4의 AI 의무화 증언은 2025-04 ~ 2026-08에 분포한다. 2026년 것을 우선 쓰되 시점을 밝힐 것.
