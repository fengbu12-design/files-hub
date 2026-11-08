# -*- coding: utf-8 -*-
"""
期末练习页用的矢量示意图（纯手写 SVG，不依赖任何图库 / CDN）

三张图：
  is_ys       IS 与 Y^s（含 ↑G_t 之后 IS 右移、r 上升、Y 不变）
  cross45     Y^d 与 45° 线（含 ↑G_t 之后支出线先上移、又被 r↑ 挤回原处）
  main4       四宫格主图（劳动市场 / 生产函数 / (r,Y) / 45°），含 ↑A_t 之后各处的移动

配色走 CSS 类（.b 蓝＝原状，.r 红＝冲击后，.g 绿＝辅助，.gd 灰虚线＝中间态），
所以浅色 / 深色主题都能自动适配，不要在 SVG 里写死颜色。

两个坑（都踩过）：
  ① SVG 的 <text> 里**不能**用 <sub>/<sup>。HTML 解析器遇到这些标签会「跳出 SVG
     命名空间」，结果所有文字失去坐标、挤到左下角。上下标一律用 <tspan dy=…>。
  ② 线的**标签别压在线上**，也别两个标签贴在一起 —— 这图是要拿去背的，
     字挤成一团等于没画。每加一个 T() 都先想「这块地方空不空」。
"""

FS = 8.6          # 上下标字号
SH = 4.4          # 上下标基线偏移


def sub(t):
    return f'<tspan dy="{SH}" font-size="{FS}">{t}</tspan>'


def sup(t):
    return f'<tspan dy="-{SH}" font-size="{FS}">{t}</tspan>'


# ---------- 小工具 ----------
def L(x1, y1, x2, y2, cls="ax", dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'class="{cls}"{d}/>')


def P(pts, cls="b", dash=None):
    d = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<polyline points="{d}" class="{cls}"{da}/>'


def T(x, y, s, cls="lab", anchor="middle"):
    return (f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}" '
            f'text-anchor="{anchor}">{s}</text>')


def DOT(x, y, cls="dot"):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.6" class="{cls}"/>'


def ARR(x1, y1, x2, y2, cls="arw"):
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'class="{cls}" marker-end="url(#ah)"/>')


DEFS = ('<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" '
        'markerWidth="5" markerHeight="5" orient="auto-start-reverse">'
        '<path d="M 0 0 L 10 5 L 0 10 z" class="ahd"/></marker></defs>')


def frame(w, h, body, cap=""):
    c = f'<div class="figcap">{cap}</div>' if cap else ""
    return (f'<div class="figwrap"><svg viewBox="0 0 {w} {h}" class="figsvg" '
            f'role="img">{DEFS}{body}</svg>{c}</div>')


# ---------- 图 1：IS 与 Y^s ----------
def is_ys(shift=False):
    """shift=False：只画两条线（对应「画出 IS 与 Y^s」这一问）
       shift=True ：再加 ↑G_t 之后右移的 IS′、两个交点、r0→r1（对应「G 上升会怎样」）"""
    X0, X1, Y0, Y1 = 95, 625, 330, 60
    b = []
    b.append(L(X0, Y0, X1, Y0, "ax"))
    b.append(L(X0, Y0, X0, Y1, "ax"))
    b.append(T(X1 + 8, Y0 + 5, "Y" + sub("t"), "axl", "start"))
    b.append(T(X0 - 10, Y1 + 4, "r" + sub("t"), "axl", "end"))

    # 竖直的 Y^s（供给面：Y 由劳动市场 ＋ 生产函数定死）
    b.append(L(430, Y0, 430, 80, "b"))
    b.append(T(430, 72, "Y" + sup("s"), "cl"))

    def isy(x):          # 原 IS
        return 108 + (195 / 450) * (x - 150)

    def isy2(x):         # ↑G_t 之后，水平右移 58 px
        return 108 + (195 / 450) * (x - 208)

    b.append(P([(150, isy(150)), (X1, isy(X1))], "b"))
    b.append(T(160, isy(160) - 9, "IS", "cl", "start"))

    ya = isy(430)
    if shift:
        b.append(P([(208, isy2(208)), (X1, isy2(X1))], "r"))
        b.append(T(218, isy2(218) - 9, "IS′", "rl", "start"))
        b.append(ARR(300, isy(300) - 26, 352, isy(300) - 26))   # 右移方向示意
        yb = isy2(430)
        b.append(L(430, ya, X0, ya, "gd", "4 4"))
        b.append(L(430, yb, X0, yb, "gd", "4 4"))
        b.append(DOT(430, ya))
        b.append(DOT(430, yb, "dot2"))
        b.append(T(X0 - 12, ya + 4, "r" + sub("0"), "axl", "end"))
        b.append(T(X0 - 12, yb + 4, "r" + sub("1"), "axl", "end"))
    else:
        b.append(L(430, ya, X0, ya, "gd", "4 4"))
        b.append(DOT(430, ya))
        b.append(T(X0 - 12, ya + 4, "r" + sup("*"), "axl", "end"))

    b.append(T(430, Y0 + 22, "Ȳ" + sub("t"), "axl"))
    b.append(T(X0 - 12, Y0 + 4, "0", "axl", "end"))
    cap = ("蓝线＝原均衡，红线＝↑G<sub>t</sub> 之后（IS 右移）。"
           "Y<sup>s</sup> 竖着不动 ⇒ 交点只往上走：r 上升、Y 不变 —— 完全挤出。") if shift else \
          ("Y<sup>s</sup> 竖在 <i>Ȳ</i> 上（与 r 无关）；IS 下斜（r↓ ⇒ I↑ ⇒ 出清所需 Y↑）。"
           "交点给出 <i>r</i>*，横坐标永远是 <i>Ȳ</i>。")
    return frame(680, 380, "".join(b), cap)


# ---------- 图 2：Y^d 与 45° 线 ----------
def cross45(shift=False):
    """shift=False：45° 线 ＋ 一条支出线（对应「画出支出线与 45° 线」这一问）
       shift=True ：再加「假设 r 不变」的灰虚线与两个箭头（对应「G 上升会怎样」）"""
    X0, Y0 = 100, 330          # 原点
    XR = 400                   # 横轴右端 / 45° 线终点
    EX, EY = 300, 130          # 均衡点（Ȳ_t, Ȳ_t），落在 45° 线上
    b = []
    b.append(L(X0, Y0, XR + 30, Y0, "ax"))
    b.append(L(X0, Y0, X0, 40, "ax"))
    b.append(T(XR + 36, Y0 + 5, "Y" + sub("t"), "axl", "start"))
    b.append(T(X0 - 12, 30, "Y" + sup("d"), "axl", "end"))
    b.append(T(X0 - 12, Y0 + 4, "0", "axl", "end"))

    # 45° 线：Y^d = Y
    b.append(P([(X0, Y0), (XR, 30)], "g"))
    # 标签放在左下空白处，别压到 x = Ȳ 那条竖直虚线
    b.append(T(X0 + 148, Y0 - 38, "45°（Y" + sup("d") + " = Y）", "gl", "end"))

    # 支出线：过 (EX, EY)，斜率 0.58（＜1）；up 为「假设 r 不变」时的上移量
    def exp(x, up=0.0):
        return EY + 0.58 * (EX - x) - up

    b.append(P([(X0, exp(X0)), (XR, exp(XR))], "b"))
    if shift:
        b.append(P([(X0, exp(X0, 20)), (XR, exp(XR, 20))], "gd", "6 5"))
        b.append(T(X0 + 6, exp(X0) + 14, "支出线 Y" + sup("d") + "（原状 ＝ 最终）", "cl", "start"))
        # ① 上移、② 被挤回来：两个小箭头，解释写在右下空白处
        b.append(ARR(195, exp(195) + 2, 195, exp(195, 20) - 2))
        b.append(T(195, exp(195, 20) - 8, "①", "rl"))
        b.append(ARR(250, exp(250, 20) - 2, 250, exp(250) + 2))
        b.append(T(250, exp(250) - 8, "②", "gl"))
        b.append(T(318, 204, "① 只有 ΔG ⇒ 上移 (1−MPC)·ΔG", "lab", "start"))
        b.append(T(318, 222, "② r 上升 ⇒ I 被挤出同样多 ⇒ 退回原线", "lab", "start"))
    else:
        b.append(T(X0 + 6, exp(X0) + 14, "支出线 Y" + sup("d") + "（斜率 ＝ MPC ＜ 1）", "cl", "start"))
        b.append(T(X0 + 210, 262, "斜率 ＜ 1 ⇒ 比 45° 线平", "lab", "start"))

    # 均衡点与两条虚线
    b.append(L(EX, EY, EX, Y0, "gd", "4 4"))
    b.append(L(EX, EY, X0, EY, "gd", "4 4"))
    b.append(DOT(EX, EY))
    b.append(T(EX, Y0 + 22, "Ȳ" + sub("t"), "axl"))
    b.append(T(X0 - 12, EY + 4, "Ȳ" + sub("t"), "axl", "end"))
    if shift:
        b.append(T(EX + 8, EY + 26, "交点 (Ȳ" + sub("t") + ", Ȳ" + sub("t") + ") 不动", "cl", "start"))
        cap = ("灰虚线只是「假设 r 不变」的假设线，不是均衡：支出线先上移 (1−MPC)·ΔG，"
               "再被 r 上升挤掉同样多的 I，最终退回原处 ⇒ 交点仍是 (Ȳ,Ȳ)。")
    else:
        b.append(T(EX + 8, EY + 26, "交点必须落在 (Ȳ" + sub("t") + ", Ȳ" + sub("t") + ")", "cl", "start"))
        cap = ("支出线斜率＝MPC（0 与 1 之间），比 45° 线平：<b>交点落在 45° 线上、横坐标正好是 Ȳ</b> —— "
               "这是与上一张 (r,Y) 图自洽的唯一画法。")
    return frame(680, 380, "".join(b), cap)


# ---------- 图 3：四宫格主图 ----------
def _panel(x0, y0, w, h, xl, yl):
    b = [L(x0, y0 + h, x0 + w, y0 + h, "ax"), L(x0, y0 + h, x0, y0, "ax")]
    b.append(T(x0 + w + 8, y0 + h + 5, xl, "axl", "start"))
    b.append(T(x0 - 10, y0 - 2, yl, "axl", "end"))
    return "".join(b)


def main4():
    W, H = 680, 600
    b = []

    # ---- 面板 1：劳动市场（↑A_t ⇒ N^d 右移，N^s 不动）----
    x, y, w, h = 70, 42, 240, 205
    b.append(_panel(x, y, w, h, "N" + sub("t"), "w" + sub("t")))
    nx = lambda N: x + N * w
    wy = lambda v: y + h - v * 140
    wS = lambda N: 0.45 + 0.7 * N          # 劳动供给
    wD = lambda N: 1.45 - 0.9 * N          # 原劳动需求
    wD2 = lambda N: 1.75 - 0.9 * N         # ↑A 之后（同样多的 N 能多雇一点）

    def curve(f, n0, n1, cls, k=24):
        pts = [(nx(n0 + (n1 - n0) * i / k), wy(f(n0 + (n1 - n0) * i / k))) for i in range(k + 1)]
        return P(pts, cls)

    b.append(curve(wS, 0.22, 0.95, "g"))
    b.append(curve(wD, 0.22, 0.98, "b"))
    b.append(curve(wD2, 0.42, 0.98, "r"))
    b.append(T(nx(0.30), wy(1.30), "N" + sup("d"), "cl", "start"))
    b.append(T(nx(0.955), wy(wS(0.955)) - 8, "N" + sup("s"), "gl", "start"))
    b.append(T(nx(0.99), wy(wD2(0.99)) + 14, "N" + sup("d") + "′", "rl", "start"))

    N0, N1 = 0.625, 0.8125
    for N, cls in ((N0, "dot"), (N1, "dot2")):
        b.append(DOT(nx(N), wy(wS(N)), cls))
        b.append(L(nx(N), wy(wS(N)), nx(N), y + h, "gd", "3 3"))
        b.append(L(nx(N), wy(wS(N)), x, wy(wS(N)), "gd", "3 3"))
    b.append(T(nx(N0), y + h + 20, "N" + sub("0"), "axl"))
    b.append(T(nx(N1), y + h + 20, "N" + sub("1"), "axl"))
    b.append(T(x - 12, wy(wS(N0)) + 4, "w" + sub("0"), "axl", "end"))
    b.append(T(x - 12, wy(wS(N1)) - 6, "w" + sub("1"), "axl", "end"))
    b.append(T(x + w / 2, y - 18, "① 劳动需求右移、供给不动 ⇒ N↑ w↑", "ttl"))

    # ---- 面板 2：生产函数 ----
    x2 = 400
    b.append(_panel(x2, y, w, h, "N" + sub("t"), "Y" + sub("t")))
    nx2 = lambda N: x2 + N * w
    yy = lambda Y: y + h - Y * 150
    pr = lambda A, N: A * (N ** 0.65)
    b.append(P([(nx2(0.02 + 0.96 * i / 30), yy(pr(0.95, 0.02 + 0.96 * i / 30))) for i in range(31)], "b"))
    b.append(P([(nx2(0.02 + 0.96 * i / 30), yy(pr(1.15, 0.02 + 0.96 * i / 30))) for i in range(31)], "r"))
    b.append(T(nx2(0.70), yy(pr(1.15, 0.70)) - 12, "A′F", "rl", "start"))
    b.append(T(nx2(0.72), yy(pr(0.95, 0.72)) + 18, "A" + sub("t") + "F", "cl", "start"))
    for N, A in ((N0, 0.95), (N1, 1.15)):
        Yv = pr(A, N)
        b.append(DOT(nx2(N), yy(Yv), "dot" if A < 1 else "dot2"))
        b.append(L(nx2(N), yy(Yv), nx2(N), y + h, "gd", "3 3"))
        b.append(L(nx2(N), yy(Yv), x2, yy(Yv), "gd", "3 3"))
    b.append(T(nx2(N0), y + h + 20, "N" + sub("0"), "axl"))
    b.append(T(nx2(N1), y + h + 20, "N" + sub("1"), "axl"))
    b.append(T(x2 - 12, yy(pr(0.95, N0)) + 4, "Y" + sub("0"), "axl", "end"))
    b.append(T(x2 - 12, yy(pr(1.15, N1)) + 4, "Y" + sub("1"), "axl", "end"))
    b.append(T(x2 + w / 2, y - 18, "② 技术上升 ＋ 就业增加 ⇒ 产出大增", "ttl"))

    # ---- 面板 3：(r, Y) ----
    y3 = 340
    b.append(_panel(x, y3, w, h, "Y" + sub("t"), "r" + sub("t")))
    yx = lambda Y: x + Y * w
    ry = lambda r: y3 + h - r * 200
    b.append(L(yx(0.62), y3 + h, yx(0.62), y3 + 16, "b"))
    b.append(L(yx(0.86), y3 + h, yx(0.86), y3 + 16, "r"))
    b.append(T(yx(0.60), y3 + 12, "Y" + sup("s"), "cl", "end"))
    b.append(T(yx(0.88), y3 + 12, "Y" + sup("s") + "′", "rl", "start"))
    b.append(P([(yx(0.10), ry(0.88)), (yx(0.97), ry(0.14))], "b"))
    b.append(T(yx(0.14), ry(0.88) - 9, "IS", "cl", "start"))
    b.append(DOT(yx(0.62), ry(0.55)))
    b.append(DOT(yx(0.86), ry(0.31), "dot2"))
    b.append(L(yx(0.62), ry(0.55), x, ry(0.55), "gd", "3 3"))
    b.append(L(yx(0.86), ry(0.31), x, ry(0.31), "gd", "3 3"))
    b.append(T(x - 12, ry(0.55) + 4, "r" + sub("0"), "axl", "end"))
    b.append(T(x - 12, ry(0.31) + 4, "r" + sub("1"), "axl", "end"))
    b.append(T(yx(0.62), y3 + h + 20, "Y" + sub("0"), "axl"))
    b.append(T(yx(0.86), y3 + h + 20, "Y" + sub("1"), "axl"))
    b.append(T(x + w / 2, y3 - 18, "③ 竖线右移 ⇒ 产出升、利率降", "ttl"))

    # ---- 面板 4：45° 图 ----
    b.append(_panel(x2, y3, w, h, "Y" + sub("t"), "Y" + sup("d")))
    y4 = lambda Y: x2 + Y * w
    d4 = lambda Y: y3 + h - Y * w
    b.append(P([(y4(0.04), d4(0.04)), (y4(0.94), d4(0.94))], "g"))
    b.append(T(y4(0.50), d4(0.30), "45°", "gl", "start"))
    for Yeq, cls in ((0.62, "b"), (0.86, "r")):
        a = Yeq - 0.6 * Yeq
        b.append(P([(y4(0.04), d4(a + 0.6 * 0.04)), (y4(0.94), d4(a + 0.6 * 0.94))], cls))
    b.append(DOT(y4(0.62), d4(0.62)))
    b.append(DOT(y4(0.86), d4(0.86), "dot2"))
    b.append(T(y4(0.62), y3 + h + 20, "Y" + sub("0"), "axl"))
    b.append(T(y4(0.86), y3 + h + 20, "Y" + sub("1"), "axl"))
    b.append(T(x2 + w / 2, y3 - 18, "④ 利率下降使支出线上移，交点右移", "ttl"))

    return frame(W, H, "".join(b),
                 "蓝线＝冲击前（<i>A</i><sub>t</sub>），红线＝↑<i>A</i><sub>t</sub> 之后。"
                 "四格必须自洽：① 定 N、w → ② 定 Y → ③ 定 r → ④ 用 r 回查支出线。")


FIGURES = {
    "is_ys": lambda: is_ys(False),
    "is_ys_shift": lambda: is_ys(True),
    "cross45": lambda: cross45(False),
    "cross45_shift": lambda: cross45(True),
    "main4": main4,
}


def get(name):
    return FIGURES[name]()
