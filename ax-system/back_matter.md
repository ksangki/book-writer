# 부록 A. 워크시트 모음 — 각 장이 남긴 아홉 개의 도구

각 장에서 만든 도구를 순서대로 모았다. 본문의 맥락 없이도 쓸 수 있게 요약했지만, 각 표가 왜 그 모양인지는 해당 장에 있다. 그리고 **앞 칸을 안 채우고 뒤 칸을 채우면 뒤 칸이 헛돈다** — 이 순서 자체가 아홉 번째 도구다.

## A-1. 재고 조사의 관문 다섯 개와 판별 3질문 (2장)

### 관문 다섯 개 — 목록 전체를 훑는 도구

값싼 판정을 앞에, 비싼 판정을 뒤에 놓았다. 순서를 뒤집으면 재고 조사가 큰 프로젝트가 되고, 큰 프로젝트가 되는 순간 다음 분기로 밀린다.

| # | 관문 | 걸러지는 것 | 판정 요령 |
|---|---|---|---|
| ① | 생성형인가 | 규칙 기반 자동화·통계 모델·기존 배치 | 걸러진 것에도 값이 있다는 점을 판정 결과에 적어 둔다 |
| ② | 행위하는가 | 답만 하는 챗봇·초안 도구 | 결과물이 사람의 손을 거치지 않고 다음 단계로 넘어가는가 |
| ③ | 산출물이 실재하는가 | 기획서·미착수·토대 인프라 | 토대 인프라는 별도 목록으로 뺀다 |
| ④ | 조직의 업무인가 | 개인 편의 도구·대고객 제품 | 팀의 업무와 목표에 연결되는가 |
| ⑤ | 무게가 있는가 | — (대상 안에서 강도를 가른다) | 되돌릴 수 없는가, 돈·대외·민감정보에 닿는가 |

**함께 둘 것:** 관문 문구의 변경 이력(언제·무엇을·왜 바꿨는지 한 줄), 판정 보류 칸, 그리고 후보별 **API 가용성 열**(호출 가능 / 부분 / 사람만).

### 판별 3질문 — 실무자가 30초 안에 쓰는 도구

자기가 만든 것 하나를 두고 판단해야 하는 실무자에게는 이 형태가 필요하다. 판정 결과가 통과/탈락이 아니라 **통제의 강도**라는 점이 관문과 다르다.

| | 묻는 것 | 아니라면 |
|---|---|---|
| **전제** | 조직의 업무인가 (팀 목표에 연결되는가) | 대상 아님 |
| **①** | 실제로 행동하는가 (쓰기·발송·처리) | 가볍게 등록만 |
| **②** | 스스로 도는가 (사람은 예외 상황에만 개입) | 보통 등록 |
| **③** | 되돌릴 수 없는 일인가 (돈·대외·민감정보) | 등록 + 모니터링 |
| | 셋 다 그렇다 | **정식 등록 + 강한 통제** (승인 게이트·감사 로그·킬 스위치) |

오른쪽 열의 세 단계는 실체가 달라야 한다. 말만 다르고 처리가 같으면 실무자는 금방 알아채고 대충 답한다.

## A-2. SOP 진단표 (3장)

적힌 절차와 실제로 하는 일을 대조한다. 로그가 없는 조직도 표본 관찰 다섯에서 열 건으로 시작할 수 있다.

| 적힌 단계 | 실제 로그·관찰에서 확인된 단계 | 간극의 성격 |
|---|---|---|
| 문서에 적힌 순서 그대로 | 기록이나 관찰로 확인한 것 | 아래 넷 중 하나 |

| 간극의 성격 | 처방 |
|---|---|
| **누락** — 실제로는 하는데 문서에 없다 | 문서에 추가한다 |
| **순서 역전** — 문서와 실제의 순서가 다르다 | 어느 쪽이 옳은지부터 판정한다 |
| **비공식 우회** — 특정 조건에서 단계를 건너뛴다 | 조건을 명문화하거나 그 단계를 없앤다. 우회 금지는 대개 답이 아니다 |
| **형식화 불가** — 사람의 판단으로만 되는 단계 | 옮기지 않는다. 사람을 남기고 경계로 표시한다 |

**쓰는 법 세 가지:** 적힌 단계를 먼저 채운다 / 한 절차에 실제 사례 다섯에서 열 건을 본다 / 간극 없는 행은 지운다. 그리고 **이 표는 그 일을 직접 하는 사람이 채운다.** 감사 담당자가 채우면 세 번째 유형이 조용히 비고, 그렇게 비어 버린 표는 원래 문서보다 나쁘다.

## A-3. 에이전트 SOP 작성 규칙 체크리스트 (4장)

여섯 항목 중 넷은 절차를 쓰는 사람의 몫이고, 나머지 둘은 유지하는 사람의 몫이다. 그리고 대개 그 둘이 같은 사람이 아니다 — 5번과 6번이 등록부에 들어가야 하는 이유다.

| # | 점검 항목 | 확인 |
|---|---|---|
| 1 | 각 단계의 **산출물 기준**을 못 박았는가 (무엇이 나와야 하고, 어떤 조건을 갖춰야 하는가) | ☐ |
| 2 | 추상적 정의 대신 **짧은 명령형**으로 썼는가 | ☐ |
| 3 | 한 덩어리 대신 **점진적 공개** 구조로 짰는가 ("X 할 때는 Y를 참조하라") | ☐ |
| 4 | **결정론적 검증 지점**이 어디인지 지정했는가 | ☐ |
| 5 | **모델 버전과 성능 기준선**을 기록했는가 | ☐ |
| 6 | **규칙 파일 정리 주기와 회귀 테스트 주기**를 정했는가 | ☐ |

## A-4. 등록 스키마 여덟 칸 (5장)

앞의 일곱은 대체로 순순히 채워지고 여덟 번째가 늘 빈다. **채워지지 않더라도 열은 남겨 둔다** — 빈 열은 부채로 보이지만, 없는 열은 부채라는 사실조차 보이지 않게 만든다.

| # | 항목 | 이 칸이 답하는 질문 |
|---|---|---|
| 1 | 디지털 신원 | 이것을 무엇으로 부르고 무엇으로 식별하는가 |
| 2 | 권한 범위 | 어디까지 접근할 수 있는가 |
| 3 | 데이터 민감도 | 무엇을 다루는가 |
| 4 | 행위 범위 | 무엇을 할 수 있는가 |
| 5 | 사람의 개입 지점 | 어디서 사람이 확인하는가 |
| 6 | 감사와 추적성 | 무엇을 했는지 어떻게 되짚는가 |
| 7 | 업무 연속성 | 담당자가 떠나면 어떻게 되는가 |
| 8 | 재심사와 폐기 기준 | 언제, 어떻게 내보내는가 |

**첫 회차에는 세 칸만 강제한다** — 디지털 신원, 스폰서, 행위 범위. 나머지는 등급이 올라갈 때 붙인다.

**세 역할의 권한 경계:** 오너(기술 관리, 선택) / **스폰서(사업 책임, 필수)** / 매니저(조직 계층, 선택). 스폰서 자리에 추진 조직이나 플랫폼 팀 이름이 들어가면 그 설계는 이미 어긋났다.

**검증 질문 한 줄:** *이 원장을 아무도 업데이트하지 않으면 무슨 일이 벌어지는가?* 답이 "아무 일도 안 벌어진다"라면 그 원장은 이미 죽어 있다.

## A-5. 두 계층 부여 기준 넷 (6장)

1계층(식별자)은 만들어진 전부에게, 2계층(사번)은 기준을 통과한 것에만.

| 기준 | 묻는 것 | 왜 이것이 기준인가 |
|---|---|---|
| 연결 범위 | 다른 시스템이나 다른 에이전트를 호출하는가 | 연결이 늘면 영향 범위가 늘어난다 |
| 접근 권한 | 어떤 데이터와 기능에 닿는가 | 닿는 곳이 곧 사고 시 피해 범위다 |
| 상시 운영 여부 | 일회성 실험인가, 계속 도는 업무인가 | 계속 도는 것에만 유지 비용이 든다 |
| **절차 문서 보유 여부** | 이 에이전트가 수행하는 절차가 글로 적혀 있는가 | 기준선이 없으면 평가가 성립하지 않는다 |

**함께 정할 것:** 등록 단위와 과금 단위를 명시적으로 분리한다. 인턴 단계를 둔다면 기한을 못 박는다. 권한은 사람에게서 위임받는 형태가 기본값이고, 에이전트 자체 권한은 고위험·상시 운영에만 남기는 예외다.

**운영 비용 항목표:**

| 비용 항목 | 언제 발생하는가 | 놓치기 쉬운 이유 |
|---|---|---|
| 인사 데이터와 접근 권한 그룹의 지속 동기화 | 상시 | 초기 구축 비용으로만 잡고 운영비를 안 잡는다 |
| 소유자 이탈 시 자격 증명 교체 | 담당자 퇴사·이동 때마다 | 사람 오프보딩 절차에 이 단계가 없다 |
| 감사 로그 적재와 보관 | 상시 | 저장 비용은 규모에 비례해 늘어난다 |
| 절차 문서의 회귀 테스트 | 모델을 교체할 때마다 | 모델 교체를 비용 이벤트로 보지 않는다 |
| 라이선스 | 2계층 부여 시점부터 | 등록 단위와 좌석 단위를 일치시키면 커진다 |
| 등록·심사 자체의 인건비 | 상시 | 제도 운영에 사람이 든다는 사실을 빼먹는다 |

**판정 형태:** 한 에이전트의 연간 유지 비용이 그 에이전트가 절감한 노동의 가치를 넘으면 그것은 폐기 후보다.

## A-6. 자율성 등급표 초안 (7장)

세로축은 허용 자율성, 가로축은 네 기능, 그리고 각 행에 위협 모델 열을 붙인다. **자율성을 숫자 하나로 적지 않는다**는 것이 이 표의 요점이다.

| 허용 자율성 | 조회 | 해석 | 선택 | 집행 | 위협 모델 | 필요한 통제 |
|---|---|---|---|---|---|---|
| A1 손을 얹고 (직접 실행) | | | | | | |
| A2 지시를 얹고 (지시) | | | | | | |
| A3 눈을 얹고 (감독) | | | | | | |
| A4 마음을 얹고 (목표·제약 설정) | | | | | | |
| A5 마음을 떼고 (정책 설정) | | | | | | |

**채울 때 세 가지:** 등급 판정은 A-1의 판별 3질문이 내놓는 산출로 한다(개인 재량에 두면 판정자마다 갈린다) / **위협 모델 열을 비워 두지 않는다** — 비면 그 행은 이름표일 뿐이다 / **2단계로 시작해도 된다.** 왜 다섯이 필요한지 답하지 못한 채 다섯을 채우는 쪽이 더 나쁘다.

**전제:** 기술 역량과 허용 자율성은 다른 축이다. 두 축이 어긋난 칸은 결함이 아니라 의도된 거버넌스 선택이며, 그 선택을 명시적으로 적는 것이 이 표의 목적이다. 그리고 승인을 등급의 축으로 삼지 않는다 — 승인은 되돌릴 수 없는 소수 행위에만 남기고 나머지는 애초에 닿을 수 없게 만든다.

## A-7. 환산식과 두 계수 (8장)

**환산 두 단:** 에이전트 처리량 → (건당 사람 소요시간) → 사람이 했다면 걸렸을 시간 → (1 FTE의 연간 시간) → FTE 환산값 → (신뢰도 등급) → 인정 FTE → (자율성 계수) → 에이전트 몫 FTE

**세 개의 벽:** 분모가 없다(1 FTE는 연 몇 시간인가 — 인사가 정해야 하고, 정하면 전사가 같은 값을 쓴다) / 분자가 부실하다(건당 기준값. 담당 조직이 적되 **공개**한다) / 실측 인프라가 아직 없다.

**계수 ① 신뢰도**

| 등급 | 근거 | 인정 |
|---|---|---|
| 실측 | 시스템 로그·처리 기록 | 전부 |
| 표본 | 시간일지·직접 관찰 등 표본 실측 | 일부 할인 |
| 자기보고 | 담당자 추정 | 절반 |

자기보고 등급에는 **폐지 시한을 못 박는다.** 시한이 없으면 자기보고는 영구 제도가 된다.

| 가산 조건 | 감산 조건 |
|---|---|
| 구체적 기간 앵커("지난주에 몇 건") | "통상적으로 얼마나" 형태로 묻기 |
| 실측 대조 예정임을 미리 알림 | 원인과 결과를 같은 설문지로 묻기 |
| 실행 당사자가 아닌 제3자 추정 | 그 숫자가 평가·보상에 연동됨 |
| 원인과 결과를 다른 출처에서 받음 | |

**계수 ② 자율성** — 사람이 남아 있는 만큼 계수를 곱하고, 실측이 되면 사람 개입 없이 끝난 비율을 그대로 쓴다.

두 계수는 서로 다른 것을 보정한다. 신뢰도는 *이 숫자를 믿을 수 있나*, 자율성은 *이 중 에이전트 몫이 얼마인가*를 묻는다. 곱해 쓰지만 이중 할인이 아니다.

**규칙 셋:** 모든 수치에 출처 성격 라벨을 붙인다(라벨 없는 숫자는 표에 올리지 않는다) / 과업 수준 이득을 조직 성과로 곱하지 않는다(흐름 전체의 처리 시간을 따로 재고 대조표를 남긴다) / 보상에 거는 지표와 관찰하는 지표를 갈라 둔다. **AI 사용량을 성과 지표로 삼지 않는다.**

## A-8. 사용 제한 선언문 초안과 커뮤니케이션 4원칙 (9장)

> **측정 결과 사용 제한 선언 (초안)**
>
> 1. 이 체계가 산출하는 절감 수치는 개인 또는 조직 단위의 인력 조정 근거로 사용하지 않는다. 적용 기간은 ○○년 ○월까지이며, 연장 여부는 그 시점에 다시 논의한다. **재논의 없이 기한이 지나면 본 선언은 자동 연장된 것으로 본다.**
> 2. 확보된 시간의 기본 용도는 **재투자**다. 다른 용도로 쓰려면 그 결정을 별도 안건으로 공개 논의한다.
> 3. 이 수치는 조직 단위로만 집계하며, 개인별로 분해해 보관하거나 인사 평가에 연동하지 않는다.
> 4. 이 체계는 에이전트의 활동을 기록한다. 구성원 개인의 도구 사용 내역을 수집 대상으로 삼지 않는다.
> 5. 위 항목의 변경은 사전에 고지하며, 소급 적용하지 않는다.

**커뮤니케이션 4원칙 (순서에 뜻이 있다):**

| # | 원칙 | 요점 |
|---|---|---|
| ① | 사전 고지 | 발견당하지 않게 한다. 알리는 시점이 늦어질수록 같은 설명이 더 비싸진다 |
| ② | 수집 범위 명시 | **무엇을 안 보는지를 함께 적는다.** 안 보는 것의 목록이 없으면 명시되지 않은 전부를 본다고 가정한다 |
| ③ | 당사자 이익과 연결 | 성과 귀속이 그 자리다. ①②를 건너뛰고 ③으로 시작하면 홍보로 들린다 |
| ④ | 폐기 규칙의 존재를 함께 고지 | 정리의 대상이 에이전트임을 제도로 보인다. 아직 없으면 "만들고 있고 언제까지 공개한다"까지만 말한다 |

**금지 어휘:** "잡아낸다." 말하는 쪽에서는 탐지 기능을 가리키는 중립적 표현이지만, 듣는 쪽에서는 자기가 잡히는 대상이라는 뜻으로 들린다.

**실행 원칙:** 사용자에게 아주 작은 수정 권한이라도 준다(단, **수정 가능 구간과 책임 귀속은 별도 필드로 둔다**) / 에이전트의 오류율을 사람의 오류율과 나란히 공개한다 / 롤아웃은 효과가 큰 집단부터 / 문화 슬로건보다 개인 수준의 작업에 투자한다 / 중간관리자를 최우선 대상으로 / 첫 단계는 실무자 교육이 아니라 리더의 자기 규율.

## A-9. 폐기 체크리스트 7항목 (10장)

**폐기 시점에 이 표를 꺼내면 늦다.** 등록 시점에 초안을 채우고 운영 중에 갱신하는 문서다.

| # | 항목 | 확인할 것 |
|---|---|---|
| ① | 공식 폐기 워크플로 | 승인 절차를 포함하는가. 누가 요청하고 누가 승인하는가 |
| ② | 자격 증명·토큰 즉시 폐기 | API 키·인증서·OAuth 토큰이 전부 목록에 있는가 |
| ③ | 아웃바운드 접근 제거 | 이 에이전트가 호출하던 연동과 도구 권한 |
| ④ | 인바운드 호출 차단 | 이 에이전트를 부르던 엔드포인트·웹훅·큐 |
| ⑤ | 메모리·데이터 정화 | 보관할 것, 익명화할 것, 안전 삭제할 것을 구분했는가 |
| ⑥ | 감사 추적 보존 | 불변 로깅. **지우지 않고 남기는 유일한 항목** |
| ⑦ | 폐기 후 잔여 리스크 모니터링 | 끈 뒤에도 한동안 본다. 기간을 숫자로 정한다 |

**용어 구분:** 취소(활성 세션 종료) ≠ 디프로비저닝(신원과 권한의 영구 제거). 취소만 된 에이전트는 등록과 신뢰 관계를 그대로 보유한다.

**재심사는 사건에 건다 (분기 재심사가 아니다):** 권한 크립 탐지 / 접근 패턴 드리프트 / 새 역량 획득 시 소유자 재확인.

**그리고 이것이 이 아홉 개 도구 전체의 마지막 규칙이다** — 폐기 절차를 사람이 지키는 규칙으로 만들지 말고, **발급 구조에 만료를 내장한다.** 기본값이 소멸이면 방치는 정리와 같은 결과를 낳는다.

---

# 부록 B. 참고문헌

본문 저술에 실제로 근거로 쓴 것만 추렸다. 축별로 묶고, 각 항목에 **출처 성격**과 **확인 등급**을 붙였다.

**확인 등급:** ★ 원문 직접 열람 / △ 검색 요약·2차 자료 경유 / ✗ 접근 실패
**문헌 유형:** `[PR]` 동료평가 논문 / `[PP]` 프리프린트 / `[WP]` 워킹페이퍼·워크숍 논문(정식 학회 논문 아님) / `[공식]` 공식 문서·보도자료 / `[규제]` 규제 원문 / `[정부]` 정부 공개 자료 / `[조사]` 컨설팅·업계 조사 / `[벤더]` 벤더 자료 / `[매체]` 언론 보도 / `[커뮤니티]` 커뮤니티 게시물 / `[학술]` 학술 기관·연구소 발간물 / `[보고서]`·`[기술보고서]` 기관 보고서 / `[문헌]` 저자·연도가 특정되지 않은 2차 문헌 / `[PR-단행본]` 동료평가 계열 단행본 / `[PP→PR]`·`[PP→워크숍]` 프리프린트에서 게재·워크숍으로 이행

웹 자료의 접근일은 모두 **2026년 9월 5일**이다. 이 영역은 분기 단위로 바뀌므로, 규제·제품·표준 항목은 인용 시점에 원문을 다시 확인하는 편이 낫다.

## B-1. 등록·아이덴티티 — 1차 자료와 제품

| 자료 | 출처 | 유형 | 확인 |
|---|---|---|---|
| Deutsche Bank's Corporate Bank onboards its first digital employee (2020-07-20) | db.com | `[공식]` | ★ |
| Administrative relationships in Microsoft Entra Agent ID — Owners, sponsors, managers (2026-04-16, 갱신 2026-09-03) | learn.microsoft.com | `[공식]` | ★ |
| What's new in Microsoft Entra Agent ID (2026-05-01, 갱신 2026-08-13) | learn.microsoft.com | `[공식]` | ★ |
| Microsoft Entra ID Governance — 에이전트 수명주기·접근 패키지 만료 (2026-06 기준) | learn.microsoft.com | `[공식]` | ★ |
| Microsoft Agent 365 (제품 페이지, 2026) | microsoft.com | `[공식]` | ★ |
| Workday Agent System of Record (2025-02-11 발표 → 2026-02 정식 출시) | workday.com | `[공식]` | △ |
| Okta brings first-class identity to AI agents with Agent SSO (2026-08-24) | okta.com | `[공식]` | ★ |
| Okta introduces Cross App Access (2025-06-23) | okta.com | `[공식]` | △ |
| Saviynt — 에이전트 아이덴티티 6단계 라이프사이클 (2026-02) | saviynt.com | `[벤더]` | △ |
| SailPoint Agentic Fabric (2026-05-11) | sailpoint.com | `[공식]` | △ |
| CyberArk Secure AI Agents (2025 말) | cyberark.com | `[공식]` | △ |
| The Non-Human Identity Governance Vacuum (CSA 백서, 2026-05-20) | cloudsecurityalliance.org | `[조사]` | ★(랜딩) / ✗(PDF) |
| Agent Identity Governance Framework v1 (CSA, 2026) | cloudsecurityalliance.org | `[조사]` | △ |
| CSA 자율성 등급 L0~L5 (2026-01-28) | cloudsecurityalliance.org | `[조사]` | △ |
| Lattice scraps plans to treat AI bots as employees (2024-07) | SHRM | `[매체]` | △ |
| Lattice / AI workers (2024-07-12) | Fortune | `[매체]` | △ |
| AGENTS.md 규약 (2025-08~) | agents.md | `[공식]` | △ |
| MCP Authorization 스펙 (2025-11-25 판) | modelcontextprotocol.io | `[공식]` | △ |
| MCP SEP-2817 — 감사 로그 이중 구조 제안 (2026-05, 제안 단계) | GitHub | `[커뮤니티]` | △ |
| Atuin Desktop — 실행 가능한 런북 (2025-04) | atuin.sh | `[공식]` | △ |
| Celonis AgentC (2024-10-23) / Agent Mining (2026-05) | celonis.com | `[공식]` | △ |

## B-2. 제도·규제

| 자료 | 출처 | 유형 | 확인 |
|---|---|---|---|
| EU AI Act Article 49: Registration (Reg. (EU) 2024/1689) | artificialintelligenceact.eu | `[규제]` | ★ |
| EU AI Act Annex VIII — 13항목, 상태 값 `recalled`·`no longer available` | artificialintelligenceact.eu | `[규제]` | △ |
| Article 71: EU database for high-risk AI systems | ai-act-service-desk.ec.europa.eu | `[규제]` | △ |
| EU AI Act Omnibus Agreement — Postponed High-Risk Deadlines (2026-05-27) | Gibson Dunn | `[매체]` | ★ |
| 「인공지능 발전과 신뢰 기반 조성 등에 관한 기본법」 (2026-01-22 시행) — 시행일·의무 주체 범위·계도 기간 | 국내 법무법인 해설 자료 | `[규제]` | △ |
| OMB M-25-21 — 연방 AI 활용 사례 인벤토리 지침 (2025-04-03) | 미 예산관리국 | `[정부]` | △ |
| 2025 Federal Agency AI Use Case Inventory (원자료, 56개 기관 3,611건, 36필드) | GitHub / ombegov | `[정부]` | △ |
| 중국 알고리즘 등록제·생성형 AI 서비스 관리 잠행 조치 (2023) — `지정 책임자` 공개 요구 | 중국 국무원 신문판공실 / AppInChina | `[규제]` | △ |
| NIST AI Risk Management Framework (2023-01) — GOVERN/MAP, `named risk acceptance` | NIST | `[공식]` | △ |
| NIST AI RMF to ISO/IEC 42001 Crosswalk | NIST AIRC | `[공식]` | △ |
| ISO 9001:2015 — 문서화된 정보의 통제·가용성 | ISO / 해설 자료 | `[공식]` | △ |
| 자율주행 국제 표준 — 인계 "충분한 시간" 미규정, 수용성 정의 | 표준 원문 및 해설 | `[공식]` | △ |

## B-3. 학술 문헌

### 등록·거버넌스·책임

1. Hübner, J. F., Sichman, J. S., & Boissier, O. (2002). A Model for the Structural, Functional, and Deontic Specification of Organizations in Multiagent Systems (MOISE+). *SBIA 2002*, LNAI 2507. Springer. `[PR]` △
2. Mitchell, M. et al. (2019). Model Cards for Model Reporting. *FAT\* '19*. arXiv:1810.03993. `[PR]` △
3. Santoni de Sio, F., & Mecacci, G. (2021). Four Responsibility Gaps with Artificial Intelligence. *Philosophy & Technology*, 34(4), 1057–1084. `[PR]` △
4. Chan, A. et al. (2024). Visibility into AI Agents. *ACM FAccT '24*. arXiv:2401.13138. `[PR]` △
5. Chan, A. (2024). IDs for AI Systems. arXiv:2406.12137. `[PP]` △
6. Kolt, N. (2025). Governing AI Agents. *Notre Dame Law Review* (게재 예정). arXiv:2501.07913. `[PP→PR]` △
7. Chan, A. et al. (2025). Infrastructure for AI Agents. *TMLR*. arXiv:2501.10114. `[PR]` △
8. Kraprayoon, J. et al. / IAPS (2025). AI Agent Governance: A Field Guide. arXiv:2505.21808. `[보고서]` △
9. Kaptein, M., Khan, V.-J., & Podstavnychy, A. (2026). Runtime Governance for AI Agents: Policies on Paths. arXiv:2603.16586. `[PP]` △
10. Nian, Y. et al. (2026). Auditable Agents. arXiv:2604.05485 (v2 2026-08-13). `[PP]` △
11. Otsuka, T., Toyoda, K., & Leung, A. (2026). AI Identity: Standards, Gaps, and Research Directions for AI Agents. arXiv:2604.23280. `[PP]` △
12. Atkinson, D. I., & O'Bryan, J. E. (2026). Government AI Use as a Monitoring Primitive. arXiv:2607.04543. ICML 2026 Workshop on Technical AI Governance. `[PP→워크숍]` △
13. Feng, K., McDonald, N., & Zhang, A. X. (2025). 자율성 등급과 자율성 인증서 (컬럼비아 나이트 제1수정헌법 연구소, 2025-07-28). `[학술]` △

### SOP·절차의 형식화

14. Adler, P. S., & Borys, B. (1996). Two Types of Bureaucracy: Enabling and Coercive. *Administrative Science Quarterly*, 41(1), 61–89. `[PR]` △ — 원문은 OCR 판독본이다. 4대 특성의 개별 정의문은 미확보이므로, 이 책이 이 논문에 귀속시킨 것은 "두 유형이 있다"는 구분까지다. 본문 1장이 인용한 enabling 형식화의 정의문은 아래 14-1의 p.296에서 왔다.
14-1. Ahrens, T., & Chapman, C. S. (2004). Accounting for Flexibility and Efficiency: A Field Study of Management Control Systems in a Restaurant Chain. *Contemporary Accounting Research*, 21(2), 271–301. `[PR]` △ — 애들러·보리스의 구분을 관리통제 연구로 옮긴 첫 연구다. 본문 1장이 인용한 enabling 사용의 정의문(p.296)의 근접 출처이며, 그 한 줄은 2차 문헌(Mamat 2012, Warwick 리포지토리) 경유로 확보했으며, 원문은 "attempts to mobilize local knowledge and experience in support of central objectives"다. 초록에는 네 설계 원리(repair·internal transparency·global transparency·flexibility)의 이름이 나열되나 개별 정의문은 미확보이므로, 이 책은 설계 특성까지 들어가지 않았다.
15. Nonaka, I. (1994). A Dynamic Theory of Organizational Knowledge Creation. *Organization Science*, 5(1), 14–37. `[PR]` △
16. Feldman, M. S., & Pentland, B. T. (2003). Reconceptualizing Organizational Routines as a Source of Flexibility and Change. *Administrative Science Quarterly*, 48(1), 94–118. `[PR]` △
17. Gourlay, S. (2006). Conceptualizing Knowledge Creation: A Critique of Nonaka's Theory. *Journal of Management Studies*, 43(7), 1415–1436. `[PR]` △
18. van der Aalst, W. M. P. (2011 / 2016). *Process Mining: Discovery, Conformance and Enhancement of Business Processes*. Springer. `[PR-단행본]` △
19. Hong, S. et al. (2024). MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework. *ICLR 2024 (Oral)*. arXiv:2308.00352. `[PR]` △
20. Nandi, S. et al. (2025/2026). SOP-Bench: Complex Industrial SOPs for Evaluating LLM Agents. arXiv:2506.08119 (v2 2026-02-23). `[PP]` △ — 2026년 2월 시점 모델 라인업 기준
21. Amazon Science (2025). Structuring the Unstructured: A Multi-Agent LLM Framework for Transforming Ambiguous SOPs into Code. *EMNLP 2025 Industry Track*. `[PR]` △ — 종단 정확도 수치는 원문 대조 미완이므로 이 책은 쓰지 않았다
22. 도요타 생산방식의 표준작업(standardized work)과 개선 사이클 | 린 생산 문헌 | `[문헌]` △

### 조직 경제학·생산성 실증

23. Klein, K. J., & Sorra, J. S. (1996). The Challenge of Innovation Implementation. *Academy of Management Review*, 21(4), 1055–1080. `[PR]` △
24. Brynjolfsson, E., Hitt, L. M., & Yang, S. (2002). Intangible Assets: Computers and Organizational Capital. *Brookings Papers on Economic Activity*, 2002(1). `[PR]` △
25. Brynjolfsson, E., Rock, D., & Syverson (2017). Artificial Intelligence and the Modern Productivity Paradox. *NBER WP 24001* `[WP]` / (2021) The Productivity J-Curve. *AEJ: Macroeconomics* `[PR]` △
26. McElheran, K. et al. (2024). AI Adoption in America: Who, What, and Where. *Journal of Economics & Management Strategy*, 33(2), 375–415. `[PR]` △ — 2018년 데이터
27. Bick, A., Blandin, A., & Deming, D. J. (2024). The Rapid Adoption of Generative AI. *NBER WP 32966*. `[WP]` △ — 자기보고 기반, 정식 게재본 아님
28. Brynjolfsson, E., Li, D., & Raymond, L. (2025). Generative AI at Work. *Quarterly Journal of Economics*, 140(2), 889–942. `[PR]` △ — GPT-3.5 세대
29. Dell'Acqua, F. et al. (2025). Navigating the Jagged Technological Frontier. *Organization Science*. HBS WP 24-013. `[PR]` △ — 2023년 GPT-4 세대
30. Cui, Z. (K.) et al. (2025). The Effects of Generative AI on High-Skilled Work. *Management Science*. `[PR]` △
31. METR (2025). Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity. arXiv:2507.09089. `[PP]` △ — 표본 16명. 같은 팀의 2026-02 후속과 반드시 병기
32. Dillon, E. et al. (2025). 대규모 현장 실험(n=7,137) — 이메일 시간 −31%, 회의 시간 변화 없음. *NBER 워킹페이퍼* 33795. `[WP]` △
33. Demirer, M. et al. (2026). 개발 도구 효과의 산출물 감쇠와 대체탄력성 0.25. *NBER 워킹페이퍼* 35275. `[WP]` △
34. Vaccaro, M., Almaatouq, A., & Malone, T. (2024). When combinations of humans and AI are useful: A systematic review and meta-analysis. *Nature Human Behaviour*, 8(12). `[PR]` △ — 2020-01~2023-06 게재 논문 대상. 인용 시 기준선 병기·이질성 명시 필수
35. Hemmer, P. et al. (연도 미확인). 인간-AI 팀의 정보 비대칭 조건. `[PP]` △ — 게재 여부 미확인
36. Bessen, J. (2015-03). 현금인출기와 창구직, 19세기 역직기 사례. IMF *Finance & Development* 2015년 3월호 기고문. `[문헌]` △ — 창구직원 총수의 절대 수치는 이 기고문에 없다
37. Goodhart, C. (1975) 원문 / Strathern, M. (1997). *European Review*, 5(3), 305–321. `[PR]` △ — "지표가 목표가 되면"의 정식화는 Strathern이며 경구는 p.308
38. Manheim, D., & Garrabrant, S. (2018). Categorizing Variants of Goodhart's Law. arXiv:1803.04585. `[PP]` △
39. Bevan, G., & Hood, C. (2006). 영국 공공 부문 지표 게이밍 — 공식 통계 96% vs 환자 설문 77%, 별점-품질 상관 0. `[PR]` △
40. Mabe, P. A., & West, S. G. (1982). 자기평가와 실제 수행의 상관 r = .29, 측정 조건이 변동의 64% 설명. `[PR]` △
41. Podsakoff, P. M. et al. (2012). 동일 설문 응답에서 상관 133~304% 팽창. `[PR]` △ — 133~304%는 2012년판 수치다. 2003년판이 정본이나 이 책이 인용한 값의 판본은 2012년이다

### 자율성 등급·감독·자동화 편향

42. Bainbridge, L. (1983). Ironies of Automation. *Automatica*, 19(6). `[PR]` △
43. Sheridan, T. B., & Verplank, W. L. (1970년대 후반). 10단계 자동화 등급. `[기술보고서]` △ — 재수록본 경유. 발표 연도 귀속이 자료마다 갈린다
44. Endsley, M. R., & Kaber, D. B. (1999). Level of automation effects on performance. *Ergonomics*. `[PR]` △ — 10단계 × 4기능 배분표
45. Skitka, L. J., Mosier, K. L., & Burdick, M. (1999). Does automation bias decision-making? *IJHCS*, 51(5), 991–1006. `[PR]` △ — 항공 시뮬레이션
46. Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). A model for types and levels of human interaction with automation. *IEEE Transactions on Systems, Man, and Cybernetics*. `[PR]` ★(초록) — 이론 정리 논문이며 원저 실증 데이터는 없다
47. Merat, N. et al. (2014). 제어 안정화까지 35~40초. `[PR]` △
48. Eriksson, A., & Stanton, N. A. (2017). 인계 시간 1.97~25.75초. `[PR]` △
49. Endsley, M. R. (2017). *Human Factors*. 자율성-상황인식 딜레마. `[PR]` △
50. Victor, T. W. et al. (2018). 테스트트랙 106명, 76명 중 21명(28%) 충돌. `[PR]` △ — 자율주행 맥락
51. Zhang, B. et al. (2019). 129편 메타분석, 평균 2.72초(0.69~19.79초). `[PR]` △
52. Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To Trust or to Think — 인지적 강제 기능. *PACM HCI*, 5(CSCW1). `[PR]` △ — 효과 크기 미확보, 방향만 인용
53. Bansal, G. et al. (2021). Does the Whole Exceed its Parts? *CHI '21*. `[PR]` △ — 그림 수치 인용 금지 대상. 방향성과 본문 z/p값만 사용
54. Green, B. (2022). The flaws of policies requiring human oversight of government algorithms. *Computer Law & Security Review*, 45. arXiv:2109.05067. `[PR]` △ — 정책 41개 조사
55. Laux, J. (2023). Institutionalised distrust and human oversight of artificial intelligence. *AI & Society*. `[PR]` △ — 구성적 vs 교정적 개입
56. Cihon, P., Stein, M., Bansal, G., Manning, S., & Xu, K. (2025). Measuring AI agent autonomy: Towards a scalable approach with code inspection. arXiv:2502.15212. NeurIPS SoLaR Workshop 2024. `[WP]`(워크숍 논문) △ — AutoGen 애플리케이션 10건, 코드 정적 검사. Actions κ = 0.30
57. Zheng, Dong, Depena, Bhatia, Xiao, & Xu (2026-07-26). Separating Capability from Permission: A Governance Framework for Agentic AI Autonomy Levels. arXiv:2607.23438v1. ExxonMobil 기술 조직. `[PP]` △ — AAL/ACL 2축 프레임. 동료심사 없음. 10페이지 산업 실무 보고, 실증 사례 단일 기업 2건
58. 미 도로교통안전국 결함조사 (2백만 대, 467건 충돌) / 국가교통안전위원회 개별 사고조사 2건 (2024) | `[정부]` △

### 변화관리·수용·저항

59. Hughes, M. (2011). Do 70 Per Cent of All Organizational Change Initiatives Really Fail? *Journal of Change Management*, 11(4), 451–464. `[PR]` △ — 이 책이 "70%" 수치를 쓰지 않는 근거
60. Dietvorst, B. J., Simmons, J. P., & Massey, C. (2015). Algorithm Aversion. *JEP: General*, 144(1), 114–126. `[PR]` △
61. Dietvorst, B. J. et al. (2018). Overcoming Algorithm Aversion. *Management Science*, 64(3), 1155–1170. `[PR]` △ — 아주 작은 수정 권한의 효과
62. Kellogg, K. C., Valentine, M. A., & Christin, A. (2020). Algorithms at Work: The New Contested Terrain of Control. *Academy of Management Annals*, 14(1), 366–410. `[PR]` ★ — 알고리즘 통제의 여섯 기제
63. Ravid, D. M. et al. (2023). A meta-analysis of the effects of electronic performance monitoring on work outcomes. *Personnel Psychology*. `[PR]` △ — 사람 모니터링 연구이며 에이전트 로깅 연구가 아니다
64. Shonhe, L., & Min, Q. (2025). Mitigating AI-induced professional identity threat and fostering adoption in the workplace. *AI & Society*, 40(5), 4079–4092. `[PR]` △ — 동·남부 아프리카 단일 직군 413명, 자기보고 횡단 연구

## B-4. 조사 보고서·산업 자료

| 자료 | 출처 | 유형 | 확인 |
|---|---|---|---|
| Gartner — 에이전트 워싱, 수천 벤더 중 약 130개 (2025-06-25) | Gartner 보도자료 | `[조사]` | ✗(403) / 복수 매체 교차 △ |
| Gartner — 비례적 거버넌스 4단계, 이분법 진단, 2027년 40% 강등·폐기 전망 (2026-05-26) | Gartner 보도자료 | `[조사]` | ✗ / 복수 매체 교차 △ |
| Agentic AI is scaling faster than guardrails — 24개국 3,235명, 사용 23% vs 성숙한 거버넌스 21% (2026-04-24) | Deloitte Insights | `[조사]` | ★ |
| The GenAI Divide: State of AI in Business 2025 — 파일럿 5% (2025-07) | MIT 프로젝트 NANDA | `[조사]` | △ — 편의표본(4개 컨퍼런스 참석 시니어 리더), 공식 원문 미확보 |
| The State of AI: Global Survey 2026 — 개인 생산성 8/10, EBIT 기여 37% 정체 | McKinsey | `[조사]` | ✗(타임아웃) / 2차 △ |
| State of AI-assisted Software Development 2025 — "AI는 증폭기다", 버전 관리·관측성·내부 플랫폼 | Google Cloud DORA | `[조사]` | △ |
| Salesforce 에이전트 성숙도 모델 5단계 (2025-04-10) | Salesforce | `[벤더]` | △ |
| Netflix — paved path / 플랫폼 엔지니어링의 golden path | 공개 발표·기술 문헌 | `[문헌]` | △ |
| Golden Cage 증후군 (2026-03) | 플랫폼 엔지니어링 계열 글 | `[커뮤니티]` | △ — 조사 수치는 인용하지 않았다 |
| RPA 시대의 FTE 환산식과 그 비판 (라이선스 1개 = 3 FTE ↔ 실무 1:1도 어렵다 / 생산 가능 시간 5.5~8시간, 연 200~255일) | 벤더·업계 문헌 | `[벤더]`·`[문헌]` | △ |
| 에이전트 KPI 지표군 제안 (과업 성공률·완료 시간·사람 개입률·완료 건당 비용) | 복수 벤더 문헌 | `[벤더]` | △ — 실제 운영 조직의 공개 사례는 확보하지 못했다 |
| Anthropic — 권한 승인 프롬프트 승인률 약 93% (2026-05-25) / 샌드박싱으로 프롬프트 84% 감소 (2025-10-20) | Anthropic 엔지니어링 포스트 | `[벤더]` | △ — 벤더 자체 계측 |
| Klarna — 700명분의 일에 상당하는 양, 예상 이익 개선 (2024-02) | Klarna 보도자료 | `[공식]` | △ — 사후 검증 공시는 확보하지 못했다 |
| Klarna — 이듬해 품질 문제로 재채용 | 복수 매체 교차 보도 | `[매체]` | △ |
| Salesforce — 고객 지원 인력 축소 발언 ↔ 공식 성명의 결원 미충원 설명 (2025-09) | 매체 보도 | `[매체]` | △ |
| BNY — 백 개 이상의 "디지털 직원", 사용자 ID·로그인·이름·페르소나 (2026) | 경영진 인터뷰 매체 보도 | `[매체]` | △ — 회사 보도자료 원문 없음. "사번"이라는 표현은 확인되지 않았다 |

## B-5. 커뮤니티 — 인용한 게시물

이 책이 인용한 커뮤니티 발언은 모두 **개인의 공개 발언이며 조사 데이터가 아니다.** 게시일을 개별로 밝혔고, 단일 게시물을 업계 관행으로 승격시키지 않았다. GeekNews 게시물의 상대 표기 시점은 **2026년 9월 5일 조회 기준 추정**이다.

| 인용 | 출처 | 게시일 | 쓰인 장 |
|---|---|---|---|
| "AX 추진팀이 나쁘다기 보다는.. AX팀을 만들어놓고 …도메인 현업자가 주도하고 AX기술자가 서포트하면서…" | GeekNews `snisty`, 토픽 「AX팀을 만드는 순간, 당신의 조직은 AX에 실패한다」 | 토픽 2026-04-09 / 댓글 ≈2026-04 (2026-09-05 조회) | **서문** |
| "mandates happened and now I'm being forced to use them. Absolutely no guidance from leadership though." | Hacker News `ares623` | 2026-03-06 | 1장 |
| "Confluence is where documentation goes to die. And then rot." | Hacker News `EdwardDiego` | 2020-07-12 | 3장 |
| 같은 게시판의 반복 증언 4건 (검색 불가·페이지 미발견·지연·불만) | Hacker News, 서로 다른 사용자 | 2019-03 / 2022-02 / 2023-08 / 2024-02 | 3장 |
| "When I get an LLM-generated doc or runbook, my first thought is that its very possible that I'm the first person who has ever read this." | Hacker News `backlava12` | 2026-08-11 | 3장 |
| AI 원샷 문서 생성 비판 — 검증 패스 복수 필요 | Hacker News, 익명 | 2026-07 | 3·4장 |
| "Claude Code doesn't validate it - it just silently ignores the skill." | 개발자 커뮤니티, 익명 | 2026-02 | 4장 |
| 긴 규칙 파일이 "잘해야 불필요하고 자주 실제로 해롭다" / 반대 증언(잘 유지된 규칙 파일이 자동 메모리보다 낫다) | 개발자 커뮤니티, 익명 | 2026-08 말 | 4장 |
| "95% is running the verification deterministically." | 개발자 커뮤니티, 익명 | 2026-08 | 4장 |
| 규칙 파일 부패·모델 교체 시 하네스 파손 / RPA의 깨지기 쉬움과 유지보수 손익 역전 | 개발자 커뮤니티, 익명 | 2026-07~08 | 4·6장 |
| "Wtf? We have been calling these workload identities for years" | Hacker News `zingababba` | 2025-02-04 | 5장 |
| 프로세스가 "그 사용자로서" 도는 발상이 지금의 난장판의 일부다 | 개발자 커뮤니티, 익명 | 2025-09 | 5장 |
| 인벤토리 대시보드를 만들었는데 방치를 막지 못했고 대시보드 자체도 방치됐다 | 개발자 커뮤니티, 익명 | 2025-05 | 5장 |
| "Client-asserted context with no signed execution record is unverifiable. A signed execution record with no intent context is hard to interpret." | MCP SEP-2817 `vaaraio` | 2026-05-29 | 5·9장 |
| "…invent some kind of digital seats so they can keep taxing the headcount." | 해외 기술 커뮤니티, 익명 | 2026-04 | 6장 |
| "So every time we fire or lay off the person whose name is on the automation, we need to rotate the keys?" | Hacker News `collabs` | 2026-04-25 | 6장 |
| "…watching the org chart explode…" (하루 반 만에 역할 20개) | Hacker News `yego` | 2026-03-04 | 6장 |
| "Pretty pleaser please people don't get your agents registered as direct-reports in the org-chart with HR!" | Hacker News `polotics` | 2026-09-04 | 6장 |
| 사람이 루프에 없는 인가에 확립된 표준이 없다 (자체 방식으로 해결) | 개발자 공개 기록, 익명 | 2026 | 6장 |
| "사용자에게 승인이나 거부를 묻는 방식은 무엇이든 터지기를 기다리는 재앙이다" / "보안은 환경에 속한다, 하네스가 아니라" | 개발자 커뮤니티, 익명 | 2026-07 | 7장 |
| 채택된 등급 수가 2로 수렴한다는 관찰 | 개발자 커뮤니티, 익명 | 2026 | 7장 |
| "'절감 시간' 사업 케이스대로 실현된 자동화 프로그램은… 1만 시간은 직원 2만 명에게서 각각 30분씩이다" | 자동화 업계 실무자 William Harris, LinkedIn Pulse 서명 글 | 게시일 미확인 | 8장 |
| "aimless tokenmaxing" — 토큰 리더보드 게이밍 | Hacker News `827a` | 2026-05-22 | 8장 |
| "AI 사용량 자체를 성과 지표로 삼으면 사람들은 필요하지 않은 작업에도 AI를 사용해 숫자를 맞추게 될 수 있음" | GeekNews `brainer` | ≈2026-08-31 | 1·8장 |
| "At my company people always understate the headcount savings… 'You estimated 40 FTE savings, why don't we pick and chose 40 FTEs to let go'." | 해외 기술 커뮤니티, 익명 | 2025-10 | 9장 |
| "개발자가 먼저 나서서 미친 생산성을 보여줬기에… 관리자는 더 미친 생산성을 바랄 뿐입니다." | GeekNews, 한국어 게시물 | ≈2026-05 | 9장 |
| "엑셀이 나와서 바뀐 것의 핵심은… 일을 실시간으로 그리고 항시적으로 만든거죠." | GeekNews, 한국어 게시물 | ≈2025-05 | 9장 |
| "일단 회사에서 AI 서비스를 지원 거의 안해주네요…" | GeekNews `akapwhd` | ≈2026-05 | 2장 |
| "직원이 민감한 데이터를 ChatGPT에 붙여넣는 걸 잡아내는(catching) 거죠" | 개발자 커뮤니티, 익명 | 2026-07-01 | 2장 |
| "…700명을 대체한 AI를 가졌다고 주장하면서… 듣는 쪽이 월가라면…" | 해외 기술 커뮤니티, 익명 | 2024-02 | 9장 |
| "all your prompts are tracked and easily viewable by whoever oversees it at your company" | Hacker News `smrtinsert` | 2026-03-29 | 9장 |
| "You work the same hours, but you're more tired, and the company pockets the profits" | Hacker News `pron` | 2026-03-28 | 9장 |
| "예전에는 구현 속도가 병목이었는데, 이제는 생각과 아이디어만이 한계다" | 개발자 커뮤니티, 익명 | 2026 | 1장 |
| 오프보딩이 진짜 통증이다 (2013) / 해고 후 1년 넘게 접근 권한 유지 (2026) | 해외 개발자 커뮤니티, 익명 | 2013-10 / 2026-03 | 10장 |
| DX가 서류 디지털화에서 멈춘 이유는 기술이 아니라 정치 | 개발자 커뮤니티, 익명 | 2026 | 9장 |

## B-6. 이 책이 의도적으로 쓰지 않은 것

인용 규율상 배제한 항목을 밝혀 둔다. 근거를 밝힌 배제는 그 자체가 근거다.

- **거시 경제 수치.** AI의 총요소생산성 효과에 대해 Acemoglu의 10년 누적 0.66%와 Aghion & Bunel의 연 0.68%포인트라는 열 배 격차의 추정이 공존한다. 병기하지 않으면 독자에게 열 배 틀린 그림을 주므로, 조직 층위의 책인 이 책은 쓰지 않는 쪽을 택했다.
- **"조직 변화의 70%는 실패한다."** 저명한 출처 다섯을 추적한 연구가 유효하고 신뢰할 만한 실증 근거가 없다고 결론지었다(B-3 59번).
- **출처·표본·연도가 특정되지 않은 수치** — 오프보딩 절차 보유율, 고아 계정 비율, DIY 플랫폼 실패율, RPA 실패율, 감사 오버헤드 감소율, 경영진의 미승인 도구 사용률, 섀도 AI 통계 일반, `AGENTS.md` 채택 저장소 수. 방향만 쓰거나 아예 쓰지 않았다.
- **그림·표에서만 읽히는 수치.** 설명 가능성과 적정 신뢰를 다룬 연구들에 대해서는 방향성과 본문의 유의성 값만 인용했다.
- **없는 사례.** 실제 조직이 공개한 에이전트 폐기 절차, 국내 기업의 에이전트 등록 사례, 에이전트에 성과 지표를 부여해 운영한 조직의 공개 사례를 이 책은 찾지 못했다. 검색 기록은 남아 있고, 그 부재를 본문에서 발견으로 다뤘다.
