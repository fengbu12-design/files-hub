# -*- coding: utf-8 -*-
"""把正文里的裸「第 N 页」「第 N–M 页」包成站内链接 [[pN|…]]。
只处理该讲真实存在的页；已链接的跳过；指向自己的跳过。"""
import re, sys, io, os
import paths as P

os.chdir(P.BUILD)

PAT = re.compile(r'第\s*(\d+)(?:\s*[–—\-]\s*(\d+))?\s*页')
CROSS = re.compile(r'Topic\s*(\d+)\s*第\s*(\d+)(?:\s*[–—\-]\s*(\d+))?\s*页')

def linkify(src, valid, cur):
    # 先把已有 [[...]] 换成占位符，避免二次包裹
    hold = []
    def stash(m):
        hold.append(m.group(0)); return f"\x00{len(hold)-1}\x00"
    s = re.sub(r'\[\[[^\]]*\]\]', stash, src)

    # 先处理「Topic N 第 M 页」这种跨讲引用，避免被当成本讲页码
    hits = []
    def crep(m):
        n, a = m.group(1), m.group(2)
        b = m.group(3)
        if P.has_page(f"Topic {n} 笔记.html"):
            hits.append(m.group(0))
            return f"[[T{n}#p{a}|{m.group(0)}]]"
        return m.group(0)
    s = CROSS.sub(crep, s)
    # 再把新生成的跨讲链接保护起来
    hold2 = []
    def stash2(m):
        hold2.append(m.group(0)); return f"\x01{len(hold2)-1}\x01"
    s = re.sub(r'\[\[T\d+#[^\]]*\]\]', stash2, s)

    def rep(m):
        a = int(m.group(1)); b = int(m.group(2)) if m.group(2) else None
        if a not in valid: return m.group(0)
        if b is not None and (b not in valid or b < a): return m.group(0)
        if a == cur: return m.group(0)          # 指向自己，别加
        hits.append(m.group(0))
        return f"[[p{a}|{m.group(0)}]]"
    s = PAT.sub(rep, s)

    def unstash2(m):
        return hold2[int(m.group(1))]
    s = re.sub(r'\x01(\d+)\x01', unstash2, s)

    def unstash(m):
        return hold[int(m.group(1))]
    s = re.sub(r'\x00(\d+)\x00', unstash, s)
    return s, hits

dry = "--write" not in sys.argv
grand = 0
for n in range(1, 11):
    p = f"content_topic{n}.py"
    src = io.open(p, encoding="utf-8").read()
    valid = set(int(x) for x in re.findall(r'\nadd\((\d+)\s*,', src))
    # 按 add 块切分，逐块知道当前页
    parts = re.split(r'(?=\nadd\(\d+\s*,)', src)
    out = []; tot = 0; sample = []
    for blk in parts:
        m = re.match(r'\nadd\((\d+)\s*,', blk)
        cur = int(m.group(1)) if m else -1
        nb, hits = linkify(blk, valid, cur)
        out.append(nb); tot += len(hits)
        if sample is None: sample = hits[:3]
        elif len(sample) < 3: sample += hits[:3-len(sample)]
    new = "".join(out)
    grand += tot
    print(f"T{n:<3d} 可加链接 {tot:4d}   例：{sample}")
    if not dry and tot:
        io.open(p, "w", encoding="utf-8").write(new)
print(f"\n合计将新增 {grand} 个站内链接" + ("（试运行，未写入）" if dry else "（已写入）"))
