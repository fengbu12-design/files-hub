// 上传前隐私扫描：个人信息、涉密文本、密钥
// 用法: node tools/scan-privacy.mjs <文件或目录> [--json <输出路径>] [--rules <规则文件>]
// 退出码: 0 = 无发现, 2 = 有发现（需人工判断）, 1 = 出错
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';

const args = process.argv.slice(2);
const target = args.find((a) => !a.startsWith('--'));
const getOpt = (name) => {
  const i = args.indexOf(name);
  return i >= 0 ? args[i + 1] : null;
};
const jsonOut = getOpt('--json');
const TOOLS_DIR = path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, '$1'));
const RULES_DIR = path.resolve(TOOLS_DIR, '..', '_private');
// 规则文件放在 _private/（已 gitignore），不要提交到仓库里
const rulesPath = getOpt('--rules') || path.join(RULES_DIR, 'privacy-rules.json');

if (!target) {
  console.error('usage: node tools/scan-privacy.mjs <path> [--json out.json]');
  process.exit(1);
}

let RULES = { names: [], schools: [], extraTerms: [], ignorePaths: [] };
try {
  RULES = { ...RULES, ...JSON.parse(fs.readFileSync(rulesPath, 'utf8').replace(/^\uFEFF/, '')) };
} catch { /* 无规则文件时用内置规则 */ }

const IGNORE = new Set(['.git', 'node_modules', 'profile', 'state', 'failures', '__pycache__',
                        '.venv', 'venv', '_previews', '_private']);
const SKIP_EXT = new Set(['png', 'jpg', 'jpeg', 'gif', 'webp', 'ico', 'zip', 'rar', '7z',
                          'mp4', 'mp3', 'woff', 'woff2', 'ttf', 'otf', 'exe', 'dll', 'bin']);

// ---------- 规则 ----------
const PATTERNS = [
  { kind: 'secret', label: 'OpenAI/Anthropic 风格密钥', re: /\bsk-(?:ant-|proj-)?[A-Za-z0-9_-]{20,}/g, block: true },
  { kind: 'secret', label: 'GitHub token', re: /\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})/g, block: true },
  { kind: 'secret', label: 'AWS Access Key', re: /\bAKIA[0-9A-Z]{16}\b/g, block: true },
  { kind: 'secret', label: 'Google API Key', re: /\bAIza[0-9A-Za-z_-]{35}\b/g, block: true },
  { kind: 'secret', label: 'Slack token', re: /\bxox[abprs]-[A-Za-z0-9-]{10,}/g, block: true },
  { kind: 'secret', label: '私钥', re: /-----BEGIN [A-Z ]*PRIVATE KEY-----/g, block: true },
  { kind: 'secret', label: 'JWT', re: /\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\./g, block: true },
  { kind: 'secret', label: '疑似 api_key / token 赋值', re: /\b(?:api[_-]?key|apikey|secret[_-]?key|access[_-]?token|password|passwd|pwd)\b\s*[:=]\s*["']?[A-Za-z0-9_\-./+]{12,}/gi, block: true },
  { kind: 'email', label: '邮箱地址', re: /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b/g, block: false },
  { kind: 'phone', label: '手机号', re: /(?<!\d)1[3-9]\d{9}(?!\d)/g, block: false },
  { kind: 'idcard', label: '身份证样式长数字', re: /(?<!\d)\d{17}[\dXx](?!\d)/g, block: false },
  { kind: 'idcard', label: '学号标记', re: /(?:学号|student\s*id|StudentID|SID)\s*[:：=]?\s*[A-Za-z]?\d{6,14}/gi, block: false },
  { kind: 'school', label: '学校名称', re: /[\u4e00-\u9fa5]{2,12}(?:大学|学院|中学|附中|小学)|[A-Z][A-Za-z. ]{2,40}(?:University|College|Institute)/g, block: false },
  { kind: 'name', label: '姓名标记', re: /(?:姓名|作者)\s*[:：]?\s*[\u4e00-\u9fa5]{2,4}/g, block: false },
  { kind: 'name', label: '英文姓名标记', re: /\b(?:Name|Author|Prepared by|Submitted by)\s*[:：]\s*[A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,3}/g, block: false },
];

function masked(s) {
  const t = s.trim();
  if (t.length <= 8) return t.slice(0, 3) + '***';
  return t.slice(0, 4) + '***' + t.slice(-2);
}

function lineOf(text, index) {
  let line = 1;
  for (let i = 0; i < index && i < text.length; i++) if (text.charCodeAt(i) === 10) line++;
  return line;
}

// ---------- zip / office 解析 ----------
function zipEntries(buf) {
  let eocd = -1;
  for (let i = buf.length - 22; i >= Math.max(0, buf.length - 66000); i--) {
    if (i >= 0 && i + 4 <= buf.length && buf.readUInt32LE(i) === 0x06054b50) { eocd = i; break; }
  }
  if (eocd < 0) return [];
  const count = buf.readUInt16LE(eocd + 10);
  let off = buf.readUInt32LE(eocd + 16);
  const out = [];
  for (let n = 0; n < count; n++) {
    if (buf.readUInt32LE(off) !== 0x02014b50) break;
    const method = buf.readUInt16LE(off + 10);
    const compSize = buf.readUInt32LE(off + 20);
    const nameLen = buf.readUInt16LE(off + 28);
    const extraLen = buf.readUInt16LE(off + 30);
    const commentLen = buf.readUInt16LE(off + 32);
    const localOff = buf.readUInt32LE(off + 42);
    const name = buf.toString('utf8', off + 46, off + 46 + nameLen);
    out.push({ name, method, compSize, localOff });
    off += 46 + nameLen + extraLen + commentLen;
  }
  return out;
}

function zipRead(buf, entry) {
  const off = entry.localOff;
  const nameLen = buf.readUInt16LE(off + 26);
  const extraLen = buf.readUInt16LE(off + 28);
  const start = off + 30 + nameLen + extraLen;
  const data = buf.subarray(start, start + entry.compSize);
  try {
    return entry.method === 0 ? data : zlib.inflateRawSync(data);
  } catch { return Buffer.alloc(0); }
}

function officeText(file) {
  const buf = fs.readFileSync(file);
  const wanted = zipEntries(buf).filter((e) =>
    /^word\/(document|header\d*|footer\d*)\.xml$/.test(e.name) ||
    /^xl\/(sharedStrings|worksheets\/sheet\d+)\.xml$/.test(e.name) ||
    /^ppt\/(slides|notesSlides)\/.*\.xml$/.test(e.name));
  return wanted.map((e) => zipRead(buf, e).toString('utf8').replace(/<[^>]+>/g, ' ')).join('\n');
}

// Office 文档属性（作者 / 最后修改人 / 公司 / 标题）——页面看不见，文件里有
function officeMeta(file) {
  const buf = fs.readFileSync(file);
  const meta = {};
  const grab = (re, key, text) => {
    const m = re.exec(text);
    if (m && m[1] && m[1].trim()) meta[key] = m[1].trim();
  };
  for (const e of zipEntries(buf)) {
    if (!/^docProps\/(core|app)\.xml$/.test(e.name)) continue;
    const xml = zipRead(buf, e).toString('utf8');
    grab(/<dc:creator>([^<]*)<\/dc:creator>/i, 'creator', xml);
    grab(/<cp:lastModifiedBy>([^<]*)<\/cp:lastModifiedBy>/i, 'lastModifiedBy', xml);
    grab(/<dc:title>([^<]*)<\/dc:title>/i, 'title', xml);
    grab(/<dc:subject>([^<]*)<\/dc:subject>/i, 'subject', xml);
    grab(/<cp:keywords>([^<]*)<\/cp:keywords>/i, 'keywords', xml);
    grab(/<Company>([^<]*)<\/Company>/i, 'company', xml);
  }
  return meta;
}

function isBinary(buf) {
  const n = Math.min(buf.length, 4000);
  for (let i = 0; i < n; i++) if (buf[i] === 0) return true;
  return false;
}

function textOf(file) {
  const ext = path.extname(file).slice(1).toLowerCase();
  if (['docx', 'xlsx', 'pptx'].includes(ext)) {
    try { return officeText(file); } catch { return ''; }
  }
  if (SKIP_EXT.has(ext)) return '';
  try {
    const buf = fs.readFileSync(file);
    if (isBinary(buf)) return '';
    return buf.toString('utf8');
  } catch { return ''; }
}

// ---------- 扫描 ----------
const findings = [];
function add(f, kind, label, sev, line, snippet) {
  findings.push({ file: f, kind, label, severity: sev, line, snippet: masked(snippet), full: snippet });
}

function scanText(file, text) {
  if (!text) return;
  // 页面里内嵌的图片/字体是 base64，扫它只会制造误报（数字串、字母串）
  text = text.replace(/data:[^"')\s]{40,}/g, ' ').replace(/[A-Za-z0-9+/]{200,}={0,2}/g, ' ');
  for (const p of PATTERNS) {
    p.re.lastIndex = 0;
    let m;
    let guard = 0;
    while ((m = p.re.exec(text)) !== null && guard++ < 100) {
      add(file, p.kind, p.label, p.block ? 'block' : 'warn', lineOf(text, m.index), m[0]);
      if (m.index === p.re.lastIndex) p.re.lastIndex++;
    }
  }
  for (const term of [...(RULES.names || []), ...(RULES.schools || []), ...(RULES.extraTerms || [])]) {
    if (!term || String(term).length < 2) continue;
    const lower = text.toLowerCase();
    const t = String(term).toLowerCase();
    let idx = lower.indexOf(t);
    let guard = 0;
    while (idx >= 0 && guard++ < 50) {
      add(file, 'term', `自定义敏感词「${term}」`, 'warn', lineOf(text, idx), text.slice(idx, idx + String(term).length));
      idx = lower.indexOf(t, idx + 1);
    }
  }
}

// 文档属性 / PDF 元数据
function scanMeta(p) {
  const ext = path.extname(p).slice(1).toLowerCase();
  if (['docx', 'xlsx', 'pptx'].includes(ext)) {
    let meta = {};
    try { meta = officeMeta(p); } catch { return; }
    for (const [k, v] of Object.entries(meta)) {
      if (!v) continue;
      if (/^(Microsoft Office User|Administrator|User|Windows User|Microsoft Office)$/i.test(v)) continue;
      const label = { creator: '文档属性-作者', lastModifiedBy: '文档属性-最后修改人',
                      title: '文档属性-标题', subject: '文档属性-主题',
                      keywords: '文档属性-关键词', company: '文档属性-公司' }[k] || ('文档属性-' + k);
      add(p, 'meta', label, 'warn', 0, `${k}: ${v}`);
    }
  } else if (ext === 'pdf') {
    try {
      const buf = fs.readFileSync(p).subarray(0, 400000).toString('latin1');
      const hits = [
        [/\/Author\s*\(([^)]{1,80})\)/, 'PDF-作者'],
        [/\/Title\s*\(([^)]{1,80})\)/, 'PDF-标题'],
        [/<dc:creator>[\s\S]{0,600}?<rdf:li>([^<]{1,120})<\/rdf:li>/, 'PDF-XMP 作者'],
        [/<dc:title>[\s\S]{0,600}?<rdf:li>([^<]{1,120})<\/rdf:li>/, 'PDF-XMP 标题'],
      ];
      for (const [re, label] of hits) {
        const m = re.exec(buf);
        if (m && m[1].trim() && /[^\s0]/.test(m[1])) add(p, 'meta', label, 'warn', 0, m[1].trim());
      }
    } catch { }
  }
}

// 文件名/目录名本身也要查
function scanName(p) {
  const base = path.basename(p);
  for (const p2 of PATTERNS) {
    if (!['school', 'name', 'phone', 'idcard', 'email'].includes(p2.kind)) continue;
    p2.re.lastIndex = 0;
    const m = p2.re.exec(base);
    if (m) add(p, p2.kind, `文件名含${p2.label}`, 'warn', 0, m[0]);
  }
  for (const term of [...(RULES.names || []), ...(RULES.schools || [])]) {
    if (term && base.toLowerCase().includes(String(term).toLowerCase())) {
      add(p, 'term', `文件名含敏感词「${term}」`, 'warn', 0, term);
    }
  }
}

const ARCHIVE = new Set(['zip', 'rar', '7z', 'tar', 'gz', 'bz2', 'xz']);

function scanOne(p) {
  scanText(p, textOf(p));
  scanMeta(p);
  scanName(p);
  const ext = path.extname(p).slice(1).toLowerCase();
  if (ARCHIVE.has(ext)) {
    const mb = (fs.statSync(p).size / 1048576).toFixed(1);
    add(p, 'archive', `压缩包 ${mb} MB，内部内容无法扫描`, 'warn', 0, path.basename(p));
  }
}

function walk(p) {
  let st;
  try { st = fs.statSync(p); } catch { return; }
  if (st.isFile()) { scanOne(p); return; }
  for (const e of fs.readdirSync(p, { withFileTypes: true })) {
    if (IGNORE.has(e.name)) continue;
    const full = path.join(p, e.name);
    if (e.isDirectory()) walk(full);
    else if (e.isFile()) scanOne(full);
  }
}

function countFiles(p) {
  let st;
  try { st = fs.statSync(p); } catch { return 0; }
  if (st.isFile()) return 1;
  let n = 0;
  for (const e of fs.readdirSync(p, { withFileTypes: true })) {
    if (IGNORE.has(e.name)) continue;
    const full = path.join(p, e.name);
    if (e.isDirectory()) n += countFiles(full);
    else if (e.isFile()) n++;
  }
  return n;
}

const ABS = path.resolve(target);
walk(ABS);

// ---------- 汇总 ----------
const blocks = findings.filter((f) => f.severity === 'block');
const warns = findings.filter((f) => f.severity === 'warn');

const rel = (p) => {
  const r = path.relative(ABS, p);
  return r || path.basename(p);
};

console.log(`\n隐私扫描: ${target}`);
console.log(`  文件数: ${countFiles(ABS)}   发现: ${blocks.length} 项高危 / ${warns.length} 项提示\n`);

if (!findings.length) {
  console.log('  ✓ 未发现敏感信息');
} else {
  const seen = new Set();
  for (const f of findings) {
    const key = f.file + '|' + f.kind + '|' + (f.full || '');
    if (seen.has(key)) continue;
    seen.add(key);
    const tag = f.severity === 'block' ? '阻断' : '提示';
    // 只有密钥类打码；姓名/学校/属性要让用户看清原文才能判断
    const shown = f.kind === 'secret' ? f.snippet : (f.full || f.snippet);
    console.log(`  [${tag}] ${f.label}  ${rel(f.file)}${f.line ? ':' + f.line : ''}  →  ${shown}`);
  }
}

if (jsonOut) {
  fs.writeFileSync(jsonOut, JSON.stringify({
    target, blocks: blocks.length, warns: warns.length, findings,
  }, null, 2), 'utf8');
}

if (blocks.length || warns.length) {
  console.log('\n  → 需要人工确认后再上传（-Force 可强行发布）。');
  process.exit(2);
}
process.exit(0);
