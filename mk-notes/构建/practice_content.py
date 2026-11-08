# -*- coding: utf-8 -*-
"""
AF5638 期末练习 · 内容文件
=========================
题目来源：老师发的 Final Practice Questions（Dynamically Updated，Last updated: Oct 27, 2026）
原文件：期末复习/final_practice.pdf（3 页）

结构：
  INTRO      首页三块（怎么用 / 范围提醒 / 答题语言）
  SECTIONS   每一节 = dict(id, num, title, sub, blocks=[...], items=[...])
  items      一道小问 = dict(tag, q, qcn, ask, steps, fig, en, cn, points, trap, refs)

题目还在更新 —— 老师加新题时，只要在对应的 SECTIONS 里再 append 一个 item，
或者新建一节，然后 `python build_practice.py` 重跑即可。旧题的进度标记不会丢
（存的是 qid，例如 q2a，不依赖顺序）。
"""

COURSE   = "AF5638 宏观经济学"
TITLE    = "期末练习精做"
SUBTITLE = "老师给的 Final Practice：16 个小问，逐题拆成「考什么 → 怎么写 → 扣分在哪」"
META = [
    "Final Practice · Last updated Oct 27, 2026",
    "覆盖 Topic 6 / 7 / 8",
    "16 小问 · 答案默认折叠",
    "先自己写，再点开",
]
SOURCE = "AF5638 期末练习精做 · 依据 final_practice.pdf（2026-10-27 版）· 单文件离线 · 答案以课件与教材为准"

# ====================================================================
INTRO = [
    ("p", "这一页把老师发的 Final Practice **逐题做穿**：每一小问都拆成四层——**题干原文 → 这题在考什么 → 分步思路 → 参考答案（中英对照）＋ 判分点**。答案默认折叠，**逼自己先写一遍再看**，否则看完就忘。"),
    ("p", "每道题右上角有「已完成」勾选，会记在浏览器里（关掉再打开还在），顶部有进度条。**目标不是把 16 题看完，是把 16 个勾打满。**"),
    ("note", "范围提醒（别误会这份练习）", "老师这份练习**只列了 Topic 6 / 7 / 8**（Key Concepts 第一节），但**期末大纲是 Topic 1–10 全考**（期末占 50%）。所以：<b>这份练习＝「重点中的重点」，不是全部范围。</b>Topic 1–5 与 9–10 的复习见 [[T1|十讲笔记]] 与 <a class='xref in' href='期末总复习.html'>期末总复习</a>。"),
    ("tip", "答题语言", "**用英文作答**（PolyU 出题、判卷都是英文）。每题的「参考答案」给的是**可直接抄进卷子的英文句子**，中文只是帮你确认自己看懂没有。**不要把中文思路翻成英文再写**——那是两倍时间。"),
    ("warn", "这份练习的三条主线", "① **Q2 考财政**：李嘉图等价 + 乘数为零 + 完全挤出；② **Q3 考生产经济的实物侧**：六个方程、一阶条件的直觉、<span class='mj'>A_{t}</span> 冲击的六个符号；③ **共同的隐藏考点**：<b>「哪个变量内生、哪个外生」</b>——每一题的第一小问几乎都在问这个。"),
]

# ====================================================================
SECTIONS = []

# ---------------- §1 考点清单 ----------------
SECTIONS.append(dict(
    id="skill", num="一", title="考点清单：老师亲手划的范围",
    sub="PDF 第 1 页的 Key Concepts 原文照抄，右边是对应到笔记的哪几页、哪一题会用到。",
    blocks=[
        ("p", "这张表是**最高优先级**：老师把「考什么」写在了纸上，等于提前给了考纲。**先把这 13 条背到能复述，再去做题。**"),
        ("table", dict(
            caption="Key Concepts → 笔记页码 → 对应题号",
            header=["老师列的考点（原文）", "具体要会什么", "笔记页码", "哪题用"],
            first_bold=True,
            cls="table",
            rows=[
                "Topic 6 – Fiscal policy（Ch. 13）",
                ["Government intertemporal budget constraint", "写出政府两期约束、消掉 <span class='mj'>B_{t}</span> 得到「支出与税收的现值相等」", "[[T6#p3|T6 p3]]、[[T6#p4|p4]]", "Q2(b)"],
                ["Ricardian equivalence", "会用一句话说清「融资方式无关」，并说出它依赖哪四个假设", "[[T6#p11|T6 p11]]、[[T6#p12|p12]]", "Q2(a)(b)"],
                ["Government spending multiplier", "知道在李嘉图等价下乘数为 <b>0</b>，并说清为什么", "[[T6#p15|T6 p15]]、[[T6#p20|p20]]", "Q2(h)"],
                ["Crowding out", "说清「完全挤出」：<span class='mj'>G</span> 上去，<span class='mj'>C</span> 与 <span class='mj'>I</span> 合起来下去同样多", "[[T6#p18|T6 p18]]、[[T8#p22|T8 p22]]", "Q2(g)(h)"],
                "Topic 7 – Equilibrium in Production Economy（Ch. 12，excluding 12.1.1）",
                ["理解家庭与企业的「目标 / 选择 / 给定」", "能分别说出两个主体的目标函数、决策变量、面对的价格", "[[T7#p3|T7 p3]]、[[T7#p6|p6]]、[[T7#p15|p15]]", "Q3(b)"],
                ["每个一阶条件的经济直觉（<b>不要求推导</b>）", "左边是什么、右边是什么、为什么相等（边际收益＝边际成本）", "[[T7#p7|T7 p7]]、[[T7#p16|p16]]、[[T7#p17|p17]]", "Q2(d)、Q3(d)"],
                ["四个函数的偏导符号 + 直觉", "<span class='mj'>C^{d}</span>、<span class='mj'>N^{s}</span>、<span class='mj'>I^{d}</span>、<span class='mj'>N^{d}</span> 各三个符号", "[[T7#p8|p8]]、[[T7#p10|p10]]、[[T7#p18|p18]]、[[T7#p20|p20]]", "Q2(c)、Q3(c)"],
                ["劳动市场 ＋ 商品市场出清 ⇒ 资金市场也出清", "说清「两个市场出清就够了」的理由（Walras 定律）", "[[T7#p21|T7 p21]]、[[T7#p22|p22]]", "Q3(b)"],
                ["分清内生与外生", "六个内生、六个外生，还要知道 <span class='mj'>Y_{t+1}</span> 是「伪外生」", "[[T7#p23|T7 p23]]、[[T7#p24|p24]]、[[T8#p4|T8 p4]]", "Q3(a)"],
                "Topic 8 – Neoclassical Model (Real Block)（Ch. 18, 19）",
                ["Ch.18：把 Topic 7 的均衡画成图", "六个方程怎么压成 IS 与 <span class='mj'>Y^{s}</span> 两条线", "[[T8#p5|T8 p5]]、[[T8#p9|p9]]、[[T8#p14|p14]]", "Q2(e)(f)、Q3(e)"],
                ["Ch.19：用图分析各种冲击", "冲击动哪条线、动多少、六个内生量怎么变", "[[T8#p18|T8 p18]]、[[T8#p19|p19]]、[[T8#p21|p21]]", "Q2(g)、Q3(f)"],
                ["IS 与 <span class='mj'>Y^{s}</span> 怎么推、均衡怎么定", "会说清「为什么 IS 下斜」「为什么 <span class='mj'>Y^{s}</span> 竖直」", "[[T8#p7|T8 p7]]–[[T8#p14|p14]]", "Q2(e)、Q3(e)"],
                ["冲击后的一般均衡效应", "六个符号 + 传导链（r → I → Y，或 Y → N → w）", "[[T8#p16|T8 p16]]、[[T8#p24|T8 p24]]", "Q2(g)、Q3(f)(g)(h)"],
            ],
            note="**「excluding 12.1.1」**是教材小节号（Ch. 12 的某小节不考），按老师标注跳过即可。<b>更值得注意的信号是「一阶条件会给出、不要求推导」——出题人想考的是</b>直觉与符号<b>，不是代数。</b>",
        )),
        ("note", "13 条里最容易被忽略的三条", "① <b>分清内生与外生</b>（Q3(a) 单独一小问，白送分）；② <b>两个市场出清 ⇒ 资金市场出清</b>（一句话的事，但很多人答不出理由）；③ <b>乘数为零</b>（不是「乘数变小」，是<b>严格为零</b>）。"),
    ],
))

# ---------------- §2 Q2 财政冲击 ----------------
SECTIONS.append(dict(
    id="q2", num="二", title="Q2 · 财政冲击（2025 Final 原题）",
    sub="八个连问，从「李嘉图等价是什么」一路问到「为什么乘数为零」。这一题基本就是 Topic 6 + Topic 8 的合并考法。",
    start=1,
    blocks=[
        ("p", "题目给的总意愿支出与出清条件如下（下面八问都在这套设定里）："),
        ("eq", [
            ("总意愿支出", "Y_{t}^{d}=C^{d}(Y_{t}-G_{t},\\ Y_{t+1}-G_{t+1},\\ r_{t})+I^{d}(r_{t},A_{t+1},K_{t})+G_{t}", "三项：家庭消费 ＋ 企业投资 ＋ 政府购买", "[[T8#p6|Topic 8 第 6 页]]"),
            ("市场出清", "Y_{t}=Y_{t}^{d}", "产出由供给定，<span class='mj'>r_{t}</span> 调到让需求恰好等于它", "[[T8#p16|Topic 8 第 16 页]]"),
        ], "**先记住一件事**：这套设定里 <span class='mj'>C^{d}</span> 的自变量是 <span class='mj'>Y-G</span>，不是 <span class='mj'>Y-T</span>。整道题（尤其 (a)(b)(c)）都从这一处长出来。"),
        ("tip", "这一题的题型", "**(a)(b)(c) 是「概念 + 读式子」；(d) 是「一阶条件的直觉」；(e)(f)(g) 是「画图 + 比较静态」；(h) 是「收口成一句结论」。** 四类题型各占 2 分左右，<b>最容易被扣分的是 (d) 与 (g)</b>——前者说不出「毛成本 / 毛回报」，后者画错线。"),
    ],
    items=[
        dict(
            tag="a",
            q="Briefly explain what Ricardian equivalence entails.",
            qcn="简要说明李嘉图等价说的是什么。",
            ask="**定义题**。三句话就够：① 融资方式无关；② 机制是家庭把政府预算约束内化了；③ 结论是实际变量不变。**不要讲历史、不要提 Ricardo 本人。**",
            steps=[
                ("先给一句话定义", "「政府的融资方式（征税 vs 借债）不影响均衡配置」——**这一句是判分的第一分**。"),
                ("再说机制", "减税必然伴随未来加税（现值相等）；**前瞻的家庭会把减税全部存起来**去付未来的税。"),
                ("最后给结论", "一生财富没变 ⇒ 消费、储蓄、利率、投资、产出**全都不变**；变的只有税收的时点与国债存量。"),
                ("（加分）点出前提", "一次性总付税、无借贷约束、家庭前瞻且在意后代。"),
            ],
            en="Ricardian equivalence is the proposition that the <b>timing of taxation is irrelevant</b> for the equilibrium allocation: for a given path of government spending, financing by debt rather than by taxes merely postpones taxes. Forward-looking households internalise the government's intertemporal budget constraint, so they understand that a tax cut today must be paid for by higher taxes in the future; they therefore save the entire tax cut. Lifetime wealth is unchanged, so consumption, saving, the real interest rate, investment and output are all unchanged — only the timing of taxes and the stock of government debt change. The result requires lump-sum taxes, no borrowing constraints, and households that are forward-looking and care about future generations.",
            cn="李嘉图等价＝「税收的**时点**不影响均衡」。政府今天减税、明天加税，与今天直接收税，对家庭一生财富**完全一样**：因为家庭前瞻，知道减税只是把税推后，于是把减税全部存起来去付未来的税。结果消费、储蓄、利率、投资、产出全不变，只有税收时点与国债存量变。前提：一次性总付税、无借贷约束、家庭在意后代。",
            points=[
                "写出「融资方式无关 / timing irrelevant」",
                "写出机制：减税＝未来加税，家庭把减税<b>全部存起来</b>",
                "写出结论：一生财富不变 ⇒ 实际变量不变",
                "（加分）列出前提：一次性总付税、无借贷约束、前瞻",
            ],
            trap="把「等价」说成「政府借钱不好」或「赤字有害」——那是规范判断，不是李嘉图等价。**等价说的是「无关」，不是说「坏」**。",
            refs=[("T6#p11", "Topic 6 第 11 页"), ("T6#p12", "第 12 页")],
        ),
        dict(
            tag="b",
            q="In the version of the model presented above, is Ricardian equivalence assumed to hold? Briefly explain.",
            qcn="在上面这个模型里，是否假设了李嘉图等价成立？简要说明。",
            ask="**读式子题**。答案藏在 <span class='mj'>C^{d}</span> 的自变量里：写的是 <span class='mj'>Y-G</span> 而不是 <span class='mj'>Y-T</span>。**这一小问是整题最送分的，也是最多人答偏的。**",
            steps=[
                ("先给结论", "**Yes**——模型<b>已经假设</b>它成立。"),
                ("找证据", "看消费函数：<span class='mj'>C^{d}(Y_{t}-G_{t},\\ Y_{t+1}-G_{t+1},\\ r_{t})</span>，<b>税 <span class='mj'>T</span> 根本没出现</b>。"),
                ("说清这是怎么来的", "把政府 IBC 代进家庭 IBC，税收的现值被换成「政府支出的现值」——<b>这就是李嘉图等价的代数形式</b>。"),
                ("给推论", "所以「用税还是用债」在式子里<b>无处出现</b>，融资方式不可能影响均衡。"),
            ],
            en="Yes. The consumption function is written as <span class='mj'>C^{d}(Y_{t}-G_{t},\\ Y_{t+1}-G_{t+1},\\ r_{t})</span>: <b>taxes do not appear at all</b> — only government spending. This form is obtained precisely by substituting the government's intertemporal budget constraint into the household's budget constraint, which is the algebraic statement of Ricardian equivalence. Hence the financing instrument (taxes versus bonds) is absent from the model by construction and cannot affect the equilibrium: only the present value of government spending matters.",
            cn="成立，而且是被**直接写进假设**的。证据：消费函数的自变量是 <span class='mj'>Y-G</span>，税 <span class='mj'>T</span> 完全不出现。这个形式正是「把政府 IBC 代入家庭 IBC」的结果——税收现值被换成政府支出，即李嘉图等价的代数表达。所以「怎么融资」在模型里根本不存在。",
            points=[
                "明确答 Yes",
                "指出消费函数的自变量写的是 <span class='mj'>Y-G</span>、不含 <span class='mj'>T</span>",
                "说明这是代入政府 IBC 的结果（不是额外假设）",
                "推论：融资方式不影响均衡，只有 <span class='mj'>G</span> 的现值重要",
            ],
            trap="不要说「假设了每年预算平衡（<span class='mj'>T=G</span>）」——**不是**。允许赤字，只是「赤字的现值＝未来税收的现值」。",
            refs=[("T6#p8", "Topic 6 第 8 页"), ("T6#p9", "第 9 页")],
        ),
        dict(
            tag="c",
            q="What is the sign of the partial derivative of the consumption function with respect to the first two arguments? Use a hypothesis we learned in this class to provide a direct answer.",
            qcn="消费函数对前两个自变量的偏导符号是什么？用课上学过的一个假说直接回答。",
            ask="**符号题 + 点名假说**。题目特地写「Use a hypothesis」，所以**不点名会扣分**——标准答案是**永久收入假说**（消费平滑）。",
            steps=[
                ("两个符号", "都**为正**：<span class='mj'>\\partial C^{d}/\\partial(Y_{t}-G_{t})>0</span>、<span class='mj'>\\partial C^{d}/\\partial(Y_{t+1}-G_{t+1})>0</span>，且都**小于 1**。"),
                ("点名假说", "**永久收入假说（permanent income hypothesis）**：消费取决于一生财富的现值，不取决于当期收入。"),
                ("解释第一个", "今天可支配收入上去 ⇒ 一生财富上去 ⇒ 今天多消费；但只多花一部分（MPC&lt;1），其余存起来摊到明天。"),
                ("解释第二个", "明天可支配收入上去 ⇒ 一生财富<b>今天</b>就变多 ⇒ <b>今天</b>就多消费。这一条最反直觉，也是「前瞻」的证据。"),
            ],
            en="Both partial derivatives are <b>positive</b>, and both are less than one: <span class='mj'>0<\\partial C^{d}/\\partial(Y_{t}-G_{t})<1</span> and <span class='mj'>0<\\partial C^{d}/\\partial(Y_{t+1}-G_{t+1})<1</span>. The direct answer comes from the <b>permanent income hypothesis</b> (equivalently, consumption smoothing): the household consumes out of the present value of its lifetime wealth, so an increase in resources in <i>either</i> period raises lifetime wealth and therefore raises consumption today. The response to future resources is smaller than the response to current resources, but it is still positive — which is exactly what makes consumption forward-looking.",
            cn="两个都为正，且都小于 1。依据：**永久收入假说**——消费取决于一生财富的现值。所以哪一期的资源增加都会提高今天的消费；对「未来收入」的反应更小，但**符号仍是正**，这正是「前瞻」的含义。",
            points=[
                "两个符号都写 +（漏一个扣一半）",
                "写出「都小于 1」（MPC 在 0 与 1 之间）",
                "<b>点名</b>永久收入假说 / 消费平滑",
                "解释：一生财富上升 ⇒ 今天多消费（对未来的收入也如此）",
            ],
            trap="只写符号不写假说 —— 题目明说「Use a hypothesis」；写「因为消费是收入的增函数」也不算答对，那是 Topic 2 的旧假设，不是这一讲的机制。",
            refs=[("T4#p18", "Topic 4 第 18 页"), ("T4#p32", "第 32 页")],
        ),
        dict(
            tag="d",
            q="The investment demand function is derived from <span class='mj'>1+r_{t}=A_{t+1}\\frac{\\partial F(K_{t+1},N_{t+1})}{\\partial K_{t+1}}+(1-\\delta)</span>. Intuitively describe what each side captures and why they are equalized at optimum.",
            qcn="投资需求来自这条一阶条件。直觉地说明等号两边各是什么、为什么在最优点相等。",
            ask="**直觉题（不要求推导）**。判分点只有两个：**左边＝借钱的毛成本、右边＝多一单位资本的毛回报**；再加上「为什么相等」＝<b>边际收益＝边际成本，否则可以调整投资增利</b>。**别忘了 (1−δ) 与「资本是提前一期决定的」。**",
            steps=[
                ("先说左边", "<b>毛成本</b>：企业今天从银行借 1 单位买资本，明年要还 <span class='mj'>1+r_{t}</span>。<b>注意是「1+r」这个总额，不是「r」。</b>"),
                ("再说右边", "<b>毛回报</b>：多持有一单位资本到明年，得到 ① 多产出的 <span class='mj'>A_{t+1}F_{K}(K_{t+1},N_{t+1})</span>；② 剩下的 <span class='mj'>(1-\\delta)</span> 单位资本（还能用/能卖）。"),
                ("为什么相等", "这是<b>边际收益＝边际成本</b>：若右边大，多投一单位能多赚 ⇒ 继续投；若右边小，少投 ⇒ 退回来。**只有相等时才不再调整。**"),
                ("（加分）点出时点", "资本是<b>今天决定、明年才产出</b>，所以回报用 <span class='mj'>t+1</span> 的边际产品——这解释了为什么右边全是 <span class='mj'>t+1</span> 的下标。"),
                ("（加分）换个说法", "移项即 <span class='mj'>r_{t}=\\mathrm{MPK}_{t+1}-\\delta</span>：<b>实际利率＝资本的净回报</b>，这就是「无套利」。"),
            ],
            en="The <b>left-hand side is the gross cost of one unit of capital</b>: the firm borrows one unit from the bank in period <span class='mj'>t</span> and repays <span class='mj'>1+r_{t}</span> in period <span class='mj'>t+1</span>. The <b>right-hand side is the gross return of one extra unit of capital</b> held into <span class='mj'>t+1</span>: it produces <span class='mj'>A_{t+1}F_{K}(K_{t+1},N_{t+1})</span> additional units of output, and it leaves <span class='mj'>(1-\\delta)</span> units of undepreciated capital. At an interior optimum the firm invests up to the point where the marginal return equals the marginal cost: if the right-hand side exceeded the left, one more unit would raise profit and investment should increase; if it fell short, investment should decrease. Equivalently, <span class='mj'>r_{t}=\\mathrm{MPK}_{t+1}-\\delta</span>: the real interest rate equals the net return on capital (no-arbitrage). Note that capital is chosen one period in advance, which is why the relevant marginal product is dated <span class='mj'>t+1</span>.",
            cn="左边＝借钱的**毛成本**：借 1 单位、明年连本带息还 <span class='mj'>1+r</span>（不是「r」）。右边＝多持有 1 单位资本的**毛回报**：多产出 <span class='mj'>\\mathrm{MPK}</span>，加上未折旧剩下的 <span class='mj'>1-\\delta</span> 单位。两者相等＝边际收益＝边际成本：右边大就多投，右边小就少投，相等时不再调整。移项得 <span class='mj'>r=\\mathrm{MPK}-\\delta</span>，即「利率＝资本净回报」（无套利）。",
            points=[
                "左边：借 1 单位、明年还 <span class='mj'>1+r</span> 的<b>毛成本</b>",
                "右边：<span class='mj'>\\mathrm{MPK}</span> ＋ <span class='mj'>(1-\\delta)</span> 的<b>残值</b>",
                "为什么相等：否则可以增减投资提高利润（边际收益＝边际成本）",
                "（加分）资本提前一期决定 ⇒ 用 <span class='mj'>t+1</span> 的边际产品",
            ],
            trap="① 把左边说成「利率 r」而不是「1+r 的毛成本」；② 漏掉 <span class='mj'>(1-\\delta)</span>——那等于假设资本一期全折旧；③ 只说「两者相等」而说不出「为什么」（不相等会怎样）。",
            refs=[("T7#p7", "Topic 7 第 7 页"), ("T7#p10", "第 10 页")],
        ),
        dict(
            tag="e",
            q="Suppose output is already determined by the supply side at a level of <span class='mj'>\\bar Y_{t}</span>. On a graph with <span class='mj'>r_{t}</span> on the vertical axis and <span class='mj'>Y_{t}</span> on the horizontal axis, draw the IS curve and the <span class='mj'>Y^{s}</span> curve that determine the equilibrium real interest rate.",
            qcn="设产出已由供给侧定为 <span class='mj'>\\bar Y</span>。在 <span class='mj'>(r,Y)</span> 平面上画出决定均衡利率的 IS 与 <span class='mj'>Y^{s}</span>。",
            ask="**画图题**。两条线 + 一个交点 + 两句理由。**图形题的分一半在图上、一半在「为什么这条线长这样」。**",
            steps=[
                ("先画 <span class='mj'>Y^{s}</span>（竖直）", "竖在 <span class='mj'>\\bar Y_{t}</span>。<b>理由</b>：产出由劳动市场 ＋ 生产函数定出，<b>与 <span class='mj'>r</span> 无关</b>，所以在 (r,Y) 平面上是一条竖线。"),
                ("再画 IS（下斜）", "<b>理由</b>：<span class='mj'>r</span> 下降 ⇒ 投资需求上升（储蓄者还会多消费）⇒ 意愿支出上升 ⇒ 出清的 <span class='mj'>Y</span> 更高。所以 r 与 Y 反向。"),
                ("标交点", "交点给出 <span class='mj'>r^{*}</span> 与 <span class='mj'>Y=\\bar Y_{t}</span>；<b>两条轴的名字、两个数都要标</b>。"),
                ("补一句「IS 是需求侧、<span class='mj'>Y^{s}</span> 是供给侧」", "IS 来自商品市场出清，<span class='mj'>Y^{s}</span> 来自劳动市场 ＋ 生产函数。<b>一句话说清两条线的出身，比画得漂亮更重要。</b>"),
            ],
            fig="is_ys",
            en="Draw <span class='mj'>Y^{s}</span> as a <b>vertical line</b> at <span class='mj'>\\bar Y_{t}</span>: output is determined on the supply side (labor market plus production function) and is independent of the interest rate. Draw <span class='mj'>IS</span> as a <b>downward-sloping</b> curve: a lower <span class='mj'>r_{t}</span> raises investment demand (and consumption, for a saver), so desired expenditure is higher and the level of output that clears the goods market is higher. The intersection of the two curves determines the equilibrium real interest rate <span class='mj'>r^{*}</span>, with <span class='mj'>Y_{t}=\\bar Y_{t}</span> unchanged.",
            cn="<span class='mj'>Y^{s}</span> 画成**竖线**（位置在 <span class='mj'>\\bar Y</span>）：产出由供给侧定，与 r 无关。IS 画成**下斜**：r 越低，投资（以及储蓄者的消费）越高，出清所需的产出越高。两线交点定出 <span class='mj'>r^{*}</span>，产出始终是 <span class='mj'>\\bar Y</span>。",
            points=[
                "<span class='mj'>Y^{s}</span> 竖直，且说明「产出与 r 无关」的理由",
                "IS 下斜，且说明「r↓ ⇒ I↑ ⇒ Y↑」的链条",
                "交点标出 <span class='mj'>r^{*}</span> 与 <span class='mj'>\\bar Y</span>，两轴有标签",
            ],
            trap="把 <span class='mj'>Y^{s}</span> 画成上斜（那是**劳动供给**，不是 <span class='mj'>Y^{s}</span>）；或把 IS 画成上斜（混淆了「沿 IS 移动」与「IS 移动」）。",
            refs=[("T8#p9", "Topic 8 第 9 页"), ("T8#p14", "第 14 页")],
        ),
        dict(
            tag="f",
            q="On another graph with <span class='mj'>Y_{t}^{d}</span> on the vertical axis and <span class='mj'>Y_{t}</span> on the horizontal axis, draw the aggregate desired expenditure line and the 45-degree line that is consistent with the equilibrium.",
            qcn="另一张图：纵轴 <span class='mj'>Y^{d}</span>、横轴 <span class='mj'>Y</span>，画出意愿支出线与 45° 线，并使其与均衡一致。",
            ask="**画图题（第二张）**。三个要点：**45° 线、支出线斜率＝MPC&lt;1、交点必须落在 <span class='mj'>(\\bar Y,\\bar Y)</span>**。",
            steps=[
                ("画 45° 线", "<span class='mj'>Y^{d}=Y</span>，斜率 1。它是「收入＝支出」这条出清条件的几何表达。"),
                ("画支出线", "<span class='mj'>Y^{d}=C^{d}(Y_{t}-G_{t},\\dots)+I^{d}+G_{t}</span>。<b>斜率</b>＝<span class='mj'>\\partial C^{d}/\\partial(Y-G)=\\mathrm{MPC}<1</span>（<span class='mj'>I^{d}</span> 与 <span class='mj'>G</span> 不随 <span class='mj'>Y</span> 变）。<b>截距</b>＝<span class='mj'>C^{d}(-G_{t},\\dots)+I^{d}(r^{*})+G_{t}</span>。"),
                ("让交点在 (Ȳ,Ȳ)", "因为 <span class='mj'>r^{*}</span> 已经把需求调到等于 <span class='mj'>\\bar Y</span>，所以<b>支出线必须正好穿过 45° 线上的那一点</b>。<b>这一点是本题的「一致性」检查。</b>"),
                ("补一句斜率的含义", "斜率小于 1 ⇒ 支出线比 45° 线平 ⇒ 乘数 <span class='mj'>1/(1-\\mathrm{MPC})>1</span> 的那套「凯恩斯交叉」逻辑在这里<b>不适用</b>，因为 r 会动。"),
            ],
            fig="cross45",
            en="The 45-degree line is <span class='mj'>Y^{d}=Y</span>. The aggregate desired expenditure line is <span class='mj'>Y^{d}=C^{d}(Y_{t}-G_{t},\\ Y_{t+1}-G_{t+1},\\ r^{*})+I^{d}(r^{*},A_{t+1},K_{t})+G_{t}</span>; its slope is the MPC, <span class='mj'>\\partial C^{d}/\\partial(Y_{t}-G_{t})\\in(0,1)</span>, because investment and government spending do not depend on <span class='mj'>Y_{t}</span>. Since <span class='mj'>r^{*}</span> already equates desired expenditure with <span class='mj'>\\bar Y_{t}</span>, the expenditure line must pass exactly through the point <span class='mj'>(\\bar Y_{t},\\bar Y_{t})</span> on the 45-degree line.",
            cn="45° 线是 <span class='mj'>Y^{d}=Y</span>。支出线的斜率是 **MPC（0 与 1 之间）**，因为 I 与 G 不随 Y 变；截距是「Y=0 时的自主支出」。因为 <span class='mj'>r^{*}</span> 已把需求调到等于 <span class='mj'>\\bar Y</span>，**支出线必须正好穿过 45° 线上的 <span class='mj'>(\\bar Y,\\bar Y)</span>**——这是与 (e) 图自洽的唯一画法。",
            points=[
                "45° 线（<span class='mj'>Y^{d}=Y</span>）",
                "支出线斜率＝MPC 且 <b>小于 1</b>，并说明理由",
                "交点标在 <span class='mj'>(\\bar Y,\\bar Y)</span>（与 (e) 一致）",
            ],
            trap="把支出线画成比 45° 线更陡（斜率 &gt; 1）——那意味着「支出对收入过度反应」，本模型里不可能；或让交点偏离 <span class='mj'>\\bar Y</span>（与 (e) 图矛盾）。",
            refs=[("T8#p7", "Topic 8 第 7 页"), ("T8#p8", "第 8 页")],
        ),
        dict(
            tag="g",
            q="Show what happens to the graph in part (e) and the graph in part (f) following an exogenous increase in G_t. Summarize the effect on equilibrium real interest rate and equilibrium output.",
            qcn="若 G_t 外生上升，(e) 与 (f) 两张图各怎么变？总结对均衡利率与均衡产出的影响。",
            ask="**两道比较静态题（必须两个图都说）**。核心：**(e) 里 IS 右移、<span class='mj'>Y^{s}</span> 不动 ⇒ Y 不变、r 上升**；**(f) 里支出线先上移、再被 r 压回去**。**「移动多少」是加分项，但要分清两个数：IS <b>水平</b>右移 <span class='mj'>\\Delta G</span>（正好等于 ΔG）；支出线<b>竖直</b>上移 <span class='mj'>(1-\\mathrm{MPC})\\Delta G</span>。二者差一个斜率，混起来就错。**",
            steps=[
                ("(e) 图：IS <b>水平右移 ΔG</b>（不是 (1−MPC)ΔG）", "给定 <span class='mj'>r</span>，<span class='mj'>G</span> 上去 <span class='mj'>\\Delta G</span>，但 <span class='mj'>C^{d}</span> 因为 <span class='mj'>Y-G</span> 下降而<b>少花</b> <span class='mj'>\\mathrm{MPC}\\cdot\\Delta G</span>，所以<b>净注入只有</b> <span class='mj'>(1-\\mathrm{MPC})\\Delta G</span>。<br>→ <b>但这是「竖直」的净注入，不是水平位移。</b>把这条净注入放进 45° 图，交点右移 <span class='mj'>(1-\\mathrm{MPC})\\Delta G\\div(1-\\mathrm{MPC})=\\Delta G</span>。<b>所以 IS 水平右移正好 ΔG。</b><br>→ 也可以直接全微分，一步得出：<span class='mj'>dY=\\mathrm{MPC}(dY-dG)+dG\\ \\Rightarrow\\ dY=dG</span>。<b>两个算法必须给同一个答案，这是检查有没有搞混的最好办法。</b>"),
                ("(e) 图：<span class='mj'>Y^{s}</span> 不动 ⇒ Y 不变", "供给侧的 <span class='mj'>A_{t},K_{t},\\theta_{t}</span> 都没变 ⇒ <span class='mj'>\\bar Y</span> 不动 ⇒ 新交点只能<b>沿竖线往上</b>：<span class='mj'>r</span> 上升，<span class='mj'>Y</span> 不变。"),
                ("(f) 图：支出线先上移", "幅度同样是 <span class='mj'>(1-\\mathrm{MPC})\\Delta G</span>。<b>如果 r 不动</b>，交点会右移到更高的 Y——<b>但 r 会动。</b>"),
                ("(f) 图：被 r 压回来", "<span class='mj'>r</span> 上升 ⇒ <span class='mj'>I</span> 下降（储蓄者的 <span class='mj'>C</span> 也降）⇒ 支出线<b>整体下移回去</b>，最终仍穿过 <span class='mj'>(\\bar Y,\\bar Y)</span>。<b>交点不动，但线的位置与构成变了。</b>"),
                ("总结成四行符号", "<span class='mj'>\\Delta r>0</span>、<span class='mj'>\\Delta Y=0</span>、<span class='mj'>\\Delta C<0</span>、<span class='mj'>\\Delta I<0</span>，且 <span class='mj'>\\Delta C+\\Delta I=-\\Delta G</span>；<span class='mj'>N,w</span> 不变（<span class='mj'>Y,A_{t},K_{t}</span> 都没变）。<br>→ <b>两个负号怎么在 C 与 I 之间分配，取决于各自对 r 的敏感度</b>——本题没有给出这个信息，所以<b>只答符号与总和就够</b>。<b>只有额外假设「C 不依赖 r」时，才能简化成 <span class='mj'>\\Delta C=-\\mathrm{MPC}\\cdot\\Delta G</span>、<span class='mj'>\\Delta I=-(1-\\mathrm{MPC})\\Delta G</span></b>。写成后者而不说明假设，是超出题意的。"),
            ],
            fig=["is_ys_shift", "cross45_shift"],
            en="<b>Panel (e):</b> the IS curve shifts <b>right</b> by <b><span class='mj'>\\Delta G</span></b> — government spending adds <span class='mj'>\\Delta G</span> to demand, but consumption falls by <span class='mj'>\\mathrm{MPC}\\cdot\\Delta G</span> because disposable income falls, leaving a net injection of only <span class='mj'>(1-\\mathrm{MPC})\\Delta G</span>; <b>this net injection is the vertical shift of the expenditure line, and dividing it by the slope <span class='mj'>1-\\mathrm{MPC}</span> gives the horizontal IS shift <span class='mj'>\\Delta G</span></b>. The <span class='mj'>Y^{s}</span> curve does <b>not</b> move, since <span class='mj'>A_{t}</span>, <span class='mj'>K_{t}</span> and <span class='mj'>\\theta_{t}</span> are unchanged. Hence the new equilibrium lies on the same vertical line: <b>the real interest rate rises and output is unchanged</b>.<br><br><b>Panel (f):</b> the expenditure line shifts <b>up</b> by <span class='mj'>(1-\\mathrm{MPC})\\Delta G</span>. On its own this would raise the 45-degree intersection, but the higher <span class='mj'>r_{t}</span> reduces investment (and consumption), shifting the line back down; the final line again passes through <span class='mj'>(\\bar Y_{t},\\bar Y_{t})</span>. <b>Summary:</b> <span class='mj'>r_{t}</span> rises, <span class='mj'>Y_{t}</span> is unchanged, <span class='mj'>C_{t}</span> and <span class='mj'>I_{t}</span> both fall, with <span class='mj'>\\Delta C+\\Delta I=-\\Delta G</span>; employment and the wage are unaffected.",
            cn="**(e) 图**：IS <b>水平右移 ΔG</b>（支出线只是竖直上移 <span class='mj'>(1-\\mathrm{MPC})\\Delta G</span>，除以斜率后正好是 ΔG），<span class='mj'>Y^{s}</span> 完全不动 ⇒ 新交点在同一竖线上：**r 上升、Y 不变**。**(f) 图**：支出线先竖直上移 <span class='mj'>(1-\\mathrm{MPC})\\Delta G</span>，若 r 不变交点会右移；但 r 上升把 I（以及 C）压下来，支出线又移回去，最终仍过 <span class='mj'>(\\bar Y,\\bar Y)</span>——**交点不动，构成变了**。总结：r↑、Y 不变、C 与 I 都下降（合起来正好等于 ΔG 的反向），N 与 w 不变。",
            points=[
                "两个图<b>都要</b>画（只答一个扣一半）",
                "IS 右移、<span class='mj'>Y^{s}</span> 不动",
                "结论：<span class='mj'>r\\uparrow</span>、<span class='mj'>Y</span> 不变",
                "（加分）IS 水平右移 <span class='mj'>\\Delta G</span>、支出线竖直上移 <span class='mj'>(1-\\mathrm{MPC})\\Delta G</span>（两个数别混）",
                "（加分）<span class='mj'>C</span> 与 <span class='mj'>I</span> 都下降、合起来等于 <span class='mj'>\\Delta G</span>",
            ],
            trap="① 在 (f) 图上直接画一个新交点就交卷（那是「r 不变」的答案，错）；② 说「Y 上升但幅度小」——在新古典模型里 Y **一点都不能变**；③ 忘了说 C 也下降（只提 I）。",
            refs=[("T8#p21", "Topic 8 第 21 页"), ("T8#p22", "第 22 页"), ("T6#p18", "Topic 6 第 18 页")],
        ),
        dict(
            tag="h",
            q="Relate your answers to part (g) to a key implication of the Neoclassical model.",
            qcn="把 (g) 的答案联系到新古典模型的一个关键含义。",
            ask="**收口题**：一句话说出「财政政策在新古典里没用」。关键词是 **zero multiplier** 与 **complete crowding out**。**这一问是 (g) 的「意义化」，不写就会少 2 分。**",
            steps=[
                ("先给那句话", "**政府支出乘数为零**：<span class='mj'>\\Delta Y/\\Delta G=0</span>。财政扩张改不了产出，只改构成。"),
                ("解释为什么", "产出由供给侧钉死（<span class='mj'>Y^{s}</span> 竖直）＋ 价格灵活 ⇒ 需求一变，<b>只推高利率</b>，不推高产量。"),
                ("把「挤出」说完整", "<span class='mj'>G</span> 增加多少，<span class='mj'>C+I</span> 就减少多少（<b>完全挤出</b>），一分不多一分不少。"),
                ("再补一层（加分）", "配合 Q2(b) 的李嘉图等价：<b>赤字本身不刺激需求</b>，因为家庭会把减税存起来。所以「减税」与「借债融资的增支」都不是刺激工具。"),
                ("对比一句（加分）", "这正是 Topic 10 存在的理由：<b>一旦价格粘住，<span class='mj'>Y^{s}</span> 不再竖直，乘数变正</b>，财政政策才「有用」。"),
            ],
            en="The key implication is that <b>the government spending multiplier is zero</b>: in the neoclassical model output is determined on the supply side (<span class='mj'>Y^{s}</span> is vertical) and prices are flexible, so an increase in government spending cannot raise output. Instead it raises the real interest rate, which crowds out consumption and investment one-for-one — <b>complete crowding out</b>: <span class='mj'>\\Delta C+\\Delta I=-\\Delta G</span>, so <span class='mj'>\\Delta Y=0</span>. Combined with Ricardian equivalence, this also implies that deficit-financed tax cuts are not expansionary. Fiscal policy only changes the <i>composition</i> of output, not its level; the multiplier becomes positive only once prices are sticky (the New Keynesian model of Topic 10).",
            cn="关键含义：**政府支出乘数为零**。产出由供给侧钉死（<span class='mj'>Y^{s}</span> 竖直）、价格灵活，所以 G 增加不能提高产出，只能推高利率，把 C 与 I 一对一挤出（**完全挤出**，<span class='mj'>\\Delta C+\\Delta I=-\\Delta G</span>）。再叠加李嘉图等价：赤字融资的减税也不刺激。财政政策只改**构成**、不改**水平**；要等价格粘住（Topic 10），乘数才为正。",
            points=[
                "说出<b>乘数为零</b>（<span class='mj'>\\Delta Y/\\Delta G=0</span>）",
                "说出<b>完全挤出</b>（<span class='mj'>\\Delta C+\\Delta I=-\\Delta G</span>）",
                "理由：<span class='mj'>Y^{s}</span> 竖直 ＋ 价格灵活 ⇒ 只有 r 变",
                "（加分）联系李嘉图等价；或对比粘性价格下乘数为正",
            ],
            trap="写「乘数较小」而不是「为零」——**新古典里是严格的零**；或只答「挤出」不说「完全」。",
            refs=[("T8#p23", "Topic 8 第 23 页"), ("T6#p20", "Topic 6 第 20 页")],
        ),
    ],
))

# ---------------- §3 Q3 新古典实际块 ----------------
SECTIONS.append(dict(
    id="q3", num="三", title="Q3 · 新古典模型实物块",
    sub="八问把 Topic 7 与 Topic 8 从头走一遍：先列方程、签符号、讲直觉，再画图、跑一个 A_t 冲击，最后跟禀赋经济对比。",
    start=9,
    blocks=[
        ("p", "两期生产经济，**没有政府**。题目给的决策规则与出清条件如下（这八问全在这套设定里）："),
        ("eq", [
            ("家庭：消费", "C_{t}=C^{d}(Y_{t},\\ Y_{t+1},\\ r_{t})", "三个自变量的符号都要会签", "[[T4#p18|Topic 4 第 18 页]]"),
            ("家庭：劳动供给", "N_{t}=N^{s}(w_{t},\\ \\theta_{t})", "<span class='mj'>\\theta_{t}</span> 是闲暇偏好的权重", "[[T7#p20|Topic 7 第 20 页]]"),
            ("企业：劳动需求", "N_{t}=N^{d}(w_{t},\\ A_{t},\\ K_{t})", "<span class='mj'>K_{t}</span> 在这里是<b>正号</b>", "[[T7#p8|Topic 7 第 8 页]]"),
            ("企业：投资需求", "I_{t}=I^{d}(r_{t},\\ A_{t+1},\\ K_{t})", "<span class='mj'>K_{t}</span> 在这里是<b>负号</b>（重置效应）", "[[T7#p10|Topic 7 第 10 页]]"),
            ("生产函数", "Y_{t}=A_{t}F(K_{t},\\ N_{t})", "两条约束之一", "[[T7#p3|Topic 7 第 3 页]]"),
            ("商品市场出清", "Y_{t}=C_{t}+I_{t}", "没有政府，所以没有 <span class='mj'>G</span>", "[[T7#p22|Topic 7 第 22 页]]"),
        ], "**六个方程、六个未知数**——这就是 (b) 要你列的东西。**注意分母里没有 <span class='mj'>G</span>**：这一题与 Q2 的设定只差一个政府。"),
        ("warn", "这一题最容易踩的两个坑", "① **<span class='mj'>K_{t}</span> 的符号在两张图里相反**（劳动需求里正、投资需求里负）——题目 (b) 之后一定会问，答反必扣；② **(f) 里 <span class='mj'>IS</span> 完全不动**——<span class='mj'>A_{t}</span> 只出现在生产函数与劳动需求里，<b>不进入消费函数与投资需求</b>。很多人顺手把 IS 也画右移，那是把 <span class='mj'>A_{t+1}</span> 当成了 <span class='mj'>A_{t}</span>。"),
    ],
    items=[
        dict(
            tag="a",
            q="Specify the endogenous variables and exogenous variables in this model.",
            qcn="指出这个模型里的内生变量与外生变量。",
            ask="**白送分题**，但要答全。**六个内生、六个外生**（含 <span class='mj'>K_{t}</span> 的「预定」身份与 <span class='mj'>Y_{t+1}</span> 的「伪外生」）。",
            steps=[
                ("内生：六个", "<span class='mj'>Y_{t},C_{t},I_{t},N_{t},w_{t},r_{t}</span>——<b>正好对应六个方程</b>，写的时候按方程顺序数一遍，不会漏。"),
                ("外生：<span class='mj'>K_{t}</span>", "<b>predetermined</b>：它是历史决定的（<span class='mj'>K_{t}=I_{t-1}+(1-\\delta)K_{t-1}</span>），本期改不了。"),
                ("外生：三个冲击", "<span class='mj'>A_{t},A_{t+1},\\theta_{t}</span>。<b>注意 <span class='mj'>A_{t+1}</span> 与 <span class='mj'>A_{t}</span> 要分开写</b>——它们进的是不同的函数。"),
                ("（加分）<span class='mj'>Y_{t+1}</span>", "它出现在消费函数里，但<b>本期没有方程能定它</b>，所以在这个「一期问题」里被当作<b>给定</b>——课件叫「伪外生 / future endogenous」。"),
                ("（加分）参数", "<span class='mj'>\\beta,\\delta</span> 与生产函数的参数——它们不是变量，是参数。"),
            ],
            en="<b>Endogenous (6):</b> <span class='mj'>Y_{t},\\ C_{t},\\ I_{t},\\ N_{t},\\ w_{t},\\ r_{t}</span> — one for each of the six equilibrium conditions.<br><b>Exogenous:</b> the predetermined capital stock <span class='mj'>K_{t}</span> (determined by past investment, so it cannot change within period <span class='mj'>t</span>); the shocks <span class='mj'>A_{t},\\ A_{t+1}</span> and <span class='mj'>\\theta_{t}</span>; and the parameters (<span class='mj'>\\beta,\\ \\delta</span> and the parameters of <span class='mj'>F</span>). Note that <span class='mj'>Y_{t+1}</span>, which appears in the consumption function, is treated as given here because no equation in this one-period problem determines it.",
            cn="内生六个：Y、C、I、N、w、r。外生：<span class='mj'>K_{t}</span>（预定，由过去投资决定）、三个冲击 <span class='mj'>A_{t},A_{t+1},\\theta_{t}</span>、以及参数。加分点：<span class='mj'>Y_{t+1}</span> 出现在消费函数里但本期没有方程定它，所以按「给定」处理（伪外生）。",
            points=[
                "六个内生变量<b>一个不漏</b>",
                "<span class='mj'>K_{t}</span> 列为外生并说明是 predetermined",
                "<span class='mj'>A_{t},A_{t+1},\\theta_{t}</span> 三个冲击都列出",
                "（加分）<span class='mj'>Y_{t+1}</span> 的处理方式",
            ],
            trap="把 <span class='mj'>K_{t}</span> 写成内生（它是本期给定的）；或只写 <span class='mj'>A_{t}</span> 忘了 <span class='mj'>A_{t+1}</span>——投资需求里用的正是 <span class='mj'>A_{t+1}</span>。",
            refs=[("T7#p23", "Topic 7 第 23 页"), ("T7#p24", "第 24 页"), ("T8#p4", "Topic 8 第 4 页")],
        ),
        dict(
            tag="b",
            q="List the set of equations characterizing the equilibrium.",
            qcn="列出刻画均衡的方程组。",
            ask="**列方程题**。六个方程要**有顺序**地列（家庭 → 企业 → 技术 → 出清），并说明「为什么两个市场出清就够了」。",
            steps=[
                ("按主体顺序列", "① 消费 ② 劳动供给 ③ 劳动需求 ④ 投资需求 ⑤ 生产函数 ⑥ 商品出清。<b>按这个顺序写，判卷人一眼能对上。</b>"),
                ("说明劳动市场出清", "② 与 ③ 合起来<b>就是</b>劳动市场出清（<span class='mj'>N^{s}=N^{d}</span>）——不用再单列一条。"),
                ("说明资金市场不必单列", "劳动市场 ＋ 商品市场都出清 ⇒ <b>资金市场自动出清</b>（Walras 定律：家庭预算约束 ＋ 政府预算 ＋ 企业利润恒等式合起来，第三个市场必然平衡）。"),
                ("点一下「六个方程六个未知数」", "方程数与未知数相等，所以均衡是<b>确定的</b>（不是欠定，也不需要额外条件）。"),
            ],
            en="(1) <span class='mj'>C_{t}=C^{d}(Y_{t},Y_{t+1},r_{t})</span><br>(2) <span class='mj'>N_{t}=N^{s}(w_{t},\\theta_{t})</span><br>(3) <span class='mj'>N_{t}=N^{d}(w_{t},A_{t},K_{t})</span><br>(4) <span class='mj'>I_{t}=I^{d}(r_{t},A_{t+1},K_{t})</span><br>(5) <span class='mj'>Y_{t}=A_{t}F(K_{t},N_{t})</span><br>(6) <span class='mj'>Y_{t}=C_{t}+I_{t}</span><br><br>Equations (2) and (3) together are labor-market clearing. Goods-market clearing is (6). Because the labor market and the goods market both clear, the funds market clears as well (Walras' law), so no separate equation is needed. Six equations, six endogenous variables.",
            cn="(1) 消费；(2) 劳动供给；(3) 劳动需求（(2)=(3) 即劳动市场出清）；(4) 投资需求；(5) 生产函数；(6) 商品市场出清。劳动市场与商品市场都出清 ⇒ 资金市场自动出清（Walras 定律），不必单列。六个方程、六个未知数。",
            points=[
                "六条方程齐全（缺一条扣一档）",
                "指出 (2)=(3) 就是劳动市场出清",
                "说明「两个市场出清 ⇒ 资金市场出清」",
                "点出方程数与未知数一致",
            ],
            trap="漏掉「劳动供给」或把劳动供给与需求写成一条却没说清是出清；或者多列一条「<span class='mj'>S_{t}=I_{t}</span>」却不解释它为什么是冗余的（它会与 (6) 重复）。",
            refs=[("T7#p22", "Topic 7 第 22 页"), ("T8#p3", "Topic 8 第 3 页")],
        ),
        dict(
            tag="c",
            q="Sign the partial derivative of the household's labor supply function with respect to each argument, and provide an intuitive explanation (θ_t is the preference parameter for leisure as defined in class).",
            qcn="给出劳动供给函数对各自变量的偏导符号，并解释直觉（θ 是闲暇偏好的参数）。",
            ask="**符号 + 直觉**。两个符号：<span class='mj'>\\partial N^{s}/\\partial w>0</span>、<span class='mj'>\\partial N^{s}/\\partial\\theta<0</span>。**关键理由是 GHH 偏好没有财富效应**——这句话不写，第一个符号就讲不圆。",
            steps=[
                ("对工资：正", "<span class='mj'>\\partial N^{s}/\\partial w_{t}>0</span>。工资是<b>闲暇的价格</b>：工资涨 ⇒ 闲暇变贵 ⇒ 用消费替代闲暇 ⇒ 多工作。"),
                ("为什么没有歧义", "一般情况下工资上升还有<b>收入效应</b>（更有钱 ⇒ 想多休息），两者相反、符号不定。<b>而 GHH 偏好让收入效应消失</b>（<span class='mj'>C</span> 在劳动的一阶条件里约掉了），所以只剩替代效应 ⇒ 符号确定为正。"),
                ("对 θ：负", "<span class='mj'>\\partial N^{s}/\\partial\\theta_{t}<0</span>。<span class='mj'>\\theta</span> 越大＝越看重闲暇 ⇒ 同样工资下更想休息 ⇒ 少工作。"),
                ("（加分）给闭式", "GHH 下 <span class='mj'>N_{t}=1-\\theta_{t}/w_{t}</span>，一眼看出 <span class='mj'>\\partial N/\\partial w=\\theta/w^{2}>0</span>、<span class='mj'>\\partial N/\\partial\\theta=-1/w<0</span>。"),
            ],
            en="<span class='mj'>\\partial N^{s}/\\partial w_{t}>0</span>: the real wage is the price of leisure, so a higher wage makes leisure more expensive and the household substitutes toward consumption, supplying more labor. In general this sign is ambiguous because a higher wage also raises income (income effect); <b>with GHH preferences the income effect is absent</b> — consumption is additive and drops out of the labor-supply first-order condition — so the substitution effect dominates unambiguously.<br><span class='mj'>\\partial N^{s}/\\partial\\theta_{t}<0</span>: <span class='mj'>\\theta_{t}</span> measures the weight on leisure in preferences, so a higher <span class='mj'>\\theta_{t}</span> means the household values leisure more and supplies less labor at any wage. (With GHH, <span class='mj'>N_{t}=1-\\theta_{t}/w_{t}</span>.)",
            cn="对工资为正：工资是闲暇的价格，涨了就用消费替代闲暇、多干活；一般情况下还有相反的收入效应，但 **GHH 偏好让收入效应消失**，所以符号确定。对 θ 为负：θ 越大越看重闲暇，同样工资下少干活。（GHH 下劳动供给可写成 <span class='mj'>N=G^{\\prime-1}(w_t)</span>——<b>只依赖工资，与收入、财富、利率都无关</b>，这正是它区别于普通偏好的地方。课件原话：<i>Under GHH preferences, <span class='mj'>r_t</span> is irrelevant for optimal labor decision</i>。）",
            points=[
                "<span class='mj'>\\partial N^{s}/\\partial w>0</span> ＋ 替代效应（闲暇变贵）",
                "指出<b>一般情形符号不定</b>，GHH 让收入效应消失才确定（关键分）",
                "<span class='mj'>\\partial N^{s}/\\partial\\theta<0</span> ＋ 「更看重闲暇」",
                "（加分）写出「GHH 下 N 只依赖 <span class='mj'>w</span> 与 <span class='mj'>\\theta</span>，与财富／利率无关」",
            ],
            trap="只写「工资高就多干活」而不提收入效应/无财富效应 —— 这在一般情况下是**错的**，判卷人会认为你不知道符号为什么确定。",
            refs=[("T7#p19", "Topic 7 第 19 页"), ("T7#p20", "第 20 页")],
        ),
        dict(
            tag="d",
            q="∂u(C_t,L_t)/∂L_t = w_t · ∂u(C_t,L_t)/∂C_t, where L_t = 1−N_t. Explain what each side captures and why they should be equal at the optimum.",
            qcn="这条一阶条件：两边各是什么？为什么最优点相等？",
            ask="**直觉题**。两个要点：**两边都是「效用」单位**（不是钱）；**不相等就能通过重新分配时间提高效用**。等价说法是 <span class='mj'>\\mathrm{MRS}=w</span>。",
            steps=[
                ("左边：放弃闲暇的边际效用成本", "多工作一单位 ⇒ 少一单位闲暇 ⇒ 效用损失 <span class='mj'>\\partial u/\\partial L</span>。<b>这是「成本」，用效用计价。</b>"),
                ("右边：多赚工资的边际效用收益", "多工作一单位 ⇒ 多拿 <span class='mj'>w</span> 的消费 ⇒ 效用增加 <span class='mj'>w\\cdot\\partial u/\\partial C</span>。<b>这是「收益」，同样用效用计价。</b>"),
                ("为什么相等：否则可以改进", "<b>左边 &gt; 右边</b>：放弃的闲暇比换来的消费更值 ⇒ 少工作；<b>左边 &lt; 右边</b>：多工作能变好 ⇒ 多工作。<b>只有相等时才不再调整。</b>"),
                ("（加分）等价说法", "两边同除 <span class='mj'>\\partial u/\\partial C</span> 得 <span class='mj'>\\mathrm{MRS}_{L,C}=w</span>：<b>闲暇对消费的边际替代率＝实际工资</b>，即「闲暇的价格」。"),
                ("（加分）连回图形", "这条关系就是劳动供给曲线的来源：给定 <span class='mj'>\\theta</span>，它把 <span class='mj'>w</span> 映射成 <span class='mj'>N</span>（<span class='mj'>N=1-L</span> 只是工时的定义）。<b>因为它不含 <span class='mj'>r</span>，所以 <span class='mj'>Y^{s}</span> 才能是竖线。</b>"),
            ],
            en="The <b>left-hand side is the marginal utility cost</b> of supplying one more unit of labor: it is the utility value of the leisure that must be given up, <span class='mj'>\\partial u/\\partial L_{t}</span>.<br>The <b>right-hand side is the marginal utility benefit</b>: one more unit of labor earns <span class='mj'>w_{t}</span> units of consumption, each worth <span class='mj'>\\partial u/\\partial C_{t}</span> in utility, so the gain is <span class='mj'>w_{t}\\,\\partial u/\\partial C_{t}</span>.<br>At an optimum they must be equal, otherwise the household could raise utility by reallocating time: if the left side exceeded the right, the leisure forgone is worth more than the consumption gained, so the household should work less; if it fell short, it should work more. Equivalently, <span class='mj'>\\mathrm{MRS}_{L,C}=w_{t}</span> — the marginal rate of substitution between leisure and consumption equals the real wage, which is the price of leisure in units of consumption.",
            cn="左边＝多工作一单位的**效用成本**（放弃闲暇的边际效用 <span class='mj'>\\partial u/\\partial L</span>）；右边＝多工作一单位的**效用收益**（多赚 <span class='mj'>w</span> 的消费 × 消费的边际效用）。相等是因为不等就能改进：左边大 ⇒ 少干活；左边小 ⇒ 多干活。等价于 <span class='mj'>\\mathrm{MRS}=w</span>——闲暇对消费的边际替代率＝实际工资。",
            points=[
                "左边＝放弃闲暇的边际效用（成本）",
                "右边＝工资 × 消费的边际效用（收益）",
                "为什么相等：否则可重新分配时间提高效用（分情况说一句）",
                "（加分）等价于 <span class='mj'>\\mathrm{MRS}_{L,C}=w</span>",
            ],
            trap="把左边说成「工资」或把右边说成「<span class='mj'>w</span>」——**两边都必须带边际效用**，否则量纲不对（一个效用、一个货币）。这是最常见的失分。",
            refs=[("T7#p16", "Topic 7 第 16 页"), ("T7#p17", "第 17 页")],
        ),
        dict(
            tag="e",
            q="Draw in the main graphical diagram for this model to show the initial equilibrium.",
            qcn="画出这个模型的主图，标出初始均衡。",
            ask="**主图题**。这门课的主图是<b>四格（课件画五格）</b>：劳动市场 → 生产函数 → (r,Y) → 45° 图。**四格必须自洽**：前两格定 <span class='mj'>Y</span>，第三格定 <span class='mj'>r</span>，第四格用 <span class='mj'>r</span> 回查。",
            steps=[
                ("① 劳动市场 (N, w)", "画 <span class='mj'>N^{s}</span> 上斜、<span class='mj'>N^{d}</span> 下斜，交点给出 <span class='mj'>(N_{0},w_{0})</span>。"),
                ("② 生产函数 (N, Y)", "把 <span class='mj'>N_{0}</span> 代进去得到 <span class='mj'>Y_{0}</span>（凹、上斜）。"),
                ("③ (r, Y) 平面", "在 <span class='mj'>Y_{0}</span> 处画<b>竖直</b>的 <span class='mj'>Y^{s}</span>，再画下斜的 IS；交点给出 <span class='mj'>(Y_{0},r_{0})</span>。"),
                ("④ 45° 图", "支出线穿过 <span class='mj'>(Y_{0},Y_{0})</span>，斜率＝MPC&lt;1。<b>它把 <span class='mj'>r_{0}</span> 与 <span class='mj'>Y_{0}</span> 的「一致性」画出来。</b>"),
                ("用箭头把四格连起来", "课件用虚线/箭头从 ①→②→③→④。**加箭头是「自洽」的可见证据，阅卷时很吃分。**"),
            ],
            fig="main4",
            en="Draw four panels: (i) the <b>labor market</b> with <span class='mj'>N^{s}</span> upward-sloping and <span class='mj'>N^{d}</span> downward-sloping, giving <span class='mj'>(N_{0},w_{0})</span>; (ii) the <b>production function</b>, mapping <span class='mj'>N_{0}</span> into <span class='mj'>Y_{0}</span>; (iii) the <b><span class='mj'>(r_{t},Y_{t})</span> plane</b> with <span class='mj'>Y^{s}</span> vertical at <span class='mj'>Y_{0}</span> and the downward-sloping IS curve, giving <span class='mj'>r_{0}</span>; (iv) the <b>45-degree diagram</b>, where the expenditure line (slope equal to the MPC) passes through <span class='mj'>(Y_{0},Y_{0})</span> at <span class='mj'>r_{0}</span>. Label all axes and use arrows to show the chain labor market → production → IS/<span class='mj'>Y^{s}</span> → 45° line, so that the four panels are mutually consistent.",
            cn="四格：① 劳动市场（供给上斜、需求下斜）定 (N0, w0)；② 生产函数把 N0 翻成 Y0；③ (r,Y) 平面：Y0 处竖直的 Ys ＋ 下斜的 IS，定 r0；④ 45° 图：支出线过 (Y0, Y0)。用箭头把四格串起来，证明自洽。",
            points=[
                "四格齐全（劳动市场 / 生产函数 / (r,Y) / 45°）",
                "每格标出交点与数值（N0、w0、Y0、r0）",
                "<span class='mj'>Y^{s}</span> 竖直、IS 下斜、支出线斜率＝MPC",
                "（加分）箭头/虚线把四格连起来",
            ],
            trap="只画 ③ 一格（那是「两条曲线交叉」，不是「主图」）；或四格的 <span class='mj'>Y</span> 对不上（② 给的 <span class='mj'>Y_{0}</span> 与 ③ 的竖线位置不一致）——**自洽比画工重要**。",
            refs=[("T8#p17", "Topic 8 第 17 页"), ("T8#p5", "第 5 页")],
        ),
        dict(
            tag="f",
            q="Suppose <span class='mj'>A_{t}</span> increases (<span class='mj'>A_{t+1}</span> unchanged). Show how this shock impacts all relevant curves; indicate whether each endogenous variable goes up, down, unaffected, or ambiguous.",
            qcn="设 <span class='mj'>A_{t}</span> 上升（<span class='mj'>A_{t+1}</span> 不变）。画出各条线怎么动，并指出每个内生变量升/降/不变/不确定。",
            ask="**全题分值最高的一问**。五个动作 + 六个符号。<b>最关键的一步是「<span class='mj'>N^{s}</span> 不动、IS 不动」</b>——这两处决定了整题对不对。",
            steps=[
                ("动<b>劳动需求</b>（右移）", "<span class='mj'>w=A_{t}F_{N}</span>：给定 <span class='mj'>N</span>，<span class='mj'>A_{t}</span> 上去 ⇒ 劳动的边际产品上去 ⇒ 同样工资下愿雇更多人。"),
                ("不动<b>劳动供给</b>", "<span class='mj'>N^{s}=N^{s}(w,\\theta)</span>：<b>只依赖 <span class='mj'>w</span> 与 <span class='mj'>\\theta</span></b>，<span class='mj'>A_{t}</span> 不在里面（GHH 无财富效应）。<b>这一步是全题的枢纽。</b>"),
                ("定 <span class='mj'>N</span> 与 <span class='mj'>w</span>", "需求右移、供给不动 ⇒ <b><span class='mj'>N\\uparrow</span>、<span class='mj'>w\\uparrow</span></b>（沿供给线上移）。"),
                ("动<b>生产函数</b>（上移）＋<b> <span class='mj'>Y^{s}</span></b>（右移）", "<span class='mj'>Y=A_{t}F(K,N)</span> 上移；<span class='mj'>Y^{s}</span> 竖线右移到 <span class='mj'>Y_{1}=A_{t}'F(K,N_{1})</span>。<b>两个渠道同向：<span class='mj'>A</span> 升 ＋ <span class='mj'>N</span> 升。</b>"),
                ("不动 <b>IS</b>", "<span class='mj'>Y^{d}=C^{d}(Y_{t},Y_{t+1},r_{t})+I^{d}(r_{t},A_{t+1},K_{t})</span>：<b><span class='mj'>A_{t}</span> 不出现</b>（投资看的是 <span class='mj'>A_{t+1}</span>）。所以 IS 原地不动。"),
                ("读新交点", "<span class='mj'>Y^{s}</span> 右移、IS 不动 ⇒ 沿 IS <b>向下滑</b>：<b><span class='mj'>Y\\uparrow</span>、<span class='mj'>r\\downarrow</span></b>。"),
                ("补完剩下两个", "<span class='mj'>C\\uparrow</span>（<span class='mj'>Y</span> 升 ＋ <span class='mj'>r</span> 降，两个渠道同向）；<span class='mj'>I\\uparrow</span>（<span class='mj'>r</span> 降）。<b>六个符号全确定，没有 ?。</b>"),
            ],
            fig="main4",
            en="An increase in <span class='mj'>A_{t}</span> shifts <b>labor demand right</b> (higher marginal product of labor at any <span class='mj'>N</span>) but leaves <b>labor supply unchanged</b>, since <span class='mj'>N^{s}</span> depends only on <span class='mj'>w_{t}</span> and <span class='mj'>\\theta_{t}</span> (GHH rules out a wealth effect). Hence <span class='mj'>N_{t}</span> and <span class='mj'>w_{t}</span> both rise. The production function shifts up and the vertical <span class='mj'>Y^{s}</span> curve shifts right, through both channels — higher <span class='mj'>A_{t}</span> and higher <span class='mj'>N_{t}</span>. The <b>IS curve does not move</b>, because <span class='mj'>A_{t}</span> does not appear in <span class='mj'>C^{d}</span> or in <span class='mj'>I^{d}</span> (investment depends on <span class='mj'>A_{t+1}</span>). The new equilibrium is therefore on the same IS at higher <span class='mj'>Y_{t}</span> and lower <span class='mj'>r_{t}</span>. Signs: <span class='mj'>Y_{t}\\uparrow</span>, <span class='mj'>C_{t}\\uparrow</span>, <span class='mj'>I_{t}\\uparrow</span>, <span class='mj'>N_{t}\\uparrow</span>, <span class='mj'>w_{t}\\uparrow</span>, <span class='mj'>r_{t}\\downarrow</span> — all six determined.",
            cn="劳动需求右移（MPK 上升）、**劳动供给不动**（只依赖 w 与 θ）⇒ N↑、w↑。生产函数上移、<span class='mj'>Y^{s}</span> 右移（A 与 N 两个渠道同向）。**IS 不动**（<span class='mj'>A_{t}</span> 不进消费与投资函数）。沿 IS 下滑 ⇒ Y↑、r↓。再补 C↑（两个渠道同向）、I↑（r 降）。六个符号全部确定。",
            points=[
                "劳动需求右移，<b>劳动供给不动</b>（并说明理由）",
                "生产函数上移 ＋ <span class='mj'>Y^{s}</span> 右移",
                "<b>IS 不动</b>（并说明 <span class='mj'>A_{t}</span> 不进需求侧）",
                "六个符号：Y↑ C↑ I↑ N↑ w↑ r↓",
                "（加分）指出 C 有两个渠道同向，所以无歧义",
            ],
            trap="① 把 IS 也右移（最常见的错，等于把 <span class='mj'>A_{t}</span> 当 <span class='mj'>A_{t+1}</span>）；② 说「劳动供给右移」（GHH 下它不动）；③ 只给 <span class='mj'>Y</span> 与 <span class='mj'>r</span> 的符号，忘了后面四个。",
            refs=[("T8#p19", "Topic 8 第 19 页"), ("T8#p20", "第 20 页"), ("T8#p24", "第 24 页")],
        ),
        dict(
            tag="g",
            q="Relative to an endowment economy where Y_t = A_t, does output Y_t increase by more or less in the production economy when A_t increases? Briefly explain.",
            qcn="与 Y_t = A_t 的禀赋经济相比，生产经济里 A_t 上升带来的产出增加更多还是更少？",
            ask="**对比题（送分但有陷阱）**。答案：**更多**。理由只有一个：**生产经济里就业会跟着涨**（<span class='mj'>N</span> 内生），禀赋经济里 <span class='mj'>N</span> 固定。",
            steps=[
                ("先给结论", "**更多**（more）。"),
                ("拆成两个渠道", "<span class='mj'>Y=A_{t}F(K,N)</span> 全微分：<span class='mj'>dY=F\\,dA+A F_{N}\\,dN</span>。"),
                ("对比禀赋经济", "禀赋经济：<span class='mj'>Y_{t}=A_{t}</span>，<b><span class='mj'>N</span> 固定</b>，所以 <span class='mj'>dY=dA</span>——只有第一项。"),
                ("生产经济", "多出 <span class='mj'>A F_{N}\\,dN>0</span> 这一项（<span class='mj'>A</span> 升 ⇒ 劳动需求右移 ⇒ <span class='mj'>N</span> 升）⇒ <b>放大</b>。"),
                ("一句话收口", "<b>内生劳动供给是放大器</b>：同样的技术冲击，在有生产的经济里被「多雇人」放大了一次。"),
            ],
            en="Output increases by <b>more</b> in the production economy. With <span class='mj'>Y_{t}=A_{t}F(K_{t},N_{t})</span>, <span class='mj'>dY_{t}=F\\,dA_{t}+A_{t}F_{N}\\,dN_{t}</span>: there is the direct productivity effect <span class='mj'>F\\,dA_{t}</span>, plus an <b>indirect effect through endogenous employment</b>, since higher <span class='mj'>A_{t}</span> shifts labor demand out along an upward-sloping labor supply, so <span class='mj'>N_{t}</span> rises and raises output further. In the endowment economy <span class='mj'>Y_{t}=A_{t}</span> and employment is fixed, so only the direct effect operates (<span class='mj'>dY_{t}=dA_{t}</span>). Hence the production economy <b>amplifies</b> productivity shocks.",
            cn="**更多**。因为 <span class='mj'>Y=A F(K,N)</span> 里 N 是内生的：<span class='mj'>dY=F dA + A F_N dN</span>，第二项正是「多雇人」带来的放大；禀赋经济里 N 固定，只有第一项 <span class='mj'>dY=dA</span>。所以**内生劳动供给是放大器**。",
            points=[
                "答 <b>more</b>",
                "拆出两个渠道：直接生产率效应 ＋ 内生就业效应",
                "说明禀赋经济里 <span class='mj'>N</span> 固定、只有直接效应",
                "（加分）写出 <span class='mj'>dY=F\\,dA+A F_{N}\\,dN</span>",
            ],
            trap="答「一样」或「更少」——那是把生产经济当成「<span class='mj'>N</span> 固定」；或只说「因为生产函数」而不提「就业会变」。",
            refs=[("T8#p14", "Topic 8 第 14 页"), ("T5#p14", "Topic 5 第 14 页")],
        ),
        dict(
            tag="h",
            q="How does consumption adjust to higher A_t relative to Y_t? How does your answer here differ (or not) from an endowment economy setup?",
            qcn="消费相对产出的调整幅度是多少？这与禀赋经济的答案有何不同？",
            ask="**最容易被答糊的一问**。要点：**生产经济里 <span class='mj'>ΔC&lt;ΔY</span>**（差额去了投资）；**禀赋经济里 <span class='mj'>ΔC=ΔY</span>**（没有投资，<span class='mj'>S=0</span>）。",
            steps=[
                ("生产经济：C 上升但少于 Y", "<span class='mj'>ΔY=ΔC+ΔI</span>，而 <span class='mj'>r</span> 下降使 <span class='mj'>I</span> 上升 ⇒ <b><span class='mj'>0<ΔC<ΔY</span></b>。<b>消费平滑</b>：这是一次暂时的高产，家庭不会全部花掉。"),
                ("禀赋经济：C 恰好等于 Y", "禀赋经济里没有投资品，出清要求 <b><span class='mj'>S=0</span> ⇒ <span class='mj'>C_{t}=Y_{t}</span></b>，所以 <b><span class='mj'>ΔC=ΔY</span></b>。"),
                ("那利率在禀赋经济里干什么", "<span class='mj'>r</span> 下降，<b>说服家庭把多出来的产出全部消费掉</b>（而不是储蓄）。<b>这是两讲最漂亮的分工：T5 的 r 是「刹车」，T7 的 r 是「出口」。</b>"),
                ("一句话对比", "**生产经济：多出来的产出被 C 与 I 分掉；禀赋经济：全部被 C 吃掉。**"),
            ],
            en="In the <b>production economy</b>, consumption rises but <b>by less than output</b>: <span class='mj'>\\Delta Y_{t}=\\Delta C_{t}+\\Delta I_{t}</span>, and because the interest rate falls, investment rises, so <span class='mj'>0<\\Delta C_{t}<\\Delta Y_{t}</span>. The household smooths a temporary windfall rather than consuming all of it.<br>In the <b>endowment economy</b> there is no investment, so market clearing requires <span class='mj'>S_{t}=0</span> and hence <span class='mj'>C_{t}=Y_{t}</span>: consumption rises <b>one-for-one</b> with output, <span class='mj'>\\Delta C_{t}=\\Delta Y_{t}</span>. The interest rate falls in order to make households willing to consume the entire increase rather than save it. So the difference is exactly the presence of an investment outlet for saving.",
            cn="**生产经济**：<span class='mj'>ΔY=ΔC+ΔI</span>，r 下降使 I 上升，所以 <span class='mj'>0<ΔC<ΔY</span>（消费平滑，不会把暂时的高产全花掉）。**禀赋经济**：没有投资，出清要求 <span class='mj'>S=0</span> ⇒ <span class='mj'>C=Y</span>，所以 <span class='mj'>ΔC=ΔY</span>；r 下降的作用是「说服家庭把多出来的全吃掉」。**差别就是「有没有投资这个出口」。**",
            points=[
                "生产经济：<span class='mj'>ΔC<ΔY</span>（且 <span class='mj'>ΔC>0</span>）",
                "理由：一部分产出被投资吸收（<span class='mj'>r</span> 下降使 <span class='mj'>I</span> 上升）",
                "禀赋经济：<span class='mj'>C=Y</span> ⇒ <span class='mj'>ΔC=ΔY</span>",
                "（加分）说清禀赋经济里 <span class='mj'>r</span> 的作用是「让 S=0」",
            ],
            trap="笼统答「消费也上升」而不比较**幅度**——题目问的是 relative to <span class='mj'>Y</span>；或忘了禀赋经济里 <span class='mj'>C=Y</span> 是**出清条件**（不是假设）。",
            refs=[("T5#p9", "Topic 5 第 9 页"), ("T7#p22", "Topic 7 第 22 页")],
        ),
    ],
))

# ---------------- §4 更新占位 ----------------
SECTIONS.append(dict(
    id="next", num="四", title="还没来的题",
    sub="这份练习老师还在更新（PDF 上写着 Dynamically Updated）。新题来了怎么加，写在这里。",
    blocks=[
        ("p", "**当前版本（Oct 27, 2026）只有 Q2、Q3 两题、16 小问，覆盖 Topic 6 / 7 / 8。** 但期末是 Topic 1–10 全考，所以下面这三块**迟早要补**——老师加题时大概率从这三块里出。"),
        ("table", dict(
            caption="按「还没被这份练习覆盖」排的优先级",
            header=["还没考到的块", "为什么大概率会考", "现在先看哪几页"],
            first_bold=True,
            rows=[
                ["Topic 9 · 货币侧", "Key Concepts 只写到 Topic 8，但期末大纲含 T9；<b>货币中性 + 实际块/名义块分离</b>是最标准的论述题", "[[T9#p14|T9 p14]]、[[T9#p15|p15]]、[[T9#p17|p17]]"],
                ["Topic 10 · 新凯恩斯", "与 Q2(h)「乘数为零」天然对照：<b>粘性价格下乘数为正</b>，几乎是必考的对比题", "[[T10#p21|T10 p21]]、[[T10#p24|p24]]、[[T10#p31|p31]]"],
                ["Topic 4 · 两期消费", "Q2(c) 已经用到永久收入假说；<b>欧拉方程 + 借贷约束</b>是可单独出大题的老考点", "[[T4#p11|T4 p11]]、[[T4#p33|p33]]"],
                ["Topic 2 · 索洛", "期中练习的主体；期末若考「增长」，多半是<b>稳态 + 黄金律 + 时间路径</b>", "[[T2#p21|T2 p21]]、[[T2#p38|p38]]"],
            ],
            note="**顺序建议**：先把现有 16 问做到能默写，再补 Topic 9/10（与 Q2 直接对照，性价比最高），最后回 Topic 2/4。",
        )),
        ("note", "到时候怎么加题", "在 `practice_content.py` 里对应节追加一个 item（`tag`／`q`／`qcn`／`ask`／`steps`／`en`／`cn`／`points`／`trap`／`refs`），然后 `python build_practice.py`。<b>进度记录按 qid 存，加新题不会清掉旧的勾。</b>"),
        ("tip", "最后提醒", "这份练习的价值不在「答案」，而在**它把出题人的语言习惯暴露了**：<b>「sign the partial derivative」「intuitively describe each side」「relate to a key implication」</b>——这三句式就是期末大题的骨架。**背句型比背答案更值钱。**"),
    ],
))
