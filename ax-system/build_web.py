#!/usr/bin/env python3
"""웹 판본(index.html) 빌드 — pandoc 산출물에 웹 전용 요소를 후처리로 주입.
EPUB(v1.2.0)과 분리된 웹 판본(v1.3.0): 삽화 6점·운영체계 도식·Executive Summary·
90일 로드맵·인쇄/모바일/다크 레이아웃. 재생성 때마다 결정적으로 동일 결과.
사용법: python3 build_web.py <출력 index.html 경로>
"""
import sys, re, subprocess, pathlib

WEB_VERSION = "1.3.0"
PUB_DATE = "2026-09-12"
HERE = pathlib.Path(__file__).resolve().parent
OUT = pathlib.Path(sys.argv[1])

# 1) mermaid 없음(수제 SVG 사용) — 04_manuscript.md 그대로 pandoc
src = HERE / "04_manuscript.md"
subprocess.run([
    "pandoc", str(src), "-s", "--embed-resources", "--toc", "--toc-depth=2",
    "--metadata", "title=디지털 워커의 시대, AI 에이전트를 조직의 성과로 만드는 체계",
    "--metadata", "lang=ko", "-o", str(OUT)
], check=True, cwd=str(HERE))

html = OUT.read_text(encoding="utf-8")

# 2) 스타일: 본문 CSS + 웹 전용 컴포넌트 CSS
STYLE = """<style>
html{-webkit-text-size-adjust:100%;text-size-adjust:100%;background:#faf9f6}
body{max-width:46em;margin:0 auto;padding:0 1.2em 3em;line-height:1.78;font-size:17px;color:#2b2b28;background:#faf9f6;font-family:'Apple SD Gothic Neo','Pretendard','Noto Sans KR',sans-serif}
h1,h2,h3{color:#23211d}
h1{margin-top:2.2em;line-height:1.3}
a,a:visited{color:#8a6320;text-decoration:none;border-bottom:1px solid #d9c9a3}
a:hover{color:#5f4415;border-bottom-color:#8a6320}
nav#TOC{background:#f3efe6;border:1px solid #e0d8c4;border-radius:10px;padding:1.1em 1.5em;margin:1.6em 0}
nav#TOC ul{list-style:none;padding-left:1em;margin:.2em 0}
nav#TOC a,nav#TOC a:visited{border-bottom:none;line-height:2;color:#8a6320}
img,svg{max-width:100%;height:auto;display:block;margin:1.2em auto}
table{display:block;overflow-x:auto;border-collapse:collapse;margin:1.4em 0;width:max-content;max-width:100%}
@media(min-width:50rem){table{max-width:calc(50vw + 21em)}}
table col{width:auto!important}
th,td{border:1px solid #ddd6c4;padding:.5em .8em;vertical-align:top}
th{background:#f3efe6}
blockquote{border-left:3px solid #c9a55a;margin-left:0;padding-left:1.1em;color:#5a544a}
figure.editorial-illustration{margin:2.2em 0 2.8em}
figure.editorial-illustration img{width:100%;border-radius:12px;box-shadow:0 12px 30px rgba(35,33,29,.10)}
figure.editorial-illustration figcaption{text-align:center;color:#756e61;font-size:.82em;margin-top:.7em}
.front-matter{margin:3.2em 0;padding-top:.3em}
.front-matter .eyebrow{color:#9a6e22;font-size:.78em;font-weight:700;letter-spacing:.16em;text-transform:uppercase}
.executive-card{background:#f3efe6;border:1px solid #ded3bc;border-radius:14px;padding:1.5em 1.6em;margin:1.2em 0}
.executive-card h3{margin-top:.2em}
.decision-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:.8em;margin:1.1em 0}
.decision-grid>div{background:#fffdf8;border-left:4px solid #c9963f;padding:.85em 1em;border-radius:4px}
.decision-grid strong{display:block;color:#23211d;margin-bottom:.2em}
.lifecycle{background:#f3efe6;border:1px solid #ded3bc;border-radius:14px;padding:1.2em;margin:1.2em 0 2.4em}
.lifecycle-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:.65em}
.life-step{position:relative;background:#fffdf8;border:1px solid #d9cfb8;border-radius:9px;padding:.85em;min-height:5.4em}
.life-step b{display:block;color:#8a6320;font-size:.78em;letter-spacing:.05em;margin-bottom:.3em}
.life-step strong{display:block;color:#23211d}
.life-step span{display:block;color:#6f6a5e;font-size:.82em;line-height:1.45;margin-top:.2em}
.registry-core{background:#16222e;color:#f3efe4;border-radius:9px;padding:.9em 1em;margin:.7em 0;text-align:center;font-weight:700}
.registry-core small{display:block;color:#c9b98f;font-weight:400;margin-top:.2em}
.roadmap{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:.8em;margin:1.2em 0 2.6em}
.roadmap-phase{border-top:5px solid #c9963f;background:#f3efe6;border-radius:7px;padding:1em}
.roadmap-phase:nth-child(2){border-top-color:#5c7a52}
.roadmap-phase:nth-child(3){border-top-color:#16222e}
.roadmap-phase h3{font-size:1em;margin:.1em 0 .6em}
.roadmap-phase ul{font-size:.88em;padding-left:1.25em}
.roadmap-phase .gate{display:block;border-top:1px solid #d9cfb8;margin-top:.8em;padding-top:.7em;color:#6f5423;font-size:.83em;font-weight:700}
@media (prefers-color-scheme: dark){
 html{background:#10161f} body{background:#10161f;color:#d8d4c8} h1,h2,h3{color:#ece8dc}
 a,a:visited{color:#e3b45f;border-bottom-color:#6b5426} a:hover{color:#f0cc85;border-bottom-color:#e3b45f}
 nav#TOC{background:#18212d;border-color:#2a3644} nav#TOC a,nav#TOC a:visited{color:#e3b45f}
 th,td{border-color:#334050} th{background:#18212d}
 blockquote{border-left-color:#a3803c;color:#a8a396}
 img[src$=".svg"],img[src^="data:image/svg"]{background:#f7f3ea;border-radius:10px;padding:6px}
 figure.editorial-illustration figcaption{color:#aaa394}
 .executive-card,.lifecycle,.roadmap-phase{background:#18212d;border-color:#2a3644}
 .decision-grid>div,.life-step{background:#10161f;border-color:#334050}
 .decision-grid strong,.life-step strong{color:#ece8dc}
 .life-step span{color:#aaa394}
 .registry-core{background:#0b1119;border:1px solid #334050}
 .roadmap-phase .gate{border-color:#334050;color:#e3b45f}
}
@media print{
 figure.editorial-illustration,.front-matter,.lifecycle,.roadmap{break-inside:avoid}
 .executive-card,.lifecycle,.roadmap-phase{background:#fff!important}
}
</style></head>"""
html = html.replace("</head>", STYLE, 1)

# 3) pandoc colgroup 고정폭 제거
html = re.sub(r'(<col[^>]*?)style="width:\s*[\d.]+%"', r'\1', html)

# 4) 프론티스피스 — 제목 H1 바로 뒤
FRONTIS = """
<figure class="editorial-illustration">
<img src="assets/illustrations/frontispiece.webp" alt="현장에서 자란 작은 AI 실험들이 조직의 운영체계 안으로 모여드는 모습을 표현한 삽화" />
<figcaption>바텀업이 씨앗을 만들고, 체계가 그것을 조직의 자산으로 거둔다.</figcaption>
</figure>"""
html = re.sub(r'(<h1 id="디지털-워커의-시대[^"]*">.*?</h1>)', r'\1' + FRONTIS, html, count=1, flags=re.S)

# 5) 웹 전용 front-matter 3섹션 — 서문 앞에 삽입
SECTIONS = """<section class="front-matter" aria-labelledby="한눈에-보는-운영체계">
<p class="eyebrow">AX Agent Operating System</p>
<h2 id="한눈에-보는-운영체계">한눈에 보는 운영체계</h2>
<p>이 책이 제안하는 것은 에이전트를 더 많이 만드는 기술이 아니다. 현장에서 생긴 에이전트를 <strong>발견하고, 조직의 자산으로 등록하고, 권한을 통제하며, 성과를 측정하고, 마지막에는 안전하게 내보내는 운영체계</strong>다. 각 단계는 앞 단계의 산출물을 입력으로 받는다.</p>
<div class="lifecycle" role="img" aria-label="AI 에이전트를 발견, 표준화, 등록, 인증, 권한 부여, 운영, 측정, 보상과 재배치, 폐기하는 아홉 단계 운영체계">
<div class="lifecycle-grid">
<div class="life-step"><b>01 DISCOVER</b><strong>발견</strong><span>후보 목록을 다섯 관문으로 가린다.</span></div>
<div class="life-step"><b>02 STANDARDIZE</b><strong>표준화</strong><span>실제 업무를 SOP로 적고 기계가 읽게 한다.</span></div>
<div class="life-step"><b>03 REGISTER</b><strong>등록</strong><span>목적·Owner·업무·시스템을 기록한다.</span></div>
<div class="life-step"><b>04 CERTIFY</b><strong>역량 인증</strong><span>무엇을 안정적으로 할 수 있는지 검증한다.</span></div>
<div class="life-step"><b>05 AUTHORIZE</b><strong>권한 부여</strong><span>데이터·도구·행동의 허용 범위를 정한다.</span></div>
<div class="life-step"><b>06 OPERATE</b><strong>운영</strong><span>실행·로그·비용·감사·중지 절차를 돌린다.</span></div>
</div>
<div class="registry-core">Agent Registry · Agent ID<small>신원, Owner, 버전, 권한, 비용, 평가, 상태와 폐기 기록을 전 단계에 연결한다.</small></div>
<div class="lifecycle-grid">
<div class="life-step"><b>07 MEASURE</b><strong>측정</strong><span>시간·FTE·품질·ROI를 함께 본다.</span></div>
<div class="life-step"><b>08 REWARD / REALLOCATE</b><strong>보상·재배치</strong><span>절감분을 성과로 인정하고 새 역량에 쓴다.</span></div>
<div class="life-step"><b>09 RETIRE</b><strong>폐기</strong><span>권한을 회수하고 계정을 닫고 기록을 남긴다.</span></div>
</div>
</div>
<p><strong>핵심 원리:</strong> 역량은 "할 수 있는 것"을 말하고, 권한은 "해도 되는 것"을 정한다. 운영 배치는 둘 중 더 낮은 쪽을 따른다. 그리고 등록되지 않은 에이전트는 권한도, 성과도, 폐기도 관리할 수 없다.</p>
</section>
<hr />
<section class="front-matter" aria-labelledby="임원용-요약">
<p class="eyebrow">Executive Summary</p>
<h2 id="임원용-요약">임원용 1페이지 요약</h2>
<div class="executive-card">
<h3>문제</h3>
<p>현장의 AI 활용은 빠르게 늘지만, 조직은 무엇이 실제 에이전트인지, 누가 책임지는지, 어디까지 행동해도 되는지, 얼마의 성과를 내는지 한 장부에서 보지 못한다. 과제 수는 늘어도 조직 성과로 응축되지 않는 이유다.</p>
<h3>제안</h3>
<p>위에서 과제를 다시 선정하는 대신 <strong>현장의 실험을 거두는 공통 운영체계</strong>를 만든다. 진입 조건은 실제 업무와 SOP, 중심 장부는 Agent Registry와 Agent ID, 통제 기준은 역량과 권한의 분리, 출구 조건은 권한 회수와 기록 보존이다.</p>
<h3>지금 결정할 네 가지</h3>
<div class="decision-grid">
<div><strong>1. 등록 원칙</strong>조직 자원과 권한을 쓰는 에이전트에는 공통 ID와 Owner를 부여한다.</div>
<div><strong>2. 권한 원칙</strong>성능이 높다는 이유만으로 실행 권한이 자동 확대되지 않게 한다.</div>
<div><strong>3. 측정 원칙</strong>절감 시간은 감원 명단이 아니라 품질·처리량·새 업무 재배치의 근거로 쓴다.</div>
<div><strong>4. 종료 원칙</strong>등록 시점부터 중지 조건, 권한 회수, 계정 폐기와 기록 보존을 적는다.</div>
</div>
<h3>90일 뒤 보여줄 증거</h3>
<p>완성된 전사 플랫폼이 아니라, 대표 업무 3~5개에서 <strong>후보 판정 → SOP → 등록 → 권한 → 운영 로그 → 성과 측정 → 폐기 리허설</strong>이 한 번 끝까지 이어졌다는 증거다. 그 증거가 있어야 다음 분기의 확대·중단 결정을 숫자와 책임자 이름으로 내릴 수 있다.</p>
</div>
</section>
<hr />
<section class="front-matter" aria-labelledby="90일-도입-로드맵">
<p class="eyebrow">90-Day Adoption Roadmap</p>
<h2 id="90일-도입-로드맵">90일 도입 로드맵</h2>
<p>90일의 목표는 전사 제도를 한 번에 완성하는 것이 아니다. 대표 업무 3~5개를 골라 운영체계의 전 구간을 실제로 통과시키고, 확산 전에 어디에서 막히는지 찾는 것이다.</p>
<div class="roadmap">
<section class="roadmap-phase"><h3>0–30일 · 발견과 기준</h3><ul><li>후보 목록과 현재 운영 상태 조사</li><li>다섯 관문으로 에이전트 여부 판정</li><li>대표 업무 3~5개와 Owner 선정</li><li>처리시간·품질·비용 기준선 확보</li><li>등록 스키마와 사용 제한 초안 합의</li></ul><span class="gate">GATE 1 · 실체와 책임자가 확인됐는가</span></section>
<section class="roadmap-phase"><h3>31–60일 · 등록과 통제</h3><ul><li>실제 업무를 SOP와 예외 규칙으로 작성</li><li>Agent ID 발급과 Registry 등록</li><li>역량 등급과 권한 등급을 따로 판정</li><li>최소 권한·승인 지점·중지 수단 설정</li><li>평가셋, 로그, 비용 태그 연결</li></ul><span class="gate">GATE 2 · 제한된 운영을 허가할 수 있는가</span></section>
<section class="roadmap-phase"><h3>61–90일 · 운영과 증명</h3><ul><li>제한된 사용자·업무 범위에서 운영</li><li>실패·개입·비용·감사 로그 점검</li><li>시간·FTE·품질·ROI를 함께 측정</li><li>절감분의 보상·재배치 원칙 선언</li><li>권한 회수와 폐기 절차 리허설</li></ul><span class="gate">GATE 3 · 확대·보완·중단 중 하나를 결정했는가</span></section>
</div>
<p><strong>운영 원칙:</strong> 30일마다 산출물보다 결정 근거를 남긴다. 통과하지 못한 후보를 억지로 다음 단계로 넘기지 않고, 보완이나 중단도 정상적인 결과로 기록한다.</p>
</section>
<hr />
"""
assert '<h2 id="서문">' in html, "서문 헤딩 없음"
html = html.replace('<h2 id="서문">', SECTIONS + '<h2 id="서문">', 1)

# 6) PART 삽화 — 각 PART 헤딩 뒤
part_ills = {
 "part-1": ("part-1-harvest.webp", "현장의 씨앗을 위의 체계가 물길과 수확 장치로 받치는 모습을 표현한 삽화", "위가 내려보낼 것은 과제 목록이 아니라, 거두는 체계다."),
 "part-2": ("part-2-procedure.webp", "문서에 적힌 절차와 실제 업무의 흔적이 하나의 기계가 읽는 경로로 합쳐지는 삽화", "절차는 문서가 아니라, 실제 일이 지나가는 길이어야 한다."),
 "part-3": ("part-3-registry.webp", "추상적인 디지털 워커가 신원과 권한과 비용이 연결된 조직 등록부에 들어오는 삽화", "등록은 이름표가 아니라 책임과 권한의 연결이다."),
 "part-4": ("part-4-measure.webp", "절감 시간과 품질을 저울에 올리고 새로운 업무 역량으로 돌려보내는 모습을 표현한 삽화", "무엇을 재느냐보다, 잰 숫자를 어디에 쓰느냐가 먼저다."),
 "part-5": ("part-5-retire.webp", "에이전트의 열쇠와 기록이 회수되고 열린 출구 너머에 다음 학습의 씨앗이 남는 삽화", "폐기는 삭제가 아니라, 권한을 거두고 기록을 남기는 운영 절차다."),
}
def part_fig(key):
    f, alt, cap = part_ills[key]
    return f'<figure class="editorial-illustration"><img src="assets/illustrations/{f}" alt="{alt}" /><figcaption>{cap}</figcaption></figure>'
for i in range(1, 6):
    # <h1 id="part-N....">...</h1> 뒤에 삽입
    pat = re.compile(r'(<h1 id="part-' + str(i) + r'[^"]*">.*?</h1>)', re.S)
    m = pat.search(html)
    assert m, f"PART {i} 헤딩 없음"
    html = html[:m.end()] + "\n" + part_fig(f"part-{i}") + html[m.end():]

# 7) TOC에 신규 3섹션 추가 — 서문 TOC 앞
toc_new = ('<li><a href="#한눈에-보는-운영체계" id="toc-한눈에-보는-운영체계">한눈에 보는 운영체계</a></li>\n'
           '<li><a href="#임원용-요약" id="toc-임원용-요약">임원용 1페이지 요약</a></li>\n'
           '<li><a href="#90일-도입-로드맵" id="toc-90일-도입-로드맵">90일 도입 로드맵</a></li>\n')
html = re.sub(r'(<li><a href="#서문")', toc_new + r'\1', html, count=1)

# 8) 웹 판본 번호: 표제지·판권의 v1.2.0 → v1.3.0 (index.html 한정)
html = html.replace("v1.2.0", f"v{WEB_VERSION}")
html = re.sub(r'(판본:</strong>\s*v1\.3\.0\s*·\s*)2026-09-12', r'\g<1>' + PUB_DATE, html)

OUT.write_text(html, encoding="utf-8")
n_ill = html.count('editorial-illustration"><img') + html.count('class="editorial-illustration">\n')
print(f"web build 완료 — 삽화 {html.count('assets/illustrations/')}개 참조, "
      f"운영체계/Executive/로드맵 섹션 {html.count('front-matter')//1}, v{WEB_VERSION}")
