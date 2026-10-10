# 보강 리서치 — 발견·관리·가치로의 이동 (검색: 2026-10-10 기준)

사용자가 제공한 서베이 요약의 공개 출처를 원문으로 대조한 기록. 사내 논의 부분은 제외.
판정: ✅ 원문 확인 / ⚠️ 2차 출처로만 확인 / ❌ 원문과 다름

## 1. 시장 진단 3건

| 출처 | 날짜 | 성격 | 확인된 내용 | 판정 |
|---|---|---|---|---|
| Gartner 보도자료 "Gartner Identifies Six Steps to Manage AI Agent Sprawl" https://www.gartner.com/en/newsroom/press-releases/2026-04-28-gartner-identifies-six-steps-to-manage-artificial-intelligence-agent-sprawl | 2026-04-28 | 컨설팅 보도자료 | 6단계: 거버넌스·정책 / 중앙 인벤토리(AI TRiSM으로 승인·섀도 에이전트 발견·분류) / 신원·권한·수명주기(중복 에이전트 폐기 포함) / 정보 거버넌스 / 행동 모니터링·교정 / 책임 있는 사용 문화. 전망: 2028년 포천 500 평균 15만+ 에이전트(2025년 15개 미만) | ⚠️ 원문 403, 다수 2차 보도 일치 |
| AWS for Industries Blog "Managing AI agent sprawl across business units" (Thoppae·Soni·Dilip) https://aws.amazon.com/blogs/industries/managing-ai-agent-sprawl-across-business-units/ | 2026-07-17 | 벤더 블로그 | 사업부별 사일로 개발 → 중복 기능·공유 시스템 충돌·자격증명 증식·사업부 예산에 숨은 비용. 허브앤스포크(중앙 거버넌스 위원회 + 사업부별 Agent Governance Lead), 8개 기능(레지스트리·신원/접근·가드레일·관측·비용·컴플라이언스/감사·사고 대응·AgentOps), "discover before you build" — 새로 만들기 전 중앙 레지스트리 검색, 위원회의 정기 교차 감사로 중복 통합 | ✅ (본문 "88% of agent pilots stall"은 출처 없음 → 사용 금지) |
| 관련: AWS Agent Registry 프리뷰 | 2026-04-09 | 벤더 발표 | 에이전트·도구·스킬 레지스트리, 클라우드 비종속 | ⚠️ 2차 보도 |
| McKinsey QuantumBlack "Cost versus value: Managing agentic AI system performance" https://www.mckinsey.com/capabilities/quantumblack/our-insights/cost-versus-value-managing-agentic-ai-system-performance | 2026-07-08 | 인터뷰(McKinsey Lari Hämäläinen × Pay-i CEO David Tepper — 측정 도구 벤더) | 생성형 AI는 첫 호출부터 소비 경제(클라우드와 다름), 토큰 단가는 실제 지불액의 척도가 아님, "토큰은 가치가 아니라 청구서", 에이전트 가치 조건 P(성공) > T(검증)/T(직접 수행) | ⚠️ 원문 타임아웃, 요지는 2차 다수 일치. 60%·93% 수치는 별도 보고서 출처 불명확 → 사용 금지 |

## 2. 기업 사례

| 출처 | 날짜 | 성격 | 확인된 내용 | 판정 |
|---|---|---|---|---|
| Microsoft 고객 사례 "Atea builds an enterprise AI agent ecosystem with Microsoft Copilot Studio" https://adoption.microsoft.com/en-us/agent-transformation-stories/atea/ | 2026-07-28 | **벤더 고객 사례** | Atea: 북유럽 IT 서비스, 7개국 8,000+명, 오슬로 본사. Agent Hotel = 사내 포털(발견·게시·요청), Entra ID 로그인 후 국가·역할·보안 그룹 기준 개인화, 프롬프트 라이브러리·스킬 마켓·사례 공유. 소규모 팀 내 공유는 자유, 민감 데이터·업무 핵심 에이전트는 검토 후 전사 마켓 배포. 1만+ 에이전트 생성, 1인 일 약 50분 절감(**자체 보고**). 오케스트레이터 Kate(Copilot Studio, 하위 에이전트 35+, MCP로 CRM·ServiceNow·ERP 연결), "Kate가 아니라 Copilot Chat이 오케스트레이터가 될 것" | ✅ ("AI 기반 Routing"은 원문상 Copilot Chat 오케스트레이션 방향으로 표현할 것) |

## 3. 플랫폼 구현

| 플랫폼 | 출처·날짜 | 확인된 내용 | 판정 |
|---|---|---|---|
| Google Gemini Enterprise Agent Gallery | https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-a2a-agent (갱신 2026-10-09) | 외부 에이전트를 A2A 에이전트 카드(JSON)로 등록, 에이전트는 **원래 호스팅에서 계속 실행**, 사용자는 Agent Gallery에서 이용. **프리뷰(Pre-GA)**. 갤러리 분류: Made by Google / From your organization / Your agents | ✅ 단 "Pinned" 분류는 미확인 |
| Microsoft 365 Copilot Agent Store | https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-agent-store (ms.date 2026-04-17, 갱신 2026-08-18) | 4경로(사전 제작 배포 / Copilot Studio 제작 / 외부 플랫폼 반입 / Agent 365 SDK). 메이커 제출 → 관리 센터 Requests에서 검토 → Publish/Reject → "Built by your org"에 게시, 거절 시 메이커에 통지·재제출. Agent Builder 개인·팀 공유와 조직 카탈로그 경로가 별도 | ✅ |
| SAP AI Agent Hub | LeanIX 블로그 https://www.leanix.net/en/blog/sap-leanix-announces-launch-of-ai-agent-hub-and-key-industry-partnerships (2025-11-04, LeanIX APM 내 GA) / SAP 참조 아키텍처 https://architecture.learning.sap.com/docs/ref-arch/jkg4j2 (갱신 2026-10-01) / Sapphire 2026에서 확대 발표 | SAP·Microsoft(Entra)·Google·AWS·ServiceNow·Databricks 등에서 에이전트·MCP 서버·LLM 자동 발견 → **discovery inbox**에서 골라 인벤토리 등록 → 표준 팩트시트(소유·조직·기술·비즈니스 역량·승인/거버넌스 상태·수명주기·사용 현황). 수명주기 5단계 끝이 Optimize & Decommission. 로컬 에이전트(Claude Code) 발견 프리뷰 | ✅ |

## 4. 원고 반영 시 규칙
- 벤더·컨설팅 출처는 성격을 본문에 밝힌다(2장 에이전트 워싱, 5장 워크데이 명명 계산과 같은 기준).
- 프리뷰 기능은 "프리뷰, 2026년 10월 기준"으로 못 박는다.
- Atea 수치는 [자체 보고] 라벨.
- 사용 금지: AWS 88%, McKinsey 60%·93%(출처 불명확), Google "Pinned".
