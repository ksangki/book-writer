# 부록 A. 워크시트 모음 — 각 장이 남긴 아홉 개의 도구

각 장에서 만든 도구를 장 순서대로 모았다. 본문을 읽지 않아도 쓸 수 있게 요약했다. 다만 표마다 왜 그런 모양인지는 해당 장에 적혀 있다. 그리고 **앞 칸을 안 채우고 뒤 칸을 채우면 뒤 칸이 헛돈다.** 이 순서를 지키는 것 자체가 목록에 없는 열 번째 도구다.

이 가운데 다섯 도구(A-1·A-3·A-6·A-7·A-9)는 예제 에이전트로 옮겨 실제로 돌려 보았다. 그 기록이 2·4·7·8·10장 끝 「만들어 보기」 상자 ①~⑤다. 도구가 코드 안에서 어떤 모양이 되는지는 그 상자에서 볼 수 있다.

## A-1. 재고 조사의 관문 다섯 개와 판별 3질문 (2장)

### 관문 다섯 개 — 목록 전체를 훑는 도구

재고 조사는 조직 안에 어떤 AI가 돌고 있는지 전부 세어 보는 일이다. 관문은 그 목록을 차례로 거르는 체다. 판정하기 쉬운 관문을 앞에, 품이 많이 드는 관문을 뒤에 놓았다. 순서를 뒤집으면 재고 조사가 큰 프로젝트가 된다. 큰 프로젝트가 되는 순간 다음 분기로 밀린다.

| # | 관문 | 걸러지는 것 | 판정 요령 |
|---|---|---|---|
| ① | 생성형인가 | 규칙 기반 자동화·통계 모델·기존 배치 | 걸러진 것에도 값이 있다는 점을 판정 결과에 적어 둔다 |
| ② | 행위하는가 | 답만 하는 챗봇·초안 도구 | 결과물이 사람의 손을 거치지 않고 다음 단계로 넘어가는가 |
| ③ | 산출물이 실재하는가 | 기획서·미착수·토대 인프라 | 토대 인프라는 별도 목록으로 뺀다 |
| ④ | 조직의 업무인가 | 개인 편의 도구·대고객 제품 | 팀의 업무와 목표에 연결되는가 |
| ⑤ | 무게가 있는가 | — (대상 안에서 강도를 가른다) | 되돌릴 수 없는가, 돈·대외·민감정보에 닿는가 |

**함께 둘 것:**

- 관문 문구의 변경 이력 — 언제·무엇을·왜 바꿨는지 한 줄씩
- 판정 보류 칸
- 후보별 **API 가용성 열** — 다른 시스템이 프로그램으로 불러 쓸 수 있는지(호출 가능 / 부분 / 사람만)

### 판별 3질문 — 실무자가 30초 안에 쓰는 도구

실무자는 자기가 만든 것 하나를 두고 판단해야 한다. 그런 사람에게는 이 형태가 필요하다. 관문과 다른 점이 있다. 판정 결과가 통과냐 탈락이냐가 아니라, **얼마나 세게 통제할지**로 나온다.

| | 묻는 것 | 아니라면 |
|---|---|---|
| **전제** | 조직의 업무인가 (팀 목표에 연결되는가) | 대상 아님 |
| **①** | 실제로 행동하는가 (쓰기·발송·처리) | 가볍게 등록만 |
| **②** | 스스로 도는가 (사람은 예외 상황에만 개입) | 보통 등록 |
| **③** | 되돌릴 수 없는 일인가 (돈·대외·민감정보) | 등록 + 모니터링 |
| | 셋 다 그렇다 | **정식 등록 + 강한 통제** (승인 게이트·감사 로그·킬 스위치) |

맨 아래 줄의 강한 통제는 세 가지다. 승인 게이트는 사람이 확인해야 다음 단계로 넘어가는 지점이다. 감사 로그는 누가 무엇을 했는지 남기는 기록이다. 킬 스위치는 문제가 생기면 즉시 멈추는 장치다.

오른쪽 열의 세 단계는 실제 처리가 서로 달라야 한다. 이름만 다르고 처리가 같으면 실무자는 금방 알아챈다. 그러면 질문에 대충 답하기 시작한다.

## A-2. SOP 진단표 (3장)

SOP는 표준 작업 절차, 곧 누가 무엇을 어떤 순서로 하는지 적은 문서다. 이 표는 문서에 적힌 절차와 실제로 하는 일을 맞대 본다. 작업 기록(로그)이 없는 조직도 시작할 수 있다. 실제 작업을 다섯에서 열 건쯤 직접 지켜보면 된다.

| 적힌 단계 | 실제 로그·관찰에서 확인된 단계 | 간극의 성격 |
|---|---|---|
| 문서에 적힌 순서 그대로 | 기록이나 관찰로 확인한 것 | 아래 넷 중 하나 |

| 간극의 성격 | 처방 |
|---|---|
| **누락** — 실제로는 하는데 문서에 없다 | 문서에 추가한다 |
| **순서 역전** — 문서와 실제의 순서가 다르다 | 어느 쪽이 옳은지부터 판정한다 |
| **비공식 우회** — 특정 조건에서 단계를 건너뛴다 | 조건을 명문화하거나 그 단계를 없앤다. 우회 금지는 대개 답이 아니다 |
| **형식화 불가** — 사람의 판단으로만 되는 단계 | 옮기지 않는다. 사람을 남기고 경계로 표시한다 |

**쓰는 법 세 가지:**

- 적힌 단계를 먼저 채운다.
- 절차 하나에 실제 사례를 다섯에서 열 건 본다.
- 간극이 없는 행은 지운다.

그리고 **이 표는 그 일을 직접 하는 사람이 채운다.** 감사 담당자가 채우면 비공식 우회 칸이 조용히 빈다. 우회를 적어 내면 불이익이 온다고 느끼기 때문이다. 그렇게 비어 버린 표는 원래 문서보다 나쁘다.

## A-3. 에이전트 SOP 작성 규칙 체크리스트 (4장)

에이전트가 읽고 따를 절차 문서를 쓸 때 점검하는 목록이다. 여섯 항목 가운데 넷은 절차를 쓰는 사람의 몫이다. 나머지 둘은 절차를 유지하는 사람의 몫이다. 그런데 쓰는 사람과 유지하는 사람은 대개 다른 사람이다. 그래서 5번과 6번은 등록부에 적어 두어야 한다.

| # | 점검 항목 | 확인 |
|---|---|---|
| 1 | 각 단계의 **산출물 기준**을 못 박았는가 (무엇이 나와야 하고, 어떤 조건을 갖춰야 하는가) | ☐ |
| 2 | 추상적 정의 대신 **짧은 명령형**으로 썼는가 | ☐ |
| 3 | 한 덩어리 대신 **점진적 공개** 구조로 짰는가 ("X 할 때는 Y를 참조하라") | ☐ |
| 4 | **결정론적 검증 지점**이 어디인지 지정했는가 | ☐ |
| 5 | **모델 버전과 성능 기준선**을 기록했는가 | ☐ |
| 6 | **규칙 파일 정리 주기와 회귀 테스트 주기**를 정했는가 | ☐ |

낯선 말 셋을 풀어 둔다. 점진적 공개는 모든 내용을 한 번에 주지 않고, 필요한 순간에 필요한 부분만 찾아보게 짜는 방식이다. 결정론적 검증 지점은 AI의 판단에 맡기지 않고 규칙이나 프로그램으로 맞고 틀림을 확인하는 곳이다. 회귀 테스트는 모델을 바꾼 뒤에도 예전처럼 제대로 도는지 다시 확인하는 시험이다.

## A-4. 등록 스키마 여덟 칸 (5장)

에이전트를 조직에 등록할 때 채우는 여덟 칸이다. 앞의 일곱 칸은 대체로 순순히 채워진다. 여덟 번째 칸이 늘 빈다. **채워지지 않더라도 칸은 남겨 둔다.** 빈 칸은 해야 할 일이 밀렸다는 표시로 보인다. 칸이 아예 없으면 밀렸다는 사실조차 보이지 않는다.

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

**첫 회차에는 세 칸만 강제한다.** 디지털 신원, 스폰서, 행위 범위다. 나머지는 등급이 올라갈 때 붙인다.

**세 역할의 권한 경계:**

- 오너 — 기술을 관리한다 (선택)
- **스폰서 — 사업의 결과를 책임진다 (필수)**
- 매니저 — 조직 계층에서 관리한다 (선택)

스폰서 자리에 추진 조직이나 플랫폼 팀의 이름이 들어가면 그 설계는 이미 어긋났다. 결과를 책임질 사람은 그 업무의 성과를 책임지는 현장 부서 쪽에 있어야 한다.

**검증 질문 한 줄:** *이 원장을 아무도 업데이트하지 않으면 무슨 일이 벌어지는가?* 답이 "아무 일도 안 벌어진다"라면 그 원장은 이미 죽어 있다.

## A-5. 두 계층 부여 기준 넷 (6장)

에이전트에게 주는 신분은 두 겹이다. 1계층은 식별자, 곧 에이전트마다 붙이는 고유 번호다. 만들어진 에이전트 전부에게 준다. 2계층은 사번이다. 평가를 받고, 자원을 배정받고, 성과가 귀속되는 자격이다. 아래 기준을 통과한 것에만 준다.

| 기준 | 묻는 것 | 왜 이것이 기준인가 |
|---|---|---|
| 연결 범위 | 다른 시스템이나 다른 에이전트를 호출하는가 | 연결이 늘면 영향 범위가 늘어난다 |
| 접근 권한 | 어떤 데이터와 기능에 닿는가 | 닿는 곳이 곧 사고 시 피해 범위다 |
| 상시 운영 여부 | 일회성 실험인가, 계속 도는 업무인가 | 계속 도는 것에만 유지 비용이 든다 |
| **절차 문서 보유 여부** | 이 에이전트가 수행하는 절차가 글로 적혀 있는가 | 기준선이 없으면 평가가 성립하지 않는다 |

**함께 정할 것:**

- 등록 단위와 과금 단위를 분명히 갈라 둔다.
- 인턴 단계를 둔다면 기한을 못 박는다.
- 권한은 사람에게서 위임받는 형태를 기본값으로 한다. 에이전트 자체 권한은 위험이 크고 계속 도는 경우에만 예외로 남긴다.

**운영 비용 항목표:**

| 비용 항목 | 언제 발생하는가 | 놓치기 쉬운 이유 |
|---|---|---|
| 인사 데이터와 접근 권한 그룹의 지속 동기화 | 상시 | 초기 구축 비용으로만 잡고 운영비를 안 잡는다 |
| 소유자 이탈 시 자격 증명 교체 | 담당자 퇴사·이동 때마다 | 사람 오프보딩 절차에 이 단계가 없다 |
| 감사 로그 적재와 보관 | 상시 | 저장 비용은 규모에 비례해 늘어난다 |
| 절차 문서의 회귀 테스트 | 모델을 교체할 때마다 | 모델 교체를 비용 이벤트로 보지 않는다 |
| 라이선스 | 2계층 부여 시점부터 | 등록 단위와 좌석 단위를 일치시키면 커진다 |
| 등록·심사 자체의 인건비 | 상시 | 제도 운영에 사람이 든다는 사실을 빼먹는다 |

**판정 형태:** 비용과 효과를 견준다. 한 에이전트를 1년 유지하는 비용이 그 에이전트가 줄여 준 일의 가치보다 크면, 그 에이전트는 폐기 후보다.

## A-6. 자율성 등급표 초안 (7장)

자율성 등급은 에이전트가 사람 없이 어디까지 스스로 해도 되는지를 정한 단계다. 표의 세로축은 허용하는 자율성이다. 가로축은 네 가지 기능이다. 그리고 행마다 위협 모델 열을 붙인다. 위협 모델은 그 칸에서 무엇이 잘못될 수 있는지 적은 것이다. 이 표의 요점은 하나다. **자율성을 숫자 하나로 적지 않는다.** 예를 들어 같은 에이전트라도 조회는 혼자 하게 두고, 집행은 사람이 확인하게 할 수 있다.

| 허용 자율성 | 조회 | 해석 | 선택 | 집행 | 위협 모델 | 필요한 통제 |
|---|---|---|---|---|---|---|
| A1 손을 얹고 (직접 실행) | | | | | | |
| A2 지시를 얹고 (지시) | | | | | | |
| A3 눈을 얹고 (감독) | | | | | | |
| A4 마음을 얹고 (목표·제약 설정) | | | | | | |
| A5 마음을 떼고 (정책 설정) | | | | | | |

**채울 때 세 가지:**

- 등급 판정은 A-1의 판별 3질문이 내놓는 결과로 한다. 개인 재량에 맡기면 판정하는 사람마다 결과가 갈린다.
- **위협 모델 열을 비워 두지 않는다.** 이 열이 비면 그 행은 이름표일 뿐이다.
- **2단계로 시작해도 된다.** 왜 다섯 단계가 필요한지 답하지 못한 채 다섯 칸을 채우는 쪽이 더 나쁘다.

**전제:** 기술적으로 할 수 있는 것(역량)과 조직이 해도 된다고 허락한 것(허용 자율성)은 다른 축이다. 두 축이 어긋난 칸은 결함이 아니라 일부러 고른 관리 방침이다. 그 선택을 분명히 적어 두는 것이 이 표의 목적이다. 그리고 사람의 승인을 등급을 나누는 축으로 삼지 않는다. 승인은 되돌릴 수 없는 소수의 행위에만 남긴다. 나머지 위험한 행위는 에이전트가 애초에 닿을 수 없게 막는다.

## A-7. 환산식과 두 계수 (8장)

에이전트가 한 일을 사람의 일손으로 바꿔 세는 식이다. 단위는 FTE다. FTE는 전일 근무자 한 명이 1년 동안 일하는 시간을 1로 잡은 단위다. 그 1년이 몇 시간인지는 아래 첫 번째 벽에서 다룬다.

**환산 두 단:** 에이전트 처리량 → (건당 사람 소요시간) → 사람이 했다면 걸렸을 시간 → (1 FTE의 연간 시간) → FTE 환산값 → (신뢰도 등급) → 인정 FTE → (자율성 계수) → 에이전트 몫 FTE

괄호 안은 각 단계에서 곱하거나 나누는 값이다. 예를 들어 처리 건수에 건당 사람 소요시간을 곱하면, 사람이 했다면 걸렸을 시간이 나온다.

**세 개의 벽:**

- **분모가 없다.** 1 FTE가 1년에 몇 시간인지 조직이 합의한 값이 없다. 이 값은 인사 부서가 정해야 한다. 한번 정하면 전사가 같은 값을 쓴다.
- **분자가 부실하다.** 건당 사람 소요시간의 기준값이 약하다. 담당 조직이 이 값을 적되, 적은 값을 **공개**한다.
- **실측 인프라가 아직 없다.**

**계수 ① 신뢰도** — 이 숫자를 얼마나 믿을 수 있는지에 따라 인정하는 몫을 줄인다.

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

**계수 ② 자율성** — 사람의 손이 아직 남아 있는 만큼 계수를 곱해 에이전트 몫을 줄인다. 실측이 가능해지면 사람이 끼어들지 않고 끝난 비율을 그대로 쓴다.

두 계수는 서로 다른 것을 바로잡는다. 신뢰도는 *이 숫자를 믿을 수 있나*를 묻는다. 자율성은 *이 가운데 에이전트 몫이 얼마인가*를 묻는다. 그래서 둘을 곱해 쓰지만, 같은 것을 두 번 깎는 것이 아니다.

**규칙 셋:**

- 모든 수치에 출처 성격 라벨을 붙인다. 라벨 없는 숫자는 표에 올리지 않는다.
- 과업 하나에서 얻은 이득을 조직 전체의 성과로 부풀려 곱하지 않는다. 업무 흐름 전체의 처리 시간을 따로 재고, 두 값을 나란히 적은 대조표를 남긴다.
- 보상에 거는 지표와 지켜보기만 하는 지표를 갈라 둔다. **AI 사용량을 성과 지표로 삼지 않는다.**

## A-8. 사용 제한 선언문 초안과 커뮤니케이션 4원칙 (9장)

측정을 시작하기 전에, 잰 숫자를 어디에 쓰지 않을지 미리 밝히는 문서의 초안이다. 날짜 칸(○○)은 조직마다 채운다.

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

**금지 어휘:** "잡아낸다." 말하는 쪽에서는 탐지 기능을 가리키는 중립적인 말이다. 하지만 듣는 쪽에서는 자기가 잡히는 대상이라는 뜻으로 들린다.

**실행 원칙:**

- 사용자에게 아주 작은 수정 권한이라도 준다. 단, **수정할 수 있는 구간과 책임이 누구에게 있는지는 별도 칸으로 나눠 적는다.**
- 에이전트의 오류율을 사람의 오류율과 나란히 공개한다.
- 도입은 효과가 큰 집단부터 넓혀 간다.
- 문화 슬로건보다 개인이 실제로 하는 작업에 투자한다.
- 중간관리자를 가장 먼저 챙긴다.
- 첫 단계는 실무자 교육이 아니라 리더의 자기 규율이다.

## A-9. 폐기 체크리스트 7항목 (10장)

다 쓴 에이전트를 안전하게 내려놓을 때 확인할 항목이다. **폐기할 때가 되어서야 이 표를 꺼내면 늦다.** 등록할 때 초안을 채우고, 운영하는 동안 갱신하는 문서다.

| # | 항목 | 확인할 것 |
|---|---|---|
| ① | 공식 폐기 워크플로 | 승인 절차를 포함하는가. 누가 요청하고 누가 승인하는가 |
| ② | 자격 증명·토큰 즉시 폐기 | API 키·인증서·OAuth 토큰이 전부 목록에 있는가 |
| ③ | 아웃바운드 접근 제거 | 이 에이전트가 호출하던 연동과 도구 권한 |
| ④ | 인바운드 호출 차단 | 이 에이전트를 부르던 엔드포인트·웹훅·큐 |
| ⑤ | 메모리·데이터 정화 | 보관할 것, 익명화할 것, 안전 삭제할 것을 구분했는가 |
| ⑥ | 감사 추적 보존 | 불변 로깅. **지우지 않고 남기는 유일한 항목** |
| ⑦ | 폐기 후 잔여 리스크 모니터링 | 끈 뒤에도 한동안 본다. 기간을 숫자로 정한다 |

③과 ④는 방향이 반대다. 아웃바운드는 이 에이전트가 밖으로 불러 쓰던 것이다. 인바운드는 밖에서 이 에이전트를 부르던 통로다.

**용어 구분:** 취소는 지금 열려 있는 작업 세션을 끝내는 일이다. 디프로비저닝은 신원과 권한을 영구히 없애는 일이다. 둘은 같지 않다. 취소만 된 에이전트는 등록과 신뢰 관계를 그대로 가지고 있다.

**재심사는 사건에 건다 (분기 재심사가 아니다):** 아래 일이 생기면 그때 다시 심사한다.

- 권한 크립 탐지 — 권한이 조금씩 늘어난 것이 보일 때
- 접근 패턴 드리프트 — 평소와 다른 곳에 접근하기 시작할 때
- 새 역량 획득 — 새 기능이 붙었을 때 소유자를 다시 확인한다

**그리고 이것이 아홉 개 도구 전체의 마지막 규칙이다.** 폐기 절차를 사람이 기억해서 지키는 규칙으로 두지 않는다. **처음 발급할 때부터 만료를 넣어 둔다.** 기본값이 소멸이면, 아무도 챙기지 않아도 정리한 것과 같은 결과가 난다.

---

# 부록 B. 참고문헌

본문을 쓸 때 실제로 근거로 삼은 것만 추렸다. 축별로 묶고, 각 항목에 **출처 성격**과 **확인 등급**을 붙였다.

**확인 등급:** ★ 원문 직접 열람 / △ 검색 요약·2차 자료 경유 / ✗ 접근 실패
**문헌 유형:** `[PR]` 동료평가 논문 / `[PP]` 프리프린트 / `[WP]` 워킹페이퍼·워크숍 논문(정식 학회 논문 아님) / `[공식]` 공식 문서·보도자료 / `[규제]` 규제 원문 / `[정부]` 정부 공개 자료 / `[조사]` 컨설팅·업계 조사 / `[벤더]` 벤더 자료 / `[매체]` 언론 보도 / `[커뮤니티]` 커뮤니티 게시물 / `[학술]` 학술 기관·연구소 발간물 / `[보고서]`·`[기술보고서]` 기관 보고서 / `[문헌]` 저자·연도가 특정되지 않은 2차 문헌 / `[PR-단행본]` 동료평가 계열 단행본 / `[PP→PR]`·`[PP→워크숍]` 프리프린트에서 게재·워크숍으로 이행 / `[저자 자료]` 저자가 만든 예제 코드·데이터

웹 자료의 접근일은 모두 **2026년 9월 5일**이다. 다만 v1.5.0에서 더한 항목(표에 *v1.5.0* 표시)의 접근일은 **2026년 10월 10일**이다. v1.6.0에서 더한 B-7의 기준일도 **2026년 10월 10일**이다. 이 분야는 분기 단위로 바뀐다. 규제·제품·표준 항목은 인용하는 시점에 원문을 다시 확인하는 편이 낫다.

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
| Register and manage A2A agents — Gemini Enterprise Agent Gallery (갱신 2026-10-09, 프리뷰) *v1.5.0* | [docs.cloud.google.com](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-a2a-agent) | `[공식]` | ★ |
| Agent Store in Microsoft Copilot — 조직 카탈로그 제출·검토·게시 (2026-04-17, 갱신 2026-08-18) *v1.5.0* | [learn.microsoft.com](https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-agent-store) | `[공식]` | ★ |
| SAP LeanIX announces launch of AI agent hub — agent discovery inbox (2025-11-04) *v1.5.0* | [leanix.net](https://www.leanix.net/en/blog/sap-leanix-announces-launch-of-ai-agent-hub-and-key-industry-partnerships) | `[벤더]` | ★ |
| SAP AI Agent Hub 참조 아키텍처 — 자동 발견·팩트시트·수명주기 (갱신 2026-10-01) *v1.5.0* | [architecture.learning.sap.com](https://architecture.learning.sap.com/docs/ref-arch/jkg4j2) | `[벤더]` | ★ |

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

1\. Hübner, J. F., Sichman, J. S., & Boissier, O. (2002). A Model for the Structural, Functional, and Deontic Specification of Organizations in Multiagent Systems (MOISE+). *SBIA 2002*, LNAI 2507. Springer. `[PR]` △
2\. Mitchell, M. et al. (2019). Model Cards for Model Reporting. *FAT\* '19*. [arXiv:1810.03993](https://arxiv.org/abs/1810.03993). `[PR]` △
3\. Santoni de Sio, F., & Mecacci, G. (2021). Four Responsibility Gaps with Artificial Intelligence. *Philosophy & Technology*, 34(4), 1057–1084. `[PR]` △
4\. Chan, A. et al. (2024). Visibility into AI Agents. *ACM FAccT '24*. [arXiv:2401.13138](https://arxiv.org/abs/2401.13138). `[PR]` △
5\. Chan, A. (2024). IDs for AI Systems. [arXiv:2406.12137](https://arxiv.org/abs/2406.12137). `[PP]` △
6\. Kolt, N. (2025). Governing AI Agents. *Notre Dame Law Review* (게재 예정). [arXiv:2501.07913](https://arxiv.org/abs/2501.07913). `[PP→PR]` △
7\. Chan, A. et al. (2025). Infrastructure for AI Agents. *TMLR*. [arXiv:2501.10114](https://arxiv.org/abs/2501.10114). `[PR]` △
8\. Kraprayoon, J. et al. / IAPS (2025). AI Agent Governance: A Field Guide. [arXiv:2505.21808](https://arxiv.org/abs/2505.21808). `[보고서]` △
9\. Kaptein, M., Khan, V.-J., & Podstavnychy, A. (2026). Runtime Governance for AI Agents: Policies on Paths. [arXiv:2603.16586](https://arxiv.org/abs/2603.16586). `[PP]` △
10\. Nian, Y. et al. (2026). Auditable Agents. [arXiv:2604.05485](https://arxiv.org/abs/2604.05485) (v2 2026-08-13). `[PP]` △
11\. Otsuka, T., Toyoda, K., & Leung, A. (2026). AI Identity: Standards, Gaps, and Research Directions for AI Agents. [arXiv:2604.23280](https://arxiv.org/abs/2604.23280). `[PP]` △
12\. Atkinson, D. I., & O'Bryan, J. E. (2026). Government AI Use as a Monitoring Primitive. [arXiv:2607.04543](https://arxiv.org/abs/2607.04543). ICML 2026 Workshop on Technical AI Governance. `[PP→워크숍]` △
13\. Feng, K., McDonald, N., & Zhang, A. X. (2025). 자율성 등급과 자율성 인증서 (컬럼비아 나이트 제1수정헌법 연구소, 2025-07-28). `[학술]` △

### SOP·절차의 형식화

14\. Adler, P. S., & Borys, B. (1996). Two Types of Bureaucracy: Enabling and Coercive. *Administrative Science Quarterly*, 41(1), 61–89. `[PR]` △ — 원문은 OCR 판독본이다. 4대 특성의 개별 정의문은 미확보이므로, 이 책이 이 논문에 귀속시킨 것은 "두 유형이 있다"는 구분까지다. 본문 1장이 인용한 enabling 형식화의 정의문은 아래 14-1의 p.296에서 왔다.
14-1\. Ahrens, T., & Chapman, C. S. (2004). Accounting for Flexibility and Efficiency: A Field Study of Management Control Systems in a Restaurant Chain. *Contemporary Accounting Research*, 21(2), 271–301. `[PR]` △ — 애들러·보리스의 구분을 관리통제 연구로 옮긴 첫 연구다. 본문 1장이 인용한 enabling 사용의 정의문(p.296)의 근접 출처이며, 그 한 줄은 2차 문헌(Mamat 2012, Warwick 리포지토리) 경유로 확보했으며, 원문은 "attempts to mobilize local knowledge and experience in support of central objectives"다. 초록에는 네 설계 원리(repair·internal transparency·global transparency·flexibility)의 이름이 나열되나 개별 정의문은 미확보이므로, 이 책은 설계 특성까지 들어가지 않았다.
15\. Nonaka, I. (1994). A Dynamic Theory of Organizational Knowledge Creation. *Organization Science*, 5(1), 14–37. `[PR]` △
16\. Feldman, M. S., & Pentland, B. T. (2003). Reconceptualizing Organizational Routines as a Source of Flexibility and Change. *Administrative Science Quarterly*, 48(1), 94–118. `[PR]` △
17\. Gourlay, S. (2006). Conceptualizing Knowledge Creation: A Critique of Nonaka's Theory. *Journal of Management Studies*, 43(7), 1415–1436. `[PR]` △
18\. van der Aalst, W. M. P. (2011 / 2016). *Process Mining: Discovery, Conformance and Enhancement of Business Processes*. Springer. `[PR-단행본]` △
19\. Hong, S. et al. (2024). MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework. *ICLR 2024 (Oral)*. [arXiv:2308.00352](https://arxiv.org/abs/2308.00352). `[PR]` △
20\. Nandi, S. et al. (2025/2026). SOP-Bench: Complex Industrial SOPs for Evaluating LLM Agents. [arXiv:2506.08119](https://arxiv.org/abs/2506.08119) (v2 2026-02-23). `[PP]` △ — 2026년 2월 시점 모델 라인업 기준
21\. Amazon Science (2025). Structuring the Unstructured: A Multi-Agent LLM Framework for Transforming Ambiguous SOPs into Code. *EMNLP 2025 Industry Track*. `[PR]` △ — 종단 정확도 수치는 원문 대조 미완이므로 이 책은 쓰지 않았다
22\. 도요타 생산방식의 표준작업(standardized work)과 개선 사이클 | 린 생산 문헌 | `[문헌]` △

### 조직 경제학·생산성 실증

23\. Klein, K. J., & Sorra, J. S. (1996). The Challenge of Innovation Implementation. *Academy of Management Review*, 21(4), 1055–1080. `[PR]` △
24\. Brynjolfsson, E., Hitt, L. M., & Yang, S. (2002). Intangible Assets: Computers and Organizational Capital. *Brookings Papers on Economic Activity*, 2002(1). `[PR]` △
25\. Brynjolfsson, E., Rock, D., & Syverson (2017). Artificial Intelligence and the Modern Productivity Paradox. *NBER WP 24001* `[WP]` / (2021) The Productivity J-Curve. *AEJ: Macroeconomics* `[PR]` △
26\. McElheran, K. et al. (2024). AI Adoption in America: Who, What, and Where. *Journal of Economics & Management Strategy*, 33(2), 375–415. `[PR]` △ — 2018년 데이터
27\. Bick, A., Blandin, A., & Deming, D. J. (2024). The Rapid Adoption of Generative AI. *NBER WP 32966*. `[WP]` △ — 자기보고 기반, 정식 게재본 아님
28\. Brynjolfsson, E., Li, D., & Raymond, L. (2025). Generative AI at Work. *Quarterly Journal of Economics*, 140(2), 889–942. `[PR]` △ — GPT-3.5 세대
29\. Dell'Acqua, F. et al. (2025). Navigating the Jagged Technological Frontier. *Organization Science*. HBS WP 24-013. `[PR]` △ — 2023년 GPT-4 세대
30\. Cui, Z. (K.) et al. (2025). The Effects of Generative AI on High-Skilled Work. *Management Science*. `[PR]` △
31\. METR (2025). Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity. [arXiv:2507.09089](https://arxiv.org/abs/2507.09089). `[PP]` △ — 표본 16명. 같은 팀의 2026-02 후속과 반드시 병기
32\. Dillon, E. et al. (2025). 대규모 현장 실험(n=7,137) — 이메일 시간 −31%, 회의 시간 변화 없음. *NBER 워킹페이퍼* 33795. `[WP]` △
33\. Demirer, M. et al. (2026). 개발 도구 효과의 산출물 감쇠와 대체탄력성 0.25. *NBER 워킹페이퍼* 35275. `[WP]` △
34\. Vaccaro, M., Almaatouq, A., & Malone, T. (2024). When combinations of humans and AI are useful: A systematic review and meta-analysis. *Nature Human Behaviour*, 8(12). `[PR]` △ — 2020-01~2023-06 게재 논문 대상. 인용 시 기준선 병기·이질성 명시 필수. 본문 8장이 지면에서 뺀 세부값: 이질성 I² 시너지 97.7%·증강 93.8% / 생성 과업 +0.19는 p=0.180, 95% CI [−0.09, 0.48], k=34로 0과 유의차 없음 / 과업 유형 간 차이 F(1,104)=7.84, p=0.006
35\. Hemmer, P., Schemmer, M., Kühl, N., Vössing, M., & Satzger, G. (2025). Complementarity in Human-AI Collaboration: Concept, Sources, and Evidence. *European Journal of Information Systems*. `[PR]` △ — [arXiv:2404.00029](https://arxiv.org/abs/2404.00029)로 공개된 뒤 게재 확인(2026-09-12 검증). 정보 비대칭과 역량 비대칭을 상보성의 두 원천으로 정리
36\. Bessen, J. (2015-03). 현금인출기와 창구직, 19세기 역직기 사례. IMF *Finance & Development* 2015년 3월호 기고문. `[문헌]` △ — 창구직원 총수의 절대 수치는 이 기고문에 없다
37\. Goodhart, C. (1975) 원문 / Strathern, M. (1997). *European Review*, 5(3), 305–321. `[PR]` △ — "지표가 목표가 되면"의 정식화는 Strathern이며 경구는 p.308
38\. Manheim, D., & Garrabrant, S. (2018). Categorizing Variants of Goodhart's Law. [arXiv:1803.04585](https://arxiv.org/abs/1803.04585). `[PP]` △
39\. Bevan, G., & Hood, C. (2006). 영국 공공 부문 지표 게이밍 — 공식 통계 96% vs 환자 설문 77%, 별점-품질 상관 0. `[PR]` △
40\. Mabe, P. A., & West, S. G. (1982). 자기평가와 실제 수행의 상관 r = .29, 측정 조건이 변동의 64% 설명. `[PR]` △
41\. Podsakoff, P. M. et al. (2012). 동일 설문 응답에서 상관 133~304% 팽창. `[PR]` △ — 133~304%는 2012년판 수치다. 2003년판이 정본이나 이 책이 인용한 값의 판본은 2012년이다

### 자율성 등급·감독·자동화 편향

42\. Bainbridge, L. (1983). Ironies of Automation. *Automatica*, 19(6). `[PR]` △
43\. Sheridan, T. B., & Verplank, W. L. (1970년대 후반). 10단계 자동화 등급. `[기술보고서]` △ — 재수록본 경유. 발표 연도 귀속이 자료마다 갈린다
44\. Endsley, M. R., & Kaber, D. B. (1999). Level of automation effects on performance. *Ergonomics*. `[PR]` △ — 10단계 × 4기능 배분표
45\. Skitka, L. J., Mosier, K. L., & Burdick, M. (1999). Does automation bias decision-making? *IJHCS*, 51(5), 991–1006. `[PR]` △ — 항공 시뮬레이션
46\. Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). A model for types and levels of human interaction with automation. *IEEE Transactions on Systems, Man, and Cybernetics*. `[PR]` ★(초록) — 이론 정리 논문이며 원저 실증 데이터는 없다
47\. Merat, N. et al. (2014). 제어 안정화까지 35~40초. `[PR]` △
48\. Eriksson, A., & Stanton, N. A. (2017). 인계 시간 1.97~25.75초. `[PR]` △
49\. Endsley, M. R. (2017). *Human Factors*. 자율성-상황인식 딜레마. `[PR]` △
50\. Victor, T. W. et al. (2018). 테스트트랙 106명, 76명 중 21명(28%) 충돌. `[PR]` △ — 자율주행 맥락
51\. Zhang, B. et al. (2019). 129편 메타분석, 평균 2.72초(0.69~19.79초). `[PR]` △
52\. Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To Trust or to Think — 인지적 강제 기능. *PACM HCI*, 5(CSCW1). `[PR]` △ — 효과 크기 미확보, 방향만 인용
53\. Bansal, G. et al. (2021). Does the Whole Exceed its Parts? *CHI '21*. `[PR]` △ — 그림 수치 인용 금지 대상. 방향성과 본문 z/p값만 사용
54\. Green, B. (2022). The flaws of policies requiring human oversight of government algorithms. *Computer Law & Security Review*, 45. [arXiv:2109.05067](https://arxiv.org/abs/2109.05067). `[PR]` △ — 정책 41개 조사
55\. Laux, J. (2023). Institutionalised distrust and human oversight of artificial intelligence. *AI & Society*. `[PR]` △ — 구성적 vs 교정적 개입
56\. Cihon, P., Stein, M., Bansal, G., Manning, S., & Xu, K. (2025). Measuring AI agent autonomy: Towards a scalable approach with code inspection. [arXiv:2502.15212](https://arxiv.org/abs/2502.15212). NeurIPS SoLaR Workshop 2024. `[WP]`(워크숍 논문) △ — AutoGen 애플리케이션 10건, 코드 정적 검사. Actions κ = 0.30
57\. Zheng, Dong, Depena, Bhatia, Xiao, & Xu (2026-07-26). Separating Capability from Permission: A Governance Framework for Agentic AI Autonomy Levels. [arXiv:2607.23438](https://arxiv.org/abs/2607.23438)v1. ExxonMobil 기술 조직. `[PP]` △ — AAL/ACL 2축 프레임. 동료심사 없음. 10페이지 산업 실무 보고, 실증 사례 단일 기업 2건
58\. 미 도로교통안전국 결함조사 (2백만 대, 467건 충돌) / 국가교통안전위원회 개별 사고조사 2건 (2024) | `[정부]` △

### 변화관리·수용·저항

59\. Hughes, M. (2011). Do 70 Per Cent of All Organizational Change Initiatives Really Fail? *Journal of Change Management*, 11(4), 451–464. `[PR]` △ — 이 책이 "70%" 수치를 쓰지 않는 근거
60\. Dietvorst, B. J., Simmons, J. P., & Massey, C. (2015). Algorithm Aversion. *JEP: General*, 144(1), 114–126. `[PR]` △
61\. Dietvorst, B. J. et al. (2018). Overcoming Algorithm Aversion. *Management Science*, 64(3), 1155–1170. `[PR]` △ — 아주 작은 수정 권한의 효과
62\. Kellogg, K. C., Valentine, M. A., & Christin, A. (2020). Algorithms at Work: The New Contested Terrain of Control. *Academy of Management Annals*, 14(1), 366–410. `[PR]` ★ — 알고리즘 통제의 여섯 기제
63\. Ravid, D. M. et al. (2023). A meta-analysis of the effects of electronic performance monitoring on work outcomes. *Personnel Psychology*. `[PR]` △ — 사람 모니터링 연구이며 에이전트 로깅 연구가 아니다
64\. Shonhe, L., & Min, Q. (2025). Mitigating AI-induced professional identity threat and fostering adoption in the workplace. *AI & Society*, 40(5), 4079–4092. `[PR]` △ — 동·남부 아프리카 단일 직군 413명, 자기보고 횡단 연구

## B-4. 조사 보고서·산업 자료

| 자료 | 출처 | 유형 | 확인 |
|---|---|---|---|
| Gartner — 에이전트 워싱, 수천 벤더 중 약 130개 (2025-06-25) | Gartner 보도자료 | `[조사]` | ✗(403) / 복수 매체 교차 △ |
| Gartner — 비례적 거버넌스 4단계, 이분법 진단, 2027년 40% 강등·폐기 전망 (2026-05-26) | Gartner 보도자료 | `[조사]` | ✗ / 복수 매체 교차 △ |
| Gartner — 에이전트 난립 관리 6단계, 2028년 포천 500 평균 15만 개 전망 (2026-04-28) *v1.5.0* | [Gartner 보도자료](https://www.gartner.com/en/newsroom/press-releases/2026-04-28-gartner-identifies-six-steps-to-manage-artificial-intelligence-agent-sprawl) | `[조사]` | ✗(403) / 복수 매체 교차 △ |
| Managing AI agent sprawl across business units — "discover before you build" (2026-07-17) *v1.5.0* | [AWS for Industries Blog](https://aws.amazon.com/blogs/industries/managing-ai-agent-sprawl-across-business-units/) | `[벤더]` | ★ |
| Cost versus value: Managing agentic AI system performance — Pay-i CEO 대담 (2026-07-08) *v1.5.0* | [McKinsey](https://www.mckinsey.com/capabilities/quantumblack/our-insights/cost-versus-value-managing-agentic-ai-system-performance) | `[조사]` | ✗(타임아웃) / 2차 △ |
| Atea builds an enterprise AI agent ecosystem — Agent Hotel (2026-07-28) *v1.5.0* | [Microsoft 고객 사례](https://adoption.microsoft.com/en-us/agent-transformation-stories/atea/) | `[벤더]` | ★ |
| Agentic AI is scaling faster than guardrails — 24개국 3,235명, 사용 23% vs 성숙한 거버넌스 21% (2026-04-24) | Deloitte Insights | `[조사]` | ★ |
| The GenAI Divide: State of AI in Business 2025 — 파일럿 5% (2025-07) | MIT 프로젝트 NANDA | `[조사]` | △ — 편의표본(4개 컨퍼런스 참석 시니어 리더), 공식 원문 미확보 — 유통 사본으로 확인했으며 1장 본문의 완충이 이를 가리킨다 |
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

이 책이 인용한 커뮤니티 발언은 모두 **개인의 공개 발언이며 조사 데이터가 아니다.** 게시일은 항목마다 따로 밝혔고, 단일 게시물을 업계 관행으로 승격시키지 않았다. GeekNews 게시물의 상대 표기 시점은 **2026년 9월 5일 조회 기준 추정**이다.

| 인용 | 출처 | 게시일 | 쓰인 장 |
|---|---|---|---|
| "AX 추진팀이 나쁘다기 보다는.. AX팀을 만들어놓고 …도메인 현업자가 주도하고 AX기술자가 서포트하면서…" | GeekNews [`snisty`](https://news.hada.io/topic?id=28341), 토픽 「AX팀을 만드는 순간, 당신의 조직은 AX에 실패한다」 | 토픽 2026-04-09 / 댓글 ≈2026-04 (2026-09-05 조회) | **서문** |
| "mandates happened and now I'm being forced to use them. Absolutely no guidance from leadership though." | Hacker News [`ares623`](https://news.ycombinator.com/item?id=47279806) | 2026-03-06 | 1장 |
| "Confluence is where documentation goes to die. And then rot." | Hacker News [`EdwardDiego`](https://news.ycombinator.com/item?id=23808854) | 2020-07-12 | 3장 |
| 같은 게시판의 반복 증언 4건 (검색 불가·페이지 미발견·지연·불만) | Hacker News, 서로 다른 사용자 | 2019-03 / 2022-02 / 2023-08 / 2024-02 | 3장 |
| "When I get an LLM-generated doc or runbook, my first thought is that its very possible that I'm the first person who has ever read this." | Hacker News [`backlava12`](https://news.ycombinator.com/item?id=49258726) | 2026-08-11 | 3장 |
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
| "So every time we fire or lay off the person whose name is on the automation, we need to rotate the keys?" | Hacker News [`collabs`](https://news.ycombinator.com/item?id=47898675) | 2026-04-25 | 6장 |
| "…watching the org chart explode…" (하루 반 만에 역할 20개) | Hacker News [`yego`](https://news.ycombinator.com/item?id=47245374) | 2026-03-04 | 6장 |
| "Pretty pleaser please people don't get your agents registered as direct-reports in the org-chart with HR!" | Hacker News [`polotics`](https://news.ycombinator.com/item?id=49561918) | 2026-09-04 | 6장 |
| 사람이 루프에 없는 인가에 확립된 표준이 없다 (자체 방식으로 해결) | 개발자 공개 기록, 익명 | 2026 | 6장 |
| "사용자에게 승인이나 거부를 묻는 방식은 무엇이든 터지기를 기다리는 재앙이다" / "보안은 환경에 속한다, 하네스가 아니라" | 개발자 커뮤니티, 익명 | 2026-07 | 7장 |
| 채택된 등급 수가 2로 수렴한다는 관찰 | 개발자 커뮤니티, 익명 | 2026 | 7장 |
| "'절감 시간' 사업 케이스대로 실현된 자동화 프로그램은… 1만 시간은 직원 2만 명에게서 각각 30분씩이다" | 자동화 업계 실무자 William Harris, LinkedIn Pulse 서명 글 | 게시일 미확인 | 8장 |
| "aimless tokenmaxing" — 토큰 리더보드 게이밍 | Hacker News [`827a`](https://news.ycombinator.com/item?id=48236051) | 2026-05-22 | 8장 |
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

인용 규율에 따라 뺀 항목을 밝혀 둔다. 근거를 밝힌 배제는 그 자체가 근거다.

- **거시 경제 수치.** AI의 총요소생산성 효과를 두고 Acemoglu의 10년 누적 0.66%와 Aghion & Bunel의 연 0.68%포인트라는, 열 배나 차이 나는 추정이 나란히 있다. 둘을 함께 적지 않으면 독자에게 열 배 틀린 그림을 준다. 그래서 조직 층위를 다루는 이 책은 쓰지 않는 쪽을 택했다.
- **"조직 변화의 70%는 실패한다."** 저명한 출처 다섯을 추적한 연구가 유효하고 신뢰할 만한 실증 근거가 없다고 결론지었다(B-3 59번).
- **출처·표본·연도가 특정되지 않은 수치** — 오프보딩 절차 보유율, 고아 계정 비율, DIY 플랫폼 실패율, RPA 실패율, 감사 오버헤드 감소율, 경영진의 미승인 도구 사용률, 섀도 AI 통계 일반, `AGENTS.md` 채택 저장소 수. 방향만 쓰거나 아예 쓰지 않았다.
- **그림·표에서만 읽히는 수치.** 설명 가능성과 적정 신뢰를 다룬 연구에서는 방향성과 본문의 유의성 값만 인용했다.
- **없는 사례.** 실제 조직이 공개한 에이전트 폐기 절차, 국내 기업의 에이전트 등록 사례, 에이전트에 성과 지표를 부여해 운영한 조직의 공개 사례를 이 책은 찾지 못했다. 검색 기록은 남아 있고, 찾지 못했다는 사실 자체를 본문에서 발견으로 다뤘다.

## B-7. 예제 저장소 — 「만들어 보기」의 코드

2·4·7·8·10장 끝 「만들어 보기」 상자 ①~⑤가 가리키는 저자의 예제 코드다. v1.6.0에서 보탠 자료다. 데이터는 모두 교육용으로 지어낸 것이고, 상자의 실행 기록은 2026년 10월 10일에 한 번 돌린 값이다.

| 자료 | 출처 | 유형 | 확인 | 쓰인 장 |
|---|---|---|---|---|
| ax-system `examples/digital-workers` — 디지털 워커 예제 에이전트 다섯과 등록부(`registry.yaml`)·실행 런타임 *v1.6.0* | [github.com/ksangki/ax-system](https://github.com/ksangki/ax-system/tree/main/examples/digital-workers) | `[저자 자료]` | ★ (공개 URL 2026-10-10 확인) | 2·4·7·8·10장 |

---

# 부록 C. 예제 직접 돌려 보기

상자 다섯을 읽고 나면 한 번쯤 의심이 든다. 정말 등록부 한 줄이 고객 공지 발송을 막을까? 직접 돌려 보는 편이 빠르다. 터미널(명령을 한 줄씩 입력하는 창)을 자주 열지 않는 사람도 따라올 수 있게, 명령은 한 줄씩 끊어 적었다. 아래 명령·파일 이름·화면 문장은 모두 2026년 10월 10일 기준 예제 저장소(B-7)의 코드에서 확인한 것이다. 코드가 바뀌면 저장소의 안내 문서(`README.md`)가 우선이다.

## C-1. 무엇을 돌려 보는가

돌려 볼 것은 에이전트 다섯과 등록부 하나다. 상자 번호가 곧 에이전트 번호다.

| 상자 | 에이전트 (등록부 ID) | 명령 | 장 | 먼저 볼 결과 파일 (`outputs/`) |
|---|---|---|---|---|
| ① | AI 과제 판별 (AGT-001) | `python run.py a1` | 2장 | `a1_report.md`, `a1_verdicts.jsonl` |
| ② | SOP 변환 (AGT-002) | `python run.py a2` | 4장 | `sop_incident_triage.md`, `a2_open_questions.md` |
| ③ | 장애 티켓 1차 분석 (AGT-003) | `python run.py a3` | 7장 | `a3_report.md`, `a3_triage.jsonl` |
| ④ | 성과 측정 (AGT-004) | `python run.py a4` | 8장 | `a4_performance_report.md` |
| ⑤ | 폐기 점검 (AGT-005) | `python run.py a5` | 10장 | `a5_report.md`, `a5_review_flags.md`, `retirement_plan_AGT-901.md` |

다섯은 따로 놀지 않는다. ②가 만든 절차서(SOP, 표준 작업 절차 — 누가 무엇을 어떤 순서로 하는지 적은 문서)를 ③이 읽는다. ①~③이 남긴 처리 건수와 비용 기록을 ④가 일손(FTE, 전일제 한 사람이 한 달에 하는 일의 양)으로 환산한다. ⑤는 등록부 전체를 점검한다. 등록부에는 예제 다섯 말고도 가상의 오래된 에이전트 셋(AGT-901~903)이 들어 있다.

구조의 요점은 하나다. 에이전트 코드에는 도구, 곧 '할 수 있는 것'만 있다. '해도 되는 것'은 등록부 파일 `registry.yaml`에 행위마다 적힌다. 수준은 넷이다. `suggest`(제안만), `read`(읽기만), `approve`(건건이 사람 승인), `auto`(범위 안에서 스스로)다. 도구를 쓰기 직전에 실행 런타임(`common/runtime.py`)이 이 둘을 맞대 본다. 과제 목록·매뉴얼·티켓·로그·기준값은 모두 교육용 가상 데이터다.

## C-2. 준비물

준비할 것은 넷이다.

첫째, Python 3.10 이상이다. 아래 명령으로 버전을 확인하자. macOS에서는 `python` 대신 `python3`으로 불러야 하는 경우가 많다. 그때는 이 부록의 `python`을 모두 `python3`으로 바꿔 읽으면 된다.

```bash
python --version
```

둘째, Anthropic API 키(외부 프로그램이 Claude를 부를 때 내미는 증표)다. Anthropic 콘솔에서 발급한다. 실제 실행에는 사용료가 든다(C-7).

셋째, 예제 저장소다. git을 쓸 수 있다면 이렇게 받는다.

```bash
git clone https://github.com/ksangki/ax-system.git
cd ax-system/examples/digital-workers
```

git이 없다면 저장소 웹 페이지의 `Code` 단추에서 `Download ZIP`을 눌러 받아도 된다. 압축을 풀고 그 안의 `examples/digital-workers` 폴더에서 터미널을 연다. 다만 ZIP으로 받으면 뒤에 나오는 `git checkout` 되돌리기 명령을 쓸 수 없다. 그때는 압축을 다시 풀면 처음으로 돌아간다. 이후 명령은 모두 이 폴더 안에서 입력한다.

넷째, 필요한 패키지다. `requirements.txt`에 적힌 세 가지(`anthropic`, `ruamel.yaml`, `PyYAML`)가 설치된다. `pip`을 찾을 수 없다는 말이 나오면 `python -m pip install -r requirements.txt`로 바꿔 입력하자.

```bash
pip install -r requirements.txt
```

마지막으로 키를 넘긴다. 키는 코드에도, 파일에도, 채팅 창에도 적지 않는다. 환경 변수(지금 연 터미널 창에만 잠시 걸어 두는 값)로 넘긴다. 이유는 5장과 10장에 이미 있다. 자격 증명은 등록부의 한 칸이고, 폐기할 때 가장 먼저 회수하는 것이다. 키를 파일 여기저기에 적어 두면 회수할 때 어디에 복사돼 있는지 아무도 모른다. 예제도 같은 규칙을 지킨다. 키가 없으면 `run.py`는 `ANTHROPIC_API_KEY 환경 변수가 없습니다. 키는 코드나 파일에 적지 말고 환경 변수로 넘기세요.`라는 문장을 남기고 멈춘다.

macOS·Linux 터미널에서는 이렇게 입력한다.

```bash
export ANTHROPIC_API_KEY="여기에-발급받은-키"
```

Windows PowerShell에서는 이렇게 입력한다.

```powershell
$env:ANTHROPIC_API_KEY = "여기에-발급받은-키"
```

이 값은 그 창을 닫으면 사라진다. 새 창을 열었다면 다시 입력하자. 혹시 키가 어딘가에 노출됐다면 콘솔에서 그 키를 지우고 새로 발급받는 편이 안전하다.

## C-3. 먼저 비용 없이 점검하기

키를 넣기 전에도 돌려 볼 수 있는 명령이 하나 있다.

```bash
python tests/dry_run.py
```

이 점검은 Claude 대신 가짜 상대를 끼운다. 가짜 상대는 미리 정해 둔 순서대로 도구를 부를 뿐이다. 그래서 API 키도, 인터넷 연결도, 비용도 들지 않는다. 패키지 설치만 끝나 있으면 된다.

무엇을 검사할까? 모델의 바깥에 세운 체계다. 등록부 확인, 행위 허가의 네 갈래(`auto`·`approve`·`suggest`·등록부에 없음), 사람에게 넘김, 산출물 형식 검증, 감사·비용 로그, 폐기 실행을 차례로 건드린다. 화면에는 일부러 틀리게 부른 결과가 함께 나온다. 예를 들어 ③이 없는 심각도 `S0`를 적으면 `형식 오류로 저장하지 않았습니다`가 뜬다. 공지 도구를 부르면 `'send_customer_notice'은 제안만 허용됩니다.`가 뜬다. ②가 등록부 파일을 읽으려 하면 `등록부의 읽기 범위 밖입니다: registry.yaml`이 뜬다. ⑤가 폐기안 없이 폐기부터 요청하면 거부되고, 일곱 항목이 덜 찬 폐기안은 저장되지 않는다.

검사하지 않는 것도 분명히 해 두자. 모델의 판단이다. 판정이 맞는지, 절차서가 잘 쓰였는지는 이 점검으로 알 수 없다. 화면에 찍히는 처리 건수·토큰·금액도 가짜 상대가 정해진 값을 돌려준 결과라 실제 청구와 무관하다.

마지막 줄에 아래 문장이 나오면 통과다.

```
점검 통과: 등록부 상태 retired, 자격 증명 회수, 묘비 기록 확인
```

점검이 끝나면 `logs/`·`outputs/`·`registry.yaml`을 실행 전 상태로 되돌린다. 저장소에 든 기록본은 그대로 남는다.

## C-4. 실제로 돌리기

이제 키를 넣고 하나씩 돌려 보자.

```bash
python run.py a1
python run.py a3
python run.py all
```

`a1`~`a5`는 에이전트 하나를, `all`은 다섯을 ①부터 ⑤까지 순서대로 돌린다. 여기에 승인 방식을 정하는 옵션 `--approve`가 붙는다. 기본값은 `ask`로, 승인이 필요한 행위가 나오면 터미널에서 묻는다. `yes`는 전부 승인, `no`는 전부 거절이다. 지금 등록부에서 `approve` 수준인 행위는 ⑤의 폐기 실행(`retire_agent`) 하나뿐이다. 그래서 질문은 ⑤에서만 뜬다. 모양은 이렇다(둘째 줄에는 에이전트가 적은 폐기 사유가 들어간다).

```
  ┌ 승인 요청 [AGT-005] retire_agent
  │ AGT-901 주간 VOC 요약 봇 — (폐기 사유)
  └ 승인할까요? (y/N)
```

`y`·`yes`·`예`·`ㅇ`을 입력하면 승인이고, 그 밖의 입력은 엔터만 친 경우까지 모두 거절이다. 기억해 두자. 책에 실린 실행 기록은 `python run.py all --approve yes`, 곧 데모용 자동 '예'로 돌린 결과다. 10장 상자가 정직하게 적었듯, 그 승인 앞에는 사람이 서 있지 않았다. 직접 돌릴 때는 기본값 `ask`로 두고 질문에 손수 답해 보는 편이 낫다.

하나씩 돌릴 때는 순서가 결과를 바꾼다. ①과 ②는 앞 단계 없이 돌아간다. ③은 시작하자마자 `절차서: …` 한 줄을 찍는다. 코드는 ②의 결과물 `outputs/sop_incident_triage.md`를 먼저 찾고, 없을 때만 미리 써 둔 예비본 `data/sop_incident_triage_fallback.md`를 읽는다. 저장소에는 ②의 2026년 10월 10일 결과물이 들어 있어서, 받은 그대로 ③만 돌려도 그 절차서를 쓴다. 처음 상태로 비운 뒤 ②를 건너뛰면 예비본으로 돈다. 예비본은 ②가 매뉴얼에서 뽑아낸 절차서가 아니다. 그러니 7장 상자의 '배정 0건'으로 이어진 사슬은 그대로 재현되지 않는다.

④는 `logs/usage.jsonl`에 쌓인 기록을 읽는다. 기록이 없는 에이전트에는 `AGT-001의 실행 기록이 없습니다. 먼저 그 에이전트를 실행하세요.` 같은 답이 돌아온다. 기준값이 있는 것도 AGT-001~003뿐이다. 또 ④는 그 파일의 모든 줄을 더한다. 기록본 위에 새로 돌리면 2026년 10월 10일 기록과 당신의 실행이 합쳐져 환산된다. 내 실행만 보고 싶다면 C-5의 '처음 상태로 되돌리기'를 먼저 하자.

⑤는 실제로 등록부 파일을 고친다. AGT-901을 폐기하면 그 칸의 상태가 `retired`로 바뀌고 자격 증명 목록이 비며 묘비(폐기 기록)가 붙는다. 되돌리지 않고 다시 돌리면 `이미 retired 상태입니다.`라는 답을 받는다.

실행이 끝날 때마다 요약 한 줄이 나온다. 2026년 10월 10일 ①의 기록이라면 이렇다.

```
  처리 18건 · 사람 개입 0회 · 토큰 입력 17,110 / 출력 9,119 · 약 $0.241
```

'처리'는 에이전트가 일을 하나 마칠 때마다 센 수다. ①은 판정, ②는 열린 질문, ③은 분석안, ④는 환산, ⑤는 재심사 사건을 센다. '사람 개입'은 승인 요청과 사람에게 넘긴 건을 더한 값으로, 8장 자율성 계수의 재료다. 입력 토큰은 일반 입력·캐시 쓰기·캐시 읽기를 모두 더한 값이다. 금액은 코드에 적힌 단가로 낸 추정치다. 같은 내용이 `logs/usage.jsonl`에 한 줄씩 쌓인다.

## C-5. 결과 읽는 법

결과 파일은 상자와 짝을 이룬다. 다음을 먼저 보면 된다.

- **①** `a1_report.md`에서 떨어진 과제가 어느 관문에서 왜 떨어졌는지 보고, `a1_verdicts.jsonl`에서 과제마다 남은 판정 한 줄(`tier`, 보류 여부 `hold`)을 본다. 2장 상자의 보류 2건이 여기 있다.
- **②** `sop_incident_triage.md`의 단계마다 붙은 '사람 확인' 줄과 '임시값' 표시를 보고, `a2_open_questions.md`의 질문을 본다. 4장 상자의 질문 9개가 이것이다.
- **③** `a3_triage.jsonl`의 `assigned` 값(실제 배정 여부)과 `team` 값을 본다. `suggestions.jsonl`은 제안으로 막힌 행위가 있을 때만 생긴다. 기록본에 이 파일이 없는 것이 곧 7장 상자의 '공지 제안 0건'이다.
- **④** `a4_performance_report.md` 맨 앞의 사용 제한 선언과 1단·2단 FTE 표를 본다(8장).
- **⑤** `a5_review_flags.md`의 재심사 사건과 `retirement_plan_AGT-901.md`의 일곱 항목을 본다(10장). 저장소의 `registry.yaml`은 폐기 전 상태로 들어 있다. 직접 돌려 폐기를 승인했다면 AGT-901 칸에 `tombstone`(묘비)이 붙은 것을 볼 수 있다.

로그는 두 파일이다. `logs/audit.jsonl`은 감사 로그로, 한 줄이 사건 하나다. 줄마다 시각, 실행 번호, 에이전트, 사건 종류(`event`)가 적힌다. `logs/usage.jsonl`은 실행 한 번에 한 줄로, 토큰·금액·처리 건수·사람 개입 수와 끝난 이유(`stop_reason`)가 적힌다. `end_turn`이면 정상 종료다.

| 사건 (`event`) | 뜻 | 기록본 건수 |
|---|---|---|
| `run_start` / `run_end` | 실행 시작·끝 | 5 / 5 |
| `read` | 등록부가 허락한 범위에서 파일을 읽음 | 19 |
| `action_auto` | `auto` 행위를 스스로 실행함 | 69 |
| `handoff_to_human` | 판정 보류로 사람에게 넘김 | 1 |
| `action_approved` | 사람(또는 데모 옵션)이 승인함 | 1 |
| `agent_retired` | 에이전트를 폐기함 | 1 |
| `action_suggested` · `action_rejected` · `action_denied` · `read_denied` · `output_invalid` · `run_blocked` | 제안으로 막힘 · 승인 거절 · 등록부에 없는 행위 · 읽기 범위 밖 · 형식 오류 · 등록부 상태 때문에 시작 안 함 | 0 |

특정 사건만 골라 보려면 메모장 같은 편집기로 열어 사건 이름을 검색해도 되고, 아래 명령을 써도 된다. 기록본에서는 T-1008을 넘긴 한 줄이 나온다.

```bash
grep handoff_to_human logs/audit.jsonl
```

PowerShell에서는 `Select-String handoff_to_human logs/audit.jsonl`이다. 같은 방법으로 `action_suggested`를 찾아보자. 기록본에는 없다. 당신의 실행에서 나온다면, 이번에는 모델이 공지 도구를 불렀고 등록부가 그것을 제안으로 돌렸다는 뜻이다.

저장소의 `logs/`·`outputs/`에는 2026년 10월 10일 기록본이 들어 있다. 상자 숫자의 원본이다. 직접 돌리면 결과 파일은 덮어쓰이고 로그는 그 뒤에 이어 쌓인다. 기록본으로 되돌리는 명령은 이렇다.

```bash
git checkout -- logs outputs registry.yaml
```

기록을 모두 비운 처음 상태에서 시작하려면 이렇게 한다(macOS·Linux). Windows에서는 `logs`와 `outputs` 폴더 안의 파일을 탐색기에서 지운 뒤 `git checkout registry.yaml`만 입력하면 된다.

```bash
rm -f logs/*.jsonl outputs/* && git checkout registry.yaml
```

## C-6. 바꿔 보기

직접 고쳐 볼 차례다. 등록부를 고칠 때는 먼저 C-3의 점검으로 확인하자. 점검은 고친 등록부를 그대로 쓰고, 끝난 뒤에도 고친 상태를 남겨 둔다. 비용 없이, 매번 같은 순서로 결과를 볼 수 있다. 다 보고 나면 `git checkout registry.yaml`로 되돌린다.

**실험 1 — 허용 수준 한 칸 바꾸기.** `registry.yaml`의 AGT-003 칸에서 `assign_ticket: auto`를 `assign_ticket: suggest`로 고친다. 점검을 돌리면 배정 줄이 `배정했습니다`에서 `'assign_ticket'은 제안만 허용됩니다.`로 바뀐다. 실제 실행에서는 배정 요청이 `outputs/suggestions.jsonl`과 감사 로그의 `action_suggested`로 가고, `a3_triage.jsonl`의 `assigned`는 그대로 `false`다. 다만 7장 상자처럼 절차서가 배정을 이미 묶었다면, 에이전트가 배정 도구를 아예 부르지 않아 차이가 안 보일 수 있다. 통제가 두 겹이라는 것도 관찰이다. 반대 방향은 더 아찔하다. `send_customer_notice: suggest`를 `auto`로 바꾸면 도구가 `발송했습니다.`를 돌려주고, 제안 목록에는 아무것도 남지 않는다. 예제에서는 실제로 나가는 것이 없다. 하지만 실제 시스템이라면 되돌릴 수 없는 대외 공지가 사람 손을 거치지 않고 나간다. 7장에서 본 것처럼, 같은 집행이라도 되돌릴 수 있느냐에 따라 허용 수준이 갈린다. 이 한 줄을 바꾸는 일은 재심사를 거치는 편이 낫다(10장).

**실험 2 — 등록부에 없는 행위.** AGT-003 칸에서 `assign_ticket: auto` 줄을 통째로 지운다. 도구는 코드에 그대로 있지만 점검 화면에는 `거부됨: 'assign_ticket'은 등록부에 없는 행위입니다. 실행하지 않았습니다.`가 뜨고, 감사 로그에는 `action_denied`가 남는다. 할 수 있는 것과 해도 되는 것이 다른 파일에 있다는 7장의 논지다. 한 걸음 더 가 보자. 같은 칸의 `status: active`를 `status: paused`로 바꾸면 ③은 `[AGT-003] 등록부 상태가 'paused'라 실행하지 않습니다.`를 남기고 시작조차 하지 않는다. 등록부가 문서가 아니라 스위치가 되는 자리다(5장).

**실험 3 — 폐기 승인을 거절하기.** 등록부를 기록본으로 되돌린 뒤 이렇게 돌린다.

```bash
python run.py a5 --approve no
```

감사 로그에 `action_rejected`가 남고, 에이전트는 `담당자가 'retire_agent'을 승인하지 않았습니다. 실행하지 않았습니다.`라는 답을 받는다. 폐기안을 썼다면 그 파일은 남지만, AGT-901의 상태와 자격 증명 셋은 그대로다. 요약 줄의 사람 개입은 거절도 1회로 센다. 이번에는 `--approve` 없이 돌려 직접 `y`를 눌러 보자. 승인 버튼 앞에 누가 서야 하는지 몸으로 알게 된다(10장 체크리스트 ①).

**실험 4 — 가상 데이터를 우리 상황에 맞게.** `data/projects.csv`에 당신 조직에 있을 법한 과제를 지어내 몇 줄 보태고 ①을 돌린다. 열은 `id,name,team,description,status,touches,users` 일곱이다. `data/baselines.yaml`에서 건당 사람 소요시간(`human_minutes_per_item`), 월 처리량(`monthly_volume`), 숫자의 출처 등급(`evidence` — 실측·표본·자기보고)을 바꾸고 ④를 돌리면 FTE가 따라 움직인다. 이 숫자는 모델이 아니라 코드가 계산한다. 8장의 분자·분모가 누구 손에 있는지 실감하게 된다. 티켓은 `data/incidents/tickets.json`과 `data/incidents/logs/`의 로그 파일을 짝으로 고친다. 단, 여기에 넣는 내용은 외부 API로 전송된다. 실제 조직 데이터, 고객 정보, 개인정보는 넣지 말자. 이름도 숫자도 지어낸 값만 쓰자.

## C-7. 비용과 주의

2026년 10월 10일에 다섯을 한 번씩 돌린 합계는 입력 127,330토큰, 출력 36,413토큰, 약 1.004달러였다(저장소 `README.md`의 실행 기록). 한 번에 0.06~0.29달러 꼴이다. 금액은 `common/runtime.py`의 단가표 `PRICE`로 계산한다. 100만 토큰당 입력 4달러, 출력 20달러, 캐시 쓰기 5달러, 캐시 읽기 0.20달러로, 2026년 10월 기준 공개 가격이다. 가격은 바뀔 수 있고, 실제 청구액은 Anthropic 콘솔에서 확인한다.

모델의 출력은 실행할 때마다 달라진다. 판정 건수, 열린 질문 수, 심각도 분포, 금액이 책과 다르게 나와도 정상이다. 같아야 하는 것은 따로 있다. 등록부가 막는 것이다. `suggest`로 묶인 공지는 발송되지 않는다. 등록부에 없는 행위는 거부된다. `approve` 행위는 승인 없이 실행되지 않는다. 형식이 틀린 분석안은 저장되지 않는다. 사람에게 넘긴 건은 사람 개입으로 세어진다. 이 다섯이 어긋난다면 모델 탓이 아니라 체계의 결함이니 저장소에 알려 주기 바란다.

사내망에서 돌린다면 한 가지를 미리 확인하자. C-3의 점검은 외부 연결 없이 끝난다. 하지만 실제 실행은 외부 API를 부르므로, 외부 접속이 막혔거나 프록시(외부로 나가는 길목 서버)를 거쳐야 하는 환경에서는 연결 오류가 날 수 있다. 회사 키를 써도 되는지, 어떤 데이터까지 외부 AI에 보내도 되는지는 보안 담당과 먼저 정해 두자. 이 책이 열 장 내내 말한 순서 그대로다. 해도 되는 것을 먼저 정하고, 그다음에 돌린다.
