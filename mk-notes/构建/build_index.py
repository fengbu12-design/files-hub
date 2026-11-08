# -*- coding: utf-8 -*-
"""
AF5638 期末复习 · 主页（index.html）生成器
==================================================================
用法：
    python build_index.py

数据来源（全部现读，不写死）：
  content_topic1..10.py  → 每讲标题、页数、EXAM（考点标注）
  review_content.py      → 总复习 9 节标题
  practice_content.py    → 练习 4 节、题目数量
所以：加课、加题、加考点之后，重跑本脚本首页自动跟上。

产物是单文件离线 HTML（与各笔记同目录），复用 _mathjax_tex_svg.js。
"""
import os, re, html, importlib.util
from datetime import datetime
import ui_shell as U
import paths as P
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = P.index_page()

COURSE = "AF5638 宏观经济学"
EXAM_LINE = "期末 50% · 考试期 12 月 3–18 日（Syllabus 原文：examination period of December 3–18）"


# ---------- 载入 ----------
def load(path, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


MJ = re.compile(r"<span class='mj'>(.*?)</span>", re.S)


def mj(s):
    """<span class='mj'>X</span> → \\(X\\)；**强调** → <b>"""
    s = MJ.sub(lambda m: "\\(" + m.group(1) + "\\)", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    return s


def plain(s):
    """给搜索用的纯文本：去标签、去公式"""
    s = MJ.sub(lambda m: " " + m.group(1) + " ", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("\\(", " ").replace("\\)", " ")
    return re.sub(r"\s+", " ", s).strip()


def fname(topic):
    return f"Topic {topic} 笔记.html"


# ---------- 十讲 ----------
KIND_LABEL = {"final": ("期末考点", "k-final"), "mid": ("期中考点", "k-mid"), "must": ("必背", "k-must")}
KIND_SHORT = {"final": "老师划的", "mid": "期中", "must": "必背"}

# 三块大陆：课程地图上的分组（与总复习 §1 一致）
BLOCKS = [
    ("长期：几十年", "T1–T3", [1, 2, 3], "增长从哪来、为什么有的国家富"),
    ("跨期与一般均衡：几年", "T4–T7", [4, 5, 6, 7], "消费怎么决策、价格怎么被解出来"),
    ("短期：几个月", "T8–T10", [8, 9, 10], "波动、货币、粘性价格"),
]

TOPICS = {}
TAGS = []
for n in range(1, 11):
    m = load(f"content_topic{n}.py", f"t{n}")
    ex = getattr(m, "EXAM", {})
    cnt = {"final": 0, "mid": 0, "must": 0}
    for pid in sorted(ex):
        for it in ex[pid]:
            if isinstance(it, str):
                it = {"k": "must", "t": it}
            k = it.get("k", "must")
            cnt[k] = cnt.get(k, 0) + 1
            TAGS.append(dict(t=n, pid=pid, k=k, ref=it.get("ref"),
                             body=mj(it["t"]), text=plain(it["t"])))
    path = P.page(fname(n))
    TOPICS[n] = dict(
        n=n, title=getattr(m, "TOPIC_TITLE", f"Topic {n}"),
        pages=getattr(m, "SLIDE_COUNT", 0),
        kb=round(os.path.getsize(path) / 1024) if os.path.exists(path) else 0,
        tags=len(TAGS) and sum(cnt.values()), cnt=cnt,
        file=quote(fname(n)),
    )

TOTAL_PAGES = sum(t["pages"] for t in TOPICS.values())
TOTAL_TAGS = len(TAGS)
N_FINAL = sum(1 for x in TAGS if x["k"] == "final")
N_MID = sum(1 for x in TAGS if x["k"] == "mid")
N_MUST = sum(1 for x in TAGS if x["k"] == "must")

# ---------- 总复习 ----------
RV = load("review_content.py", "rv")
REVIEW_FILE = quote("期末总复习.html")

# ---------- 练习 ----------
PC = load("practice_content.py", "pc")
P_FILE = quote("期末练习.html")
N_Q = sum(len(s.get("items", [])) for s in PC.SECTIONS)
QIDS = sorted({f"{s['id']}{it['tag']}" for s in PC.SECTIONS for it in s.get("items", [])})
PSEC = [(s.get("num", ""), s.get("title", ""), s.get("id", ""), len(s.get("items", [])))
        for s in PC.SECTIONS]


# ---------- 片段 ----------
def topic_card(n):
    t = TOPICS[n]
    dots = ""
    if t["cnt"]["final"]:
        dots += f'<span class="dot f" title="老师划的期末考点 {t["cnt"]["final"]} 条">{t["cnt"]["final"]}</span>'
    if t["cnt"]["mid"]:
        dots += f'<span class="dot m" title="期中考点 {t["cnt"]["mid"]} 条">{t["cnt"]["mid"]}</span>'
    if t["cnt"]["must"]:
        dots += f'<span class="dot u" title="必背 {t["cnt"]["must"]} 条">{t["cnt"]["must"]}</span>'
    return (f'<a class="tcard" href="{t["file"]}">'
            f'<div class="tnum">T{n}</div>'
            f'<div class="tbody"><div class="tname">{html.escape(t["title"].split("·", 1)[-1].strip())}</div>'
            f'<div class="tmeta">{t["pages"]} 页 · {t["kb"]} KB</div></div>'
            f'<div class="tdots">{dots}</div></a>')


def block_html(label, rng, ns, sub):
    cards = "".join(topic_card(n) for n in ns)
    return (f'<div class="block"><div class="bhead"><b>{html.escape(label)}</b>'
            f'<span class="brange">{rng}</span><span class="bsub">{html.escape(sub)}</span></div>'
            f'<div class="tgrid">{cards}</div></div>')


def refdisp(ref):
    """q2g → Q2(g)"""
    m = re.fullmatch(r"([qQ])(\d)([a-h])", ref or "")
    return f"{m.group(1).upper()}{m.group(2)}({m.group(3)})" if m else (ref or "")


def tag_row(x):
    label, cls = KIND_LABEL[x["k"]]
    t = TOPICS[x["t"]]
    note = (f'<a class="go" href="{t["file"]}#p{x["pid"]}">笔记 p{x["pid"]}</a>')
    # 没有对应题号的就不放占位符（整列都是「—」很吵）
    q = (f' <a class="q" href="{P_FILE}#{x["ref"].lower()}">{html.escape(refdisp(x["ref"]))}</a>'
         if x["ref"] else "")
    return (f'<tr data-k="{x["k"]}" data-t="{x["t"]}" '
            f'data-s="{html.escape((x["text"] + " t" + str(x["t"]) + " p" + str(x["pid"]) + " " + (x["ref"] or "")).lower())}">'
            f'<td class="c1"><span class="tt">T{x["t"]}</span><span class="pp">p{x["pid"]}</span></td>'
            f'<td class="c2"><span class="kind {cls}">{label}</span></td>'
            f'<td class="c3">{x["body"]}</td>'
            f'<td class="c4">{note}{q}</td></tr>')


def route(num, title, when, steps):
    lis = "".join(f'<li>{s}</li>' for s in steps)
    return (f'<div class="rcard"><div class="rnum">{num}</div><div class="rh">'
            f'<b>{title}</b><span>{when}</span></div><ol>{lis}</ol></div>')


N_PAGES = f'{TOTAL_PAGES}'

ROUTES = "".join([
    route("A", "只剩两天：先做真题", "最省时间的顺序", [
        f'先把 <a href="{P_FILE}">16 道练习</a>自己写一遍，写完再点开答案对判分点',
        f'背 <a href="{REVIEW_FILE}#s7">总复习 §7 的四张表</a>（T8 6×5 / T9 8×7 / T10 九情形 / 三种粘性）',
        f'把笔记里 <b>{N_FINAL} 条红色徽标</b>（老师亲手划的）逐页过一遍：从 <a href="Topic 6 笔记.html#examidx">T6</a>、'
        f'<a href="Topic 7 笔记.html#examidx">T7</a>、<a href="Topic 8 笔记.html#examidx">T8</a> 的一览卡进',
        f'最后看 <a href="{REVIEW_FILE}#s8">总复习 §8 三套答题模板</a>，背句型而不是背答案',
    ]),
    route("B", "还有五到七天：按讲补", "每天两讲，配总复习兜底", [
        f'第一天只做两件事：<a href="{REVIEW_FILE}">总复习</a>的 §1 三块大陆 + §2 八模型对照表',
        '之后每天两讲：先看该讲「速览 + 图」，再逐页看，最后做讲末自测（答案折叠）',
        f'补完 <a href="Topic 4 笔记.html">T4</a>–<a href="Topic 7 笔记.html">T7</a> 那天，回头读 '
        f'<a href="{REVIEW_FILE}#s5">§5「消费函数被装配七次」</a>——这四讲其实只改了它一次',
        f'考前两天切到路线 A 的第 1、2 步（练习 + 四张表）',
    ]),
    route("C", "从头补：十天以上", "按大陆推进，别按页码", [
        '第一块 <a href="Topic 1 笔记.html">T1</a>→<a href="Topic 3 笔记.html">T3</a>：增长事实、索洛、跨国差异（一条资本积累式串完）',
        '第二块 <a href="Topic 4 笔记.html">T4</a>→<a href="Topic 7 笔记.html">T7</a>：两期消费、禀赋经济、财政、生产经济（都在装配同一条消费函数）',
        '第三块 <a href="Topic 8 笔记.html">T8</a>→<a href="Topic 10 笔记.html">T10</a>：两条曲线、货币进来、价格粘住（同一个需求侧，三个供给侧）',
        f'每讲收尾都用 <a href="{REVIEW_FILE}#s9">§9 的 24 问自测</a>验一遍，答不上来说明该回哪一节',
    ]),
])


def kb_fmt(kb):
    return f"{kb / 1024:.1f} MB" if kb >= 1024 else f"{kb} KB"


MATERIALS = [
    ("index.html", "本页：总入口 + 99 条考点总表", ""),
    ("Topic 1–10 笔记.html", f"十讲逐页精讲，共 {TOTAL_PAGES} 页", kb_fmt(sum(t["kb"] for t in TOPICS.values()))),
    ("期末总复习.html", "九节横向拉通：八模型 / 45 条公式 / 四张必背表 / 三套模板", kb_fmt(78)),
    ("期末练习.html", f"老师给的 Final Practice 逐题精做，{N_Q} 小问", kb_fmt(115)),
    ("final_practice.pdf", "练习卷原件（老师在更新，10-27 版）", kb_fmt(136)),
    ("使用说明.md", "这套材料怎么改、怎么加题、怎么加考点", kb_fmt(26)),
]

MAT_ROWS = "".join(
    f'<tr><td class="mf">{html.escape(a)}</td><td>{html.escape(b)}</td><td class="ms">{c}</td></tr>'
    for a, b, c in MATERIALS
)


# ---------- 页面 ----------
CSS = """
:root{
 --bg:#f6f8fc; --card:#fff; --card2:#f1f5f9; --card3:#e8eef7;
 --ink:#0f172a; --ink2:#334155; --muted:#64748b; --line:#dbe3ee;
 --accent:#2563eb; --accent-soft:#eff6ff; --accent-ink:#1d4ed8;
 --green:#047857; --green-soft:#ecfdf5;
 --orange:#b45309; --orange-soft:#fffbeb;
 --red:#b91c1c; --red-soft:#fef2f2;
 --purple:#6d28d9; --purple-soft:#f5f3ff;
}
[data-theme="dark"]{
 --bg:#0f172a; --card:#1b2437; --card2:#243146; --card3:#2d3b53;
 --ink:#f8fafc; --ink2:#d4dded; --muted:#94a3b8; --line:#3b4a63;
 --accent:#7db4ff; --accent-soft:#152f52; --accent-ink:#8cc0ff;
 --green:#4ade80; --green-soft:#08301f;
 --orange:#fbbf24; --orange-soft:#3a2708;
 --red:#fb8a8a; --red-soft:#3d1414;
 --purple:#b9a2ff; --purple-soft:#251a45;
}
*{box-sizing:border-box;}
body{margin:0;background:var(--bg);color:var(--ink);
 font-family:"Segoe UI","Microsoft YaHei",-apple-system,sans-serif;line-height:1.75;font-size:16px;}
.wrap{max-width:1180px;margin:0 auto;padding:26px 24px 70px;}
a{color:var(--accent-ink);text-decoration:none;}
a:hover{text-decoration:underline;}

/* 顶栏 */
.top{display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;}
.top .brand{font-weight:800;font-size:15px;color:var(--ink2);letter-spacing:.3px;}
.theme-toggle{display:flex;gap:4px;background:var(--card);border:1px solid var(--line);border-radius:999px;padding:4px;}
.theme-toggle button{border:none;background:transparent;color:var(--ink2);font-size:13px;font-weight:600;
 padding:4px 12px;border-radius:999px;cursor:pointer;font-family:inherit;}
.theme-toggle button.active{background:var(--accent);color:#fff;}

/* hero */
.hero{background:linear-gradient(135deg,#1e3a8a,#2563eb 55%,#0ea5e9);color:#fff;
 border-radius:20px;padding:34px 38px 30px;position:relative;overflow:hidden;}
.hero:after{content:"";position:absolute;right:-60px;top:-60px;width:260px;height:260px;
 background:radial-gradient(circle,rgba(255,255,255,.18),transparent 70%);}
.hero h1{margin:0 0 8px;font-size:30px;letter-spacing:.5px;}
.hero p{margin:0;opacity:.94;font-size:14.5px;}
.hero .examline{margin-top:12px;display:inline-block;background:rgba(255,255,255,.16);
 border-radius:999px;padding:4px 14px;font-size:13px;}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:22px;position:relative;z-index:1;}
.stat{background:rgba(255,255,255,.13);border-radius:12px;padding:12px 14px;}
.stat b{display:block;font-size:26px;line-height:1.2;}
.stat span{font-size:12.5px;opacity:.9;}

/* 三块主体 */
.mains{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:18px 0 6px;}
.main{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:20px 22px;
 box-shadow:0 1px 3px rgba(15,23,42,.05);transition:.18s;display:flex;flex-direction:column;}
.main:hover{transform:translateY(-3px);box-shadow:0 10px 24px rgba(15,23,42,.10);border-color:var(--accent);}
.main .tagline{font-size:12px;font-weight:800;letter-spacing:.6px;color:var(--accent);text-transform:uppercase;}
.main h2{margin:6px 0 6px;font-size:20px;}
.main p{margin:0 0 10px;color:var(--ink2);font-size:13.8px;}
.main ul{margin:0 0 14px;padding-left:18px;color:var(--muted);font-size:13px;}
.main ul li{margin:3px 0;}
.main .go-btn{margin-top:auto;display:inline-block;background:#2563eb;color:#fff;
 border-radius:10px;padding:9px 16px;font-size:14px;font-weight:700;text-align:center;}
.main .go-btn:hover{text-decoration:none;filter:brightness(1.06);}
.main.rev .go-btn{background:#6d28d9;}
.main.pra .go-btn{background:#047857;}

/* 通用节标题 */
.sec{margin:34px 0 12px;display:flex;align-items:baseline;gap:10px;}
.sec h2{margin:0;font-size:19px;padding-left:11px;border-left:5px solid var(--accent);}
.sec .hint{font-size:13px;color:var(--muted);}

/* 十讲 */
.block{margin-bottom:16px;}
.bhead{display:flex;align-items:center;gap:10px;margin:0 0 8px;}
.bhead b{font-size:14.5px;}
.brange{font-size:12px;color:#fff;background:#475569;border-radius:6px;padding:1px 8px;font-weight:700;}
.bsub{font-size:12.5px;color:var(--muted);}
.tgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(268px,1fr));gap:10px;}
.tcard{display:flex;align-items:center;gap:11px;background:var(--card);border:1px solid var(--line);
 border-radius:12px;padding:11px 14px;color:var(--ink);transition:.15s;}
.tcard:hover{border-color:var(--accent);background:var(--accent-soft);text-decoration:none;transform:translateX(2px);}
.tnum{font-weight:800;font-size:13px;color:#fff;background:#2563eb;border-radius:8px;padding:3px 9px;min-width:34px;text-align:center;}
.tbody{flex:1;min-width:0;}
.tname{font-size:14px;font-weight:700;}
.tmeta{font-size:11.8px;color:var(--muted);}
.tdots{display:flex;gap:4px;}
.dot{font-size:11px;font-weight:800;color:#fff;border-radius:999px;min-width:19px;text-align:center;padding:1px 5px;}
.dot.f{background:#b91c1c;} .dot.m{background:#b45309;} .dot.u{background:#6d28d9;}

/* 路线 */
.routes{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;}
.rcard{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px 18px 14px;position:relative;}
.rnum{position:absolute;right:14px;top:10px;font-size:30px;font-weight:900;color:var(--card3);line-height:1;}
.rh b{display:block;font-size:15.5px;}
.rh span{font-size:12.3px;color:var(--muted);}
.rcard ol{margin:8px 0 0;padding-left:20px;font-size:13.2px;color:var(--ink2);}
.rcard li{margin:6px 0;}

/* 考点表 */
.tools{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:0 0 10px;}
.chip{border:1px solid var(--line);background:var(--card);color:var(--ink2);border-radius:999px;
 padding:4px 13px;font-size:13px;cursor:pointer;font-family:inherit;font-weight:600;}
.chip.on{background:#2563eb;border-color:#2563eb;color:#fff;}
.chip .c{opacity:.75;font-weight:700;margin-left:3px;}
.search{flex:1;min-width:200px;border:1px solid var(--line);background:var(--card);color:var(--ink);
 border-radius:999px;padding:6px 15px;font-size:13.5px;font-family:inherit;outline:none;}
.search:focus{border-color:var(--accent);}
.count{font-size:12.5px;color:var(--muted);margin-left:auto;}
.tblwrap{background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden;}
table{width:100%;border-collapse:collapse;font-size:13.6px;}
thead th{background:var(--card2);color:var(--ink2);font-size:12.5px;text-align:left;
 padding:9px 12px;border-bottom:1px solid var(--line);font-weight:700;position:sticky;top:0;}
tbody td{padding:8px 12px;border-bottom:1px solid var(--line);vertical-align:middle;}
tbody tr:hover{background:var(--accent-soft);}
tbody tr:last-child td{border-bottom:none;}
.c1{white-space:nowrap;}
.tt{font-weight:800;color:var(--accent-ink);}
.pp{color:var(--muted);margin-left:5px;font-size:12.5px;}
.kind{font-size:11.5px;font-weight:800;color:#fff;border-radius:999px;padding:1px 8px;white-space:nowrap;}
.k-final{background:#b91c1c;} .k-mid{background:#b45309;} .k-must{background:#6d28d9;}
.c3{color:var(--ink);}
.c4{white-space:nowrap;text-align:right;}
.go{font-size:12.5px;border-bottom:1px dashed var(--accent);}
.q{font-size:11.8px;color:#fff;background:#2563eb;border-radius:6px;padding:1px 7px;font-weight:700;}
.q.off{background:transparent;color:var(--muted);}
.q:hover{text-decoration:none;filter:brightness(1.1);}
tr.hide{display:none;}
.tnote{font-size:12.5px;color:var(--muted);margin-top:8px;}

/* 材料表 */
.mf{font-family:Consolas,monospace;font-size:12.8px;color:var(--accent-ink);}
.ms{color:var(--muted);text-align:right;}
footer{margin-top:44px;color:var(--muted);font-size:12.8px;text-align:center;line-height:1.9;}
@media(max-width:900px){
 .mains,.routes{grid-template-columns:1fr;}
 .stats{grid-template-columns:repeat(2,1fr);}
}
"""

CSS += U.CSS
UI_HTML = U.html("index.html", U.order(HERE), bare=True)
UI_JS = U.JS()


def doc():
    nav_blocks = "".join(block_html(lb, rg, ns, sb) for lb, rg, ns, sb in BLOCKS)
    rows = "".join(tag_row(x) for x in TAGS)
    # 总复习九节：用「一、标题」的写法，别写成 §一
    rv_secs = " · ".join(f'{s.get("num")}、{s.get("title").split("：")[0]}' for s in RV.SECTIONS)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    total_kb = sum(t["kb"] for t in TOPICS.values())

    return f"""<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{html.escape(COURSE)} · 期末复习总台</title>
<style>{CSS}</style>
</head>
<body>
{UI_HTML}
<div class="wrap">

<div class="top">
 <div class="brand">{html.escape(COURSE)} · 期末复习总台</div>
 <div class="theme-toggle">
  <button id="btn-light" onclick="setTheme('light')">☀ 浅色</button>
  <button id="btn-dark" onclick="setTheme('dark')">🌙 深色</button>
 </div>
</div>

<header class="hero">
 <h1>AF5638 · 期末复习总台</h1>
 <p>十讲逐页笔记 ＋ 横向总复习 ＋ 老师那份练习 —— 三样东西从这一页进，考点从这一页查。</p>
 <div class="examline">{html.escape(EXAM_LINE)}</div>
 <div class="stats">
  <div class="stat"><b>10</b><span>讲 · {TOTAL_PAGES} 页课件</span></div>
  <div class="stat"><b>{TOTAL_TAGS}</b><span>条考点标注 · 其中老师划的 {N_FINAL} 条</span></div>
  <div class="stat"><b>{N_Q}</b><span>道练习小问 · 答案折叠</span></div>
  <div class="stat"><b>9</b><span>节总复习 · 4 张必背表</span></div>
 </div>
</header>

<div class="mains">
 <div class="main">
  <div class="tagline">读教材那一层</div>
  <h2>十讲逐页笔记</h2>
  <p>课件每一页都拆成：核心 · 白话 · 讲解 · 图的读法 · 等式两边 · 易错。</p>
  <ul>
   <li>{TOTAL_PAGES} 页逐页精讲，每页都有中文</li>
   <li>每讲末尾：公式速查 / 概念表 / 易错 / 自测</li>
   <li>页首红色徽标＝考点，本讲开头有「考点一览」</li>
  </ul>
  <a class="go-btn" href="Topic 1 笔记.html">从 Topic 1 开始 →</a>
 </div>
 <div class="main rev">
  <div class="tagline">横向拉通那一层</div>
  <h2>期末总复习</h2>
  <p>不按讲次，按「模型 / 方程 / 图 / 模板」重排一遍，专门治「学过但串不起来」。</p>
  <ul>
   <li>§2 八个模型对照表：每列只改一处</li>
   <li>§7 四张必背表 + §8 三套答题模板</li>
   <li>§9 二十四问自测，答不上来说明回哪节</li>
  </ul>
  <a class="go-btn" href="{REVIEW_FILE}">打开总复习 →</a>
 </div>
 <div class="main pra">
  <div class="tagline">动手那一层</div>
  <h2>期末练习精做</h2>
  <p>老师发的 Final Practice 原题 {N_Q} 小问，一题一卡：先自己写，再点开答案。</p>
  <ul>
   <li>每题四层：考什么 → 怎么写 → 判分点 → 扣分在哪</li>
   <li>答案给英文原句，可直接抄进卷子</li>
   <li>进度可勾选，关掉再开还在</li>
  </ul>
  <a class="go-btn" href="{P_FILE}">开始做题 →</a>
 </div>
</div>

<div class="sec"><h2>十讲地图</h2><span class="hint">按三块大陆分组；右边的小圆点是该讲的考点条数（红＝老师划的，橙＝期中，紫＝必背）</span></div>
{nav_blocks}

<div class="sec"><h2>按剩余时间选路线</h2><span class="hint">同一个材料库，三种走法；不知道从哪开始就先看 A</span></div>
<div class="routes">{ROUTES}</div>

<div class="sec"><h2>考点总表</h2><span class="hint">{TOTAL_TAGS} 条，可筛可搜；点「笔记 pXX」跳到那一页，点 Q 号跳到练习题</span></div>
<div class="tools">
 <button class="chip on" data-k="all">全部<span class="c">{TOTAL_TAGS}</span></button>
 <button class="chip" data-k="final">老师划的<span class="c">{N_FINAL}</span></button>
 <button class="chip" data-k="mid">期中<span class="c">{N_MID}</span></button>
 <button class="chip" data-k="must">必背<span class="c">{N_MUST}</span></button>
 <input class="search" id="q" type="search" placeholder="搜考点：挤出 / 稳态 / 李嘉图 / T8 / Q2g …"/>
 <span class="count" id="cnt"></span>
</div>
<div class="tblwrap">
<table id="tagtable">
 <thead><tr><th style="width:88px">讲 · 页</th><th style="width:104px">类型</th><th>考点</th><th style="width:150px;text-align:right">去哪看</th></tr></thead>
 <tbody>{rows}</tbody>
</table>
</div>
<div class="tnote">「老师划的」＝期末练习卷首页 Key Concepts 的原文落点（{N_FINAL} 条，只在 Topic 6/7/8）；
「期中」＝期中练习的 Key Concepts（{N_MID} 条）；「必背」＝我横向整理判断的高频项（{N_MUST} 条），<b>没有老师名录背书，别当考纲</b>。</div>

<div class="sec"><h2>材料清单</h2><span class="hint">全部单文件离线，双击即可；十讲笔记合计 {kb_fmt(total_kb)}</span></div>
<div class="tblwrap">
<table>
 <thead><tr><th style="width:240px">文件</th><th>说明</th><th style="width:90px;text-align:right">大小</th></tr></thead>
 <tbody>{MAT_ROWS}</tbody>
</table>
</div>

<footer>
 {html.escape(COURSE)} · 复习材料库 · 生成于 {now}<br/>
 总复习九节：{html.escape(rv_secs)}<br/>
 改完内容（加题 / 加考点 / 加讲）后重跑 <b>python build_index.py</b> 更新本页
</footer>
</div>

<script>
function setTheme(t){{
 document.documentElement.setAttribute('data-theme',t);
 document.getElementById('btn-light').classList.toggle('active',t==='light');
 document.getElementById('btn-dark').classList.toggle('active',t==='dark');
 try{{localStorage.setItem('af5638_theme',t);}}catch(e){{}}
}}
(function(){{
 var t=null;
 try{{t=localStorage.getItem('af5638_theme');}}catch(e){{}}
 // 没有保存过偏好时，尊重 <html data-theme>（否则深色会被强行改回浅色）
 setTheme(t||document.documentElement.getAttribute('data-theme')||'light');
}})();

/* 考点筛选 + 搜索：用 data-s（纯文本，事先去标签去公式）匹配，
   不依赖 MathJax 渲染后的 DOM，因此公式里的中文也能搜到 */
(function(){{
 var rows=[].slice.call(document.querySelectorAll('#tagtable tbody tr'));
 var chips=[].slice.call(document.querySelectorAll('.chip'));
 var q=document.getElementById('q'), cnt=document.getElementById('cnt');
 var kind='all';
 function apply(){{
   var kw=(q.value||'').trim().toLowerCase();
   var n=0;
   rows.forEach(function(r){{
     var ok=(kind==='all'||r.dataset.k===kind)&&(!kw||r.dataset.s.indexOf(kw)>=0);
     r.classList.toggle('hide',!ok);
     if(ok)n++;
   }});
   cnt.textContent='显示 '+n+' / '+rows.length+' 条';
 }}
 chips.forEach(function(c){{
   c.addEventListener('click',function(){{
     chips.forEach(function(x){{x.classList.remove('on');}});
     c.classList.add('on'); kind=c.dataset.k; apply();
   }});
 }});
 q.addEventListener('input',apply);
 document.addEventListener('keydown',function(e){{
   if(e.key==='/'&&document.activeElement!==q){{e.preventDefault();q.focus();}}
 }});
 apply();
}})();
{UI_JS}
</script>
<script>window.MathJax={{tex:{{inlineMath:[['\\\\(','\\\\)']]}},svg:{{fontCache:'global'}},startup:{{typeset:true}}}};</script>
<script src="./网页/_mathjax_tex_svg.js" defer></script>
</body>
</html>"""


# ---------- 输出 ----------
# 本页在根目录，12 个内容页在 网页/，所以正文里指向 .html 的链接统一补前缀。
# 只动「不带协议 / 不带 # / 不带 ../ / 不是 index.html 自己」的那一类，其余原样。
_HREF = re.compile(r'href="((?!https?:|mailto:|#|\.\.?/)(?!index\.html)[^"#/]+\.html)')


def _to_web(s):
    return _HREF.sub(lambda m: 'href="网页/' + m.group(1) + '"', s)


with open(OUT, "w", encoding="utf-8") as f:
    f.write(_to_web(doc()))

# ---------- 自检 ----------
_d = open(OUT, encoding="utf-8").read()
print("wrote", OUT, "size KB:", round(len(_d.encode("utf-8")) / 1024, 1))
print("topics:", len(TOPICS), "| pages:", TOTAL_PAGES, "| tags:", TOTAL_TAGS,
      f"(final {N_FINAL} / mid {N_MID} / must {N_MUST})", "| questions:", N_Q)

_ids = set(re.findall(r'id="([^"]+)"', _d))
_dead = sorted({h for h in re.findall(r'href="#([^"]+)"', _d) if h not in _ids})
if _dead:
    print("!! 站内跳转找不到目标：", _dead)

# 跨文件链接：目标文件存在 + 锚点真的在
import urllib.parse
_bad = []
for href in re.findall(r'href="([^"#]+\.html)(#[^"]*)?"', _d):
    fn, anchor = href
    path = os.path.join(P.ROOT, urllib.parse.unquote(fn))
    if not os.path.exists(path):
        _bad.append((fn, anchor, "文件不存在"))
        continue
    if anchor:
        if f'id="{anchor[1:]}"' not in open(path, encoding="utf-8").read():
            _bad.append((fn, anchor, "锚点不存在"))
if _bad:
    print("!! 坏链：", _bad[:6], "共", len(_bad))
else:
    print("链接自检：0 坏链")

if "<span class='mj'>" in _d:
    print("!! 还有未转换的公式标记")
if re.search(r"@@[A-Z]+@@", _d):
    print("!! 模板占位没替换")
