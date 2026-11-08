# -*- coding: utf-8 -*-
"""check_all.py —— 全套材料的交叉核对（不是构建，只检查）

跑法：python check_all.py
覆盖六类：
  1. 每页内部锚点（href="#x" 的 x 是否存在）
  2. 跨文件锚点（Topic N 笔记.html#pX 的 X 是否在该讲范围内、id 是否真的存在）
  3. 模板残留（[[ ]] / <span class='mj'> / ** / 裸露 LaTeX）
  4. 结构完整（每讲 p1..pN 齐全、每页有课件图、练习 qid 齐全）
  5. 双向引用（考点 ref → 练习 qid；练习跨讲链接 → 笔记页）
  6. 主页统计数字 vs 真实文件
"""
import os
import re
import sys
from urllib.parse import unquote

HERE = os.path.dirname(os.path.abspath(__file__))          # 构建/
ROOT = os.path.dirname(HERE)                               # 期末复习/
WEB = os.path.join(ROOT, "网页")
ASSET = os.path.join(ROOT, "素材")
SLIDES = os.path.join(ASSET, "幻灯片图片")
# 12 个页面都在 网页/，跨页链接写的是裸文件名，所以切到 网页/ 里按裸名读最省事
os.chdir(WEB)

TOPICS = {n: f"Topic {n} 笔记.html" for n in range(1, 11)}
PAGES = {f"T{n}": v for n, v in TOPICS.items()}
PAGES["复习总台"] = "../index.html"
PAGES["期末总复习"] = "期末总复习.html"
PAGES["期末练习"] = "期末练习.html"

err = []
warn = []


def read(fn):
    with open(fn, encoding="utf-8") as f:
        return f.read()


print("=" * 62)
print("① 文件是否齐全")
missing = [fn for fn in PAGES.values() if not os.path.exists(fn)]
if missing:
    err.append(f"缺文件：{missing}")
print("   应有 %d 个，实有 %d 个" % (len(PAGES), len(PAGES) - len(missing)))

# ---------- 每页 id 表 ----------
ids = {}
for label, fn in PAGES.items():
    if not os.path.exists(fn):
        continue
    ids[fn] = set(re.findall(r'id="([^"]+)"', read(fn)))
    print(f"   {label:8s} {fn:22s} id {len(ids[fn]):5d}")

print("=" * 62)
print("② 站内锚点")
for label, fn in PAGES.items():
    if fn not in ids:
        continue
    s = read(fn)
    dead = sorted({h for h in re.findall(r'href="#([^"]+)"', s) if h not in ids[fn] and h})
    if dead:
        err.append(f"{fn} 站内锚点不存在：{dead[:6]}")
        print(f"   !! {fn}: {len(dead)} 个坏锚点 {dead[:5]}")
print("   站内检查完毕")

print("=" * 62)
print("③ 跨文件锚点")
# 主页在上一层，它里面的链接带 网页/ 前缀；页面之间是裸文件名。两种都要认。
CROSS = re.compile(r'href="(?:网页/|\.\./)?(Topic%20\d+%20[^"#]*|Topic \d+ 笔记\.html)(?:#([^"]+))?"')
cross_n = 0
for fn in ids:
    s = read(fn)
    for m in CROSS.finditer(s):
        target = unquote(m.group(1))
        frag = m.group(2)
        cross_n += 1
        if target not in ids:
            err.append(f"{fn} → {target}（文件不存在）")
            continue
        if frag and frag not in ids[target]:
            err.append(f"{fn} → {target}#{frag}（锚点不存在）")
print(f"   共 {cross_n} 条跨文件链接，坏 {len([e for e in err if '跨' in e or '→' in e])} 条")

print("=" * 62)
print("④ 模板残留")
for label, fn in PAGES.items():
    if fn not in ids:
        continue
    s = read(fn)
    body = s[s.index("<body"):]
    body_nomath = re.sub(r"\\\(.*?\\\)", "", body, flags=re.S)
    body_nomath = re.sub(r"\\\[.*?\\\]", "", body_nomath, flags=re.S)
    body_nomath = re.sub(r"<script.*?</script>", "", body_nomath, flags=re.S)
    left = body_nomath.count("[[") + body.count("<span class='mj'>")
    star = len(re.findall(r"\*\*[^*\n]{2,40}\*\*", body_nomath))
    leak = [t.strip() for t in re.findall(r">([^<>]{2,})<", body_nomath)
            if re.search(r"[A-Za-z]\^|[A-Za-z]_\{", t)]
    flag = []
    if left:
        flag.append(f"[[ 或 mj 残留 {left}")
    if star:
        flag.append(f"** 残留 {star}")
    if leak:
        flag.append(f"裸露 LaTeX {len(leak)}（例 {leak[0][:30]}）")
    if flag:
        err.append(f"{fn}: " + "；".join(flag))
    print(f"   {fn:22s} {'OK' if not flag else '!! ' + '；'.join(flag)}")

print("=" * 62)
print("⑤ 结构完整性（十讲）")
for n in range(1, 11):
    fn = TOPICS[n]
    if fn not in ids:
        continue
    s = read(fn)
    pids = {i for i in ids[fn] if re.fullmatch(r"p\d+", i)}
    nums = sorted(int(i[1:]) for i in pids)
    total = len(nums)
    gap = [i for i in range(1, total + 1) if f"p{i}" not in pids]
    imgs = s.count('class="slide-img"')
    figs = s.count('class="fig"')
    bad = []
    if gap:
        bad.append(f"缺页 {gap[:5]}")
    if imgs != total:
        bad.append(f"图 {imgs} ≠ 页 {total}")
    jd = os.path.join(SLIDES, f"Topic{n}_slides_jpg")
    jpgs = len([f for f in os.listdir(jd) if f.endswith(".jpg")]) if os.path.isdir(jd) else -1
    if jpgs != total:
        bad.append(f"jpg 文件 {jpgs} ≠ 页 {total}")
    if bad:
        err.append(f"{fn}: " + "；".join(bad))
    print(f"   T{n:<2} 页 {total:3d} 图 {imgs:3d} 图注块 {figs:3d} jpg {jpgs:3d}  {'OK' if not bad else '!! ' + '；'.join(bad)}")

print("=" * 62)
print("⑥ 练习与考点的双向引用")
pf = "期末练习.html"
if pf in ids:
    s = read(pf)
    qids = sorted({i for i in ids[pf] if re.fullmatch(r"q\d+[a-z]", i)})
    print(f"   练习页 qid {len(qids)} 个：{qids[:6]}…")
    # 笔记里的 ref（形如 q2g）是否都有对应 qid
    for n in range(1, 11):
        fn = TOPICS[n]
        if fn not in ids:
            continue
        sn = read(fn)
        refs = set(re.findall(r'href="期末练习\.html#(q\d+[a-z])"', sn))
        miss = sorted(r for r in refs if r not in ids[pf])
        if miss:
            err.append(f"{fn} 指向不存在的题号：{miss}")
        print(f"   T{n:<2} 指向练习 {len(refs):2d} 条，坏 {len(miss)}")

print("=" * 62)
print("⑦ 主页统计一致性")
if "../index.html" in ids:
    s = read("../index.html")
    m = re.search(r'<b>(\d+)</b><span>讲 · (\d+) 页课件', s)
    m2 = re.search(r'<b>(\d+)</b><span>条考点标注', s)
    m3 = re.search(r'<b>(\d+)</b><span>道练习小问', s)
    real_pages = 0
    real_tags = 0
    for n in range(1, 11):
        fn = TOPICS[n]
        if fn in ids:
            real_pages += len([i for i in ids[fn] if re.fullmatch(r"p\d+", i)])
        ctn = os.path.join(HERE, f"content_topic{n}.py")
        if os.path.exists(ctn):
            real_tags += read(ctn).count('"k":')
    real_q = len([i for i in ids.get(pf, set()) if re.fullmatch(r"q\d+[a-z]", i)])
    print(f"   主页写：{m.group(1) if m else '?'} 讲 / {m.group(2) if m else '?'} 页 · "
          f"{m2.group(1) if m2 else '?'} 考点 · {m3.group(1) if m3 else '?'} 题")
    print(f"   实际是：10 讲 / {real_pages} 页 · {real_tags} 考点 · {real_q} 题")
    if m and int(m.group(2)) != real_pages:
        err.append(f"主页页数 {m.group(2)} ≠ 实际 {real_pages}")
    if m2 and int(m2.group(1)) != real_tags:
        err.append(f"主页考点数 {m2.group(1)} ≠ 实际 {real_tags}")
    if m3 and int(m3.group(1)) != real_q:
        err.append(f"主页题数 {m3.group(1)} ≠ 实际 {real_q}")

print("=" * 62)
print("结论")
if err:
    print(f"   {len(err)} 个问题：")
    for e in err:
        print("   -", e)
    sys.exit(1)
print("   全部通过")
