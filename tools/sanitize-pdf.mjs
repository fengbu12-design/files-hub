// 抹掉 PDF 里的作者/标题/主题/关键词元数据，保持文件字节长度不变（不破坏 xref 偏移）
// 用法: node tools/sanitize-pdf.mjs <a.pdf> [b.pdf ...]
import fs from 'node:fs';

const files = process.argv.slice(2).filter((a) => !a.startsWith('--'));
if (!files.length) {
  console.error('usage: node tools/sanitize-pdf.mjs <file.pdf> ...');
  process.exit(1);
}

const FIELDS = {
  Author: ' ',
  Creator: ' ',
  Producer: ' ',
  Title: ' ',
  Subject: ' ',
  Keywords: ' ',
};

function blank(str) {
  return str.replace(/[^\r\n]/g, ' ');
}

function sanitize(raw) {
  let text = raw.toString('latin1');
  const before = Buffer.byteLength(text, 'latin1');
  const stats = {};

  // 1) Info 字典: /Author (xxx) 或 /Author <FEFF...>
  for (const key of Object.keys(FIELDS)) {
    // 字面量字符串
    const reLit = new RegExp(`(/${key}\\s*\\()((?:\\\\.|[^\\\\()])*)(\\))`, 'g');
    text = text.replace(reLit, (m, p1, body, p3) => {
      if (!body.trim()) return m;
      stats[key] = (stats[key] || 0) + 1;
      return p1 + blank(body) + p3;
    });
    // 十六进制字符串
    const reHex = new RegExp(`(/${key}\\s*<)([0-9A-Fa-f\\s]+)(>)`, 'g');
    text = text.replace(reHex, (m, p1, body, p3) => {
      const cleaned = body.replace(/\s+/g, '');
      if (!cleaned || /^0*$/.test(cleaned)) return m;
      stats[key] = (stats[key] || 0) + 1;
      // 保留 <FEFF...> 头，其余填 0（UTF-16 的 NUL）
      const zeros = '0'.repeat(cleaned.length);
      const out = cleaned.toUpperCase().startsWith('FEFF') ? 'FEFF' + zeros.slice(4) : zeros;
      return p1 + out + p3;
    });
  }

  // 2) XMP: <dc:creator><rdf:Seq><rdf:li>xxx</rdf:li></rdf:Seq></dc:creator>
  const xmpTargets = [
    ['dc:creator', /(<dc:creator>[\s\S]*?<rdf:li[^>]*>)([\s\S]*?)(<\/rdf:li>)/g],
    ['dc:title', /(<dc:title>[\s\S]*?<rdf:li[^>]*>)([\s\S]*?)(<\/rdf:li>)/g],
    ['dc:description', /(<dc:description>[\s\S]*?<rdf:li[^>]*>)([\s\S]*?)(<\/rdf:li>)/g],
    ['pdf:Producer', /(<pdf:Producer>)([\s\S]*?)(<\/pdf:Producer>)/g],
    ['xmp:CreatorTool', /(<xmp:CreatorTool>)([\s\S]*?)(<\/xmp:CreatorTool>)/g],
    ['dc:subject', /(<dc:subject>[\s\S]*?<rdf:li[^>]*>)([\s\S]*?)(<\/rdf:li>)/g],
  ];
  for (const [name, re] of xmpTargets) {
    text = text.replace(re, (m, p1, body, p3) => {
      if (!body.trim()) return m;
      stats['xmp:' + name] = (stats['xmp:' + name] || 0) + 1;
      return p1 + blank(body) + p3;
    });
  }

  // 3) 属性值内的 PDF 字符串 <rdf:li rdf:parseType="Resource"> 不处理（无敏感内容）
  const out = Buffer.from(text, 'latin1');
  if (out.length !== before) throw new Error(`length changed ${before} -> ${out.length}`);
  return { buf: out, stats };
}

let changed = 0;
for (const f of files) {
  const abs = f;
  if (!fs.existsSync(abs)) { console.error(`skip (missing): ${abs}`); continue; }
  const raw = fs.readFileSync(abs);
  const { buf, stats } = sanitize(raw);
  const keys = Object.keys(stats);
  if (!keys.length) {
    console.log(`clean  ${abs}  (无元数据)`);
    continue;
  }
  fs.writeFileSync(abs, buf);
  changed++;
  console.log(`scrub  ${abs}  ${keys.map((k) => `${k}×${stats[k]}`).join(', ')}`);
}
console.log(`\n处理完成: ${changed} 个文件已清洗 / 共 ${files.length} 个`);
