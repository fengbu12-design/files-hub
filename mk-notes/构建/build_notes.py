# -*- coding: utf-8 -*-
"""
通用课件逐页笔记生成器（AF5638 期末复习版）
==================================================================
用法：
    python build_notes.py          # 默认生成 Topic 1
    python build_notes.py 3        # 生成 Topic 3

工作原理：
  本脚本只负责「排版」，所有课程内容都在 content_topicN.py 里。
  想加一讲，只要复制 content_topic1.py → content_topic2.py 改内容即可。

配套文件：
  make_slides.py         渲染课件 PDF → TopicN_slides_jpg/ + _ref/SlidesN.txt
  _mathjax_tex_svg.js    离线 MathJax（必须与生成的 HTML 放在同一目录）
  content_topicN.py      每讲的内容文件

公式写法：在 content 文件里写
    '<span class=''mj''>Y=AK^{\\alpha}L^{1-\\alpha}</span>'
  本脚本会把 <span class='mj'> 转成 \\( ，</span> 转成 \\) ，交给 MathJax 渲染。
"""
import os, re, sys, base64, html, importlib.util
from PIL import Image
import ui_shell as U
import paths as P

HERE = os.path.dirname(os.path.abspath(__file__))
TOPIC = int(sys.argv[1]) if len(sys.argv) > 1 else 1

# 全站导航顺序（上一份 / 下一份）
ORDER = U.order(HERE)
CURFILE = f"Topic {TOPIC} 笔记.html"


# ---------- 载入内容文件 ----------
def load_content(topic):
    path = os.path.join(HERE, f"content_topic{topic}.py")
    if not os.path.exists(path):
        raise SystemExit(f"找不到内容文件：{path}\n请先复制 content_topic1.py 为 content_topic{topic}.py 再改内容。")
    spec = importlib.util.spec_from_file_location(f"content_topic{topic}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


M = load_content(TOPIC)

COURSE      = getattr(M, "COURSE", "课程")
TOPIC_TITLE = getattr(M, "TOPIC_TITLE", f"Topic {TOPIC}")
SUBTITLE    = getattr(M, "SUBTITLE", "课件逐页精讲")
INSTRUCTOR  = getattr(M, "INSTRUCTOR", "")
SOURCES     = getattr(M, "SOURCES", "")
SLIDE_COUNT = getattr(M, "SLIDE_COUNT", 0)
MAP_CHIPS   = getattr(M, "MAP_CHIPS", [])
SECTIONS    = getattr(M, "SECTIONS", [])
TLDR        = getattr(M, "TLDR", [])
C           = getattr(M, "C", {})
FORMULA_ROWS = getattr(M, "FORMULA_ROWS", [])
SUMMARY_ROWS = getattr(M, "SUMMARY_ROWS", [])
PITFALLS    = getattr(M, "PITFALLS", [])
QUIZ        = getattr(M, "QUIZ", [])
EXTRA_TABLES = getattr(M, "EXTRA_TABLES", [])   # 额外总表（可选）：定性效应表、模型vs数据表…
NOTATION     = getattr(M, "NOTATION", [])        # 符号表：[(组名, [(符号, 读法, 含义), ...]), ...]
HOWTO_READ   = getattr(M, "HOWTO_READ", [])      # 读方程的方法：[(小标题, 说明), ...]
DIVIDER_PAGES = getattr(M, "DIVIDER_PAGES", set())
# 考点标注：{页码: [ {"k": "final|mid|must", "t": "一句话考点", "ref": "Q2(g)"}, ... ]}
# final = 期末练习 Key Concepts（老师亲手划的）／mid = 期中练习 Key Concepts
# must  = 期末总复习里点名的必背项（自己横向整理，无老师名录）
EXAM = getattr(M, "EXAM", {})

# 路径全部来自 paths.py：图片在 素材/幻灯片图片/、文字稿在 素材/课件文本/、成品在 网页/
JPGDIR = P.slide_jpg_dir(TOPIC)
REF    = P.slides_txt(TOPIC)
OUT    = P.page(CURFILE)


# ---------- 公式：<span class='mj'> 转 \( ... \) ----------
XREF_RE = re.compile(r"\[\[([A-Za-z0-9_#]+)\|([^\]]+)\]\]")


def xref(s):
    """站内跳转语法：[[p29|第 29 页]] / [[xt2|均衡系统]] / [[T1#p12|Topic 1 第 12 页]]。
    指向的文件不存在时（例如还没做的 Topic 10），降级成不可点的弱化标记，避免死链。"""
    if "[[" not in s:
        return s

    def rep(m):
        tgt, txt = m.group(1), m.group(2)
        if (re.fullmatch(r"p\d+", tgt) or re.fullmatch(r"xt\d+", tgt)
                or tgt in ("notation", "formulas", "summary", "pitfalls", "quiz")):
            return f'<a class="xref" href="#{tgt}">{txt}</a>'
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
    """把 <span class='mj'>…</span> 转成 MathJax 行内定界符（单反斜杠），并解析站内跳转。
    只在还含 mj 标记时才替换，保证重复调用安全（不会把 xref 生成的 </span> 误伤）。"""
    if not isinstance(s, str):
        return s
    if "<span class='mj'>" in s:
        s = s.replace("<span class='mj'>", "\\(").replace("</span>", "\\)")
    return xref(s)


def _rt(s):
    """表格标题/副标题/脚注这类「自由文本」也走一遍公式与跳转解析。
    含 mj 标记时按 mj 处理，否则只解析 [[ ]] 跳转（避免误伤已有的 </span>）。"""
    if not isinstance(s, str):
        return s
    return mj(s) if "<span class='mj'>" in s else xref(s)


def _conv(v):
    if isinstance(v, str):
        return mj(v)
    if isinstance(v, dict):
        return {k: _conv(x) for k, x in v.items()}
    if isinstance(v, (list, tuple)):
        return type(v)(_conv(x) for x in v)
    return v


for _p in list(C):
    C[_p] = {k: _conv(v) for k, v in C[_p].items()}
FORMULA_ROWS = [(mj(a), mj(b), mj(c)) for (a, b, c) in FORMULA_ROWS]
SUMMARY_ROWS = [(mj(a), mj(b), mj(c)) for (a, b, c) in SUMMARY_ROWS]
PITFALLS     = [(mj(a), mj(b)) for (a, b) in PITFALLS]
QUIZ         = [(mj(a), mj(b)) for (a, b) in QUIZ]

_ET = []
for _t in EXTRA_TABLES:
    _t2 = dict(_t)
    if "header" in _t2: _t2["header"] = [mj(x) for x in _t2["header"]]
    if "rows"   in _t2:
        _t2["rows"] = [mj(r) if isinstance(r, str) else [mj(c) for c in r] for r in _t2["rows"]]
    if "note"   in _t2: _t2["note"] = mj(_t2["note"])
    _ET.append(_t2)
EXTRA_TABLES = _ET

NOTATION   = [(mj(g), [(mj(a), mj(b), mj(c)) for (a, b, c) in items])
              for (g, items) in NOTATION]
HOWTO_READ = [(mj(a), mj(b)) for (a, b) in HOWTO_READ]


# ---------- 组装 ----------
def toc_html():
    items = "".join(f'<a href="#p{s[1]}">{html.escape(s[0])}</a>' for s in SECTIONS)
    extra = ""
    if EXAM:     extra += '<a href="#examidx">※ 🎯 考点一览</a>'
    if NOTATION: extra += '<a href="#notation">※ 符号表 / 怎么读方程</a>'
    if FORMULA_ROWS: extra += '<a href="#formulas">※ 公式速查</a>'
    for i, t in enumerate(EXTRA_TABLES, 1):
        extra += f'<a href="#xt{i}">※ {html.escape(t.get("title", "总表"))}</a>'
    extra += '<a href="#summary">※ 概念速查</a>'
    if PITFALLS: extra += '<a href="#pitfalls">※ 易错清单</a>'
    if QUIZ:     extra += '<a href="#quiz">※ 自测（答案折叠）</a>'
    return f"<b>本讲目录</b>{items}{extra}"


def map_html():
    out = ""
    for i, (label, cur, fin) in enumerate(MAP_CHIPS):
        if i > 0:
            out += '<span class="arrow">→</span>'
        cls = "chip cur" if cur else ("chip fin" if fin else "chip")
        out += f'<div class="{cls}"><b>{html.escape(label)}</b></div>'
    return out


KIND = {"final": ("期末考点", "final"), "mid": ("期中考点", "mid"), "must": ("必背", "must")}


def _refdisp(ref):
    """q2g → Q2(g)；也允许直接写 'Topic 8' 这种自由文本"""
    m = re.fullmatch(r"([qQ])(\d)([a-h])", ref or "")
    return f"{m.group(1).upper()}{m.group(2)}({m.group(3)})" if m else (ref or "")


def exam_tags_html(pid):
    """这一页顶部的考点标签（没有就返回空串）"""
    items = EXAM.get(pid)
    if not items:
        return ""
    out = []
    for it in items:
        if isinstance(it, str):
            it = {"k": "must", "t": it}
        label, cls = KIND.get(it.get("k", "must"), ("考点", "must"))
        ref = it.get("ref")
        src = ""
        if ref:
            src = (f'<span class="etsrc">· 对应 <a href="期末练习.html#{html.escape(ref.lower())}">'
                   f'{html.escape(_refdisp(ref))}</a></span>')
        out.append(f'<span class="et {cls}">🎯 {label}</span>'
                   f'<span class="etx">{mj(it["t"])}</span>{src}')
    return '<div class="examtags">' + "".join(out) + "</div>"


def exam_index_html():
    """本讲考点索引：一次性看到「哪几页是考点」"""
    if not EXAM:
        return ""
    rows = []
    for pid in sorted(EXAM):
        for it in EXAM[pid]:
            if isinstance(it, str):
                it = {"k": "must", "t": it}
            label, cls = KIND.get(it.get("k", "must"), ("考点", "must"))
            ref = it.get("ref")
            r = (f' <a class="exq" href="期末练习.html#{html.escape(ref.lower())}">'
                 f'{html.escape(_refdisp(ref))}</a>' if ref else "")
            # 注意：<a> 不能套 <a>（浏览器会把外层提前闭合），所以行是 div、里面两个独立链接
            rows.append(f'<div class="exrow">'
                        f'<a class="exmain" href="#p{pid}">'
                        f'<span class="pn">p{pid}</span>'
                        f'<span class="et {cls}">{label}</span>'
                        f'<span class="exr-t">{mj(it["t"])}</span></a>{r}</div>')
    return ('<section class="card examidx" id="examidx">'
            '<h2>🎯 本讲考点一览（点页码直接跳）</h2>'
            '<div class="exsub">老师在练习卷首页划的 Key Concepts 落在这一讲的哪几页；'
            '「必背」是我横向整理时判断的高频项，没有老师名录背书。</div>'
            f'<div class="exlist">{"".join(rows)}</div></section>')


def tldr_html():
    if not TLDR:
        return ""
    lis = "".join(f"<li>{mj(x)}</li>" for x in TLDR)
    return f'<section class="card tldr"><h2>本讲速览（先看这 5 条）</h2><ul>{lis}</ul></section>'


def formula_html():
    if not FORMULA_ROWS:
        return ""
    rows = "".join(
        f'<tr><td class="fname">{a}</td><td>{b}</td><td class="fexp">{c}</td></tr>'
        for (a, b, c) in FORMULA_ROWS)
    return (f'<div class="sec-title" id="formulas">公式与恒等式速查</div>'
            f'<div class="sec-sub">考场上直接调用；带 α 的两条是「事实 → 模型」的桥。</div>'
            f'<div class="card"><div class="tw"><table class="table">'
            f'<tr><th style="width:23%">名称</th><th style="width:42%">公式</th><th>用途 / 备注</th></tr>'
            f'{rows}</table></div></div>')


def notation_html():
    if not NOTATION:
        return ""
    rows = []
    for group, items in NOTATION:
        rows.append(f'<tr class="grp"><td colspan="3">{group}</td></tr>')
        for sym, read, mean in items:
            rows.append(f'<tr><td class="nsym">{mj(sym)}</td>'
                        f'<td class="nread">{mj(read)}</td><td>{mj(mean)}</td></tr>')
    how = ""
    if HOWTO_READ:
        lis = "".join(f'<li><b>{a}</b>：{mj(b)}</li>' for (a, b) in HOWTO_READ)
        how = (f'<div class="howto"><b>读方程的五个动作</b>'
               f'<ol>{lis}</ol></div>')
    return (f'<div class="sec-title" id="notation">读前必读：符号怎么念、方程怎么读</div>'
            f'<div class="sec-sub">先花三分钟把这张表扫一遍。下面每一页都会用到这里的记号，'
            f'认不出符号时随时回来查。</div>'
            f'<div class="card"><div class="tw"><table class="table"><tr>'
            f'<th style="width:17%">符号</th><th style="width:15%">怎么念</th><th>含义</th></tr>'
            f'{"".join(rows)}</table></div>{how}</div>')


def extra_tables_html():
    if not EXTRA_TABLES:
        return ""
    out = []
    for i, t in enumerate(EXTRA_TABLES, 1):
        cls = "table " + t.get("table_class", "")
        head = "".join(f"<th>{c}</th>" for c in t["header"])
        body = ""
        for r in t["rows"]:
            if isinstance(r, str):                      # 字符串行 = 分组标题行
                body += f'<tr class="grp"><td colspan="{len(t["header"])}">{r}</td></tr>'
            else:
                body += ("<tr>" + "".join(
                    f'<td class="{"rowhead" if (j == 0 and t.get("first_col_bold")) else ""}">{c}</td>'
                    for j, c in enumerate(r)) + "</tr>")
        note = f'<div class="tnote">{_rt(t["note"])}</div>' if t.get("note") else ""
        out.append(
            f'<div class="sec-title" id="xt{i}">{_rt(t.get("title", "总表"))}</div>'
            f'<div class="sec-sub">{_rt(t.get("sub", ""))}</div>'
            f'<div class="card"><div class="tw"><table class="{cls}">'
            f'<tr>{head}</tr>{body}</table></div>{note}</div>')
    return "".join(out)


def summary_html():
    rows = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for (a, b, c) in SUMMARY_ROWS)
    return (f'<div class="sec-title" id="summary">本讲概念速查</div>'
            f'<div class="sec-sub">考试若涉及本讲，多为选择题 / 概念题 / 小型计算，背熟下表即可。</div>'
            f'<div class="card"><div class="tw"><table class="table">'
            f'<tr><th style="width:17%">概念</th><th>要点</th><th style="width:30%">关键词 / 公式</th></tr>'
            f'{rows}</table></div></div>')


def pitfall_html():
    if not PITFALLS:
        return ""
    rows = "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for (a, b) in PITFALLS)
    return (f'<div class="sec-title" id="pitfalls">易错清单（考前 3 分钟过一遍）</div>'
            f'<div class="sec-sub">左边是常见错误说法，右边是正解。逐条打勾，错的做记号。</div>'
            f'<div class="card"><div class="tw"><table class="table pit">'
            f'<tr><th>✗ 常见错误</th><th>✓ 正解</th></tr>{rows}</table></div></div>')


def quiz_html():
    if not QUIZ:
        return ""
    lis = "".join(
        f'<li>{q}<details><summary>▸ 看答案</summary><div class="ans">{a}</div></details></li>'
        for (q, a) in QUIZ)
    return (f'<div class="sec-title" id="quiz">自测（答案默认折叠）</div>'
            f'<div class="sec-sub">先自己在纸上写完，再点开对答案。做错的那题回到对应课件页重看。</div>'
            f'<div class="card quiz"><ol>{lis}</ol></div>')


_TAG = re.compile(r"(<[^<>]+>)")
_ASCII = re.compile(r"([\x20-\x7e]+)")


def _wrap_ascii(seg):
    """在一段文字中，把「像公式」的 ASCII 片段自动包进 \\( \\)。
    判据：含 ^ _ \\ { } 之一，且含字母。这样 'M_t（货币需求）' 里的 M_t 会变成公式，
    而 'AS 右移'、'45° 线'、'0/1' 仍是普通文字。"""
    out = []
    for part in _ASCII.split(seg):
        if not part:
            continue
        if "\\(" not in part and re.search(r"[\^_\\{}]", part) and re.search(r"[A-Za-z]", part):
            out.append(f"\\({part.strip()}\\)")
        else:
            out.append(part)
    return "".join(out)


def _fx(s):
    """图上的坐标轴 / 曲线标签：
    · 纯 ASCII 标签 → 整段当公式（'r_t\\times Y_t'）；
    · 含中文的标签 → 只把其中像公式的片段当公式，中文部分保持文字
      （'LM(M_{0,t},P_{0,t})（黑，左上）'、'N^s(w_t,\\theta_t)（向上）'）。
    否则混排标签里的下标会原样漏出成 'M^s' 这样的源码。"""
    if not isinstance(s, str):
        return s
    if "<span class='mj'>" in s:                   # 直接调用 _fx 时还没过 _conv，先就地转换
        s = s.replace("<span class='mj'>", "\\(").replace("</span>", "\\)")
    has_math = "\\(" in s                          # 内容载入时 _conv 已把 span.mj 转成 \( \)
    if not has_math and not re.search(r"[^\x20-\x7e]", s):   # 纯 ASCII 且不含公式 ⇒ 整段当公式
        return f"\\({mj(s)}\\)"
    out = []
    for piece in _TAG.split(s):
        if not piece:
            continue
        out.append(piece if _TAG.fullmatch(piece) else _wrap_ascii(piece))
    return mj("".join(out))


def slide_html(pid):
    jpg = os.path.join(JPGDIR, f"p{pid:02d}.jpg")
    if os.path.exists(jpg):
        b64 = base64.b64encode(open(jpg, "rb").read()).decode("ascii")
        # 显式写出宽高，避免图片解码前布局高度为 0 导致锚点跳错位置
        with Image.open(jpg) as im:
            w, h = im.size
        img = (f'<img class="slide-img" alt="slide {pid}" width="{w}" height="{h}" '
               f'src="data:image/jpeg;base64,{b64}"/>'
               f'<div class="zoom-hint">点图放大 · Esc 关闭</div>')
    else:
        img = '<div class="noimg">（本页无对应图片：请先运行 make_slides.py 生成 JPG）</div>'
    v = verbatim.get(pid, "")
    vblock = ""
    if v:
        vblock = (f'<details class="orig"><summary>📄 本页逐字原文（PDF 抽取，公式以讲解 LaTeX 为准）</summary>'
                  f'<pre>{html.escape(v)}</pre></details>')
    c = C.get(pid, {})
    parts = []
    if c.get("kp"):   parts.append(f'<div class="kp"><b>核心：</b>{c["kp"]}</div>')
    if c.get("plain"):parts.append(f'<div class="plain"><b>💬 白话：</b>{mj(c["plain"])}</div>')
    if c.get("note"): parts.append(f'<div class="explain"><b>讲解：</b>{c["note"]}</div>')
    if c.get("fig"):
        its = []
        for f in c["fig"]:
            rows = []
            if f.get("axes"):
                inner = "".join(f'<div class="figline"><b>{mj(a)}</b>：{_fx(b)} —— {mj(d)}</div>'
                                for (a, b, d) in f["axes"])
                rows.append(f'<div class="figrow"><span class="figtag">轴</span><div>{inner}</div></div>')
            if f.get("marks"):
                inner = "".join(f'<div class="figline"><b>{_fx(a)}</b> —— {mj(b)}</div>'
                                for (a, b) in f["marks"])
                rows.append(f'<div class="figrow"><span class="figtag">线上</span><div>{inner}</div></div>')
            read = f'<div class="figread"><b>怎么读：</b>{mj(f["read"])}</div>' if f.get("read") else ""
            exam = f'<div class="figexam"><b>考法：</b>{mj(f["exam"])}</div>' if f.get("exam") else ""
            its.append(f'<div class="figi"><div class="nm">{mj(f["name"])}</div>'
                       f'{"".join(rows)}{read}{exam}</div>')
        parts.append(f'<div class="fig"><b>📊 这张图怎么看</b>{"".join(its)}</div>')
    if c.get("lr"):
        blocks = []
        for it in c["lr"]:
            rel = it.get("rel", "＝")
            why_t = it.get("why_t", "为什么两边相等")
            blocks.append(
                f'<div class="lri">'
                f'<div class="nm">{mj(it["name"])}</div>'
                f'<div class="lrow"><span class="ltag l">左</span><div class="lbody">'
                f'<div class="leq">\\({mj(it["lhs"])}\\)</div>'
                f'<div class="lmean">{mj(it["lhs_t"])}</div></div></div>'
                f'<div class="ldiv"><span>{rel}</span><hr/></div>'
                f'<div class="lrow"><span class="ltag r">右</span><div class="lbody">'
                f'<div class="leq">\\({mj(it["rhs"])}\\)</div>'
                f'<div class="lmean">{mj(it["rhs_t"])}</div></div></div>'
                f'<div class="lwhy"><b>{why_t}：</b>{mj(it["why"])}</div>'
                f'</div>')
        parts.append(f'<div class="lr"><b>⚖️ 等式两边各是什么</b>{"".join(blocks)}</div>')
    if c.get("dec"):
        def _drow(it):
            if len(it) == 2:
                return it[0], it[1]
            a, b, txt = it[0], it[1], it[2]
            return a, f'<span class="dm">{b}</span>{txt}'
        rows = "".join(f'<div class="drow"><span class="dsym">{mj(a)}</span>'
                       f'<span class="dtxt">{mj(b)}</span></div>'
                       for a, b in (_drow(it) for it in c["dec"]))
        parts.append(f'<div class="dec"><b>🔍 逐符号拆解</b>{rows}</div>')
    if c.get("tip"):  parts.append(f'<div class="tip"><b>直觉：</b>{c["tip"]}</div>')
    if c.get("warn"): parts.append(f'<div class="warn"><b>易错 / 考点：</b>{c["warn"]}</div>')
    divider = ' data-div="1"' if pid in DIVIDER_PAGES else ''
    return (f'<div class="slide-note" id="p{pid}"{divider}>'
            f'<span class="pg">第 {pid} 页</span>{exam_tags_html(pid)}{img}'
            f'<div class="cn"><span class="lbl">🌐 中文讲解（翻译 + 解读 + 考点）</span>'
            f'{"".join(parts)}</div>{vblock}</div>')


# ---------- 解析逐字原文 ----------
verbatim = {}
if os.path.exists(REF):
    text = open(REF, encoding="utf-8").read()
    blocks = re.split(r"===== SLIDE PAGE (\d+) =====", text)
    for i in range(1, len(blocks), 2):
        verbatim[int(blocks[i])] = blocks[i + 1].strip()
else:
    print("警告：未找到原文文件", REF, "—— 将只渲染讲解、不附逐字原文。")

slides = "\n".join(slide_html(p) for p in range(1, SLIDE_COUNT + 1))

CSS = """
:root{
 --bg:#f8fafc; --card:#fff; --card2:#f1f5f9; --card3:#e8eef7;
 --ink:#0f172a; --ink2:#334155; --muted:#64748b; --line:#dbe3ee;
 --accent:#2563eb; --accent-soft:#eff6ff; --accent-ink:#1d4ed8; --accent2:#6d28d9;
 --green:#047857; --green-soft:#ecfdf5; --green-ink:#047857;
 --orange:#b45309; --orange-soft:#fffbeb; --orange-ink:#92400e;
 --red:#b91c1c; --red-soft:#fef2f2; --purple:#6d28d9; --purple-soft:#f5f3ff;
 --key-bg:#fef3c7; --key-ink:#78350f; --formula-bg:#f1f5f9; --formula-ink:#0f172a;
 --th-bg:#eef2f9; --th-ink:#1e40af; --plain-bg:#eef6ff;
}
[data-theme="dark"]{
 --bg:#0f172a; --card:#1b2437; --card2:#243146; --card3:#2d3b53;
 --ink:#f8fafc; --ink2:#d4dded; --muted:#94a3b8; --line:#3b4a63;
 --accent:#7db4ff; --accent-soft:#152f52; --accent-ink:#8cc0ff; --accent2:#b9a2ff;
 --green:#4ade80; --green-soft:#08301f; --green-ink:#4ade80;
 --orange:#fbbf24; --orange-soft:#3a2708; --orange-ink:#fcd34d;
 --red:#fb8a8a; --red-soft:#3d1414; --purple:#b9a2ff; --purple-soft:#251a45;
 --key-bg:#3a2c08; --key-ink:#fde68a; --formula-bg:#0b2038; --formula-ink:#c7e0ff;
 --th-bg:#22304a; --th-ink:#9ec9ff; --plain-bg:#132742;
}
*{box-sizing:border-box;}
body{margin:0;background:var(--bg);color:var(--ink);font-family:"Segoe UI","Microsoft YaHei",-apple-system,sans-serif;line-height:1.85;font-size:16px;}
.wrap{max-width:1000px;margin:0 auto;padding:32px 24px 104px;}
header.hero{background:linear-gradient(135deg,#1e3a8a,#2563eb);color:#fff;border-radius:16px;padding:30px 36px;margin-bottom:22px;}
.home{display:inline-block;background:rgba(255,255,255,.2);color:#fff;border-radius:999px;
 padding:2px 12px;font-size:12.5px;font-weight:700;text-decoration:none;margin-bottom:10px;}
.home:hover{background:rgba(255,255,255,.34);text-decoration:none;color:#fff;}
header.hero h1{margin:0 0 8px;font-size:25px;line-height:1.4;}
header.hero p{margin:6px 0 0;opacity:.92;font-size:14.5px;}
.hero .meta{display:flex;flex-wrap:wrap;gap:10px;margin-top:14px;}
.hero .meta span{background:rgba(255,255,255,.16);border-radius:999px;padding:3px 14px;font-size:13px;}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:22px 26px;margin:18px 0;box-shadow:0 1px 3px rgba(15,23,42,.05);}
.card h2,.card h3{margin-top:0;}
.tldr h2{font-size:17px;color:var(--accent-ink);margin-bottom:4px;}
.tldr ul{margin:4px 0 0;padding-left:20px;}
.tldr li{margin:7px 0;font-size:14.5px;}
.kp{background:var(--accent-soft);border-radius:10px;padding:10px 16px;margin:12px 0;font-size:14.5px;}
.kp b{color:var(--accent);}
.explain{background:var(--card2);border-radius:10px;padding:10px 16px;margin:10px 0;font-size:15px;}
.tip{background:var(--orange-soft);border-radius:10px;padding:10px 16px;margin-top:10px;font-size:14px;}
.tip b{color:var(--orange);}
.warn{background:var(--red-soft);border-radius:10px;padding:10px 16px;margin-top:10px;font-size:14px;}
.warn b{color:var(--red);}
/* ---- 考点标注 ---- */
.examtags{display:flex;flex-wrap:wrap;align-items:center;gap:6px;margin:0 0 10px;padding:7px 12px;
 background:var(--red-soft);border-radius:9px;border:1px dashed var(--red);}
.et{font-size:11.8px;font-weight:800;padding:1px 9px;border-radius:999px;white-space:nowrap;
 background:var(--red);color:#fff;letter-spacing:.3px;}
.et.mid{background:var(--orange);color:#fff;}
.et.must{background:var(--purple);color:#fff;}
.etx{font-size:13.6px;color:var(--ink);font-weight:600;}
.etsrc{font-size:12.2px;color:var(--muted);}
.etsrc a{color:var(--accent-ink);text-decoration:none;border-bottom:1px dashed var(--accent);}
.examidx h2{font-size:17px;color:var(--red);}
.exsub{font-size:13px;color:var(--muted);margin:2px 0 12px;}
.exlist{display:flex;flex-direction:column;gap:6px;}
.exrow{display:flex;align-items:center;gap:9px;padding:6px 10px;border-radius:8px;
 color:var(--ink);background:var(--card2);border:1px solid transparent;font-size:14px;}
.exrow:hover{border-color:var(--red);background:var(--red-soft);}
.exmain{display:flex;align-items:center;gap:9px;flex:1;text-decoration:none;color:inherit;}
.exrow .pn{font-weight:800;color:var(--accent-ink);font-size:13px;min-width:34px;}
.exr-t{flex:1;color:var(--ink2);font-size:13.8px;}
.exq{font-size:12px;color:#fff;background:var(--accent);border-radius:999px;padding:0 9px;text-decoration:none;}
.sec-title{font-size:22px;margin:38px 0 6px;padding-left:12px;border-left:6px solid var(--accent);}
.sec-sub{color:var(--muted);font-size:14px;margin-bottom:14px;}
.slide-note{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px 20px;margin:16px 0;box-shadow:0 1px 3px rgba(15,23,42,.04);}
.slide-note .pg{display:inline-block;font-weight:800;font-size:13px;color:#fff;background:var(--accent);border-radius:999px;padding:2px 12px;margin-bottom:8px;}
.slide-note .cn{background:var(--green-soft);border-radius:10px;padding:12px 16px;margin-top:10px;font-size:15px;}
.slide-note .cn .lbl{font-weight:700;color:var(--green);display:block;margin-bottom:6px;font-size:12.5px;}
.slide-img{max-width:100%;height:auto;display:block;margin:6px auto;border:1px solid var(--line);border-radius:10px;background:#fff;box-shadow:0 1px 4px rgba(15,23,42,.08);cursor:zoom-in;}
.zoom-hint{text-align:center;font-size:12px;color:var(--muted);margin:2px 0 0;}
#lb{position:fixed;inset:0;background:rgba(6,10,18,.94);display:none;z-index:9999;overflow:auto;padding:18px;}
#lb.on{display:block;}
#lb img{display:block;margin:0 auto;border-radius:8px;background:#fff;box-shadow:0 10px 50px rgba(0,0,0,.55);}
#lb .lh{position:fixed;left:0;right:0;bottom:0;padding:16px 0 10px;text-align:center;color:#c9d4e3;font-size:12.5px;pointer-events:none;background:linear-gradient(180deg,rgba(6,10,18,0),rgba(6,10,18,.92));}
.noimg{max-width:100%;text-align:center;color:var(--muted);background:var(--card2);border:1px dashed var(--line);border-radius:10px;padding:24px;margin:6px auto;}
.orig{margin-top:10px;font-size:13.5px;}
.orig summary{cursor:pointer;color:var(--purple);font-weight:700;}
.orig pre{white-space:pre-wrap;background:var(--card2);border-radius:8px;padding:10px 12px;margin:8px 0 0;font-family:inherit;font-size:13px;color:var(--ink2);}
.map{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px 22px;margin:18px 0;box-shadow:0 1px 3px rgba(15,23,42,.05);}
.map h3{margin:0 0 12px;font-size:15px;color:var(--ink2);}
.track{display:flex;flex-wrap:wrap;gap:8px;align-items:center;}
.chip{flex:1 1 150px;text-align:center;background:var(--card2);border:1px solid var(--line);border-radius:10px;padding:10px 6px;font-size:13px;color:var(--ink2);}
.chip b{display:block;color:var(--accent-ink);font-size:13px;line-height:1.5;}
.chip.cur{border-color:var(--accent);background:var(--accent-soft);box-shadow:0 0 0 2px var(--accent-soft);}
.chip.fin{border-color:#c7d2fe;background:var(--purple-soft);}
.chip.fin b{color:var(--purple);}
.arrow{color:var(--muted);font-size:15px;font-weight:700;}
.tw{overflow-x:auto;-webkit-overflow-scrolling:touch;}
.tw table{min-width:600px;}
.table{width:100%;border-collapse:collapse;margin:12px 0;font-size:14px;}
.table th{background:var(--th-bg);color:var(--th-ink);padding:8px 10px;text-align:left;border:1px solid var(--line);}
.table td{padding:8px 10px;border:1px solid var(--line);vertical-align:top;}
.table td.fname{font-weight:700;color:var(--accent-ink);}
.table td.fexp{color:var(--muted);font-size:13px;}
.table.pit td:first-child{color:var(--red);font-weight:600;width:44%;}
.table td.rowhead{font-weight:700;color:var(--accent-ink);background:var(--card2);white-space:nowrap;}
.table.ctr td,.table.ctr th{text-align:center;}
.table.ctr td.rowhead{text-align:left;}
.tnote{color:var(--muted);font-size:13px;margin-top:6px;line-height:1.7;}
/* 白话 / 符号拆解 / 符号表 */
.plain{background:var(--plain-bg);border-left:4px solid var(--accent);border-radius:0 10px 10px 0;padding:10px 16px;margin:10px 0;font-size:15px;}
.plain b{color:var(--accent-ink);}
.dec{background:var(--card3);border-radius:10px;padding:12px 16px;margin-top:10px;font-size:14px;}
.dec>b{display:block;color:var(--accent2);font-size:12.5px;margin-bottom:4px;letter-spacing:.5px;}
.drow{display:grid;grid-template-columns:210px 1fr;gap:12px;padding:6px 0;border-top:1px dashed var(--line);align-items:baseline;}
.drow:first-of-type{border-top:none;}
.dsym{font-weight:700;color:var(--accent-ink);}
.dtxt{color:var(--ink2);line-height:1.75;}
.dm{color:var(--muted);font-size:13px;margin-right:6px;}
@media (max-width:720px){.drow{grid-template-columns:1fr;gap:0;}}
/* ---- 图片解读 ---- */
.fig{background:var(--orange-soft);border:1px solid var(--line);border-radius:10px;padding:12px 16px;margin-top:10px;font-size:14px;}
.fig>b{display:block;color:var(--orange-ink);font-size:12.5px;margin-bottom:6px;letter-spacing:.5px;}
.figi{padding:9px 0 3px;border-top:1px dashed var(--line);}
.figi:first-of-type{border-top:none;padding-top:2px;}
.figi .nm{font-weight:800;font-size:13.5px;color:var(--orange-ink);margin-bottom:6px;}
.figrow{display:grid;grid-template-columns:44px minmax(0,1fr);gap:10px;margin:4px 0;align-items:start;}
.figtag{font-size:11.5px;font-weight:800;text-align:center;line-height:1.7;border-radius:6px;
  background:var(--card);color:var(--orange-ink);border:1.5px solid var(--orange);}
.figline{line-height:1.9;color:var(--ink2);}
.figline b{color:var(--ink);}
.figread{margin-top:8px;background:var(--card);border-radius:8px;padding:8px 12px;
  border-left:3px solid var(--accent);font-size:13.8px;line-height:1.8;color:var(--ink2);}
.figread b{color:var(--accent-ink);}
.figexam{margin-top:6px;background:var(--card);border-radius:8px;padding:8px 12px;
  border-left:3px solid var(--red);font-size:13.8px;line-height:1.8;color:var(--ink2);}
.figexam b{color:var(--red);}
/* ---- 等式两边 ---- */
.lr{background:var(--card3);border-radius:10px;padding:12px 16px;margin-top:10px;font-size:14px;}
.lr>b{display:block;color:var(--accent2);font-size:12.5px;margin-bottom:6px;letter-spacing:.5px;}
.lri{padding:10px 0 4px;border-top:1px dashed var(--line);}
.lri:first-of-type{border-top:none;padding-top:2px;}
.lri .nm{font-weight:800;font-size:13.5px;color:var(--accent-ink);margin-bottom:6px;}
.lrow{display:grid;grid-template-columns:26px minmax(0,1fr);gap:10px;align-items:start;margin:5px 0;}
.ltag{font-size:12px;font-weight:800;border-radius:6px;text-align:center;line-height:1.65;}
.ltag.l{background:var(--accent-soft);color:var(--accent-ink);border:1.5px solid var(--accent);}
.ltag.r{background:var(--purple-soft);color:var(--purple);border:1.5px solid var(--purple);}
.lbody{min-width:0;}
.leq{font-size:15.5px;line-height:1.7;overflow-x:auto;overflow-y:hidden;padding:1px 0 3px;}
.lmean{font-size:13.5px;color:var(--ink2);line-height:1.75;}
.ldiv{display:grid;grid-template-columns:26px 1fr;gap:10px;margin:1px 0;align-items:center;}
.ldiv>span{text-align:center;font-weight:900;color:var(--accent2);font-size:17px;line-height:1;}
.ldiv>hr{border:0;border-top:1px dotted var(--line);margin:0;}
.lwhy{margin-top:8px;font-size:13.8px;background:var(--card);border-radius:8px;padding:8px 12px;border-left:3px solid var(--green);color:var(--ink2);line-height:1.8;}
.lwhy b{color:var(--green);}
a.xref{color:var(--accent-ink);text-decoration:none;border-bottom:1.5px solid var(--accent-soft);padding-bottom:1px;white-space:nowrap;}
a.xref:hover{border-bottom-color:var(--accent);background:var(--accent-soft);border-radius:3px;}
a.xref::after{content:"↗";font-size:.8em;vertical-align:super;margin-left:2px;opacity:.75;}
.xref-off{color:var(--muted);border-bottom:1px dashed var(--muted);cursor:help;white-space:nowrap;}
.table tr.grp td{background:var(--th-bg);color:var(--th-ink);font-weight:800;font-size:13.5px;letter-spacing:.5px;}
.table td.nsym{font-weight:700;color:var(--accent-ink);white-space:nowrap;}
.table td.nread{color:var(--muted);font-size:13px;}
.howto{margin-top:16px;background:var(--card2);border-radius:10px;padding:12px 18px;font-size:14.5px;}
.howto>b{color:var(--accent);display:block;margin-bottom:6px;}
.howto ol{margin:4px 0 0;padding-left:0;list-style:none;}
.howto li{margin:7px 0;padding-left:2px;}

.table.pit td:last-child{color:var(--green-ink);}
.quiz ol{padding-left:24px;margin:6px 0;}
.quiz li{margin:14px 0;font-size:14.8px;}
.quiz details{margin-top:6px;}
.quiz summary{cursor:pointer;color:var(--accent);font-weight:700;font-size:13.5px;display:inline-block;}
.quiz .ans{background:var(--card2);border-left:3px solid var(--green);border-radius:8px;padding:8px 14px;margin-top:6px;font-size:14px;}
.theme-toggle{position:fixed;top:16px;right:20px;z-index:999;display:flex;gap:4px;background:var(--card)!important;border:1px solid var(--line)!important;border-radius:999px;padding:4px;box-shadow:0 2px 8px rgba(15,23,42,.15);}
.theme-toggle button{border:none;background:transparent!important;color:var(--ink2)!important;font-size:13px;font-weight:600;padding:5px 14px;border-radius:999px;cursor:pointer;font-family:inherit;}
.theme-toggle button:hover{background:var(--card2)!important;}
.theme-toggle button.active{background:var(--accent)!important;color:#fff!important;}
#toc{position:fixed;top:70px;right:20px;z-index:998;width:240px;max-height:82vh;overflow:auto;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:10px 14px;font-size:13px;box-shadow:0 2px 8px rgba(15,23,42,.1);}
#toc b{display:block;margin-bottom:6px;color:var(--accent);}
#toc a{display:block;color:var(--ink2);text-decoration:none;padding:3px 0;border-bottom:1px dashed var(--line);}
#toc a:hover{color:var(--accent);}
#toc{display:none;}
@media (min-width:1520px){#toc{display:block;}}
@media print{#toc,.theme-toggle{display:none!important;} details{open:true;}}
footer{margin-top:48px;color:var(--muted);font-size:13px;text-align:center;}
.mj{font-family:"Cambria Math","Times New Roman",serif;color:var(--accent-ink);font-style:italic;}
"""

# 共用外壳（常驻导航 / 进度条 / 页码跳转）
CSS += U.CSS
UI_HTML = U.html(CURFILE, ORDER, paged=True, toc=True)
UI_JS = U.JS(paged=True)
NEXTNAV = U.bottom(CURFILE, ORDER)

doc = f"""<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{html.escape(COURSE)} · {html.escape(TOPIC_TITLE)}</title>
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
  <h1>{html.escape(COURSE)} · {html.escape(TOPIC_TITLE)}</h1>
  <p>{html.escape(SUBTITLE)}</p>
  <div class="hero meta">
   <span>{html.escape(INSTRUCTOR)}</span>
   <span>{html.escape(SOURCES)}</span>
  </div>
 </header>
{tldr_html()}
{exam_index_html()}
{notation_html()}
 <section class="map">
  <h3>课程地图（本讲所属位置）</h3>
  <div class="track">{map_html()}</div>
 </section>

 <div class="sec-title">第一部分 · 课件逐页精讲（{SLIDE_COUNT} 页）</div>
 <div class="sec-sub">每页 = 课件原图 + 核心 / 讲解 / 直觉 / 易错考点，下面附可折叠的逐字原文。</div>
{slides}
{formula_html()}
{extra_tables_html()}
{summary_html()}
{pitfall_html()}
{quiz_html()}
{NEXTNAV}

 <footer>{html.escape(COURSE)} · 由课件逐页拆解生成 · 单文件离线 · MathJax 渲染</footer>
</div>
<script>
function setTheme(t){{document.documentElement.setAttribute('data-theme',t);document.getElementById('btn-light').classList.toggle('active',t==='light');document.getElementById('btn-dark').classList.toggle('active',t==='dark');try{{localStorage.setItem('af5638_theme',t);}}catch(e){{}}}}
(function(){{var t=null;try{{t=localStorage.getItem('af5638_theme');}}catch(e){{}}
 setTheme(t||document.documentElement.getAttribute('data-theme')||'light');}})();
// 展开折叠块时补排公式（若启动时被跳过，这里会补上；已排过的不会重复）
document.querySelectorAll('details').forEach(function(d){{d.addEventListener('toggle',function(){{
  if(d.open&&window.MathJax&&MathJax.typesetPromise){{MathJax.typesetPromise([d]).catch(function(){{}});}}
}});}});
// 点图放大：课件字号小，考试前需要看清每一处标注与曲线标签
(function(){{
  var lb=null;
  function close(){{if(lb){{lb.classList.remove('on');document.body.style.overflow='';}}}}
  function open(im){{
    if(!lb){{
      lb=document.createElement('div');lb.id='lb';
      lb.innerHTML='<img alt="放大"><div class="lh">点击空白处或按 Esc 关闭 · 按原始分辨率显示</div>';
      lb.addEventListener('click',function(e){{if(e.target===lb)close();}});
      document.body.appendChild(lb);
    }}
    var z=lb.querySelector('img');
    z.style.width=Math.min(im.naturalWidth||im.width,Math.max(320,window.innerWidth-36))+'px';
    z.src=im.src;
    lb.classList.add('on');document.body.style.overflow='hidden';
  }}
  document.querySelectorAll('.slide-img').forEach(function(im){{
    im.title='点击放大';
    im.addEventListener('click',function(){{open(im);}});
  }});
  document.addEventListener('keydown',function(e){{if(e.key==='Escape')close();}});
}})();
// 公式/图片渲染完成后重新对齐锚点，避免跳转位置偏移
(function(){{var jump=function(){{if(location.hash){{var el=document.querySelector(location.hash);if(el){{el.scrollIntoView();}}}}}};
window.addEventListener('load',function(){{setTimeout(jump,120);}});
if(window.MathJax&&MathJax.startup&&MathJax.startup.promise){{MathJax.startup.promise.then(function(){{setTimeout(jump,60);}});}}}})();
window.__PAGED=true;window.__PGMAX={SLIDE_COUNT};
{UI_JS}
</script>
</body></html>"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(doc)

# ---------- 自检 ----------
missing = [p for p in range(1, SLIDE_COUNT + 1) if p not in C]
noimg = [p for p in range(1, SLIDE_COUNT + 1) if not os.path.exists(os.path.join(JPGDIR, f"p{p:02d}.jpg"))]
print("wrote", OUT, "size KB:", round(len(doc.encode("utf-8")) / 1024, 1))
print("slides:", SLIDE_COUNT, "| commentary:", len(C), "| verbatim:", len(verbatim))
if missing: print("!! 缺讲解的页：", missing)
if noimg:   print("!! 缺图片的页：", noimg)
if len(verbatim) != SLIDE_COUNT:
    print(f"!! 原文页数({len(verbatim)}) 与 SLIDE_COUNT({SLIDE_COUNT}) 不一致")

_ids = set(re.findall(r'id="([^"]+)"', doc))
_dead = sorted({h for h in re.findall(r'href="#([^"]+)"', doc) if h not in _ids})
if _dead:
    print("!! 站内跳转找不到目标：", _dead)
_left = doc.count("[[") - doc.count("[[\\") - doc.count("[[\'") - doc.count('[["')
if _left > 0:
    print("!! 还有未解析的跳转标记 [[ ]]：", _left)
# 公式之外还残留 LaTeX 记号（说明某处该包 mj 或该写 HTML 上下标）
_body = doc[doc.index('<body'):]
_body = re.sub(r'\\\(.*?\\\)', '', _body, flags=re.S)
_leak = [t.strip() for t in re.findall(r'>([^<>]{2,})<', _body)
         if ('\\' in t) or re.search(r'[A-Za-z]\^|[A-Za-z]_\{', t)]
if _leak:
    print('!! 公式之外有裸露的 LaTeX：', len(_leak), '处，例：', _leak[0][:60])
_tag = doc.count("<span class='mj'>")
if _tag:
    print("!! 还有未转换的公式标记（span.mj）：", _tag)
