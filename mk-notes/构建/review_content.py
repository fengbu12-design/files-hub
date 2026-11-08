# -*- coding: utf-8 -*-
"""
AF5638 期末总复习 · 内容文件

组织方式（与十讲笔记不同）：
  十讲笔记是「纵向」——一页一页把课件讲透。
  这份总复习是「横向」——把十个模型摆在一起比、把同一件事在各讲里的说法串起来。

所有公式与结论都取自十讲 content_topicN.py 中已核对过的内容，
并在每处标注出处（可点击跳回原讲对应页）。
"""

COURSE   = "AF5638 宏观经济学"
TITLE    = "期末总复习"
SUBTITLE = "十个模型、一条主线、五张必背表：把「每一讲都懂、合起来就乱」治掉"
META = [
    "期末 50% · 12/3–18 考试周",
    "教材 GLS (2021)",
    "讲师 Elaine Liu（PolyU）",
    "覆盖 Topic 1–10 · 共 300 页课件",
]

OPENER = [
    ("这门课只有一句话",
     "先用<b>一条差分方程</b>解释「为什么有的国家富」（Topic 1–3），再用<b>一个最优化问题</b>把「储蓄」从假设变成结论（Topic 4），然后把结论放进<b>市场</b>（Topic 5–7），最后把市场画成<b>两条线</b>、装上<b>货币</b>、粘住<b>价格</b>（Topic 8–10）。",
     "一句话：从「增长」到「波动」，中间只换了三个假设"),
    ("考试怎么考",
     "三种题型：<b>① 比较静态</b>（某个外生变量变了，六个内生量怎么变）；<b>② 图形</b>（画两条线、标出移动、说清交点）；<b>③ 论述</b>（某个结论在什么条件下成立、破了会怎样）。<b>三种题用的是同一套库存</b>：模型 + 曲线 + 符号。",
     "三题型 · 一套库存"),
    ("这份材料怎么用",
     "不要从头读到尾。<b>先看第 2 节的八模型对照表</b>（把结论归位），<b>再看第 6 节的十六组易混</b>（把错位纠正），<b>最后做第 9 节的自测清单</b>。<b>第 7 节的四张表是考场默写用的，建议单独打印。</b>",
     "建议顺序：2 → 6 → 9 → 7"),
]

FLOW = [
    dict(num="T2", title="Solow 模型", desc="只有资本积累。储蓄率 s 是天上掉的参数。", tag="增长"),
    dict(num="T4", title="两期消费", desc="把 s 换成「家庭最优选择」，生出欧拉方程。", tag="造零件"),
    dict(num="T5", title="禀赋经济", desc="加一个市场：利率被解出来，让储蓄归零。", tag="一般均衡"),
    dict(num="T6", title="财政政策", desc="加一个政府：税消失，融资方式无关。", tag="加主体"),
    dict(num="T7", title="生产经济", desc="加企业、让劳动内生：储蓄有了出口（=投资）。", tag="加生产"),
    dict(num="T8", title="两条曲线", desc="把六个方程压成 IS + Yˢ，产出由供给定。", tag="画图"),
    dict(num="T9", title="装上货币", desc="MIU 引入 M/P，物价与名义利率出场，货币中性。", tag="加货币"),
    dict(num="T10", title="粘住价格", desc="AS 不再竖直，需求终于能改产量。", tag="换假设"),
]

# ============================================================
SECTIONS = []

# ---------- §1 三块大陆 ----------
SECTIONS.append(dict(
    id="s1", num="一", title="三块大陆：这门课的地形",
    sub="十讲不是十件互不相干的事，而是三块大陆。每一块有自己的「核心问题」与「核心工具」，混着记就会乱。",
    blocks=[
        ("p", "把课程按「时间尺度」切三刀，十讲立刻归位。**跨块比较是最大的失分来源**——比如拿 Topic 6 的「乘数为零」去答 Topic 10 的题，方向就全错了。"),
        ("table", dict(
            caption="三块大陆的对照",
            header=["", "长期增长（T1–3）", "跨期与一般均衡（T4–7）", "短期波动（T8–10）"],
            first_bold=True,
            rows=[
                ["<b>核心问题</b>", "为什么有的国家富、增长为什么会慢", "储蓄率从哪来、利率怎么被定出来", "衰退时政策有没有用"],
                ["<b>时间尺度</b>", "几十年", "两期（今天 vs 明天）", "一期内（价格来不及调整）"],
                ["<b>核心工具</b>", "一条差分方程 + 稳态", "一个最优化问题 + 市场出清", "两条曲线 + 一条 AS"],
                ["<b>产出 <span class='mj'>Y</span></b>", "内生（由 <span class='mj'>K,A,s</span> 决定）", "<b>给定</b>（T5/6）或<b>生产出来</b>（T7）", "<b>供给定</b>（T8/9）或<b>需求定</b>（T10）"],
                ["<b>价格</b>", "不出现（或只出现要素价格）", "<span class='mj'>r</span>（T5–7 再加 <span class='mj'>w</span>）", "<span class='mj'>r,w,P,i</span>"],
                ["<b>一句话结论</b>", "资本积累只有水平效应，持续增长靠技术", "利率让储蓄找到出口", "价格粘不粘，决定需求有没有用"],
                ["<b>最容易混的</b>", "水平效应 vs 增长效应", "<span class='mj'>S=0</span>（T5）vs <span class='mj'>S=I</span>（T7）", "乘数 0（T6/8）vs 乘数正（T10）"],
            ],
            note="**三块大陆之间只有一条通道**：Topic 4 造出来的消费函数 <span class='mj'>C^{d}</span>。它先被 Topic 5/6/7 塞进一般均衡，再被 Topic 8 塞进 IS，最后被 Topic 10 塞进 AD。**所以「消费函数」是整门课唯一一个贯穿全部十讲的零件。**",
        )),
        ("note", "三面承重墙", "不管哪一块大陆，都靠三样东西撑着：**① 生产函数 <span class='mj'>Y=AF(K,N)</span>**（决定「能产多少」）；**② 欧拉方程**（决定「怎么在时间上分配」）；**③ 市场出清**（决定「价格是多少」）。**任何一道题，先问「这三样里哪一样被动了」，就知道该从哪儿下手。**"),
        ("warn", "最常见的跨块错误", "把「乘数为零」当成整门课的结论。**它只在「产出不能变」时成立**（Topic 6 的禀赋经济、Topic 8/9 的竖直 <span class='mj'>Y^{s}</span>）。**一旦价格粘住（Topic 10），乘数就为正。**"),
    ],
))

# ---------- §2 八模型对照 ----------
SECTIONS.append(dict(
    id="s2", num="二", title="八个模型：一张表把结论归位",
    sub="每一个模型都是在上一个模型上「只改一处」。这张表的每一列，都是一处改动带来的后果。",
    blocks=[
        ("p", "读法：**先看「改了什么」，再看「结论变了什么」**。如果你能说出「Topic 7 相比 Topic 5 只多了一个投资出口」，那这一列就不用背了。"),
        ("table", dict(
            caption="八个模型逐项对照（横向读完，等于把十讲重读一遍）",
            header=["模型", "谁在决策", "外生给定", "被解出来", "价格", "出清条件", "一句话结论"],
            first_bold=True,
            cls="table",
            rows=[
                ["<b>T2 Solow</b><br><span class='pj'>（长期）</span>", "一个「储蓄率 <span class='mj'>s</span>」", "<span class='mj'>s,n,z,\\delta,A</span>", "<span class='mj'>k,y,c</span> 的路径与稳态", "无", "稳态：<span class='mj'>sAf(k)=\\delta k</span>", "资本积累只有水平效应"],
                ["<b>T4 两期</b><br><span class='pj'>（造零件）</span>", "家庭：选 <span class='mj'>C_{t},C_{t+1}</span>", "<span class='mj'>Y_{t},Y_{t+1},r</span>", "<span class='mj'>C_{t},C_{t+1},S</span>", "<span class='mj'>r</span> <b>给定</b>", "IBC（个体）", "欧拉方程定时序，IBC 定水平"],
                ["<b>T5 禀赋</b>", "家庭（<span class='mj'>N,I</span> 固定）", "<span class='mj'>Y_{t},Y_{t+1}</span>", "<span class='mj'>C_{t},C_{t+1},r</span>", "<b><span class='mj'>r</span> 解出来</b>", "<span class='mj'>S=0\\Leftrightarrow Y=C</span>", "利率把储蓄逼回零"],
                ["<b>T6 财政</b>", "家庭 ＋ 政府", "<span class='mj'>G_{t},G_{t+1}</span>", "<span class='mj'>C,r</span>（<span class='mj'>T,B</span> 消失）", "<span class='mj'>r</span>", "<span class='mj'>S-B=0</span>", "融资方式无关，只有 <span class='mj'>G</span> 重要；乘数 0"],
                ["<b>T7 生产</b>", "企业（选 <span class='mj'>N,I</span>）＋ 家庭（选 <span class='mj'>N</span>）", "<span class='mj'>K_{t},A_{t},A_{t+1},\\theta_{t}</span>", "<span class='mj'>C,I,N,Y,w,r</span>", "<span class='mj'>w,r</span>", "三市场（两条独立）", "储蓄有了出口：<span class='mj'>S=I</span>"],
                ["<b>T8 实物侧</b>", "同上，但把方程压成两条线", "同上 ＋ <span class='mj'>G</span>", "<span class='mj'>Y,r,N,w,C,I</span>", "<span class='mj'>w,r</span>", "IS ∩ <span class='mj'>Y^{s}</span>", "<b>产出由供给定</b>，需求只改构成"],
                ["<b>T9 名义侧</b>", "同上 ＋ 央行（<span class='mj'>M</span>）", "另加 <span class='mj'>M_{t}</span>", "另加 <span class='mj'>P,i</span>", "<span class='mj'>P,i</span>（名义）", "另加货币市场", "<b>货币中性</b>：钱只改物价"],
                ["<b>T10 新凯恩斯</b>", "同上，但价格<b>粘住</b>", "另加 <span class='mj'>\\bar P</span>（或 <span class='mj'>\\gamma</span>）", "同 T9，但 <span class='mj'>P</span> 不再清市场", "<b>粘住</b>", "AD ∩ AS（AS 不竖直）", "<b>需求能改产量</b>，政策有效"],
            ],
            note="**这张表最重要的一列是「一句话结论」**。考试时先在草稿纸上写这一列，就知道该用哪个模型的结论——**不要凭印象挑模型，要凭「哪个假设成立」挑模型**。",
        )),
        ("big", "把这张表竖过来读，就是整门课的剧情：**<span class='mj'>s</span> 外生（T2）→ <span class='mj'>s</span> 解出来（T4）→ <span class='mj'>r</span> 让 <span class='mj'>S=0</span>（T5）→ 政府进来（T6）→ <span class='mj'>r</span> 让 <span class='mj'>S=I</span>（T7）→ 画成两条线（T8）→ 装上钱（T9）→ 粘住价格（T10）。**"),
        ("tip", "背这张表的方法", "**只背「改了什么」这一句**：T5 改了「加市场」、T6「加政府」、T7「加生产」、T8「加图形」、T9「加货币」、T10「改价格假设」。**五个动词，八个模型全记住。**"),
    ],
))

# ---------- §3 核心方程 ----------
SECTIONS.append(dict(
    id="s3", num="三", title="核心方程：六个模块，四十五条",
    sub="只收「考场上要写出来」的式子。每条都标了出处，点进去能看推导。",
    blocks=[
        ("p", "按模块分组，**不按讲次**——因为同一个模块的式子往往跨好几讲（比如「利率」这个模块横跨 T4–T10）。**每组后面的「用途」一栏，是判卷时看的「这句话说明了什么」。**"),

        ("note", "模块一 · 增长（T1–T3）", "这一组只在「长期」出现，**不要和短期模型的式子混用**：这里的 <span class='mj'>s</span> 是外生参数，不是「储蓄函数」。"),
        ("eq", [
            ("生产函数（人均）", "y=A f(k)", "由 CRTS 得到；CD 特例 <span class='mj'>y=Ak^{\\alpha}</span>，<span class='mj'>\\alpha\\approx0.35</span> 是资本份额", "[[T2#p18|Topic 2 第 18 页]]"),
            ("资本积累（人均）", "k_{t+1}=sAf(k_{t})+(1-\\delta)k_{t}", "**全讲唯一的方程**：明天存下的 ＋ 今天没折旧的", "[[T2#p19|Topic 2 第 19 页]]"),
            ("稳态条件", "sAf(k^{*})=\\delta k^{*}", "**增长率归零**，不是「产出归零」", "[[T2#p21|Topic 2 第 21 页]]"),
            ("稳态资本（CD）", "k^{*}=\\left(\\frac{sA}{\\delta}\\right)^{\\frac{1}{1-\\alpha}}", "反解出来；指数 <span class='mj'>1/(1-\\alpha)>1</span> 是关键", "[[T2#p25|Topic 2 第 25 页]]"),
            ("增长核算", "g_{Y}=\\alpha g_{K}+(1-\\alpha)g_{L}+g_{A}", "**残差法**：算不出来的那部分叫 TFP（水平式 <span class='mj'>\\ln A=\\ln Y-\\alpha\\ln K-(1-\\alpha)\\ln L</span>）", "[[T3#p12|Topic 3 第 12 页]]"),
            ("相对收入（两国相比）", "\\frac{y_{1}}{y_{2}}=\\left(\\frac{s_{1}}{s_{2}}\\right)^{\\frac{\\alpha}{1-\\alpha}}\\left(\\frac{A_{1}}{A_{2}}\\right)^{\\frac{1}{1-\\alpha}}", "**Topic 3 的全部论证工具**：s 的指数小、A 的指数大", "[[T3#p9|Topic 3 第 9 页]]"),
        ], "六条。**注意第三条与第一条的区别**：第一条是「每期都成立」，第三条只在稳态成立。"),

        ("note", "模块二 · 消费（T4 造，T5–T10 用）", "这个模块只有一个零件，但它是全课唯一贯穿十讲的式子。**凡是看到「家庭」，第一个想到它。**"),
        ("eq", [
            ("跨期预算（IBC）", "C_{t}+\\frac{C_{t+1}}{1+r_{t}}=Y_{t}+\\frac{Y_{t+1}}{1+r_{t}}", "**一生花的现值 = 一生赚的现值**；<span class='mj'>S</span> 被消掉", "[[T4#p6|Topic 4 第 6 页]]"),
            ("欧拉方程", "u_{C}(C_{t})=\\beta(1+r_{t})u_{C}(C_{t+1})", "**只定「比例」，定不出「水平」**——水平靠 IBC", "[[T4#p11|Topic 4 第 11 页]]"),
            ("消费函数", "C_{t}=C^{d}(Y_{t}^{+},Y_{t+1}^{+},r_{t}^{-})", "**这就是那个零件**：收入↑多花，利率↑少花（储蓄者）", "[[T4#p18|Topic 4 第 18 页]]"),
            ("含政府（李嘉图等价）", "C_{t}=C^{d}(Y_{t}-G_{t},\\ Y_{t+1}-G_{t+1},\\ r_{t})", "自变量是 <span class='mj'>G</span> 不是 <span class='mj'>T</span>：**税被看穿了**", "[[T6#p8|Topic 6 第 8 页]]"),
        ], "四条。**第二、三条的分工**：欧拉管「斜率」（时序），IBC 管「高度」（水平）。"),

        ("note", "模块三 · 企业（T7）", "只在 Topic 7 出现，但 **Topic 8 的 IS 与 Yˢ 全靠它**。三条一阶条件都是「边际成本 = 边际收益」。"),
        ("eq", [
            ("生产与积累", "Y_{t}=A_{t}F(K_{t},N_{t}),\\qquad K_{t+1}=I_{t}+(1-\\delta)K_{t}", "两条约束；<span class='mj'>K_{t}</span> 是 **predetermined**", "[[T7#p3|Topic 7 第 3 页]]"),
            ("劳动条件（每期一条）", "w_{t}=A_{t}F_{N}(K_{t},N_{t})", "工资 = 劳动的边际产品", "[[T7#p7|Topic 7 第 7 页]]"),
            ("投资条件", "1+r_{t}=A_{t+1}F_{K}(K_{t+1},N_{t+1})+1-\\delta", "两边都按「明年的总金额」计价", "[[T7#p7|Topic 7 第 7 页]]"),
            ("投资条件（净形式）", "r_{t}=\\mathrm{MPK}_{t+1}-\\delta", "**利率 = 资本的净回报**（无套利）", "[[T7#p7|Topic 7 第 7 页]]"),
            ("劳动需求", "N_{t}=N^{d}(w_{t}^{-},A_{t}^{+},K_{t}^{+})", "**<span class='mj'>K_{t}</span> 正号**（<span class='mj'>F_{KN}>0</span>）", "[[T7#p8|Topic 7 第 8 页]]"),
            ("投资需求", "I_{t}=I^{d}(r_{t}^{-},A_{t+1}^{+},K_{t}^{-})", "**<span class='mj'>K_{t}</span> 负号**（重置效应）——与上一条对照记", "[[T7#p10|Topic 7 第 10 页]]"),
            ("GHH 劳动供给", "\\frac{\\theta_{t}}{1-N_{t}}=w_{t}\\ \\Rightarrow\\ N_{t}=1-\\frac{\\theta_{t}}{w_{t}}", "**<span class='mj'>C</span> 消失** ⇒ 无财富效应 ⇒ T8 的 <span class='mj'>Y^{s}</span> 竖直", "[[T7#p19|Topic 7 第 19 页]]"),
        ], "七条。**第五、六条是「同名不同号」的一对**，考试最爱在这里设陷阱。"),

        ("note", "模块四 · 均衡（T5–T8）", "「出清」这件事在各讲长得不一样，但逻辑一样：**让某个市场的供给等于需求，从而定出一个价格**。"),
        ("eq", [
            ("禀赋经济出清", "S_{t}=0\\ \\Longleftrightarrow\\ Y_{t}=C_{t}", "**没有投资，所以储蓄只能为零**", "[[T5#p9|Topic 5 第 9 页]]"),
            ("有政府时", "S_{t}=B_{t}\\ \\Longleftrightarrow\\ Y_{t}=C_{t}+G_{t}", "家庭储蓄要吸收政府借款", "[[T6#p13|Topic 6 第 13 页]]"),
            ("生产经济", "S_{t}=I_{t},\\qquad Y_{t}=C_{t}+I_{t}", "**储蓄有了出口**——这是 T7 与 T5 的分水岭", "[[T7#p22|Topic 7 第 22 页]]"),
            ("IS 曲线", "Y_{t}=C^{d}(\\cdot)+I^{d}(\\cdot)+G_{t}", "商品市场出清 ⇒ 给定 <span class='mj'>r</span> 对应的 <span class='mj'>Y</span>", "[[T8#p9|Topic 8 第 9 页]]"),
            ("Yˢ 曲线", "N^{s}(w)=N^{d}(w)\\Rightarrow Y_{t}=A_{t}F(K_{t},N_{t})", "劳动市场 + 生产函数 ⇒ **与 <span class='mj'>r</span> 无关，所以竖直**", "[[T8#p14|Topic 8 第 14 页]]"),
            ("一般均衡", "IS\\cap Y^{s}\\ \\Rightarrow\\ (Y_{t},r_{t})", "交点定产出与利率，其余变量是下游", "[[T8#p16|Topic 8 第 16 页]]"),
        ], "六条。**第三条是整门课最重要的一次「解锁」**：从 <span class='mj'>S=0</span> 到 <span class='mj'>S=I</span>。"),

        ("note", "模块五 · 货币（T9）", "装货币只有一个技术难点：**钱不生息，凭什么有人拿着？** 答案是把实际余额写进效用（MIU）。"),
        ("eq", [
            ("MIU 效用", "U=u(C_{t},1-N_{t})+\\nu\\!\\left(\\frac{M_{t}}{P_{t}}\\right)+\\beta(\\cdots)", "**拿着钱本身就舒服**——这是唯一的动机", "[[T9#p4|Topic 9 第 4 页]]"),
            ("Fisher（精确）", "1+r_{t}=\\frac{1+i_{t}}{1+\\pi^{e}_{t+1}}", "**实际 = 名义 ÷ 通胀**；分母是「预期」", "[[T9#p7|Topic 9 第 7 页]]"),
            ("Fisher（近似）", "r_{t}=i_{t}-\\pi^{e}_{t+1}", "小通胀下可用；**考试默认写这条**", "[[T9#p7|Topic 9 第 7 页]]"),
            ("货币需求", "\\nu^{\\prime}\\!\\left(\\frac{M_{t}}{P_{t}}\\right)=\\frac{i_{t}}{1+i_{t}}", "**持有成本是 <span class='mj'>i/(1+i)</span> 不是 <span class='mj'>i</span>**（本讲最难的一步）", "[[T9#p10|Topic 9 第 10 页]]"),
            ("货币市场出清", "M_{t}=P_{t}M^{d}(i_{t},Y_{t})\\ \\Rightarrow\\ P_{t}=\\frac{M_{t}}{M^{d}}", "**物价由「想持多少现金」定**，不是由商品市场定", "[[T9#p15|Topic 9 第 15 页]]"),
            ("货币中性", "M_{t}\\uparrow\\Rightarrow P_{t}\\propto M_{t}", "实际块一个方程都没变 ⇒ **钱只改物价**", "[[T9#p17|Topic 9 第 17 页]]"),
        ], "六条。**第四条是本讲唯一的「推导题」**，一定要会从 FOC 走一遍。"),

        ("note", "模块六 · 粘性与政策（T10）", "把价格假设换掉，整个结论就翻了。**三种 AS 是这个模块的骨架。**"),
        ("eq", [
            ("IS（同 T8）", "Y_{t}=C^{d}(\\cdot)+I^{d}(\\cdot)+G_{t}", "**需求侧与 T8 完全一样**", "[[T10#p6|Topic 10 第 6 页]]"),
            ("LM", "\\frac{M_{t}}{P_{t}}=M^{d}\\!\\left(r_{t}+\\pi^{e}_{t+1},\\ Y_{t}\\right)", "货币市场出清；<b>LM 上移 ⇔ <span class='mj'>P</span> 下降</b>", "[[T10#p8|Topic 10 第 8 页]]"),
            ("AD", "AD=\\{(P_{t},Y_{t}):IS\\cap LM\\}", "**把 (r, Y) 上的交点搬到 (P, Y) 平面**", "[[T10#p13|Topic 10 第 13 页]]"),
            ("新古典 AS（竖直）", "Y_{t}=Y^{f}_{t}", "劳动市场清 ⇒ 产出与 <span class='mj'>P</span> 无关", "[[T10#p17|Topic 10 第 17 页]]"),
            ("简单粘性 AS（水平）", "P_{t}=\\bar P_{t}", "**价格外生** ⇒ 需求全由产量吸收", "[[T10#p21|Topic 10 第 21 页]]"),
            ("部分粘性 AS（上斜）", "P_{t}=\\bar P_{t}+\\gamma(Y_{t}-Y^{f}_{t})", "**<span class='mj'>\\gamma</span> 就是「粘性程度」的旋钮**", "[[T10#p33|Topic 10 第 33 页]]"),
            ("产出缺口", "Y_{t}-Y^{f}_{t}", "正 = 过热；负 = 衰退。**政策只盯它**", "[[T10#p39|Topic 10 第 39 页]]"),
            ("最优政策", "Y_{t}=Y^{f}_{t}\\ \\Longleftrightarrow\\ P_{t}=\\bar P_{t}", "**divine coincidence**：稳物价与补缺口同时达成", "[[T10#p41|Topic 10 第 41 页]]"),
        ], "八条。**第四到第六条是同一条 AS 的三个取值**，比较着记：<span class='mj'>\\gamma=0</span> 水平、<span class='mj'>\\gamma\\to\\infty</span> 竖直。"),

        ("tip", "四十五条怎么背", "**不要平铺着背。** 每一组先记「这一组解决什么问题」，再记「第一条」，最后记「最反常的那一条」。<b>比如模块三：问题是「企业要多少投入」，第一条是工资 = 边际产品，最反常的是「投资需求里资本是负号」。三条一记，一组就下来了。</b>"),
    ],
))

# ---------- §4 图形总表 ----------
SECTIONS.append(dict(
    id="s4", num="四", title="图形总表：十一张图，四个坐标系",
    sub="图画错，通常不是记不住线，而是「轴放反了」或「动的其实不是这条线」。先把坐标系认准。",
    blocks=[
        ("p", "十个模型画了十一张图，但**只有四个平面**。每一张新图，都是把前一张图的某个变量「挪到轴上」。**看懂「挪了哪个变量」，就永远不会把图记混。**"),
        ("cards", [
            dict(title="跨期平面　<span class='mj'>C_{t}</span> × <span class='mj'>C_{t+1}</span>",
                 sub="只有 Topic 4 用",
                 body="横轴今天的消费、纵轴明天的消费。<b>点＝一生的计划</b>，斜率＝跨期价格。<b>这里是「局部均衡」</b>：<span class='mj'>r</span> 从外面给。"),
            dict(title="利率平面　<span class='mj'>Y_{t}</span> × <span class='mj'>r_{t}</span>",
                 sub="IS、Yˢ、LM 都在这里",
                 body="横轴产出、纵轴利率。<b>同一个平面里放三种线</b>：<span class='mj'>IS</span>（下斜）、<span class='mj'>Y^{s}</span>（竖直）、<span class='mj'>LM</span>（上斜）。<b>纵轴永远是「价格」——利率就是钱的价格。</b>"),
            dict(title="劳动平面　<span class='mj'>N_{t}</span> × <span class='mj'>w_{t}</span>",
                 sub="Topic 7 起才出现",
                 body="横轴就业、纵轴工资。<b>两条线（供给、需求）一交叉，<span class='mj'>N</span> 与 <span class='mj'>w</span> 同时定出</b>——这是后面所有「供给面」的源头。"),
            dict(title="物价平面　<span class='mj'>Y_{t}</span> × <span class='mj'>P_{t}</span>",
                 sub="Topic 10 用",
                 body="横轴产出、纵轴物价。AD 下斜、AS 按粘性程度取水平／上斜／竖直。<b>这一张图是本课程最后要交的答卷。</b>"),
        ]),
        ("table", dict(
            caption="十一张图的对照：轴、形状、什么时候动",
            header=["图", "坐标轴（横 × 纵）", "形状", "什么会让它动", "出处"],
            first_bold=True,
            rows=[
                ["45° 图／凯恩斯交叉", "<span class='mj'>Y_{t}</span> × <span class='mj'>Y^{d}_{t}</span>", "支出线斜率＝MPC（小于 1），与 45° 线相交", "↑<span class='mj'>A_{t+1}</span>、↑<span class='mj'>G_{t}</span> 上移；↑<span class='mj'>G_{t+1}</span> 下移", "[[T5#p11|T5 p11]]　[[T8#p8|T8 p8]]"],
                ["IS", "<span class='mj'>Y_{t}</span> × <span class='mj'>r_{t}</span>", "<b>下斜</b>（<span class='mj'>r\\downarrow\\Rightarrow I\\uparrow\\Rightarrow Y\\uparrow</span>）", "任何抬高意愿支出的冲击都<b>右移</b>", "[[T8#p9|T8 p9]]"],
                ["<span class='mj'>Y^{s}</span>", "<span class='mj'>Y_{t}</span> × <span class='mj'>r_{t}</span>", "<b>竖直</b>（与 <span class='mj'>r</span> 无关）", "↑<span class='mj'>A_{t}</span> 右；↑<span class='mj'>\\theta_{t}</span> 左；↓<span class='mj'>K_{t}</span> 左", "[[T8#p14|T8 p14]]"],
                ["劳动市场", "<span class='mj'>N_{t}</span> × <span class='mj'>w_{t}</span>", "需求<b>下斜</b>、供给<b>上斜</b>", "↑<span class='mj'>A_{t}</span>／↑<span class='mj'>K_{t}</span> 使需求右移；↓<span class='mj'>\\theta_{t}</span> 使供给右移", "[[T7#p9|T7 p9]]　[[T7#p20|T7 p20]]"],
                ["生产函数", "<span class='mj'>N_{t}</span> × <span class='mj'>Y_{t}</span>", "上斜、凹", "↑<span class='mj'>A_{t}</span> 整体上移", "[[T8#p13|T8 p13]]"],
                ["投资需求", "<span class='mj'>I_{t}</span> × <span class='mj'>r_{t}</span>", "下斜", "↑<span class='mj'>A_{t+1}</span> 右移；↑<span class='mj'>K_{t}</span> <b>左移</b>", "[[T7#p11|T7 p11]]"],
                ["跨期预算线", "<span class='mj'>C_{t}</span> × <span class='mj'>C_{t+1}</span>", "斜率 <span class='mj'>-(1+r_{t})</span>", "↑<span class='mj'>r</span> <b>绕禀赋点旋转变陡</b>（不是平移）", "[[T4#p15|T4 p15]]"],
                ["货币市场", "<span class='mj'>M_{t}</span> × <span class='mj'>P_{t}</span>", "供给竖线（外生）＋需求过原点的射线", "↑<span class='mj'>M</span> 供给线右移；↑<span class='mj'>Y</span> 需求线变陡", "[[T9#p16|T9 p16]]"],
                ["LM", "<span class='mj'>Y_{t}</span> × <span class='mj'>r_{t}</span>", "<b>上斜</b>", "↑<span class='mj'>M</span> 下移；↑<span class='mj'>\\pi^{e}</span> 下移；↑<span class='mj'>P</span> <b>上移</b>", "[[T10#p8|T10 p8]]"],
                ["AD", "<span class='mj'>Y_{t}</span> × <span class='mj'>P_{t}</span>", "<b>下斜</b>", "IS 右移、或 LM 下移 ⇒ AD 右移", "[[T10#p13|T10 p13]]"],
                ["AS（三种）", "<span class='mj'>Y_{t}</span> × <span class='mj'>P_{t}</span>", "水平（<span class='mj'>\\gamma=0</span>）／上斜（斜率 <span class='mj'>\\gamma</span>）／竖直（<span class='mj'>\\gamma\\to\\infty</span>）", "三个模型各自<b>固定</b>一种形状，不是「移动」", "[[T10#p17|T10 p17]]"],
            ],
            note="**读这张表只读两列**：「坐标轴」告诉你这是哪个平面，「什么会让它动」告诉你考场要写什么。中间的「形状」是推导结果，忘了可以现推。",
        )),
        ("note", "三种「竖直」不是一回事", "全课有三条线是竖直的，**理由完全不同，最爱在这里出辨析题**：<br>① <b>Topic 5 的 <span class='mj'>Y^{s}</span></b>：因为 <span class='mj'>Y_{t}</span> <b>本来就是外生给的</b>（禀赋），跟 <span class='mj'>r</span> 自然无关；<br>② <b>Topic 8 的 <span class='mj'>Y^{s}</span></b>：<span class='mj'>Y</span> 是生产出来的，但 <b>GHH 偏好让劳动供给只依赖 <span class='mj'>w</span></b>（<span class='mj'>C</span> 约掉了），于是 <span class='mj'>N</span>、<span class='mj'>Y</span> 与 <span class='mj'>r</span> 脱钩；<br>③ <b>Topic 10 的新古典 AS</b>：劳动市场出清定出 <span class='mj'>N</span>，且<b>物价不进入任何实际方程</b>，所以 <span class='mj'>Y</span> 与 <span class='mj'>P</span> 无关。<br><b>判据：题目里 <span class='mj'>Y</span> 是「给的」还是「产出的」？前者是 ①，后者是 ② 或 ③。</b>"),
        ("warn", "图形题的三个固定扣分点", "① <b>把「沿曲线移动」写成「曲线移动」</b>——问 <span class='mj'>r</span> 变导致 <span class='mj'>Y</span> 变，那是沿 IS 走，不是 IS 移；<br>② <b><span class='mj'>Y^{s}</span> 右移后忘了 <span class='mj'>r</span> 也变</b>——供给冲击里 <span class='mj'>r</span> 是<b>被解出来</b>的，不是不动；<br>③ <b>画 AD-AS 时只动 AD</b>——<span class='mj'>P</span> 一变，<b>LM 跟着动</b>，这才是 AD 下斜的原因。"),
        ("tip", "一张图记住全部移动", "**纵轴是谁，谁就是「价格」；价格上涨，需求收缩、供给扩张。** 把这句话套到四个平面上，十一条结论全部对得上：<span class='mj'>r</span> 涨 ⇒ 投资需求降；<span class='mj'>w</span> 涨 ⇒ 劳动需求降；<span class='mj'>P</span> 涨 ⇒ 实际余额降 ⇒ <span class='mj'>r</span> 涨 ⇒ 产出降。"),
    ],
))

# ---------- §5 主线串联 ----------
SECTIONS.append(dict(
    id="s5", num="五", title="一条主线：消费函数被装配了七次",
    sub="整门课只有一件零件从头用到尾。看清它被改了哪一次、又在哪里原封不动地出现，十讲就串成一条线了。",
    blocks=[
        ("p", "回头看第 2 节那张表，你会发现一个奇怪的事实：**从 Topic 4 到 Topic 10，消费函数只被改过「一次」**。其余六次，它的形式一个字都没动——动的只是「它被放进哪个方程组」。"),
        ("big", "**七次装配，一次改型**：<span class='mj'>C_{t}=C^{d}(Y_{t},Y_{t+1},r_{t})</span> 在 Topic 4 出生，在 Topic 6 因为「税被看穿」变成 <span class='mj'>C^{d}(Y_{t}-G_{t},\\,Y_{t+1}-G_{t+1},\\,r_{t})</span>，此后一直到 Topic 10 再没变过。"),
        ("table", dict(
            caption="消费函数的七次装配",
            header=["工位", "消费函数此刻长什么样", "这一步新加了什么", "于是谁被解出来", "出处"],
            first_bold=True,
            rows=[
                ["<b>T4 出生</b>", "<span class='mj'>C^{d}(Y_{t}^{+},Y_{t+1}^{+},r_{t}^{-})</span>", "一个最优化问题 ＋ IBC", "<span class='mj'>C_{t},C_{t+1},S_{t}</span>", "[[T4#p18|T4 p18]]"],
                ["<b>T5 进市场</b>", "同上（<b>形式不变</b>）", "市场出清 <span class='mj'>S_{t}=0</span>", "<b><span class='mj'>r_{t}</span></b>", "[[T5#p9|T5 p9]]"],
                ["<b>T6 加政府</b>", "<span class='mj'>C^{d}(Y_{t}-G_{t},\\ Y_{t+1}-G_{t+1},\\ r_{t})</span>", "政府 IBC 把 <span class='mj'>T</span> 的现值换成 <span class='mj'>G</span> 的现值", "<span class='mj'>C_{t},r_{t}</span>（<span class='mj'>T,B</span> 消失）", "[[T6#p8|T6 p8]]"],
                ["<b>T7 加生产</b>", "同上（<b>一个字没改</b>）", "企业 ＋ 劳动市场：<span class='mj'>Y</span> 从「禀赋」变成「生产出来」", "<span class='mj'>Y,N,w,r,C,I</span>", "[[T7#p22|T7 p22]]"],
                ["<b>T8 压成线</b>", "代入 <span class='mj'>Y^{d}=C^{d}+I^{d}+G</span>", "六条方程压成两条线", "<span class='mj'>Y_{t},r_{t}</span>（交点）", "[[T8#p9|T8 p9]]"],
                ["<b>T9 不动</b>", "完全没有变化", "只加名义块（<span class='mj'>M</span>、<span class='mj'>P</span>、<span class='mj'>i</span>）", "外加 <span class='mj'>P_{t},i_{t}</span>", "[[T9#p15|T9 p15]]"],
                ["<b>T10 装上 AD</b>", "同上（<b>仍然没改</b>）", "IS ＋ LM ⇒ AD", "<span class='mj'>P_{t},Y_{t}</span>（联立）", "[[T10#p13|T10 p13]]"],
            ],
            note="**七行里只有第三行改动了式子。** 这就是整门课最省力的一条记忆线：其余六次都只是「换地方用」。",
        )),
        ("note", "为什么只改这一次", "因为政府进入家庭的方式**不是改变偏好，而是改变可支配收入**。Topic 6 做的事只有一步：把家庭 IBC 里的「税收现值」用政府 IBC 替换成「支出<b>减</b>初始债务」。于是「税前收入 <span class='mj'>Y</span>」变成「税后收入 <span class='mj'>Y-G</span>」，**偏好、欧拉方程、IBC 的结构一律不动**。<b>这就是李嘉图等价的代数来源</b>：<span class='mj'>T</span> 被完全替换掉了，所以「怎么融资」在式子里根本看不到。"),
        ("warn", "最容易被扣分的写法", "**把消费函数写成单变量 <span class='mj'>C(Y)</span>。** 在 Topic 1–3 里，「消费是收入的固定比例」是一个<b>假设</b>（因为那时家庭不做最优化）；从 Topic 4 起它<b>变成结论</b>，必须带三个自变量。<b>考卷上写 <span class='mj'>C=C(Y)</span> 会被判为「不知道消费函数从哪来」，写 <span class='mj'>C=C(Y-T)</span> 会被判为「不知道李嘉图等价」。</b>"),
        ("note", "利率的符号为什么「有条件」", "<span class='mj'>\\partial C^{d}/\\partial r&lt;0</span> 这条**只对储蓄者成立**（替代效应占优）。对<b>借款人</b>，利率上升等于「收入变少」，收入效应反向，净效应<b>符号不定</b>。<b>所以答题时必须加一句「假设替代效应占优」，否则这个负号是没根据的。</b>（[[T4#p24|Topic 4 第 24 页]]画借款人、[[T4#p27|第 27 页]]画储蓄者，两页对照着看）"),
        ("tip", "这条主线怎么用", "**任何一道「某冲击对消费的影响」的题，都从这七行里找位置**：先问「现在在哪个模型」，就知道该不该让 <span class='mj'>r</span> 变、该不该让 <span class='mj'>Y</span> 变。<b>Topic 5/6 里 <span class='mj'>Y</span> 外生、<span class='mj'>r</span> 内生；Topic 8/9 里 <span class='mj'>Y</span> 由供给定、<span class='mj'>r</span> 内生；Topic 10 里 <span class='mj'>Y</span> 由需求定。同一个 <span class='mj'>\\uparrow G_{t}</span>，在三个地方结论完全不同，原因就在这里。</b>"),
    ],
))

# ---------- §6 十六组易混辨析 ----------
SECTIONS.append(dict(
    id="s6", num="六", title="十六组易混：把错位的结论搬回原位",
    sub="这一节是全篇最值钱的部分。十讲的易错清单共 175 条，去重之后真正会「跨讲串味」的只有这十六组。",
    blocks=[
        ("p", "**每一组的第三列都是「判据」**——考场上不需要回忆结论，只需要问自己那一个问题，答案就唯一了。"),
        ("table", dict(
            caption="十六组易混：错在哪、怎么判",
            cls="table pit",
            header=["易混的一对（或一组）", "常见错误", "正解与判据"],
            first_bold=True,
            rows=[
                ["① 水平效应 vs 增长效应", "认为提高储蓄率能永久提高增长率", "<b>↑<span class='mj'>s</span> 只提高水平</b>：路径上一段高增长，随后回到零增长。<b>判据：有没有变量在稳态还在长？</b>"],
                ["② <span class='mj'>S=0</span>（T5）vs <span class='mj'>S=I</span>（T7）", "在 Topic 5 的题里写 <span class='mj'>S=I</span>", "T5 没有投资品，储蓄只能归零；T7 有企业，储蓄变成资本。<b>判据：模型里有没有 <span class='mj'>K</span> 与 <span class='mj'>I</span>？</b>"],
                ["③ 乘数为零 vs 乘数为正", "把「乘数为零」当成全课结论", "只在<b>产出不能变</b>时成立（T6 禀赋、T8/T9 竖直 <span class='mj'>Y^{s}</span>）。T10 粘性下乘数<b>为正</b>。<b>判据：AS 竖不竖？</b>"],
                ["④ 欧拉方程 vs IBC", "以为欧拉方程能算出 <span class='mj'>C_{t}</span> 的具体数值", "欧拉只定<b>比例</b> <span class='mj'>C_{t+1}/C_{t}</span>，水平必须由 IBC 补。<b>判据：一个方程能不能解两个未知数？</b>"],
                ["⑤ <span class='mj'>Y^{s}</span> 竖直的三个理由", "一律回答「因为 <span class='mj'>Y</span> 外生」", "T5 是<b>真外生</b>；T8 是 <b>GHH 让 <span class='mj'>N</span> 只依赖 <span class='mj'>w</span></b>；T10 新古典是<b>劳动市场出清 ＋ <span class='mj'>P</span> 不进实际块</b>。<b>判据：<span class='mj'>Y</span> 是给的还是产出的？</b>"],
                ["⑥ <span class='mj'>K_{t}</span> 的符号", "以为两张图里同号", "劳动需求里 <span class='mj'>K_{t}</span> <b>正</b>（<span class='mj'>F_{KN}>0</span>）；投资需求里 <span class='mj'>K_{t}</span> <b>负</b>（已有很多资本就不必再买）。<b>判据：边际产品，还是重置需求？</b>"],
                ["⑦ 局部均衡 vs 一般均衡", "在 Topic 4 里就把 <span class='mj'>r</span> 当成内生", "T4 的 <span class='mj'>r</span> 是<b>外部给定的市场价格</b>；T5 起 <span class='mj'>r</span> 由市场出清解出。<b>判据：<span class='mj'>r</span> 有没有一条自己的方程？</b>"],
                ["⑧ 实际利率 <span class='mj'>r</span> vs 名义利率 <span class='mj'>i</span>", "说「货币中性，所以利率不变」", "中性说的是 <b><span class='mj'>r</span> 不变</b>；<span class='mj'>i</span> 与 <span class='mj'>P</span> <b>同比例上升</b>。<b>判据：Fisher 方程 <span class='mj'>r=i-\\pi^{e}</span>。</b>"],
                ["⑨ 完全挤出 vs 不挤出", "以为任何模型都完全挤出", "T8／T10 新古典：<b>完全挤出</b>（<span class='mj'>Y</span> 不变，只有 <span class='mj'>r</span> 升）；T10 粘性：<b>部分或不挤出</b>。<b>判据：<span class='mj'>Y</span> 能不能变？</b>"],
                ["⑩ ↑<span class='mj'>A_{t}</span> 在三种 AS 下", "以为供给冲击总是「增产降物价」", "简单粘性：<b><span class='mj'>Y</span> 完全不动，<span class='mj'>N</span> 与 <span class='mj'>w</span> 反而下降</b>（紧缩效应）；新古典：<span class='mj'>Y</span> 升、<span class='mj'>N</span> 升。<b>判据：劳动需求在不在模型里？</b>"],
                ["⑪ 利率上升对消费", "一律说消费下降", "对<b>储蓄者</b>替代效应占优 ⇒ 消费降；对<b>借款人</b>符号不定。<b>判据：禀赋点落在最优点的哪一侧？</b>"],
                ["⑫ ↑<span class='mj'>G_{t}</span> vs ↑<span class='mj'>G_{t+1}</span>", "以为两者都让 IS 右移", "<span class='mj'>G_{t}</span> <b>右移</b>（需求直接加一项）；<span class='mj'>G_{t+1}</span> <b>左移</b>（未来税负 ⇒ 负财富效应 ⇒ 今天少花）。<b>判据：<span class='mj'>G</span> 出现在哪一期？</b>"],
                ["⑬ 减税 vs 增支", "以为减税能刺激消费", "<b>李嘉图等价</b>：<span class='mj'>T</span> 被完全看穿，只有 <span class='mj'>G</span> 的现值重要——同额减税与借债融资<b>效果完全相同</b>。<b>判据：政府 IBC 有没有被代进家庭约束？</b>"],
                ["⑭ 「粘性」粘的是什么", "答成「工资粘性」", "这三个模型粘的是<b>产品价格 <span class='mj'>P</span></b>。实际工资仍由劳动市场（或由 <span class='mj'>N</span> 反解）决定。<b>判据：哪一种方程被删掉了？</b>"],
                ["⑮ <span class='mj'>\\gamma</span> 的方向", "以为 <span class='mj'>\\gamma</span> 大＝价格更粘", "<b><span class='mj'>\\gamma</span> 越大＝价格越灵活＝AS 越陡</b>；<span class='mj'>\\gamma=0</span> 才是完全粘（水平线）。<b>判据：把 <span class='mj'>\\gamma</span> 代 0 与代 ∞ 各试一遍。</b>"],
                ["⑯ 预期通胀 ↑", "以为 LM 上移、物价下跌", "<span class='mj'>\\pi^{e}\\uparrow</span> ⇒ 给定 <span class='mj'>i</span> 下 <span class='mj'>r\\downarrow</span> ⇒ 投资↑ ⇒ <b>LM 下移</b>、AD 右移、<b><span class='mj'>P</span> 上升</b>。<b>判据：Fisher 里 <span class='mj'>r</span> 与 <span class='mj'>\\pi^{e}</span> 反向。</b>"],
            ],
            note="**必考级的是 ②③⑤⑩⑮**——这五组的共同点是「同一个符号，在两讲里意思不同」。**其余的只要记住判据那一句就够了，不必背结论。**",
        )),
        ("note", "为什么「跨讲串味」比「不会」更致命", "不会做，最多丢一道题的分；<b>串味则会「答得很有条理但方向全错」</b>——判卷人看到你把 Topic 6 的结论搬到 Topic 10 的题上，会认为你<b>不理解模型边界</b>，那是更重的扣分。<b>所以每道题动笔前先花十秒：这是哪块大陆？产出能不能变？<span class='mj'>r</span> 是给的还是解的？</b>"),
        ("tip", "十六条怎么在考前一天过一遍", "**只看第一列和第三列的句号前那半句。** 十六句话，五分钟扫完：<b>水平不是增长、<span class='mj'>S=0</span> 是没投资、乘数看 AS、欧拉定比例、竖直三理由、<span class='mj'>K</span> 一正一负、T4 是局部、<span class='mj'>r</span> 不变 <span class='mj'>i</span> 变、挤出看 <span class='mj'>Y</span>、供给冲击看劳动需求、利率看储蓄者、<span class='mj'>G</span> 看哪期、税被看穿、粘的是 <span class='mj'>P</span>、<span class='mj'>\\gamma</span> 大更灵活、<span class='mj'>\\pi^{e}</span> 使 LM 下移。</b>"),
    ],
))

# ---------- §7 四张必背表 ----------
SECTIONS.append(dict(
    id="s7", num="七", title="四张表：考场默写用",
    sub="这四张表建议单独打印。但先看清楚一件事——它们不是四张表，是「一张表长出来的」。",
    blocks=[
        ("warn", "先别背", "**这四张表加起来有 60 多个格子，硬背必忘。** 正确用法是：**平时靠推，考前 48 小时靠它校验**。推的时候只要三个信息——冲击动了哪条线、<span class='mj'>Y</span> 能不能变、<span class='mj'>r</span> 往哪走——剩下的格子是算出来的。"),
        ("note", "四张表其实是一张", "**Topic 9 的表 ＝ Topic 8 的表 ＋ 两行（<span class='mj'>i,P</span>）＋ 两列（<span class='mj'>M,\\pi^{e}</span>）。** 前 6 行 × 前 5 列**完全一样**——因为「货币中性」的意思就是「实际块一个格子都不变」。**Topic 10 的九情形表**则是把「一张表」按 AS 的形状切成三段。<b>看懂这个结构，四张表就只剩一张要记。</b>"),
        ("table", dict(
            caption="表一 · Topic 8：实物侧定性效应（6 变量 × 5 冲击）",
            cls="table ctr",
            header=["变量", "↑<span class='mj'>A_{t}</span>", "↑<span class='mj'>\\theta_{t}</span>", "↑<span class='mj'>A_{t+1}</span>", "↑<span class='mj'>G_{t}</span>", "↑<span class='mj'>G_{t+1}</span>"],
            first_bold=True,
            rows=[
                ["<span class='mj'>Y_{t}</span>", "<b>+</b>", "<b>−</b>", "0", "0", "0"],
                ["<span class='mj'>C_{t}</span>", "<b>+</b>", "<b>−</b>", "?", "<b>−</b>", "<b>−</b>"],
                ["<span class='mj'>I_{t}</span>", "<b>+</b>", "<b>−</b>", "?", "<b>−</b>", "<b>+</b>"],
                ["<span class='mj'>N_{t}</span>", "<b>+</b>", "<b>−</b>", "0", "0", "0"],
                ["<span class='mj'>w_{t}</span>", "<b>+</b>", "<b>+</b>", "0", "0", "0"],
                ["<span class='mj'>r_{t}</span>", "<b>−</b>", "<b>+</b>", "<b>+</b>", "<b>+</b>", "<b>−</b>"],
            ],
            note="[[T8#p24|Topic 8 第 24 页]]原表。**只有 <span class='mj'>A_{t+1}</span> 这一列的 <span class='mj'>C,I</span> 是问号**——因为它是「未来」冲击，符号依赖参数，课件也不给。<b>考场上写「符号不定，取决于替代与收入效应的大小」就是满分。</b>",
        )),
        ("table", dict(
            caption="表二 · Topic 9：加上名义侧（8 变量 × 7 冲击）",
            cls="table ctr",
            header=["变量", "↑<span class='mj'>A_{t}</span>", "↑<span class='mj'>\\theta_{t}</span>", "↑<span class='mj'>A_{t+1}</span>", "↑<span class='mj'>G_{t}</span>", "↑<span class='mj'>G_{t+1}</span>", "↑<span class='mj'>M_{t}</span>", "↑<span class='mj'>\\pi^{e}</span>"],
            first_bold=True,
            rows=[
                ["<span class='mj'>Y_{t}</span>", "<b>+</b>", "<b>−</b>", "0", "0", "0", "0", "0"],
                ["<span class='mj'>C_{t}</span>", "<b>+</b>", "<b>−</b>", "?", "<b>−</b>", "<b>−</b>", "0", "0"],
                ["<span class='mj'>I_{t}</span>", "<b>+</b>", "<b>−</b>", "?", "<b>−</b>", "<b>+</b>", "0", "0"],
                ["<span class='mj'>N_{t}</span>", "<b>+</b>", "<b>−</b>", "0", "0", "0", "0", "0"],
                ["<span class='mj'>w_{t}</span>", "<b>+</b>", "<b>+</b>", "0", "0", "0", "0", "0"],
                ["<span class='mj'>r_{t}</span>", "<b>−</b>", "<b>+</b>", "<b>+</b>", "<b>+</b>", "<b>−</b>", "0", "0"],
                ["<span class='mj'>i_{t}</span>", "<b>−</b>", "<b>+</b>", "<b>+</b>", "<b>+</b>", "<b>−</b>", "0", "<b>+</b>"],
                ["<span class='mj'>P_{t}</span>", "<b>−</b>", "<b>+</b>", "<b>+</b>", "<b>+</b>", "<b>−</b>", "<b>+</b>", "<b>+</b>"],
            ],
            note="前 6 行前 5 列与表一**逐格相同**。<b>最后两列最值钱</b>：<span class='mj'>M</span> 只动 <span class='mj'>P</span>（其余全 0，这就是货币中性）；<span class='mj'>\\pi^{e}</span> 动 <span class='mj'>i</span> 与 <span class='mj'>P</span>，<b><span class='mj'>r</span> 不动</b>。见 [[T9#p23|Topic 9 第 23 页]]。",
        )),
        ("table", dict(
            caption="表三 · Topic 10：九种情形（三个模型 × 三种冲击）",
            cls="table ctr",
            header=["模型", "冲击", "<span class='mj'>P_{t}</span>", "<span class='mj'>Y_{t}</span>", "<span class='mj'>r_{t}</span>", "<span class='mj'>N_{t}</span>", "<span class='mj'>w_{t}</span>", "缺口"],
            first_bold=True,
            rows=[
                "简单粘性（γ = 0）· AS 水平",
                ["简单粘性", "↑<span class='mj'>M_{t}</span>", "0", "<b>+</b>", "<b>−</b>", "<b>+</b>", "<b>+</b>", "<b>+</b>"],
                ["简单粘性", "↑IS（含 ↑<span class='mj'>G_{t}</span>）", "0", "<b>+</b>", "<b>+</b>", "<b>+</b>", "<b>+</b>", "<b>+</b>"],
                ["简单粘性", "↑<span class='mj'>A_{t}</span>", "0", "0", "0", "<b>−</b>", "<b>−</b>", "<b>−</b>"],
                "部分粘性（0 &lt; γ &lt; ∞）· AS 上斜",
                ["部分粘性", "↑<span class='mj'>M_{t}</span>", "<b>+</b>", "<b>+</b>", "<b>−</b>", "<b>+</b>", "<b>+</b>", "<b>+</b>"],
                ["部分粘性", "↑IS（含 ↑<span class='mj'>G_{t}</span>）", "<b>+</b>", "<b>+</b>", "<b>+</b>", "<b>+</b>", "<b>+</b>", "<b>+</b>"],
                ["部分粘性", "↑<span class='mj'>A_{t}</span>", "<b>−</b>", "<b>+</b>", "<b>−</b>", "?", "?", "<b>−</b>"],
                "新古典（γ → ∞）· AS 竖直",
                ["新古典", "↑<span class='mj'>M_{t}</span>", "<b>+</b>", "0", "0", "0", "0", "0"],
                ["新古典", "↑IS（含 ↑<span class='mj'>G_{t}</span>）", "<b>+</b>", "0", "<b>+</b>", "0", "0", "0"],
                ["新古典", "↑<span class='mj'>A_{t}</span>", "<b>−</b>", "<b>+</b>", "<b>−</b>", "<b>+</b>", "<b>+</b>", "0"],
            ],
            note="[[T10#p31|Topic 10 第 31 页]]原表。**读法：先看 <span class='mj'>Y_{t}</span> 那一列**——它在简单粘性下随需求走、在新古典下恒为 0，**这一列就是三个模型的全部差别**；其余各列都是它的下游。",
        )),
        ("table", dict(
            caption="表四 · 三种粘性程度对照：同一条 AS，三个 γ",
            header=["维度", "简单粘性 <span class='mj'>\\gamma=0</span>", "部分粘性 <span class='mj'>0&lt;\\gamma&lt;\\infty</span>", "新古典 <span class='mj'>\\gamma\\to\\infty</span>"],
            first_bold=True,
            rows=[
                ["<b>价格</b>", "<b>外生给定</b> <span class='mj'>\\bar P</span>，与 <span class='mj'>Y</span> 无关", "部分内生：随缺口调整", "<b>完全内生</b>，即时出清"],
                ["<b>AS 形状</b>", "<b>水平线</b>（高度 <span class='mj'>\\bar P</span>）", "<b>正斜率</b>（斜率 <span class='mj'>\\gamma</span>），过 <span class='mj'>(Y^{f},\\bar P)</span>", "<b>竖直线</b>（位于 <span class='mj'>Y^{f}</span>）"],
                ["<b>供给侧方程</b>", "劳动供给、<span class='mj'>P=\\bar P</span>、生产函数（<b>删掉劳动需求</b>）", "劳动供给、<span class='mj'>P=\\bar P+\\gamma(Y-Y^{f})</span>、生产函数", "劳动供给、劳动需求、生产函数（<b>三条都在</b>）"],
                ["<b>求解顺序</b>", "AD 定 <span class='mj'>Y</span> → 反解 <span class='mj'>N</span> → 反解 <span class='mj'>w</span>", "AD 与 AS 同时定 <span class='mj'>(P,Y)</span>", "劳动市场定 <span class='mj'>N</span> → 定 <span class='mj'>Y</span> → AD 定 <span class='mj'>P</span>"],
                ["<b>一个需求冲击</b>", "<span class='mj'>Y</span> 大幅变动，<b><span class='mj'>P</span> 完全不变</b>", "<span class='mj'>Y</span> 与 <span class='mj'>P</span> <b>都动</b>，比例由 <span class='mj'>\\gamma</span> 定", "<span class='mj'>Y</span> 不变，<b><span class='mj'>P</span> 全部吸收</b>"],
                ["<b>一个供给冲击</b>", "<span class='mj'>Y</span> <b>完全不动</b>，<span class='mj'>N,w</span> <b>下降</b>", "<span class='mj'>Y</span> 升但<b>不到 <span class='mj'>Y^{f}</span></b>，<span class='mj'>N,w</span> 方向不定", "<span class='mj'>Y</span> 升到 <span class='mj'>Y^{f}</span>，<span class='mj'>N,w</span> <b>上升</b>"],
                ["<b>货币中性</b>", "<b>非中性</b>（效应最大）", "<b>部分非中性</b>", "<b>中性</b>"],
                ["<b>效率</b>", "无效率（价格没出清）", "部分无效率", "有效率（帕累托最优）"],
                ["<b>政策空间</b>", "最大", "存在", "<b>没有</b>（缺口恒为零）"],
                ["<b>一句话</b>", "「需求说了算，产量全吸收」", "「物价与产量分摊冲击」", "「供给说了算，物价全吸收」"],
            ],
            note="这张表是**三道论述题的答案骨架**：问「财政政策在什么条件下有效」，答的就是这张表的需求冲击行；问「货币是否中性」，答的就是第七行；问「供给冲击为什么在衰退里出现」，答的是第六行的第一格。",
        )),
        ("tip", "默写时只默三格", "如果时间不够，**只默这三格**：① 新古典 + 需求冲击 ⇒ <span class='mj'>Y</span> 不变、<span class='mj'>r</span> 升（完全挤出）；② 简单粘性 + 供给冲击 ⇒ <span class='mj'>Y</span> 不动、<span class='mj'>N</span> 降（紧缩效应）；③ 部分粘性 + 货币冲击 ⇒ <span class='mj'>P,Y</span> 同升。<b>这三格记住了，剩下六个格子可以从「<span class='mj'>\\gamma</span> 在两端之间」推出来。</b>"),
    ],
))

# ---------- §8 答题模板 ----------
SECTIONS.append(dict(
    id="s8", num="八", title="答题模板：三种题型，三套动作",
    sub="同一套库存，三种取用方式。模板的作用不是「套话」，而是保证你不漏掉判卷人要看的那几步。",
    blocks=[
        ("p", "期末三道大题基本是这三种之一（或组合）。**每一步都对应一个给分点**，所以宁可写得短，也不要跳过任何一步。"),
        ("note", "模板一 · 比较静态（「如果 X 上升，各变量怎么变」）", "这是最常见、也最容易拿满分的题型。**六步走完，一分不丢。**"),
        ("steps", [
            ("圈出「变了什么」", "题干里那个外生变量，**先在草稿上写成「↑<span class='mj'>A_{t}</span>」这样的符号**，不要用文字描述。<b>这一步错了，后面全错，所以要慢。</b>"),
            ("判断时间尺度", "「长期／稳态」⇒ T2–T3；「一生／跨期」⇒ T4；「今年／本期内」⇒ T8–T10。<b>这一步决定你用哪块大陆的模型。</b>"),
            ("写内生量清单", "把该模型要解的变量<b>全部列出来</b>（T8 是六个、T9 是八个）。<b>列清单本身就是给分点</b>——它证明你知道模型有几个未知数。"),
            ("找「第一块多米诺」", "问：这个冲击<b>直接进入哪一条方程</b>？是需求函数、供给函数，还是约束？<b>只有一条方程会被直接推动</b>，其余都是间接的。"),
            ("顺着链条走", "从第一块多米诺推到最后一个：<span class='mj'>r\\to I\\to Y</span>，或 <span class='mj'>Y\\to N\\to w</span>。<b>每一步都要说「为什么」，而不是只给符号。</b>"),
            ("回表核对", "拿 [[s7|第 7 节的表]] 对一遍。<b>如果有一个格子对不上，说明链条断了一环</b>——通常是漏了「<span class='mj'>r</span> 也会变」或「<span class='mj'>Y</span> 根本不变」。"),
        ]),
        ("note", "模板二 · 图形题（「画图说明」）", "图形题的分数一半在图上、一半在话上。**图只画三条线，话要说清两个交点。**"),
        ("steps", [
            ("先写坐标轴", "**纵轴永远是「价格」**（<span class='mj'>r</span>、<span class='mj'>w</span>、<span class='mj'>P</span>），横轴永远是「量」（<span class='mj'>Y</span>、<span class='mj'>N</span>、<span class='mj'>M</span>）。写错轴，全图作废。"),
            ("画初始均衡", "标出交点与两个坐标值 <span class='mj'>(Y_{0},r_{0})</span>。<b>不标数值的图会被认为「没有均衡概念」。</b>"),
            ("说「哪条线动、往哪动」", "用箭头画出来。<b>同时明确说「另一条不动」</b>——这一句是给分点，因为考试就考你分不分得清 shift 与 movement along。"),
            ("说「为什么动」", "一句话机制，**必须含一个符号变化**：「<span class='mj'>A_{t}</span> 上升 ⇒ 劳动的边际产品上升 ⇒ 劳动需求右移」。"),
            ("读新交点，并沿链条说完", "新的 <span class='mj'>(Y_{1},r_{1})</span> 读出来，然后<b>不要停在交点</b>：继续说到 <span class='mj'>N</span>、<span class='mj'>w</span>、<span class='mj'>C</span>、<span class='mj'>I</span>。<b>多面版题的分数几乎全在这一步。</b>"),
        ]),
        ("note", "模板三 · 论述题（「某结论在什么条件下成立」）", "论述题考的不是知识量，是**边界感**：你知道这个结论什么时候会破。"),
        ("steps", [
            ("立论：把结论写成可证伪的一句话", "「在 <b>X 假设</b>下，<b>Y 不变</b>」。<b>不要写成「讨论一下……」</b>——那句话没法判分。"),
            ("论证：用方程推，不要用形容词", "两三条式子足够：约束 → 一阶条件 → 出清。<b>每写一条，加半句白话翻译。</b>"),
            ("破题：指出「如果 X 不成立会怎样」", "<b>这是高分与及格的分界线。</b>比如「若价格粘住，<span class='mj'>Y</span> 不再由供给定，乘数由 0 变为正，结论反转——这就是 Topic 10 存在的理由」。"),
        ]),
        ("table", dict(
            caption="题干里的词 → 该用哪个模型",
            header=["题干里的词", "用哪个模型", "一句话理由"],
            first_bold=True,
            rows=[
                ["「长期」「稳态」「增长」「收敛」", "T2–T3 Solow", "时间尺度以十年计，价格不出现"],
                ["「一生」「跨期」「借贷约束」「欧拉」", "T4", "只有这一讲同时有 <span class='mj'>C_{t}</span> 与 <span class='mj'>C_{t+1}</span>"],
                ["「利率被决定」「储蓄归零」", "T5", "没有投资品，<span class='mj'>S</span> 只能为 0"],
                ["「政府支出」「赤字」「减税」「李嘉图」", "T6", "政府 IBC 把 <span class='mj'>T</span> 消掉"],
                ["「企业」「劳动需求」「投资需求」「股息」", "T7", "只有这一讲有生产与要素市场"],
                ["「画出 IS」「供给面」「一般均衡」", "T8", "六条方程压成两条线"],
                ["「货币中性」「通胀」「物价水平」", "T9", "只有这一讲有名义块"],
                ["「衰退」「政策有效」「价格粘性」「缺口」", "T10", "AS 不竖直，需求能改产量"],
                ["「挤出」", "T8／T9 看完全挤出，T10 看部分", "判据：<span class='mj'>Y</span> 能不能变"],
            ],
            note="**这张表是「第一分钟」用的**：读完题先在草稿上写下模型编号，再动笔。**写错模型的代价是整题作废，而不是扣几分。**",
        )),
        ("warn", "三个通用的扣分点", "① **只给符号不给机制**（「<span class='mj'>Y</span> 上升」——为什么？）；② **把内生量当外生量用**（在 T5 里把 <span class='mj'>r</span> 当参数、在 T8 里把 <span class='mj'>Y</span> 当参数）；③ **结论与图形不一致**（图上画的是左移，文字写的是上升）。<b>第③条最冤——写完检查一遍图和字对不对得上。</b>"),
    ],
))

# ---------- §9 自测清单 ----------
SECTIONS.append(dict(
    id="s9", num="九", title="自测清单：二十四问，三档",
    sub="每题只问「答不上来说明什么」——因为复习的终点不是「都看过」，而是「知道哪里还漏」。",
    blocks=[
        ("p", "分三档：**能背（8 题）**检验公式与定义；**能推（8 题）**检验机制；**能画（8 题）**检验图形。**答不上来的题，右边一栏直接告诉你回哪一节。**"),
        ("table", dict(
            caption="第一档 · 能背：公式与定义",
            cls="table",
            header=["问题", "答不上来说明什么", "回看"],
            first_bold=True,
            rows=[
                ["① 稳态条件是什么？为什么它意味着「增长率归零」而不是「产出归零」？", "把「<span class='mj'>\\Delta k=0</span>」与「<span class='mj'>y=0</span>」混为一谈", "[[s3|§3 模块一]]"],
                ["② 欧拉方程与 IBC 各定什么？", "以为欧拉方程能定出消费的<b>水平</b>", "[[s6|§6 第 ④ 组]]"],
                ["③ 消费函数三个自变量的符号分别是什么？哪一个有前提？", "忘了 <span class='mj'>r</span> 的符号只对储蓄者成立", "[[s5|§5]]"],
                ["④ 企业的三条一阶条件分别是什么？", "记不住投资条件里「<span class='mj'>1-\\delta</span>」的位置", "[[s3|§3 模块三]]"],
                ["⑤ GHH 偏好推出什么结论？", "说不出「<span class='mj'>N</span> 只依赖 <span class='mj'>w</span>」", "[[s3|§3 模块三]]"],
                ["⑥ Fisher 方程的精确式与近似式？分母是哪个变量？", "把分母写成 <span class='mj'>1+\\pi</span> 而不是 <span class='mj'>1+\\pi^{e}</span>", "[[s3|§3 模块五]]"],
                ["⑦ 持有货币的成本是什么？为什么不是 <span class='mj'>i</span>？", "没记住 <span class='mj'>i/(1+i)</span> 这一步", "[[s3|§3 模块五]]"],
                ["⑧ 三种 AS 的方程各是什么？<span class='mj'>\\gamma</span> 是什么？", "不知道 <span class='mj'>\\gamma</span> 是<b>斜率</b>", "[[s6|§6 第 ⑮ 组]]"],
            ],
            note="**这一档答不上来，说明公式没进手**——只能靠抄写，不能靠理解。建议把 §3 的四十五行抄一遍。",
        )),
        ("table", dict(
            caption="第二档 · 能推：机制",
            cls="table",
            header=["问题", "答不上来说明什么", "回看"],
            first_bold=True,
            rows=[
                ["⑨ 为什么 Topic 5 的储蓄必须是零？", "没意识到「没有投资品」这个前提", "[[s6|§6 第 ② 组]]"],
                ["⑩ 为什么 Topic 8 的 <span class='mj'>Y^{s}</span> 是竖直的？", "说不出 GHH 那一步", "[[s4|§4 三种竖直]]"],
                ["⑪ ↑<span class='mj'>G_{t}</span> 与 ↑<span class='mj'>G_{t+1}</span> 为什么让 IS 反向移动？", "只记结论，没有「负财富效应」这一环", "[[s6|§6 第 ⑫ 组]]"],
                ["⑫ 货币为什么中性？机制是什么？", "只会说「价格同比例上升」，说不出「实际块一条方程都没变」", "[[s3|§3 模块五]]"],
                ["⑬ 为什么简单粘性下乘数为正？", "接不上「<span class='mj'>P</span> 不动 ⇒ 需求全部由产量吸收」", "[[s6|§6 第 ③ 组]]"],
                ["⑭ ↑<span class='mj'>A_{t}</span> 在简单粘性下为什么就业反而下降？", "直觉想反了（以为技术好就多雇人）", "[[s6|§6 第 ⑩ 组]]"],
                ["⑮ 为什么「稳物价」与「补缺口」在部分粘性下是同一件事？", "不知道它俩是 <span class='mj'>P-\\bar P=\\gamma(Y-Y^{f})</span> 的两边", "[[s3|§3 模块六]]"],
                ["⑯ 为什么 <span class='mj'>\\gamma</span> 越大价格越不粘？", "把 <span class='mj'>\\gamma</span> 当成「粘性程度」而不是「斜率」", "[[s6|§6 第 ⑮ 组]]"],
            ],
            note="**这一档答不上来最危险**——因为它意味着你「会用结论但不会推」，一旦题目换个问法就崩。建议把每一题的链条在纸上写一遍（三到四步）。",
        )),
        ("table", dict(
            caption="第三档 · 能画：图形与传导",
            cls="table",
            header=["问题", "答不上来说明什么", "回看"],
            first_bold=True,
            rows=[
                ["⑰ 怎么从 45° 图推出 IS？（两个面板怎么对应）", "不会「把纵轴从支出换成利率」", "[[s4|§4]]"],
                ["⑱ 怎么从劳动市场＋生产函数推出 <span class='mj'>Y^{s}</span>？", "画不出四宫格", "[[s4|§4]]"],
                ["⑲ 怎么从货币市场推出 LM？", "不会「左边换 <span class='mj'>Y</span>、右边读 <span class='mj'>r</span>」", "[[s4|§4]]"],
                ["⑳ 怎么从 IS＋LM 推出 AD？", "不会把 <span class='mj'>(r,Y)</span> 平面的交点搬到 <span class='mj'>(P,Y)</span> 平面", "[[s4|§4]]"],
                ["㉑ 三种 AS 分别怎么画？它们都过哪个点？", "不知道都过 <span class='mj'>(Y^{f},\\bar P)</span>", "[[s7|§7 表四]]"],
                ["㉒ 一个 IS 冲击在六个面板上的完整反应？", "漏掉「劳动市场不动」", "[[s7|§7 表三]]"],
                ["㉓ 一个供给冲击在简单粘性下怎么画？", "画不出 <span class='mj'>N</span> 左移、<span class='mj'>w</span> 下降", "[[s7|§7 表三]]"],
                ["㉔ 最优政策怎么画？目标点在哪？", "不知道目标是 <span class='mj'>(Y^{f},\\bar P)</span>", "[[s3|§3 模块六]]"],
            ],
            note="**这一档答不上来，考试时图形题会直接空着**——那是整张卷子最容易被放弃、也最好拿的分。把 §4 的十一张图各画一遍，只需两小时。",
        )),
        ("note", "考前 48 小时怎么排", "**不要重读笔记。** 按下面六步走，每一步都用「合上材料、白纸默写」的方式，写完再对。"),
        ("steps", [
            ("第 1 天上午 · 默四张表", "拿白纸默写 [[s7|§7 的四张表]]。<b>只默「+ / − / 0」与模型名，不默解释。</b>错一个格子就在旁边标红。"),
            ("第 1 天下午 · 默四十五条", "默写 [[s3|§3 的公式]]：<b>只写式子，不写说明</b>。写完对照，把写不出的那几条单独抄三遍。"),
            ("第 1 天晚上 · 扫易错", "把十讲的「易错清单」翻一遍（每讲约 15–20 条，共 175 条）。<b>只看标题，看到「这个我好像犯过」就停三秒。</b>"),
            ("第 2 天上午 · 三个模型的完整求解", "新古典、简单粘性、部分粘性，各走一遍「谁定 <span class='mj'>Y</span> → 谁定 <span class='mj'>P</span> → 谁定 <span class='mj'>N,w</span>」。<b>这是论述题与图形题共同的骨架。</b>"),
            ("第 2 天下午 · 三套模板各写一次", "用一道真题，把 [[s8|§8 的三个模板]] 各套一遍。<b>重点练「第一分钟」——读完题先写模型编号。</b>"),
            ("考前两小时 · 只看两页", "只看 [[s2|§2 的八模型表]] 与 [[s6|§6 的十六句判据]]。<b>不再碰新内容，只做「确认」。</b>"),
        ]),
        ("big", "**十个模型，一句话：**增长靠技术（T1–3）；储蓄靠偏好（T4）；利率靠出清（T5–7）；产出靠供给（T8–9）；**而只要价格不肯动，产出就改由需求决定**（T10）。<br>这门课从头到尾只做了一件事：**把「假设的行为规则」一个个换成「最优化的结果」，然后看每换一次，结论翻了多少。**"),
        ("tip", "最后一句", "考场上真正需要的只有三样：**[[s2|一张八模型表]]**（知道用哪个模型）、**[[s7|四张定性表]]**（知道结论往哪边动）、**[[s6|十六句判据]]**（知道边界在哪）。<b>其余的推导，都能在这三样的框架里现场做出来。</b>"),
    ],
))

# ===== END =====
