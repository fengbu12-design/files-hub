# -*- coding: utf-8 -*-
"""paths.py —— 全项目唯一的「路径账本」。

以前每个 build_*.py 各写一遍 os.path.join(HERE, ...)，目录一动就要改八处、
还容易漏。现在所有路径只在这里定义一次，别的脚本 from paths import ... 就行。

目录约定（期末复习/）：

    index.html              入口，双击它开始（留在根目录）
    网页/                    12 个生成好的页面 + 公式引擎 _mathjax_tex_svg.js
    构建/                    所有 .py：生成器、检查器、内容源（本文件所在处）
    素材/
        幻灯片图片/TopicN_slides_jpg/   课件逐页 jpg
        课件文本/SlidesN.txt            课件文字稿（写笔记时对照用）
        试题/final_practice.pdf         老师给的期末练习
    归档/                    整理前的整包备份、旧版内容源
    使用说明.md

两条硬约束（改目录时务必同时满足）：
  1. 公式引擎是用 <script src="./_mathjax_tex_svg.js"> 外链引入的，
     所以它必须和那 12 个页面同处 网页/。
  2. 页面之间互相链接写的是裸文件名（Topic 5 笔记.html），
     所以 12 个页面必须始终在同一个目录里；只有 index.html 在上一层，
     从内容页回主页要用 HOME 这个带 ../ 的链接。
"""
import os

BUILD = os.path.dirname(os.path.abspath(__file__))          # 期末复习/构建
ROOT = os.path.dirname(BUILD)                               # 期末复习
WEB = os.path.join(ROOT, "网页")
ASSET = os.path.join(ROOT, "素材")
SLIDE_DIR = os.path.join(ASSET, "幻灯片图片")
TEXT_DIR = os.path.join(ASSET, "课件文本")
PAPER_DIR = os.path.join(ASSET, "试题")
ARCHIVE = os.path.join(ROOT, "归档")

HOME_FILE = "index.html"
# 从 网页/ 里的内容页看，主页在上一层
HOME = "../" + HOME_FILE

# 网页/ 里放哪些页面（顺序即阅读顺序，ui_shell 也照这个走）
PAGE_REVIEW = "期末总复习.html"
PAGE_PRACTICE = "期末练习.html"


def topic_page(n):
    return f"Topic {n} 笔记.html"


def page(name):
    """网页/ 下某个页面的绝对路径（读写文件用）"""
    return os.path.join(WEB, name)


def index_page():
    return os.path.join(ROOT, HOME_FILE)


def content(n):
    """第 n 讲的内容源 content_topicN.py"""
    return os.path.join(BUILD, f"content_topic{n}.py")


def slides_txt(n):
    """第 n 讲的课件文字稿"""
    return os.path.join(TEXT_DIR, f"Slides{n}.txt")


def slide_jpg_dir(n):
    """第 n 讲的逐页 jpg 目录"""
    return os.path.join(SLIDE_DIR, f"Topic{n}_slides_jpg")


def has_page(name):
    """网页/ 里这个页面是否已经生成过（跨讲链接据此决定是链还是置灰）"""
    return os.path.exists(page(name))


def main():
    """python paths.py —— 打印目录体检结果，找不到的会标 !!"""
    print("期末复习根目录:", ROOT)
    items = [
        ("入口页", index_page()),
        ("网页目录", WEB),
        ("公式引擎", page("_mathjax_tex_svg.js")),
        ("构建目录", BUILD),
        ("素材目录", ASSET),
        ("归档目录", ARCHIVE),
    ]
    for label, p in items:
        print(f"  {'OK ' if os.path.exists(p) else '!! '}{label:8s} {p}")
    print("\n页面：")
    rows = [("根目录/", HOME_FILE, index_page())]
    rows += [("网页/", topic_page(n), page(topic_page(n))) for n in range(1, 11)]
    rows += [("网页/", PAGE_REVIEW, page(PAGE_REVIEW)), ("网页/", PAGE_PRACTICE, page(PAGE_PRACTICE))]
    for where, name, p in rows:
        print(f"  {'OK ' if os.path.exists(p) else '!! '}{where:6s}{name}")
    print("\n每讲素材：")
    for n in range(1, 11):
        jp = slide_jpg_dir(n)
        cnt = len([f for f in os.listdir(jp) if f.endswith(".jpg")]) if os.path.isdir(jp) else -1
        print(f"  T{n:<2} jpg {cnt:3d} 张   {os.path.basename(slides_txt(n))} "
              f"{'OK' if os.path.exists(slides_txt(n)) else '!! 缺'}")


if __name__ == "__main__":
    main()
