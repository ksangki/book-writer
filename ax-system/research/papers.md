# 학술 리서치 — AX 체계 구축

검색 시점: **2026-09-05**
대상 독자: AX 실무 리더·기획자 (조직에 AI 체계를 실제로 세우는 사람)
수집 원칙: 이론을 위한 이론이 아니라 **설계 근거로 쓸 수 있는 실증** 우선. 프리프린트와 피어리뷰를 구분 표기.

**표기 규칙**
- `[PR]` = 피어리뷰 게재 (학회·저널)
- `[PP]` = 프리프린트 단독 (arXiv 등, 미검증)
- `[WP]` = 워킹페이퍼/기관 보고서 (NBER·SSRN·재단 등)
- `⚠️` = 서지 정보 또는 수치의 일부가 미확인 — 저술 전 재확인 필요
- 모든 항목에 발행일(연-월)과 "검색: 2026-09-05 기준" 적용

---

## 축 1 — 에이전트 등록·아이덴티티·거버넌스

### 핵심 논문

---

- **Chan, A., Ezell, C., Kaufmann, M., Wei, K., Hammond, L., Bradley, H., Bluemke, E., Rajkumar, N., Krueger, D., Kolt, N., Heim, L., & Anderljung, M. (2024). 「Visibility into AI Agents」.** `[PR]` ACM FAccT '24 (Conference on Fairness, Accountability, and Transparency). DOI: 10.1145/3630106.3658948. arXiv:2401.13138 (v1 2024-01-23 → **v6 2024-05-17**, 현재 버전). 검색: 2026-09-05 기준.
  - **핵심 주장:** AI 에이전트에 대한 위임이 늘어날수록 "어디서·왜·어떻게·누구에 의해 그 에이전트가 사용되는가"에 대한 정보 — 저자들이 **가시성(visibility)** 이라 부르는 것 — 이 거버넌스의 전제 조건이 된다. 가시성을 확보하는 수단을 세 범주로 나눈다: **(1) 에이전트 식별자(agent identifiers), (2) 실시간 모니터링(real-time monitoring), (3) 활동 로깅(activity logging)**. 각 수단을 중앙집중형 배포 맥락과 분산형 배포 맥락 양쪽에서 검토하고, 하드웨어·소프트웨어 제공자가 각각 어떤 지점에서 개입할 수 있는지 분석한다. 마지막으로 각 수단이 프라이버시와 권력 집중에 미치는 영향을 다룬다.
  - **이 책에 쓸 수 있는 부분:** 이 책이 제안하는 "에이전트를 조직에 등록한다(사번·계정·소유자·매니저)"는 실무 설계의 **학술적 정본**이 바로 이 세 축이다. 사번 = agent identifier, 매니저·소유자 = 책임 귀속을 위한 실시간 모니터링 주체, 감사 로그 = activity logging. 즉 이 책의 3종 세트가 임의 발명이 아니라 FAccT에서 피어리뷰된 프레임워크와 1:1 대응한다는 것을 보여줄 수 있다.
  - **인용 가능한 문장/수치:**
    - 저자들의 정의 그대로: 가시성이란 "**where, why, how, and by whom certain AI agents are used**"에 대한 정보다. → 한국어 번안: "어떤 에이전트가 **어디서·왜·어떻게·누구에 의해** 쓰이는가."
    - 세 범주 원어: agent identifiers / real-time monitoring / activity logging.
    - 논문 자체가 "increased delegation of commercial, scientific, governmental, and personal activities to AI agents ... may exacerbate existing societal risks and introduce new risks"라고 위임 확대를 리스크의 근원으로 명시한다.
  - **한계·반박:** 정책 제안 논문이며 **실증 실험이 없다**. 세 수단의 효과 크기를 측정한 데이터는 제시되지 않는다. 또 저자들 스스로 프라이버시 침해와 권력 집중(가시성 인프라를 쥔 쪽이 힘을 갖는 문제)을 반작용으로 인정한다 — 사내 도입 시 "감시로 인식되는" 축4의 문제와 정확히 맞물린다.
  - **독자 전달 제안:** "사번을 준다"는 말을 먼저 던지고, 그 다음에 "이건 내가 만든 말이 아니라 FAccT 논문의 agent identifier다"로 받는 순서가 좋다.

---

- **Chan, A., Wei, K., Huang, S., Rajkumar, N., Perrier, E., Lazar, S., Hadfield, G. K., & Anderljung, M. (2025). 「Infrastructure for AI Agents」.** `[PR]` Transactions on Machine Learning Research (TMLR) 게재 확정. arXiv:2501.10114 (v1 2025-01-17 → v2 2025-05-16 → **v3 2025-06-19**). 검색: 2026-09-05 기준.
  - **핵심 주장:** 인터넷이 HTTPS·DNS 같은 기반 프로토콜 위에서 돌아가듯, 에이전트 생태계도 **에이전트 인프라(agent infrastructure)** — 에이전트 상호작용을 매개·제약하는 외부 기술 시스템과 프로토콜 — 를 필요로 한다. 인프라의 기능을 셋으로 정의한다: **(1) 귀속(attribution)** — 행위·속성·정보를 특정 에이전트, 그 사용자, 또는 다른 행위자에게 귀속시키기, **(2) 상호작용 형성(shaping interactions)**, **(3) 유해 행위 탐지·구제(detecting and remedying harmful actions)**. 그 아래에 agent IDs, agent channels, OAuth for agents, 검증 가능한 자격 증명 등 구체 후보를 카탈로그화한다.
  - **이 책에 쓸 수 있는 부분:** **"agent ID"의 정의가 이 책의 사번 설계를 그대로 지지한다.** 논문은 agent ID를 "최소한 에이전트 인스턴스에 대한 고유 식별자, 그리고 잠재적으로 시스템 카드나 인증 같은 부가 정보를 담는 컨테이너"로 규정한다. 즉 사번은 숫자 하나가 아니라 **소유자·권한·인증 이력을 매다는 고리**여야 한다는 설계 원칙이 여기서 나온다.
  - **인용 가능한 문장/수치:**
    - 저자들의 비유가 강력하다: ID 유사 체계는 이미 여러 영역에 존재한다 — "**serial numbers on consumer products, tail numbers on aircraft, and registration numbers for businesses**"(소비재의 일련번호, 항공기의 기체등록번호, 사업자등록번호). 리스크·사고 관리를 가능하게 하기 위해서다.
    - 세 기능 원어: attributing / shaping / detecting and remedying.
    - "just as the Internet depends on foundational protocols, agent ecosystems will require comparable infrastructure."
  - **한계·반박:** 역시 **제안·의제 설정 논문**이다. 어느 인프라가 실제로 채택될지, 채택 비용이 얼마인지에 대한 실증이 없다. 저자들도 채택 challenge를 미해결 문제로 남긴다. 사내 도입 관점에서는 "표준이 아직 없다"는 것이 오히려 핵심 메시지 — 지금 세우는 사내 등록부가 나중에 표준으로 마이그레이션 가능하도록 설계해야 한다는 실무 함의로 쓸 수 있다.
  - **독자 전달 제안:** 항공기 기체등록번호 비유를 그대로 가져다 쓰면 비기술 임원 설득에 바로 먹힌다.

---

- **Chan, A. (2024). 「IDs for AI Systems」.** `[PP]` arXiv:2406.12137 (v1 2024-06-17, 최종 수정 **2024-10-28**). 피어리뷰 게재 확인 안 됨 — 프리프린트로 취급. 검색: 2026-09-05 기준.
  - **핵심 주장:** AI 시스템의 **인스턴스** 단위(예: Claude와의 특정 채팅 세션)로 ID를 부여하고, 그 ID에 연결된 정보를 상호작용 상대방이 조회할 수 있게 하자는 제안. AI ID는 **(1) 식별자(identifier)** 와 **(2) 속성(attributes)** 을 담는 컨테이너로 정의된다. 식별자는 인스턴스를 가리키는 고유 문자열이며 무작위 생성일 수도, 특정 패턴을 따를 수도 있다.
  - **이 책에 쓸 수 있는 부분:** **"에이전트에 사번을 준다면, 무엇의 사번인가?"** 라는 실무의 첫 난관에 답을 준다. 모델? 배포? 세션? 이 논문은 **인스턴스 단위**를 택한다. 조직 설계에서는 "역할 단위로 등록하되 실행 세션마다 하위 식별자를 발급"하는 절충으로 번역할 수 있다. 또 "ID가 필요한 지점"의 판단 기준도 준다.
  - **인용 가능한 문장/수치:**
    - 필요성의 근거: "AI systems are increasingly pervasive, yet **information needed to decide whether and how to engage with them may not exist or be accessible.** A user may not be able to verify whether a system has certain safety certifications."
    - 적용 우선순위: ID는 "settings where AI systems could have a large impact upon the world, such as in **making financial transactions or contacting real humans**"에서 가장 정당화된다. → 사내 등록 정책의 **티어링 근거**로 직접 인용 가능: 결제·대외 커뮤니케이션에 닿는 에이전트부터 등록하라.
    - 워터마크·콘텐츠 프로버넌스가 ID를 실어 나르는 매개가 될 수 있다는 연결 고리도 제시된다.
  - **한계·반박:** 프리프린트 단독. 인스턴스 단위 ID는 **양이 폭증**한다 — 세션마다 ID면 로그·저장 비용과 프라이버시 문제가 커진다. 저자도 이를 미해결로 둔다.

---

- **South, T., Marro, S., Hardjono, T., Mahari, R., Whitney, C. D., Greenwood, D., Chan, A., & Pentland, A. (2025). 「Authenticated Delegation and Authorized AI Agents」.** `[PP→PR]` arXiv:2501.09674 (v1 **2025-01-16**). ICML 2025에 「Position: AI Agents Need Authenticated Delegation」이라는 제목으로 포지션 페이퍼 채택 (OpenReview id: 9skHxuHyM4). **arXiv 제목과 ICML 게재 제목이 다르므로 인용 시 어느 쪽인지 명시할 것.** 검색: 2026-09-05 기준.
  - **핵심 주장:** 에이전트에게 **인증되고(authenticated)·인가되며(authorized)·감사 가능한(auditable) 권한 위임**을 제공하는 프레임워크를 제안한다. 새 프로토콜을 발명하지 않고 **기존 OAuth 2.0 / OpenID Connect를 에이전트 전용 자격 증명과 메타데이터로 확장**하는 것이 핵심 설계 결정이다 — 기존 인증·웹 인프라와 호환성을 유지하기 위해서다. 여기에 더해, **자연어로 표현된 권한 부여를 감사 가능한 접근 제어 설정으로 번역**하는 방법을 제시한다.
  - **이 책에 쓸 수 있는 부분:** 이 책의 "에이전트에 계정을 준다"를 **기술적으로 실행 가능한 형태로** 못 박아준다. 요지는 **새 IAM을 만들지 말고 지금 쓰는 OAuth/OIDC를 확장하라**는 것. AX 리더가 보안팀과 처음 대화할 때 가장 먼저 꺼내야 할 논문이다. "자연어 권한 → 감사 가능한 접근 제어" 부분은 SOP를 권한으로 번역하는 축2와 직접 연결된다.
  - **인용 가능한 문장/수치:**
    - 문제 정의: "The rapid deployment of autonomous AI agents creates urgent challenges around **authorization, accountability, and access control** in digital spaces."
    - 설계 원칙: 사용자가 "**securely delegate and restrict the permissions and scope of agents while maintaining clear chains of accountability**"할 수 있어야 한다. → "책임의 사슬(chains of accountability)"은 이 책의 소유자·매니저 지정 규칙에 그대로 쓸 수 있는 표현이다.
    - 기존 표준과의 관계: OAuth 2.0·OpenID Connect를 "agent-specific credentials and metadata"로 확장하되 "maintaining compatibility with established authentication and web infrastructure."
  - **한계·반박:** ICML 게재 형태가 **포지션 페이퍼**다 — 즉 실험적 검증이 아니라 주장을 담은 글이다. 실제 배포 데이터나 성능 평가가 없다. 또 자연어 권한을 접근 제어로 번역하는 부분은 LLM 기반 번역의 오류율이 보고되지 않았다는 공백이 있다.
  - **참고 (표준 트랙, 학술 아님):** IETF에 「OAuth 2.0 Extension: On-Behalf-Of User Authorization for AI Agents」(draft-oauth-ai-agents-on-behalf-of-user-00) 인터넷 드래프트가 올라와 있으며 `requested_agent` 인가 요청 파라미터와 전용 grant type을 정의한다. ⚠️ **드래프트이며 표준이 아님 — 저술 시 "표준화 진행 중" 이상으로 쓰지 말 것.**

---

- **Kolt, N. (2025). 「Governing AI Agents」.** `[PP→PR]` arXiv:2501.07913. **101 Notre Dame Law Review (forthcoming)**. 최근 개정 2025-02-11. SSRN abstract 4772956. 검색: 2026-09-05 기준.
  - **핵심 주장:** AI 거버넌스를 **대리인 문제(principal-agent problem)** 의 경제학 이론과 **영미법의 대리(agency) 법리**로 재구성한다. AI 에이전트가 일으키는 문제를 세 갈래로 특징짓는다 — **정보 비대칭(information asymmetry), 재량권(discretionary authority), 충성(loyalty)**. 그리고 인간 대리인에게 통하던 전통적 해법(인센티브 설계, 모니터링, 신인의무)이 AI 에이전트에 적용될 때 왜 한계에 부딪히는지를 보인다.
  - **이 책에 쓸 수 있는 부분:** **"에이전트에 매니저를 붙인다"는 이 책의 설계에 가장 직접적인 이론적 근거.** 매니저를 붙이는 이유가 관리 취향이 아니라 대리인 문제 해결 장치라는 것 — 정보 비대칭을 줄이고, 재량권의 범위를 정하고, 이해 상충 시 누구의 이익을 따를지를 사전에 정하는 것. 조직도에 에이전트를 올린다는 발상의 **법학적 계보**를 여기서 끌어올 수 있다.
  - **인용 가능한 문장/수치:** 세 문제 축의 원어 — information asymmetry / discretionary authority / loyalty. 논문의 요지는 "conventional solutions to principal-agent problems"이 AI 에이전트에는 **그대로 통하지 않는다**는 것 (limitations를 명시적으로 논증).
  - **한계·반박:** 법학 논문이며 **미국법 중심**이다. 한국 조직·법제에 그대로 대응하지 않는다. 또 forthcoming 상태이므로 최종본에서 논지가 조정될 수 있다 — 인용 시 "101 Notre Dame L. Rev. (forthcoming)" 표기 필수.

---

- **Santoni de Sio, F., & Mecacci, G. (2021). 「Four Responsibility Gaps with Artificial Intelligence: Why they Matter and How to Address them」.** `[PR]` Philosophy & Technology, 34(4), 1057–1084. DOI: 10.1007/s13347-021-00450-x. 검색: 2026-09-05 기준.
  - **핵심 주장:** "책임 공백(responsibility gap)"은 **하나의 문제가 아니라 최소 네 개의 서로 얽힌 문제**다: **(1) 유책성(culpability) 공백, (2) 도덕적 책임(moral accountability) 공백, (3) 공적 책임(public accountability) 공백, (4) 능동적 책임(active responsibility) 공백.** 각 공백의 원인은 다르다 — 어떤 것은 기술적, 어떤 것은 **조직적·법적·윤리적·사회적**이다. 따라서 하나의 처방으로는 해결되지 않는다.
  - **이 책에 쓸 수 있는 부분:** 이 책이 던지는 "에이전트가 사고 치면 누가 책임지나"에 대한 **가장 정밀한 분해 도구**다. 네 공백을 조직 설계 언어로 번역하면: 유책성 → 징계·법적 책임 주체 지정, 도덕적 책임 → 소유자, 공적 책임 → 감사 로그·대외 설명 책임, 능동적 책임 → **사고가 나기 전에 예방할 의무를 진 사람** = 매니저. 특히 **네 번째 공백(능동적 책임)이 조직 설계로만 메울 수 있는 유일한 공백**이라는 점이 이 책의 핵심 논지와 정확히 겹친다.
  - **인용 가능한 문장/수치:**
    - "The responsibility gap is **not one problem but a set of at least four interconnected problems** — gaps in culpability, moral and public accountability, and active responsibility — caused by different sources, **some technical, others organisational, legal, ethical, and societal.**"
    - → 이 한 문장이 "기술로만 풀려는 시도가 왜 실패하는가"의 근거로 쓸 수 있다.
  - **한계·반박:** 철학 논문이다. **실증 데이터가 없고**, 네 공백의 경계가 실무에서 늘 선명하지는 않다. 또 "many hands problem"(책임이 여러 손에 분산되어 흐려지는 문제)을 책임 공백보다 더 근본적인 문제로 보는 후속 논의도 있다 — 병기하면 논쟁이 살아난다.

---

- **Nian, Y., Yuan, A., Zhang, H., Li, J., Li, L., Hu, X., Wei, H., Xiao, X., Xiao, C., & Zhao, Y. (2026). 「Auditable Agents」.** `[PP]` arXiv:2604.05485 (v1 **2026-04-07**, v2 2026-08-13). 프리프린트 — 피어리뷰 미확인. 검색: 2026-09-05 기준.
  - **핵심 주장:** 명제는 단순하고 강하다 — **"감사 가능성 없이는 어떤 에이전트 시스템도 책임질 수 없다(no agent system can be accountable without auditability)."** 감사 가능성을 다섯 차원으로 분해한다: **(1) 행위 복구 가능성(action recoverability), (2) 생애주기 커버리지(lifecycle coverage), (3) 정책 검사 가능성(policy checkability), (4) 책임 귀속(responsibility attribution), (5) 증거 무결성(evidence integrity).** 그리고 에이전트 시스템을 위한 **Auditability Card**(모델 카드의 감사 버전)를 제안한다.
  - **이 책에 쓸 수 있는 부분:** **등록만으로는 부족하고 로그가 있어야 한다**는 주장의 최신 근거. 특히 "오버헤드가 커서 못 한다"는 현장 반론에 대한 **정량 반박**을 준다. 다섯 차원은 사내 에이전트 감사 체크리스트로 그대로 옮겨 쓸 수 있다.
  - **인용 가능한 문장/수치:**
    - **"617 security findings"** — 오픈소스 에이전트 프로젝트 **6개**를 조사한 결과. 저자들의 해석: 감사 가능성의 기본 전제조건조차 생태계 전반에 구현되어 있지 않다.
    - **"8.3 ms median overhead"** — 변조 탐지 가능한 기록(tamper-evident records)과 사전 실행 중재(pre-execution mediation)를 추가했을 때의 중앙값 오버헤드. → "감사 붙이면 느려진다"는 반론에 대한 직접 반증 수치.
    - 통제 실험 결과: 전통적 로깅이 실패하는 상황에서도 **책임 귀속에 필요한 정보는 부분적으로 복구 가능**했다.
  - **한계·반박:** **프리프린트다.** 617건은 6개 프로젝트 표본이며 프로젝트 선정 편향 가능성이 있다. 8.3 ms는 특정 실험 환경의 중앙값이므로 사내 워크로드에 그대로 대입할 수 없다 — 인용 시 "이 실험 조건에서"를 반드시 붙일 것.

---

- **Kaptein, M., Khan, V.-J., & Podstavnychy, A. (2026). 「Runtime Governance for AI Agents: Policies on Paths」.** `[PP]` arXiv:2603.16586 [cs.AI] (**2026-03-17**). 프리프린트. 검색: 2026-09-05 기준.
  - **핵심 주장:** 에이전트는 비결정적이라서 **설계 시점에 완전히 통제할 수 없다.** 따라서 거버넌스의 중심 대상은 정적 권한이 아니라 **실행 경로(execution path)** 여야 한다. 컴플라이언스 정책을 **(에이전트 아이덴티티, 실행 이력, 제안된 행위, 조직 맥락) → 위반 확률**로 매핑하는 함수로 형식화한다. 이 틀 안에서 프롬프트 수준 지시와 정적 접근 제어는 **더 넓은 런타임 거버넌스 모델의 특수 사례**로 드러난다.
  - **이 책에 쓸 수 있는 부분:** **"등록 = 정적 권한 부여"라는 순진한 그림을 깨준다.** 사번과 계정을 발급했다고 끝이 아니라, 실행 이력에 의존하는 정책(예: "오늘 이미 3건 승인했으면 4번째는 사람 검토")은 런타임에서만 판정 가능하다. 축1의 등록 설계와 축4의 인간 감독 설계를 잇는 다리다. 조직 맥락(organizational context)이 정책 함수의 입력에 명시적으로 들어간다는 점이 이 책의 주제와 정확히 맞는다.
  - **인용 가능한 문장/수치:** "**the execution path is the central object for effective runtime governance**." 정책 함수의 네 입력: agent identity / execution history / proposed actions / organizational context. EU AI Act에서 영감을 받은 정책 예시와 참조 구현이 함께 제공된다.
  - **한계·반박:** 프리프린트. 저자들 스스로 **리스크 캘리브레이션(위반 확률을 어떻게 신뢰성 있게 추정하는가)과 집행 한계**를 미해결 문제로 남긴다. 실전 배포 데이터 없음.

---

- **Otsuka, T., Toyoda, K., & Leung, A. (2026). 「AI Identity: Standards, Gaps, and Research Directions for AI Agents」.** `[PP]` arXiv:2604.23280 (**2026-04-25**). 프리프린트. 검색: 2026-09-05 기준.
  - **핵심 주장:** **AI 아이덴티티**를 이렇게 정의한다 — "에이전트가 **무엇이라고 선언된 것**과 **무엇을 하는 것으로 관찰되는 것** 사이의 지속적 관계이며, 그 둘이 어느 시점에서든 서로 대응한다는 신뢰의 정도로 한정된다." 인간 아이덴티티와 AI 아이덴티티를 **기질(substrate)·지속성(persistence)·검증 가능성(verifiability)·법적 지위(legal standing)** 네 차원에서 대조해, 인간용 프레임워크를 에이전트에 직수입할 때 왜 체계적으로 실패하는지를 보인다. 현행 기술·규제 문서를 검토한 결론은 **비결정적이고 경계를 넘나드는 자율 개체를 다스릴 수 있는 표준은 아직 없다**는 것.
  - **다섯 가지 결정적 공백:** (1) 의미적 의도 검증(semantic intent verification), (2) 재귀적 위임의 책임(recursive delegation accountability), (3) 에이전트 아이덴티티 무결성(agent identity integrity), (4) 거버넌스 불투명성과 집행(governance opacity and enforcement), (5) 운영 지속 가능성(operational sustainability).
  - **이 책에 쓸 수 있는 부분:** 이 책이 "사람과 똑같이 사번을 준다"고 말할 때 **바로 따라붙는 반론**을 미리 처리해준다. 인사 시스템을 그대로 복사하면 안 되는 지점이 어디인지(특히 지속성과 법적 지위) 명확하다. **재귀적 위임** — 에이전트가 다른 에이전트를 호출할 때의 책임 — 은 이 책이 반드시 다뤄야 할 공백이다.
  - **인용 가능한 문장/수치:** 정의 원문 — AI Identity is "the continuous relationship between **what an AI agent is declared to be** and **what it is observed to do**, bounded by the confidence that those two things correspond at any given moment." 저자들의 결론: 공백은 **구조적(structural)** 이며 "engineering efforts alone are insufficient" — 엔지니어링만으로는 부족하고 기초 연구가 필요하다.
  - **한계·반박:** 프리프린트, 2026-04 시점 표준 지형 기준이므로 **신선도 민감**하다. 실증 없음, 개념 정리와 갭 분석 위주.

---

- **Hübner, J. F., Sichman, J. S., & Boissier, O. (2002). 「A Model for the Structural, Functional, and Deontic Specification of Organizations in Multiagent Systems」(MOISE+).** `[PR]` SBIA 2002, Lecture Notes in Computer Science (LNAI) vol. 2507, Springer. DOI: 10.1007/3-540-36127-8_12. 검색: 2026-09-05 기준.
  - **핵심 주장:** 조직을 명시적으로 표현하는 다중 에이전트 시스템은 보통 **기능(functioning)** 또는 **구조(structure)** 중 한쪽에만 집중하는데, 둘 다 다루는 것이 훨씬 생산적이다. MOISE+는 조직을 **세 차원**으로 명세한다: **(1) 구조적 차원(structural)** — 역할(role), 역할 간 상속 링크, 그룹(group), **(2) 기능적 차원(functional)** — 목표 달성을 위한 전역 계획(global plans)과 미션(mission), **(3) 규범적/의무론적 차원(deontic)** — 어느 역할이 어느 미션에 대해 **의무(obligation)** 또는 **허가(permission)** 를 갖는지.
  - **이 책에 쓸 수 있는 부분:** **"에이전트를 조직에 등록한다"는 발상의 학술적 계보가 2002년까지 거슬러 올라간다는 것 — 이 책의 가장 강력한 정당화 카드 중 하나.** LLM이 나오기 20년 전에 이미 다중 에이전트 연구자들은 "역할·그룹·의무"로 에이전트 조직을 명세했다. 이 책의 등록 스키마(소유자·매니저·권한)는 MOISE+의 structural/deontic 차원의 실무 버전이다. 특히 **deontic 차원 = 권한 부여**가 별도 차원으로 분리되어야 한다는 통찰이 실무 설계에 직접 적용된다.
  - **인용 가능한 문장/수치:** 세 차원 원어 — structural / functional / deontic. 역할의 기능에 대한 정리: 역할은 "**constrain the individual behaviors of the agents**", 조직 링크는 "**regulate the social exchanges between these agents**", 그룹은 "**constrain the layout of agents involved in strong interactions**". 후속 연구(MOISE+ 확장)는 **규범 명세를 강제하기 위한 제재(sanctions)** 를 통합했다.
  - **재조직화(reorganization) 메커니즘:** MOISE+의 재조직 프로세스는 **OrgManager 역할**을 맡은 에이전트가 전체 재구성을 조율하고, **Designer 역할**을 맡은 에이전트가 현 구조를 분석해 더 나은 구조를 제안하는 특수 그룹 구조를 형성해야 한다. → 이 책의 "에이전트 조직을 누가 관리하는가"에 20년 전 답이 있다.
  - **한계·반박:** **LLM 이전의 심볼릭 MAS 연구**다. 당시 에이전트는 명세된 대로만 행동하는 결정적 프로그램이었고, LLM 에이전트의 비결정성·프롬프트 취약성은 전제에 없다. 그래서 deontic 명세만으로는 부족하고 런타임 거버넌스(Kaptein et al. 2026)가 필요하다. **고전으로 인용하되 "그대로 적용 가능"이라고 쓰면 안 된다.**
  - **관련 후속:** Hübner, Sichman, Boissier, 「Developing organised multi-agent systems using the MOISE+ model: programming issues at the system and agent levels」, *International Journal of Agent-Oriented Software Engineering*, 2007. DOI: 10.1504/IJAOSE.2007.016266.

---

- **Dignum, V. (2004). 「A Model for Organizational Interaction: Based on Agents, Founded in Logic」(OperA).** `[PR-thesis]` PhD dissertation, Utrecht University / Dutch Research School for Information and Knowledge Systems (SIKS), 2004. ⚠️ **부제("Based on Agents, Founded in Logic")는 2차 출처 기반 — 인용 전 원문 표제지 확인 필요.** 검색: 2026-09-05 기준.
  - **핵심 주장:** 에이전트 사회(agent society)를 **전역 조직 특성**과 **개별 에이전트의 목표·역량**을 함께 담는 개념 틀로 모형화한다. 사회를 서로 연결된 세 모델로 기술하며, 그중 **조직 모델(organizational model)** 이 에이전트 사회를 **역할(roles)·제약(constraints)·상호작용 규칙(interaction rules)** 으로 기술한다.
  - **이 책에 쓸 수 있는 부분:** MOISE+가 "구조와 의무"라면 OperA는 **"조직의 목표와 개별 에이전트의 목표가 다를 수 있다"** 는 긴장을 정면으로 다룬다 — 조직이 원하는 것과 에이전트(그리고 그 에이전트를 돌리는 개인)가 원하는 것이 어긋나는 문제. 바텀업 실험을 탑다운 체계로 전향할 때 정확히 이 긴장이 터진다.
  - **인용 가능한 문장/수치:** 조직 모델은 에이전트 사회를 "in terms of **roles, constraints and interaction rules**"로 기술한다.
  - **한계·반박:** 학위 논문이며 접근성이 낮다. MOISE+와 마찬가지로 심볼릭 MAS 시대의 산물.
  - **계보 메모:** OperA(Dignum 2004)와 HARMONIA(Vázquez-Salceda 2003)에서 **OMNI** 모델이 파생되었다 — Vázquez-Salceda, Dignum & Dignum, 「OMNI: Introducing Social Structure, Norms and Ontologies into Agent Organizations」, Springer LNCS. ⚠️ OMNI의 정확한 권·페이지 미확인.

---

- **Esteva, M., Rodríguez-Aguilar, J. A., Sierra, C., Garcia, P., & Arcos, J. L. (2001). 「On the Formal Specification of Electronic Institutions」.** `[PR]` Agent Mediated Electronic Commerce, LNCS/LNAI vol. 1991, pp. 126–147. Springer, Heidelberg. ⚠️ **2차 출처(다른 논문의 참고문헌) 기반 — 권·페이지 재확인 권장.** 검색: 2026-09-05 기준.
  - **관련 구현:** Esteva, M., Rodríguez-Aguilar, J. A., Rosell, B., & Arcos, J. L. (2004). 「AMELI: An Agent-based Middleware for Electronic Institutions」. `[PR]` AAMAS 2004, vol. 1, pp. 236–243. ACM, New York.
  - **핵심 주장:** **전자 제도(electronic institution)** — 에이전트들이 상호작용할 때 지켜야 하는 규범과 프로토콜을 **형식적으로 명세**하고, 그 명세를 **런타임에 강제하는 미들웨어**(AMELI)로 실행한다. 즉 "규칙을 문서로 쓰는 것"과 "규칙이 실제로 강제되는 것"을 분리하지 않는다.
  - **이 책에 쓸 수 있는 부분:** SOP를 문서로만 두지 말고 **실행 환경이 강제하게 하라**는 이 책의 주장에 대한 20년 전 선례. 축2의 "적힌 절차와 실제 수행의 간극"(Feldman & Pentland)에 대한 **공학적 응답**이 바로 electronic institutions다. 두 계보를 나란히 놓으면 좋은 장면이 나온다.
  - **한계·반박:** 형식 명세의 작성 비용이 크다. 규칙이 자주 바뀌는 조직에서는 명세 유지가 병목이 된다. ⚠️ 서지 재확인 필요.

---

- **Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D., & Gebru, T. (2019). 「Model Cards for Model Reporting」.** `[PR]` FAT* '19 (Conference on Fairness, Accountability, and Transparency), 2019-01-29~31, Atlanta, GA. DOI: 10.1145/3287560.3287596. arXiv:1810.03993. 10페이지. 검색: 2026-09-05 기준.
  - **핵심 주장:** 배포되는 머신러닝 모델에는 **성능 특성을 기술한 문서가 함께 따라와야 한다**. 그 문서 형식을 **모델 카드(model card)** 로 제안한다. 핵심은 전체 평균 성능이 아니라 **하위 집단별 성능(disaggregated evaluation)** 을 밝히는 것, 그리고 **의도된 사용처와 의도되지 않은 사용처**를 명시하는 것.
  - **이 책에 쓸 수 있는 부분:** 에이전트 등록부의 **필수 필드 설계에 그대로 쓸 수 있는 원형**. 모델 카드가 "이 모델은 무엇이고 어디까지 쓸 수 있는가"를 문서화했듯, 에이전트 등록은 "이 에이전트는 무엇이고 **어디까지 권한이 있는가**"를 문서화한다. 특히 **intended use / out-of-scope use** 구분은 에이전트 권한 명세의 필드로 직수입 가능하다.
  - **인용 가능한 문장/수치:** "recommends that released machine learning models be accompanied by documentation detailing their performance characteristics." 카드의 통상 구성: 모델 상세, 의도된 사용, 요인(factors), 지표, 평가 데이터, 학습 데이터, 정량 분석, 윤리적 고려, 주의사항.
  - **한계·반박:** 모델 카드는 **자발적 공시**이며 강제력이 없다. 실제로 발행률이 낮고 품질 편차가 크다는 후속 비판이 있다 — 아래 AI Agent Index의 수치가 그 증거다. 이 책의 등록부가 "문서를 만들자"에서 멈추면 똑같은 운명이라는 경고로 쓸 것.

---

- **McGregor, S. (2021). 「Preventing Repeated Real World AI Failures by Cataloging Incidents: The AI Incident Database」.** `[PR]` Proceedings of the AAAI Conference on Artificial Intelligence, 35(17), 15458–15463. arXiv:2011.08512. 검색: 2026-09-05 기준.
  - **핵심 주장:** 항공 같은 성숙 산업은 **실제 실패를 사고 데이터베이스에 축적**해 안전을 개선해왔다. AI에도 같은 장치가 필요하다. AI Incident Database는 산업·비영리 협력체가 시작한 사고 수집 체계이며, 패싯 검색과 전문 검색을 지원한다.
  - **인용 가능한 수치:** 논문 시점 기준 **1,000건 이상의 사고 보고(incident reports)** 가 아카이브되어 있다. ⚠️ **이는 2021년 기준 수치다. 현재(2026) 숫자를 쓰려면 반드시 재확인할 것.**
  - **이 책에 쓸 수 있는 부분:** 항공 비유가 Chan et al. 2025의 tail number 비유와 이어진다 — **등록번호가 있어야 사고 기록이 쌓이고, 사고 기록이 쌓여야 안전이 개선된다.** 사내에서도 에이전트 사고 원장(incident log)을 등록부와 같은 키로 묶어야 한다는 설계 원칙의 근거.
  - **한계·반박:** 공개 사고 DB는 **보고 편향**이 크다 — 언론에 난 것만 들어온다. 사내 사고는 대부분 보고되지 않는다. 이 편향 자체가 "사내 등록·로깅이 왜 필요한가"의 논거가 된다.

---

- **Casper, S. 외 (2025). 「The AI Agent Index」.** `[PP]` arXiv:2502.01635 (2025-02). 프리프린트. ⚠️ **전체 저자 명단 미확인 — 인용 시 arXiv 페이지에서 확인할 것.** 검색: 2026-09-05 기준.
  - **핵심 주장:** 현재 배포된 **에이전틱 AI 시스템의 기술 구성·의도된 용도·안전 기능을 문서화한 최초의 공개 데이터베이스**. 폭보다 깊이를 택해, 가장 널리 배포된 **30개 에이전틱 시스템**을 **6개 범주**(법적 사항, 기술적 역량, 자율성·통제, 생태계 상호작용, 평가, 안전)로 심층 기록한다. 각 시스템의 구성 요소(기반 모델, 추론 구현, 도구 사용), 응용 도메인, 리스크 관리 관행(평가 결과, 가드레일)을 공개 정보와 개발사 서신을 근거로 정리했다.
  - **이 책에 쓸 수 있는 부분:** **"등록부는 만들 수 있다"의 실존 증명.** 외부 연구자도 30개 시스템을 6개 범주로 정리해냈다면, 조직이 자기 에이전트를 등록하는 것은 훨씬 쉬운 일이다. 6개 범주는 사내 등록 스키마의 초안으로 바로 쓸 수 있다.
  - ⚠️ **주의 — 수치 출처 불명확:** 검색 과정에서 "공개 문서 제공 70.1%, 코드 공개 49.3%, 공식 안전 정책 공시 19.4%, 외부 안전 평가 보고 10% 미만"이라는 수치가 확인되었으나, 이것이 **arXiv:2502.01635(2025년판)** 의 수치인지 **arXiv:2602.17753 「The 2025 AI Agent Index: Documenting Technical and Safety Features of Deployed Agentic AI Systems」(2026년판)** 의 수치인지 판별되지 않았다. **본문에 쓰려면 두 논문 중 어느 쪽인지 확정한 뒤 인용할 것.** 확정만 되면 "공시는 절반, 안전 정책은 5분의 1"이라는 강력한 수치가 된다.

---

- **Atkinson, D. I., & O'Bryan, J. E. (2026). 「Government AI Use as a Monitoring Primitive: A Public Document Pilot Study」.** `[PP→워크숍]` arXiv:2607.04543 (**2026-07-05**), 34페이지. **ICML 2026 Workshop on Technical AI Governance 채택.** 검색: 2026-09-05 기준.
  - **핵심 주장:** 정부 문서에서 **언어모델의 흔적을 탐지**하는 방법을 만들고, 미국·중국 정부의 공개 문서 스트림 10개에 적용했다. 요지는 **선언이 아니라 실제 행동에서 AI 사용을 측정**한다는 것 — "lightweight, externally reproducible, and based on **revealed behavior rather than stated intent**."
  - **핵심 수치:** **2026년 기준, 10개 소스 중 4개에서 AI 보조 작성의 통계적으로 유의한 징후**가 나타났다. **2021년 기준선은 일관되게 0에 가까웠다.** 패턴은 정부별로 달랐다 — 미국의 신호는 정책 작업의 **하류(downstream) 발간물**에 몰렸고, 중국의 신호는 정책 작업 **자체에 더 가까이** 몰렸다.
  - **이 책에 쓸 수 있는 부분:** **"등록되지 않은 사용은 이미 일어나고 있다"** 는 축3 shadow AI 논지의 **학술적 측정 사례**. 공식 발표를 믿지 말고 산출물의 흔적을 보라는 방법론 자체가, 사내 AX 성숙도를 "몇 명이 쓴다고 답했나"가 아니라 "산출물에 흔적이 있나"로 재라는 실무 제안으로 번역된다.
  - **한계·반박:** **파일럿 연구**이며 프리프린트다. LLM 텍스트 탐지는 오탐·미탐이 알려진 난제이므로 절대 수치가 아니라 **추세(2021 ≈ 0 → 2026 4/10)** 로만 인용해야 한다.

---

- **Miller, M. S., Yee, K.-P., & Shapiro, J. (2003). 「Capability Myths Demolished」.** `[TR]` Technical Report SRL2003-02, Johns Hopkins University Systems Research Laboratory. 검색: 2026-09-05 기준.
  - **핵심 주장:** 능력 기반 보안(capability-based security)에 대한 세 가지 통념을 반박한다: **(1) 동등성 신화(Equivalence Myth)** — ACL 시스템과 capability 시스템은 형식적으로 동등하다, **(2) 봉쇄 신화(Confinement Myth)** — capability 시스템은 봉쇄를 강제할 수 없다, **(3) 취소 불가 신화(Irrevocability Myth)** — capability 기반 접근은 취소할 수 없다. 세 모델과 일곱 가지 보안 속성으로 분석해, 순수 capability 시스템이 ACL 시스템 대비 유의한 장점을 갖는다고 결론짓는다.
  - **이 책에 쓸 수 있는 부분:** 에이전트 권한 설계에서 **"역할별 ACL"이 왜 부족한가**의 고전적 근거. 에이전트는 다른 에이전트를 호출하고 권한을 전달한다 — 이 **위임 사슬**을 ACL로 표현하기가 어렵다는 것이 capability 모델이 다시 주목받는 이유다. 축1의 재귀적 위임 공백(Otsuka et al. 2026)과 직접 연결된다.
  - **한계·반박:** 2003년 기술 보고서이며 **피어리뷰 학회 논문이 아니다.** 논쟁적 문헌이고 반론도 존재한다. 고전 계보로만 쓰고 "정설"로 쓰지 말 것.

---

- **South, T., Nagabhushanaradhya, S. 외 (총 19인 공저) (2025). 「Identity Management for Agentic AI: The new frontier of authorization, authentication, and security for an AI agent world」.** `[백서]` **OpenID Foundation Whitepaper 2025**, arXiv:2510.25819 [cs.CR] (**2025-10-29**, v1). 라이선스 CC BY-SA 4.0. 검색: 2026-09-05 기준.
  - **핵심 주장:** 에이전트 확산에 따른 보안 과제를 정리한 **표준화 기구 백서**. 현행 에이전트 중심 프로토콜(MCP 등)이 인증·인가 모범 사례의 명확화를 요구하고 있다고 진단하고, 단기(현존 에이전트 보안)와 장기(확장 가능한 접근 제어, 에이전트 중심 아이덴티티 체계, AI 워크로드 구분, 위임 권한 프레임워크) 과제를 나눈다.
  - **이 책에 쓸 수 있는 부분:** **"표준이 어디까지 왔는가"의 스냅샷.** OpenID Foundation·AI Identity Management Community Group·Stanford Loyal Agents Initiative가 참여했다는 사실 자체가, 이 책의 등록·계정 설계가 업계 표준 흐름과 같은 방향임을 보여준다. 사내 IAM 팀 설득 자료로 유용하다.
  - **한계·반박:** **백서이지 피어리뷰 논문이 아니다.** 표준 기구 문서 특유의 합의적 서술이며 실증 평가가 없다. 2025-10 시점 기준이므로 **신선도 민감** — 인용 시 "2025년 10월 기준"을 반드시 붙일 것.

---

- **Kraprayoon, J. 외 / IAPS (2025). 「AI Agent Governance: A Field Guide」.** `[보고서]` arXiv:2505.21808 (**2025-05**). Institute for AI Policy and Strategy (IAPS), 2025-04 발행. ⚠️ **전체 저자 명단 미확인 — arXiv 페이지에서 확인 후 인용할 것.** 검색: 2026-09-05 기준.
  - **핵심 주장:** 에이전트 거버넌스 분야의 입문 지도. 개입 수단을 **5분류 taxonomy**로 정리한다: **정렬(Alignment) / 통제(Control) / 가시성(Visibility) / 보안·견고성(Security & robustness) / 사회적 통합(Societal integration).** 에이전트는 계획하고 기억하고 실행하므로, 콘텐츠 필터와 배포 전 평가 같은 고전적 안전 장치만으로는 부족하며 **추적을 위한 ID와 로그, 피해 통제를 위한 롤백·셧다운, 봉쇄를 위한 샌드박싱·접근 제어, 책임 프레임워크**가 함께 필요하다고 본다.
  - **인용 가능한 문장/수치:** 분야 현황에 대한 진단이 인상적이다 — 에이전트 거버넌스 질문과 개입 수단의 탐색은 **"in their infancy"** 이며, **극소수의 연구자들**(주로 시민사회 조직, 공공 연구기관, 프런티어 AI 기업)만이 이 문제를 다루고 있다. → "아직 아무도 정답을 모른다, 그러니 지금 세우는 사내 체계가 곧 실험이다"는 이 책의 톤과 잘 맞는다.
  - **한계·반박:** 정책 연구소 보고서이며 **피어리뷰 아님.** 규범적 제안 위주.

---

### 축 1 커버리지

**확보한 것**
- 에이전트 등록·식별의 정본 프레임워크 3종 (Chan 2024 Visibility / Chan 2025 Infrastructure / Chan 2024 IDs) — 이 책의 "사번" 설계에 대한 피어리뷰 근거 확보 (Visibility는 FAccT, Infrastructure는 TMLR)
- 계정·권한의 기술 기반: OAuth/OIDC 확장 (South et al. 2025, ICML 포지션) + OpenID Foundation 백서 + capability 고전 (Miller et al. 2003)
- 책임 귀속 이론: 네 가지 책임 공백 (Santoni de Sio & Mecacci 2021, P&T) + 대리인 문제 법리 (Kolt, Notre Dame L. Rev. forthcoming) — **"매니저를 붙이는 이유"의 이중 근거**
- 감사·로깅: Auditable Agents (5차원 + 8.3ms 오버헤드 수치), Model Cards (문서화 원형), AI Incident Database (사고 원장 계보)
- 조직 이론적 MAS 계보: MOISE+ (구조·기능·의무 3차원, 2002) / OperA (2004) / electronic institutions (2001·2004) — **"에이전트를 조직에 등록한다"의 20년 계보**
- 등록부의 실존 증명·정책 평가: AI Agent Index (30개 시스템 6범주), 미 연방기관 AI use case inventory 실태 (아래 축3 참조), 정부 AI 사용의 행동 기반 측정 (Atkinson & O'Bryan 2026)
- 런타임 거버넌스: 정적 권한만으로 부족하다는 형식화 (Kaptein et al. 2026)
- 최신 갭 분석: AI Identity 5대 공백 (Otsuka et al. 2026) — 특히 **재귀적 위임 책임**

**비어 있는 것 (후속 리서치 권장)**
- **SPIFFE/SPIRE 워크로드 아이덴티티의 피어리뷰 평가 논문이 없다.** 검색으로 확인된 것은 arXiv 프리프린트(2504.14760, 2504.14761, 2504.14777, 2504.17759)와 벤더 문서뿐이다. SPIFFE 자체는 CNCF 프로젝트이자 사실상 표준이므로, **학술 인용 대신 공식 스펙 문서를 1차 출처로 쓰는 편이 정확하다** — web-researcher에게 이관 권장.
- **Verifiable Credentials / DID의 에이전트 적용**에 대한 피어리뷰 실증을 확보하지 못했다. W3C VC/DID 권고안 자체(표준 문서)로 대체 필요.
- **Confidential computing 기반 attestation**을 에이전트 아이덴티티에 적용한 학술 평가 미확보.
- **EU AI Act 데이터베이스에 대한 본격 학술 평가 논문**을 특정하지 못했다. 확인된 것은 관련 arXiv 프리프린트(2501.04014 AICat, 2512.13907 high-risk 검증)와 법률 해설 사이트뿐이다. ⚠️ **본문에서 EU 데이터베이스를 다룰 경우 법령 원문(Art. 49, Art. 71 등)을 직접 인용하고 학술 평가는 보류할 것.**
- 한국 조직 맥락의 에이전트 거버넌스 실증은 전무하다 (전 세계적으로도 부족).

---

## 축 2 — SOP·절차·프로세스의 형식화

### 핵심 논문

---

- **Feldman, M. S., & Pentland, B. T. (2003). 「Reconceptualizing Organizational Routines as a Source of Flexibility and Change」.** `[PR]` Administrative Science Quarterly, 48(1), 94–118. DOI: 10.2307/3556620. 검색: 2026-09-05 기준.
  - **핵심 주장:** 조직 루틴은 관성의 원천이라는 통념을 뒤집는다. Latour의 **ostensive / performative** 구분을 조직 루틴에 적용해, 루틴이 **안정의 원천이자 동시에 변화의 원천**임을 이론화한다. **ostensive(명시적) 측면**은 우리가 보통 "구조"라고 부르는 것 — 적힌 절차, 사람들이 머릿속에 갖고 있는 루틴의 관념. **performative(수행적) 측면**은 특정 사람들이 특정 시간·장소에서 실제로 하는 구체적 행위. 둘의 관계가 핵심이다: **ostensive는 사람들이 특정 수행을 안내·설명·참조할 수 있게 하고, performative는 ostensive를 창조·유지·수정한다.**
  - **이 책에 쓸 수 있는 부분: 이 책의 가장 중요한 이론적 기둥 중 하나.** "SOP에서 출발한다"고 할 때, 그 SOP는 ostensive 측면일 뿐이다. **적힌 절차와 실제 수행 사이에는 원리적으로 간극이 있다** — 이건 사람들이 게을러서가 아니라 루틴의 구조 자체가 그렇다. 따라서:
    - (a) SOP를 그대로 에이전트에 넣으면 **실제로 일이 되는 방식이 아니라 일이 된다고 적힌 방식**을 자동화하게 된다.
    - (b) 반대로 이 간극은 **자원**이기도 하다 — performative가 ostensive를 갱신하는 경로가 있어야 SOP가 살아 있는 문서가 된다. 에이전트 실행 로그가 그 갱신 경로가 될 수 있다 (프로세스 마이닝과 연결).
  - **인용 가능한 문장/수치:**
    - "The **ostensive** aspect of a routine embodies what we typically think of as **the structure**, while the **performative** aspect embodies **the specific actions, by specific people, at specific times and places**, that bring the routine to life."
    - "The ostensive aspect enables people to **guide, account for, and refer to** specific performances of a routine, and the performative aspect **creates, maintains, and modifies** the ostensive aspect of the routine."
    - "The relationship between ostensive and performative aspects of routines creates an **on-going opportunity for variation, selection, and retention** of new practices and patterns of action within routines."
  - **한계·반박:** 이론 논문이며 이 논문 자체는 대규모 실증이 아니다(사례 기반). 또 ostensive/performative 구분이 실무에서 늘 깔끔하게 나뉘지는 않는다. 그럼에도 ASQ 게재 + 폭넓은 후속 연구로 조직 이론의 표준 어휘가 되었다.
  - **독자 전달 제안:** 어려운 용어를 그대로 쓰지 말고 — **"적힌 절차"와 "실제로 하는 일"** 로 번역해서 먼저 던지고, 그 다음에 "학계에서는 이걸 ostensive와 performative라고 부른다"로 받는다. 그리고 AX 실무의 뼈아픈 장면과 붙인다: SOP 문서를 그대로 프롬프트에 넣었는데 결과가 엉망이었던 경험.

---

- **Adler, P. S., & Borys, B. (1996). 「Two Types of Bureaucracy: Enabling and Coercive」.** `[PR]` Administrative Science Quarterly, 41(1), 61–89. DOI: 10.2307/2393986. Sage Publications (Johnson Graduate School of Management, Cornell University 위탁 발행). 검색: 2026-09-05 기준.
  - **핵심 주장:** 관료제(형식화된 절차)가 직원을 **소외시킨다**는 평가와 **능력을 실어준다**는 평가가 정면으로 충돌해왔다. 저자들은 **워크플로 형식화(workflow formalization)의 개념화**를 새로 제시해 이 상반된 평가를 화해시킨다. 핵심은 형식화의 **양**이 아니라 **유형**이다 — **enabling(활성화형)** 형식화와 **coercive(강압형)** 형식화.
  - **이 책에 쓸 수 있는 부분: "탑다운 체계가 왜 어떤 조직에서는 살아나고 어떤 조직에서는 질식시키는가"에 대한 정본 답.** 이 책이 제안하는 SOP 기반 체계화는 잘못 설계되면 정확히 coercive 관료제가 된다 — 현장이 규칙을 피해 shadow AI로 도망가는 결과(축3)를 낳는다. Adler & Borys의 구분은 **"체계를 세우되 질식시키지 않는" 설계 원칙의 체크리스트**로 번역 가능하다.
  - **인용 가능한 문장/수치:** 논문의 자기 규정 — "proposes a conceptualization of **workflow formalization** that helps reconcile contrasting assessments of bureaucracy as **alienating or enabling** to employees."
  - ⚠️ **enabling 형식화의 네 가지 설계 특성**(통상 repair, internal transparency, global transparency, flexibility로 요약됨)은 이 논문의 핵심 실무 산출물이나, **이번 검색으로 원문 확인을 못 했다.** 본문에 네 특성을 쓰려면 **원문 pp. 61–89를 직접 확인할 것.** (공개 PDF 확인됨: faculty.marshall.usc.edu/Paul-Adler/research/ASQ copy-1.pdf)
  - **한계·반박:** 1996년 논문으로 제조업 맥락(NUMMI 등 Adler의 연구 배경)이 강하다. 지식노동·AI 맥락에 옮길 때의 검증은 별도로 필요하다.
  - **독자 전달 제안:** 이 책 전체의 반론 방어에 쓸 수 있다 — "체계를 세우자"고 하면 반드시 "관료제 만들지 마라"가 돌아온다. 그때 "관료제에는 두 종류가 있다"로 받는다.

---

- **Nonaka, I. (1994). 「A Dynamic Theory of Organizational Knowledge Creation」.** `[PR]` Organization Science, 5(1), 14–37. DOI: 10.1287/orsc.5.1.14. 검색: 2026-09-05 기준.
  - **핵심 주장:** 조직 지식은 **암묵지(tacit)와 형식지(explicit) 사이의 지속적 대화**를 통해 창조된다. 네 가지 지식 변환 모드 — **사회화(Socialization), 외재화(Externalization), 조합(Combination), 내면화(Internalization)**, 즉 **SECI** — 와, 개인에서 조직으로 지식을 증폭시키는 **지식 나선(knowledge spiral)** 을 제시한다.
  - **이 책에 쓸 수 있는 부분:** 이 책의 "SOP에서 출발한다"는 **외재화(Externalization) 단계**에 해당한다 — 사람 머릿속의 암묵지를 문서로 끄집어내기. 에이전트에 SOP를 넣는 것은 여기서 한 걸음 더 나간 것: **형식지를 기계가 실행 가능한 형태로 조합(Combination)** 하는 일. SECI를 AX 체계의 단계 지도로 쓰면 "왜 SOP 작성이 첫 단계인가"를 이론적으로 설명할 수 있다.
  - **인용 가능한 문장/수치:** 중심 명제 — 조직 지식은 "**a continuous dialogue between tacit and explicit knowledge**"를 통해 창조된다.
  - **한계·반박 (반드시 병기할 것):** 아래 Gourlay 2006 참조. **Nonaka 이론은 널리 인용되지만 실증적 뒷받침이 약하다는 비판을 정면으로 받았다.** 이 책이 SECI를 쓴다면 비판도 함께 제시해야 지적 정직성이 선다.

- **Gourlay, S. (2006). 「Conceptualizing Knowledge Creation: A Critique of Nonaka's Theory」.** `[PR]` Journal of Management Studies, 43(7), 1415–1436. DOI: 10.1111/j.1467-6486.2006.00637.x. 검색: 2026-09-05 기준.
  - **핵심 주장:** Nonaka의 네 변환 모드 명제는 **결함이 있다.** 네 모드 중 셋은 그럴듯해 보이지만, **더 단순하게 설명할 수 없는 증거로 뒷받침되는 모드는 하나도 없다.** 또 Nonaka의 개념 틀은 **본질적으로 암묵적인 지식(inherently tacit knowledge)을 누락**하고, **급진적으로 주관적인 지식 정의**를 쓴다 — 사실상 지식이 **관리자에 의해 창조**되는 셈이 된다. 대안으로, 서로 다른 종류의 지식은 서로 다른 종류의 **행동**에서 창조된다는 틀을 제시한다: 암묵지와 연결된 **비반성적 행동(non-reflectional behavior)**, 형식지와 연결된 **반성적 행동(reflective behavior)**.
  - **이 책에 쓸 수 있는 부분: 이 책에서 가장 중요한 실무적 함의 중 하나가 여기서 나온다 — "본질적으로 암묵적인 지식은 SOP로 안 나온다."** 모든 노하우를 문서화할 수 있다는 전제로 AX 체계를 설계하면 반드시 실패한다. 어디까지 형식화하고 어디부터는 사람에게 남길 것인가의 경계 설정이 설계의 일부가 되어야 한다.
  - **인용 가능한 문장/수치:** "**none are supported by evidence that cannot be explained more simply**" (네 모드 중 어느 것도 더 단순한 설명으로 대체 불가능한 증거를 갖지 못했다). 그리고 개념 틀이 "**omits inherently tacit knowledge**"라는 지적.
  - **한계·반박:** Gourlay의 대안 틀 역시 광범위한 실증 검증을 받은 것은 아니다. 이 항목은 **Nonaka와 반드시 병기**해서 논쟁으로 제시할 것 (아래 "상충하는 연구 결과" 섹션 참조).

---

- **van der Aalst, W. M. P. (2011 / 2016). 「Process Mining: Discovery, Conformance and Enhancement of Business Processes」(초판) / 「Process Mining: Data Science in Action」(2판).** `[PR-book]` Springer. 초판 2011, ISBN 978-3-642-19344-6, DOI: 10.1007/978-3-642-19345-3. 2판 2016, DOI: 10.1007/978-3-662-49851-4. 검색: 2026-09-05 기준.
  - **핵심 주장:** 프로세스 마이닝 분야를 정립한 정본 교과서. 세 가지 축 — **발견(discovery)**: 이벤트 로그에서 실제 프로세스 모델을 자동으로 뽑아내기, **적합성 검사(conformance checking)**: 적힌 모델과 실제 로그를 대조해 어긋난 지점을 찾기, **강화(enhancement)**: 실제 데이터로 모델을 개선하기. 이를 통해 병목을 탐지하고 실행 문제를 예측한다. 2판은 데이터 사이언스·빅데이터 맥락으로 확장되었고, 귀납적 마이닝 기법(inductive mining), 정렬(alignments) 개념, 대규모 프로세스 마이닝 장이 추가되었다.
  - **이 책에 쓸 수 있는 부분: 축2의 결정적 연결 고리.** Feldman & Pentland가 "적힌 절차와 실제 수행은 다르다"고 이론적으로 말했다면, **프로세스 마이닝은 그 간극을 실제로 측정하는 도구**다. conformance checking이 바로 ostensive와 performative를 기계적으로 대조하는 절차다. 이 책의 실무 제안으로 번역하면: **SOP를 쓰기 전에 로그부터 봐라. 사람들이 실제로 하는 절차를 발견한 다음, 그것을 SOP로 정련하고, 에이전트에 넣어라.** 그리고 에이전트가 돌기 시작하면 그 실행 로그로 다시 conformance를 검사한다 — 루프가 닫힌다.
  - **인용 가능한 개념 (용어 그대로):** discovery / conformance checking / enhancement. "check the conformance of processes, detect bottlenecks, and predict execution problems."
  - **한계·반박:** 프로세스 마이닝은 **양질의 이벤트 로그를 전제**한다. 로그가 없거나 케이스 ID·타임스탬프·액티비티가 정리되어 있지 않은 조직에서는 시작조차 못 한다 — 이 전제가 대부분의 조직에서 병목이다. 이것 자체가 "에이전트를 등록하고 로깅부터 세워야 하는" 이유가 된다.
  - **독자 전달 제안:** "지도를 그리기 전에 발자국을 봐라"로 요약하면 비기술 독자에게도 통한다.

- **Berti, A., Kourani, H., & van der Aalst, W. M. P. (2024). 「PM-LLM-Benchmark: Evaluating Large Language Models on Process Mining Tasks」.** `[PP]` arXiv:2407.13244 (2024-07). ⚠️ 피어리뷰 게재 여부 미확인. 검색: 2026-09-05 기준.
  - **핵심 주장:** LLM이 프로세스 마이닝 과제를 얼마나 수행할 수 있는지를 평가하는 벤치마크.
  - ⚠️ **수치 주의:** 검색 결과에 "**16개 최신 LLM을 20개의 다양한 비즈니스 프로세스로 구성된 맞춤 벤치마크로 평가**했고, **LLM 간 성능 편차가 크며 효율적 오류 처리와 생성된 모델의 품질 사이에 양의 상관**이 있었다"는 서술이 확인되었으나, 이 수치가 PM-LLM-Benchmark의 것인지 인접 논문의 것인지 **완전히 분리되지 않았다.** 본문 인용 전 arXiv:2407.13244 원문 확인 필수.
  - **관련 문헌 (계보용):** Berti, A., Schuster, D., & van der Aalst, W. (2023). 「Abstractions, Scenarios, and Prompt Definitions for Process Mining with LLMs: A Case Study」. BPM 2023, pp. 427–439. / Berti, A., Kourani, H., Häfke, H., Li, C.-Y., & Schuster, D. (2024). 「Evaluating Large Language Models in Process Mining: Capabilities, Benchmarks, and Evaluation Strategies」. BPMDS/EMMSAD 2024, Springer, DOI: 10.1007/978-3-031-61007-3_2. `[PR]`
  - **이 책에 쓸 수 있는 부분:** "프로세스 마이닝 + LLM"이 이미 학술 의제로 자리 잡았다는 증거. 프로세스 발견을 LLM에 맡길 수 있다는 낙관과, 성능 편차가 크다는 현실을 함께 제시할 수 있다.

---

- **Hong, S. 외 (2024). 「MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework」.** `[PR]` **ICLR 2024 (Oral).** arXiv:2308.00352 (v1 2023-08-01, v3). ⚠️ 제1저자 성명 표기는 arXiv 원문에서 확인할 것 (검색 결과에 전체 저자 명단 미노출). 검색: 2026-09-05 기준.
  - **핵심 주장:** **SOP를 프롬프트 시퀀스로 인코딩**해 LLM 다중 에이전트 협업에 인간의 효율적 워크플로를 이식한다. 조립 라인(assembly line) 패러다임으로 에이전트마다 역할을 배분하고 복잡한 과제를 하위 과제로 분해한다. 문제의식이 명확하다: LLM을 순진하게 연결하면 **연쇄적 환각(cascading hallucinations)** 으로 논리적 불일치가 생긴다. SOP는 **과제 분해와 효과적 조율**을 뒷받침하고, 각 팀원의 책임을 규정하며, **중간 산출물의 기준(standards for intermediate outputs)** 을 세운다.
  - **이 책에 쓸 수 있는 부분: "SOP에서 출발한다"는 이 책의 명제가 LLM 에이전트 연구에서도 독립적으로 도달한 결론이라는 증거.** ICLR Oral 채택 논문이 SOP를 핵심 기제로 삼았다는 사실은 강력한 방증이다. 특히 **"중간 산출물의 기준"** — SOP의 가치가 단계 나열이 아니라 **각 단계의 산출물이 무엇이어야 하는지를 못 박는 데** 있다는 통찰은 실무 SOP 작성 지침으로 직접 쓸 수 있다.
  - **인용 가능한 문장/수치:**
    - "MetaGPT encodes **Standardized Operating Procedures (SOPs) into prompt sequences** for more streamlined workflows, thus allowing agents with human-like domain expertise to **verify intermediate results and reduce errors**."
    - "More complex tasks face challenges through **logic inconsistencies due to cascading hallucinations** caused by naively chaining LLMs."
    - SOP는 "**outline the responsibilities of each team member, while establishing standards for intermediate outputs**."
  - **한계·반박:** MetaGPT의 SOP는 **소프트웨어 개발이라는 잘 정의된 도메인**의 절차다. 조직의 실제 SOP는 그만큼 깔끔하지 않다 (Feldman & Pentland의 간극). 또 2023~2024년 모델 기준 성능이며, 프레임워크 자체의 벤치마크 성능은 이후 모델 세대에서 재현성이 논쟁적이다.

---

- **Nandi, S. 외 (총 24인) (2025/2026). 「SOP-Bench: Complex Industrial SOPs for Evaluating LLM Agents」.** `[PP]` arXiv:2506.08119 [cs.AI] (v1 **2025-06-09**, v2 **2026-02-23**). Amazon Science 외. 코드: github.com/amazon-science/sop-bench. 검색: 2026-09-05 기준.
  - **핵심 주장:** **인간 전문가가 작성한 실제 SOP에서 도출한 2,000개 이상의 과제**를 **12개 비즈니스 도메인**(헬스케어, 물류, 금융, 콘텐츠 모더레이션 등)에 걸쳐 구축한 평가 벤치마크. 전문가가 진짜 SOP를 쓰고 AI가 도구·API·데이터셋 같은 부속물을 생성한 뒤 전부 사람이 검증하는 **인간-AI 협업 프레임워크**로 만들었다.
  - **핵심 수치 (v2 초록 기준):**
    - 도메인별 **과제 성공률 57% ~ 100%** — 편차가 매우 크다.
    - ReAct 방식 최고 성능: **Claude 4 Opus 72.4%**, Claude 4.5 Sonnet **63.3%**.
    - **어떤 모델-에이전트 조합도 전 도메인을 지배하지 못했다.**
    - 저자들의 결론: **"Newer models do not guarantee better performance"** — 프로덕션 업그레이드는 점진적 개선을 가정하지 말고 **경험적 검증을 거쳐야 한다.**
  - **이 책에 쓸 수 있는 부분: AX 실무 리더에게 가장 실용적인 수치.** "최신 모델로 갈아끼우면 좋아지겠지"라는 흔한 가정을 정면으로 반박한다. **에이전트를 등록하고 관리한다는 것은 곧 모델 교체를 관리한다는 뜻**이며, 등록부에 모델 버전과 성능 기준선을 함께 기록해야 하는 이유가 여기 있다. 또 도메인별 편차(57~100%)는 **에이전트를 도메인별로 등록·평가해야 한다**는 근거다.
  - **인용 가능한 문장/수치:** 위 수치 그대로. 특히 "newer models do not guarantee better performance"는 짧고 강해서 소제목으로도 쓸 만하다.
  - **한계·반박:** **프리프린트다.** 위 수치는 **v2(2026-02) 초록 기준**이며, 언급된 모델 라인업은 그 시점 기준이므로 **신선도 민감** — 인용 시 "2026년 2월 시점 평가"를 반드시 붙일 것. ⚠️ 저술 전 v2 원문에서 수치 재확인 권장. 또 벤치마크 과제는 실제 조직의 SOP를 모사한 것이지 실제 운영 환경이 아니다.
  - **관련 문헌 (동일 계열, 계보용):**
    - 「Agent-S: LLM Agentic workflow to automate Standard Operating Procedures」 arXiv:2503.15520 (2025-03) `[PP]` — 고객 응대 SOP 자동화. 3개의 과제별 LLM + Global Action Repository(GAR) + 실행 메모리 구조.
    - 「SOP-Maze: Evaluating Large Language Models on Complicated Business Standard Operating Procedures」 arXiv:2510.08942 (2025-10) `[PP]`
    - 「Compile, Then Page: Executable SOP Programs and a Capability-Gated Runtime for Procedural LLM Agents」 arXiv:2607.11346 (2026-07) `[PP]` — ⚠️ 미검증. **"SOP를 실행 가능한 프로그램으로 컴파일하고 능력 게이트 런타임에서 돌린다"는 접근은 이 책의 주제와 매우 가까우므로 후속 확인 권장.**

---

- **BPM × LLM 연구 지형 (개별 논문이 아니라 흐름으로 정리)**
  - **「Large Language Models for Business Process Management: Opportunities and Challenges」** (2023) `[PR]` — BPM 학회 계열. LLM이 BPM 생애주기 전 단계에 관여할 수 있으나 특히 **발견(discovery) 단계**에서 역할이 크다고 본다. ⚠️ 정확한 저자·게재처 미확인.
  - **「Towards a Benchmark for Large Language Models for Business Process Management Tasks」** arXiv:2410.03255 (2024-10) `[PP]`
  - **「Large Language Models to Enhance Business Process Modeling: Past, Present, and Future Trends」** arXiv:2604.14034 (2026-04) `[PP]` — 최신 동향 리뷰.
  - **「Evaluating large language models on business process modeling: framework, benchmark, and self-improvement analysis」** Software and Systems Modeling (2025) `[PR]` DOI: 10.1007/s10270-025-01318-w
  - **확인된 추세 서술:** "By **2024–2025, generative AI approaches clearly surpass non-generative AI approaches**" — BPM 분야에서 생성형 접근이 비생성형을 명확히 앞질렀다. 실제 적용은 **발견(discovery)과 구현(implementation) 단계, 특히 추출(extraction) 활동**에 집중되어 있다. RAG로 사내 문서·용어집·규정·프로세스 모델링 규칙을 끌어오는 연구가 늘고 있다.
  - **이 책에 쓸 수 있는 부분:** "SOP를 에이전트에 넣는다"는 실무 작업이 **BPM 학계에서는 이미 하나의 연구 프로그램**이라는 것. 특히 **RAG로 사내 규정을 끌어오는 패턴**이 학계에서도 주류라는 점은 실무 아키텍처 결정을 지지한다.
  - ⚠️ **개별 논문의 저자·게재처를 확정하지 못한 항목이 있으므로, 본문에서 특정 논문을 지목해 인용하려면 재확인 필수.** 추세 서술만 쓰는 편이 안전하다.

---

### 축 2 커버리지

**확보한 것**
- **적힌 절차 vs 실제 수행의 간극**에 대한 정본 이론 (Feldman & Pentland 2003, ASQ) — 이 책의 핵심 논점에 대한 최상급 근거 확보
- **형식화가 살리기도 죽이기도 한다**는 이론 (Adler & Borys 1996, ASQ) — 탑다운 체계의 양면성에 대한 정본
- **암묵지 형식화의 이론과 그 비판** (Nonaka 1994, Org Sci / Gourlay 2006, JMS) — 병기 가능한 논쟁 확보
- **프로세스 마이닝의 정본 교과서** (van der Aalst) + conformance checking = ostensive/performative 대조의 공학적 구현
- **LLM 에이전트가 SOP를 쓰는 방식**에 대한 최상급 사례 (MetaGPT, ICLR 2024 Oral)
- **SOP 수행 능력의 정량 평가** (SOP-Bench: 12도메인, 2,000+ 과제, 57~100% 편차, "최신 모델이 더 낫다는 보장 없음") — 실무 리더가 바로 쓸 수 있는 수치
- BPM × LLM 연구 지형의 최신 추세 (2024~2026)

**비어 있는 것 (후속 리서치 권장)**
- ⚠️ **Adler & Borys의 enabling 형식화 4대 설계 특성**을 원문 확인하지 못했다 — **이 책에 가장 실용적으로 쓸 수 있는 부분인데 미확보.** 공개 PDF가 있으므로 저술 전 반드시 확인할 것.
- **한국 조직의 SOP 형식화 실태**에 대한 학술 실증 없음.
- **SOP의 형식화 정도와 에이전트 성능 사이의 관계**를 직접 측정한 연구를 찾지 못했다 ("SOP를 얼마나 자세히 써야 하는가"의 답이 없음). 이 책이 현장 관찰로 채워야 할 공백.
- 프로세스 마이닝을 **에이전트 실행 로그**에 적용한 연구 (에이전트가 만든 이벤트 로그로 conformance를 검사하는 루프)를 특정하지 못했다 — 유망한 공백이자 이 책의 독자적 기여 지점이 될 수 있다.

---

## 축 3 — AI 도입의 조직 경제학·실증

> **이 축의 인용 규율:** 아래 효과 크기는 **각각 다른 직무·다른 과제·다른 모델 세대**에서 측정된 것이다. 하나로 뭉뚱그려 "AI는 N% 생산성을 올린다"고 쓰면 안 된다. 각 수치에는 **직무·표본·연도·모델 세대**를 반드시 붙일 것.

### 핵심 논문

---

- **Brynjolfsson, E., Li, D., & Raymond, L. (2025). 「Generative AI at Work」.** `[PR]` The Quarterly Journal of Economics, 140(2), 889–942. 원래 NBER Working Paper **31161** (2023-04)으로 유통. DOI: 10.3386/w31161 (WP). 검색: 2026-09-05 기준.
  - **핵심 주장:** 생성형 AI 기반 대화 어시스턴트가 고객지원 조직에 **단계적으로(staggered) 도입된** 자연 실험을 활용한 준실험 연구. **가장 중요한 결과는 평균이 아니라 이질성(heterogeneity)** 이다.
  - **핵심 수치 (원문 그대로):**
    - 표본: **고객지원 상담원 5,172명**.
    - 평균 효과: **시간당 처리 건수(issues resolved per hour) 기준 생산성 15% 증가**, "with **substantial heterogeneity** across workers."
    - **경험이 적고 숙련도가 낮은 노동자**는 산출의 **속도와 품질 양쪽에서 개선**되었다.
    - **가장 경험 많고 숙련도 높은 노동자**는 **속도에서 작은 이득, 품질에서 작은 하락**을 보였다.
    - 부수 효과: **고객 감정(customer sentiment) 개선, 직원 유지율(retention) 상승**, 그리고 노동자 학습(worker learning)의 가능성.
  - **이 책에 쓸 수 있는 부분: AX 체계 설계의 배분 원칙에 대한 근거.** 에이전트를 조직에 등록할 때 "누구에게 먼저 붙이는가"의 답이 여기 있다 — **신입·저숙련 직무에서 효과가 크고, 고숙련 직무에서는 품질이 오히려 떨어질 수 있다.** 등록·권한 설계를 직무 숙련도별로 차등화해야 하는 실증 근거. 또 **직원 유지율 상승**은 변화관리(축4)에서 "AI가 사람을 밀어낸다"는 프레임에 대한 반증 카드로 쓸 수 있다.
  - **인용 가능한 문장/수치:** 위 수치 그대로. 특히 "**less experienced and lower-skilled workers improve both the speed and quality of their output, while the most experienced and highest-skilled workers see small gains in speed and small declines in quality**" — 이 대비가 이 책의 핵심 장면 중 하나가 될 수 있다.
  - **한계·반박:** **관찰 기반 준실험**이며 무작위 배정 RCT가 아니다. 단일 기업(고객지원 소프트웨어 제공사의 고객사) 데이터이며, 고객지원이라는 **고도로 반복적이고 측정 가능한 직무**다 — 기획·설계 같은 비정형 직무로 외삽할 수 없다. 또 도입 시점 모델은 GPT-3.5 세대다 (**모델 세대 명시 필수**).

---

- **Dell'Acqua, F., McFowland III, E., Mollick, E. R., Lifshitz-Assaf, H., Kellogg, K., Rajendran, S., Krayer, L., Candelon, F., & Lakhani, K. R. (2023/2025). 「Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality」.** `[PR]` **Organization Science (2025), DOI: 10.1287/orsc.2025.21838.** 원래 Harvard Business School Working Paper 24-013 (**2023-09**), SSRN 4573321. 검색: 2026-09-05 기준.
  - **핵심 주장:** BCG와 공동으로 수행한 **사전 등록(preregistered) 무작위 실험**. 조건은 셋 — AI 없이 / GPT-4와 함께 / GPT-4 + 프롬프트 엔지니어링 개요와 함께. **핵심 발견은 "들쭉날쭉한 경계(jagged frontier)"** — AI 역량의 경계는 매끄럽지 않고 들쭉날쭉해서, 겉보기에 비슷한 난이도의 과제인데도 어떤 것은 AI가 잘하고 어떤 것은 못한다. 그리고 **어느 쪽인지는 사전에 알기 어렵다.**
  - **핵심 수치 (원문 그대로):**
    - 표본: **고숙련 경영 컨설턴트 758명**, **18개의 현실적 지식노동 과제** (창의적 과제부터 분석적 과제까지).
    - **AI 역량 경계 안(within the frontier)** 의 과제에서: 과제 완수 **12.2% 증가**, 완수 속도 **25.1% 향상**, 그리고 맹검 평가자(blind evaluators)가 매긴 **품질 40% 상승**.
    - **경계 밖(outside the frontier)** 으로 선정된 복잡한 경영 과제에서: AI를 쓴 참가자가 정답을 낼 확률이 **19% 낮았다.**
  - ⚠️ **수치 표기 주의:** 마지막 항목은 출처에 따라 "19% less likely"와 "19 percentage points less likely"로 갈린다. **본문에 쓰기 전 원문(Organization Science 게재본 또는 HBS WP 24-013)에서 정확한 표현을 확인할 것.** 확인 전에는 "약 19% 낮았다"로 완충해 쓸 것.
  - **이 책에 쓸 수 있는 부분: 이 책이 왜 "실험을 체계로 전향해야 한다"고 말하는지의 가장 강력한 근거.** jagged frontier는 **개인이 시행착오로 알아낼 수 없는 지형**이다. 어떤 과제가 경계 안이고 밖인지는 **조직이 축적해야 알 수 있는 지식**이며, 그것을 축적하는 장치가 바로 등록부·평가·로그다. 바텀업 실험이 개인 안에서 끝나면 이 지식은 조직에 남지 않는다.
  - **인용 가능한 문장/수치:** 위 수치 그대로. "jagged technological frontier"는 용어 자체가 강력하다 — **한국어로 "들쭉날쭉한 경계"** 로 번안하면 그림이 바로 그려진다.
  - **한계·반박:** **컨설턴트라는 단일 직군**, **GPT-4 시점(2023년)** 이다. 모델 세대가 바뀌면 경계의 모양이 바뀐다 — 실제로 Mollick 본인도 이후 "경계가 매끈해지고 있다"는 취지의 후속 논평을 냈다. ⚠️ 인용 시 "2023년 GPT-4 기준"을 반드시 붙일 것. 또 실험실적 과제이지 실제 고객 프로젝트가 아니다.

---

- **Noy, S., & Zhang, W. (2023). 「Experimental evidence on the productivity effects of generative artificial intelligence」.** `[PR]` **Science**, 2023-07-13 온라인 게재. DOI: 10.1126/science.adh2586. SSRN 4375283. 검색: 2026-09-05 기준.
  - **핵심 주장:** 직군별로 맞춘 **인센티브가 걸린 글쓰기 과제**를 부여하고 절반에게 무작위로 ChatGPT를 노출시킨 실험.
  - **핵심 수치 (원문 그대로):**
    - 표본: **대졸 전문직 453명**.
    - **평균 소요 시간 40% 감소**, **산출 품질 18% 상승**.
    - **노동자 간 불평등(inequality between workers)이 감소**했다 — 즉 원래 못하던 사람이 더 많이 올라왔다.
    - AI에 대한 **우려와 흥분이 일시적으로 함께 상승**했다.
  - **이 책에 쓸 수 있는 부분:** Brynjolfsson et al.의 이질성 발견과 **같은 방향**의 독립 증거 — **격차 축소 효과.** 두 연구가 서로 다른 직무·다른 설계에서 같은 결론에 도달했다는 점을 강조할 수 있다. 변화관리(축4) 관점에서는 **"AI가 잘하는 사람에게 유리하다"는 통념이 실증과 어긋난다**는 반전 소재.
  - **인용 가능한 문장/수치:** 위 수치 그대로. "**inequality between workers decreased**"는 조직 내 형평성 논의에 바로 쓸 수 있다.
  - **한계·반박:** **글쓰기 과제 한정**, 과제 소요 시간이 짧고(대략 20~30분급) **실제 업무 맥락이 아니다.** ChatGPT 초기(2023년 초, GPT-3.5 세대) 실험이다. 짧은 단발 과제의 효과가 장기 업무 성과로 이어지는지는 이 연구가 답하지 않는다.

---

- **Cui, Z. (K.), Demirer, M., Jaffe, S., Musolff, L., Peng, S., & Salz, T. (2025). 「The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers」.** `[PR]` **Management Science (2025), DOI: 10.1287/mnsc.2025.00535.** SSRN 4945566. 검색: 2026-09-05 기준.
  - **핵심 주장:** **Microsoft, Accenture, 그리고 익명의 Fortune 100 기업**에서 수행한 **3개의 무작위 대조 현장 실험**. 개발자 중 무작위 부분집합에게 AI 코딩 어시스턴트(지능형 코드 완성) 접근권을 부여했다.
  - **핵심 수치 (원문 그대로):**
    - 표본: **3개 실험 통합 개발자 4,867명**.
    - **완료 과제 수 26.08% 증가 (표준오차 SE: 10.3%).**
    - **경험이 적은 개발자일수록 채택률이 높고 생산성 향상도 컸다.**
  - **이 책에 쓸 수 있는 부분: 실험실이 아니라 실제 기업 세 곳의 현장 RCT라는 점에서 이 축에서 가장 신뢰도 높은 증거 중 하나.** 그리고 다시 한번 **"경험이 적을수록 효과가 크다"** 는 이질성이 재현되었다 — 세 번째 독립 증거. 이 책의 배분 원칙(신입·저숙련 직무 우선)이 세 개의 서로 다른 연구에서 지지된다고 쓸 수 있다.
  - **인용 가능한 문장/수치:** "**a 26.08% increase (SE: 10.3%) in completed tasks**" — 표준오차를 함께 인용할 것. SE가 10.3%라는 것은 **효과 크기의 불확실성이 상당하다**는 뜻이므로, 정직하게 쓰려면 "약 26%, 다만 추정의 표준오차가 10%p 수준"으로 표기해야 한다.
  - **한계·반박:** 코드 완성 도구(에이전트가 아니라 자동완성) 세대의 실험이다. 또 "완료 과제 수"는 과제 난이도를 통제하지 않으면 오도될 수 있는 지표다. 아래 METR 결과와 **정면으로 충돌**하므로 반드시 병기할 것.

---

- **METR (2025). 「Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity」.** `[PP]` arXiv:2507.09089 (**2025-07-10**). METR 발행. 프리프린트 — 피어리뷰 미확인. ⚠️ 전체 저자 명단 미확인. 검색: 2026-09-05 기준.
  - **핵심 주장: 이 축에서 가장 중요한 반증.** 2025년 2~6월 프런티어 AI 도구가 **경험 많은 오픈소스 개발자**의 생산성에 미치는 영향을 무작위 대조로 측정했더니, **AI가 개발자를 느리게 만들었다.**
  - **핵심 수치 (원문 그대로):**
    - 표본: **AI 사용 경험이 중간 수준인 개발자 16명**, **246개 과제**, 대상 프로젝트에 대한 **평균 5년의 사전 경험**을 가진 성숙한 프로젝트.
    - 각 과제는 2025년 초 AI 도구 사용 허용/불허로 **무작위 배정**. 허용 시 주로 **Cursor Pro와 Claude 3.5/3.7 Sonnet** 사용.
    - **과제 시작 전 개발자들의 예측: AI가 완료 시간을 24% 줄일 것.**
    - **실제 결과: 완료 시간이 19% 증가했다** — AI 도구가 개발자를 느리게 만들었다.
    - **연구 종료 후 개발자들의 사후 추정: AI가 완료 시간을 20% 줄였다.** → **실제로는 19% 느려졌는데, 본인들은 20% 빨라졌다고 믿었다.**
  - **이 책에 쓸 수 있는 부분: 이 책 전체에서 가장 강력한 한 장면이 될 수 있다.** 인식과 실측의 39%p 괴리는 **"체감으로 AX 성과를 관리하면 안 된다"** 는 주장의 결정적 근거다. 바텀업 실험이 자기 보고에 의존하는 한 조직은 자기가 어디 있는지 모른다. **측정 체계를 세우는 것이 등록·로깅의 목적 중 하나**라는 논지로 이어진다. 또 Brynjolfsson·Cui의 "경험 적을수록 효과 크다"와 맞물려 **"고숙련·성숙 코드베이스에서는 오히려 손해일 수 있다"** 는 대칭을 완성한다.
  - **인용 가능한 문장/수치:** 24% → +19% → 20%의 세 숫자를 나란히 놓는 것 자체가 문장이다. "developers **forecast** that allowing AI would reduce completion time by **24%**. Surprisingly, allowing AI actually **increased** completion time by **19%**." 그리고 사후 추정 **20% 감소**.
  - **한계·반박 (반드시 병기):** **표본이 16명, 246과제로 작다.** 대상이 **자기 코드베이스에 평균 5년 숙련된 오픈소스 개발자**라는 매우 특수한 집단이다 — 이 조건은 AI의 상대 우위가 가장 작은 조건이다. 프리프린트이며 2025년 2~6월 모델 기준. **"AI는 생산성을 떨어뜨린다"로 일반화하면 심각한 오독이다.** 이 책은 반드시 "누구에게, 어떤 조건에서"를 붙여 인용해야 한다.

---

- **Peng, S., Kalliamvakou, E., Cihon, P., & Demirer, M. (2023). 「The Impact of AI on Developer Productivity: Evidence from GitHub Copilot」.** `[PP]` arXiv:2302.06590 (**2023-02-13**). 프리프린트 — 피어리뷰 게재 미확인. 검색: 2026-09-05 기준.
  - **핵심 주장:** GitHub Copilot을 이용한 통제 실험. 모집된 소프트웨어 개발자에게 **JavaScript로 HTTP 서버를 최대한 빨리 구현**하게 했다.
  - **핵심 수치:** **AI 페어 프로그래머 접근권을 가진 처치군이 대조군보다 과제를 55.8% 빨리 완료했다.** 이질적 효과가 관찰되어, AI 페어 프로그래머가 사람들의 소프트웨어 개발 커리어 진입을 도울 가능성을 시사한다.
  - ⚠️ **표본 크기 미확인** — 이번 검색으로 참가자 수를 확정하지 못했다. **본문에 쓰려면 arXiv 원문에서 N을 확인할 것.**
  - **이 책에 쓸 수 있는 부분:** 가장 자주 인용되는 "55.8%" 수치의 **정확한 출처와 조건**을 밝히는 데 쓴다. 이 책이 할 수 있는 좋은 서비스 중 하나가 **"그 55.8%는 HTTP 서버 하나 짜는 단일 과제였다"** 를 알려주는 것이다.
  - **한계·반박 (강조):** **단일 과제, 잘 정의된 그린필드 과제, 프리프린트, GitHub(Copilot 제공사) 소속 저자 포함.** 실제 업무의 유지보수·디버깅·레거시 작업과 성격이 완전히 다르다. **METR 결과와 정확히 반대 조건**이라는 점을 짚으면 두 연구가 왜 갈리는지가 설명된다 — 그린필드 단일 과제 vs 성숙 코드베이스.

---

- **Brynjolfsson, E., Rock, D., & Syverson, C. (2017). 「Artificial Intelligence and the Modern Productivity Paradox: A Clash of Expectations and Statistics」.** `[WP]` NBER Working Paper **24001** (**2017-11**). 검색: 2026-09-05 기준.
  - **핵심 주장:** **역설의 정식화** — AI 시스템은 점점 더 많은 영역에서 인간 수준 성능을 따라잡거나 넘어서는데, **측정된 생산성 증가율은 지난 10년간 절반으로 떨어졌다.** 저자들은 이 괴리를 설명하는 네 가지 후보를 검토한다: 잘못된 기대, 잘못된 측정, 이익의 재분배와 소모, 그리고 **구현 지연(implementation lags)**. 그리고 마지막 설명 — **보완적 혁신과 조직 재설계에 시간이 걸린다** — 이 가장 설득력 있다고 결론짓는다.
  - **관련 후속 (J-curve의 정식 논문):** Brynjolfsson, E., Rock, D., & Syverson, C. (2021). 「The Productivity J-Curve: How Intangibles Complement General Purpose Technologies」. `[PR]` **American Economic Journal: Macroeconomics**, 2021-01. ⚠️ 권·호·페이지 미확인. **J-curve 비유 자체는 Larry Summers가 제안한 것**이라고 저자들이 밝히고 있다.
  - **이 책에 쓸 수 있는 부분: 이 책의 존재 이유를 한 장의 그림으로 만들어주는 이론.** J-curve는 이렇게 읽힌다 — **범용 기술을 도입하면 초기에는 측정 생산성이 오히려 떨어진다.** 왜냐하면 조직은 눈에 안 보이는 무형자산(프로세스 재설계, 사람 재교육, 새 역할 정의)에 자원을 쏟고 있는데, 이 투자는 비용으로 계상되고 산출로는 잡히지 않기 때문이다. **바텀업 실험 단계에서 성과가 안 보이는 것이 정상**이며, 곡선의 아래쪽 골짜기를 건너려면 **체계 구축이라는 무형 투자를 의도적으로 해야 한다.**
  - **인용 가능한 문장/수치:** 역설의 정식 — AI가 "match or surpass human-level performance in increasingly more domains, yet **measured productivity growth has declined by half over the past decade**."
  - **한계·반박:** 2017년 워킹페이퍼이며 거시 통계 기반 논증이다. J-curve의 골짜기가 얼마나 깊고 얼마나 긴지는 **사전에 알 수 없다** — 이 이론은 "기다려라"의 알리바이로 오용될 수 있다. 이 책은 그 오용을 경계하면서 써야 한다. ⚠️ 2017년 시점 진단이므로 인용 시 연도 명시 필수.

---

- **Brynjolfsson, E., Hitt, L. M., & Yang, S. (2002). 「Intangible Assets: Computers and Organizational Capital」.** `[PR]` Brookings Papers on Economic Activity, 2002(1). DOI: 10.1353/eca.2002.0003. 검색: 2026-09-05 기준.
  - **핵심 주장:** IT의 광범위한 사용이 **무형 조직 자산(intangible organizational assets)에 대한 투자를 증가시켰다**는 명제를 기업 수준 데이터로 검증한다. **왜 기술만 사서는 성과가 안 나는가**에 대한 정본 근거.
  - **핵심 수치 (원문 그대로):** 다른 자산을 통제한 뒤, 기업에 설치된 **컴퓨터 자본 1달러가 최소 5달러의 시장 가치와 연관**되어 있었다. 저자들은 이 차액을 **컴퓨터 투자와 보완적인 무형자산의 큰 스톡이 존재한다는 증거**로 해석한다.
  - **이 책에 쓸 수 있는 부분: "AI 도구 라이선스를 사는 비용"과 "AI 체계를 세우는 비용"의 비율을 논할 때 인용할 정본 수치.** 1:5라는 비율은 예산 협상 자리에서 바로 쓸 수 있다 — **기술 구매 1에 조직 보완재 5.** 이 책의 등록 체계·SOP 정비·변화관리가 바로 그 "5"에 해당한다.
  - **인용 가능한 문장/수치:** "**each dollar of installed computer capital in a firm is associated with at least five dollars of market value**, after controlling for other assets."
  - **계보 메모:** Bresnahan, Brynjolfsson & Hitt은 특정 **조직 관행**이 IT 투자와 결합될 때 1980년대 후반~1990년대 초 생산성이 유의하게 상승했음을 보였다. ⚠️ 해당 논문(통상 QJE 2002, 「Information Technology, Workplace Organization, and the Demand for Skilled Labor」)의 정확한 서지는 재확인 필요.
  - **한계·반박:** **1990년대 컴퓨터 도입 데이터**다. AI에 그대로 적용된다는 보장은 없으며, 1:5 비율을 AI에 직접 대입하면 과대 해석이다. **"기술만으로는 부족하다"는 원리**를 인용하되 **비율 숫자는 IT 사례임을 밝히고** 쓸 것.

---

- **McElheran, K., Li, J. F., Brynjolfsson, E., Kroff, Z., Dinlersoz, E., Foster, L., & Zolas, N. J. (2024). 「AI Adoption in America: Who, What, and Where」.** `[PR]` Journal of Economics & Management Strategy, 33(2), 375–415. DOI: 10.1111/jems.12576. NBER WP 31788. SSRN 4673528. 검색: 2026-09-05 기준.
  - **핵심 주장:** 미국 인구조사국 **2018년 Annual Business Survey**의 **약 850,000개 기업** 데이터로 AI 관련 기술 5종(자율주행 운반차, 머신러닝, 머신비전, 자연어처리, 음성인식)의 채택 실태를 측정했다.
  - **핵심 수치 (원문 그대로):**
    - **측정된 AI 관련 기술 중 어느 하나라도 사용하는 기업은 6% 미만.**
    - 다만 **매우 큰 기업 대부분은 어떤 형태로든 AI를 사용**한다고 보고했다.
    - **고용 가중 평균 채택률은 18%를 조금 넘는다.**
    - 생산 현장의 AI 사용은 산업별 편차가 크지만 **경제의 모든 부문에 존재**했고, **클라우드 컴퓨팅·로보틱스 같은 신흥 기술과 함께 군집**했다.
  - **이 책에 쓸 수 있는 부분: "채택은 기업 수로 세면 낮고, 사람 수로 세면 높다"는 비대칭.** AX 리더가 자기 조직의 성숙도를 판단할 때 어떤 분모를 쓰느냐에 따라 그림이 완전히 달라진다는 방법론적 교훈. 그리고 **AI가 클라우드·로보틱스와 군집한다**는 발견은 **"AI 체계는 기존 인프라 위에 얹힌다"** 는 이 책의 아키텍처 주장을 지지한다.
  - **한계·반박:** **2018년 데이터**다 — 생성형 AI 이전 세대이며, 오늘의 채택률과는 완전히 다르다. ⚠️ **반드시 "2018년 기준, 생성형 AI 이전"을 명시하고, 현재 수치로 오도되지 않게 할 것.** 이 논문의 가치는 절대 수치가 아니라 **분모 선택의 방법론적 교훈과 군집 발견**에 있다.

---

- **Bick, A., Blandin, A., & Deming, D. J. (2024). 「The Rapid Adoption of Generative AI」.** `[WP]` NBER Working Paper **32966** (2024-09). St. Louis Fed Working Paper 2024-027. SSRN 4964384. 검색: 2026-09-05 기준.
  - **핵심 주장:** 2024년 8월과 11월에 실시한 설문(합계 **10,000명 이상 응답**)으로 생성형 AI 채택 속도를 측정했다.
  - **핵심 수치 (2024년 말 기준, 원문 그대로):**
    - **미국 18~64세 인구의 거의 40%가 생성형 AI를 사용.**
    - **취업자 응답자의 23%가 직전 1주일 내 업무 목적으로 최소 1회 사용**, **9%는 매 근무일 사용.**
    - **전체 근로 시간의 1~5%가 현재 생성형 AI의 보조를 받고 있다.**
    - 응답자들이 보고한 **절감 시간은 총 근로 시간의 1.4%에 해당.**
    - 각 기술의 첫 대중 시장 제품 출시 시점 대비, 생성형 AI의 **업무 채택은 PC만큼 빨랐고**, **전체 채택은 PC나 인터넷보다 빨랐다.**
  - **이 책에 쓸 수 있는 부분: 바텀업 실험의 규모를 보여주는 정본 수치.** 조직이 체계를 세우기 전에 이미 **취업자 4명 중 1명이 주간 단위로 쓰고 있었다**는 사실. 그리고 결정적으로, **자기 보고 절감 시간이 총 근로 시간의 1.4%에 불과**하다는 점 — 개인 사용이 아무리 퍼져도 **조직 성과로 응축되지 않는다**는 것을 보여준다. 이것이 "실험을 체계로 전향해야 하는" 이유다.
  - **인용 가능한 문장/수치:** 위 수치 그대로. **"채택은 인터넷보다 빨랐지만 절감 시간은 총 근로 시간의 1.4%"** 라는 대비가 이 책의 논지를 한 문장에 담는다.
  - **한계·반박:** **자기 보고 설문**이다. METR 결과(자기 보고와 실측의 39%p 괴리)를 고려하면 **1.4%라는 숫자조차 신뢰 구간이 넓다.** ⚠️ **2024년 말 기준 수치이며 이 논문은 이후 갱신되었을 가능성이 높다 — 2026년 저술 시점에서는 최신판 확인 필수.**

---

- **Klein, K. J., & Sorra, J. S. (1996). 「The Challenge of Innovation Implementation」.** `[PR]` Academy of Management Review, 21(4), 1055–1080. DOI: 10.5465/amr.1996.9704071863. 검색: 2026-09-05 기준.
  - **핵심 주장: "파일럿은 성공했는데 확산이 안 된다"의 정본 이론.** 도입(adoption)과 **구현(implementation)** 을 분리한다. 구현이란 "대상 조직 구성원들이 혁신을 **적절하고 헌신적으로 사용하게 되는 과정**"이다. 구현 효과성 — 대상 구성원의 사용의 **일관성과 품질** — 은 두 가지의 함수다: **(a) 그 혁신의 구현에 대한 조직의 풍토(implementation climate)의 강도**, **(b) 그 혁신이 대상 사용자의 가치에 부합하는 정도(innovation-values fit)**.
  - **핵심 정의 (인용 가능):**
    - **implementation climate** = "targeted employees' **shared summary perceptions** of the extent to which their use of a specific innovation is **rewarded, supported, and expected** within an organization" — 즉 **보상받고, 지원받고, 기대되는가**에 대한 구성원들의 공유된 인식.
    - **innovation-values fit** = "the extent to which targeted users perceive that use of the innovation will **foster (or, conversely, inhibit) their values**."
    - **구현 결과의 스펙트럼:** **저항(resistance) — 회피(avoidance) — 순응(compliance) — 헌신(commitment).**
  - **이 책에 쓸 수 있는 부분: 이 책의 변화관리 파트를 Kotter 대신 이걸로 세울 수 있다** (Kotter의 실증 문제는 축4 참조). 세 가지 실무 함의가 바로 나온다:
    1. **"쓰라고 시켰는데 안 쓴다"의 원인은 두 개뿐**이다 — 풍토가 약하거나(보상·지원·기대가 없거나), 가치가 안 맞거나.
    2. **순응(compliance)과 헌신(commitment)은 다르다.** AX 지표가 "사용률"만 본다면 순응까지만 측정하는 것이다.
    3. **"AI가 내 가치를 촉진하는가 저해하는가"** 라는 개인 판단이 구현 성패를 가른다 → 축4의 직업 정체성 위협과 직결.
  - **한계·반박:** **이론 논문(AMR)** 이며 이 논문 자체에 실증이 없다. 다만 후속 실증 검증이 다수 이루어졌다 (예: 「Testing Klein and Sorra's innovation implementation model: An empirical examination」, Journal of Engineering and Technology Management, 2008; 「The missing link: a test of Klein and Sorra's proposed relationship between implementation climate, innovation-values fit and implementation effectiveness」, Implementation Science 계열). ⚠️ 후속 검증 논문의 정확한 서지는 재확인 필요.

---

- **Shadow AI (비공식 사용) — 학술 근거와 벤더 통계의 구분**
  - **학술:** Silic, M. 외. 「From Shadow IT to Shadow AI – Threats, Risks and Opportunities for Organizations」. `[PR]` **Strategic Change** (Wiley), DOI: **10.1002/jsc.2682**. ⚠️ **발행 연도·권·호 미확인 (본문 접근 403 차단).** 검색 결과에 따르면 **전문직 140명 설문 + 임원 10명 심층 인터뷰**의 혼합 방법 연구로, Shadow AI(조직 내 비인가 AI 도구 사용)의 리스크·동인·거버넌스 과제를 다룬다. **본문 인용 전 서지 확정 필수.**
  - **⚠️ 아래는 전부 벤더·업계 조사이며 피어리뷰 논문이 아니다. 이 책에서 쓸 경우 반드시 "업계 조사"로 명시하고 학술 근거와 섞지 말 것.**
    - 조직의 **98%가 비인가 AI 사용을 보고**, **49%가 12개월 내 shadow AI 사고를 예상** (출처 미확정)
    - **직원의 78%가 IT 승인 없이 AI 도구 사용**, **46%는 명시적으로 금지되어도 계속 쓰겠다**고 응답
    - UpGuard 2025년 11월 조사: 응답자의 **80% 이상**이 업무에서 비인가 AI 도구 사용
    - CybSafe/National Cybersecurity Alliance 2024년 말 조사 (n≈7,000): **직원의 약 38%가 승인 없이 기밀 데이터를 AI 플랫폼에 공유**
    - IBM 2025: **조직의 37%만이 shadow AI를 관리하거나 탐지할 정책을 보유**
    - 기업 직원의 생성형 AI 앱 채택률 **2023년 74% → 2024년 96%**; 2024년 GenAI 트래픽 **890% 이상 급증**; Menlo Security 2025: shadow GenAI 사용 **68% 급증**
  - **이 책에 쓸 수 있는 부분: 이 책의 출발 전제 — "바텀업 실험은 이미 일어나고 있고, 등록되지 않았을 뿐이다."** 특히 **"금지해도 46%는 계속 쓴다"** 는 수치가 사실이라면, 금지 전략의 실패와 **등록 전략의 필요**를 동시에 말해준다. 다만 위 수치들은 벤더 조사이므로 **이 책의 논증을 여기 얹으면 안 된다** — 분위기 전달용으로만 쓰고, 논증의 하중은 학술 근거(Atkinson & O'Bryan 2026의 행동 기반 측정, Bick et al.의 채택률)에 싣는다.
  - **미 연방기관 AI use case inventory 실태 (정책 등록부의 실제 작동을 보여주는 사례):**
    - **2025년 연방기관 AI use case inventory: 56개 제출 기관에서 3,611건의 개별 use case** — 2024년 1,757건 대비 **105% 증가**.
    - 다수의 인벤토리가 **일관성 없는 문서화와 필수 리스크 관리 관행 준수에 대한 불충분한 세부 정보**를 담고 있었다. 리스크 관리 관행의 **면제(waiver)·연장(extension)에 대한 공개 보고는 전 기관에 걸쳐 압도적으로 희소**했으며, **국토안보부(DHS)만이 연장 기간에 대한 구체 정보를 포함**했다.
    - **고영향(high-impact) AI use case**는 이론상 배포 전 테스트·영향 평가·모니터링·이의제기 절차 정보를 제공해야 하지만, **실무에서는 정보가 불완전**하다.
    - ⚠️ **출처가 학술 논문이 아니라 시민사회 분석(Center for Democracy and Technology의 2024 인벤토리 분석)과 언론 보도(Nextgov/FCW)다. 본문 인용 시 출처 성격을 명시할 것.** 원자료는 GitHub `ombegov/2025-Federal-Agency-AI-Use-Case-Inventory`에 공개되어 있다.
    - **이 책에 쓸 수 있는 부분: 등록부를 만들면 어떤 일이 실제로 벌어지는가의 살아 있는 사례.** 등록부는 만들어졌고 숫자는 두 배로 늘었지만, **정작 리스크 관리 항목은 비어 있었다.** 이 책의 등록 설계가 "필드를 만드는 것"에서 멈추면 똑같이 된다는 경고로 쓸 것. **등록부의 실패 모드는 "등록이 안 되는 것"이 아니라 "등록은 되는데 알맹이가 비는 것"이다.**

---

### 축 3 커버리지

**확보한 것**
- **생산성 효과의 정본 실증 6건**을 효과 크기·표본·연도·모델 세대와 함께 확보:
  - Brynjolfsson·Li·Raymond (QJE 2025, n=5,172, +15%, 이질성)
  - Dell'Acqua 외 (Organization Science 2025, n=758, +12.2%/+25.1%/+40%, 경계 밖 −19%)
  - Noy·Zhang (Science 2023, n=453, −40% 시간/+18% 품질, 격차 축소)
  - Cui 외 (Management Science 2025, n=4,867, +26.08% SE 10.3%)
  - Peng 외 (arXiv 2023, +55.8%, 단일 과제)
  - **METR (arXiv 2025, n=16/246과제, +19% 소요 시간 = 느려짐, 인식-실측 39%p 괴리)** ← 결정적 반증
- **세 개의 독립 연구가 같은 이질성**(경험 적을수록 효과 크다)에 도달 — 배분 원칙의 강한 근거
- **왜 기술만 사서는 안 되는가**의 정본 (Brynjolfsson·Hitt·Yang 2002, 컴퓨터 자본 1달러 : 시장가치 5달러)
- **J-curve / 생산성 역설** (Brynjolfsson·Rock·Syverson 2017 NBER 24001, 2021 AEJ:Macro)
- **파일럿-확산 실패의 조직 이론** (Klein & Sorra 1996 AMR: implementation climate × innovation-values fit, 저항→회피→순응→헌신 스펙트럼)
- **채택 규모** (McElheran 외 2024 JEMS: 기업 6%/고용가중 18%, 2018년 기준 / Bick 외 2024 NBER: 취업자 23% 주간 사용, 절감 시간 총 근로 시간의 1.4%)
- **등록부가 실제로 어떻게 실패하는가**의 사례 (미 연방 AI use case inventory: 3,611건으로 두 배 증가했으나 리스크 관리 필드는 공백)

**비어 있는 것 (후속 리서치 권장)**
- ⚠️ **METR 논문의 전체 저자 명단, Peng 외 2023의 표본 크기(N), Dell'Acqua "19%" vs "19%p" 표기** — 세 건 모두 원문 확인 필요.
- **2025~2026년의 최신 후속 연구와 재현 연구**를 충분히 확보하지 못했다. 특히 **에이전트(자동완성이 아닌) 세대의 현장 RCT**를 찾지 못했다 — 위 실증은 전부 chat/completion 세대다. **이 책이 다루는 "등록된 에이전트"의 생산성 효과에 대한 실증은 아직 존재하지 않을 가능성이 높으며, 그 사실 자체를 정직하게 밝히는 것이 이 책의 신뢰도를 높인다.**
- **"파일럿 95% 실패" 같은 널리 인용되는 업계 수치**의 학술적 검증을 찾지 못했다 — 해당 수치는 MIT/BCG 계열 업계 보고서이며 **web-researcher가 원 출처를 확인해야 한다.** ⚠️ 학술 근거로 쓰면 안 된다.
- **한국 기업의 AI 도입 생산성 실증**은 확보하지 못했다.
- **shadow AI의 피어리뷰 실증**은 Silic et al. 1건뿐이며 서지도 미확정. 이 영역은 학술 공백이 크다.

---

## 축 4 — 변화관리·수용·저항

### 핵심 논문

---

- **Dietvorst, B. J., Simmons, J. P., & Massey, C. (2015). 「Algorithm Aversion: People Erroneously Avoid Algorithms After Seeing Them Err」.** `[PR]` Journal of Experimental Psychology: General, 144(1), 114–126. 검색: 2026-09-05 기준.
  - **핵심 주장:** 증거 기반 알고리즘이 인간 예측가보다 더 정확하게 미래를 예측하는데도, 사람들은 둘 중 하나를 고르라 하면 **인간 예측가를 고른다.** 저자들은 이를 **알고리즘 혐오(algorithm aversion)** 라 부르고, 그것이 **비용을 발생시킨다**고 못 박는다.
  - **방법·수치 (원문 그대로):** **5개 연구(5 studies).** 참가자는 알고리즘의 예측을 보거나, 인간의 예측을 보거나, 둘 다 보거나, 아무것도 보지 않은 뒤, 자기 인센티브를 알고리즘의 예측에 걸 것인지 인간의 예측에 걸 것인지 결정했다.
  - **결정적 발견:** **알고리즘이 수행하는 것을 본 참가자는 알고리즘에 대한 확신이 낮아졌고, 열등한 인간 예측가보다 알고리즘을 고를 확률이 낮아졌다.** 심지어 **알고리즘이 인간을 능가하는 것을 본 뒤에도 그랬다.** 이유는 **사람들이 같은 실수를 보았을 때 인간보다 알고리즘에 대한 신뢰를 훨씬 빨리 잃기 때문이다.**
  - **이 책에 쓸 수 있는 부분: AX 롤아웃의 가장 잔인한 함정.** 파일럿에서 에이전트가 **한 번 틀리는 순간** 조직의 신뢰가 비대칭적으로 무너진다 — 사람이 같은 실수를 했을 때보다 훨씬 크게. 이것은 **에이전트 도입 시 "완벽한 데모"를 보여주려는 유혹의 근거이자, 동시에 그 전략이 위험한 이유**다. 실무 함의: **에이전트의 오류율을 사람의 오류율과 나란히 공개**하지 않으면, 에이전트만 불공정하게 심판받는다.
  - **인용 가능한 문장/수치:** "people **more quickly lose confidence in algorithmic than human forecasters after seeing them make the same mistake**." 그리고 "algorithm aversion ... **is costly**."
  - **한계·반박:** **실험실 예측 과제**이며 실제 조직 맥락이 아니다. 그리고 아래 Logg et al.의 정반대 발견과 병기해야 한다.

- **Logg, J. M., Minson, J. A., & Moore, D. A. (2019). 「Algorithm Appreciation: People Prefer Algorithmic to Human Judgment」.** `[PR]` Organizational Behavior and Human Decision Processes, 151, 90–103. DOI: 10.1016/j.obhdp.2018.12.005. SSRN 2941774. 검색: 2026-09-05 기준.
  - **핵심 주장: 정반대의 발견.** 일반인은 조언이 **사람에게서 온 것보다 알고리즘에서 왔다고 생각할 때 그 조언을 더 많이 따랐다.** 저자들은 이를 **알고리즘 선호(algorithm appreciation)** 라 부른다.
  - **방법·수치:** 시각 자극에 대한 수치 추정, 노래의 인기 예측, 로맨틱 매칭 예측 등 여러 과제에서 알고리즘 선호가 관찰되었다.
  - **이 책에 쓸 수 있는 부분: 이 두 논문을 반드시 나란히 놓아야 한다.** (아래 "상충하는 연구 결과" 참조.) 실무적으로는 **조건이 결과를 뒤집는다**는 것이 핵심 교훈 — 오류를 본 뒤인가 아닌가, 판단자가 자기 전문성을 걸고 있는가 아닌가, 조언인가 대체인가. **AX 리더는 "우리 조직은 AI를 싫어한다/좋아한다"를 고정된 성향으로 진단하면 안 된다. 그것은 설계 변수다.**
  - **인용 가능한 문장/수치:** "lay people **adhere more to advice when they think it comes from an algorithm than from a person**."
  - **한계·반박:** 대상이 **일반인(lay people)** 이다. Logg 본인의 후속 연구는 **전문가는 알고리즘 조언을 덜 따른다**는 방향을 시사한다 — 조직 내 전문가 집단에 그대로 적용할 수 없다. ⚠️ 이 후속 발견의 정확한 서지는 재확인 필요.

- **Dietvorst, B. J., Simmons, J. P., & Massey, C. (2018). 「Overcoming Algorithm Aversion: People Will Use Imperfect Algorithms If They Can (Even Slightly) Modify Them」.** `[PR]` Management Science, 64(3), 1155–1170. DOI: 10.1287/mnsc.2016.2643. SSRN 2616787. 검색: 2026-09-05 기준.
  - **핵심 주장: 처방이 나온다.** 세 개의 연구에서, 참가자는 인센티브가 걸린 예측 과제에서 자기 예측과 전문가가 만든 알고리즘 중 하나를 선택했다. **알고리즘의 예측을 수정할 수 있을 때 참가자들은 불완전한 알고리즘을 선택할 확률이 상당히 높아졌고, 그 결과 성과도 더 좋았다.** 결정적으로, **수정 가능 범위가 심하게 제한되어 있어도 이 선호는 유지되었다.**
  - **이 책에 쓸 수 있는 부분: 이 책의 변화관리 파트에서 가장 실행 가능한 설계 원칙.** 에이전트 도입 시 **사용자에게 아주 작은 수정 권한이라도 주라.** 수정 폭이 실질적으로 무의미할 정도로 작아도 수용률이 올라가고 **실제 성과도 개선된다.** 이것은 "human-in-the-loop"를 형식적 승인 버튼이 아니라 **수정 권한**으로 설계해야 하는 이유다. 그리고 등록 체계와 연결하면: **에이전트의 권한 스펙에 "사용자 수정 가능 구간"을 명시 필드로 넣어라.**
  - **인용 가능한 문장/수치:** "participants were **considerably more likely to choose to use an imperfect algorithm when they could modify its forecasts**, and they **performed better as a result** — 이 선호는 "**even when participants were severely restricted in the modifications they could make**"에도 유지되었다.
  - **한계·반박:** 실험실 예측 과제. "약간의 수정 권한"이 실제 조직에서 **책임 소재를 흐리는 부작용**을 낳을 수 있다 (사용자가 수정했으니 사용자 책임? 이는 축1의 책임 귀속과 충돌한다). **이 긴장 자체가 이 책이 다뤄야 할 좋은 논점이다.**

---

- **Venkatesh, V., Thong, J. Y. L., & Xu, X. (2012). 「Consumer Acceptance and Use of Information Technology: Extending the Unified Theory of Acceptance and Use of Technology」(UTAUT2).** `[PR]` MIS Quarterly, 36(1), 157–178. SSRN 2002388. 검색: 2026-09-05 기준.
  - **핵심 주장:** UTAUT를 소비자 맥락으로 확장해 **쾌락적 동기(hedonic motivation), 가격 가치(price value), 습관(habit)** 세 구성 개념을 추가한다. 개인 차이(연령·성별·경험)가 이들이 행동 의도와 실제 사용에 미치는 효과를 조절한다고 가정한다.
  - **핵심 수치 (원문 그대로):** **모바일 인터넷 이용자 1,512명**을 대상으로 한 2단계 온라인 설문(1차 설문 4개월 뒤 실제 사용 데이터 수집)이 모델을 지지했으며, UTAUT2는 **행동 의도의 설명 분산을 56%에서 74%로** 크게 개선했다.
  - **이 책에 쓸 수 있는 부분: 수용 모델을 쓰되 무엇이 빠졌는지 알고 쓰기 위한 기준점.** 특히 **습관(habit)** 구성 개념이 중요하다 — 이 책이 다루는 문제(개인이 이미 shadow로 쓰고 있는 습관을 조직 체계로 옮기기)는 정확히 습관과 조직 규범의 충돌이다. 다만 **UTAUT2는 소비자 맥락 모델**이라는 점을 짚어야 한다 — 조직 의무 사용 맥락에는 원판 UTAUT(2003)가 더 맞다.
  - **한계·반박 (중요):** UTAUT 계열은 **설명 분산이 높다는 것이 곧 처방을 준다는 뜻이 아니다.** "성과 기대가 수용을 예측한다"는 발견은 실무자에게 무엇을 하라고 말해주지 않는다. 또 **자기 보고 행동 의도**에 크게 의존한다 — METR의 인식-실측 괴리를 생각하면 심각한 한계다. **이 책에서는 UTAUT를 "설계 도구"가 아니라 "진단 어휘"로만 쓰는 것을 권한다.**
  - **AI 확장 사례:** 「Revisiting UTAUT for the Age of AI: Understanding Employees' AI Adoption and Usage Patterns Through an Extended UTAUT Framework」 arXiv:2510.15142 (2025-10) `[PP]` ⚠️ 미검증 — 필요 시 확인.

---

- **Shonhe, L., & Min, Q. (2025). 「Mitigating AI-induced professional identity threat and fostering adoption in the workplace」.** `[PR]` AI & Society, 40(5), 4079–4092. DOI: 10.1007/s00146-024-02170-0. 온라인 게재 **2025-01-15**. 검색: 2026-09-05 기준.
  - **핵심 주장:** AI가 유발하는 **직업 정체성 위협(professional identity threat, PIT)** 과 업무 현장의 AI 사용 의도 사이의 관계를 검증한다. 조절·매개 변수로 **AI 정체성(AI identity)**, 기록·정보 관리(RIM) 문화, **협력자로서의 설명 가능한 AI(XAI as a collaborator)**, 직업 경력, 시간적 거리를 넣었다.
  - **핵심 수치:** **동·남부 아프리카의 기록·정보 관리(RIM) 전문가 413명** 온라인 설문.
  - **핵심 발견:** **RIM 문화는 PIT나 AI 사용 의도에 유의한 영향을 주지 못했다.** 반면 **XAI(설명 가능한 AI)와 강한 AI 정체성이 PIT를 줄이고 AI 채택을 높이는 데 결정적이었다.**
  - **이 책에 쓸 수 있는 부분: "AI가 내 일을 대체한다"는 인식을 다루는 설계 근거.** 두 지렛대가 확인되었다 — **(1) 설명 가능성**(에이전트가 왜 그렇게 했는지 보여주기), **(2) AI 정체성 형성**(자기 개념 안에 AI 사용을 통합하도록 돕기). 그리고 **문화(조직 차원의 일반적 정보관리 문화)는 효과가 없었다**는 음성 결과가 실무적으로 중요하다 — **"문화를 바꾸자"는 슬로건이 아니라 개인 수준의 정체성 작업이 먹힌다.**
  - **한계·반박:** **단일 직군(RIM 전문가), 단일 지역(동·남부 아프리카), 자기 보고 설문, 횡단 연구(cross-sectional)** 다 — 인과 추론이 약하다. 한국 조직에 외삽하려면 조심해야 한다. ⚠️ **이 책에서 인용할 때 반드시 표본 특성을 밝힐 것.**
  - **관련 문헌 (병기 후보, 서지 재확인 필요):**
    - 「A Moderated Mediation Model of AI-Driven Identity Threats and Employee Cyberloafing: The Role of AI-Inclusive Identity」 (MDPI). ⚠️ 서지 미확인. 확인된 발견: **기술 상실감과 자율성 상실감이 직업 정체성 위협과 정적 상관**이며, 이것이 **사이버로핑(업무 회피)을 매개**한다.
    - 확인된 패턴 (출처 종합, ⚠️ 개별 논문 미특정): **경험이 적은 전문가는 증강형(augmentative) AI에서 이득을 보는 반면, 시니어는 대체(substitution)를 기존 자율성과 전문성에 대한 위협으로 인식하는 경우가 더 많다.** → 축3의 이질성 발견(경험 적을수록 생산성 효과 크다)과 **정확히 겹친다.** 즉 **효과가 큰 집단과 저항이 작은 집단이 같다.** 이 책의 롤아웃 순서 설계에 직접 쓸 수 있는 강력한 정합성이다.

---

- **Kellogg, K. C., Valentine, M. A., & Christin, A. (2020). 「Algorithms at Work: The New Contested Terrain of Control」.** `[PR]` Academy of Management Annals, 14(1), 366–410. DOI: 10.5465/annals.2018.0174. 온라인 게재 2020-01-15. 검색: 2026-09-05 기준.
  - **핵심 주장:** 조직 내 알고리즘 기술이 **조직 통제(organizational control)를 재편**하는 방식을 학제적으로 종합한 리뷰. Edwards(1979)의 **"쟁투의 장(contested terrain)"** 관점 — 경영자는 노동의 가치를 극대화하려 생산 기술을 도입하고 노동자는 저항한다 — 을 틀로 삼는다. 작업장 알고리즘 통제가 작동하는 **여섯 가지 주요 기제("6 Rs")** 를 식별한다.
  - ⚠️ **"6 Rs"의 개별 항목명을 이번 검색으로 확정하지 못했다.** (통상 restricting, recommending, recording, rating, replacing, rewarding으로 인용되나 **원문 pp. 366–410에서 확인 필요.**) 저자 공개 PDF: angelechristin.com/wp-content/uploads/2020/01/Algorithms-at-Work_Annals.pdf
  - **이 책에 쓸 수 있는 부분: 이 책의 가장 위험한 지점을 정면으로 비추는 문헌.** "에이전트를 등록하고 로그를 남긴다"는 설계는 **알고리즘 통제 장치와 기술적으로 구별되지 않는다.** 로그는 감사에도 쓰이고 감시에도 쓰인다. 이 책이 이 긴장을 회피하면 현장에서 반드시 역풍을 맞는다. Kellogg 외의 프레임은 **"통제는 늘 쟁투의 장"** 이라는 것 — 즉 등록 체계의 도입은 기술 프로젝트가 아니라 **협상**이다.
  - **인용 가능한 개념:** "contested terrain", "6 Rs", 그리고 알고리즘 통제가 **경영자가 노동 가치를 극대화하는 수단**이자 **노동자 저항의 대상**이라는 이중성.
  - **한계·반박:** **리뷰 논문**이며 자체 실증이 없다. 또 노동 과정 이론(labor process theory)의 관점이 강해, 협력적 도입 사례를 상대적으로 덜 다룬다.

- **전자적 성과 모니터링(EPM)의 메타분석 — 감시로 인식될 때의 실증적 대가**
  - **Ravid, D. M. 외 (2023). 「A meta-analysis of the effects of electronic performance monitoring on work outcomes」.** `[PR]` **Personnel Psychology**. DOI: 10.1111/peps.12514. ⚠️ **정확한 권·호·페이지 미확인.**
  - **⚠️ 수치 귀속 주의:** 검색 과정에서 "**94개 독립 표본, 총 23,461명 참가자**"라는 수치가 확인되었으나, 이것이 위 Ravid 외 (Personnel Psychology)의 것인지 **인접 메타분석**(「The impact of electronic monitoring on employees' job satisfaction, stress, performance, and counterproductive work behavior: A meta-analysis」, *Computers in Human Behavior Reports*, 2022)의 것인지 **판별되지 않았다. 본문 인용 전 반드시 확정할 것.**
  - **확인된 발견 (메타분석 종합):**
    - **EPM이 노동자 성과를 개선한다는 증거는 없다** ("no evidence that EPM improves worker performance").
    - **EPM의 존재는 모니터링의 특성과 무관하게 노동자 스트레스 증가와 연관**된다.
    - **더 투명하고 덜 침습적으로 모니터링하는 조직은 노동자로부터 더 긍정적인 태도를 기대할 수 있다.**
    - 모니터링이 **자율성을 줄이고 성과 지표를 강조하면 스트레스가 증가**할 가능성이 높다.
    - **전자 모니터링과 반생산적 업무 행동(CWB) 사이에 정적 관계**가 발견되었다.
  - **이 책에 쓸 수 있는 부분: 로깅 설계의 결정적 제약 조건.** 에이전트 활동 로깅은 **에이전트를 대상으로 하지 사람을 대상으로 하지 않는다**는 경계를 설계와 커뮤니케이션 양쪽에서 명확히 해야 한다. 그리고 메타분석이 준 처방은 정확하다 — **투명하게, 덜 침습적으로.** 등록·로깅 정책을 공개하고, 무엇이 수집되고 무엇이 수집되지 않는지를 명시하는 것이 실증적으로 지지되는 설계다.
  - **한계·반박:** 사람 모니터링 연구이지 **에이전트 로깅 연구가 아니다.** 직접 외삽은 부당하다. 그러나 **직원이 에이전트 로그를 자기 감시로 인식하는 순간** 이 결과들이 그대로 발동한다는 것이 요점이다.

---

- **Hughes, M. (2011). 「Do 70 Per Cent of All Organizational Change Initiatives Really Fail?」.** `[PR]` Journal of Change Management, 11(4), 451–464. DOI: 10.1080/14697017.2011.630506. 2011-12. 검색: 2026-09-05 기준.
  - **핵심 주장: 변화관리 담론의 가장 유명한 통계가 근거 없다는 것을 문헌 추적으로 입증한다.** "조직 변화 이니셔티브의 70%가 실패한다"는 수치가 등장하는 **다섯 개의 출판된 사례**를 비판적으로 검토한 결과, **그런 서사가 대중적으로 존재한다는 것은 인정하되, 그것을 뒷받침하는 타당하고 신뢰할 만한 실증 증거는 없다**고 결론짓는다.
  - **핵심 발견 (인용 가능):** Hughes는 70% 주장의 가장 저명한 출처 다섯을 추적했다 — **Hammer & Champy, Beer & Nohria, Bain & Company 기사, McKinsey 기사, 그리고 Kotter.** 각각의 경우 **출처가 증거 없이 그 숫자를 진술했거나, 증거 없이 그 숫자를 진술한 다른 출처를 인용**하고 있었다.
  - **이 책에 쓸 수 있는 부분: 이 책이 변화관리를 다루는 태도 자체를 규정하는 논문.** AX 문서와 컨설팅 자료에 "변화의 70%는 실패한다"가 그대로 복사되어 다닌다. 이 책이 그것을 인용하지 않고 **왜 인용하지 않는지 밝히는 것**만으로도 다른 책들과 구별된다. 그리고 더 중요한 함의: **인기 있는 프레임이 반드시 검증된 프레임은 아니다.**
  - **인용 가능한 문장/수치:** "whilst the existence of a popular narrative of 70 percent organizational change failure is acknowledged, **there is no valid and reliable empirical evidence to support such a narrative.**"

- **Kotter 8단계 / ADKAR의 실증적 지위 — ⚠️ 주의해서 다룰 것**
  - **확인된 사실:**
    - Hughes(2011)는 70% 수치를 다섯 출처에서 추적했고 **Kotter를 그중 하나로 포함**시켰으며, 어느 출처에도 타당한 실증 근거가 없다고 결론지었다.
    - Kotter 모델에 대한 통상적 비판 세 갈래: **(a) 선형적**이며 실제 변화는 선형이 아니다 (Kotter Inc. 자신도 *Accelerate*에서 단계를 동시적인 것으로 재구성하며 이를 사실상 인정), **(b) 탑다운**이어서 리더가 무엇을 해야 하는지는 강하지만 나머지 모두가 변화를 어떻게 경험하는지는 얇다, **(c) 개인 수준의 정서적 여정**(두려움·저항·상실감·수용)을 다루지 않는다.
    - ADKAR(Prosci)은 **Kotter 8단계 모델의 영향이 뚜렷**하며, 두 모델은 서로 다른 방식으로 보완적이라고 통상 설명된다.
  - ⚠️ **아래 진술들은 검색으로 접한 2차 자료(블로그·컨설팅 사이트)의 주장이며 학술 문헌으로 확인하지 못했다. 이 책에 쓰려면 반드시 1차 출처 확인이 필요하다:**
    - "Kotter 모델은 주로 일화적 증거 — Kotter 자신의 관찰과 컨설팅 경험 — 에 기반하며 체계적 연구가 아니다"
    - "Kotter가 분석했다고 주장하는 '100개 이상의 기업'은 표본으로 문서화된 적이 없다 — 산업 구분도, 규모 구분도, 분석 방법론도 없다"
    - "실증적으로 검증된 예측 모델이 아니다 — 8단계를 모두 따른다고 성공이 보장되지 않는다"
  - **이 책에 쓸 수 있는 부분 (신중하게):** **"인기와 실증 근거의 간극"은 좋은 논쟁 소재지만, 이 책이 그 논쟁을 하려면 Hughes(2011) 같은 피어리뷰 근거 위에서만 해야 한다.** 안전한 논지는 이것이다 — **Kotter를 쓰지 말라는 게 아니라, Kotter가 실증 검증된 예측 모델이라고 믿지 말라는 것.** 그리고 **대안으로 Klein & Sorra(1996, AMR)의 구현 모델**을 제시한다 — 이쪽은 후속 실증 검증이 이루어진 이론이다.
  - **관련 학술 문헌 (확인됨):** 「Why Vilifying the Status Quo Can Derail a Change Effort: Kotter's Contradiction, and Theory Adaptation」, *Journal of Change Management* (Taylor & Francis), DOI: 10.1080/14697017.2022.2137835. ⚠️ 저자·권호 미확인. **Kotter의 1단계("위기감 조성")가 역효과를 낼 수 있다는 이론적 반박** — AX 도입에서 "안 하면 도태된다"는 위기 프레임을 남발하는 실무 관행에 직접 적용된다. **후속 확인 강력 권장.**

---

- **Green, B. (2022). 「The flaws of policies requiring human oversight of government algorithms」.** `[PR]` Computer Law & Security Review, Vol. 45 (2022). SSRN 3921216. arXiv:2109.05067. **Future of Privacy Forum "Privacy Papers for Policymakers" 수상 (2022).** 검색: 2026-09-05 기준.
  - **핵심 주장: 이 책의 등록·감독 설계에 직접 반영되어야 할 가장 날카로운 비판.** 정부 알고리즘에 대한 인간 감독을 규정한 **41개 정책**을 조사한 결과, 이들이 **두 가지 심각한 결함**을 갖는다고 결론짓는다:
    1. **증거에 따르면 사람들은 요구되는 감독 기능을 수행할 능력이 없다.**
    2. 첫 번째 결함의 결과로, **인간 감독 정책은 결함 있고 논쟁적인 알고리즘의 정부 사용을 정당화(legitimize)하면서 그 도구의 근본 문제는 다루지 않는다.**
  - **핵심 주장 (인용 가능):** 인간 감독 정책은 알고리즘 의사결정의 잠재적 해악으로부터 보호하기는커녕, **"알고리즘 채택에 대한 잘못된 안전감(a false sense of security)을 제공하고, 벤더와 기관이 알고리즘 피해에 대한 책임을 회피(shirk accountability)하게 만든다."**
  - **대안:** 정부 알고리즘 규제의 중심 기제를 **인간 감독(human oversight)에서 제도적 감독(institutional oversight)으로 전환**할 것을 제안한다.
  - **이 책에 쓸 수 있는 부분: "매니저를 붙이면 된다"는 이 책의 설계에 대한 가장 강한 반론이자, 동시에 그 설계를 정교하게 만드는 재료.** 사람 한 명을 승인자로 세워놓는 것은 **책임 세탁(accountability laundering)** 이 될 수 있다 — 사고가 나면 "승인자가 있었다"로 방어하고, 실제로 그 승인자는 판단할 능력도 시간도 없었다. Green의 대안(제도적 감독)은 이 책의 방향과 오히려 일치한다 — **개인 감독자가 아니라 등록·로그·감사라는 제도로 감독을 구성하라.** 이 논문을 정면으로 다루면 이 책의 설계가 순진하지 않다는 것을 증명할 수 있다.
  - **인용 가능한 문장/수치:** **"41 policies"**, "**people are unable to perform the desired oversight functions**", "**a false sense of security**", "**shirk accountability**", 그리고 처방 "**from human oversight to institutional oversight.**"
  - **한계·반박:** **정부 알고리즘 맥락**이며 기업 조직과는 인센티브 구조가 다르다. 또 41개는 정책 문서 분석이지 감독자 행동의 직접 실측이 아니다 — 다만 "사람들이 감독 기능을 수행할 능력이 없다"는 근거는 아래 자동화 편향 문헌에서 온다.

- **Laux, J. (2023). 「Institutionalised distrust and human oversight of artificial intelligence: towards a democratic design of AI governance under the European Union AI Act」.** `[PR]` AI & Society. DOI: 10.1007/s00146-023-01777-z. 온라인 게재 **2023-08-25**. SSRN 4377481. ⚠️ 권·호·페이지 미확인. 검색: 2026-09-05 기준.
  - **핵심 주장:** EU AI Act를 포함한 신흥 감독 법제를 조사한 결과, **AI Act는 인간 감독자의 역량(competence)에 관심을 두지만, 효과적 감독을 어떻게 달성할지에 대한 지침은 거의 제공하지 않으며, AI 개발자의 감독 관련 의무를 미정의 상태로 남긴다.** 저자는 **인간 감독 역할의 새로운 분류 체계**를 제시하는데, 기준은 **인간의 개입이 AI가 내리거나 지원한 결정에 대해 구성적(constitutive)인가, 아니면 교정적(corrective)인가**이다. 그리고 민주주의 통치에서 역사적으로 실천되어온 **"불신의 제도화(institutionalisation of distrust)"** 를 AI 거버넌스에 처음으로 적용한다 — **인간 감독자의 오류 가능성을 미리 전제하고, 제도 설계 수준에서 그것을 완화**함으로써 인간 감독의 신뢰성을 높이자는 것.
  - **이 책에 쓸 수 있는 부분: Green의 비판에 대한 건설적 응답.** "감독자를 세우되, **감독자가 틀릴 것을 전제로 설계하라.**" 이것이 이 책의 매니저 설계에 들어가야 할 원칙이다. 그리고 **구성적 개입 vs 교정적 개입**의 구분이 실무적으로 유용하다 — 에이전트의 어떤 행위는 사람의 사전 승인 없이는 성립하지 않아야 하고(구성적), 어떤 행위는 사후 교정으로 충분하다(교정적). **등록부의 권한 필드를 이 두 등급으로 나누는 설계**를 제안할 수 있다.
  - **인용 가능한 개념:** "institutionalisation of distrust", constitutive vs corrective oversight, 그리고 AI Act가 감독을 요구하되 **"does not provide much guidance on how to achieve effective oversight."**
  - **한계·반박:** 법·정치이론 논문이며 실증 없음. EU 맥락 특수성.

- **Skitka, L. J., Mosier, K. L., & Burdick, M. (1999). 「Does automation bias decision-making?」.** `[PR]` International Journal of Human-Computer Studies, 51(5), 991–1006. DOI: 10.1006/ijhc.1999.0252. 검색: 2026-09-05 기준.
  - **핵심 주장: "감독자가 감독하지 못한다"는 Green의 전제에 대한 고전적 실증 근거.** **자동화 편향(automation bias)** — 자동화를 **경계심 있는 정보 탐색과 처리의 휴리스틱 대체물로 사용하는 경향** — 을 정의하고 측정한다.
  - **방법·결과 (원문 그대로):** 시뮬레이션 비행 과제에서, 시스템 상태를 모니터링하고 의사결정 권고를 제공하는 컴퓨터가 있는 조건과 없는 조건의 오류율을 비교했다. **결과: 비자동화 조건의 참가자가, 매우 신뢰할 만하지만 완벽하지는 않은(very but not perfectly reliable) 자동화 보조를 받은 참가자보다 모니터링 과제에서 더 나은 성과를 냈다.**
  - **이 책에 쓸 수 있는 부분: 이것이 이 책의 인간 감독 설계에서 가장 중요한 한 문장이다 — "거의 항상 맞는 시스템이 가장 위험하다."** 에이전트가 95% 맞으면 사람은 검토를 멈춘다. 오히려 70% 맞는 에이전트가 더 안전하게 감독된다. 이것은 **에이전트 성능 향상이 감독 품질을 떨어뜨린다**는 역설이며, 등록 체계가 성능 지표와 감독 강도를 **함께** 관리해야 하는 이유다.
  - **인용 가능한 개념:** automation bias = "the tendency to use automation as **a heuristic replacement for vigilant information seeking and processing**." 그리고 비자동화 조건이 준(準)신뢰 자동화 조건을 능가했다는 결과.
  - **관련 후속:** 같은 연구진의 「Automation bias and errors: are crews better than individuals?」 (2000, *The International Journal of Aviation Psychology*) — **팀이 개인보다 나은가**를 검증. ⚠️ 서지 재확인 필요. **에이전트 감독을 개인이 아니라 팀에 맡길 때의 효과라는 실무 질문에 직접 대응한다.**
  - **한계·반박:** 1999년 항공 시뮬레이션 연구다. 현대 LLM 에이전트의 오류 양상(그럴듯한 환각)은 당시 자동화의 오류 양상과 다르다 — 오히려 **더 탐지하기 어렵다**는 방향으로 다르다.

- **Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). 「To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making」.** `[PR]` Proceedings of the ACM on Human-Computer Interaction (PACM HCI), 5(CSCW1), Article 188, 1–21. DOI: 10.1145/3449287. 2021-04-22. arXiv:2102.09692. 검색: 2026-09-05 기준.
  - **핵심 주장:** AI 기반 의사결정 지원 도구를 쓰는 사람들은 **AI의 제안이 틀렸을 때조차 받아들이는 과의존(overreliance)** 을 자주 보인다. 저자들은 사람이 AI 설명에 더 사려 깊게 관여하도록 **강제하는 개입 — 인지적 강제 기능(cognitive forcing functions)** 세 가지를 설계하고 실험했다.
  - **핵심 발견:** 인지적 강제 기능은 **비판적 평가를 유도해 과의존을 줄인다.** (⚠️ 정확한 효과 크기는 이번 검색으로 확보하지 못했다 — 원문 확인 필요.)
  - **이 책에 쓸 수 있는 부분: "승인 버튼을 누르게 하는 것"과 "실제로 검토하게 하는 것"의 차이를 설계로 구현하는 방법.** Green의 rubber-stamping 비판에 대한 **UI/워크플로 수준의 처방**이 여기 있다. 예: 에이전트의 결론을 보여주기 전에 사람에게 먼저 자기 판단을 적게 하기, 일정 시간 지연 후에만 AI 답을 노출하기 등. **등록된 에이전트의 감독 절차를 설계할 때 이 문헌군이 정본 참조가 된다.**
  - **관련 문헌 (확인됨):**
    - Bansal 외 (CHI 2021): **AI 설명이 팀 성과의 상보성(complementary team performance)을 높이지 못했고, 오히려 정답 여부와 무관하게 권고 수용률을 높이는 경향**이 있었다. ⚠️ 정확한 서지 미확인 — 통상 「Does the Whole Exceed its Parts? The Effect of AI Explanations on Complementary Team Performance」로 인용됨. **"설명을 붙이면 감독이 나아진다"는 통념에 대한 정면 반박이므로 확인 권장.**
    - Schemmer 외, 「Appropriate Reliance on AI Advice: Conceptualization and the Effect of Explanations」, `[PR]` IUI 2023, DOI: 10.1145/3581641.3584066, arXiv:2302.02187. **적정 의존(appropriate reliance)** 을 개념화하고 설명의 효과를 측정.
    - 「From Trust to Appropriate Reliance: Measurement Constructs in Human-AI Decision-Making」 arXiv:2604.23896 (2026-04) `[PP]` ⚠️ 미검증 — 최신 측정론 정리.
  - **핵심 개념 정리 (이 책에 유용):**
    - **적정 의존(appropriate reliance)** = AI 조언이 맞을 때 따르고 틀릴 때 따르지 않는 것. 즉 **의존의 양이 아니라 의존의 정확성.**
    - **과의존(over-reliance)** = 틀린 조언에 맹목적으로 동의 / **과소의존(under-reliance)** = 맞는 조언을 무시. **둘은 별개 지표로 측정해야 한다.**
    - 적정 의존은 **잘 보정된(well-calibrated) AI 신뢰도**를 요구하는데, **현대 신경망은 보정이 나쁘다** — 높은 신뢰도 예측이 자주 틀리고, 낮은 신뢰도 예측이 맞기도 한다.

---

- **인간-에이전트 팀(human-agent teaming) — 연구 지형**
  - **Wildman, J. L., Nguyen, D., Thayer, A. L., Robbins-Roth, V. T., Carroll, M., Carmody, K., Ficke, C., Akib, M., & Addis, A. (2024). 「Trust in Human-Agent Teams: A Multilevel Perspective and Future Research Agenda」.** `[PR]` Sage 저널 게재, DOI: 10.1177/20413866241253278. ⚠️ 저널명·권호 미확인 (*Organizational Psychology Review*로 추정 — 확인 필요). 검색: 2026-09-05 기준.
    - **다층적 관점** — 신뢰를 개인·팀·조직 수준으로 나누어 보는 틀. 이 책의 "에이전트를 팀원으로 등록한다"는 발상에 직접 대응.
  - **「Adaptive Human-Agent Teaming: A Review of Empirical Studies from the Process Dynamics Perspective」** arXiv:2504.10918 (2025-04) `[PP]` ⚠️ 저자 미확인.
    - **확인된 발견:** 2019~2024년 인간-에이전트 팀 실증 연구에서 **주관적 측정(자기 보고)이 압도적으로 지배적**이며, 과제 중단·연구 간 보정 불일치 같은 한계가 있다.
  - **핵심 개념 구분 (이 책에 중요):** **신뢰(trust)는 에이전트에 대한 믿음으로 나타나고, 의존(reliance)은 행동으로 나타난다 — 사람은 신뢰하지 않으면서도 의존할 수 있다.** 따라서 **신뢰 보정은 적정 의존을 달성하는 여러 요인 중 하나일 뿐이다.**
  - **이 책에 쓸 수 있는 부분:** AX 성과 측정에서 **"직원들이 AI를 신뢰하나요?"라는 설문 문항이 왜 부족한지**의 근거. 신뢰 설문은 태도를 재고, 실제로 필요한 것은 **행동(의존)의 정확성**이다. 등록·로그 체계가 있어야 이것을 잴 수 있다 — 축1로 다시 연결된다.

---

### 축 4 커버리지

**확보한 것**
- **알고리즘 혐오 vs 알고리즘 선호의 정본 상충 3편** (Dietvorst 외 2015 JEPG / Logg 외 2019 OBHDP / Dietvorst 외 2018 Management Science) — 그리고 **처방까지** (수정 권한을 조금만 줘도 수용과 성과가 함께 오름)
- **인간 감독의 실효성 비판** — Green 2022 (CLSR, 41개 정책, "false sense of security", "shirk accountability") + Laux 2023 (AI & Society, 불신의 제도화, 구성적/교정적 구분)
- **감독이 왜 실패하는가의 인지 근거** — Skitka 외 1999 (자동화 편향, "거의 항상 맞는 시스템이 가장 위험") + Buçinca 외 2021 (CSCW, 인지적 강제 기능) + 적정 의존 개념군
- **알고리즘 관리·감시의 조직 이론과 실증** — Kellogg 외 2020 (AMA, contested terrain, 6 Rs) + EPM 메타분석 (성과 개선 증거 없음, 스트레스 증가, CWB와 정적 관계, "투명하게·덜 침습적으로")
- **직업 정체성 위협** — Shonhe & Min 2025 (AI & Society, n=413, XAI와 AI 정체성이 지렛대, 문화는 무효), 그리고 **저항이 작은 집단 = 효과가 큰 집단**이라는 축3과의 정합성
- **변화 프레임의 실증적 지위** — Hughes 2011 (JCM, 70% 신화 해체, Kotter 포함 5개 출처 추적) + 대안 이론 (Klein & Sorra 1996, 축3 참조)
- 기술 수용 모델의 기준점 (UTAUT2, Venkatesh 외 2012 MISQ, n=1,512, 설명 분산 56%→74%)
- 인간-에이전트 팀 연구 지형과 신뢰/의존 개념 구분

**비어 있는 것 (후속 리서치 권장)**
- ⚠️ **Kellogg 외 2020의 "6 Rs" 개별 항목명** 미확정 — 저자 공개 PDF 있음, 저술 전 확인 필수.
- ⚠️ **EPM 메타분석의 표본 수치(94표본/23,461명) 귀속** 미확정 — Ravid 2023(Personnel Psychology)인지 2022 CHB Reports인지 확정 필요.
- ⚠️ **Buçinca 외 2021의 효과 크기**, **Bansal 외 CHI 2021의 정확한 서지** 미확보.
- **Kotter/ADKAR에 대한 본격적 피어리뷰 비판 논문**을 Hughes(2011) 외에 확보하지 못했다. 「Kotter's Contradiction」(JCM 2022, DOI: 10.1080/14697017.2022.2137835)이 유망한 후보이나 미확인 — **"위기감 조성이 역효과"라는 논지는 이 책에 매우 유용하므로 확인 강력 권장.**
- **직무 재설계(job crafting)와 AI**의 실증을 확보하지 못했다 — 정체성 위협 쪽만 확보됨.
- **에이전트(자율 행위자)와 사람이 한 팀으로 일할 때의 조직 수준 실증**은 사실상 존재하지 않는다. 기존 human-agent teaming 문헌은 대부분 **의사결정 지원 도구(조언자)** 맥락이지 **자율 실행자** 맥락이 아니다. ⚠️ **이 공백은 이 책이 정직하게 밝히고 넘어가야 할 지점이다.**
- **한국 조직의 AI 수용·저항 실증** 없음.

---

## 상충하는 연구 결과 (병기 필수)

> 아래 네 쌍은 **어느 한쪽만 인용하면 이 책이 틀린 책이 된다.** 저술 시 반드시 양쪽을 함께 제시하고, 왜 갈리는지(조건 차이)를 설명할 것.

### 상충 1 — AI는 생산성을 올리는가, 내리는가

| 근거 | 결과 | 대상 | 조건 |
|---|---|---|---|
| Peng 외 2023 `[PP]` | **−55.8% 소요 시간** (빨라짐) | 개발자 | HTTP 서버 구현, **단일 그린필드 과제** |
| Cui 외 2025 `[PR]` Management Science | **+26.08% 완료 과제** (SE 10.3%), n=4,867 | 개발자 | 3개 기업 현장 RCT, **코드 완성 도구** |
| **METR 2025** `[PP]` | **+19% 소요 시간 (느려짐)**, n=16 / 246과제 | 개발자 | **평균 5년 숙련된 성숙 오픈소스 코드베이스** |

**갈리는 이유 (이 책의 해석):** 세 연구는 **같은 직군을 다르게 잘랐다.** 그린필드 단일 과제 → 크게 빨라짐. 일상적 코드 완성 → 중간. **자기가 5년 다룬 코드베이스에서 복잡한 실제 과제 → 느려짐.** 즉 **AI의 상대 우위는 사용자의 도메인 숙련도에 반비례**한다. 이것은 Brynjolfsson 외(2025)·Cui 외(2025)의 이질성 발견과 **완벽하게 정합**한다 — 경험이 적을수록 이득이 크다.

**이 책의 결론으로 삼을 만한 것:** "AI가 생산성을 올리는가"는 **잘못된 질문**이다. 옳은 질문은 **"누구의, 어떤 과제의 생산성을 올리는가"** 이며, 그 답을 조직이 알려면 **측정 체계 = 등록·로그**가 있어야 한다. 실증들이 이 책의 주장으로 수렴한다.

### 상충 2 — 사람은 알고리즘을 싫어하는가, 좋아하는가

| 근거 | 결과 | 대상 | 조건 |
|---|---|---|---|
| Dietvorst 외 2015 `[PR]` JEPG | **알고리즘 혐오** — 오류를 본 뒤 열등한 인간을 선택 | 실험 참가자 | **알고리즘이 틀리는 것을 본 뒤**, 자기 인센티브를 거는 선택 |
| Logg 외 2019 `[PR]` OBHDP | **알고리즘 선호** — 조언이 알고리즘 출처일 때 더 따름 | **일반인(lay people)** | 수치 추정·인기 예측, **조언 수용** 상황 |
| Dietvorst 외 2018 `[PR]` Mgmt Sci | **수정 권한을 주면 혐오가 크게 줄고 성과도 개선** | 실험 참가자 | 아주 제한적인 수정 권한이어도 효과 유지 |

**갈리는 이유:** **(a) 오류를 목격했는가**, **(b) 조언인가 대체인가**, **(c) 판단자가 자기 전문성을 걸고 있는가.** Logg의 후속 방향은 **전문가는 알고리즘 조언을 덜 따른다**는 것이므로, 조직 내 전문가 집단에는 Dietvorst 쪽이 더 가깝다.

**이 책의 결론으로 삼을 만한 것:** **수용 성향은 조직의 고정 속성이 아니라 설계 변수다.** 그리고 검증된 처방이 하나 있다 — **작은 수정 권한.** 다만 이는 축1의 책임 귀속과 긴장한다(사용자가 수정했으면 책임은 누구에게?). **그 긴장을 등록부의 권한 필드에서 명시적으로 해소하는 것이 이 책의 설계 과제다.**

### 상충 3 — 암묵지는 형식화될 수 있는가

| 근거 | 입장 |
|---|---|
| Nonaka 1994 `[PR]` Organization Science | **가능하다.** SECI의 외재화(Externalization)를 통해 암묵지가 형식지로 전환된다 |
| Gourlay 2006 `[PR]` Journal of Management Studies | **네 모드 중 어느 것도 더 단순한 설명으로 대체 불가능한 증거를 갖지 못했다.** Nonaka의 틀은 **본질적으로 암묵적인 지식을 누락**하며, 지식이 사실상 관리자에 의해 창조되는 주관적 정의를 쓴다 |

**이 책의 결론으로 삼을 만한 것:** SOP 작성은 **전부를 옮기는 작업이 아니라 옮길 수 있는 것을 골라내는 작업**이다. 형식화 불가능한 영역을 인정하고 **그 영역을 사람에게 남기는 경계 설정이 설계의 일부**여야 한다. "모든 노하우를 문서화하면 에이전트가 다 한다"는 전제로 시작한 AX 프로젝트는 반드시 좌초한다.

### 상충 4 — 인간 감독은 작동하는가

| 근거 | 입장 |
|---|---|
| **EU AI Act Art. 14 등 규제 프레임** | 인간 감독이 고위험 AI의 핵심 안전장치 |
| Green 2022 `[PR]` CLSR | **41개 정책 조사 — 사람들은 요구되는 감독 기능을 수행할 능력이 없으며, 감독 정책은 오히려 결함 있는 알고리즘 사용을 정당화하고 책임 회피를 가능하게 한다** ("false sense of security") |
| Skitka 외 1999 `[PR]` IJHCS | **자동화 편향** — 비자동화 조건이 "매우 신뢰할 만하지만 완벽하지 않은" 자동화 보조 조건보다 모니터링 성과가 좋았다 |
| Laux 2023 `[PR]` AI & Society | 감독을 폐기하지 말고 **불신을 제도화**하라 — 감독자의 오류 가능성을 전제로 제도를 설계 |
| Buçinca 외 2021 `[PR]` CSCW | **인지적 강제 기능**으로 과의존을 줄일 수 있다 (설계 수준 처방) |

**이 책의 결론으로 삼을 만한 것:** **매니저를 세우는 것만으로는 감독이 되지 않는다.** 이것이 이 책의 등록 설계에 반영되어야 할 가장 어려운 진실이다. 세 겹의 처방이 문헌에서 나온다 — **(1) 제도적 감독**(개인이 아니라 등록·로그·감사로 감독을 구성, Green), **(2) 감독자의 오류를 전제한 설계**(구성적/교정적 권한 등급 분리, Laux), **(3) 인지적 강제 기능**(승인 버튼이 아니라 실제 검토를 유도하는 워크플로, Buçinca). 그리고 가장 반직관적인 함의 — **에이전트 성능이 좋아질수록 인간 감독의 품질은 떨어진다**(Skitka). **성능 지표와 감독 강도를 함께 관리하지 않으면 개선이 위험을 만든다.**

---

## 참고문헌 전체

> 정렬: 축별 → 발행 연도순. 각 항목에 게재 유형과 확인 상태 표기. **검색: 2026-09-05 기준.**

### 축 1 — 에이전트 등록·아이덴티티·거버넌스

1. Miller, M. S., Yee, K.-P., & Shapiro, J. (2003). *Capability Myths Demolished*. Technical Report SRL2003-02, Johns Hopkins University Systems Research Laboratory. `[기술보고서]` URL: papers.agoric.com/assets/pdf/papers/capability-myths-demolished.pdf
2. Esteva, M., Rodríguez-Aguilar, J. A., Sierra, C., Garcia, P., & Arcos, J. L. (2001). On the Formal Specification of Electronic Institutions. *Agent Mediated Electronic Commerce*, LNAI 1991, 126–147. Springer. `[PR]` ⚠️ 2차 출처 기반 — 권·페이지 재확인 필요
3. Hübner, J. F., Sichman, J. S., & Boissier, O. (2002). A Model for the Structural, Functional, and Deontic Specification of Organizations in Multiagent Systems. *SBIA 2002*, LNCS/LNAI 2507. Springer. DOI: 10.1007/3-540-36127-8_12 `[PR]` PDF: moise.sourceforge.net/doc/publications/Hubner-sbia2002.pdf
4. Dignum, V. (2004). *A Model for Organizational Interaction* (OperA). PhD dissertation, Utrecht University / SIKS. `[학위논문]` ⚠️ 부제 미확인
5. Esteva, M., Rodríguez-Aguilar, J. A., Rosell, B., & Arcos, J. L. (2004). AMELI: An Agent-based Middleware for Electronic Institutions. *AAMAS 2004*, vol. 1, 236–243. ACM. `[PR]` ⚠️ 2차 출처 기반
6. Hübner, J. F., Sichman, J. S., & Boissier, O. (2007). Developing organised multi-agent systems using the MOISE+ model: programming issues at the system and agent levels. *International Journal of Agent-Oriented Software Engineering*. DOI: 10.1504/IJAOSE.2007.016266 `[PR]`
7. Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D., & Gebru, T. (2019). Model Cards for Model Reporting. *FAT* '19*. DOI: 10.1145/3287560.3287596. arXiv:1810.03993. `[PR]` 2019-01
8. McGregor, S. (2021). Preventing Repeated Real World AI Failures by Cataloging Incidents: The AI Incident Database. *Proceedings of the AAAI Conference on Artificial Intelligence*, 35(17), 15458–15463. arXiv:2011.08512. `[PR]` 2021
9. Santoni de Sio, F., & Mecacci, G. (2021). Four Responsibility Gaps with Artificial Intelligence: Why they Matter and How to Address them. *Philosophy & Technology*, 34(4), 1057–1084. DOI: 10.1007/s13347-021-00450-x `[PR]` 2021
10. Chan, A., Ezell, C., Kaufmann, M., Wei, K., Hammond, L., Bradley, H., Bluemke, E., Rajkumar, N., Krueger, D., Kolt, N., Heim, L., & Anderljung, M. (2024). Visibility into AI Agents. *ACM FAccT '24*. DOI: 10.1145/3630106.3658948. arXiv:2401.13138v6 (2024-05-17). `[PR]`
11. Chan, A. (2024). IDs for AI Systems. arXiv:2406.12137 (2024-06-17, 최종 수정 2024-10-28). `[PP]`
12. Casper, S. 외 (2025). The AI Agent Index. arXiv:2502.01635 (2025-02). `[PP]` ⚠️ 전체 저자 미확인
13. Kolt, N. (2025). Governing AI Agents. *101 Notre Dame Law Review* (forthcoming). arXiv:2501.07913. SSRN 4772956. 최근 개정 2025-02-11. `[PP→PR]`
14. South, T., Marro, S., Hardjono, T., Mahari, R., Whitney, C. D., Greenwood, D., Chan, A., & Pentland, A. (2025). Authenticated Delegation and Authorized AI Agents. arXiv:2501.09674 (2025-01-16). ICML 2025 게재 제목: *Position: AI Agents Need Authenticated Delegation* (OpenReview 9skHxuHyM4). `[PP→PR]`
15. Chan, A., Wei, K., Huang, S., Rajkumar, N., Perrier, E., Lazar, S., Hadfield, G. K., & Anderljung, M. (2025). Infrastructure for AI Agents. *Transactions on Machine Learning Research (TMLR)*. arXiv:2501.10114v3 (2025-06-19). `[PR]`
16. Kraprayoon, J. 외 / IAPS (2025). AI Agent Governance: A Field Guide. arXiv:2505.21808 (2025-05). `[보고서]` ⚠️ 전체 저자 미확인
17. South, T., Nagabhushanaradhya, S. 외 (19인) (2025). Identity Management for Agentic AI. *OpenID Foundation Whitepaper 2025*. arXiv:2510.25819 (2025-10-29). CC BY-SA 4.0. `[백서]`
18. Kaptein, M., Khan, V.-J., & Podstavnychy, A. (2026). Runtime Governance for AI Agents: Policies on Paths. arXiv:2603.16586 (2026-03-17). `[PP]`
19. Nian, Y., Yuan, A., Zhang, H., Li, J., Li, L., Hu, X., Wei, H., Xiao, X., Xiao, C., & Zhao, Y. (2026). Auditable Agents. arXiv:2604.05485 (v1 2026-04-07, v2 2026-08-13). `[PP]`
20. Otsuka, T., Toyoda, K., & Leung, A. (2026). AI Identity: Standards, Gaps, and Research Directions for AI Agents. arXiv:2604.23280 (2026-04-25). `[PP]`
21. Atkinson, D. I., & O'Bryan, J. E. (2026). Government AI Use as a Monitoring Primitive: A Public Document Pilot Study. arXiv:2607.04543 (2026-07-05). ICML 2026 Workshop on Technical AI Governance. `[PP→워크숍]`

**축 1 표준·정책 문서 (학술 아님 — 별도 취급)**
- IETF Internet-Draft: *OAuth 2.0 Extension: On-Behalf-Of User Authorization for AI Agents* (draft-oauth-ai-agents-on-behalf-of-user-00) ⚠️ 드래프트, 표준 아님
- 미 연방기관 AI Use Case Inventory: github.com/ombegov/2025-Federal-Agency-AI-Use-Case-Inventory (2025년판, 56개 기관 3,611건)
- Center for Democracy and Technology, *Exploring the 2024 Federal AI Inventories: Key Improvements, Trends, and Continued Inconsistencies* `[시민사회 분석]`

### 축 2 — SOP·절차의 형식화

22. Nonaka, I. (1994). A Dynamic Theory of Organizational Knowledge Creation. *Organization Science*, 5(1), 14–37. DOI: 10.1287/orsc.5.1.14 `[PR]`
23. Adler, P. S., & Borys, B. (1996). Two Types of Bureaucracy: Enabling and Coercive. *Administrative Science Quarterly*, 41(1), 61–89. DOI: 10.2307/2393986 `[PR]` PDF: faculty.marshall.usc.edu/Paul-Adler/research/ASQ copy-1.pdf
24. Feldman, M. S., & Pentland, B. T. (2003). Reconceptualizing Organizational Routines as a Source of Flexibility and Change. *Administrative Science Quarterly*, 48(1), 94–118. DOI: 10.2307/3556620 `[PR]` PDF: socialecology.uci.edu/sites/socialecology.uci.edu/files/users/feldmanm/Feldman_and_Pentland_2003.pdf
25. Gourlay, S. (2006). Conceptualizing Knowledge Creation: A Critique of Nonaka's Theory. *Journal of Management Studies*, 43(7), 1415–1436. DOI: 10.1111/j.1467-6486.2006.00637.x `[PR]`
26. van der Aalst, W. M. P. (2011). *Process Mining: Discovery, Conformance and Enhancement of Business Processes*. Springer. ISBN 978-3-642-19344-6. DOI: 10.1007/978-3-642-19345-3 `[PR-book]`
27. van der Aalst, W. M. P. (2016). *Process Mining: Data Science in Action* (2nd ed.). Springer. DOI: 10.1007/978-3-662-49851-4 `[PR-book]`
28. Berti, A., Schuster, D., & van der Aalst, W. (2023). Abstractions, Scenarios, and Prompt Definitions for Process Mining with LLMs: A Case Study. *BPM 2023*, 427–439. `[PR]`
29. Hong, S. 외 (2024). MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework. *ICLR 2024 (Oral)*. arXiv:2308.00352. `[PR]` ⚠️ 제1저자·전체 저자 확인 필요
30. Berti, A., Kourani, H., Häfke, H., Li, C.-Y., & Schuster, D. (2024). Evaluating Large Language Models in Process Mining: Capabilities, Benchmarks, and Evaluation Strategies. *BPMDS/EMMSAD 2024*. Springer. DOI: 10.1007/978-3-031-61007-3_2 `[PR]`
31. Berti, A., Kourani, H., & van der Aalst, W. M. P. (2024). PM-LLM-Benchmark: Evaluating Large Language Models on Process Mining Tasks. arXiv:2407.13244 (2024-07). `[PP]` ⚠️ 수치 귀속 재확인 필요
32. Nandi, S. 외 (24인) (2025/2026). SOP-Bench: Complex Industrial SOPs for Evaluating LLM Agents. arXiv:2506.08119 (v1 2025-06-09, v2 2026-02-23). 코드: github.com/amazon-science/sop-bench `[PP]`
33. Agent-S: LLM Agentic workflow to automate Standard Operating Procedures. arXiv:2503.15520 (2025-03). `[PP]` ⚠️ 저자 미확인
34. SOP-Maze: Evaluating Large Language Models on Complicated Business Standard Operating Procedures. arXiv:2510.08942 (2025-10). `[PP]` ⚠️ 저자 미확인
35. Evaluating large language models on business process modeling: framework, benchmark, and self-improvement analysis. *Software and Systems Modeling* (2025). DOI: 10.1007/s10270-025-01318-w `[PR]` ⚠️ 저자 미확인
36. Large Language Models to Enhance Business Process Modeling: Past, Present, and Future Trends. arXiv:2604.14034 (2026-04). `[PP]` ⚠️ 저자 미확인
37. Compile, Then Page: Executable SOP Programs and a Capability-Gated Runtime for Procedural LLM Agents. arXiv:2607.11346 (2026-07). `[PP]` ⚠️ 미검증 — 확인 권장

### 축 3 — 도입의 조직 경제학·실증

38. Klein, K. J., & Sorra, J. S. (1996). The Challenge of Innovation Implementation. *Academy of Management Review*, 21(4), 1055–1080. DOI: 10.5465/amr.1996.9704071863 `[PR]`
39. Brynjolfsson, E., Hitt, L. M., & Yang, S. (2002). Intangible Assets: Computers and Organizational Capital. *Brookings Papers on Economic Activity*, 2002(1). DOI: 10.1353/eca.2002.0003 `[PR]` PDF: brookings.edu/wp-content/uploads/2002/01/2002a_bpea_brynjolfsson.pdf
40. Brynjolfsson, E., Rock, D., & Syverson, C. (2017). Artificial Intelligence and the Modern Productivity Paradox: A Clash of Expectations and Statistics. *NBER Working Paper 24001* (2017-11). `[WP]`
41. Brynjolfsson, E., Rock, D., & Syverson, C. (2021). The Productivity J-Curve: How Intangibles Complement General Purpose Technologies. *American Economic Journal: Macroeconomics* (2021-01). `[PR]` ⚠️ 권·호·페이지 미확인
42. Peng, S., Kalliamvakou, E., Cihon, P., & Demirer, M. (2023). The Impact of AI on Developer Productivity: Evidence from GitHub Copilot. arXiv:2302.06590 (2023-02-13). `[PP]` ⚠️ 표본 크기(N) 미확인
43. Noy, S., & Zhang, W. (2023). Experimental evidence on the productivity effects of generative artificial intelligence. *Science* (2023-07-13). DOI: 10.1126/science.adh2586. SSRN 4375283. `[PR]`
44. McElheran, K., Li, J. F., Brynjolfsson, E., Kroff, Z., Dinlersoz, E., Foster, L., & Zolas, N. J. (2024). AI adoption in America: Who, what, and where. *Journal of Economics & Management Strategy*, 33, 375–415. DOI: 10.1111/jems.12576. NBER WP 31788. `[PR]`
45. Bick, A., Blandin, A., & Deming, D. J. (2024). The Rapid Adoption of Generative AI. *NBER Working Paper 32966* (2024-09). St. Louis Fed WP 2024-027. `[WP]` ⚠️ 이후 갱신 가능성 — 최신판 확인 권장
46. Brynjolfsson, E., Li, D., & Raymond, L. (2025). Generative AI at Work. *The Quarterly Journal of Economics*, 140(2), 889–942. NBER WP 31161 (2023-04). `[PR]`
47. Dell'Acqua, F., McFowland III, E., Mollick, E. R., Lifshitz-Assaf, H., Kellogg, K., Rajendran, S., Krayer, L., Candelon, F., & Lakhani, K. R. (2025). Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality. *Organization Science*. DOI: 10.1287/orsc.2025.21838. HBS WP 24-013 (2023-09). SSRN 4573321. `[PR]`
48. Cui, Z. (K.), Demirer, M., Jaffe, S., Musolff, L., Peng, S., & Salz, T. (2025). The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers. *Management Science*. DOI: 10.1287/mnsc.2025.00535. SSRN 4945566. `[PR]`
49. METR (2025). Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity. arXiv:2507.09089 (2025-07-10). `[PP]` ⚠️ 전체 저자 미확인
50. Silic, M. 외. From Shadow IT to Shadow AI – Threats, Risks and Opportunities for Organizations. *Strategic Change* (Wiley). DOI: 10.1002/jsc.2682 `[PR]` ⚠️ **연도·권·호 미확인 (본문 403 차단)**

### 축 4 — 변화관리·수용·저항

51. Skitka, L. J., Mosier, K. L., & Burdick, M. (1999). Does automation bias decision-making? *International Journal of Human-Computer Studies*, 51(5), 991–1006. DOI: 10.1006/ijhc.1999.0252 `[PR]`
52. Hughes, M. (2011). Do 70 Per Cent of All Organizational Change Initiatives Really Fail? *Journal of Change Management*, 11(4), 451–464. DOI: 10.1080/14697017.2011.630506 `[PR]` 2011-12
53. Venkatesh, V., Thong, J. Y. L., & Xu, X. (2012). Consumer Acceptance and Use of Information Technology: Extending the Unified Theory of Acceptance and Use of Technology. *MIS Quarterly*, 36(1), 157–178. SSRN 2002388. `[PR]`
54. Dietvorst, B. J., Simmons, J. P., & Massey, C. (2015). Algorithm Aversion: People Erroneously Avoid Algorithms After Seeing Them Err. *Journal of Experimental Psychology: General*, 144(1), 114–126. `[PR]`
55. Dietvorst, B. J., Simmons, J. P., & Massey, C. (2018). Overcoming Algorithm Aversion: People Will Use Imperfect Algorithms If They Can (Even Slightly) Modify Them. *Management Science*, 64(3), 1155–1170. DOI: 10.1287/mnsc.2016.2643. SSRN 2616787. `[PR]`
56. Logg, J. M., Minson, J. A., & Moore, D. A. (2019). Algorithm appreciation: People prefer algorithmic to human judgment. *Organizational Behavior and Human Decision Processes*, 151, 90–103. DOI: 10.1016/j.obhdp.2018.12.005. SSRN 2941774. `[PR]`
57. Kellogg, K. C., Valentine, M. A., & Christin, A. (2020). Algorithms at Work: The New Contested Terrain of Control. *Academy of Management Annals*, 14(1), 366–410. DOI: 10.5465/annals.2018.0174 `[PR]` PDF: angelechristin.com/wp-content/uploads/2020/01/Algorithms-at-Work_Annals.pdf
58. Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making. *PACM HCI*, 5(CSCW1), Article 188, 1–21. DOI: 10.1145/3449287. arXiv:2102.09692. `[PR]`
59. Green, B. (2022). The flaws of policies requiring human oversight of government algorithms. *Computer Law & Security Review*, 45. SSRN 3921216. arXiv:2109.05067. `[PR]` PDF: benzevgreen.com/wp-content/uploads/2022/04/22-clsr.pdf
60. Ravid, D. M. 외 (2023). A meta-analysis of the effects of electronic performance monitoring on work outcomes. *Personnel Psychology*. DOI: 10.1111/peps.12514 `[PR]` ⚠️ 권·호·페이지 미확인
61. Laux, J. (2023). Institutionalised distrust and human oversight of artificial intelligence: towards a democratic design of AI governance under the European Union AI Act. *AI & Society*. DOI: 10.1007/s00146-023-01777-z (2023-08-25). SSRN 4377481. `[PR]` ⚠️ 권·호 미확인
62. Schemmer, M. 외 (2023). Appropriate Reliance on AI Advice: Conceptualization and the Effect of Explanations. *IUI 2023*. DOI: 10.1145/3581641.3584066. arXiv:2302.02187. `[PR]` ⚠️ 전체 저자 미확인
63. Wildman, J. L., Nguyen, D., Thayer, A. L., Robbins-Roth, V. T., Carroll, M., Carmody, K., Ficke, C., Akib, M., & Addis, A. (2024). Trust in Human-Agent Teams: A Multilevel Perspective and Future Research Agenda. DOI: 10.1177/20413866241253278 `[PR]` ⚠️ 저널명·권호 미확인
64. Why Vilifying the Status Quo Can Derail a Change Effort: Kotter's Contradiction, and Theory Adaptation. *Journal of Change Management*. DOI: 10.1080/14697017.2022.2137835 `[PR]` ⚠️ 저자·권호 미확인 — **확인 강력 권장**
65. Shonhe, L., & Min, Q. (2025). Mitigating AI-induced professional identity threat and fostering adoption in the workplace. *AI & Society*, 40(5), 4079–4092. DOI: 10.1007/s00146-024-02170-0 (2025-01-15). `[PR]`
66. Adaptive Human-Agent Teaming: A Review of Empirical Studies from the Process Dynamics Perspective. arXiv:2504.10918 (2025-04). `[PP]` ⚠️ 저자 미확인
67. Revisiting UTAUT for the Age of AI: Understanding Employees' AI Adoption and Usage Patterns Through an Extended UTAUT Framework. arXiv:2510.15142 (2025-10). `[PP]` ⚠️ 미검증
68. From Trust to Appropriate Reliance: Measurement Constructs in Human-AI Decision-Making. arXiv:2604.23896 (2026-04). `[PP]` ⚠️ 미검증

---

## 미확인·주의 항목 (⚠️ 모아보기)

> **fact-checker 및 저술가 필독.** 아래 항목은 **본문에 쓰기 전에 반드시 원문 확인**이 필요하다. 확인 못 하면 쓰지 말고 넘길 것.

### A. 서지 정보 미확정 — 인용 전 확인 필수

| # | 항목 | 미확인 내용 | 확인처 |
|---|---|---|---|
| A1 | Esteva 외 2001, 전자 제도 | 권(LNAI 1991)·페이지(126–147) 2차 출처 기반 | Springer LNCS 1991 |
| A2 | Dignum 2004, OperA | 학위논문 정확한 부제 | Utrecht Univ. 리포지토리 |
| A3 | Esteva 외 2004, AMELI | AAMAS 2004 권·페이지 2차 출처 기반 | ACM DL |
| A4 | Casper 외 2025, AI Agent Index | **전체 저자 명단** | arxiv.org/abs/2502.01635 |
| A5 | IAPS 2025, Field Guide | **전체 저자 명단** | arxiv.org/abs/2505.21808 |
| A6 | MetaGPT (ICLR 2024) | **제1저자 표기·전체 저자** | arxiv.org/abs/2308.00352 |
| A7 | METR 2025 | **전체 저자 명단** | arxiv.org/abs/2507.09089 |
| A8 | Peng 외 2023 (Copilot) | **표본 크기 N** | arxiv.org/abs/2302.06590 |
| A9 | Silic 외, Shadow AI | **발행 연도·권·호** (본문 403) | Wiley, DOI 10.1002/jsc.2682 |
| A10 | Ravid 외 2023, EPM 메타분석 | **권·호·페이지** | Personnel Psychology |
| A11 | Laux 2023 | **권·호·페이지** | AI & Society |
| A12 | Wildman 외 2024 | **저널명·권호** (Organizational Psychology Review 추정) | DOI 10.1177/20413866241253278 |
| A13 | Kotter's Contradiction (JCM 2022) | **저자·권호** | DOI 10.1080/14697017.2022.2137835 |
| A14 | Brynjolfsson·Rock·Syverson 2021 J-curve | **권·호·페이지** | AEJ: Macroeconomics |
| A15 | Bresnahan·Brynjolfsson·Hitt (조직 보완재) | **전체 서지** | 통상 QJE 2002 |
| A16 | Schemmer 외 2023 (IUI) | **전체 저자** | DOI 10.1145/3581641.3584066 |
| A17 | Bansal 외 CHI 2021 (설명의 역효과) | **전체 서지** | ACM DL |
| A18 | Skitka·Mosier 2000, crews vs individuals | **전체 서지** | Int'l J. Aviation Psychology |
| A19 | OMNI (Vázquez-Salceda·Dignum·Dignum) | **권·페이지** | Springer LNCS |
| A20 | BPM×LLM 개별 논문 다수 (37, 33~36) | **저자·게재처** | arXiv / Springer |

### B. 수치 귀속 불명확 — 확정 전 사용 금지

| # | 수치 | 문제 | 확인 방법 |
|---|---|---|---|
| B1 | AI Agent Index의 공시 비율 (문서 70.1% / 코드 49.3% / 안전 정책 19.4% / 외부 평가 <10%) | **arXiv:2502.01635(2025년판)인지 arXiv:2602.17753(2026년판)인지 불명** | 두 논문 초록 대조 |
| B2 | Dell'Acqua 외, 경계 밖 성과 "19%" | **"19% less likely"인가 "19 percentage points less likely"인가** | Organization Science 게재본 |
| B3 | EPM 메타분석 "94개 표본 / 23,461명" | **Ravid 2023(Personnel Psych)인지 2022 CHB Reports 메타분석인지 불명** | 두 논문 방법 섹션 |
| B4 | PM-LLM-Benchmark "16개 LLM / 20개 프로세스" | **해당 논문의 수치인지 인접 논문의 수치인지 불명** | arXiv:2407.13244 원문 |
| B5 | SOP-Bench 성능 수치 (57~100%, Claude 4 Opus 72.4%, Claude 4.5 Sonnet 63.3%) | **v2(2026-02) 초록 기준 — 원문 재확인 권장**, 모델 라인업 신선도 민감 | arXiv:2506.08119v2 |
| B6 | AI Incident Database "1,000건 이상" | **2021년 시점 수치** — 현재 숫자로 쓰면 오류 | incidentdatabase.ai |
| B7 | Adler & Borys enabling 형식화 **4대 설계 특성** | **원문 미확인** — 통상 repair / internal transparency / global transparency / flexibility로 인용됨. **이 책에 가장 유용한 부분인데 미확보** | ASQ 41(1), 61–89 공개 PDF |
| B8 | Kellogg 외 2020 **"6 Rs" 개별 항목명** | **원문 미확인** — 통상 restricting/recommending/recording/rating/replacing/rewarding | AMA 14(1) 공개 PDF |
| B9 | Buçinca 외 2021 **효과 크기** | 방향(과의존 감소)만 확인, 수치 미확보 | DOI 10.1145/3449287 |
| B10 | Logg의 "전문가는 알고리즘 조언을 덜 따른다" 후속 발견 | **서지 미확인** | jennlogg.com/papers |

### C. 학술 근거 아님 — 출처 성격을 반드시 명시할 것

| # | 내용 | 성격 |
|---|---|---|
| C1 | Shadow AI 전 통계 (98% 비인가 사용 / 78% IT 승인 없이 사용 / 46% 금지해도 계속 / UpGuard 80%+ / CybSafe 38% 기밀 공유 / IBM 37%만 정책 보유 / 채택률 74%→96% / GenAI 트래픽 890% 급증 / Menlo 68% 급증) | **전부 벤더·업계 조사.** 분위기 전달용으로만, 논증 하중을 싣지 말 것 |
| C2 | 미 연방 AI use case inventory 실태 (3,611건/56기관, 105% 증가, DHS만 연장 기간 공개 등) | **시민사회 분석(CDT) + 언론 보도(Nextgov/FCW).** 원자료는 GitHub 공개 |
| C3 | "AI 파일럿의 95%가 실패" 류 수치 | **학술 검증 없음.** MIT/BCG 계열 업계 보고서 — **web-researcher가 원 출처 확인 필요. 학술 근거로 쓰면 안 됨** |
| C4 | Kotter 모델 비판 중 "100개 이상 기업이 표본으로 문서화된 적 없다", "일화적 증거에 기반" | **블로그·컨설팅 사이트 주장.** 학술 확인 실패 — **Hughes(2011) 피어리뷰 근거 위에서만 논할 것** |
| C5 | KPMG 2026 "대기업 리더 75%가 보안·컴플라이언스·감사 가능성을 최우선 요구로 꼽음", Gravitee 2026 "거버넌스 자신감 82% vs 실제 모니터링 47.1%" | **업계 설문.** 인용 시 출처·연도 명시 |
| C6 | NIST AI Agent Standards Initiative (2026-02), CSA Addendum(2025-10), WEF Framework for Agentic AI(2026-01), Singapore IMDA Model AI Governance Framework for Agentic AI(2026-01), IETF AIMS draft | **표준·정책 문서.** 학술 인용이 아니라 1차 문서로 직접 참조할 것 — **web-researcher 이관 권장** |
| C7 | SPIFFE/SPIRE 관련 arXiv 항목 (2504.14760/14761/14777/17759) | **피어리뷰 없음.** SPIFFE는 CNCF 사실상 표준이므로 **공식 스펙 문서를 1차 출처로 쓰는 편이 정확** |

### D. 신선도 경고 — 인용 시 반드시 시점 명시

| # | 항목 | 시점 | 경고 |
|---|---|---|---|
| D1 | Brynjolfsson·Li·Raymond | 도입 시점 **GPT-3.5 세대** | 모델 세대 명시 |
| D2 | Dell'Acqua 외 | **2023년 GPT-4** | jagged frontier의 모양은 세대마다 변함 |
| D3 | Noy·Zhang | **2023년 초 ChatGPT(GPT-3.5)** | 짧은 단발 과제 |
| D4 | METR | **2025년 2~6월, Cursor Pro + Claude 3.5/3.7 Sonnet** | |
| D5 | McElheran 외 | **2018년 ABS — 생성형 AI 이전** | 현재 수치로 오도 금지 |
| D6 | Bick 외 | **2024년 말 설문** | 이후 갱신 가능성 높음 |
| D7 | SOP-Bench v2 | **2026년 2월 모델 라인업** | |
| D8 | OpenID Foundation 백서 | **2025년 10월 표준 지형** | |
| D9 | Otsuka 외 AI Identity | **2026년 4월 표준 지형** | |
| D10 | AI Incident Database 건수 | **2021년** | 현재 수치 별도 확인 |

### E. 이 책이 정직하게 밝혀야 할 학술 공백

1. **"등록된 자율 에이전트"의 생산성 효과에 대한 현장 실증은 사실상 존재하지 않는다.** 축3의 모든 RCT는 chat/completion 세대(조언자·자동완성)이지 자율 실행자가 아니다.
2. **인간-에이전트 팀 문헌도 대부분 "의사결정 지원 도구" 맥락**이며, 사람과 자율 실행 에이전트가 한 팀으로 일하는 조직 수준 실증은 공백이다.
3. **SOP의 형식화 정도와 에이전트 성능의 관계**("얼마나 자세히 써야 하는가")를 직접 측정한 연구를 찾지 못했다.
4. **프로세스 마이닝을 에이전트 실행 로그에 적용해 conformance를 검사하는 루프**에 대한 연구를 특정하지 못했다 — **이 책의 독자적 기여 지점이 될 수 있다.**
5. **한국 조직 맥락의 실증**은 네 축 전부에서 확보되지 않았다 (AI 도입 생산성, SOP 형식화 실태, 수용·저항, 에이전트 거버넌스).
6. **EU AI Act 데이터베이스에 대한 본격 학술 평가 논문**을 특정하지 못했다 — 법령 원문(Art. 49, Art. 71)을 직접 인용하는 편이 안전하다.
7. **Verifiable Credentials / DID의 에이전트 적용, confidential computing attestation**에 대한 피어리뷰 실증 미확보 — W3C 권고안 등 표준 문서로 대체 필요.
