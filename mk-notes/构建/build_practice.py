# -*- coding: utf-8 -*-
"""
AF5638 期末练习 · 逐题精做页生成器

用法：
    python build_practice.py
读：
    practice_content.py   题目与答案（唯一需要改的文件）
    practice_svgs.py      矢量示意图
写：
    期末练习.html          单文件离线

与另外两个引擎的区别：
    build_notes.py     纵向：一页课件一个块
    build_review.py    横向：跨讲重组
    build_practice.py  按题：一题一小问一卡，答案默认折叠（先写再看）
"""
import os, re, html, importlib.util
import ui_shell as U
import paths as P

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = P.page(P.PAGE_PRACTICE)
CURFILE = "期末练习.html"

XREF_RE = re.compile(r"\[\[([A-Za-z0-9_#]+)\|([^\]]+)\]\]")


def xref(s):
    """[[T6#p11|文字]] 跨文件；[[q2a|文字]] 本页锚点。"""
    if "[[" not in s:
        return s

    def rep(m):
        tgt, txt = m.group(1), m.group(2)
        if re.fullmatch(r"T\d+(?:#.+)?", tgt):
            n = re.match(r"T(\d+)", tgt).group(1)
            frag = tgt.split("#", 1)[1] if "#" in tgt else ""
            fn = f"Topic {n} 笔记.html"
            if P.has_page(fn):
                return f'<a class="xref" href="{fn}{"#" + frag if frag else ""}">{txt}</a>'
            return f'<span class="xref-off">{txt}</span>'
        return f'<a class="xref in" href="#{tgt}">{txt}</a>'

    return XREF_RE.sub(rep, s)


def mj(s):
    if not isinstance(s, str):
        return s
    if "<span class='mj'>" in s:
        s = s.replace("<span class='mj'>", "\\(").replace("</span>", "\\)")
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s, flags=re.S)
    return xref(s)


def load(name, alias):
    p = os.path.join(HERE, name + ".py")
    spec = importlib.util.spec_from_file_location(alias, p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


M = load("practice_content", "practice_content")
S = load("practice_svgs", "practice_svgs")

COURSE   = getattr(M, "COURSE", "AF5638 宏观经济学")
TITLE    = getattr(M, "TITLE", "期末练习精做")
SUBTITLE = getattr(M, "SUBTITLE", "")
META     = getattr(M, "META", [])
INTRO    = getattr(M, "INTRO", [])
SECTIONS = getattr(M, "SECTIONS", [])
SOURCE   = getattr(M, "SOURCE", "")


# ---------------- 通用块 ----------------
def render_block(b):
    k = b[0]
    if k == "p":
        return f'<p class="rp">{mj(b[1])}</p>'
    if k == "big":
        return f'<div class="rbig">{mj(b[1])}</div>'
    if k == "ul":
        return '<ul class="rul">' + "".join(f"<li>{mj(x)}</li>" for x in b[1]) + "</ul>"
    if k == "ol":
        return '<ol class="rol">' + "".join(f"<li>{mj(x)}</li>" for x in b[1]) + "</ol>"
    if k == "warn":
        return f'<div class="warn"><b>⚠ {mj(b[1])}：</b>{mj(b[2])}</div>'
    if k == "tip":
        return f'<div class="tip"><b>💡 {mj(b[1])}：</b>{mj(b[2])}</div>'
    if k == "note":
        return f'<div class="explain"><b>{mj(b[1])}：</b>{mj(b[2])}</div>'
    if k == "table":
        return render_table(b[1])
    if k == "eq":
        rows = []
        for it in b[1]:
            name, tex, note = it[0], it[1], it[2]
            ref = it[3] if len(it) > 3 else ""
            rh = f'<div class="eqref">{mj(ref)}</div>' if ref else ""
            rows.append(f'<div class="eqrow"><div class="eqn">{mj(name)}</div>'
                        f'<div class="eqm">\\[{mj(tex)}\\]</div>'
                        f'<div class="eqd">{mj(note)}{rh}</div></div>')
        cap = b[2] if len(b) > 2 else ""
        ch = f'<div class="eqcap">{mj(cap)}</div>' if cap else ""
        return f'<div class="eqbox">{ch}{"".join(rows)}</div>'
    if k == "steps":
        rows = []
        for i, (t, body) in enumerate(b[1], 1):
            rows.append(f'<div class="stp"><span class="stn">{i}</span>'
                        f'<div><div class="stt">{mj(t)}</div>'
                        f'<div class="stb">{mj(body)}</div></div></div>')
        return f'<div class="steps">{"".join(rows)}</div>'
    if k == "svg":
        return S.get(b[1])
    if k == "raw":
        return b[1]
    raise ValueError("未知块类型 " + k)


def render_table(d):
    cls = d.get("cls", "table")
    cap = f'<div class="tcap">{mj(d["caption"])}</div>' if d.get("caption") else ""
    head = ""
    if d.get("header"):
        head = "<tr>" + "".join(f"<th>{mj(h)}</th>" for h in d["header"]) + "</tr>"
    body = []
    for r in d["rows"]:
        if isinstance(r, str):
            body.append(f'<tr class="grp"><td colspan="{len(d.get("header") or [1])}">{mj(r)}</td></tr>')
        else:
            cells = []
            for i, c in enumerate(r):
                k = ' class="rowhead"' if i == 0 and d.get("first_bold") else ""
                cells.append(f"<td{k}>{mj(c)}</td>")
            body.append("<tr>" + "".join(cells) + "</tr>")
    note = f'<div class="tnote">{mj(d["note"])}</div>' if d.get("note") else ""
    return (f'<div class="tbox">{cap}<div class="tw"><table class="{cls}">'
            f'{head}{"".join(body)}</table></div>{note}</div>')


# ---------------- 一道小问 ----------------
def render_item(sid, it, n):
    qid = f'{sid}{it["tag"]}'
    out = [f'<div class="qcard" id="{qid}" data-k="{qid}">']
    out.append('<div class="qh">'
               f'<span class="qn">({it["tag"]})</span>'
               f'<span class="qidx">第 {n} 问</span>'
               f'<label class="done"><input type="checkbox" class="donebox" data-k="{qid}">'
               '<span>已完成</span></label></div>')
    out.append(f'<div class="qtext">{mj(it["q"])}</div>')
    if it.get("qcn"):
        out.append(f'<div class="qcn">{mj(it["qcn"])}</div>')
    if it.get("ask"):
        out.append(f'<div class="ask"><b>这题在考</b>{mj(it["ask"])}</div>')
    if it.get("steps"):
        rows = []
        for i, (t, b) in enumerate(it["steps"], 1):
            rows.append(f'<div class="stp"><span class="stn">{i}</span><div>'
                        f'<div class="stt">{mj(t)}</div><div class="stb">{mj(b)}</div></div></div>')
        out.append(f'<div class="steps">{ "".join(rows) }</div>')
    if it.get("fig"):
        _fs = it["fig"]
        if isinstance(_fs, str):
            _fs = [_fs]
        for _n in _fs:
            out.append(S.get(_n))
    if it.get("en") or it.get("cn") or it.get("points"):
        out.append('<details class="ans"><summary>参考答案 · 先自己写，再点开</summary>')
        if it.get("en"):
            out.append(f'<div class="enblk"><div class="enh">Answer（可直接抄的英文）</div>'
                       f'<div class="entx">{mj(it["en"])}</div></div>')
        if it.get("cn"):
            out.append(f'<div class="cnblk"><div class="enh">中文对照</div>'
                       f'<div class="cntx">{mj(it["cn"])}</div></div>')
        if it.get("points"):
            li = "".join(f"<li>{mj(x)}</li>" for x in it["points"])
            out.append(f'<div class="pts"><b>判分点</b><ul>{li}</ul></div>')
        out.append('</details>')
    if it.get("trap"):
        out.append(f'<div class="warn"><b>⚠ 常见失分：</b>{mj(it["trap"])}</div>')
    if it.get("refs"):
        rs = "　".join(mj(f"[[{a}|{b}]]") for a, b in it["refs"])
        out.append(f'<div class="refs"><b>回看：</b>{rs}</div>')
    out.append("</div>")
    return "".join(out)


def toc_html():
    items = []
    for s in SECTIONS:
        sub = "".join(
            f'<a class="tq" href="#{s["id"]}{it["tag"]}">{it["tag"]}</a>'
            for it in s.get("items", []))
        items.append(f'<div class="tg"><a href="#{s["id"]}">{s["num"]}、{s["title"]}</a>'
                     f'<div class="tqs">{sub}</div></div>')
    return '<b>题目目录</b>' + "".join(items)


CSS = """
:root{
 --bg:#f8fafc; --card:#fff; --card2:#f1f5f9; --card3:#e8eef7;
 --ink:#0f172a; --ink2:#334155; --muted:#64748b; --line:#dbe3ee;
 --accent:#2563eb; --accent-soft:#eff6ff; --accent-ink:#1d4ed8; --accent2:#6d28d9;
 --green:#047857; --green-soft:#ecfdf5; --green-ink:#047857;
 --orange:#b45309; --orange-soft:#fffbeb; --orange-ink:#92400e;
 --red:#b91c1c; --red-soft:#fef2f2; --purple:#6d28d9; --purple-soft:#f5f3ff;
 --th-bg:#eef2f9; --th-ink:#1e40af; --en-bg:#f0f7ff; --cn-bg:#fbfaf5;
}
[data-theme="dark"]{
 --bg:#0f172a; --card:#1b2437; --card2:#243146; --card3:#2d3b53;
 --ink:#f8fafc; --ink2:#d4dded; --muted:#94a3b8; --line:#3b4a63;
 --accent:#7db4ff; --accent-soft:#152f52; --accent-ink:#8cc0ff; --accent2:#b9a2ff;
 --green:#4ade80; --green-soft:#08301f; --green-ink:#4ade80;
 --orange:#fbbf24; --orange-soft:#3a2708; --orange-ink:#fcd34d;
 --red:#fb8a8a; --red-soft:#3d1414; --purple:#b9a2ff; --purple-soft:#251a45;
 --th-bg:#22304a; --th-ink:#9ec9ff; --en-bg:#12263f; --cn-bg:#241f14;
}
*{box-sizing:border-box;}
body{margin:0;background:var(--bg);color:var(--ink);font-family:"Segoe UI","Microsoft YaHei",-apple-system,sans-serif;line-height:1.85;font-size:16px;}
.wrap{max-width:1000px;margin:0 auto;padding:32px 24px 104px;}
header.hero{background:linear-gradient(135deg,#1e3a8a,#2563eb);color:#fff;border-radius:16px;padding:30px 36px;margin-bottom:18px;}
.home{display:inline-block;background:rgba(255,255,255,.2);color:#fff;border-radius:999px;
 padding:2px 12px;font-size:12.5px;font-weight:700;text-decoration:none;margin-bottom:10px;}
.home:hover{background:rgba(255,255,255,.34);text-decoration:none;color:#fff;}
header.hero h1{margin:0 0 8px;font-size:25px;line-height:1.4;}
header.hero p{margin:8px 0 0;opacity:.93;font-size:15px;}
.hero .meta{display:flex;flex-wrap:wrap;gap:9px;margin-top:15px;}
.hero .meta span{background:rgba(255,255,255,.16);border-radius:999px;padding:3px 13px;font-size:12.5px;}
.sec-title{font-size:21px;margin:42px 0 6px;padding-left:12px;border-left:6px solid var(--accent);}
.sec-sub{color:var(--muted);font-size:14px;margin:0 0 14px;padding-left:18px;}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:20px 24px;margin:14px 0;box-shadow:0 1px 3px rgba(15,23,42,.05);}
.rp{margin:10px 0;font-size:15.2px;}
.rbig{background:var(--accent-soft);border-left:5px solid var(--accent);border-radius:0 10px 10px 0;padding:13px 17px;margin:14px 0;font-size:15.3px;}
.rbig b{color:var(--accent-ink);}
.rul,.rol{margin:8px 0;padding-left:22px;font-size:15px;}
.rul li,.rol li{margin:6px 0;}
.explain{background:var(--card2);border-radius:10px;padding:10px 15px;margin:10px 0;font-size:14.6px;}
.tip{background:var(--orange-soft);border-radius:10px;padding:10px 15px;margin-top:11px;font-size:14px;}
.tip b{color:var(--orange);}
.warn{background:var(--red-soft);border-radius:10px;padding:10px 15px;margin-top:11px;font-size:14px;}
.warn b{color:var(--red);}
/* 表格 */
.tw{overflow-x:auto;}
.tw table{min-width:600px;}
.table{width:100%;border-collapse:collapse;margin:6px 0;font-size:13.8px;}
.table th{background:var(--th-bg);color:var(--th-ink);padding:8px 10px;text-align:left;border:1px solid var(--line);font-size:13.4px;}
.table td{padding:8px 10px;border:1px solid var(--line);vertical-align:top;}
.table td.rowhead{font-weight:700;color:var(--accent-ink);background:var(--card2);}
.table tr.grp td{background:var(--th-bg);color:var(--th-ink);font-weight:800;font-size:13.2px;}
.tbox{margin:14px 0;}
.tcap{font-weight:800;font-size:15px;color:var(--accent-ink);margin-bottom:6px;}
.tnote{color:var(--muted);font-size:13px;margin-top:6px;line-height:1.75;}
/* 步骤 */
.steps{margin:12px 0;}
.stp{display:grid;grid-template-columns:32px 1fr;gap:11px;align-items:start;padding:9px 0;border-top:1px dashed var(--line);}
.stp:first-child{border-top:none;}
.stn{width:25px;height:25px;line-height:25px;text-align:center;border-radius:50%;background:var(--accent);color:#fff;font-weight:800;font-size:12.5px;}
.stt{font-weight:800;font-size:14.4px;color:var(--accent-ink);}
.stb{font-size:14.2px;color:var(--ink2);line-height:1.8;}
/* 公式 */
.eqbox{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 16px;margin:13px 0;}
.eqcap{font-weight:800;font-size:14.4px;color:var(--accent-ink);margin-bottom:6px;}
.eqrow{display:grid;grid-template-columns:170px minmax(0,1fr);gap:12px;padding:9px 0;border-top:1px dashed var(--line);align-items:start;}
.eqrow:first-of-type{border-top:none;}
.eqn{font-weight:700;font-size:13.6px;line-height:1.7;}
.eqm{overflow-x:auto;font-size:15px;}
.eqd{grid-column:2;font-size:13.2px;color:var(--muted);line-height:1.75;margin-top:-4px;}
.eqref{color:var(--accent-ink);font-size:12.4px;}
@media(max-width:720px){.eqrow{grid-template-columns:1fr;}.eqd{grid-column:1;}}
/* 题目卡 */
.qcard{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px 22px 16px;margin:14px 0;box-shadow:0 1px 3px rgba(15,23,42,.05);position:relative;}
.qcard.is-done{border-left:5px solid var(--green);}
.qh{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:6px;}
.qn{font-weight:900;font-size:16px;color:#fff;background:var(--accent);border-radius:8px;padding:0 9px;line-height:26px;}
.qidx{font-size:12.5px;color:var(--muted);}
.done{margin-left:auto;font-size:12.8px;color:var(--muted);display:flex;align-items:center;gap:5px;cursor:pointer;user-select:none;}
.done input{width:15px;height:15px;accent-color:var(--green);cursor:pointer;}
.qtext{font-size:15.2px;color:var(--ink);background:var(--card2);border-radius:9px;padding:11px 14px;margin:6px 0 4px;}
.qcn{font-size:14.2px;color:var(--muted);padding:0 2px 4px;line-height:1.8;}
.ask{background:var(--purple-soft);border-left:4px solid var(--purple);border-radius:0 8px 8px 0;padding:9px 14px;margin:10px 0;font-size:14.4px;}
.ask b{color:var(--purple);margin-right:6px;}
details.ans{margin:12px 0 4px;border:1px solid var(--line);border-radius:11px;background:var(--card);overflow:hidden;}
details.ans>summary{cursor:pointer;padding:9px 15px;font-size:14px;font-weight:700;color:var(--accent-ink);background:var(--accent-soft);list-style:none;}
details.ans>summary::-webkit-details-marker{display:none;}
details.ans>summary::before{content:"▸ ";font-weight:900;}
details.ans[open]>summary::before{content:"▾ ";}
.enblk{margin:12px 14px;border-radius:10px;background:var(--en-bg);padding:10px 14px;}
.cnblk{margin:10px 14px;border-radius:10px;background:var(--cn-bg);padding:10px 14px;}
.enh{font-size:11.8px;font-weight:800;letter-spacing:.6px;color:var(--muted);text-transform:uppercase;margin-bottom:4px;}
.entx{font-family:"Georgia","Times New Roman",serif;font-size:14.6px;line-height:1.9;color:var(--ink);}
.cntx{font-size:14.2px;line-height:1.9;color:var(--ink2);}
.pts{margin:6px 14px 14px;font-size:13.6px;}
.pts b{color:var(--green-ink);}
.pts ul{margin:5px 0 0;padding-left:20px;}
.pts li{margin:3px 0;}
.refs{margin-top:10px;font-size:13px;color:var(--muted);}
a.xref{color:var(--accent-ink);text-decoration:none;border-bottom:1.5px solid var(--accent-soft);padding-bottom:1px;white-space:nowrap;}
a.xref:hover{border-bottom-color:var(--accent);background:var(--accent-soft);border-radius:3px;}
a.xref::after{content:"↗";font-size:.8em;vertical-align:super;margin-left:2px;opacity:.75;}
a.xref.in::after{content:"";}
/* 表格里整列都是链接时，↗ 会挤成一个小符号（看起来像「p15⁄」），去掉更干净 */
.table td a.xref::after{content:"";}
.table td a.xref{border-bottom-width:1px;}
.xref-off{color:var(--muted);border-bottom:1px dashed var(--muted);}
/* 进度条 */
.pbar{display:flex;align-items:center;gap:12px;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:10px 16px;margin:0 0 6px;font-size:13.8px;flex-wrap:wrap;}
.pbar .track2{flex:1;min-width:160px;height:8px;background:var(--card2);border-radius:999px;overflow:hidden;}
.pbar .fill{height:100%;width:0;background:linear-gradient(90deg,#2563eb,#047857);transition:width .25s;}
.pbar b{color:var(--accent-ink);}
.pbar button{border:1px solid var(--line);background:var(--card2);color:var(--ink2);border-radius:8px;padding:3px 11px;font-size:12.8px;cursor:pointer;font-family:inherit;}
.pbar button:hover{border-color:var(--accent);color:var(--accent-ink);}
/* 图 */
.figwrap{margin:12px 0;background:var(--card2);border-radius:12px;padding:10px 8px 6px;}
.figsvg{width:100%;height:auto;display:block;}
.figcap{font-size:12.6px;color:var(--muted);text-align:center;margin-top:4px;line-height:1.7;padding:0 10px;}
.figsvg .ax{stroke:var(--muted);stroke-width:1.3;}
.figsvg .axl{fill:var(--muted);font-size:13px;font-style:italic;}
.figsvg .b{stroke:var(--accent);stroke-width:2.2;fill:none;}
.figsvg .r{stroke:var(--red);stroke-width:2.2;fill:none;}
.figsvg .g{stroke:var(--green);stroke-width:1.8;fill:none;}
.figsvg .gd{stroke:var(--muted);stroke-width:1;opacity:.75;fill:none;}
.figsvg .dot{fill:var(--accent);}
.figsvg .dot2{fill:var(--red);}
.figsvg .lab{fill:var(--ink2);font-size:12.2px;}
.figsvg .cl{fill:var(--accent-ink);font-size:12.6px;font-weight:700;}
.figsvg .rl{fill:var(--red);font-size:12.6px;font-weight:700;}
.figsvg .gl{fill:var(--green);font-size:12.6px;font-weight:700;}
.figsvg .ttl{fill:var(--ink2);font-size:12.4px;font-weight:800;}
.figsvg .arw{stroke:var(--muted);stroke-width:1.6;}
.figsvg .ahd{fill:var(--muted);}
/* 目录 / 主题 */
.theme-toggle{position:fixed;top:16px;right:20px;z-index:999;display:flex;gap:4px;background:var(--card)!important;border:1px solid var(--line)!important;border-radius:999px;padding:4px;box-shadow:0 2px 8px rgba(15,23,42,.15);}
.theme-toggle button{border:none;background:transparent!important;color:var(--ink2)!important;font-size:13px;font-weight:600;padding:5px 13px;border-radius:999px;cursor:pointer;font-family:inherit;}
.theme-toggle button.active{background:var(--accent)!important;color:#fff!important;}
#toc{position:fixed;top:70px;right:20px;z-index:998;width:220px;max-height:80vh;overflow:auto;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:10px 13px;font-size:12.8px;display:none;box-shadow:0 2px 8px rgba(15,23,42,.1);}
#toc b{display:block;margin-bottom:6px;color:var(--accent);}
#toc .tg{margin-bottom:8px;}
#toc .tg>a{color:var(--ink2);text-decoration:none;font-weight:700;display:block;border-bottom:1px dashed var(--line);padding:2px 0;}
#toc .tg>a:hover{color:var(--accent);}
#toc .tqs{display:flex;gap:4px;flex-wrap:wrap;margin-top:4px;padding-left:2px;}
#toc .tq{font-size:11.5px;color:var(--accent-ink);background:var(--accent-soft);border-radius:5px;padding:0 6px;text-decoration:none;}
@media(min-width:1480px){#toc{display:block;}}
@media print{#toc,.theme-toggle,.pbar{display:none!important;}details.ans{page-break-inside:avoid;}}
footer{margin-top:48px;color:var(--muted);font-size:13px;text-align:center;}
"""

JS = """
function setTheme(t){document.documentElement.setAttribute('data-theme',t);document.getElementById('btn-light').classList.toggle('active',t==='light');document.getElementById('btn-dark').classList.toggle('active',t==='dark');try{localStorage.setItem('af5638_theme',t);}catch(e){}}
(function(){var t=null;try{t=localStorage.getItem('af5638_theme');}catch(e){}
 setTheme(t||document.documentElement.getAttribute('data-theme')||'light');})();
(function(){
 var KEY='af5638_final_progress_v1';
 var saved={};
 try{saved=JSON.parse(localStorage.getItem(KEY)||'{}');}catch(e){saved={};}
 var boxes=[].slice.call(document.querySelectorAll('.donebox'));
 function save(){var o={};boxes.forEach(function(b){if(b.checked)o[b.dataset.k]=1;});
   try{localStorage.setItem(KEY,JSON.stringify(o));}catch(e){}}
 function refresh(){
   var n=0;boxes.forEach(function(b){if(b.checked)n++;
     var c=b.closest('.qcard'); if(c){c.classList.toggle('is-done',b.checked);}});
   document.getElementById('pcount').textContent=n;
   document.getElementById('ptotal').textContent=boxes.length;
   document.getElementById('pfill').style.width=(boxes.length?100*n/boxes.length:0)+'%';
 }
 boxes.forEach(function(b){
   if(saved[b.dataset.k])b.checked=true;
   b.addEventListener('change',function(){save();refresh();});
 });
 refresh();
 document.getElementById('bopen').addEventListener('click',function(){
   [].forEach.call(document.querySelectorAll('details.ans'),function(d){d.open=true;});
   if(window.MathJax&&MathJax.typesetPromise){MathJax.typesetPromise().catch(function(){});}});
 document.getElementById('bclose').addEventListener('click',function(){
   [].forEach.call(document.querySelectorAll('details.ans'),function(d){d.open=false;});});
 document.getElementById('breset').addEventListener('click',function(){
   if(!confirm('清空所有「已完成」标记？'))return;
   boxes.forEach(function(b){b.checked=false;});save();refresh();});
})();
(function(){var jump=function(){if(location.hash){var el=document.querySelector(location.hash);
  if(el){el.scrollIntoView();}}};
 window.addEventListener('load',function(){setTimeout(jump,120);});
 if(window.MathJax&&MathJax.startup&&MathJax.startup.promise){
   MathJax.startup.promise.then(function(){setTimeout(jump,60);});}})();
"""


def build_body():
    out = []
    for s in SECTIONS:
        out.append(f'<div class="sec-title" id="{s["id"]}">{s["num"]}、{mj(s["title"])}</div>')
        if s.get("sub"):
            out.append(f'<div class="sec-sub">{mj(s["sub"])}</div>')
        if s.get("blocks"):
            out.append('<div class="card">' + "".join(render_block(b) for b in s["blocks"]) + '</div>')
        n = s.get("start", 1)
        for it in s.get("items", []):
            out.append(render_item(s["id"], it, n))
            n += 1
    return "".join(out)


CSS += U.CSS
UI_HTML = U.html(CURFILE, U.order(HERE), toc=True)
UI_JS = U.JS()
NEXTNAV = U.bottom(CURFILE, U.order(HERE))

doc = """<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>@@COURSE@@ · @@TITLE@@</title>
<style>@@CSS@@</style>
<script>window.MathJax={tex:{inlineMath:[['\\\\(','\\\\)']],displayMath:[['\\\\[','\\\\]']]},svg:{fontCache:'global'}};</script>
<script src="./_mathjax_tex_svg.js"></script>
</head>
<body>
@@UI@@
<div class="theme-toggle">
 <button id="btn-light" onclick="setTheme('light')">☀ 浅色</button>
 <button id="btn-dark" onclick="setTheme('dark')">🌙 深色</button>
</div>
<div id="toc">@@TOC@@</div>
<div class="wrap">
 <header class="hero">
  <a class="home" href="../index.html">← 复习总台</a>
  <h1>@@COURSE@@ · @@TITLE@@</h1>
  <p>@@SUBTITLE@@</p>
  <div class="hero meta">@@META@@</div>
 </header>
 <div class="pbar">
  <span>进度 <b id="pcount">0</b> / <span id="ptotal">0</span> 问</span>
  <div class="track2"><div class="fill" id="pfill"></div></div>
  <button id="bopen">展开全部答案</button>
  <button id="bclose">折叠全部答案</button>
  <button id="breset">清空进度</button>
 </div>
@@INTRO@@
@@BODY@@
@@NEXTNAV@@
 <footer>@@SOURCE@@</footer>
</div>
<script>@@JS@@
@@UIJS@@</script>
</body></html>"""

doc = (doc
       .replace("@@COURSE@@", html.escape(COURSE))
       .replace("@@TITLE@@", html.escape(TITLE))
       .replace("@@SUBTITLE@@", html.escape(SUBTITLE))
       .replace("@@META@@", "".join(f"<span>{html.escape(m)}</span>" for m in META))
       .replace("@@TOC@@", toc_html())
       .replace("@@INTRO@@", "".join(render_block(b) for b in INTRO))
       .replace("@@UI@@", UI_HTML)
       .replace("@@UIJS@@", UI_JS)
       .replace("@@NEXTNAV@@", NEXTNAV)
       .replace("@@BODY@@", build_body())
       .replace("@@SOURCE@@", html.escape(SOURCE))
       .replace("@@CSS@@", CSS)
       .replace("@@JS@@", JS))

with open(OUT, "w", encoding="utf-8") as f:
    f.write(doc)

# ---------- 自检 ----------
n_items = sum(len(s.get("items", [])) for s in SECTIONS)
print("wrote", OUT, "size KB:", round(len(doc.encode("utf-8")) / 1024, 1))
print("sections:", len(SECTIONS), "| questions:", n_items)

_ids = set(re.findall(r'id="([^"]+)"', doc))
_dead = sorted({h for h in re.findall(r'href="#([^"]+)"', doc) if h not in _ids})
if _dead:
    print("!! 站内跳转找不到目标：", _dead)
_left = len([m for m in re.finditer(r"\[\[", doc)
             if "inlineMath" not in doc[max(0, m.start() - 60):m.start() + 10]])
if _left:
    print("!! 还有未解析的跳转标记：", _left)
_tag = doc.count("<span class='mj'>")
if _tag:
    print("!! 还有未转换的公式标记：", _tag)
_ast = doc.count("**")
if _ast:
    print("!! 还有未转换的 ** 强调：", _ast)
_bad = re.findall(r"@@[A-Z]+@@", doc)
if _bad:
    print("!! 模板占位没替换：", set(_bad))
_body = doc[doc.index("<body"):]
_body = re.sub(r"\\\(.*?\\\)", "", _body, flags=re.S)
_body = re.sub(r"\\\[.*?\\\]", "", _body, flags=re.S)
_leak = [t.strip() for t in re.findall(r">([^<>]{2,})<", _body)
         if ("\\" in t) or re.search(r"[A-Za-z]\^|[A-Za-z]_\{", t)]
if _leak:
    print("!! 公式之外有裸露的 LaTeX：", len(_leak), "处，例：", _leak[0][:60])

# ⑤ JS 语法检查：一个多余的括号会让整段脚本静默失效（进度条永远 0/0），
#    页面看起来「能打开」，只有交互全死 —— 必须让构建期就报出来。
import subprocess, tempfile, os
_jsf = os.path.join(tempfile.gettempdir(), "_af5638_check.js")
with open(_jsf, "w", encoding="utf-8") as f:
    f.write(JS)
try:
    _r = subprocess.run(["node", "--check", _jsf], capture_output=True, text=True)
    if _r.returncode != 0:
        print("!! JS 语法错误（交互会全部失效）：")
        print((_r.stderr or "").strip()[:600])
except FileNotFoundError:
    print("~~ 未装 node，跳过 JS 语法检查")
_nb = doc.count('<input type="checkbox" class="donebox"')
_ng = doc.count('id="ptotal"')
print("donebox:", _nb, "| ptotal 元素:", _ng)
if _ng != 1:
    print("!! 进度条元素数量异常：", _ng)
