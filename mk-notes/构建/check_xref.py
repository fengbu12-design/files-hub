# -*- coding: utf-8 -*-
"""check_xref.py —— 跨讲引用的「语义核对」

check_all.py 只验「锚点存在」，这个脚本验「指过去的那一页，内容对不对得上」。

做法：对每条 [[T6#p11|文字]]，取被引那页的全部文字，与引用处的上下文
（含所在表格行的行首列、所在块的标题）做二元字组重合度比较。
重合度过低 → 列出来人工看一眼。这是启发式，宁可多报也不漏报。
"""
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


MODS = {}
for n in range(1, 11):
    try:
        MODS[n] = load(f"content_topic{n}")
    except Exception as e:
        print(f"!! 载入 content_topic{n} 失败：{e}")

RV = load("review_content")
PR = load("practice_content")


def container(mod):
    for attr in ("C", "PAGES", "SLIDES"):
        d = getattr(mod, attr, None)
        if isinstance(d, dict) and d and all(isinstance(k, int) for k in d):
            return d
    return {}


PAGES = {n: container(m) for n, m in MODS.items()}


def flatten(obj, depth=0):
    """把任意嵌套结构里的字符串都掏出来。"""
    if depth > 6:
        return ""
    if isinstance(obj, str):
        return obj
    if isinstance(obj, dict):
        return " ".join(flatten(v, depth + 1) for v in obj.values())
    if isinstance(obj, (list, tuple)):
        return " ".join(flatten(v, depth + 1) for v in obj)
    if isinstance(obj, (int, float)):
        return ""
    return ""


PAGE_TEXT = {n: {pid: flatten(c) for pid, c in d.items()} for n, d in PAGES.items()}


def clean(s):
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"\\\(.*?\\\)|\\\[.*?\\\]", "", s, flags=re.S)
    s = re.sub(r"[^\u4e00-\u9fff]", "", s)   # 只比中文：术语是中文，公式符号反而干扰
    return s


def bigrams(s):
    return {s[i:i + 2] for i in range(len(s) - 1)}


def overlap(a, b):
    A, B = bigrams(clean(a)), bigrams(clean(b))
    if not A or not B:
        return 1.0
    return len(A & B) / min(len(A), len(B))


PAT = re.compile(r"\[\[T(\d+)#p(\d+)\|([^\]]+)\]\]")


def walk(obj, path="", hint=""):
    """yield (path, 字符串, 上下文提示)。表格行会把同行的短字符串当提示传下去。"""
    if isinstance(obj, str):
        yield path, obj, hint
    elif isinstance(obj, dict):
        h = " ".join(str(v) for k, v in obj.items()
                     if k in ("t", "title", "h", "num", "q", "label", "name") and isinstance(v, str))
        for k, v in obj.items():
            yield from walk(v, f"{path}.{k}", (h + " " + hint)[:500])
    elif isinstance(obj, (list, tuple)):
        if obj and all(isinstance(x, (str, int, float)) for x in obj):
            h = " ".join(x for x in obj if isinstance(x, str))
            for i, v in enumerate(obj):
                yield from walk(v, f"{path}[{i}]", (h + " " + hint)[:500])
        else:
            for i, v in enumerate(obj):
                yield from walk(v, f"{path}[{i}]", hint)


problems = []
total = 0
seen = set()

for mod_name, mod in [("review_content", RV), ("practice_content", PR)] + \
                     [(f"T{n}", m) for n, m in MODS.items()]:
    for key, val in vars(mod).items():
        if key.startswith("_") or key in ("os", "re", "html", "importlib"):
            continue
        if not isinstance(val, (str, dict, list, tuple)):
            continue
        for path, s, hint in walk(val, key):
            for m in PAT.finditer(s):
                total += 1
                n, p, label = int(m.group(1)), int(m.group(2)), m.group(3)
                nearby = s[max(0, m.start() - 160):m.start()] + " " + s[m.end():m.end() + 160]
                ctx = nearby + " " + hint
                target = PAGE_TEXT.get(n, {}).get(p, "")
                tag = (mod_name, path, f"T{n}#p{p}", label)
                if tag in seen:
                    continue
                seen.add(tag)
                if not target:
                    problems.append((*tag, 0.0, "目标页无内容"))
                    continue
                sc = overlap(ctx, target)
                if sc < 0.10:
                    problems.append((*tag, sc, ""))

print("=" * 66)
print(f"跨讲引用（去重后）{len(seen)} 条，可疑 {len(problems)} 条")
print("=" * 66)
for mod_name, path, tgt, label, sc, why in sorted(problems, key=lambda x: x[4]):
    n = int(tgt[1:tgt.index('#')])
    p = int(tgt.split('#p')[1])
    print(f"[{mod_name}] {path}")
    print(f"    → {tgt}｜文字「{label[:40]}」｜重合 {sc:.2f} {why}")
    print(f"    被指页开头：{clean(PAGE_TEXT.get(n, {}).get(p, ''))[:80]}")
    print()
