<!-- 검색 시점: 2026-09-05 기준 -->
<!-- 2차 보강. 1차 결과는 research/web.md에 별도 보존. 병합은 research-lead가 수행. -->

# 웹 리서치 2차 보강 — AX 체계 구축

검색 시점: **2026-09-05 기준**
genre: tech-book / 대상 독자: AX 실무 리더·기획자
1차에서 확보한 항목(Deutsche Bank 'Yi', Entra Agent ID GA, Okta Agent SSO, CSA 78%, Deloitte 21%, EU AI Act Art.49 + Digital Omnibus, OMB M-25-21, MIT NANDA 95%, Gartner 40% 취소, Lattice 3일 철회 등)은 **중복 조사하지 않았다.**

**출처 성격 라벨 범례:**
`[보도자료]` `[벤더 문서]` `[벤더 백서]` `[벤더 블로그]` `[매체 보도]` `[컨설팅 조사]` `[정부·중앙은행]` `[규제 원문]` `[학술]` `[커뮤니티/개인 블로그]`

---

# A. 축 1 검증 리드

## A-1. BNY (BNY Mellon) — "디지털 직원"의 실체

### 결론 요약 (먼저)

> **BNY가 준 것은 `사번(employee ID)`이 아니라 `user ID·로그인·페르소나·이름`이다. 그리고 사람 매니저가 붙는다.**
> 이 구분이 이 책에서 결정적이다. Deutsche Bank의 'Yi'는 **인사 시스템의 사번**을 받았고(1차 확보), BNY는 **IT 시스템의 계정**을 받았다. 둘은 다른 층위다.
> BNY가 디지털 직원을 **HR 시스템(Workday류)에 정식 등록했다는 증거는 찾지 못했다.** → `⚠️ 미확인` (A-1-F 참조)

### A-1-①. 회사 최고경영자의 직접 발언 【가장 강한 근거】

- **주장:** BNY CEO Robin Vince가 디지털 직원을 "user ID·로그인·페르소나·이름으로 감싼 멀티에이전트 솔루션"이라고 정의했다.
- **원문 인용:**
  > "We also have digital employees — multi-agent solutions wrapped with a user ID, a login, a persona, a name"
  > — Robin Vince, BNY CEO
- 출처: https://www.tbpndigest.com/story/2026-03-23/bny-mellon-ceo-robin-vince-on-eliza-their-internal-ai-platform-powering-125-solutions-and-digital-employee-agents
- 발행일: **2026-03-23**
- 출처 성격: `[매체 보도]` (CEO 인터뷰 트랜스크립트 기반 다이제스트)
- 신뢰성: **중~최상** — 발언 자체는 CEO 1인칭이나, 매체가 2차 게재한 것. 원 인터뷰 영상·트랜스크립트 원본은 미확보 `⚠️`
- **책에서의 값어치:** 이 한 문장이 "사번이냐 계정이냐" 논쟁을 정리한다. **`user ID, a login, a persona, a name` — 여기에 `employee number`는 없다.**

### A-1-②. 최초 보도 계보 (2025-07, WSJ 발) 【사람 매니저 부여】

- **주장:** BNY는 2025년 7월 시점에 "수십 개(dozens)"의 AI 디지털 직원을 배치했고, 이들은 **회사 로그인**을 갖고 **사람 라인 매니저에게 보고**한다.
- 근거 인용:
  > "dozens of AI-powered 'digital employees'" — 부서 전반에 배치
  > 디지털 직원은 "equipped with company email accounts and potentially able to collaborate via tools like Microsoft Teams"
  > 이들은 "report to direct managers who review and approve their work"
- **명시된 임원 발언 (BNY CIO Leigh-Ann Russell):**
  > "This is the next level"
  > "I'm sure in six months' time it will become very, very prevalent"
- **초기 2개 페르소나:** (1) 코드 취약점 식별·수정 (2) 지급 지시(payment instruction) 검증 — BNY AI Hub가 개발
- **접근 통제:** 각 인스턴스는 **좁게 정의된 팀에 한정** 배치되어 전사 정보 접근을 갖지 않음
- 출처: https://www.cutoday.info/Fresh-Today/BNY-Mellon-Blurs-The-Line-Between-Staff-And-Software-With-AI-Powered-Employees
- 발행일: **2025-07-10**
- **원 취재 출처: Wall Street Journal** (CU Today가 WSJ 보도를 인용) — WSJ 원문은 유료·403으로 미접근 `⚠️` (E 섹션 로그)
- 출처 성격: `[매체 보도]` (2차 인용)
- 신뢰성: **중** — CIO 실명 발언이 있으나 WSJ 원문 대조 실패

### A-1-③. 규모의 변화 (시계열) 【발표 vs 시행 구분】

| 시점 | 보도된 규모 | 표현 | 출처 | 라벨 |
|---|---|---|---|---|
| 2025-07-10 | "dozens" (수십) | 운영 중 (in production) | CU Today / WSJ | `[매체 보도]` |
| 2025-10-17 | "over 100 digital employees" | 운영 중 | Axios | `[매체 보도]` |
| 2026-02-09 | 디지털 직원 + AI 부트캠프 | 운영 중 | CNBC | `[매체 보도]` |
| 2026-03-23 | "over 130 specialized Digital Employees", "125+ live use cases", "20,000 Empowered Builders" | 운영 중 | TBPN Digest (CEO 인터뷰) | `[매체 보도]` |

- Axios 인용: "This Wall Street bank has over 100 'digital employees'" — 업무 범위는 "payment remediation to engineering and code repair"
  - 출처: https://www.axios.com/2025/10/17/ai-wall-street-digital-workers (발행일 2025-10-17, **본문 403 미접근** — 제목·검색 스니펫만 확보 `⚠️`)

### A-1-④. BNY 공식 웹사이트가 말하는 것 (그리고 말하지 않는 것) 【중요】

- BNY 공식 AI 페이지 원문:
  > "We have over 125 AI-enabled solutions in production"
  > "20,000 employees actively building agents"
  > Eliza는 "enterprise AI platform"으로 "offers BNY employees a marketplace of AI solutions, access to approved datasets and a community for insights into intelligent tools and platforms."
  > "AI governance at BNY is a multidisciplinary activity" — Legal, Privacy, Responsible AI, Data Governance, Information Security, Resiliency, Risk and Compliance 참여
- 출처: https://www.bny.com/corporate/global/en/about-us/technology-innovation/artificial-intelligence.html
- 발행일: 미표기 (2026-09-05 접속 기준 현행)
- 출처 성격: `[벤더 문서]` (회사 공식)
- 신뢰성: **최상**
- **⚠️ 결정적 관찰:** **BNY 공식 페이지는 "digital employees"라는 표현도, 로그인·자격증명·매니저 부여도 언급하지 않는다.** 공식 웹 채널은 "AI-enabled solutions"라는 중립적 표현만 쓴다. "디지털 직원"이라는 프레이밍은 **CEO/CIO의 구두 발언과 기자 서술**에서 나온다.
- **책에서의 값어치:** 이 비대칭 자체가 서술 소재다. 회사의 **공식 문서**와 **경영진의 무대 발언** 사이에 온도차가 있다.

### A-1-⑤. CIO 인터뷰 (The Stack, 2025-08-26 최초 / 2025-12-28 갱신)

- Leigh-Ann Russell(BNY CIO 겸 Global Head of Engineering) 인용:
  > "We have more than 40 AI solutions in full production. They touch almost everything at the bank"
  > "8,000 of those people – bear in mind, we're a 50,000 person bank – are building their own agents"
  > "we have 85% of the bank fully trained"
  > 거버넌스: "massive team sport between legal, our risk function, our cyber teams, our AI hub; we have set up model governance"
- 출처: https://www.thestack.technology/the-big-interview-bny-cio-leigh-ann-russell/
- 발행일: 2025-08-26 (2025-12-28 갱신)
- 출처 성격: `[매체 보도]` (직접 인터뷰)
- 신뢰성: **최상** (1차 인터뷰)
- **주의:** 이 인터뷰에는 **디지털 직원의 식별자·로그인·매니저·라이프사이클에 관한 구체 언급이 없다.** 전략 레벨 발언에 그친다. → A-1-⑥ 공백의 근거

### A-1-⑥. 표 (요구 형식)

| 조직/제품 | 실제로 부여하는 식별자 | 권한 모델 | 감사·폐기 | 실제 시행 여부 | 출처 URL | 발행일 |
|---|---|---|---|---|---|---|
| **BNY / Eliza "Digital Employees"** | **user ID + 로그인 + 페르소나 + 이름** (CEO 발언). 이메일 계정은 2025-07 시점 "예정". **사번(employee number) 확인 안 됨** `⚠️` | 인스턴스별 **좁은 팀 범위 한정**, 전사 접근 없음. 사람 라인 매니저가 산출물 검토·승인 | **공개 자료에 폐기·재심사 절차 없음** `⚠️` | **운영 중 (in production)** — 130+ (2026-03 기준) | tbpndigest.com(2026-03-23) / cutoday.info(2025-07-10, WSJ 인용) / bny.com | 2025-07 ~ 2026-03 |

### A-1-⑦. `⚠️ 미확인` 항목 (BNY)

1. **사번(employee ID) 부여 여부** — 확인된 것은 `user ID / login`뿐. "사번"으로 쓰면 **과장**이다.
2. **매니저 지정이 인사 시스템(HRIS) 상의 실제 보고 라인인가, 운영상의 감독 관계인가** — 보도는 "report to direct managers"라고만 함. Workday/HR 레코드 등재 증거 없음.
3. **회사 보도자료(press release) 원문 부재** — BNY 뉴스룸에서 "digital employee" 명의의 공식 보도자료를 확보하지 못했다. 근거는 전부 **경영진 구두 발언 + 기자 서술**이다.
4. WSJ 원 기사 본문 미접근 (유료·403).
5. "20,000 AI Assistants 배치" 표제의 신디케이트 기사(financialcontent.com / times-online.com, 2026-01-16)는 **출처 불명 나열형**이라 신뢰성 **하**로 판정하고 채택하지 않았다.

> **저술 시 권장 표현:** "BNY는 디지털 직원에게 **사용자 ID와 로그인, 이름과 페르소나**를 부여하고 **사람 매니저**를 붙였다. 다만 이것이 인사 시스템의 사번인지는 공개 자료로 확인되지 않는다."

---

## A-2. Microsoft Entra Agent ID — 라이선스·과금 구조 【신규 확인】

### 핵심 답 (실무의 최대 질문에 대한)

> **"에이전트마다 사람용 라이선스를 사야 하는가?"**
> → **아이덴티티 생성 자체는 아니다. 하지만 실제로 쓰려면 산다.**
> Entra Agent ID(에이전트 신원 생성·관리 플랫폼)는 **모든 Entra 고객에게 제공**된다. 그러나 에이전트가 M365 위에서 실제로 일하게 하려면 **Microsoft Agent 365 라이선스가 per-user 단위로 필요**하다.

### A-2-①. 공식 라이선스 문서 원문

- 원문 인용 (Microsoft 공식 문서, `licensing-agent-id.md`):
  > "Microsoft Entra Agent ID is a product within Microsoft Entra that provides the platform for creating and managing agent identities and agent identity blueprints. **Agent ID is available for all Microsoft Entra customers.**"
- 출처: https://github.com/MicrosoftDocs/entra-docs/blob/main/docs/includes/licensing-agent-id.md
- 출처 성격: `[벤더 문서]` (Microsoft 공식 문서 소스)
- 신뢰성: **최상**
- 검색 시점: 2026-09-05 기준 main 브랜치

### A-2-②. 기능별 라이선스 매트릭스 (2026-09 기준)

| 기능 | 필요 라이선스 |
|---|---|
| 에이전트 신원 생성·관리 (Agent ID 자체) | **모든 Entra 고객** (추가 비용 없음) |
| 에이전트가 M365 서비스·워크플로에서 동작 | **Microsoft Agent 365 라이선스 (per user)** |
| 에이전트에 **Conditional Access** 적용 | Microsoft Entra ID **P1** |
| 에이전트에 **ID Protection**(위험 탐지) 적용 | Microsoft Entra ID **P2** |
| 에이전트에 **ID Governance**(액세스 검토·라이프사이클) 적용 | Entra ID **P1** + Agent 365 |
| 에이전트에 **네트워크 통제** 적용 | Entra Internet Access (Entra Suite 포함 또는 별도) |

- **ID Governance for agents 공식 문구:**
  > "Using Microsoft Entra ID Governance for agent identities requires one of the following license plans:
  > - **Microsoft 365 E7**, which includes Agent 365 and Microsoft Entra Suite, to provide governance of user and agent identities.
  > - **Microsoft Agent 365** license paired with at least **Microsoft Entra P1 or Microsoft 365 E3**."
- 출처: https://learn.microsoft.com/en-us/entra/id-governance/agent-id-governance-overview
- 문서 날짜: **ms.date 2026-06-05, updated 2026-06-24**
- 출처 성격: `[벤더 문서]` — 신뢰성 **최상**

### A-2-③. 가격

- Microsoft Agent 365: **약 $15/user/월** (standalone), **Microsoft 365 E7에 포함**. E5/A5/Business Premium(또는 Defender Suite + Purview Suite)에 **애드온**으로 구매 가능.
- Microsoft Entra Suite: 약 **$12/user/월** (연간 약정, Entra ID P1 애드온 기준)
- 출처: 검색 결과 종합 + https://www.microsoft.com/en-us/security/business/microsoft-entra-pricing
- 출처 성격: `[벤더 문서]`
- 신뢰성: **중** — `$15`, `$12` 수치는 **가격 페이지 원문을 직접 열어 확정하지 못했다** `⚠️` (403/동적 렌더). 인용 시 "약" 표기 필수, 또는 fact-checker 재확인 필요.

### A-2-④. "user account"를 갖는 에이전트가 M365 라이선스를 소비하는가

- Entra Agent ID는 **4종의 신규 객체**를 도입한다 (공식 문서 원문):
  > "four new types of object: **agent identity blueprint, agent identity blueprint principal, agent identity, and agent user**"
  > "Through the agent identity blueprint, the agent can create one or more agent identities, and **optionally an agent user for each agent identity**. Each agent identity and agent user can have distinct access rights."
- **판정:** `agent user` 객체가 별도로 존재한다는 것은 **사람 user 객체와 구분되는 클래스**임을 뜻한다. 다만 **agent user가 M365 시트 라이선스를 소비하는지에 대한 명시 문장은 확보하지 못했다** `⚠️`. 실무적으로는 Agent 365 per-user 라이선스가 그 자리를 대신하는 구조로 읽힌다.
- 출처: 위 governance overview 문서
- 신뢰성: 객체 구조는 **최상**, 시트 소비 여부는 `⚠️ 미확인`

### A-2-⑤ 표

| 조직/제품 | 실제로 부여하는 식별자 | 권한 모델 | 감사·폐기 | 실제 시행 여부 | 출처 URL | 발행일 |
|---|---|---|---|---|---|---|
| **Microsoft Entra Agent ID** | agent identity blueprint / blueprint principal / **agent identity** / **agent user** (4객체) | blueprint 상속 권한 + **access package**(엔타이틀먼트 관리) + Conditional Access + 역할 할당 | **access package 만료일 기반 자동 소멸**, sponsor 알림·연장 승인 사이클, Lifecycle Workflows | **GA** (Agent ID GA 2026-05-01, 1차 확보) / governance 문서 2026-06 갱신 | learn.microsoft.com/entra/id-governance/agent-id-governance-overview | 2026-06-05 (갱신 2026-06-24) |

---

## A-3. Workday — Agent System of Record 【Lattice와의 대비 핵심】

### A-3-①. 발표 (2025-02-11) — 발표 시점의 프레이밍

- **주장:** Workday는 2025-02-11 "Agent System of Record"를 발표하며, Workday·서드파티 에이전트 전체를 한 곳에서 관리한다고 했다.
- 원문 인용 (Workday 뉴스룸):
  > 조직이 "manage their entire fleet of AI agents – from Workday and third-parties alike – in one place"
  - 핵심 기능: **중앙 가시성**, **역할·스킬·보안 데이터 접근이 정의된 온보딩(streamlined agent onboarding with defined roles and skills)**, **예산·예측·ROI 추적**, **자동 구성 및 접근 통제 기반 컴플라이언스 배포**, **에이전트 활동·정책·비용 실시간 모니터링**
  - 리더십 발언: "humans and agents should peacefully coexist"
  - 신규 **역할 기반(role-based) 에이전트** 4종: Contracts Agent / Payroll Agent / Financial Auditing Agent / Policy Agent — 태스크 기반과 달리 **구성 가능한 "skills"**를 가져 더 높은 자율성을 지님
- 출처: https://newsroom.workday.com/2025-02-11-The-Next-Generation-of-Workforce-Management-is-Here-Workday-Unveils-New-Agent-System-of-Record
- 발행일: **2025-02-11**
- 출처 성격: `[보도자료]`
- 신뢰성: **최상** (회사 공식)
- **당시 가용성: "later in 2025 예정" — 즉 발표 시점엔 개발 중이었다.**

### A-3-②. GA (2026-02) — 시행

- **주장:** Agent System of Record는 **2026년 2월 GA**되었다.
- 근거: Workday 공식 블로그 제목 "**The Workday Agent System of Record Is Now Generally Available**"
  > "The Workday Agent System of Record (ASOR) is now generally available, giving customers visibility and control over all of their AI agents."
  - 해결 대상 문제를 Workday는 **"agent sprawl"**이라 명명
  - **Agent Registry 대시보드**: 에이전트 목록, 설명, **어느 보안 그룹이 접근 권한을 갖는지**, **국가별 가용 지역**, **현재 상태(status)**
- 출처: https://blog.workday.com/en-us/managing-ai-powered-future-of-work.html
- 발행일: **2026-02 (정확한 일자 미표기)** `⚠️` — 블로그 본문에 GA 날짜가 명기되지 않았다. "2026년 2월 GA"는 검색 스니펫·LinkedIn 게시(activity-7429600853726085121) 기준. **일자 단위 인용은 피할 것.**
- 출처 성격: `[벤더 블로그]`
- 신뢰성: **최상**(GA 사실) / **중**(정확 일자)

### A-3-③. 【핵심】 Workday의 프레이밍 — Lattice와 무엇이 달랐는가

- **결정적 원문 인용 (Workday 블로그):**
  > "agents become part of an organization's workforce strategy — **measured like investments, governed like employees, and improved by training and learning**."
- Workday는 에이전트를 **"employees"가 아니라 "digital labor" / "digital workforce" / "digital capabilities"** 로 부른다. 보도자료는 "employees, contingent workers, **and agents**"를 나란히 관리한다고 쓰되, **에이전트가 직원과 동등한 법적 지위를 갖는다고는 말하지 않는다.**
- **대비 정리 (책의 장면용):**

| | **Lattice (2024, 3일 만에 철회 — 1차 확보)** | **Workday ASoR (2025 발표 → 2026 GA)** |
|---|---|---|
| 배치 위치 | **HR 시스템 안, 사람 직원과 같은 레코드로** | **별도의 Agent Registry** (HCM·재무와 *연동*하되 분리) |
| 용어 | "AI **employees**" — 직원이라고 불렀다 | "**agents**", "digital labor", "digital workforce" |
| 프레이밍 | 사람과 **동렬** | "measured like **investments**, governed **like** employees" — **"like"가 들어간다** |
| 관리 축 | 인사 평가 축에 편입 시도 | **비용·ROI·접근권한·상태** 축 |
| 결과 | 3일 만에 철회 | GA, 제품으로 존속 |

- **해석(저자 판단용 재료):** Workday가 다르게 한 것은 **위치와 조사(助詞)**다. 에이전트를 직원 *으로* 만들지 않고, 직원*처럼* 통치했다. 레지스트리를 인사 레코드와 **분리**하되 같은 플랫폼에서 **나란히 보이게** 했다.
- 신뢰성: **최상** (양쪽 다 회사 공식 문구)

### A-3-④ 표

| 조직/제품 | 실제로 부여하는 식별자 | 권한 모델 | 감사·폐기 | 실제 시행 여부 | 출처 URL | 발행일 |
|---|---|---|---|---|---|---|
| **Workday Agent System of Record** | Agent Registry 상의 **에이전트 레코드**(이름·설명·소유/보안그룹·국가·상태). **사번 아님** | **보안 그룹 기반 접근**, 역할·스킬 정의 온보딩, 자동 구성 | 활동·정책·**비용** 실시간 모니터링, 상태(status) 필드. **명시적 폐기 워크플로는 공개 문서에 미기술** `⚠️` | **GA (2026-02)**, 발표는 2025-02-11 | blog.workday.com/en-us/managing-ai-powered-future-of-work.html / newsroom.workday.com | 2025-02-11 / 2026-02 |

---

## A-4. 기타 주요 벤더 훑기

> 판정 기준: **"에이전트에 신원을 부여하고 관리하는 기능이 실제로 있는가"** + GA/프리뷰/발표 라벨.

| 조직/제품 | 실제로 부여하는 식별자 | 권한 모델 | 감사·폐기 | 실제 시행 여부 | 출처 URL | 발행일 |
|---|---|---|---|---|---|---|
| **ServiceNow AI Control Tower** | **AI Asset Inventory** 레지스트리 레코드 — systems / models / prompts / datasets / **MCP servers**, 각각 provider·vendor·**lifecycle phase**·state·**risk classification** | CMDB·CSDM 관계로 비즈니스 서비스·인프라에 연결 | **lifecycle phase / state 필드 보유** — 폐기 단계가 데이터 모델에 존재. 서드파티 에이전트도 자동 탐지 | **GA** (Innovation Lab 2025-01 → GA 2025-05 계획). **2026-06 릴리스**부터 관리 에이전트를 **Microsoft Agent 365 디렉터리로 직접 게시** 가능 | servicenow.com/community (2026-06 릴리스 노트) | 2026-06 |
| **AWS Bedrock AgentCore Identity** | **에이전트/워크로드별 고유 identity + 메타데이터**, 중앙 **agent identity directory**("Cognito User Pools와 유사한 거버넌스 단위") | 사용자 대행(on-behalf-of) 인증·인가, 서드파티 서비스 자격증명 관리, **감사 추적(audit trails)** | 자격증명 관리·감사 추적 명시. **폐기 절차는 문서에서 미확인** `⚠️` | **GA** — Bedrock AgentCore GA **2025-10** | docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html / aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available | 2025-10 |
| **Salesforce Agentforce** | 에이전트 정의 + **Agentic Maturity / Levels of Determinism** 프레임 (A-5 참조) | Assistive(부분 자율) vs Autonomous(가드레일 하 독립 + 사람 핸드오프) 구분, 6단계 agentic control | 미확인 `⚠️` | **GA** (Agentforce 제품 자체) | salesforce.com/agentforce/levels-of-determinism/ | 2026 접속 기준 |
| **Google (Agentspace → Gemini Enterprise)** | **⚠️ 미확인** — Agentspace는 **2026 Cloud Next에서 Vertex AI Agent Builder와 통합되어 "Gemini Enterprise"로 리브랜딩**. 에이전트 신원 부여 기능은 별도 확인 실패 | 미확인 | 미확인 | 제품 통합·리브랜딩 확인, **신원 기능 미확인** | (검색 결과 요약 기반, 1차 문서 미접근) | 2026 |
| **SAP (Joule agents)** | **⚠️ 미확인** — 검색으로 거버넌스·신원 부여 근거 확보 실패 | — | — | **미확인** | — | — |
| **Atlassian / Slack** | **⚠️ 미확인** — 이번 라운드에서 개별 조사 예산 미배정 | — | — | **미조사** | — | — |

- 출처 성격: ServiceNow `[벤더 문서/커뮤니티]`, AWS `[벤더 문서]`, Salesforce `[벤더 문서]`
- **주목할 상호운용 사실 (책 소재):** ServiceNow가 **자기 레지스트리의 에이전트를 Microsoft Agent 365 디렉터리로 게시**하고 "single source of truth for governance is maintained across both registries"를 표방한다. → **에이전트 레지스트리 간 연합(federation)이 이미 시작됐다.** (2026-06 릴리스)

---

## A-5. 【필수】 자율성 등급 프레임 — **4종 확보 (수락 기준 2종 초과 달성)**

### 종합 비교표

| # | 프레임 | 출처 유형 | 등급 수 | 등급 이름 | **통제 차등 존재?** | 출처 URL | 발행일 |
|---|---|---|---|---|---|---|---|
| 1 | **Gartner 비례적 거버넌스(proportional governance)** | `[컨설팅 조사]` | **4** | Observe / Advise / Act with Approval / Act Autonomously | **✅ 있음 — 가장 명확** | gartner.com 보도자료 (403, 2차 인용) | **2026-05-26** |
| 2 | **CSA(Cloud Security Alliance) Autonomy Levels** | `[표준·기관]` | **6 (L0~L5)** | No Autonomy / Assisted / Supervised / Conditional / High Autonomy / Full Autonomy | **✅ 있음** | cloudsecurityalliance.org/blog/2026/01/28/levels-of-autonomy | **2026-01-28** |
| 3 | **Feng·McDonald·Zhang, "Levels of Autonomy for AI Agents"** | `[학술]` | **5 (L1~L5)** | User as Operator / Collaborator / Consultant / Approver / Observer | **✅ 있음 + 인증제(autonomy certificates) 제안** | knightcolumbia.org/content/levels-of-autonomy-for-ai-agents-1 / arxiv.org/abs/2506.12469 | **2025-07-28** (arXiv 2025-06) |
| 4 | **Salesforce Agentic Maturity Model** | `[벤더 문서]` | **5 (L0~L4)** | Fixed Rules / Information Retrieval / Simple Orchestration Single Domain / Complex Orchestration Multi Domain / Multi-Agent Orchestration | **△ 부분적 — 성숙도 축이 주. 통제는 L2부터 언급, L3에서 세분화 접근통제·계층적 감독 도입** | salesforce.com/news/stories/agentic-maturity-model/ | **2025-04-10** |

---

### A-5-①. Gartner — 비례적 거버넌스 【실무 리더에게 가장 직접적】

- **핵심 주장:** 자율성 수준과 무관하게 **획일적 거버넌스**를 적용하면 엔터프라이즈 AI 에이전트는 실패한다.
- **분석가:** **Shiva Varma, Senior Director Analyst, Gartner**
- **원문 인용:**
  > "Enterprises are treating AI agent governance as **binary, either locked down or fully trusted**, and that is the root cause of failure."
- **두 가지 실패 모드:**
  - **과잉 제한(over-restriction)** of simple agents → 딜리버리 지연 + **섀도 개발(shadow development)** 유발
  - **과소 제한(under-restriction)** of more autonomous agents → 운영·보안·컴플라이언스 리스크 증가
- **4단계와 통제 차등 (이 표가 이 책 축 1의 뼈대가 될 수 있다):**

| 레벨 | 이름 | 할 수 있는 일 | **차등 통제** |
|---|---|---|---|
| **L1** | **Observe** | 정의된 데이터 소스에 **읽기 전용** 접근. 출력은 요청한 사용자에게만 표시. 문서 요약·지식 검색·코드 설명 | **경량 통제** — 범위 지정된 데이터 접근, 사용자 인증, **사용 로깅**, 기본 기능·보안 테스트 |
| **L2** | **Advise** | 추천·초안·제안 행동 **생성**. 사람이 검토 후 수동 실행. 쓰기 권한 없음. 이메일 초안·리포트 생성·의사결정 지원 | L1 + **정확도/할루시네이션 테스트**, 도메인별 품질 평가, **적정 의존에 대한 사용자 교육** |
| **L3** | **Act with Approval** | 데이터 쓰기·통신 발송·구성 변경 실행. 단 **매 행동마다 명시적 사람 승인** | **강한 보안 테스트**, **감사 추적을 갖춘 명확한 승인 워크플로**, **에이전트 전용 인시던트 대응 절차** |
| **L4** | **Act Autonomously** | 정의된 가드레일 안에서 **독립 실행**. 사람은 개별 결정이 아니라 **예외·감사 로그·집계 결과**를 검토 | **지속 모니터링**, 강제 가드레일, **신속 롤백**, **서킷 브레이커**, 에이전트 행동에 대한 **명확한 소유권** |

- **예측 (수치):**
  > "by **2027, 40% of enterprises will demote or decommission autonomous AI agents** due to governance gaps identified only after production incidents occur."
  - `[컨설팅 조사]` — **주의:** 1차에서 확보한 "Gartner 40% 취소(2027년까지 agentic AI 프로젝트의 40%+ 취소, 2025-06-25 보도자료)"와 **다른 예측**이다. 이건 **"강등 또는 폐기(demote or decommission)"**다. **혼동 금지.**
- 출처: https://www.gartner.com/en/newsroom/press-releases/2026-05-26-gartner-says-applying-uniform-governance-across-ai-agents-will-lead-to-enterprise-ai-agent-failure
- 발행일: **2026-05-26**
- **접근 상태: Gartner 원문 403** → 2차 인용 https://techedgeai.com/gartner-says-applying-uniform-governance-across-ai-agents-will-lead-to-enterprise-ai-agent-failure/ 및 securitypointbreak.com, enterprisedna.co 교차 확인 (3개 매체가 동일 등급명·동일 인용문 보도)
- 신뢰성: **중~최상** — 원문 미접근이나 **3개 독립 매체 교차 일치**. 인용 시 "Gartner 보도자료(2026-05-26)" 표기 + fact-checker 재대조 권장 `⚠️`

### A-5-②. CSA — Autonomy Levels for Agentic AI (6단계)

- **저자:** **Jim Reavis, Co-founder and CEO, Cloud Security Alliance**
- **발행일: 2026-01-28**
- 출처: https://cloudsecurityalliance.org/blog/2026/01/28/levels-of-autonomy
- 출처 성격: `[표준·기관]` — 신뢰성 **최상**
- **6단계 + 통제 차등:**

| 레벨 | 이름 | 원문 정의 | **차등 통제** |
|---|---|---|---|
| **L0** | No Autonomy (Human Execution) | "The AI system provides information, analysis, or recommendations, but **humans perform all actions**." | 최소 리스크. **출력 품질·정보 유출 방지**에 집중 |
| **L1** | Assisted (Human Decision + AI Execution) | "The AI can execute actions, but **each action requires explicit human approval** before execution." | 의도와 행동 사이 **명확한 승인 게이트** = 책임성·오류 포착 체크포인트 |
| **L2** | Supervised (Human Approval + Batch Execution) | "Humans review and approve **a plan or batch of actions**, and the AI then executes autonomously within that approved scope." | 건별 승인 → **상위 레벨 인가**로 대체. **모니터링 + 롤백 메커니즘 필수** |
| **L3** | Conditional (AI Decision within Boundaries) | "The AI makes decisions and takes actions autonomously **within defined boundaries**, escalating to humans only when it exceeds those boundaries." | **기계가 읽을 수 있는 경계 정의 + 기술적 강제**(정책 문서만으로는 불가), 경계 위반 시 **에스컬레이션 워크플로** |
| **L4** | High Autonomy (Minimal Supervision) | "The AI operates autonomously across a broad scope, with human involvement **shifting from decision approval to monitoring and exception handling**." | **지속 모니터링, 이상 탐지, 킬 스위치, 경영진 수준의 리스크 수용(executive-level risk acceptance)** |
| **L5** | Full Autonomy (Self-Directed) | "Full autonomy, including the ability to **set goals and potentially modify its own behavior**." | 저자 직접 발언: **"I don't believe Level 5 is appropriate for enterprise deployment today."** |

- **책에서의 값어치:** L3의 "**기계가 읽을 수 있는 경계 정의 + 기술적 강제 — 정책만으로는 안 된다**"는 문장이 이 책의 "체계는 문서가 아니라 시스템"이라는 논지에 직결된다.

### A-5-③. Feng·McDonald·Zhang (학술) — 5단계 + **자율성 인증서**

- **저자:** K. J. Kevin Feng, David W. McDonald, Amy X. Zhang (University of Washington)
- **발행:** arXiv 2506.12469 (2025-06) / Knight First Amendment Institute 게재 **2025-07-28**
- 출처: https://knightcolumbia.org/content/levels-of-autonomy-for-ai-agents-1
- 출처 성격: `[학술]` — 신뢰성 **최상**
- **정의 축이 독특하다: "사용자가 맡는 역할"로 등급을 나눈다.**

| 레벨 | 이름 | 사람의 역할 | 감독 | **통제 메커니즘** |
|---|---|---|---|---|
| **L1** | User as **Operator** | 주 의사결정자, 장기 계획 전담 | 완전 — 모든 실질 행동 승인 | 사용자가 명시적으로 에이전트를 호출 |
| **L2** | User as **Collaborator** | 태스크 위임하는 능동 파트너 | 높음 — 계획 공동 수립, 산출물 직접 수정 | **언제든 인계(take over) 가능**, 태스크 공동 소유 |
| **L3** | User as **Consultant** | 입력 제공하는 전문 자문 | 중간 — **직접 통제는 불가**, 코멘트·변경 요청만 | 메시지를 통한 간접 영향, 일시정지·수정 요청 |
| **L4** | User as **Approver** | 예외 상황의 수동적 검토자 | 낮음 — **선택적** 승인 | 자격증명 제공 또는 사전 선택된 옵션 확인. 에이전트는 **블로커(실패·자격증명 부재·중대 결정)** 만날 때만 사람 호출 |
| **L5** | User as **Observer** | 수동 모니터링만 | 최소 — **비상 정지만** | **비상 off-switch**, 감사용 활동 로그 |

- **자율성 인증서(autonomy certificates) — 이 프레임의 진짜 기여:**
  > 인증서는 "**prescribe[s] the maximum level of autonomy at which an agent can operate**" — 특정 기술 사양과 운영 환경을 전제로 한 **자율성 상한**을 규정한다.
  - 발급 절차: 개발자가 에이전트 + **"autonomy case"**(해당 등급 **이하**로 동작함을 입증하는 증거 기반 논증)를 제출 → **제3자 거버닝 바디**(정부기관·비영리·기업)가 평가·발급
  - **갱신 요건:** 기술 사양이나 **운영 환경이 바뀌면 갱신 필요** — 변경이 상호작용 행태를 바꿀 수 있기 때문
- **책에서의 값어치:** "등록 → 등급 부여 → **상한 규정** → 환경 변경 시 **재심사**"라는 완결 루프. 저자의 등록 스키마 + 재심사 논지와 정확히 맞물린다. 그리고 **A-6(폐기·재심사 반례)의 학술 쪽 반례**이기도 하다.

### A-5-④. Salesforce Agentic Maturity Model (참고 — 통제 차등 약함)

- **저자:** Shibani Ahuja, SVP of Enterprise IT Strategy, Salesforce / **발행일 2025-04-10**
- 출처: https://www.salesforce.com/news/stories/agentic-maturity-model/
- 출처 성격: `[벤더 문서]` — 신뢰성 **중~최상**
- L0 Fixed Rules → L1 Information Retrieval → L2 Simple Orchestration(단일 도메인) → L3 Complex Orchestration(다중 도메인) → L4 Multi-Agent Orchestration("any-to-any-agent operability across disparate stacks with agent supervision")
- **통제 차등 판정: △ 부분적.** 이건 **자율성 등급이라기보다 성숙도 로드맵**이다. 다만:
  - **L2**부터 "거버넌스 프레임워크가 테스팅·성과 지표를 수립하기 시작"
  - **L3**에서 "**세분화된 접근 통제(fine-grained access controls)와 계층적 사람/AI 감독**", "AI Agent Lifecycle Management 방법론 수립"
  - **L4**에서 "생태계 전반 보안·거버넌스", ROI를 비즈니스 임팩트로 측정
- ⚠️ **등급이 올라갈수록 통제가 "달라진다"기보다 "많아진다"는 서술.** Gartner/CSA처럼 **레벨별 필수 통제 목록**을 제시하진 않는다. 책에서 쓸 때 이 차이를 명시할 것.
- 별개로 Salesforce는 **"Levels of Determinism"**(6단계 agentic control)이라는 다른 축의 프레임도 운영한다: https://www.salesforce.com/agentforce/levels-of-determinism/ — 상세 미조사 `⚠️`

### A-5-⑤. 유사 계보 — SAE J3016 자율주행 등급 적용 문서

- 검색 결과 **CSA·Feng 등 다수 프레임이 L0~L5 넘버링을 SAE 자율주행 등급에서 차용**한 것이 명백하나, "SAE J3016을 에이전트에 명시적으로 매핑한 단일 권위 문서"는 **이번 라운드에서 확정하지 못했다** `⚠️ 미확인`.
- 참고로 확인된 다른 등급 프레임(신뢰성 **하~중**, 보조 자료로만):
  - Cisco Outshift, "5 Levels of agentic AI intelligence for enterprise use" — https://outshift.cisco.com/blog/ai-ml/agentic-ai-intelligence-for-enterprise-use `[벤더 블로그]`
  - Vellum, "LLM Agents: The Six Levels of Agentic Behavior" — https://www.vellum.ai/blog/levels-of-agentic-behavior `[벤더 블로그]`
  - Deloitte "intelligence maturity curve": assisted intelligence → artificial intelligence → **autonomous intelligence**("AI decides and executes **in defined boundaries**") — https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html `[컨설팅 조사]`, 3단계, **통제 차등 없음**

### A-5-⑥. ⚠️ 오귀속 주의 (fact-checker 필독)

검색 과정에서 "**L0 Observe / L1 Draft / L2 Prepare / L3 Bounded execute / L4 High-autonomy execute**"라는 5단계 프레임이 등장했으나, **이것을 Gartner로 귀속시킨 근거를 찾지 못했다.** 검색엔진 요약이 "an emerging enterprise framework"라고만 표기했다. **Gartner의 4단계(Observe/Advise/Act with Approval/Act Autonomously)와 혼동하지 말 것.** 출처 미상이므로 **책에 쓰지 말 것.** `⚠️ 미확인 — 사용 금지`

---

## A-6. 폐기·재심사(offboarding/recertification) 절차의 **반례 찾기**

### 결론 먼저

> **저자의 주장 "다들 들이는 건 설계하는데 내보내는 건 아무도 설계 안 한다"는 — 2026-09 시점에서 부분적으로 낡았다.**
> **벤더 문서 층위에서는 폐기·재심사 절차가 이미 상세히 규정돼 있다.** Microsoft Entra는 자동 만료·후원자 자동 승계까지 문서화했다.
> **다만 "조직이 실제로 그렇게 운영한다"는 증거는 여전히 못 찾았다.** 1차의 CSA 78%(폐기 정책 없음)와 모순되지 않는다.
> → **논지를 이렇게 조정하는 것이 사실에 부합한다: "도구는 이미 폐기를 설계했다. 조직이 아직 안 켰다."**

### A-6-①. 【최강 반례】 Microsoft Entra ID Governance — 에이전트 신원 라이프사이클

- 출처: https://learn.microsoft.com/en-us/entra/id-governance/agent-id-governance-overview
- 문서 날짜: **ms.date 2026-06-05 / updated 2026-06-24** · `[벤더 문서]` · 신뢰성 **최상**
- **원문 인용 (목적 진술):**
  > "you can govern and manage the identity and access lifecycle of agents, ensuring the agents have a **responsible person providing oversight throughout the agent lifecycle** and **agent's access does not persist longer than it is needed**."
- **문서화된 폐기·재심사 메커니즘:**
  1. **Sponsor(후원자) 제도** — "Sponsors of agent identities are **human users accountable for making decisions about its lifecycle and access**."
  2. **접근 자동 만료:** access package 할당에 만료일이 있고, 만료가 다가오면 **sponsor에게 알림**. sponsor는 (a) 연장 요청 → **새 승인 사이클 트리거**, 승인자가 계속 접근이 적절한지 재확인, (b) 무대응 → **"the access package assignment automatically expires on its end date, and the agent identity loses access to the target resources."**
  3. **후원자 이탈 시 자동 승계 【이게 백미】:**
     > "**If the sponsor is leaving the organization, sponsorship of the agent identities is automatically transferred to their manager.** With sponsorship transferred, **there's always a human user accountable** for managing the access and lifecycle of the agent identities."
     - Lifecycle Workflows가 **공동 후원자·후원자의 매니저에게 임박한 후원권 변경을 통지**하는 태스크들을 포함
  4. **활성화/비활성화:** My Account 포털에서 Sponsor·Owner가 **에이전트를 enable/disable** 가능, 접근·활동·라이프사이클 정보 조회
  5. **Conditional Access + ID Protection**: 에이전트 신원 위험(agent identity risk)을 평가해 접근 전 차단. blueprint 레벨에 적용하면 그 blueprint에서 생성된 모든 에이전트가 상속
- **책에서의 값어치:** **"사람이 퇴사하면 그가 후원하던 에이전트의 책임이 그의 매니저에게 자동으로 넘어간다."** — 고아 계정(orphaned identity) 문제에 대한 구체적 제도 설계. 저자의 등록 스키마에 **"책임자 + 책임자 승계 규칙"** 항목이 있어야 한다는 근거.

### A-6-②. 벤더 라이프사이클 프레임 — Saviynt 6단계

- **저자:** Vibhuti Sinha, Chief Product Officer, Saviynt / **발행일 2026-02-26**
- 출처: https://saviynt.com/blog/ai-agent-lifecycle-management
- 출처 성격: `[벤더 블로그]` · 신뢰성 **중** (벤더 마케팅 성격, 단 절차 기술은 구체적)
- **6단계:** Registration → Ownership Management → Entitlement Assignment → Lifecycle Governance → **Retirement** → IGA 통합
- **Retirement 단계가 요구하는 것 (책의 "폐기 체크리스트"에 그대로 쓸 수 있다):**
  1. 승인을 포함한 **공식 폐기 워크플로**
  2. **즉시 자격증명·토큰 폐기** (API 키, 인증서, OAuth 토큰)
  3. **아웃바운드 접근 체계적 제거** (모든 연동, 도구 권한)
  4. **인바운드 호출 차단** (API 엔드포인트, 웹훅, 큐)
  5. **메모리·데이터 정화** (보관 / 익명화 / 안전 삭제)
  6. **감사 추적 보존** (불변 로깅)
  7. **폐기 후 잔여 리스크 모니터링**
- **Lifecycle Governance 단계의 재심사 규정:** "**event-driven, continuous re-certification (not quarterly)**" — 분기 재인증이 아니라 **이벤트 기반 연속 재인증**. 엔타이틀먼트 크립 탐지 행동 분석, 접근 패턴 드리프트 자동 알림, **에이전트가 새 역량을 얻으면 소유자 재확인(re-attestation)**
- **인용된 통계 (⚠️ 2차 인용 주의):**
  - Gartner: "40% of enterprise applications will integrate task-specific AI agents in 2026, up from under 5% in 2025" `[컨설팅 조사]` — 원문 미대조 `⚠️`
  - "Orphaned accounts in traditional IAM are implicated in **20% of insider-related breaches**" — 출처 인포그래픽, **원자료 미확인** `⚠️`
- **사례 언급:** 미국 병원 시스템이 AI 코파일럿 라이프사이클 거버넌스(등록 + 범위 제한 + **분기 재인증**)를 도입해 HIPAA 컴플라이언스 충족 — **익명 사례, 검증 불가** `⚠️`

### A-6-③. 자율성 인증서의 갱신 요건 (학술 반례)

- A-5-③ 참조. Feng 등의 **autonomy certificate는 "기술 사양 또는 운영 환경이 바뀌면 갱신 필요"**를 명시한다. 이것도 재심사 설계의 반례다.
- `[학술]` · 신뢰성 **최상**

### A-6-④. NHI 접근 재인증(access recertification) 관행

- **정의:** "Access recertification is the **periodic revalidation of permissions, roles, and account entitlements** to confirm that access still has a business purpose." NHI 프로그램에서는 service accounts, API keys, workload identities, 위임 자동화에 적용된다.
- **관행:** 분기 또는 반기 리뷰에서 **NHI 소유자가 해당 신원이 여전히 유효한 목적을 갖는지 확인(affirm)** → 드리프트 포착·방치 식별
- **리스크 티어별 주기 차등:** admin 역할은 더 자주, 저위험 읽기 전용은 덜 자주
- **자동 조치:** "리뷰를 통과 못 한 NHI는 **자동 비활성화**(이의신청 유예기간 부여)"
- 출처: https://nhimg.org/glossary/access-recertification/ , https://entro.security/blog/nhi-campaigns-the-access-reviews-your-non-human-identities-have-been-missing/
- 출처 성격: `[벤더 블로그]` / 업계 용어집 · 신뢰성 **중~하** — 벤더 마케팅 콘텐츠. **구체 조직의 시행 사례 아님**

### A-6-⑤. 폐기 정의 (업계 용어)

- "**Agent decommissioning** is the controlled retirement of an AI agent after its business role ends, with **explicit removal of every credential, token, certificate, endpoint binding, callback route, and delegated permission it ever used.**"
- "A decommissioned agent has had its **new work frozen and queues drained**, its traffic redirected, its credentials revoked, its identity **tombstoned in a governance record**, its records retained per policy, and the whole sequence verified."
- 출처: https://nhimg.org/glossary/agent-decommissioning/ , https://www.truefoundry.com/blog/ai-agent-decommissioning-lifecycle-playbook
- 출처 성격: `[벤더 블로그]`/용어집 · 신뢰성 **중**
- **"tombstoned in a governance record"** — 삭제가 아니라 **묘비(tombstone) 처리**. 좋은 어휘다.
- **⚠️ 통계 주의:** "Only **20% of organisations** have formal processes for offboarding and revoking API keys"라는 수치가 검색 결과에 등장했으나 **원자료(조사 주체·표본·연도) 확인 실패**. → `⚠️ 미확인, 인용 금지`

### A-6-⑥. 【그래서 "없더라"인 부분】 — 뒤진 곳 목록

**공개된 "실제 조직의" 에이전트/NHI 폐기 절차 문서는 여전히 못 찾았다.** 다음을 뒤졌다:

| 뒤진 곳 | 결과 |
|---|---|
| 검색어 `AI agent decommissioning policy` | 벤더 블로그·용어집만. 조직 정책 원문 0건 |
| 검색어 `agent offboarding procedure` | 동일 |
| 검색어 `non-human identity lifecycle policy` | 동일 |
| 검색어 `service account recertification` | 벤더/컨설팅 베스트프랙티스만 |
| 검색어 `agent retirement governance` | 동일 |
| 기업 엔지니어링 블로그 (Netflix·Cloudflare·우아한형제들·카카오·토스·네이버 D2·LINE) | **에이전트 폐기 절차 공개 사례 0건** |
| 공공기관 정책 | OMB M-25-21(1차 확보) 외 **에이전트 단위 폐기 규정 미발견**. 단 연방 인벤토리 스키마에 `development_stage`의 값으로 **"Retired"**가 존재 (A-7-② 참조) — **간접 반례** |
| 표준 문서 | ISO/IEC 42001 원문 유료로 미접근 `⚠️` |

- **발견 자체가 결론:** **벤더는 폐기를 설계했고, 조직은 폐기를 공개하지 않는다.** (혹은 안 한다.) 1차의 CSA 78%와 정합적이다.

### A-6-⑦ 표

| 조직/제품 | 실제로 부여하는 식별자 | 권한 모델 | **감사·폐기** | 실제 시행 여부 | 출처 URL | 발행일 |
|---|---|---|---|---|---|---|
| **Microsoft Entra ID Governance (agent identities)** | agent identity / agent user + **Sponsor(사람)** | access package, Conditional Access, blueprint 상속 | **만료일 자동 소멸 + 연장 시 재승인 사이클 + 후원자 퇴사 시 매니저 자동 승계 + enable/disable** | **GA (문서 2026-06 기준)** | learn.microsoft.com/entra/id-governance/agent-id-governance-overview | 2026-06-05 |
| **Saviynt (프레임 제안)** | 암호학적 고유 식별자 + 생성 증명(attestation) + 책임 소유자 | RBAC 템플릿 + ABAC + 단명 자격증명 + JIT | **7단계 Retirement 체크리스트 + 이벤트 기반 연속 재인증** | **벤더 제안 프레임 (조직 시행 사례 아님)** | saviynt.com/blog/ai-agent-lifecycle-management | 2026-02-26 |
| **미 연방 AI 인벤토리** | use case `id` = `[Agency Abbrev.]–[#]` | — | `development_stage` 값에 **"Retired"** 존재 | **시행 중** (2025년분 2026-01-28 공개) | github.com/ombegov/2025-Federal-Agency-AI-Use-Case-Inventory | 2026-04-13 (repo 상태) |

---

## A-7. 등록 스키마 — 무엇을 기록하게 하는가

> **저자의 8항목 스키마와 대조할 공개 목록 3종 확보.**

### A-7-①. EU AI Act **Annex VIII** — 전체 항목 (규제 원문)

- 출처: https://artificialintelligenceact.eu/annex/8/ · `[규제 원문]` · 신뢰성 **최상**
- 근거 조문: Article 49 (등록). **적용 시점은 1차 확보 정보 참조 (Digital Omnibus로 Annex III 고위험 2027-12-02 연기)**

**Section A — 제공자(provider)가 제출, Art.49(1) [13항목]**
1. 제공자의 **이름·주소·연락처**
2. (해당 시) **대리 제출자**의 이름·주소·연락처
3. (해당 시) **공인 대리인(authorised representative)**의 이름·주소·연락처
4. AI 시스템 **상품명 및 식별 참조번호**
5. **의도된 목적(intended purpose)·맥락·사용 조건**에 대한 기술
6. 시스템 **입력값 및 작동 로직(operating logic)**에 대한 기본 기술
7. **시스템 상태** — 시장 출시됨 / 서비스 중 / 더 이상 제공 안 됨 / **리콜됨**
8. **인증서 유형·번호·만료일** 및 인증기관(notified body) 식별정보
9. (해당 시) 인증서 **스캔본**
10. 시스템이 출시·서비스 개시된 **회원국 목록**
11. **EU 적합성 선언서(declaration of conformity) 사본**
12. **전자 사용설명서** (법 집행·이주·망명·국경관리 시스템은 예외)
13. 추가 정보 **URL** (선택)

**Section B — 제공자 제출, Art.49(2) [고위험 아님으로 분류한 경우]**
1. 제공자 이름·주소·연락처 / 2. 대리 제출자 / 3. 공인 대리인
4. AI 시스템 상품명·식별 참조번호
5. 의도된 목적·맥락·사용 조건 기술
6. **Article 6(3)에 근거해 고위험이 아니라고 판단한 조건(들)**
7. *(개정으로 삭제)*
8. **시스템 상태** (시장/서비스/중단/리콜)
9. *(개정으로 삭제)*

**Section C — 배포자(deployer) 제출, Art.49(3) [5항목]**
1. 배포자의 **이름·주소·연락처**
2. (해당 시) 대리 제출자의 이름·주소·연락처
3. 제공자가 등록한 **EU 데이터베이스 항목의 URL**
4. **기본권 영향평가(fundamental rights impact assessment) 결과 요약**
5. (해당 시) **개인정보 영향평가(DPIA) 요약**

- **책에서의 값어치:** **Section A-7 "시스템 상태"에 `no longer available`과 `recalled`가 있다.** 규제가 이미 **폐기 상태를 스키마에 넣어놨다.** A-6의 반례로도 쓸 수 있다. 그리고 **Section C(배포자)가 별도로 존재**한다는 것 — 만든 자와 쓰는 자의 등록 의무가 분리돼 있다.

### A-7-②. 미 연방기관 AI use case inventory — **36개 필드 전체** (정부 원자료)

- 출처: https://github.com/ombegov/2025-Federal-Agency-AI-Use-Case-Inventory (데이터 딕셔너리: `/Validation/data_dictionary.md`)
- 출처 성격: `[정부 통계]` / 원자료 · 신뢰성 **최상**
- 리포지토리 상태 기준일: **2026-04-13** / 기관 제출 마감 **2025-12-22** / 공개 마감 **2026-01-28**
- **규모:** 기관 제출 **56건**, 개별 보고 유스케이스 **3,611건**, **고영향(high-impact) 445건**, 배포/파일럿 **1,818건**

| # | 필드명 | 설명 |
|---|---|---|
| 1 | `agency` | 보고 기관 약칭 (예: USDA) |
| 2 | `agency_name` | 기관 정식 명칭 |
| 3 | `id` | **고유 식별자** — `[Agency Abbrev.]–[#]` 형식 |
| 4 | `use_case_name` | 유스케이스 제목 |
| 5 | `agency_bureau` | 책임 조직(내부 부서) |
| 6 | `contact_email` | **책임 개인 또는 팀의 이메일** |
| 7 | `is_withheld` | 비공개 여부 **및 사유** |
| 8 | `development_stage` | **Pre-deployment / Pilot / Deployed / Retired** |
| 9 | `is_high_impact` | OMB M-25-21 기준 고영향 여부 |
| 10 | `HI_justification` | 고영향 **아님** 판정의 근거 |
| 11 | `topic_area` | 주제 영역 (14개 분류) |
| 12 | `classification` | 기술 분류 6종 — **Agentic** / Classical ML / Computer Vision / Generative AI / NLP / Reinforcement Learning |
| 13 | `problem_solved` | 해결하려는 문제 |
| 14 | `benefits` | 기대 편익 |
| 15 | `system_outputs` | 산출물 유형 (예측/추천/결정) |
| 16 | `operational_date` | 운영 개시일 또는 파일럿 시작일 |
| 17 | `contracting_usage` | 조달 방식 — 벤더 구매 / 자체 개발 / 혼합 |
| 18 | `vendor_name` | 벤더 식별 |
| 19 | `have_ato` | **ATO(운영 인가) 보유 여부** |
| 20 | `system_name_ato` | ATO 연계 시스템명 |
| 21 | `data_description` | 학습·테스트·운영 데이터 기술 |
| 22 | `link_to_data` | Federal Data Catalog 링크 |
| 23 | `has_pii` | **개인식별정보 포함 여부** |
| 24 | `pia_url` | 개인정보 영향평가(PIA) 링크 |
| 25 | `demographic_features` | 모델 피처로 쓰인 인구통계 변수 (12개 옵션) |
| 26 | `has_custom_code` | 자체 개발 코드 포함 여부 |
| 27 | `code_url` | 공개 소스코드 링크 |
| 28 | `hi_testing_conducted` | (고영향) 배포 전 테스트 상태 |
| 29 | `hi_assessment_completed` | (고영향) AI 영향평가 완료 여부 |
| 30 | `hi_potential_impacts` | (고영향) 프라이버시·시민권·자유에 대한 예견 가능 영향 |
| 31 | `hi_independent_review` | (고영향) 독립 검토 완료 여부 및 검토자 유형 |
| 32 | `hi_ongoing_monitoring` | (고영향) **지속 모니터링 프로세스** |
| 33 | `hi_training_established` | (고영향) **운영자 교육** 수립 여부 |
| 34 | `hi_failsafe_presence` | (고영향) **페일세이프 메커니즘** 존재 여부 |
| 35 | `hi_appeal_process` | (고영향) **결과에 이의를 제기할 절차** |
| 36 | `hi_public_consultation` | (고영향) 공개 의견수렴 및 반영 |

- **책에서의 값어치 (매우 큼):**
  - `development_stage`에 **`Retired`가 값으로 존재** → **정부는 이미 "은퇴한 AI"를 스키마에 넣어놨다.**
  - `classification`에 **`Agentic`이 별도 분류로 존재** → 에이전트를 따로 세고 있다.
  - `contact_email` — **책임자 필드가 이메일 하나로 강제**된다. 저자 스키마의 "책임자" 항목과 대조.
  - 28~36번 9개 필드가 **고영향에만 붙는다** → **위험 등급에 따라 요구 항목이 달라진다.** A-5의 "비례적 거버넌스"가 **정부 등록 스키마에 이미 구현돼 있다.**

### A-7-③. 벤더 레지스트리가 요구하는 필드

| 제품 | 요구 필드 | 출처 | 발행일 |
|---|---|---|---|
| **ServiceNow AI Control Tower** (AI Asset Inventory) | **provider, vendor, lifecycle phase, state, risk classification** + 자산 유형(systems / models / prompts / datasets / **MCP servers**) + CMDB·CSDM 관계 | servicenow.com/community | 2026-06 릴리스 |
| **Workday Agent System of Record** (Agent Registry) | 에이전트 **목록, 설명, 접근 권한을 가진 보안 그룹, 국가별 가용 지역, 현재 상태(status)** + 비용·ROI | blog.workday.com/en-us/managing-ai-powered-future-of-work.html | 2026-02 |
| **Microsoft Entra Agent ID / Agent 365** | agent identity blueprint / blueprint principal / agent identity / agent user + **Owner·Sponsor·Manager 3역할**(1차 확보) + access package 만료일 | learn.microsoft.com | 2026-06-05 |
| **Saviynt(제안)** | 암호학적 고유 ID, **생성 증명(creation attestation)**, model version, hosting environment, owner, purpose, 베이스라인 최소권한 정책 | saviynt.com/blog/ai-agent-lifecycle-management | 2026-02-26 |

### A-7-④. Model Card / System Card 표준 섹션 — `⚠️ 미확인`

- 이번 라운드에서 **조사 예산이 소진**되어 Model Card(Mitchell et al. 2019) / System Card의 표준 섹션 목록을 확정하지 못했다. **paper-researcher 담당 영역과 겹칠 가능성이 높다** — research-lead가 papers.md와 대조 후 필요 시 3차 요청 권장.

### A-7-⑤. ISO/IEC 42001 AI 시스템 인벤토리 요구 항목 — `⚠️ 미확인`

- 표준 원문 **유료(ISO 유료 배포)** 로 미접근. 무료 해설 문서에서도 **인벤토리 요구 항목의 조항 단위 목록**을 확보하지 못했다. → E 섹션 로그.

---

## A 커버리지

| 항목 | 상태 | 비고 |
|---|---|---|
| A-1 BNY | ✅ **확보 (부분 조건부)** | CEO 직접 발언 확보. **단 "사번"은 미확인 — `user ID/login`까지만** |
| A-2 Entra 라이선스 | ✅ **확보** | 공식 문서 기준 매트릭스 완성. **$ 가격은 신뢰성 중** |
| A-3 Workday | ✅ **확보** | 발표(2025-02-11)/GA(2026-02) 분리. Lattice 대비 프레이밍 원문 확보 |
| A-4 기타 벤더 | ⚠️ **부분 확보** | ServiceNow·AWS·Salesforce 확보 / **SAP·Google·Atlassian·Slack 미확인** |
| A-5 자율성 등급 | ✅ **초과 달성 (4종)** | Gartner·CSA·Feng·Salesforce. 통제 차등 명시 3종 |
| A-6 폐기·재심사 반례 | ✅ **확보 — 단 논지 조정 필요** | 벤더 층위 반례 다수. **조직 시행 사례는 여전히 0건** |
| A-7 등록 스키마 | ✅ **확보 (2/4)** | EU Annex VIII 전체 + OMB 36필드 전체. **Model Card·ISO 42001 미확보** |

---

# B. 축 5 — 등록된 에이전트의 성과관리·FTE·생산성

> ⚠️ **이 섹션의 모든 수치에 출처 성격 라벨이 붙어 있다. 라벨 없는 수치는 이 문서에 넣지 않았다.**

## B-1. FTE 환산·정원 산입

### B-1-①. RPA 시대의 봇 FTE 환산 관행 — **계보의 뿌리**

- **표준 계산식 (업계 관행):**
  > `FTE = 봇이 한 달에 처리한 건수 / 사람이 한 달에 처리하는 건수`
  > 또는 `FTE = (건당 사람 소요시간 × 봇 처리 건수) / 사람의 월 정규 근로시간`
- **채택 문턱(rule of thumb):** "**한 프로세스를 자동화해서 최소 2 FTE는 확보돼야 할 만하다**"
- **봇:사람 환산비 — 여기가 중요하다:**
  > "보수적 계산에서는 **라이선스 1개 = 3 FTE**로 가정하기도 한다. **그러나 실무에서는 1:1을 넘기는 것조차 어렵다** — 로봇은 대체로 정규 업무시간에만 돌고, 시스템 지연과 애플리케이션 응답시간 때문에 사람보다 빠르지도 않기 때문이다."
- 출처: https://www.itconvergence.com/blog/robotic-process-automation-rpa-roi/ , https://dtmates.com/en/business/return-on-investment-from-rpa-vs-hidden-costs/ , https://digitalworkforce.com/rpa-news/measuring-rpa-roi-how-to-do-it-right/
- 출처 성격: `[벤더 백서]` / 컨설팅 블로그 · 신뢰성 **중**
- **책에서의 값어치:** **"1 라이선스 = 3 FTE"라는 영업 숫자와 "실무에선 1:1도 어렵다"는 현장 숫자가 같은 업계 안에 공존한다.** 이게 축 5의 경고 문장이다.

### B-1-②. 그 관행이 비판받은 지점 【"이번엔 다르다"를 증명하려면 반드시 넘어야 할 것】

- **① 벤더 비즈니스 케이스의 과장:**
  > 벤더와 컨설팅은 흔히 "**12개월 미만 회수기간, 3년 ROI 약 500%**"의 하이레벨 비즈니스 케이스를 제시한다. 그러나 조직은 **RPA에 적합한 프로세스의 개수를 과대평가**하고 **프로세스 룰 정교화에 드는 작업량을 과소평가**한다. 그 결과 **비용 절감이라는 핵심 마일스톤이 결코 실현되지 않고(never materialize) 정치적 지지가 증발한다.**
- **② "시간 절감" 비즈니스 케이스의 근본 결함 【최고의 인용문】:**
  > "There is unlikely a single automation program in the world that has delivered to an '**Hours saved**' business case, and this is simply due to the lack of consideration of Human Capital Change — **10,000 hours sounds great until you realize it is 30 minutes from each of your 20,000 employees.**"
  - 출처: https://www.linkedin.com/pulse/benefit-realization-horror-movie-rpa-william-harris (저자: William Harris)
  - 출처 성격: `[커뮤니티/개인 블로그]` · 신뢰성 **중** (실무자 서명 글, 데이터 아님)
  - **책에서의 값어치: 최상급.** "AI로 연 10,000시간 절감"이라는 보고서를 받았을 때 던져야 할 질문이 이 한 문장에 있다.
- **③ 이중 계상(double counting):**
  > "**FTE 절감의 이중 계상은 흔한 오류다** — 사무 인력이 제거되지 않고 **재배치(redeployed)**되었다면, 재배치 가치는 **정원 절감과 별도로** 계상해야 한다."
- **④ 계산식 자체가 표준화돼 있지 않다:**
  > "**모두가 자기만의 FTE 편익 계산식을 쓴다** — 생산 가능 시간은 하루 **5.5시간에서 8시간** 사이 어디든이고, 연간 생산일수는 **200일에서 255일** 사이 어디든이다."
  - **책에서의 값어치:** 같은 자동화가 계산식에 따라 **편익이 40% 이상 차이 난다**는 뜻이다. 대리지표 조작(B-4)의 원형.
- **⑤ 실패율:** "RPA 도입은 **30~50%가 실패할 확률**이 있다 — EY 2016년 리포트"
  - 출처 성격: `[컨설팅 조사]` · **⚠️ EY 원 리포트 미대조. 2차 인용.**
- 출처(①③④⑤): https://www.advsyscon.com/blog/why-rpa-fails-robotic-process-automation/ , https://www.itconvergence.com/blog/robotic-process-automation-rpa-roi/
- 발행일: 개별 게시물 날짜 미표기 다수 `⚠️` — **연도 인용 시 주의**

### B-1-③. 현재의 "agentic workforce planning" 프레임

- **인력계획이 두 개의 산출물로 쪼개진다:**
  > "연간 계획은 이제 **두 개의 평행한 산출물**을 낸다: **사람 정원 계획(human headcount plan)**과 **AI 캐파 계획(AI capacity plan)**."
  - AI 에이전트가 인력의 일부가 되면 연간 사이클은 **AI 라이선스 물량, 플랫폼 벤더 계약, containment rate 궤적 가정**을 추가로 다뤄야 한다.
- **재무·인사에 대한 구체 권고:**
  > **재무:** "소프트웨어 라이선스와 **분리된 별도의 'agent labor' OpEx 계정**을 만들라."
  > **인사:** "**workflow deprecation protocol**을 만들라 — 이전에 FTE에게 할당됐던 태스크가 계획 주기 안에서 **공식적으로 ALU(agentic labor unit)로 이관되는 절차**."
- **FTE 지표 자체의 퇴조 주장:**
  > "디지털 워커를 통합하면서 **FTE라는 지표는 산출 측정에 덜 유효해지고 있다.** 선도 기업은 프로젝트에 사람 시간이 몇 시간 드는지 계산하는 대신 **토큰 캐파와 컴퓨트 할당**으로 운영 대역폭을 측정한다."
- 출처: https://blog.traversaal.ai/ai-agent-workforce-planning-product-roadmap/ , https://www.digitalapplied.com/blog/agentic-agency-reinventing-digital-services-2026 , https://ucstrategies.com/news/autonomous-ai-agent-pricing-2026-2/
- 출처 성격: `[커뮤니티/개인 블로그]` · 신뢰성 **하~중** `⚠️`
- **⚠️ 중대 경고:** 이 문단의 프레임들은 **실증 사례가 아니라 컨설턴트·블로거의 제안**이다. "60 FTE 규모 에이전틱 에이전시 구성"이나 "툴 COGS 3~5% → 12~18%", "주니어 정원 30~50% 압축" 같은 수치는 **출처 불명의 예시 모델**이므로 **책에 수치로 인용하지 말 것.** 개념(두 개의 계획, 별도 OpEx 계정, workflow deprecation protocol)만 **"이런 제안이 나오고 있다"** 수준으로 쓸 것.

### B-1-④ 표

| 항목 | 실체 | 출처 라벨 | 신뢰성 | 책 활용 |
|---|---|---|---|---|
| 봇 FTE 환산식 | 건수 기반 나눗셈, 표준 없음 | `[벤더 백서]` | 중 | 계보의 뿌리 |
| "1 라이선스 = 3 FTE" 보수 가정 vs "실무 1:1도 어렵다" | 업계 자기모순 | `[벤더 백서]` | 중 | **핵심 대비** |
| "10,000시간 = 2만 명 × 30분" | 시간절감 케이스의 결함 | `[커뮤니티]` | 중 | **최고 인용문** |
| 이중 계상 / 계산식 비표준(5.5~8h, 200~255일) | 측정 조작 여지 | `[벤더 백서]` | 중 | 축 5 경고 |
| 두 개의 평행 계획(사람/AI 캐파) | 제안 프레임 | `[커뮤니티]` | 하~중 | **개념만** |

---

## B-2. 회계·공시 축

### B-2-①. Klarna — **가장 중요한 계보** (선언 → 검증 → 번복)

**① 2024-02-27 원 발표 [보도자료 — 회사 공식]**

- 출처: https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/
- 발행일: **2024-02-27** · 출처 성격: **`[보도자료]`** · 신뢰성 **최상**
- **원문 수치:**
  - 첫 달 **2.3백만 건**의 대화 처리 = Klarna 전체 고객서비스 채팅의 **3분의 2**
  - > "doing the **equivalent work of 700 full-time agents**"
  - 고객 만족도는 사람 상담원과 **동등(on par)**
  - 오류 해결 정확도 향상 → **반복 문의 25% 감소**
  - 처리 시간 **11분 → 2분 미만**
  - **23개 시장, 35개 이상 언어**
  - > "estimated to drive a **$40 million USD in profit improvement** to Klarna in 2024"
  - CEO Sebastian Siemiatkowski: "This AI breakthrough in customer interaction means superior experiences for our customers at better prices, more interesting challenges for our employees, and better returns for our investors."
- **⚠️ 정확히 읽을 것:** 보도자료는 "**700명을 대체했다**"가 아니라 "**700 full-time agents의 일에 상당하는 양(equivalent work)**"이라고 썼다. **환산이지 대체가 아니다.** 이 문장이 언론에서 "700명 해고"로 번역되는 과정 자체가 축 5의 소재다.
- 참고: OpenAI 측 게재본 https://openai.com/index/klarna/ `[벤더 백서]` (본문 403 미접근 `⚠️`)

**② 2025-05 번복 [매체 보도 — Bloomberg 인터뷰]**

- **CEO Sebastian Siemiatkowski가 Bloomberg에 밝힌 내용:** AI 챗봇이 사람보다 **싸긴 했지만 "lower quality"**를 낳았다. Klarna는 고객이 원하면 **항상 사람과 대화할 수 있도록** 사람 인력을 다시 채용하고 있다.
- 출처(2차): https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396 , https://www.forbes.com/sites/quickerbettertech/2025/05/18/business-tech-news-klarna-reverses-on-ai-says-customers-like-talking-to-people/ , https://www.customerexperiencedive.com/news/klarna-reinvests-human-talent-customer-service-AI-chatbot/747586/
- 발행일: **2025-05-09 ~ 2025-05-18** · 출처 성격: `[매체 보도]` · 신뢰성 **중~최상** (복수 매체 일치, **Bloomberg 원문 미접근** `⚠️`)
- **현재 구조:** AI가 일반 소비자 채팅의 대부분을 1선에서 처리하고, **프리미엄·복잡 케이스 계층에는 사람을 재투입**한 하이브리드.

**③ 계보 요약 (책의 장면)**

| 시점 | 무엇을 말했나 | 라벨 |
|---|---|---|
| 2024-02-27 | "700 FTE **상당**의 일", "2024년 **$40M** 이익 개선 **추정**" | `[보도자료]` |
| 2025-05 | "싸지만 **품질이 낮다**", 사람 재채용 | `[매체 보도]` |

- **⚠️ 검증 불가 지점:** **$40M 이익 개선이 실제로 실현됐는지에 대한 사후 공시·검증 자료를 찾지 못했다.** 원 발표는 "estimated"였고, 실현 여부는 공개되지 않았다. → **이것 자체가 축 5의 논지다: 선언은 공개되고 검증은 공개되지 않는다.** `⚠️ 미확인 — 단, 이 미확인이 곧 발견`

### B-2-②. Salesforce — "I need less heads" [실적/경영진 발언]

- **Marc Benioff (Salesforce CEO), "The Logan Bartlett Show" 팟캐스트 출연:**
  > "**I was able to rebalance my headcount on my support**"
  > "**I've reduced it from 9,000 heads to about 5,000, because I need less heads.**"
  - AI 에이전트가 고객 상호작용의 **약 50%**를 처리하게 되면서 가능했다고 설명
- **회사 공식 입장 (프레이밍이 다르다):**
  > "Because of the benefits and efficiencies of Agentforce, we've seen the number of support cases we handle **decline** and we **no longer need to actively backfill support engineer roles**."
  - 즉 **해고가 아니라 "결원 미충원(no backfill) + 재배치"** 로 설명. 수백 명을 professional services, sales, customer success로 **재배치**했다고 밝힘.
- **다른 수치:** Agentforce로 지원 비용 **$100M 절감**, **300만 건** 고객 대화 처리 `[벤더 백서/경영진 발언]`
- 출처: https://www.cnbc.com/2025/09/02/salesforce-ceo-confirms-4000-layoffs-because-i-need-less-heads-with-ai.html , https://fortune.com/2025/09/02/salesforce-ceo-billionaire-marc-benioff-ai-agents-jobs-layoffs-customer-service-sales/ , https://www.foxbusiness.com/economy/salesforce-cuts-4000-jobs-due-ai-ceo-says
- 발행일: **2025-09-02** · 출처 성격: `[매체 보도]` (CEO 팟캐스트 발언 인용) · 신뢰성 **중~최상** (복수 매체 일치)
- 후속: 2026년 초 추가 1,000명 감축 보도 → 누적 약 5,000명 `[매체 보도]` `⚠️ 원 출처 미대조`
- **책에서의 값어치:** **같은 사실에 대해 CEO는 "heads를 줄였다"고 하고 회사 성명은 "백필을 안 한다"고 한다.** 축 5의 "정원 감축을 AI 성과로 보고할 때의 함정"이 한 회사 안에서 두 개의 문장으로 존재한다.

### B-2-③. AI 비용의 회계 분류 문제

- **핵심 문제 진술:**
  > 기업이 **인건비는 줄이면서** 소프트웨어 개발용 AI 토큰에 쓴 수백만 달러를 **자본화하지 않고 OpEx로 처리**할 때 중대한 회계 문제가 발생한다.
- **왜 분류가 안 되는가:**
  > AI 토큰 지출은 **어느 회계 항목에도 깔끔히 들어맞지 않은 채 여러 버킷을 넘나든다** — 클라우드처럼 소비 기반이지만 사람의 클릭이 아니라 **자율적 의사결정**이 유발하고, SaaS처럼 운영에 통합돼 있지만 SaaS 라이선스와 다르게 스케일하며, **일부 인건비를 대체하지만 정원 감축에 1:1로 매핑되지 않는다.**
- **권고되는 처리:**
  - 제품 경험의 일부라면 → 범용 AWS·호스팅 계정이 아니라 **COGS/DevOps 안의 별도 inference 계정**으로
  - **명시적 인력 대체·인력 회피(labor-substitution or labor-avoidance)** AI라면 → **수혜 기능(function) 안의 별도 서브계정**에 추적
- 출처: https://www.slash.com/blog/how-to-classify-ai-token-spend , https://valueops.broadcom.com/blog/accounting-best-practices-for-ai-use-in-software-development , https://www.thesaascfo.com/a-cfos-guide-to-tracking-digital-labor-and-agentic-ai/ , https://www.ey.com/en_us/insights/ai/agentic-ai-token-costs `[컨설팅 조사]`
- 출처 성격: `[벤더 블로그]` / `[컨설팅 조사]` · 신뢰성 **중** (개별 게시물 발행일 대부분 미표기 `⚠️`)
- **1차 확보분과의 연결:** 닛케이 2026-07-09 표제(본문 유료)와 같은 문제를 다룬다. **본 라운드에서도 닛케이 본문은 접근 실패** — E 섹션.
- **책에서의 값어치:** **"AI가 사람 일을 했는데, 그 비용은 인건비 줄에 안 잡힌다."** → 손익계산서상 인건비는 줄고 OpEx는 늘지만, **어느 줄에서 늘었는지 아무도 합의하지 못했다.** 축 5의 회계 파트 핵심.

---

## B-3. 생산성 측정 프레임 (실무용)

### B-3-①. 【최우선】 DORA 2025 — "AI는 증폭기다"

- **정식 명칭:** *State of AI-assisted Software Development* (2025) — DORA / Google Cloud
- 출처: https://dora.dev/dora-report-2025/ , https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report
- 발행: **2025** · 출처 성격: **`[벤더 백서]`** (Google Cloud 발간, 대규모 설문 기반. 연구 파트너: GitHub, GitLab, IT Revolution, SkillBench, Workhelix)
- 신뢰성: **최상** (업계 표준 레퍼런스)
- **핵심 결론 (공식 페이지 원문 인용):**
  > "AI's primary role is as an **amplifier**, magnifying an organization's **existing strengths and weaknesses**. The greatest returns on AI investment come **not from the tools themselves, but from a strategic focus on the underlying organizational system**."
- **수치 (⚠️ 2차 인용 — 원 리포트 PDF 미접근):**

| 수치 | 내용 | 라벨 | 대조 상태 |
|---|---|---|---|
| **90%** | 소프트웨어 개발 전문가의 AI 채택률 (전년 대비 +14%) | `[벤더 백서]` | ⚠️ 2차 |
| **80%+** | AI가 생산성을 높였다고 응답 | `[벤더 백서]` | ⚠️ 2차 |
| **59%** | AI가 코드 품질에 긍정적 영향이라고 응답 | `[벤더 백서]` | ⚠️ 2차 |
| **30%** | AI 생성 코드를 **거의 또는 전혀 신뢰하지 않는다** | `[벤더 백서]` | ⚠️ 2차 |
| **약 2시간/일** | 개발자의 일평균 AI 도구 사용 시간 | `[벤더 백서]` | ⚠️ 2차 |

- **⚠️ 축 5에 가장 중요한 대목 — "빨라졌지만 나아졌는가":** 복수의 리뷰가 DORA 2025를 두고 **"AI가 생산성은 올리지만 딜리버리(안정성)는 저해한다"**는 긴장을 지적한다.
  - https://devops.com/dora-2025-faster-but-are-we-any-better/ (제목: "DORA 2025: Faster, But Are We Any Better?")
  - https://bitbytebit.substack.com/p/dora-ai-boosting-productivity-hindering (제목: "DORA: AI boosting productivity, hindering delivery")
  - 출처 성격: `[매체 보도]`/`[커뮤니티]` · 신뢰성 **중**
  - **⚠️ 처리량↑ / 불안정성↑의 정확한 수치는 확보하지 못했다.** 원 리포트 PDF 대조 필요 `⚠️ 미확인`
- **동반 산출물:** **DORA AI Capabilities Model** (조직 역량 모델) — https://dora.dev/ai/capabilities-model/report/ (미조사 `⚠️`)
- **책에서의 값어치 (최상급):**
  > **"AI는 팀을 고치지 않는다. 팀을 증폭한다."** 강한 팀은 AI로 더 강해지고, **문제 있는 팀은 문제가 확대된다.** 버전 관리·관측성·**내부 플랫폼**이 강한 고성숙 조직이 **불균형하게 큰 편익**을 얻는다.
  > → **이 문장 하나가 축 3(중앙이 공급할 것)과 축 5(성과 측정)를 연결한다.** 중앙이 플랫폼을 깔아야 AI 투자 수익이 난다는 실증이다.

### B-3-②. SPACE / DX Core 4

- **DX Core 4:** DORA·SPACE·DevEx를 통합한 프레임. **4개 차원 — Speed, Effectiveness, Quality, Impact**
  - **개발:** Laura Tacho, Abi Noda가 **DORA·SPACE·DevEx 저자들과 협업**해 개발
  - **검증:** **300개 이상 조직**에서 테스트·정련 → **엔지니어링 효율 3~12% 증가**, **R&D 시간 중 기능 개발 비중 14% 증가**
  - Speed 차원의 지표 예: 엔지니어당 PR 수, lead time, 배포 빈도, **perceived rate of delivery**(주관적 체감 속도)
  - 출처: https://getdx.com/dx-core-4/ , https://getdx.com/research/measuring-developer-productivity-with-the-dx-core-4/
  - 출처 성격: **`[벤더 백서]`** (DX사 자체 프레임 + 자체 검증) · 신뢰성 **중** — **자사 프레임의 효과를 자사가 측정한 수치임을 반드시 명시**
- **SPACE의 한계 (DX 측 서술 — 이해상충 유의):**
  > "SPACE는 **자기 지표를 스스로 정의하는 프레임**을 제공하는데, 이게 실제로 하기가 어렵다. DevEx는 개발자 경험과 자기보고 지표에 집중하지만 **생산성이라는 더 넓은 개념과 분리돼 있다.**"
  - 출처: https://getdx.com/blog/space-metrics/ · 신뢰성 **중** (경쟁 프레임에 대한 벤더 평가)
- **중립 비교 자료:** https://www.swarmia.com/blog/comparing-developer-productivity-frameworks/ (DORA vs SPACE vs DX Core 4) `[벤더 블로그]`
- **⚠️ SPACE 원논문**(Forsgren·Storey·Maddila·Zimmermann·Houck·Butler, ACM Queue 2021)은 **paper-researcher 영역** — papers.md 대조 권장.

---

## B-4. 측정의 함정

### B-4-①. Goodhart's law — 원전과 정식 진술 【둘이 다르다】

| | 진술 | 출처 |
|---|---|---|
| **원전 (Goodhart, 1975)** | > "**Any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes.**" | Charles Goodhart, 영국 통화정책 논문, **1975** |
| **대중화 진술 (Strathern, 1997)** | > "**When a measure becomes a target, it ceases to be a good measure.**" | Marilyn Strathern (인류학자), **1997** — Hoskin의 1996 논문에 대한 응답 |

- 출처: https://en.wikipedia.org/wiki/Goodhart's_law , https://pmc.ncbi.nlm.nih.gov/articles/PMC7901608/ (PMC 게재 논평, 제목이 곧 Strathern 진술)
- 출처 성격: `[학술]` / 백과 · 신뢰성 **최상**(사실관계) / **중**(위키피디아 경유)
- **⚠️ 저술 시 필수 주의:** 널리 인용되는 **"When a measure becomes a target…"은 Goodhart가 한 말이 아니라 Strathern(1997)의 정식화**다. **Goodhart 1975로 귀속시키면 사실 오류.** — fact-checker 필독
- **관련 계보:** Campbell's law, Cobra effect — https://psychsafety.com/goodharts-law-campbells-law-and-the-cobra-effect/ `[커뮤니티]`

### B-4-②. 생산성 역설 — 정부·중앙은행 자료 【`[정부·중앙은행]` 라벨】

**① Atlanta Fed / Richmond Fed 워킹페이퍼 (2026) — 최고 등급 근거**

- **제목:** *Artificial Intelligence, Productivity, and the Workforce: Evidence from Corporate Executives*
- **저자:** Baslandze, Edwards, Graham, McClure, Sparks, Meyer, Waddell, Weitz
- **기관:** Federal Reserve Banks of **Atlanta and Richmond**
- **표본:** 기업 임원 **약 750명** 설문
- **날짜:** 워킹페이퍼 **2026-03-25**, SF Fed 게재 **2026-04-14**
- 출처: https://www.frbsf.org/research-and-insights/publications/system-research-atlanta-fed/2026/04/artificial-intelligence-productivity-workforce-evidence-from-corporate-executives/ / PDF: https://www.atlantafed.org/-/media/Project/Atlanta/FRBA/Documents/research/publication/working-paper/2026/03/25/04-artificial-intelligence-productivity-and-the-workforce-evidence-from-corporate-executives.pdf
- 출처 성격: **`[정부·중앙은행]`** (연준 워킹페이퍼) · 신뢰성 **최상**
- **핵심 발견 (원문 인용):**
  > **생산성 역설:** "a **productivity paradox, in which perceived productivity gains are larger than measured productivity gains**" — 매출 실현의 지연을 반영한 것으로 보임
  > **채택:** "substantial heterogeneity in AI adoption across firms, with **more than half having already invested**"
  > **어디서 나오나:** 이득은 자본 심화가 아니라 "**increases in revenue-based total factor productivity, closely associated with innovation- and demand-oriented channels**"에서 나온다
  > **업종:** "the largest effects concentrated in **high-skill services and finance**"
  > **고용:** "**little evidence of near-term aggregate employment declines due to AI**" — 대기업은 인력 감축을 예상하나 소기업은 소폭 증가 예상. 구성 변화: **정형 사무직 감소, 숙련 기술직 수요 증가**
- **2026 전망 수치 (⚠️ 2차 인용, PDF 원문 미대조):** 응답 기반 노동생산성 증가율 평균 **3.0%**, 함의된(implied) 측정치 **1.8%** `[정부·중앙은행]` `⚠️`
- **책에서의 값어치 (최상급):** **"체감한 생산성 향상이 측정된 생산성 향상보다 크다."** — 연준이 750명 임원에게 물어서 확인한 격차다. 축 5 전체의 논지를 한 문장으로 지지한다. **그리고 "AI 때문에 총고용이 줄었다는 증거는 아직 미미하다"는 것도 같은 논문에서 나온다** — 균형 잡힌 서술 가능.

**② OECD**

- **제목:** *Miracle or Myth? Assessing the macroeconomic productivity gains from Artificial Intelligence*
- 출처: https://www.oecd.org/en/publications/miracle-or-myth-assessing-the-macroeconomic-productivity-gains-from-artificial-intelligence_b524a072-en.html
- 출처 성격: **`[정부·중앙은행]`** (국제기구) · 신뢰성 **최상**
- **수치 (⚠️ 2차 인용):**
  - AI로 인한 연간 **총요소생산성(TFP)** 증가 주 추정치: **0.25~0.6%p** (노동생산성 기준 **0.4~0.9%p**)
  - **국가 단위로는 AI 채택률과 TFP 증가 사이에 강한 양의 상관이 없다**; TFP 분산의 **3분의 1 미만**만 설명됨
- **발행일 미확인** `⚠️` — 원 문서 페이지 직접 대조 필요
- **책에서의 값어치:** **"국가 단위로 보면 AI 많이 쓴 나라가 더 생산적이지 않다."** Solow 역설의 2026년판.

**③ 참고 (신뢰성 중~하)**
- Fortune, "Why AI is raising worker productivity but not making the economy more efficient" — https://fortune.com/2026/05/27/ai-productivity-internet-boom-solow-paradox/ (2026-05-27) `[매체 보도]`
- Man Group, "The Productivity Paradox: When Will AI Deliver?" — https://www.man.com/insights/the-productivity-paradox `[벤더 백서]` (자산운용사 리서치, 이해상충 유의)
- ⚠️ "전 세계 AI 투자가 연 **$500B**를 넘는데 OECD TFP 증가는 여전히 평평하다"는 서술이 검색 결과에 등장했으나 **원자료 미확인** → `⚠️ 인용 금지`

### B-4-③. 대리지표 조작 — `⚠️ 부분 확보`

- 이번 라운드에서 **"토큰 사용량·요청 수·도입률을 대리지표로 삼았다가 조작된 공개 사례"**를 **확보하지 못했다.** 대신 **구조적 근거**는 확보했다:
  - B-1-②-④ **FTE 계산식 비표준화**(5.5~8h, 200~255일) — 같은 자동화의 편익을 계산식으로 부풀릴 수 있다
  - B-1-②-③ **이중 계상**
  - B-3-②의 **"perceived rate of delivery"**가 정식 지표로 들어가 있다는 사실 — 자기보고 지표의 구조적 취약성
  - Golden Cage Syndrome(C-③)의 **"vanity metrics over friction reduction"** — 조직이 인지 부하 대신 **배포 빈도 같은 무관한 지표를 추적한다**는 지적
- → `⚠️ 미확인 — 3차 조사 시 커뮤니티 리서처와 분담 권장` (개발자 커뮤니티에 실사례가 있을 가능성이 높다)

---

## B-5. 성과관리 제도 설계

### B-5-①. 에이전트 자체에 KPI를 부여한 사례 — 프레임은 있고 **조직 사례는 없다**

- **제안되는 핵심 지표군 (복수 벤더 프레임 공통):**
  - **end-to-end task-success rate** (종단 태스크 성공률)
  - **task-completion time**
  - **human-intervention rate** (사람 개입률) ← **자율성 등급과 직결**
  - **cost per completed task** (완료 태스크당 단가)
  - 해결계: resolution rate, deflection rate, **reopen rate**, first contact resolution(FCR)
  - **Autonomous SLA Compliance** — 에이전틱 결과가 사전 정의된 SLO를 충족하는 비율
  - 거버넌스계: **Goal Alignment Rate**(에이전트 행동이 전략·윤리 목표와 정렬되는 빈도), **Policy Violation Rate**(규칙 위반·의도치 않은 행동 빈도)
- 출처: https://fin.ai/learn/ai-agent-kpis-enterprise-performance-metrics-framework , https://oteemo.com/blog/kpis-measuring-agentic-ai/ , https://omnithium.ai/blog/agentic-ai-performance-slas.html , https://agility-at-scale.com/ai/strategy/performance-metrics-and-kpis/
- 출처 성격: `[벤더 블로그]` · 신뢰성 **중~하** · 발행일 대부분 미표기 `⚠️`
- **⚠️ 판정: 이것들은 전부 "이렇게 재라"는 제안이다. 실제 조직이 에이전트에 KPI를 걸고 운영한 공개 사례는 이번 라운드에서 0건.**
- **책에서 쓸 만한 관찰:** **`human-intervention rate`가 지표로 제안된다는 것 자체가 A-5의 자율성 등급과 축 5를 잇는 다리다.** 개입률이 낮아지면 등급이 오르고, 등급이 오르면 통제가 달라진다. **측정이 곧 등급 심사가 된다.**

### B-5-②. 절감 인력의 처리 — 재배치 선언과 그 결과 【가장 민감한 대목】

**① 재배치를 선언한 쪽**

- **Salesforce:** "결원을 적극적으로 백필하지 않는다" + 수백 명을 professional services / sales / customer success로 **재배치** (B-2-② 참조) `[매체 보도]` 2025-09-02
- **Accenture:** CEO Julie Sweet — 역할이 진화하는 직원의 재교육에 계속 투자하겠다면서 동시에 **"those we cannot reskill will be exited."** `[매체 보도]` — **⚠️ 발언 시점·원 출처 미확정**
- **⚠️ 순수한 "무해고 선언(no-layoff pledge)"의 확정 공개 사례는 찾지 못했다.** 검색어 `no layoff pledge automation`, `automation redeployment commitment`, `AI reskilling instead of layoffs company` 모두 **제도 선언 원문에 도달하지 못했다.** → `⚠️ 미확인` (E 섹션)

**② 그 결과 — 되돌린 쪽**

- **CNBC (2026-07-01), "Employers who laid off workers citing AI are already starting to regret it"** — https://www.cnbc.com/2026/07/01/employers-who-laid-off-workers-for-ai-are-reversing-their-decisions.html
  - **⚠️ 본문 403 미접근.** 제목과 2차 요약만 확보.
- **2차 보도로 확보한 수치 (⚠️ 조사 주체·표본 미확인 — 인용 시 반드시 재검증):**

| 수치 | 내용 | 라벨 | 상태 |
|---|---|---|---|
| **33%** | AI 감원 후 핵심 스킬·전문성을 상실한 기업 비율 | `[컨설팅 조사]` | ⚠️ **조사명·표본 미확인** |
| **약 2/3** | 자동화 감원 후 인력을 재채용한 고용주 비율 | `[컨설팅 조사]` | ⚠️ **동일** |
| **55.1%** | 재교육·재배치를 **공식적으로 논의조차 하지 않은** 기업 비율 | `[컨설팅 조사]` | ⚠️ **동일** |
| **51.3%** | 제거한 역할의 최대 1/4은 재배치 지원이 있었다면 다른 역할로 전환 가능했다고 보는 기업 비율 (추가 28.3%는 26~50%로 추정) | `[컨설팅 조사]` | ⚠️ **동일** |
| **75%** | AI 기반 감원이 절감액보다 비용이 더 들었다고 판단한 조직 비율 | `[컨설팅 조사]` | ⚠️ **동일 — 특히 강한 주장이므로 원자료 없이 인용 금지** |

  - 출처: https://www.peoplematters.in/amp/news/workforce-planning/ai-layoffs-backfire-as-33percent-of-companies-lose-critical-skills-and-expertise-report-48771
  - **⚠️⚠️ 이 다섯 수치는 전부 동일 매체가 인용한 미상의 리포트에서 나왔다. 원 리포트를 특정하지 못했다. 책에 쓰려면 fact-checker가 원 조사를 먼저 찾아야 한다. 못 찾으면 삭제.**
- **되돌린 기업 (개별 사례, `[매체 보도]`):** Ford(품질 이슈 대응 위해 숙련 엔지니어 수백 명 재채용), Commonwealth Bank of Australia, IBM — **⚠️ 각 사례의 원 보도 미대조**
- **HBR (2026-08), "AI Transformation Requires Redesigning Work, Not Cutting Roles"** — https://hbr.org/2026/08/ai-transformation-requires-redesigning-work-not-cutting-roles `[매체 보도]` — 본문 미접근, **제목이 곧 논지**

### B-5-③. 사람+에이전트 팀의 성과 귀속(attribution) — `⚠️ 미확인`

- **"에이전트가 한 일을 사람의 평가에 어떻게 반영하는가"에 대한 공개된 인사 제도 사례를 찾지 못했다.**
- 가장 근접한 것: Workday의 "measured like investments, governed like employees"(A-3-③) — **제도가 아니라 프레이밍**이다.
- BNY의 "디지털 직원이 사람 매니저에게 보고하고 매니저가 산출물을 검토·승인한다"(A-1-②) — **평가 반영 여부는 불명**
- → `⚠️ 미확인 — 이 공백이 크다. 책이 여기서 독자적 기여를 할 여지가 있다는 뜻이기도 하다.`

---

## B 커버리지

| 항목 | 상태 | 비고 |
|---|---|---|
| B-1 FTE 환산·정원 산입 | ✅ **확보** | RPA 계보 + 4가지 비판점 확보. **현행 agentic 프레임은 신뢰성 하~중, 개념만 사용** |
| B-2 회계·공시 | ✅ **확보** | Klarna 보도자료 원문 + 번복 / Salesforce CEO 발언 + 회사 성명 대비 / 회계 분류 문제 |
| B-3 생산성 측정 프레임 | ✅ **확보** | **DORA "증폭기" 결론 확보(최상급)**. 단 **수치는 전부 2차 인용, PDF 대조 필요** |
| B-4 측정의 함정 | ⚠️ **부분 확보** | Goodhart 원전/정식화 구분 확보. **연준·OECD 확보(최상급)**. **대리지표 조작 실사례 0건** |
| B-5 성과관리 제도 | ⚠️ **부분 확보** | KPI 프레임 확보(조직 사례 0건). **재배치 수치 5개가 전부 원자료 미확인 — 위험** |

---

# C. 축 3 재각도 — "중앙이 무엇을 공급했을 때 현장 혁신이 살아남았나"

> 교정된 논지: **"바텀업이 씨앗을 만든다. 탑다운이 할 일은 지시가 아니라 거두는 체계다. 탑다운이 공급하는 것은 과제 목록이 아니라 기준·자원·제도다."**

## C-①. 【최강 근거】 DORA 2025 — 플랫폼이 있는 조직만 AI 수익을 낸다

- **원문 인용:**
  > "AI's primary role is as an **amplifier**... The greatest returns on AI investment come not from the tools themselves, but from **a strategic focus on the underlying organizational system**."
  > 고성숙 조직 — **강한 버전 관리, 관측성, 그리고 내부 플랫폼(internal platforms)**을 갖춘 조직 — 이 **불균형하게 큰 편익(outsized benefits)**을 본다.
- 출처: https://dora.dev/dora-report-2025/ · 발행 2025 · `[벤더 백서]` · 신뢰성 **최상**
- **왜 이게 축 3의 뼈대인가:** 이 문장은 **"중앙이 무엇을 공급해야 하는가"에 대한 실증적 답**이다. 과제 목록이 아니다. **버전 관리, 관측성, 내부 플랫폼** — 전부 **기준·자원·제도**다. 그걸 깔아둔 조직에서만 현장의 AI 활용이 수익으로 전환됐다.

## C-②. Paved road / Golden path — 중앙이 길을 깔되 강제하지 않는다

- **Netflix의 "paved road":**
  > Netflix는 자기 플랫폼을 "**paved path**"라 부른다 — 일급으로 지원되는 인프라·언어·툴링을 포함한 **더 매끄러운 길**. 내부 도구는 표준 워크로드에 대해 아이디어에서 프로덕션 배포까지 **몇 분** 만에 가게 한다. **그러나 누구도 paved road로 강제되지 않는다(they never force anyone onto the paved road).**
  - 출처: https://thenewstack.io/developer-productivity-engineering-at-netflix/ , https://developer-enablement.com/what-is-the-paved-road/
  - 출처 성격: `[매체 보도]` / `[커뮤니티]` · 신뢰성 **중** · 발행일 미표기 `⚠️`
- **Golden path의 원리 (핵심 정의):**
  > "반복되는 작업을 통과하는 **지원되고 의견이 있는(opinionated) 경로**를 팀에 제공하는 것 — 손으로 하는 것보다 빠르고, 피하는 것보다 안전하다. **플랫폼은 옳은 길을 쉬운 길로 만든다.** 표준·가드레일·제도적 지식이 **몇몇 시니어의 머릿속이 아니라 그 길 자체에 구워져 있다.**"
  - **책에서의 값어치 (최상급):** **"기준을 문서로 배포하지 말고 길에 구워 넣어라."** 이 문장 하나가 축 3의 교정된 논지를 정확히 표현한다. 중앙이 공급하는 것은 **지시가 아니라 길**이다.
- **Spotify Backstage:**
  > Backstage는 **골든 패스 철학을 구현한 소프트웨어 템플릿 시스템**을 갖춘 내부 개발자 포털. 템플릿으로 **CI/CD·모니터링·로깅·문서가 이미 구성된 마이크로서비스를 몇 분 만에** 생성. 내부 버전은 **2,000+ 백엔드 서비스, 300개 웹사이트, 4,000개 데이터 파이프라인** 관리.
  - 출처: https://www.infoq.com/news/2021/03/spotify-paved-paths (2021-03) `[매체 보도]`, https://sph.sh/en/posts/paved-road-frontend-platform/ `[커뮤니티]`
  - **⚠️ "2026년 Backstage를 agent-first 플랫폼으로 진화시켜 AI 어시스턴트가 개발자 오버헤드를 약 47% 줄였다"는 서술이 검색 결과에 있었으나 원 출처 미확인 → `⚠️ 인용 금지`**
- **Team Topologies와의 연결:**
  > Team Topologies는 **제품 흐름에는 stream-aligned 스쿼드, paved road에는 platform team, 역량 부스트에는 enabling team, 필요한 곳에 complicated-subsystem team**을 권한다. Netflix는 Team Topologies가 말하는 enabling / complicated-subsystem / platform 팀의 복합 구성을 갖고 있다.
  - 출처: https://thenewstack.io/developer-productivity-engineering-at-netflix/ · `[매체 보도]` · 신뢰성 **중**
  - **⚠️ Team Topologies 원저(Skelton & Pais, 2019)는 미대조.** 개념 인용 시 원저 확인 권장.

## C-③. 하향식 강제가 역효과를 낸 사례 — 균형

- **"Golden Cage Syndrome"** — Vladimir Mikhalev (Field CTO, Valdemar.ai), **2026-03-05**, Platform Engineering 블로그
  - 출처: https://platformengineering.org/blog/golden-cage-syndrome-why-internal-developer-platforms-fail
  - 출처 성격: `[커뮤니티/개인 블로그]` (플랫폼 엔지니어링 커뮤니티 게재) · 신뢰성 **중**
- **세 가지 실패 원인:**
  1. **Field of Dreams 오류** — "If we build it, they will come. **No, they won't.**" 개발자는 플랫폼을 **소비자로서** 대하고, 네이티브 도구보다 느리다고 인지되면 우회한다. **정책 강제로는 진짜 채택을 만들 수 없다.**
  2. **허영 지표(vanity metrics)가 마찰 감소를 대체** — 조직이 인지 부하가 아니라 배포 빈도 같은 무관한 지표를 추적한다.
     > "**If I can deploy in 5 minutes, but I have to spend 4 hours debugging a cryptic error message... your platform has failed.**"
  3. **탈출구 없는 새는 추상화(leaky abstractions without escape hatches)** — 인프라 복잡성을 감췄다가 장애 시 개발자를 가둔다. 디버깅이 불가능해져 플랫폼 팀에 의존하게 된다.
- **강제 vs 자발 — 결정적 테스트:**
  > "**Mandatory adoption breeds workarounds**" — 개발자는 raw AWS 자격증명을 쓰며 "paved road"를 우회한다.
  > 정의적 질문: **"If I made this platform optional tomorrow, would you still use it?"**
- **올바른 모델 vs 틀린 모델:**
  > **옳은 모델:** "**A paved highway next to off-road terrain**" — 속도를 원하면 표준 경로를, 필요하면 raw 인프라를
  > **틀린 모델:** **케이지(cage)** — 경직되고, **의무적이고**, 불투명하고, 엔지니어의 자율성을 제한하는 추상화
- **⚠️ "80%의 DIY 플랫폼이 실패한다"는 수치**가 이 계열 자료에 반복 등장하나(platformengineering.org, hackernoon), **조사 방법·표본이 공개되지 않았다.** → `⚠️ 수치 인용 금지, 서술만`
- **다른 실패 분석:**
  - Thoughtworks, "Turning the tide: Overcoming the platform challenge of low developer adoption" — https://www.thoughtworks.com/insights/blog/platforms/platform-engineering-challenges--a-guide-to-overcoming-an-inadeq/turning-the-tide--overcoming-the-platform-challenge-of-low-devel `[컨설팅 조사]`
  - "Why Internal Developer Platform Adoption Fails: **Trust**, Breaking Changes, and Backward Compatibility" — https://www.thecloudplaybook.com/p/developer-platform-adoption-trust-internal-developer-platform `[커뮤니티]`
    > "**Trust drives adoption behavior.** 개발자가 플랫폼을 우회하거나 자기 해법을 짤 때, 그들은 당신에게 무언가를 말하고 있는 것이다."
- **책에서의 값어치:** 축 3의 **반대편 난간**. 중앙이 기준·자원·제도를 공급하되 **강제하는 순간 섀도 개발이 시작된다.** 이건 Gartner의 "과잉 제한 → shadow development"(A-5-①)와 **정확히 같은 실패 모드**다. **거버넌스와 플랫폼이 같은 함정을 공유한다** — 좋은 교차 참조.

## C-④. InnerSource — 사내 오픈소스

- **채택 기업:** SAP, Microsoft, IBM이 InnerSource 개념을 일찍 수용. InnerSource Commons Foundation이 금융·제조·통신·헬스케어 등 유럽·미국 중심의 기업 사례집 운영.
- **사례 (Robert Bosch):** 제품 개발 부문과 서비스 부문 간 **공통 코드베이스 공유** → 현장으로부터의 **빠른 피드백 사이클** 구현, 내부 협업 효율과 제품 품질 개선
- **금융권:** 엄격한 보안·컴플라이언스를 지키면서 **내부 코드 공유·리뷰 프레임워크**를 구축해 리스크 완화와 개발 효율을 양립
- **채택 동기:** "기업이 InnerSource를 채택하는 주된 이유 중 하나는 **소프트웨어 재사용 증가**다 — 재사용 가능한 자산을 공유하는 **공통 공간**을 만드는 InnerSource 관행이 투명성을 높이고 중복 작업을 피하게 해준다."
- **실증 (조직 효과):** "이너소스 프로젝트에 참여하는 직원은 **더 많은 사회적 상호작용 유대**를 형성하고 소프트웨어 프로젝트에 대한 **공유된 이해 수준이 높다.** **사회적 자본이 이너소스 참여와 직무 만족 사이를 매개**한다."
- 출처: https://innersourcecommons.org/learn/books/adopting-innersource-principles-and-case-studies/ , https://patterns.innersourcecommons.org/p/maturity-model , https://community.sap.com/t5/open-source-blog-posts/everything-you-always-wanted-to-know-about-innersource-adoption-in-your/ba-p/14355677
- 출처 성격: `[학술]`(Adopting InnerSource 서적·논문) / `[벤더 블로그]`(SAP) · 신뢰성 **중~최상**
- **학술 뒷받침 (paper-researcher 영역과 중복 가능):**
  - "Inner source software development: Current thinking and an agenda for future research" — https://www.sciencedirect.com/science/article/pii/S0164121220300030 `[학술]`
  - "Large scale reuse of microservices using DevOps and InnerSource practices — A longitudinal case study" — https://arxiv.org/pdf/2309.15175 `[학술]`
  - "InnerSource Circumplex Model: Mapping Cross-organizational Developer Collaboration Patterns with Insights from Japanese Corporate Experience" — https://arxiv.org/pdf/2502.15747 `[학술]`
- **InnerSource Patterns의 Maturity Model** — https://patterns.innersourcecommons.org/p/maturity-model (성숙도 모델 원문, 상세 미조사 `⚠️`)
- **책에서의 값어치:** **중앙이 "코드를 이렇게 짜라"고 지시하는 대신 "공유할 공간과 리뷰 규칙"을 공급했을 때 재사용이 늘었다.** 축 3의 교정된 논지에 정확히 부합하는 계보 — 그리고 AX 시대에 그대로 이식 가능하다(에이전트·프롬프트·툴의 이너소스).

## C 커버리지

| 항목 | 상태 | 비고 |
|---|---|---|
| DORA "증폭기 + 내부 플랫폼" | ✅ **확보 (최상급)** | 축 3의 실증적 뼈대 |
| Paved road / Golden path | ✅ **확보** | Netflix "강제하지 않는다" + "길에 구워 넣는다" 정의. **발행일 미표기 다수** `⚠️` |
| Team Topologies | ⚠️ **부분** | 2차 인용만. **원저 미대조** |
| 하향식 강제의 역효과 | ✅ **확보** | Golden Cage Syndrome(2026-03-05). **"80% 실패" 수치는 사용 금지** |
| InnerSource | ✅ **확보** | Bosch 사례 + 사회적 자본 실증. 학술 연결 있음 |

---

# D. 참고문헌

> 형식: `제목 — URL — 발행일 — [출처 성격 라벨] — 신뢰성`

## D-1. 공식 1차 소스 (규제·정부·표준)

1. **EU AI Act Annex VIII: Information to be Submitted upon the Registration of High-Risk AI Systems** — https://artificialintelligenceact.eu/annex/8/ — 현행(2026-09-05 접속) — `[규제 원문]` — **최상**
2. **2025 Federal Agency AI Use Case Inventory (data dictionary, 36 fields)** — https://github.com/ombegov/2025-Federal-Agency-AI-Use-Case-Inventory — repo 상태 2026-04-13 / 공개 2026-01-28 — `[정부 통계]` — **최상**
3. **Artificial Intelligence, Productivity, and the Workforce: Evidence from Corporate Executives** (Atlanta & Richmond Fed) — https://www.frbsf.org/research-and-insights/publications/system-research-atlanta-fed/2026/04/artificial-intelligence-productivity-workforce-evidence-from-corporate-executives/ — 2026-03-25 (게재 2026-04-14) — `[정부·중앙은행]` — **최상**
4. **OECD, Miracle or Myth? Assessing the macroeconomic productivity gains from Artificial Intelligence** — https://www.oecd.org/en/publications/miracle-or-myth-assessing-the-macroeconomic-productivity-gains-from-artificial-intelligence_b524a072-en.html — 발행일 미확인 `⚠️` — `[정부·중앙은행]` — **최상**
5. **CSA, Autonomy Levels for Agentic AI** (Jim Reavis) — https://cloudsecurityalliance.org/blog/2026/01/28/levels-of-autonomy — 2026-01-28 — `[표준·기관]` — **최상**

## D-2. 벤더 공식 문서

6. **Governing Agent Identities — Microsoft Entra ID Governance** — https://learn.microsoft.com/en-us/entra/id-governance/agent-id-governance-overview — 2026-06-05 (갱신 2026-06-24) — `[벤더 문서]` — **최상**
7. **Microsoft Entra Agent ID licensing (docs source)** — https://github.com/MicrosoftDocs/entra-docs/blob/main/docs/includes/licensing-agent-id.md — main 브랜치 2026-09-05 기준 — `[벤더 문서]` — **최상**
8. **Microsoft Entra plans and pricing** — https://www.microsoft.com/en-us/security/business/microsoft-entra-pricing — 현행 — `[벤더 문서]` — **중** (본문 직접 대조 실패)
9. **Workday newsroom, The Next Generation of Workforce Management is Here — Workday Unveils New Agent System of Record** — https://newsroom.workday.com/2025-02-11-The-Next-Generation-of-Workforce-Management-is-Here-Workday-Unveils-New-Agent-System-of-Record — **2025-02-11** — `[보도자료]` — **최상**
10. **Workday blog, The Workday Agent System of Record Is Now Generally Available** — https://blog.workday.com/en-us/managing-ai-powered-future-of-work.html — **2026-02** (정확 일자 미표기 `⚠️`) — `[벤더 블로그]` — **최상**
11. **BNY, Artificial Intelligence (corporate)** — https://www.bny.com/corporate/global/en/about-us/technology-innovation/artificial-intelligence.html — 현행 — `[벤더 문서]` — **최상**
12. **Klarna press release, Klarna AI assistant handles two-thirds of customer service chats in its first month** — https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/ — **2024-02-27** — `[보도자료]` — **최상**
13. **Amazon Bedrock AgentCore Identity (docs)** — https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html — 현행 — `[벤더 문서]` — **최상**
14. **Amazon Bedrock AgentCore is now generally available** — https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available — **2025-10** — `[보도자료]` — **최상**
15. **Salesforce, The Agentic Maturity Model** (Shibani Ahuja) — https://www.salesforce.com/news/stories/agentic-maturity-model/ — **2025-04-10** — `[벤더 문서]` — **중~최상**
16. **Salesforce, Achieving Reliable Agent Behavior (Levels of Determinism)** — https://www.salesforce.com/agentforce/levels-of-determinism/ — 현행 — `[벤더 문서]` — **중** (상세 미조사)
17. **ServiceNow Community, AI Control Tower: What's new in the June 2026 release** — https://www.servicenow.com/community/ai-control-tower-articles/ai-control-tower-what-s-new-in-the-june-2026-release/ta-p/3561445 — **2026-06** — `[벤더 문서]` — **최상**
18. **DORA, State of AI-assisted Software Development 2025** — https://dora.dev/dora-report-2025/ — **2025** — `[벤더 백서]` — **최상**
19. **Google Cloud Blog, Announcing the 2025 DORA Report** — https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report — 2025 — `[벤더 백서]` — **최상**
20. **DX, DX Core 4** — https://getdx.com/dx-core-4/ — 현행 — `[벤더 백서]` — **중** (자사 프레임 자체 검증)

## D-3. 컨설팅·기관 조사

21. **Gartner, Applying Uniform Governance Across AI Agents Will Lead to Enterprise AI Agent Failure** — https://www.gartner.com/en/newsroom/press-releases/2026-05-26-gartner-says-applying-uniform-governance-across-ai-agents-will-lead-to-enterprise-ai-agent-failure — **2026-05-26** — `[컨설팅 조사]` — **중~최상** (**원문 403, 3개 매체 교차 확인**)
22. Gartner 2차 인용본 — https://techedgeai.com/gartner-says-applying-uniform-governance-across-ai-agents-will-lead-to-enterprise-ai-agent-failure/ — 2026-05~ — `[매체 보도]` — **중**
23. **Deloitte Insights, Agentic AI strategy (Tech Trends 2026)** — https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html — 2026 — `[컨설팅 조사]` — **최상** (본문 미대조 `⚠️`)

## D-4. 학술

24. **Feng, McDonald, Zhang, Levels of Autonomy for AI Agents** — https://knightcolumbia.org/content/levels-of-autonomy-for-ai-agents-1 / https://arxiv.org/abs/2506.12469 — **2025-07-28** (arXiv 2025-06) — `[학술]` — **최상**
25. **"When a Measure Becomes a Target, It Ceases to be a Good Measure" (PMC)** — https://pmc.ncbi.nlm.nih.gov/articles/PMC7901608/ — `[학술]` — **최상**
26. **Goodhart's law (Wikipedia, 원전·정식화 계보)** — https://en.wikipedia.org/wiki/Goodhart's_law — `[백과]` — **중**
27. **Inner source software development: Current thinking and an agenda for future research** — https://www.sciencedirect.com/science/article/pii/S0164121220300030 — `[학술]` — **최상**
28. **Large scale reuse of microservices using DevOps and InnerSource practices** — https://arxiv.org/pdf/2309.15175 — `[학술]` — **최상**

## D-5. 매체 보도

29. **TBPN Digest, BNY Mellon CEO Robin Vince on Eliza** — https://www.tbpndigest.com/story/2026-03-23/bny-mellon-ceo-robin-vince-on-eliza-their-internal-ai-platform-powering-125-solutions-and-digital-employee-agents — **2026-03-23** — `[매체 보도]` — **중~최상**
30. **CU Today, BNY Mellon Blurs The Line Between Staff And Software** (WSJ 인용) — https://www.cutoday.info/Fresh-Today/BNY-Mellon-Blurs-The-Line-Between-Staff-And-Software-With-AI-Powered-Employees — **2025-07-10** — `[매체 보도]` — **중**
31. **The Stack, The Big Interview: BNY CIO Leigh-Ann Russell** — https://www.thestack.technology/the-big-interview-bny-cio-leigh-ann-russell/ — **2025-08-26** (갱신 2025-12-28) — `[매체 보도]` — **최상**
32. **Axios, This Wall Street bank has over 100 "digital employees"** — https://www.axios.com/2025/10/17/ai-wall-street-digital-workers — **2025-10-17** — `[매체 보도]` — **중** (본문 403 `⚠️`)
33. **CNBC, Digital employees, AI bootcamps: America's oldest bank is spending billions on tech** — https://www.cnbc.com/2026/02/09/digital-employees-ai-bootcamps-americas-oldest-bank-spends-billions-on-tech.html — **2026-02-09** — `[매체 보도]` — **중** (본문 403 `⚠️`)
34. **CNBC, Salesforce CEO confirms 4,000 layoffs 'because I need less heads' with AI** — https://www.cnbc.com/2025/09/02/salesforce-ceo-confirms-4000-layoffs-because-i-need-less-heads-with-ai.html — **2025-09-02** — `[매체 보도]` — **중~최상**
35. **Fortune, Salesforce CEO Marc Benioff says his company has cut 4,000 customer service jobs** — https://fortune.com/2025/09/02/salesforce-ceo-billionaire-marc-benioff-ai-agents-jobs-layoffs-customer-service-sales/ — **2025-09-02** — `[매체 보도]` — **중~최상**
36. **Entrepreneur, Klarna Is Hiring Customer Service Agents After AI Couldn't Cut It** — https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396 — **2025-05-09** — `[매체 보도]` — **중**
37. **Forbes, Klarna Reverses On AI, Says Customers Like Talking To People** — https://www.forbes.com/sites/quickerbettertech/2025/05/18/business-tech-news-klarna-reverses-on-ai-says-customers-like-talking-to-people/ — **2025-05-18** — `[매체 보도]` — **중**
38. **CNBC, Employers who laid off workers citing AI are already starting to regret it** — https://www.cnbc.com/2026/07/01/employers-who-laid-off-workers-for-ai-are-reversing-their-decisions.html — **2026-07-01** — `[매체 보도]` — **중** (본문 403 `⚠️`)
39. **HBR, AI Transformation Requires Redesigning Work, Not Cutting Roles** — https://hbr.org/2026/08/ai-transformation-requires-redesigning-work-not-cutting-roles — **2026-08** — `[매체 보도]` — **최상** (본문 미접근 `⚠️`)
40. **DevOps.com, DORA 2025: Faster, But Are We Any Better?** — https://devops.com/dora-2025-faster-but-are-we-any-better/ — 2025 — `[매체 보도]` — **중**
41. **The New Stack, Developer Productivity Engineering at Netflix** — https://thenewstack.io/developer-productivity-engineering-at-netflix/ — 발행일 미표기 `⚠️` — `[매체 보도]` — **중**
42. **InfoQ, Spotify paved paths** — https://www.infoq.com/news/2021/03/spotify-paved-paths — **2021-03** — `[매체 보도]` — **중**
43. **Fortune, Why AI is raising worker productivity but not making the economy more efficient** — https://fortune.com/2026/05/27/ai-productivity-internet-boom-solow-paradox/ — **2026-05-27** — `[매체 보도]` — **중**

## D-6. 실무자·벤더 블로그 (신뢰성 중~하 — 보조 자료)

44. **Saviynt, Managing AI Agent Lifecycles: Birth to Retirement** (Vibhuti Sinha) — https://saviynt.com/blog/ai-agent-lifecycle-management — **2026-02-26** — `[벤더 블로그]` — **중**
45. **Platform Engineering, Golden cage syndrome: Why Internal Developer Platforms fail** (Vladimir Mikhalev) — https://platformengineering.org/blog/golden-cage-syndrome-why-internal-developer-platforms-fail — **2026-03-05** — `[커뮤니티]` — **중**
46. **William Harris, Benefit Realization: The Horror Movie of RPA** — https://www.linkedin.com/pulse/benefit-realization-horror-movie-rpa-william-harris — 발행일 미표기 `⚠️` — `[커뮤니티]` — **중**
47. **IT Convergence, FTE in RPA: Measuring ROI on Robotic Process Automation** — https://www.itconvergence.com/blog/robotic-process-automation-rpa-roi/ — 발행일 미표기 `⚠️` — `[벤더 백서]` — **중**
48. **Advanced Systems Concepts, Here's Why RPA Fails** — https://www.advsyscon.com/blog/why-rpa-fails-robotic-process-automation/ — 발행일 미표기 `⚠️` — `[벤더 블로그]` — **중**
49. **NHI Mgmt Group glossary, Agent decommissioning / Access recertification** — https://nhimg.org/glossary/agent-decommissioning/ , https://nhimg.org/glossary/access-recertification/ — 현행 — `[벤더 블로그]` — **중**
50. **TrueFoundry, AI Agents Retire Too: The Decommissioning Playbook** — https://www.truefoundry.com/blog/ai-agent-decommissioning-lifecycle-playbook — 발행일 미표기 `⚠️` — `[벤더 블로그]` — **중**
51. **Slash, How to Classify AI Token Spending in Accounting** — https://www.slash.com/blog/how-to-classify-ai-token-spend — 발행일 미표기 `⚠️` — `[벤더 블로그]` — **중**
52. **EY, Agentic AI Enterprise Token Cost** — https://www.ey.com/en_us/insights/ai/agentic-ai-token-costs — 발행일 미확인 `⚠️` — `[컨설팅 조사]` — **중~최상** (본문 미대조)
53. **InnerSource Commons, Adopting InnerSource: Principles and Case Studies** — https://innersourcecommons.org/learn/books/adopting-innersource-principles-and-case-studies/ — `[학술/커뮤니티]` — **최상**
54. **InnerSource Patterns, Maturity Model** — https://patterns.innersourcecommons.org/p/maturity-model — 현행 — `[커뮤니티]` — **중~최상**
55. **Thoughtworks, Overcoming the platform challenge of low developer adoption** — https://www.thoughtworks.com/insights/blog/platforms/platform-engineering-challenges--a-guide-to-overcoming-an-inadeq/turning-the-tide--overcoming-the-platform-challenge-of-low-devel — 발행일 미표기 `⚠️` — `[컨설팅 조사]` — **중**
56. **People Matters, AI layoffs backfire as 33% of companies lose critical skills** — https://www.peoplematters.in/amp/news/workforce-planning/ai-layoffs-backfire-as-33percent-of-companies-lose-critical-skills-and-expertise-report-48771 — 2026 — `[매체 보도]` — **하** (**원 리포트 미특정 — 수치 인용 금지**)

---

# E. 접근 실패 로그

> **어디를 뒤졌는지가 그 자체로 증거다.**

| # | URL / 대상 | 실패 유형 | 영향 | 대체 조치 |
|---|---|---|---|---|
| 1 | https://www.cnbc.com/2026/02/09/digital-employees-ai-bootcamps-... (BNY) | **HTTP 403** | BNY 2026-02 시점 규모·발언 미확보 | TBPN Digest(CEO 인터뷰)로 대체 |
| 2 | https://www.axios.com/2025/10/17/ai-wall-street-digital-workers | **HTTP 403** | "over 100 digital employees" 본문 미확보 | 검색 스니펫만 사용, `⚠️` 표기 |
| 3 | https://www.finextra.com/newsarticle/46243/... (BNY 이메일) | **HTTP 403** | 이메일 계정 부여 상세 미확보 | CU Today로 대체 |
| 4 | https://www.fastcompany.com/91360855/... (BNY) | **HTTP 403** | — | CU Today로 대체 |
| 5 | https://www.hrgrapevine.com/us/content/article/2025-07-17-bny-mellon-... | **HTTP 403** | 제목("gives AI 'staff' logins & human managers")만 확보 | CU Today로 대체 |
| 6 | **Wall Street Journal** BNY 원 기사 (2025-07) | **유료·미도달** | **BNY 최초 보도 원문 대조 실패** — A-1의 최대 약점 | CU Today의 WSJ 인용으로 대체, `⚠️` 명시 |
| 7 | https://www.gartner.com/en/newsroom/press-releases/2026-05-26-... | **HTTP 403** | 4단계 자율성 프레임 원문 미대조 | **3개 매체 교차 확인**(techedgeai, securitypointbreak, enterprisedna) |
| 8 | https://openai.com/index/bny/ | **HTTP 403** | 벤더 케이스 스터디 미확보 | BNY 공식 페이지로 대체 |
| 9 | https://openai.com/index/klarna/ | **미접근** | — | Klarna 보도자료 원문으로 대체(더 나음) |
| 10 | https://arxiv.org/pdf/2506.12469 (PDF 직접) | **바이너리 추출 실패** | — | Knight Columbia HTML판에서 전문 확보 ✅ |
| 11 | https://dora.dev/dora-report-2025/ | **랜딩 페이지** — 수치 없음 | **DORA 수치 전부 2차 인용 상태** | 리뷰 기사로 보완, fact-checker 재대조 필요 `⚠️` |
| 12 | https://www.microsoft.com/.../microsoft-entra-pricing | **동적 렌더** — 가격 미대조 | $15 / $12 수치 신뢰성 **중** | 문서 소스에서 라이선스 요건만 확정 |
| 13 | https://www.cnbc.com/2026/07/01/employers-who-laid-off-workers... | **HTTP 403** | AI 감원 되돌리기 수치 미검증 | People Matters 2차 인용, **수치 사용 금지** 처리 |
| 14 | **ISO/IEC 42001** 원문 | **유료 표준** | AI 시스템 인벤토리 요구 항목 미확보 | `⚠️ 미확인`으로 남김 |
| 15 | **닛케이 2026-07-09** (AI 비용 회계) — 1차에서 표제만 | **유료** | 본 라운드에서도 미접근 | 영어권 회계 논의로 대체 |
| 16 | Bloomberg Klarna 인터뷰 원문 (2025-05) | **미도달** | CEO "lower quality" 발언 원문 미대조 | Entrepreneur·Forbes·CX Dive **3개 매체 교차** |
| 17 | https://github.com/ombegov/... GitHub 웹 UI | 컬럼명 미노출 | — | **raw.githubusercontent.com의 data_dictionary.md 직접 fetch로 해결** ✅ |

**의도적으로 제외한 소스 유형:**
- 출처 불명 신디케이트 기사 (financialcontent.com, times-online.com의 "BNY 20,000 AI Assistants" 등) — 신뢰성 **하**
- 날짜 없는 SEO 나열형 아티클 (programs.com "List of Companies Announcing AI-Driven Layoffs" 등)
- 1차(`research/web.md`)에서 이미 확보한 항목 전체
- 논문 원문 심층 분석 (paper-researcher 담당) / 커뮤니티 토론 (community-researcher 담당)

---

# F. ⚠️ 미확인 항목 모아보기

> **fact-checker 최우선 대조 목록.** 아래는 등급별로 정리했다.

## F-1. 【사용 금지】 원 출처를 특정하지 못한 수치

| 수치 | 어디서 나왔나 | 왜 금지인가 |
|---|---|---|
| "L0 Observe / L1 Draft / L2 Prepare / L3 Bounded execute / L4 High-autonomy execute" 5단계 | 검색 요약이 "an emerging enterprise framework"라고만 표기 | **Gartner 4단계와 혼동 위험**. 귀속 불가 |
| "Only **20%** of organisations have formal processes for offboarding and revoking API keys" | nhimg.org 용어집 | 조사 주체·표본·연도 전부 미상 |
| "**80%** of DIY platforms fail" | platformengineering.org, hackernoon 반복 인용 | 조사 방법 미공개 |
| "**33%** 핵심 스킬 상실 / **2/3** 재채용 / **55.1%** 재교육 미논의 / **51.3%** 재배치 가능 / **75%** 감원이 절감보다 비쌌다" | People Matters 인용 미상 리포트 | **5개 전부 동일 미상 출처.** 특히 75%는 강한 주장 |
| "전 세계 AI 투자 연 **$500B** 초과" | 검색 요약 | 원자료 미확인 |
| "Spotify Backstage agent-first 전환으로 개발자 오버헤드 **약 47%** 감소 (2026)" | 검색 요약 | 원 출처 미확인 |
| 에이전틱 에이전시 단위경제 ("툴 COGS 3~5%→12~18%", "주니어 정원 30~50% 압축", "60 FTE 구성") | 개인 블로그 | 예시 모델, 실증 아님 |
| "RPA 도입 **30~50%** 실패 — EY 2016" | 2차 인용 | EY 원 리포트 미대조 |
| "Orphaned accounts가 인사이더 침해의 **20%**에 관여" | Saviynt 인포그래픽 | 원자료 미확인 |
| Gartner "2026년 엔터프라이즈 앱의 **40%**가 태스크 특화 AI 에이전트 통합, 2025년 5% 미만에서" | Saviynt 2차 인용 | Gartner 원 보도자료 미대조 |

## F-2. 【조건부 사용 — 표현 주의】

| 항목 | 확인된 것 | 확인 안 된 것 | 권장 표현 |
|---|---|---|---|
| **BNY 식별자** | `user ID, a login, a persona, a name` (CEO 발언) | **사번(employee ID/number)**, HR 시스템 등재 | "사번"이라 쓰지 말 것. "**사용자 ID와 로그인**"으로 |
| **BNY 매니저** | "report to direct managers who review and approve their work" (WSJ 경유) | 인사 시스템상 실제 보고 라인인지 | "**사람 매니저가 붙어 산출물을 검토·승인한다**" 정도로 |
| **BNY 공식성** | CEO·CIO 구두 발언 | **회사 보도자료 원문 없음**. 공식 웹페이지는 "digital employees" 미언급 | "경영진이 밝힌 바에 따르면"을 붙일 것 |
| **Workday ASoR GA** | 2026-02 GA (블로그 제목) | **정확한 일자** | "**2026년 2월**" (일자 없이) |
| **Gartner 4단계** | 등급명·통제 차등·분석가명·예측 (3개 매체 일치) | **Gartner 원문 직접 대조** | "Gartner 보도자료(2026-05-26)에 따르면" |
| **Entra 가격** | 라이선스 **요건**은 공식 문서로 확정 | **$15 / $12 금액** | "**약 $15**", 또는 금액 생략하고 요건만 |
| **DORA 수치 (90%/80%/59%/30%/2시간)** | 결론 문장은 공식 페이지 원문 확보 | **개별 수치는 전부 2차 인용** | 원 리포트 PDF 대조 후 사용. 미대조면 "**약**" |
| **DORA "빨라졌지만 불안정"** | 복수 리뷰가 지적 | **정확한 수치·방향성** | 정성 서술만 |
| **OECD TFP 0.25~0.6%p** | 2차 인용 | 원 문서 직접 대조, **발행일** | 원 문서 확인 후 사용 |
| **Atlanta Fed 2026 전망 3.0%/1.8%** | 2차 인용 | PDF 원문 대조 | 대조 후 사용. **"생산성 역설" 결론 자체는 확정** |
| **Klarna $40M** | 보도자료 원문 = "**estimated**" | **실현 여부** | "**2024년 $40M 이익 개선을 예상한다고 밝혔다**" — 과거 추정임을 명시 |
| **Klarna 700** | 보도자료 = "**equivalent work of** 700 full-time agents" | "700명 대체·해고"는 **보도자료에 없음** | "**700명분의 일에 상당하는 양**" |
| **Accenture "exited" 발언** | 발언 내용 | 시점·원 출처 | 원 출처 확인 후 사용 |
| **Team Topologies** | 2차 요약 | **원저(Skelton & Pais, 2019) 미대조** | 개념만, 원저 확인 권장 |

## F-3. 【공백 — 못 찾은 것】

1. **A-4:** SAP Joule / Google Gemini Enterprise(구 Agentspace) / Atlassian / Slack의 에이전트 신원 부여 기능 — **미확인**
2. **A-5:** SAE J3016을 에이전트에 명시 매핑한 권위 문서 — **미확인**
3. **A-7:** Model Card / System Card 표준 섹션 목록 — **미조사** (papers.md 대조 권장)
4. **A-7:** ISO/IEC 42001 AI 시스템 인벤토리 요구 항목 — **유료 표준, 미접근**
5. **A-6:** **실제 조직이 공개한** 에이전트/NHI 폐기 절차 문서 — **0건** (7개 검색어 + 6개 기업 엔지니어링 블로그 + 공공기관 정책 뒤짐)
6. **B-4:** 대리지표(토큰 사용량·요청 수·도입률) 조작의 **실사례** — **0건** (community-researcher 분담 권장)
7. **B-5:** **에이전트가 한 일을 사람 평가에 반영하는 공개 인사 제도** — **0건**
8. **B-5:** 사람+에이전트 팀의 **성과 귀속(attribution)** 공개 사례 — **0건**
9. **B-5:** 순수한 **무해고 선언(no-layoff pledge)** 공개 사례 — **0건**
10. **B-2:** Klarna $40M의 **사후 검증·공시** — **0건** (단, 이 공백 자체가 발견)
11. **B-3:** SPACE 원논문(ACM Queue 2021) 직접 대조 — **미조사** (papers.md 영역)
12. **C:** DORA AI Capabilities Model 상세 — **미조사**

## F-4. 【논지 조정 권고】 — 저자에게

> **A-6 관련.** "다들 들이는 건 설계하는데 내보내는 건 아무도 설계 안 한다"는 **2026-09 시점에 그대로 쓰면 사실과 어긋난다.**
> Microsoft Entra는 **후원자 퇴사 시 매니저 자동 승계**까지 문서화했고, EU AI Act Annex VIII은 **`recalled` 상태값**을 가졌고, 미 연방 인벤토리는 **`development_stage = Retired`**를 필드로 갖고 있다.
> **조정안:** *"내보내는 절차는 이미 설계돼 있다. 문서 안에. 켜져 있지 않을 뿐이다."*
> 이 조정은 논지를 약화시키지 않는다 — **오히려 1차의 CSA 78%(폐기 정책 없음)와 결합하면 훨씬 날카로워진다: 도구는 준비됐는데 조직이 안 쓴다.**

> **축 3 관련.** Gartner의 "**과잉 제한 → 섀도 개발**"(A-5-①)과 Golden Cage Syndrome의 "**강제 → 우회**"(C-③)는 **동일한 실패 모드**다. 거버넌스(축 1)와 플랫폼(축 3)이 같은 함정을 공유한다는 교차 참조는 이 책의 구조적 논거가 될 수 있다.
