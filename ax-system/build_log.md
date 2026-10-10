# Build Log — 디지털 워커의 시대, AI 에이전트를 조직의 성과로 만드는 체계 v1.6.0

- **Date:** 2026-10-10T07:09:11Z
- **Output:** `디지털-워커의-시대,-AI-에이전트를-조직의-성과로-만드는-체계-v1.6.0.epub`
- **Size:** 390727 bytes
- **Pandoc exit:** 0
- **epubcheck:** passed
- **epubcheck strict:** 1
- **mermaid:** not present in manuscript
- **images:** 10 local reference(s), all present
- **cover alt:** injected alt="디지털 워커의 시대 표지"

## Metadata
- title: 디지털 워커의 시대, AI 에이전트를 조직의 성과로 만드는 체계
- author: 김상기
- language: ko
- version: 1.6.0
- pub_date: 2026-10-10
- identifier: urn:uuid:5cef80ff-b2ad-43fd-b003-63c0f827313f
- license: CC BY-NC-SA 4.0
- genre: tech-book
- cover_alt: 디지털 워커의 시대 표지
- stylesheet: epub.css
- harness_version: 1.11.0
- rights: © 2026 김상기 — Licensed under CC BY-NC-SA 4.0

## Phase 5 필수 확인 (epub-builder, 2026-10-10)

- **입력 원고 해시:** `04_manuscript.md` sha256 `b71af5d8be0091ebcd625331629d1e18957620139eb477da7bc4d3c7991e2ca1`, 수락본과 일치 (빌드 전후 동일)
- **표지:** 기존 `cover.png` 재사용 (196,748 bytes, cover-designer 호출 없음)
- **빌드 명령:** `bash .claude/skills/epub-build/scripts/build_epub.sh ax-system` → exit 0
- **epubcheck:** PASS (스크립트 strict=1 게이트 통과 + 단독 재실행 `epubcheck <epub>` exit 0, 오류·경고 출력 없음)
- **이미지 pre-flight:** 로컬 참조 10건(`figures/fig-01..10.svg`) 모두 존재, MISSING 0. EPUB `media/`에 SVG 10점 + cover.png 포함
- **mermaid:** 원고에 mermaid 블록 없음(그림은 사전 렌더 SVG). 해당 없음
- **콜로폰 라이선스 문자열:** 원고 `## 판권`에 `CC BY-NC-SA 4.0` 그대로 등장(ch001.xhtml), 매니페스트 `license`와 일치. 판본 v1.6.0·발행일 2026-10-10·식별자 모두 매니페스트와 일치
- **OPF 메타:** dc:title / dc:creator=김상기 / dc:language=ko / dc:date=2026-10-10 / dc:identifier=`urn:uuid:5cef80ff-b2ad-43fd-b003-63c0f827313f`(직전 판과 동일, 보존) / dc:subject=tech-book / dc:rights=`© 2026 김상기 — Licensed under CC BY-NC-SA 4.0`
- **표지 alt:** cover.xhtml에 `aria-label="디지털 워커의 시대 표지"` 주입 확인
- **사례 상자:** XHTML에 `<div class="case">` 5개 (ch005·ch007·ch011·ch013·ch016 = 2·4·7·8·10장). `stylesheet1.css`에 `div.case` 규칙 실림(라이트 + `prefers-color-scheme: dark` 보정)
- **코드 블록:** `pre.sourceCode yaml` 2 · `pre.sourceCode python` 1 · `pre.text` 2, 총 5(원고 펜스 5개와 일치). 구문 강조 span(kw·fu·co·st·at 등) 렌더, 강조 CSS는 각 xhtml `<style>`에 인라인
- **관찰(비블로킹):** pandoc 3.1.3이 SVG 그림을 `media/fileN.svgz` 확장자로 저장함(내용은 비압축 SVG, OPF media-type은 `image/svg+xml`). epubcheck는 통과. v1.3.0 EPUB은 `.svg`였다. 확장자로 형식을 판단하는 리더가 있으면 그림 표시에 문제가 생길 수 있음
- **책 소개 md:** `/home/user/book-writer/디지털-워커의-시대,-AI-에이전트를-조직의-성과로-만드는-체계-v1.6.0.md` (신규. 같은 버전 기존 파일 없음 → `_prev/` 이동 불요)

## 재빌드 — pandoc 3.9 (orchestrator, 2026-10-10)
- 위 필수 확인은 pandoc 3.1.3 빌드 기준이다. 그 빌드는 SVG 그림 10점을 `EPUB/media/fileN.svgz` 이름(내용은 비압축 SVG)으로 실어, 확장자로 형식을 판단하는 리더에서 그림이 깨질 위험이 있었다(v1.3.0은 `.svg`).
- 하네스 스크립트는 바꾸지 않고 pandoc 3.9(pypandoc_binary)를 PATH 앞에 두고 `build_epub.sh ax-system`으로 재빌드했다. 결과: `.svg` 10점·`.svgz` 0, epubcheck 통과(exit 0), `<div class="case">` 5, stylesheet에 `div.case` 규칙, 콜로폰 `CC BY-NC-SA 4.0`, 원고 sha256 b71af5d8be00 그대로. 위 Metadata 절이 재빌드 값이다.
- 하네스 후속: 환경 pandoc이 3.1.x면 같은 문제가 재발한다 — main에서 최소 pandoc 버전 점검 또는 svgz 후처리 검토.
