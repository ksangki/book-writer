# 구글 기업용 제미나이 에이전트 (Gemini at Work 2026) — 책 반영 검토

검토: 2026-10-11 (orchestrator). 원문 접근: zdnet.co.kr은 이 환경의 네트워크 정책으로 차단 — 저자가 붙여 준 본문으로 검토. 1차 출처(Google Cloud 발표·문서)는 아직 대조하지 못함.

## 출처
- 지디넷코리아 김미정 기자, "이메일 계정 갖춘 AI 동료"…구글, 기업용 제미나이 에이전트 공개, 2026-10-11 09:19 — `[언론]` 2차 보도(테크크런치 등 외신 인용).
- 행사: 구글클라우드 'Gemini at Work 2026'(10월 8일까지). 검색으로 확인된 다른 2차 보도: reworked.co, windowsreport.com, letsdatascience.com (각 에이전트에 고유 신원·제한된 접근·활동 기록, IT가 정한 회사 규칙이 모든 에이전트에 적용, Gemini Enterprise 고객에게 추가 요금 없음, 초기 비공개 프리뷰, 전용 신원·저장소·역할을 갖는 상주 '동료' 에이전트) — 모두 2차, 1차 대조 필요.

## 기사 주장 (원문 표현)
- 에이전트에 "직원처럼 별도 구글 워크스페이스 계정과 이메일 주소가 부여"
- 소속 팀·시간대·"업무 승인권자"·캘린더 파악
- 호출: 태그·이메일·자료 공유·단체 채팅방 추가
- '작업 수신함': 처리 과정·하위 에이전트 업무 배분·요청 기능·코드·진행 상황
- "사람이 아닌 에이전트를 수행 주체로 명시한 감사 기록"
- 연동: Workspace·M365·Slack·Jira·Confluence·BigQuery·Databricks·Postgres·Snowflake, 사내외 MCP 서버
- 모델 자동 선택/사용자 선택, 외부 모델(Claude부터), 오케스트레이션·스마트 라우팅·실시간 지출 한도
- 수치: 제미나이 MAU 10억+, 포천 100 약 90%가 Gemini Enterprise 사용 — `[벤더 자체 발표]`, 2차 보도

## 책과의 연결 (쓸모: 높음)
| 장·소절 | 연결 | 쓰는 방식 |
|---|---|---|
| 6장 「새 신원인가, 있는 신원인가」 | 최대 업무 플랫폼이 "에이전트에 직원처럼 계정·이메일" 쪽을 택함 | 도이체방크·BNY 사번 사례에 이은 '플랫폼 기본값'의 사례. 책의 답(발급은 런타임, 원장은 조직)으로 읽으면: 이 계정을 발급하는 것은 구글이고, 조직이 따로 원장을 갖는지가 질문으로 남는다 |
| 5장 「사번이 하는 일은 귀속이다」 | "에이전트를 수행 주체로 명시한 감사 기록" | 책의 세 항(에이전트가·누구를 대신해·어떤 권한 맥락으로) 중 첫 항이 제품 기본값이 됨. 나머지 두 항이 남는지는 기사에 없음 — 독자가 확인할 질문으로 |
| 7장 「감독자를 세우는 것만으로는…」 | 에이전트가 승인권자를 '파악', 작업 수신함으로 과정 공개 | 승인권자를 아는 것과 승인 관문이 있는 것은 다르다. 공개된 과정은 감독 장치의 재료이지 감독 자체가 아니다 |
| 6장 「청구서를 처음부터…」·「디지털 좌석」 | 실시간 지출 한도·라우팅, (2차) 추가 요금 없음 | 비용 통제가 제품에 들어옴. 좌석 과금 여부는 1차 확인 전 쓰지 않음 |
| 10장 폐기 체크리스트 | 계정·메일함을 가진 에이전트 | 폐기가 키 회수만이 아니라 계정 비활성·메일함·공유 자료 처리까지 됨 — 체크리스트 ①·③ 예시 |
| 9장 | "AI 동료" 프레이밍 | 앞선 monday.com 검토와 같은 축 — '동료' 문장이 구성원에게 어떻게 들리는가 |

## 원문 대조 전 쓰지 말 것
MAU 10억·포천 100 약 90%, "추가 요금 없음", 상주 동료 에이전트의 '역할', 감사 기록의 항목 구성.

## 1차 출처 대조 — 2026-10-11 (orchestrator)
**원문:** Thomas Kurian, "Gemini at Work 2026: Introducing Gemini agent", Google Cloud Blog, 2026-10-08 (`datePublished`) — https://cloud.google.com/blog/products/ai-machine-learning/welcome-to-gemini-at-work-2026 — `[공식]` ★ (원문 직접 열람, 검색: 2026-10-11 기준). 기조연설을 옮긴 글.

**원문에서 확인된 것 (인용):**
- 동료 에이전트: "The agent receives its own Workspace account, including an email address, calendar, Drive, and presence in your company directory." / "A coworker agent acts under its own identity rather than yours, and it sees only what you share with it." / "Coworker agents have dedicated identities including their own @agents.company.com emails, their own persistent storage"
- 하위 에이전트: "a roster of sub-agents — temporary, job-specific agents, each with their own identity"
- 거버넌스 네 질문: "Who is the agent, and what identity does it have? / What is it allowed to do or what permissions is it granted? / What did it do and where can I see what it did? / What should it never touch?"
- 신원: "Every agent gets its own identity, cryptographically attested and governed like an employee, with least-privilege permissions. That identity is stamped into the logs that capture its work"
- 권한: "fine-grained, role-based access permissions, approved by your organization’s security administrators" / 외부 시스템에는 "identity is mapped and propagated through industry standards such as OAuth"
- 감사: "every action Gemini takes is written to an audit trail and attributed to the agent rather than to a person"
- 정책: Agent Sandbox, Agent Gateway("an AI network firewall"), 예 "agents may not open documents classified Need to Know"
- 비용: "Real-time spend caps … if a spend cap is triggered, that project's agent pauses … Because the tracking is per project, companies can charge AI costs back to specific departments."
- 모델: Gemini 계열과 Anthropic Claude 모델을 오케스트레이션, Smart Routing
- 연결: Confluence·Microsoft Office·Teams·Slack·Workspace·Git·Jira·Salesforce·ServiceNow·BigQuery·Databricks·Postgres·Snowflake, MCP 서버, "enterprise tools registry"
- 수치(`[벤더 자체 발표]`): "nearly 90% of the Fortune 100 use Gemini Enterprise", "nearly 80% of all Google Cloud customers are using our AI products"
- 가용성: 산업별(금융·법률) "now in preview"

**지디넷 기사에 있으나 원문에서 확인 안 됨 → 쓰지 않음:** '업무 승인권자' 파악, '작업 수신함', 제미나이 MAU 10억, 테스트 참여사(온·쇼피파이·페이팔), 피차이 인용(blog.google 글에 있을 수 있으나 그 도메인은 이 환경에서 차단).
**국내 보도:** 지디넷코리아 김미정, 2026-10-11 — https://zdnet.co.kr/view/?no=20261010221851 — `[언론]` 2차(외신 인용), 원문 대조 결과 일부 항목 원문에 없음.
