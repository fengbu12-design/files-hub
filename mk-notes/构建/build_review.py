# -*- coding: utf-8 -*-
"""
AF5638 期末总复习 · 生成器

与 build_notes.py 的区别：
  - 不做「逐页课件 + 逐页讲解」，而是「跨讲重组」：模型对照 / 公式总表 / 图形总表 /
    主线串联 / 辨析 / 答题模板 / 易错总清单。
  - 内容全部来自十讲 content_topicN.py 里已经核对过的公式与结论，不新造事实。

用法：
    python build_review.py
输出：
    期末总复习.html（单文件离线，公式由 _mathjax_tex_svg.js 渲染）
"""
import os, re, sys, html, importlib.util
import ui_shell as U
import paths as P

HERE = os.path.dirname(os.path.abspath(__file__))
CURFILE = "期末总复习.html"
OUT = P.page(P.PAGE_REVIEW)

XREF_RE = re.compile(r"\[\[([A-Za-z0-9_#]+)\|([^\]]+)\]\]")


def xref(s):
    """[[T7#p9|文字]] 跨讲跳转；[[s3|文字]] 站内跳转。"""
    if "[[" not in s:
        return s

    def rep(m):
        tgt, txt = m.group(1), m.group(2)
        if re.fullmatch(r"s\d+", tgt) or tgt in ("top",):
            return f'<a class="xref in" href="#{tgt}">{txt}</a>'
        m2 = re.fullmatch(r"T(\d+)(?:#(.+))?", tgt)
        if m2:
            n, frag = m2.group(1), m2.group(2)
            fn = f"Topic {n} 笔记.html"
            if P.has_page(fn):
                return f'<a class="xref" href="{fn}{"#" + frag if frag else ""}">{txt}</a>'
            return f'<span class="xref-off" title="这一讲的笔记还没做">{txt}</span>'
        return txt

    return XREF_RE.sub(rep, s)


def mj(s):
    if not isinstance(s, str):
        return s
    if "<span class='mj'>" in s:
        s = s.replace("<span class='mj'>", "\\(").replace("</span>", "\\)")
    s = xref(s)
    # 支持 **强调** 写法（避免内容文件里到处敲 <b>）
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s, flags=re.S)
    return s


def load_content():
    path = os.path.join(HERE, "review_content.py")
    spec = importlib.util.spec_from_file_location("review_content", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


M = load_content()

COURSE   = getattr(M, "COURSE", "AF5638 宏观经济学")
TITLE    = getattr(M, "TITLE", "期末总复习")
SUBTITLE = getattr(M, "SUBTITLE", "")
META     = getattr(M, "META", [])
OPENER   = getattr(M, "OPENER", [])       # 首页大卡片 [(标题, 正文, 标签)]
FLOW     = getattr(M, "FLOW", [])          # 模型进化链
SECTIONS = getattr(M, "SECTIONS", [])

# ---------------- 渲染 ----------------

def render_block(b):
    kind = b[0]
    if kind == "p":
        return f'<p class="rp">{mj(b[1])}</p>'
    if kind == "big":
        return f'<div class="rbig">{mj(b[1])}</div>'
    if kind == "ul":
        items = "".join(f"<li>{mj(x)}</li>" for x in b[1])
        return f'<ul class="rul">{items}</ul>'
    if kind == "ol":
        items = "".join(f"<li>{mj(x)}</li>" for x in b[1])
        return f'<ol class="rol">{items}</ol>'
    if kind == "warn":
        return f'<div class="warn"><b>⚠ {mj(b[1])}：</b>{mj(b[2])}</div>'
    if kind == "tip":
        return f'<div class="tip"><b>💡 {mj(b[1])}：</b>{mj(b[2])}</div>'
    if kind == "note":
        return f'<div class="explain"><b>{mj(b[1])}：</b>{mj(b[2])}</div>'
    if kind == "table":
        return render_table(b[1])
    if kind == "cards":
        cards = []
        for c in b[1]:
            tag = f'<div class="msub">{mj(c["sub"])}</div>' if c.get("sub") else ""
            cards.append(
                f'<div class="mcard"><div class="mhead">{mj(c["title"])}</div>{tag}'
                f'<div class="mbody">{mj(c["body"])}</div></div>')
        return f'<div class="cards">{ "".join(cards) }</div>'
    if kind == "steps":
        rows = []
        for i, (t, body) in enumerate(b[1], 1):
            rows.append(f'<div class="stp"><span class="stn">{i}</span>'
                        f'<div><div class="stt">{mj(t)}</div>'
                        f'<div class="stb">{mj(body)}</div></div></div>')
        return f'<div class="steps">{"".join(rows)}</div>'
    if kind == "eq":
        rows = []
        for it in b[1]:
            name, tex, note = it[0], it[1], it[2]
            ref = it[3] if len(it) > 3 else ""
            refhtml = f'<div class="eqref">{mj(ref)}</div>' if ref else ""
            rows.append(
                f'<div class="eqrow"><div class="eqn">{mj(name)}</div>'
                f'<div class="eqm">\\[{mj(tex)}\\]</div>'
                f'<div class="eqd">{mj(note)}{refhtml}</div></div>')
        cap = b[2] if len(b) > 2 else ""
        caphtml = f'<div class="eqcap">{mj(cap)}</div>' if cap else ""
        return f'<div class="eqbox">{caphtml}{"".join(rows)}</div>'
    if kind == "raw":
        return b[1]
    raise ValueError(f"未知块类型 {kind}")


def render_table(d):
    cls = d.get("cls", "table")
    cap = f'<div class="tcap">{mj(d["caption"])}</div>' if d.get("caption") else ""
    head = ""
    if d.get("header"):
        head = "<tr>" + "".join(f"<th>{mj(h)}</th>" for h in d["header"]) + "</tr>"
    body = []
    for r in d["rows"]:
        if isinstance(r, str):                       # 分组行
            body.append(f'<tr class="grp"><td colspan="{len(d.get("header") or [1])}">{mj(r)}</td></tr>')
        elif r and r[0] == "__grp__":
            body.append(f'<tr class="grp"><td colspan="{len(d.get("header") or [1])}">{mj(r[1])}</td></tr>')
        else:
            cells = []
            for i, c in enumerate(r):
                k = ' class="rowhead"' if i == 0 and d.get("first_bold") else ""
                cells.append(f"<td{k}>{mj(c)}</td>")
            body.append("<tr>" + "".join(cells) + "</tr>")
    note = f'<div class="tnote">{mj(d["note"])}</div>' if d.get("note") else ""
    return (f'<div class="tbox">{cap}<div class="tw"><table class="{cls}">{head}{"".join(body)}</table></div>{note}</div>')


def render_flow():
    if not FLOW:
        return ""
    nodes = []
    for i, n in enumerate(FLOW):
        tag = n.get("tag", "")
        taghtml = f'<span class="ftag">{mj(tag)}</span>' if tag else ""
        nodes.append(
            f'<div class="fnode"><div class="fnum">{mj(n["num"])}</div>'
            f'<div class="fttl">{mj(n["title"])}</div>'
            f'<div class="fdesc">{mj(n["desc"])}</div>{taghtml}</div>')
    return f'<div class="flow">{"".join(nodes)}</div>'


CSS = """
:root{
 --bg:#f8fafc; --card:#fff; --card2:#f1f5f9; --card3:#e8eef7;
 --ink:#0f172a; --ink2:#334155; --muted:#64748b; --line:#dbe3ee;
 --accent:#2563eb; --accent-soft:#eff6ff; --accent-ink:#1d4ed8; --accent2:#6d28d9;
 --green:#047857; --green-soft:#ecfdf5; --green-ink:#047857;
 --orange:#b45309; --orange-soft:#fffbeb; --orange-ink:#92400e;
 --red:#b91c1c; --red-soft:#fef2f2; --purple:#6d28d9; --purple-soft:#f5f3ff;
 --formula-bg:#f1f5f9; --formula-ink:#0f172a;
 --th-bg:#eef2f9; --th-ink:#1e40af; --plain-bg:#eef6ff;
}
[data-theme="dark"]{
 --bg:#0f172a; --card:#1b2437; --card2:#243146; --card3:#2d3b53;
 --ink:#f8fafc; --ink2:#d4dded; --muted:#94a3b8; --line:#3b4a63;
 --accent:#7db4ff; --accent-soft:#152f52; --accent-ink:#8cc0ff; --accent2:#b9a2ff;
 --green:#4ade80; --green-soft:#08301f; --green-ink:#4ade80;
 --orange:#fbbf24; --orange-soft:#3a2708; --orange-ink:#fcd34d;
 --red:#fb8a8a; --red-soft:#3d1414; --purple:#b9a2ff; --purple-soft:#251a45;
 --formula-bg:#0b2038; --formula-ink:#c7e0ff;
 --th-bg:#22304a; --th-ink:#9ec9ff; --plain-bg:#132742;
}
*{box-sizing:border-box;}
body{margin:0;background:var(--bg);color:var(--ink);font-family:"Segoe UI","Microsoft YaHei",-apple-system,sans-serif;line-height:1.85;font-size:16px;}
.wrap{max-width:1040px;margin:0 auto;padding:32px 24px 104px;}
header.hero{background:linear-gradient(135deg,#1e3a8a,#2563eb);color:#fff;border-radius:16px;padding:32px 38px;margin-bottom:20px;}
.home{display:inline-block;background:rgba(255,255,255,.2);color:#fff;border-radius:999px;
 padding:2px 12px;font-size:12.5px;font-weight:700;text-decoration:none;margin-bottom:10px;}
.home:hover{background:rgba(255,255,255,.34);text-decoration:none;color:#fff;}
header.hero h1{margin:0 0 8px;font-size:26px;line-height:1.4;}
header.hero p{margin:8px 0 0;opacity:.93;font-size:15px;}
.hero .meta{display:flex;flex-wrap:wrap;gap:10px;margin-top:16px;}
.hero .meta span{background:rgba(255,255,255,.16);border-radius:999px;padding:3px 14px;font-size:13px;}
.sec-title{font-size:22px;margin:44px 0 6px;padding-left:12px;border-left:6px solid var(--accent);}
.sec-sub{color:var(--muted);font-size:14px;margin:0 0 16px;padding-left:18px;}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:22px 26px;margin:16px 0;box-shadow:0 1px 3px rgba(15,23,42,.05);}
.rp{margin:10px 0;font-size:15.3px;}
.rbig{background:var(--accent-soft);border-left:5px solid var(--accent);border-radius:0 10px 10px 0;padding:14px 18px;margin:14px 0;font-size:15.5px;}
.rbig b{color:var(--accent-ink);}
.rul{margin:8px 0;padding-left:22px;font-size:15px;}
.rul li{margin:6px 0;}
.rol{margin:8px 0;padding-left:24px;font-size:15px;}
.rol li{margin:7px 0;}
.explain{background:var(--card2);border-radius:10px;padding:11px 16px;margin:11px 0;font-size:14.8px;}
.tip{background:var(--orange-soft);border-radius:10px;padding:10px 16px;margin-top:12px;font-size:14px;}
.tip b{color:var(--orange);}
.warn{background:var(--red-soft);border-radius:10px;padding:10px 16px;margin-top:12px;font-size:14px;}
.warn b{color:var(--red);}
.tw{overflow-x:auto;-webkit-overflow-scrolling:touch;}
.tw table{min-width:640px;}
.table{width:100%;border-collapse:collapse;margin:6px 0;font-size:13.8px;}
.table th{background:var(--th-bg);color:var(--th-ink);padding:8px 10px;text-align:left;border:1px solid var(--line);font-size:13.5px;}
.table td{padding:8px 10px;border:1px solid var(--line);vertical-align:top;}
.table td.rowhead{font-weight:700;color:var(--accent-ink);background:var(--card2);}
.table tr.grp td{background:var(--th-bg);color:var(--th-ink);font-weight:800;font-size:13.2px;letter-spacing:.4px;}
.table.ctr td,.table.ctr th{text-align:center;}
.table.ctr td.rowhead{text-align:left;}
.table.pit td:first-child{font-weight:700;color:var(--accent-ink);width:19%;}
.table.pit td:nth-child(2){color:var(--red);}
.table.pit td:last-child{color:var(--green-ink);}
.tbox{margin:14px 0;}
.tcap{font-weight:800;font-size:15px;color:var(--accent-ink);margin-bottom:6px;padding-left:2px;}
.tnote{color:var(--muted);font-size:13px;margin-top:6px;line-height:1.75;}
.pj{color:var(--muted);font-size:11.5px;font-weight:400;}
/* 模型卡片 */
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(215px,1fr));gap:12px;margin:14px 0;}
.mcard{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--accent);border-radius:10px;padding:12px 16px;}
.mhead{font-weight:800;font-size:14.5px;color:var(--accent-ink);}
.msub{font-size:12.5px;color:var(--muted);margin:2px 0 6px;}
.mbody{font-size:14px;color:var(--ink2);line-height:1.8;}
/* 模型进化链 */
.flow{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px;margin:16px 0;}
.fnode{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 14px;position:relative;}
.fnode::after{content:"→";position:absolute;right:-13px;top:50%;transform:translateY(-50%);color:var(--muted);font-weight:900;font-size:15px;}
.fnode:nth-child(4n)::after,.fnode:last-child::after{content:"";}
.fnum{font-size:11.5px;font-weight:800;color:#fff;background:var(--accent);border-radius:999px;display:inline-block;padding:1px 9px;margin-bottom:6px;}
.fttl{font-weight:800;font-size:14px;color:var(--ink);line-height:1.5;}
.fdesc{font-size:12.8px;color:var(--muted);margin-top:4px;line-height:1.65;}
.ftag{display:inline-block;margin-top:6px;font-size:11.5px;background:var(--accent-soft);color:var(--accent-ink);border-radius:6px;padding:1px 8px;}
@media (max-width:820px){.fnode::after{display:none;}}
/* 步骤 */
.steps{margin:14px 0;}
.stp{display:grid;grid-template-columns:34px 1fr;gap:12px;align-items:start;padding:10px 0;border-top:1px dashed var(--line);}
.stp:first-child{border-top:none;}
.stn{width:26px;height:26px;line-height:26px;text-align:center;border-radius:50%;background:var(--accent);color:#fff;font-weight:800;font-size:13px;}
.stt{font-weight:800;font-size:14.6px;color:var(--accent-ink);}
.stb{font-size:14.2px;color:var(--ink2);line-height:1.8;}
/* 公式块 */
.eqbox{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 18px;margin:14px 0;}
.eqcap{font-weight:800;font-size:14.5px;color:var(--accent-ink);margin-bottom:8px;}
.eqrow{display:grid;grid-template-columns:190px minmax(0,1fr);gap:14px;padding:10px 0;border-top:1px dashed var(--line);align-items:start;}
.eqrow:first-of-type{border-top:none;}
.eqn{font-weight:700;font-size:13.8px;color:var(--ink);line-height:1.7;}
.eqm{overflow-x:auto;overflow-y:hidden;font-size:15px;padding:2px 0;}
.eqd{grid-column:2;font-size:13.2px;color:var(--muted);line-height:1.75;margin-top:-4px;}
.eqref{color:var(--accent-ink);font-size:12.5px;margin-top:2px;}
@media (max-width:720px){.eqrow{grid-template-columns:1fr;}.eqd{grid-column:1;}}
a.xref{color:var(--accent-ink);text-decoration:none;border-bottom:1.5px solid var(--accent-soft);padding-bottom:1px;white-space:nowrap;}
a.xref:hover{border-bottom-color:var(--accent);background:var(--accent-soft);border-radius:3px;}
a.xref::after{content:"↗";font-size:.8em;vertical-align:super;margin-left:2px;opacity:.75;}
a.xref.in::after{content:"";}
.xref-off{color:var(--muted);border-bottom:1px dashed var(--muted);white-space:nowrap;}
.theme-toggle{position:fixed;top:16px;right:20px;z-index:999;display:flex;gap:4px;background:var(--card)!important;border:1px solid var(--line)!important;border-radius:999px;padding:4px;box-shadow:0 2px 8px rgba(15,23,42,.15);}
.theme-toggle button{border:none;background:transparent!important;color:var(--ink2)!important;font-size:13px;font-weight:600;padding:5px 14px;border-radius:999px;cursor:pointer;font-family:inherit;}
.theme-toggle button.active{background:var(--accent)!important;color:#fff!important;}
#toc{position:fixed;top:70px;right:20px;z-index:998;width:236px;max-height:82vh;overflow:auto;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:10px 14px;font-size:12.8px;box-shadow:0 2px 8px rgba(15,23,42,.1);display:none;}
#toc b{display:block;margin-bottom:6px;color:var(--accent);}
#toc a{display:block;color:var(--ink2);text-decoration:none;padding:3px 0;border-bottom:1px dashed var(--line);}
#toc a:hover{color:var(--accent);}
@media (min-width:1540px){#toc{display:block;}}
@media print{#toc,.theme-toggle{display:none!important;}}
footer{margin-top:52px;color:var(--muted);font-size:13px;text-align:center;}
.mj{font-family:"Cambria Math","Times New Roman",serif;color:var(--accent-ink);font-style:italic;}
"""


def toc_html():
    items = "".join(f'<a href="#{s["id"]}">{s["num"]}、{s["title"]}</a>' for s in SECTIONS)
    return f'<b>总复习目录</b>{items}'


def opener_html():
    if not OPENER:
        return ""
    cards = []
    for t, body, tag in OPENER:
        cards.append(
            f'<div class="mcard"><div class="mhead">{mj(t)}</div>'
            f'<div class="mbody">{mj(body)}</div>'
            f'<div class="ftag">{mj(tag)}</div></div>')
    return f'<div class="cards">{"".join(cards)}</div>'


body = []
for s in SECTIONS:
    parts = [f'<div class="sec-title" id="{s["id"]}">{s["num"]}、{mj(s["title"])}</div>']
    if s.get("sub"):
        parts.append(f'<div class="sec-sub">{mj(s["sub"])}</div>')
    parts.append('<div class="card">')
    for b in s["blocks"]:
        parts.append(render_block(b))
    parts.append('</div>')
    body.append("".join(parts))

CSS += U.CSS
UI_HTML = U.html(CURFILE, U.order(HERE), toc=True)
UI_JS = U.JS()
NEXTNAV = U.bottom(CURFILE, U.order(HERE))

doc = f"""<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{html.escape(COURSE)} · {html.escape(TITLE)}</title>
<style>{CSS}</style>
<script>window.MathJax={{tex:{{inlineMath:[['\\\\(','\\\\)']],displayMath:[['\\\\[','\\\\]']]}},svg:{{fontCache:'global'}}}};</script>
<script src="./_mathjax_tex_svg.js"></script>
</head>
<body>
{UI_HTML}
<div class="theme-toggle">
 <button id="btn-light" onclick="setTheme('light')">☀ 浅色</button>
 <button id="btn-dark" onclick="setTheme('dark')">🌙 深色</button>
</div>
<div id="toc">{toc_html()}</div>
<div class="wrap">
 <header class="hero">
  <a class="home" href="../index.html">← 复习总台</a>
  <h1>{html.escape(COURSE)} · {html.escape(TITLE)}</h1>
  <p>{html.escape(SUBTITLE)}</p>
  <div class="hero meta">{''.join(f'<span>{html.escape(m)}</span>' for m in META)}</div>
 </header>
{opener_html()}
 <div class="sec-title" id="flow">课程主干：八个模型怎么长出下一个</div>
 <div class="sec-sub">从左到右读：每一个模型都是在上一个模型上「只改一处」。<b>第一行读到 T6，第二行接着 T7 起。</b>看清改的是哪一处，就记住了它为什么存在。</div>
 <div class="card">{render_flow()}</div>
{''.join(body)}
{NEXTNAV}
 <footer>{html.escape(COURSE)} · 期末总复习 · 单文件离线 · 公式由 MathJax 渲染</footer>
</div>
<script>
function setTheme(t){{document.documentElement.setAttribute('data-theme',t);document.getElementById('btn-light').classList.toggle('active',t==='light');document.getElementById('btn-dark').classList.toggle('active',t==='dark');try{{localStorage.setItem('af5638_theme',t);}}catch(e){{}}}}
(function(){{var t=null;try{{t=localStorage.getItem('af5638_theme');}}catch(e){{}}
 setTheme(t||document.documentElement.getAttribute('data-theme')||'light');}})();
(function(){{var jump=function(){{if(location.hash){{var el=document.querySelector(location.hash);if(el){{el.scrollIntoView();}}}}}};
window.addEventListener('load',function(){{setTimeout(jump,120);}});
if(window.MathJax&&MathJax.startup&&MathJax.startup.promise){{MathJax.startup.promise.then(function(){{setTimeout(jump,60);}});}}}})();
{UI_JS}
</script>
</body></html>"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(doc)

print("wrote", OUT, "size KB:", round(len(doc.encode("utf-8")) / 1024, 1))
print("sections:", len(SECTIONS), "| flow nodes:", len(FLOW), "| blocks:",
      sum(len(s["blocks"]) for s in SECTIONS))
