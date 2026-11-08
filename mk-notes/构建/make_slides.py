# -*- coding: utf-8 -*-
"""
把课件 PDF 渲染成逐页 JPG + 抽取逐字原文（AF5638 宏观经济学专用版）

用法：
    python make_slides.py <讲次号> "<pdf 文件名或路径>" ["<pdf2>" ...]

PDF 默认在 ../../files/ 下（即 macro/files/），也接受绝对路径。
输出：
    素材/幻灯片图片/TopicN_slides_jpg/p01.jpg … （按传入顺序连续编号）
    素材/课件文本/SlidesN.txt                  （格式 ===== SLIDE PAGE N =====）
"""
import os, sys
import pymupdf
import paths as P

HERE = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = os.path.normpath(os.path.join(P.ROOT, "..", "files"))   # macro/files

DPI = int(os.environ.get("SLIDE_DPI", "130"))


def resolve(p):
    """绝对路径直接用；相对路径先在 ../files 找，再在脚本目录找。"""
    if os.path.isabs(p) and os.path.exists(p):
        return p
    for base in (FILES_DIR, HERE, os.getcwd()):
        cand = os.path.join(base, p)
        if os.path.exists(cand):
            return cand
    return p


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    num = int(sys.argv[1])
    pdfs = [resolve(p) for p in sys.argv[2:]]

    jpg_dir = P.slide_jpg_dir(num)
    os.makedirs(jpg_dir, exist_ok=True)
    os.makedirs(P.TEXT_DIR, exist_ok=True)
    out_txt = P.slides_txt(num)

    page = 0
    parts = []
    for pf in pdfs:
        if not os.path.exists(pf):
            print("MISSING:", pf)
            continue
        doc = pymupdf.open(pf)
        print(f"open {os.path.basename(pf)}  pages={doc.page_count}")
        for pi in range(doc.page_count):
            page += 1
            pg = doc.load_page(pi)
            pix = pg.get_pixmap(dpi=DPI)
            pix.save(os.path.join(jpg_dir, f"p{page:02d}.jpg"))
            parts.append(f"===== SLIDE PAGE {page} =====\n{pg.get_text('text').strip()}")
        doc.close()

    with open(out_txt, "w", encoding="utf-8") as f:
        f.write("\n\n".join(parts) + "\n")
    print(f"rendered {page} pages -> {jpg_dir}")
    print(f"verbatim -> {out_txt}")


if __name__ == "__main__":
    main()
