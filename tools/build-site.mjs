// 生成 GitHub Pages 首页 index.html —— files-hub 通用版
// 用法: node tools/build-site.mjs [仓库根目录]
import fs from 'node:fs';
import path from 'node:path';

const OWNER = 'fengbu12-design';
const REPO = 'files-hub';
const BRANCH = 'main';
const SITE = `https://${OWNER}.github.io/${REPO}/`;

const ROOT = path.resolve(process.argv[2] || '.');

// 不参与索引的目录
const SKIP_DIRS = new Set(['.git', '.github', '.preview', '_previews', '_private', 'node_modules',
                           'profile', 'state', 'failures', 'tools', '__pycache__']);
const SKIP_FILES = new Set(['index.html', '.gitignore', '.gitattributes', '_groups.json',
                            'README.md', 'Thumbs.db', 'desktop.ini']);

// 可选：目录到中文标题的映射，放在仓库根 _groups.json
let TITLES = {};
try { TITLES = JSON.parse(fs.readFileSync(path.join(ROOT, '_groups.json'), 'utf8')); } catch { TITLES = {}; }

const TYPES = {
  md: { l: 'MD', c: 'blue' }, txt: { l: 'TXT', c: 'gray' }, csv: { l: 'CSV', c: 'green' },
  r: { l: 'R', c: 'blue' }, py: { l: 'PY', c: 'blue' }, mjs: { l: 'JS', c: 'yellow' },
  js: { l: 'JS', c: 'yellow' }, ts: { l: 'TS', c: 'blue' }, json: { l: 'JSON', c: 'yellow' },
  yml: { l: 'YML', c: 'purple' }, yaml: { l: 'YML', c: 'purple' }, html: { l: 'HTML', c: 'orange' },
  css: { l: 'CSS', c: 'purple' }, ipynb: { l: 'IPY', c: 'orange' },
  docx: { l: 'DOC', c: 'word' }, doc: { l: 'DOC', c: 'word' }, pdf: { l: 'PDF', c: 'red' },
  xlsx: { l: 'XLS', c: 'excel' }, xls: { l: 'XLS', c: 'excel' },
  pptx: { l: 'PPT', c: 'ppt' }, ppt: { l: 'PPT', c: 'ppt' },
  png: { l: 'IMG', c: 'teal' }, jpg: { l: 'IMG', c: 'teal' }, jpeg: { l: 'IMG', c: 'teal' },
  gif: { l: 'IMG', c: 'teal' }, webp: { l: 'IMG', c: 'teal' }, svg: { l: 'SVG', c: 'teal' },
  mp4: { l: 'VID', c: 'purple' }, mp3: { l: 'SND', c: 'purple' },
  zip: { l: 'ZIP', c: 'gray' }, rar: { l: 'ZIP', c: 'gray' }, '7z': { l: 'ZIP', c: 'gray' },
};
const IMG = new Set(['png', 'jpg', 'jpeg', 'gif', 'webp', 'svg']);
const OFFICE = new Set(['docx', 'doc', 'xlsx', 'xls', 'pptx', 'ppt']);

const enc = (p) => p.split('/').map(encodeURIComponent).join('/');
const blobUrl = (p) => `https://github.com/${OWNER}/${REPO}/blob/${BRANCH}/${enc(p)}`;
const rawUrl = (p) => `https://raw.githubusercontent.com/${OWNER}/${REPO}/${BRANCH}/${enc(p)}`;
const pdfPath = (p) => '_previews/' + p.replace(/\.[^./]+$/, '') + '.pdf';
const hasPdf = (p) => fs.existsSync(path.join(ROOT, pdfPath(p)));

function human(bytes) {
  if (bytes < 1024) return bytes + ' B';
  if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB';
  return (bytes / 1024 / 1024).toFixed(2) + ' MB';
}

function walk(dir, rel, out) {
  let entries;
  try { entries = fs.readdirSync(dir, { withFileTypes: true }); } catch { return; }
  for (const e of entries) {
    const r = rel ? rel + '/' + e.name : e.name;
    if (e.isDirectory()) {
      if (SKIP_DIRS.has(e.name)) continue;
      walk(path.join(dir, e.name), r, out);
    } else if (e.isFile()) {
      if (!rel && SKIP_FILES.has(e.name)) continue;
      if (/^~\$/.test(e.name) || e.name === '.DS_Store') continue;
      const st = fs.statSync(path.join(dir, e.name));
      out.push({ path: r, size: st.size, mtime: st.mtime, ext: path.extname(e.name).slice(1).toLowerCase() });
    }
  }
}

const files = [];
walk(ROOT, '', files);

const groups = new Map();
for (const f of files) {
  const seg = f.path.includes('/') ? f.path.split('/')[0] : '';
  if (!groups.has(seg)) groups.set(seg, []);
  groups.get(seg).push(f);
}
// 目录在前（按名称），根目录文件最后
const keys = [...groups.keys()].filter((k) => k !== '').sort((a, b) => a.localeCompare(b, 'zh'));
if (groups.has('')) keys.push('');

const totalBytes = files.reduce((a, f) => a + f.size, 0);
const builtAt = new Date().toLocaleString('zh-CN', { timeZone: 'Asia/Shanghai', hour12: false });
const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

function fileRow(f) {
  const t = TYPES[f.ext] || { l: (f.ext || 'FILE').slice(0, 4).toUpperCase(), c: 'gray' };
  const name = f.path.split('/').pop();
  const sub = f.path.includes('/') ? f.path.slice(f.path.indexOf('/') + 1, f.path.length - name.length) : '';
  const isHtml = f.ext === 'html' || f.ext === 'htm';
  const acts = isHtml
    ? [`<a class="act act-main" href="${SITE}${enc(f.path)}" target="_blank" rel="noopener">打开</a>`,
       `<a class="act" href="${rawUrl(f.path)}" target="_blank" rel="noopener" download>下载</a>`]
    : [`<a class="act" href="${blobUrl(f.path)}" target="_blank" rel="noopener">预览</a>`,
       `<a class="act" href="${rawUrl(f.path)}" target="_blank" rel="noopener" download>下载</a>`];
  if (OFFICE.has(f.ext) && hasPdf(f.path)) {
    acts.push(`<a class="act act-main" href="${SITE}${enc(pdfPath(f.path))}" target="_blank" rel="noopener">在线阅读</a>`);
  }
  const thumb = IMG.has(f.ext)
    ? `<a class="thumb" href="${rawUrl(f.path)}" target="_blank" rel="noopener"><img loading="lazy" src="${rawUrl(f.path)}" alt=""></a>`
    : '';
  const nameHref = isHtml ? `${SITE}${enc(f.path)}` : blobUrl(f.path);
  return `        <li class="file" data-name="${esc(f.path.toLowerCase())}">
          <span class="ext ext-${t.c}">${t.l}</span>
          ${thumb}
          <div class="meta">
            <a class="fname" href="${nameHref}" target="_blank" rel="noopener">${esc(name)}</a>
            <span class="sub">${sub ? esc(sub) : ''}<span class="size">${human(f.size)}</span><span class="date">${f.mtime.toLocaleDateString('zh-CN')}</span></span>
          </div>
          <div class="acts">${acts.join('')}</div>
        </li>`;
}

const sections = [];
for (const key of keys) {
  const list = groups.get(key);
  if (!list || !list.length) continue;
  // 网页/说明类文件排前面，剩下的按路径
  const RANK = { html: 0, htm: 0, md: 1, pdf: 2 };
  list.sort((a, b) => (RANK[a.ext] ?? 3) - (RANK[b.ext] ?? 3) || a.path.localeCompare(b.path, 'zh'));
  const title = key === '' ? '根目录文件' : (TITLES[key] || key);
  // 该目录里有 index.html 就给一个整页入口
  const entry = key ? list.find((f) => f.path.toLowerCase() === (key + '/index.html').toLowerCase()) : null;
  const openAll = entry
    ? `<a class="act act-main" href="${SITE}${enc(entry.path)}" target="_blank" rel="noopener">打开</a>`
    : '';
  const clamp = list.length > 12;
  const more = clamp
    ? `      <button class="more" type="button">显示全部 ${list.length} 个文件</button>\n`
    : '';
  sections.push(`    <section class="group">
      <h2>${esc(title)} <span class="count">${list.length}</span><span class="h2acts">${openAll}</span></h2>
      <ul class="files${clamp ? ' clamp' : ''}">
${list.map(fileRow).join('\n')}
      </ul>
${more}    </section>`);
}

const body = sections.length
  ? sections.join('\n')
  : `    <p class="placeholder">还没有托管任何文件。把文件夹或文件交给助手发布后，这里会自动出现。</p>`;

const html = `<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<meta name="robots" content="noindex, nofollow, noarchive, nosnippet">
<meta name="referrer" content="no-referrer">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%232f6feb'/%3E%3Cpath d='M9 12h14M9 16h14M9 20h9' stroke='white' stroke-width='2.5' stroke-linecap='round'/%3E%3C/svg%3E">
<title>文件库 · ${OWNER}</title>
<style>
  :root{
    --bg:#f6f7f9; --card:#fff; --text:#1a1d23; --muted:#6b7280; --line:#e6e8ec;
    --accent:#2f6feb; --accent-soft:#eaf1ff; --shadow:0 1px 2px rgba(16,24,40,.06),0 4px 14px rgba(16,24,40,.05);
  }
  @media (prefers-color-scheme:dark){
    :root{ --bg:#0f1115; --card:#171a21; --text:#e7e9ee; --muted:#9aa3b2; --line:#262b36;
           --accent:#6ea8ff; --accent-soft:#1b2433; --shadow:0 1px 2px rgba(0,0,0,.4); }
  }
  *{box-sizing:border-box}
  body{margin:0;background:var(--bg);color:var(--text);
       font:15px/1.55 -apple-system,"Segoe UI","Microsoft YaHei",system-ui,sans-serif;}
  header{padding:40px 24px 24px;max-width:960px;margin:0 auto}
  h1{margin:0 0 6px;font-size:26px;letter-spacing:-.02em}
  .sub-line{color:var(--muted);font-size:13px;margin-bottom:18px}
  .sub-line a{color:var(--accent);text-decoration:none}
  .search{width:100%;padding:11px 14px;border:1px solid var(--line);border-radius:10px;
          background:var(--card);color:var(--text);font-size:15px;outline:none;box-shadow:var(--shadow)}
  .search:focus{border-color:var(--accent)}
  main{max-width:960px;margin:0 auto;padding:0 24px 64px}
  .group{margin-top:28px}
  h2{font-size:14px;font-weight:600;color:var(--muted);margin:0 0 10px;display:flex;align-items:center;gap:8px}
  h2 .count{background:var(--accent-soft);color:var(--accent);border-radius:999px;
            padding:1px 8px;font-size:12px;font-weight:600}
  h2 .h2acts{margin-left:auto}
  h2 .h2acts .act{font-size:12.5px;padding:5px 12px;border-radius:7px;text-decoration:none;
                  color:#fff;background:var(--accent);border:1px solid var(--accent)}
  ul.files.clamp li.file:nth-child(n+13){display:none}
  .more{display:block;width:100%;margin-top:8px;padding:9px;border:1px dashed var(--line);
        border-radius:10px;background:transparent;color:var(--muted);font:inherit;font-size:13px;cursor:pointer}
  .more:hover{color:var(--accent);border-color:var(--accent)}
  ul.files{list-style:none;margin:0;padding:0;background:var(--card);border:1px solid var(--line);
           border-radius:14px;overflow:hidden;box-shadow:var(--shadow)}
  li.file{display:flex;align-items:center;gap:12px;padding:12px 16px;border-top:1px solid var(--line)}
  li.file:first-child{border-top:none}
  li.file:hover{background:var(--accent-soft)}
  .ext{flex:none;width:38px;height:38px;border-radius:9px;display:grid;place-items:center;
       font-size:10px;font-weight:700;letter-spacing:.03em;color:#fff;background:#8a93a3}
  .ext-blue{background:#2f6feb}.ext-gray{background:#8a93a3}.ext-green{background:#1a9e6a}
  .ext-yellow{background:#c08a1e}.ext-purple{background:#8a5cf6}.ext-orange{background:#e0671b}
  .ext-word{background:#2b579a}.ext-excel{background:#1e7145}.ext-ppt{background:#b7472a}
  .ext-red{background:#c03a3a}.ext-teal{background:#0e8c9a}
  .thumb{flex:none;width:38px;height:38px;border-radius:9px;overflow:hidden;border:1px solid var(--line)}
  .thumb img{width:100%;height:100%;object-fit:cover;display:block}
  .meta{min-width:0;flex:1}
  .fname{color:var(--text);text-decoration:none;font-weight:500;display:block;
         overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
  .fname:hover{color:var(--accent)}
  .sub{color:var(--muted);font-size:12px;display:flex;gap:10px;flex-wrap:wrap}
  .size,.date{font-variant-numeric:tabular-nums}
  .acts{flex:none;display:flex;gap:6px}
  .act{font-size:12.5px;padding:5px 10px;border-radius:7px;text-decoration:none;
       color:var(--muted);border:1px solid var(--line);background:var(--card);white-space:nowrap}
  .act:hover{color:var(--accent);border-color:var(--accent)}
  .act-main{color:#fff;background:var(--accent);border-color:var(--accent)}
  .act-main:hover{color:#fff;opacity:.9}
  .empty{color:var(--muted);text-align:center;padding:40px 0;display:none}
  .placeholder{color:var(--muted);text-align:center;padding:64px 0;font-size:14px}
  footer{max-width:960px;margin:0 auto;padding:0 24px 40px;color:var(--muted);font-size:12px}
  @media (max-width:560px){
    .acts .act:not(.act-main){display:none}
    li.file{padding:10px 12px}
    header{padding:28px 16px 18px} main{padding:0 16px 48px}
  }
</style>
</head>
<body>
<header>
  <h1>文件库</h1>
  <div class="sub-line">
    跨设备访问 · 共 <b>${files.length}</b> 个文件 / ${human(totalBytes)} ·
    更新于 ${builtAt} ·
    <a href="https://github.com/${OWNER}/${REPO}" target="_blank" rel="noopener">GitHub 仓库</a>
  </div>
  <input id="q" class="search" type="search" placeholder="搜索文件名或目录…" autocomplete="off">
</header>
<main id="list">
${body}
  <p class="empty" id="empty">没有匹配的文件</p>
</main>
<footer>
  Word / Excel / PPT 若已生成 PDF 预览，会多出「在线阅读」按钮；「下载」拿到的是原始文档。
</footer>
<script>
  const q = document.getElementById('q');
  const empty = document.getElementById('empty');
  document.querySelectorAll('button.more').forEach(btn => {
    btn.addEventListener('click', () => {
      const ul = btn.previousElementSibling;
      const open = ul.classList.toggle('clamp') === false;
      btn.textContent = open ? '收起' : '显示全部 ' + ul.querySelectorAll('li.file').length + ' 个文件';
    });
  });
  q.addEventListener('input', () => {
    const k = q.value.trim().toLowerCase();
    let visible = 0;
    document.querySelectorAll('.group').forEach(g => {
      let shown = 0;
      g.querySelectorAll('li.file').forEach(li => {
        const hit = !k || li.dataset.name.includes(k);
        li.style.display = k ? (hit ? 'flex' : 'none') : '';
        if (hit) shown++;
      });
      g.style.display = shown ? '' : 'none';
      visible += shown;
    });
    empty.style.display = visible ? 'none' : 'block';
  });
</script>
</body>
</html>
`;

fs.writeFileSync(path.join(ROOT, 'index.html'), html, 'utf8');
console.log(`index.html generated: ${files.length} files, ${human(totalBytes)}`);
for (const [k, v] of groups) console.log(`  ${k || '(root)'}: ${v.length}`);
