// 캐러셀 HTML의 .s 요소마다 1080×1350 PNG를 찍고 넘침을 점검한다. 이어서 carousel.pdf를 만든다(magick이 있으면).
// 사용: node carousel_shot.js <carousel.html이 있는 폴더(절대경로)> <출력 폴더>
// 출력 폴더의 예전 NN.png는 먼저 지운다(장 수를 줄였을 때 이전 페이지가 PDF에 섞이지 않게).
// 종료 코드: 0 정상 · 1 넘침·크기 오류 · 2 페이지 없음
const path = require('path'), fs = require('fs'), { execFileSync } = require('child_process');
let pw;
try { pw = require(path.join(process.env.HOME, '.claude/skills/showreel/scripts/node_modules/playwright-core')); }
catch { pw = require('playwright-core'); }
(async () => {
  const [src, out] = process.argv.slice(2);
  fs.mkdirSync(out, { recursive: true });
  for (const f of fs.readdirSync(out)) if (/^\d\d\.png$/.test(f)) fs.unlinkSync(path.join(out, f));
  const b = await pw.chromium.launch({ channel: 'chrome' }).catch(() => pw.chromium.launch());
  const pg = await b.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
  await pg.goto('file://' + path.join(src, 'carousel.html'));
  await pg.waitForTimeout(800);
  const els = await pg.$$('.s');
  if (!els.length) { console.log('.s 페이지가 없음'); await b.close(); process.exit(2); }
  let bad = 0; const files = [];
  for (let i = 0; i < els.length; i++) {
    const r = await els[i].evaluate(x => {
      const p = x.getBoundingClientRect();
      const size = Math.round(p.width) === 1080 && Math.round(p.height) === 1350;
      const out = [...x.querySelectorAll('*')].some(c => {
        const q = c.getBoundingClientRect();
        if (!q.width && !q.height) return false;
        return q.bottom > p.bottom + 1 || q.right > p.right + 1 || q.top < p.top - 1 || q.left < p.left - 1
          || c.scrollWidth > c.clientWidth + 1 && getComputedStyle(c).overflowX === 'hidden'
          || c.scrollHeight > c.clientHeight + 1 && getComputedStyle(c).overflowY === 'hidden';
      });
      return { size, out };
    });
    const f = path.join(out, String(i + 1).padStart(2, '0') + '.png');
    await els[i].screenshot({ path: f }); files.push(f);
    const ok = r.size && !r.out;
    console.log(i + 1, ok ? 'ok' : (!r.size ? 'SIZE' : 'OVERFLOW')); bad += ok ? 0 : 1;
  }
  await b.close();
  try { execFileSync('magick', [...files, path.join(out, 'carousel.pdf')]); console.log('pdf:', path.join(out, 'carousel.pdf')); }
  catch { console.log('magick 없음: PDF는 건너뜀'); }
  process.exit(bad ? 1 : 0);
})();
