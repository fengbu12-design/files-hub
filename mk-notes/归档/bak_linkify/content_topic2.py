# -*- coding: utf-8 -*-
"""
AF5638 Macroeconomics · Topic 2 内容文件
The Solow Model（Part I + Part II，GLS Ch. 5–6）

写作原则（与 Topic 1 / 8 / 9 / 10 一致）：
  1) 每页先给「白话」——用日常语言说这页在干什么，尽量不含符号；
  2) 再给「讲解」——展开推导；
  3) 凡有公式的页，「等式两边」说清左右各是什么、为什么相等；
  4) 凡有图的页，「这张图怎么看」说清坐标轴、每条线、怎么读、会怎么考。

本讲主线（务必先记住）：
  一条动态方程 k_{t+1}=sAf(k_t)+(1-δ)k_t → 一个稳态 k* → 三个问题
  （为什么收敛？什么能让 k* 上升？为什么这仍然解释不了长期增长？）
"""

COURSE      = "AF5638 宏观经济学 · Macroeconomics"
TOPIC       = 2
TOPIC_TITLE = "Topic 2 · 索洛模型（资本积累与增长）"
SUBTITLE    = "一条差分方程定出稳态：为什么资本积累只带来「水平效应」、不能带来持续增长，以及把技术进步装进模型需要改哪一步"
INSTRUCTOR  = "讲师：Elaine Liu（PolyU）· Fall 2026"
SOURCES     = "课件：Topic 2 - The Solow Model（Part I 46 页 + Part II 9 页）· 教材：GLS Ch. 5–6"
SLIDE_COUNT = 55

MAP_CHIPS = [
    ("Topic 1 · 增长事实", False, False),
    ("Topic 2 · Solow", True, True),
    ("Topic 3 · 跨国收入差异", False, False),
    ("Topic 4–7 · 跨期模型", False, False),
    ("Topic 8–9 · 新古典", False, False),
    ("Topic 10 · 新凯恩斯", False, False),
]

SECTIONS = [
    ("① 为什么还要写这个模型", 1),
    ("② 世界设定：家庭与厂商", 4),
    ("③ 生产函数的七条假设", 7),
    ("④ 要素需求与零利润", 10),
    ("⑤ 三个市场出清", 12),
    ("⑥ 均衡与资本积累方程", 15),
    ("⑦ 改写成人均形式", 17),
    ("⑧ 稳态与收敛", 21),
    ("⑨ 冲击实验一：↑A", 26),
    ("⑩ 冲击实验二：↑s", 30),
    ("⑪ 增长到底从哪来", 34),
    ("⑫ 稳态的第二种画法", 36),
    ("⑬ 黄金律与动态无效", 38),
    ("⑭ 附录：三个证明", 43),
    ("⑮ Part II：劳动增强型技术进步", 47),
]

TLDR = [
    "全讲只有<b>一条动态方程</b>：<span class='mj'>k_{t+1}=sAf(k_t)+(1-\\delta)k_t</span>。它说「明天的资本 = 今天存下来的产出 + 今天没折旧掉的资本」。其余六个变量都是这条方程的<b>静态附属</b>——知道 k<sub>t</sub> 就知道全部。",
    "稳态由<b>两条线</b>的交点决定：45° 线（<span class='mj'>k_{t+1}=k_t</span>）与储蓄曲线（<span class='mj'>sAf(k_t)+(1-\\delta)k_t</span>）。曲线在 45° 之上则 k 上升，之下则 k 下降——这就是<b>收敛</b>，也是「稳态唯一且全局稳定」的图形证明。",
    "<b>↑A 与 ↑s 都能提高 k*，都只带来「水平效应」</b>：转型期增长加快，到达新稳态后增长率回到零。<b>原因只有一个：资本的边际报酬递减。</b>这就是「你没法靠储蓄变富」的正式版本。",
    "<b>持续增长必须来自生产率</b>：A 可以无限增长，s 有上界 1；而且反复提高 s 会让 r 一路下降，与「r 大致不变」的事实矛盾。Part II 正是为此引入劳动增强型技术 <span class='mj'>Z_t</span>。",
    "两个最容易被扣分的点：① <b>冲击当期 k 不动</b>（存量预定，只有流量与价格能跳）；② <b>c 在 ↑s 时先跌后升</b>，最终高低<b>不确定</b>——除非用黄金律判断。",
]

# ==================== 符号表 ====================
NOTATION = [
    ("一、三种「资本/劳动」口径（最容易混）", [
        ("<span class='mj'>K_t,\\ L_t</span>", "总量", "<b>资本存量、劳动投入</b>（水平值，不是人均）。"),
        ("<span class='mj'>k_t,\\ y_t,\\ c_t,\\ i_t</span>", "人均（per worker）", "<b>除以 L</b>：<span class='mj'>k_t=K_t/L_t</span>。Part I 的主角。"),
        ("<span class='mj'>\\hat{k}_t,\\ \\hat{y}_t</span>", "每效率单位（per efficiency unit）", "<b>除以 Z<sub>t</sub>L<sub>t</sub></b>。Part II 的主角——因为人均量在增长路径上不稳定，除以效率单位才稳定。<b>帽子 = 效率单位</b>。"),
    ]),
    ("二、外生参数（模型给定了就不动，除非做实验）", [
        ("<span class='mj'>s</span>", "储蓄率", "<b>收入的固定比例被储蓄</b>，<span class='mj'>0\\le s\\le 1</span>。<b>家庭不优化</b>——这是 Solow 与 Topic 4 最大的差别。"),
        ("<span class='mj'>\\delta</span>", "折旧率（delta）", "<b>每期资本磨损掉的比例</b>，<span class='mj'>0&lt;\\delta&lt;1</span>。折旧是<b>存量</b>的比例，所以写 <span class='mj'>\\delta k</span>。"),
        ("<span class='mj'>A</span>", "生产率（水平）", "Hicks 中性技术：<b>同样投入能产出多少</b>。Part I 里 A 不变，做实验时才变。"),
        ("<span class='mj'>Z_t</span>", "劳动增强型技术", "<b>效率单位</b>的来源，<span class='mj'>Z_t=(1+z)^t</span>。A 管「水平」，Z 管「增长」。"),
        ("<span class='mj'>n,\\ z</span>", "人口增长率、技术进步率", "<span class='mj'>L_t=(1+n)^t</span>、<span class='mj'>Z_t=(1+z)^t</span>。Part II 里两个都大于零。"),
        ("<span class='mj'>\\alpha</span>", "资本份额", "Cobb-Douglas 里 <span class='mj'>Y=AK^{\\alpha}L^{1-\\alpha}</span> 的 α；实测约 1/3。"),
    ]),
    ("三、函数与导数（认名字就够）", [
        ("<span class='mj'>F(K,L)</span>", "生产函数", "两种投入的<b>总量</b>生产函数，满足一次齐次（CRTS）。"),
        ("<span class='mj'>f(k)</span>", "人均生产函数", "<span class='mj'>f(k)\\equiv F(k,1)</span>。<b>小写 f 就是「每单位劳动的产出」</b>，是整个模型的核心曲线。"),
        ("<span class='mj'>f'(k)</span>", "资本的边际产品（人均）", "<span class='mj'>f'(k)&gt;0</span> 且 <span class='mj'>f''(k)&lt;0</span>（递减）。<b>它同时决定 r</b>：<span class='mj'>r=Af'(k)</span>。"),
        ("<span class='mj'>f(k)-kf'(k)</span>", "劳动的边际产品（人均）", "CRTS 下剩下的都归劳动，所以 <span class='mj'>w=A[f(k)-kf'(k)]</span>。<b>不用记，会用欧拉定理推即可</b>。"),
    ]),
    ("四、三种「均衡点」别搞混", [
        ("<span class='mj'>k^*</span>", "稳态（steady state）", "<b>模型自己收敛到的点</b>，由 s、A、δ 决定。没有「最优」含义。"),
        ("<span class='mj'>k^*_{GR}</span>", "黄金律资本（Golden Rule）", "<b>使稳态消费最大的那个 k</b>，由 <span class='mj'>Af'(k)=\\delta</span> 定。<b>它是「应该选哪个 s」的答案，不是模型的结果</b>。"),
        ("<span class='mj'>\\hat{k}^*</span>", "效率单位稳态", "Part II 的稳态。<b>人均</b>资本在这一点上是<b>以 z 的速度增长</b>的，不是不变。"),
    ]),
]

HOWTO_READ = [
    ("① 先问「这是水平值还是人均值」", "整套推导的前提是<b>除以 L</b>。看到 <span class='mj'>K</span> 与 <span class='mj'>k</span> 分不清，后面每一步都会错。Part II 还要再除以 Z。"),
    ("② 再看「哪条线动了」", "所有比较静态都只有两种：<b>储蓄曲线上移</b>（↑A、↑s 都是乘性放大）或 <b>折旧线变陡</b>（↑δ）。45° 线永远不动。"),
    ("③ 区分「跳变」与「连续」", "<b>存量 k 是预定的，冲击当期不动</b>；能跳的是流量（y、c、i）与价格（w、r）。判断依据：这个变量能不能在当期重新决定。"),
    ("④ 最后问「增长率变没变」", "Solow 的全部悲剧都在这一步：<b>任何参数变化都只改变水平，不改变长期增长率</b>——除非让 A 或 Z 自己一直增长。"),
]

# ============================ 逐页讲解 ============================
C = {}
def add(p, **kw): C[p] = kw

add(1, kp="这一讲要回答两个问题：<b>国家之间为什么贫富悬殊</b>？<b>长期增长到底由什么驱动</b>？",
      plain="上一讲我们看到：各国人均收入差几十倍，而人均工作时间几十年来几乎没变。既然「干活的人均时长」没增加，增长就只能来自「每个人能生产出更多东西」——要么是每人配的机器更多（资本积累），要么是同样机器能生产更多（技术进步）。这一讲就是建一个模型，把这两条路分开算清楚，然后告诉你：只有第二条能走长远。",
      note="课件 Part I 共 46 页（其中编号 44 页 + 附录），Part II 9 页。<br>"
            "结构非常清楚，可以按「四步」走：<br>"
            "① <b>搭模型</b>（p4–16）：家庭、厂商、三个市场出清、一条资本积累方程；<br>"
            "② <b>解稳态</b>（p17–25）：人均化 → 图形 → 闭式解；<br>"
            "③ <b>做实验</b>（p26–33）：↑A、↑s 两个冲击，各看「新稳态」与「转型路径」；<br>"
            "④ <b>下结论</b>（p34–41）：为什么这解释不了持续增长 → 黄金律 → 动态无效；<br>"
            "⑤ <b>打补丁</b>（Part II，p47–55）：加一个会增长的技术项 Z<sub>t</sub>，人均量才能长期增长。",
      tip="记住这个模型的「一句话身份」：<b>它是宏观里第一个能算出「收敛速度」和「资本积累上限」的模型</b>。后面 Topic 3（跨国收入差异）就是拿它去做定量核算的。",
      warn="不要把它当成「过时的模型」。它有三个东西一直用到期末：<b>① 人均化技巧；② 稳态＋转型的分析范式；③ 「边际报酬递减 ⇒ 资本积累不能带来持续增长」这个结论</b>。第十讲的 AK 式增长、Topic 3 的发展核算，都以它为基准。")

add(2, kp="三个事实把问题逼到一个岔路口：既然劳动投入没有趋势，增长只能来自<b>资本</b>或<b>生产率</b>。",
      plain="课件先把上一讲的事实摆出来：① 各国人均收入差距巨大；② 生产要素只有资本和劳动两种；③ 人均工时基本没有趋势（既没大涨也没大跌）。第三条最关键——它排除了「靠多干活变富」这条路，于是只剩两个嫌疑：机器更多，或者技术更好。",
      note="课件四句原文的意思：<br>"
            "① <b>Vast disparities exist in per capita income across nations</b>——人均收入差距极大，这是要被解释的现象；<br>"
            "② <b>Two types of factors of production</b>——只有资本与劳动，所以生产函数写成 <span class='mj'>F(K,L)</span>；<br>"
            "③ <b>Hours worked per capita is roughly trendless</b>——<b>人均工时无趋势</b>。这条是排除法的关键：如果劳动投入长期不变，那么「劳动投入的增加」就解释不了长期增长；<br>"
            "④ 于是问题变成：<b>资本积累还是生产率改进</b>？换个问法：<b>富国是因为资本多，还是因为生产率高</b>？",
      tip="第③条值得单独记：它把「增长核算」里的一项直接划掉。<b>增长 = 资本深化 + 劳动投入 + 生产率</b>，而中间那项在长期近似为零，所以争论只在第一项与第三项之间。",
      warn="「人均工时无趋势」是<b>经验事实</b>，不是模型假设。答题时如果要用它，要说「按课件引用的数据事实」，不能当成定理。")

add(3, kp="Solow 模型的两个核心结论：<b>生产率决定长期增长</b>、<b>生产率决定跨国收入差异</b>——都不是资本。",
      plain="这个模型是 1953 年 Solow 提出来的，用来研究长期增长和各国收入差距。它解释「典型事实」解释得不错。它给出的主要结论只有一句：生产率是关键。两个含义——持续增长靠生产率（不是靠攒机器），理解各国贫富也靠生产率（不是靠资本水平）。但模型有个软肋：它把生产率当成外生给定的，既没解释它是什么，也没说怎么提高。",
      note="课件三句结论：<br>"
            "① <b>Productivity key to sustained growth (not factor accumulation)</b>——持续增长靠生产率，不靠要素积累；<br>"
            "② <b>Productivity key to understanding cross-country income differences (not level of capital)</b>——跨国差异也主要靠生产率；<br>"
            "③ <b>Model takes productivity to be exogenous</b>——模型把 A 当外生。<b>What is it? How to increase it?</b> 这两个问题本讲不回答，留给后续（内生增长）。",
      tip="这两条结论在期末是「论证题」的答案骨架：<b>先证明「资本积累有上限」（稳态＋边际报酬递减），再由此推出「剩下的只能是生产率」</b>。第 34–35 页就是把这条逻辑走完。",
      warn="别把①和②混成一句「生产率很重要」。<b>①是时间维度</b>（同一个国家为什么越来越富），<b>②是横截面维度</b>（同一年为什么有的国家富）。两者论证路径不同：①靠「增长率」，②靠「稳态水平的比较」。")

add(4, kp="五个建模约定：<b>封闭经济、单一最终品、离散时间、代表性个体、物价归一</b>。",
      plain="先把世界简化到最小：一个国家自己生产一种东西，时间按天（期）数，所有人一模一样所以可以当成一个人，所有企业技术一样所以可以当成一家。最后，因为只有一种商品，就把它的价格定为 1——所有东西都用「多少单位的这种商品」来计价。",
      note="课件五条：<br>"
            "① <b>Closed economy, unique final good</b>——封闭经济、只有一种最终品。所以没有贸易、没有相对价格问题；<br>"
            "② <b>Discrete time</b>，<span class='mj'>t=0,1,2,\\cdots</span>——离散时间。这一条决定了图形是<b>阶梯</b>而不是连续曲线；<br>"
            "③ <b>Representative household</b>——大量相同家庭 ⇒ 加总成一个；<br>"
            "④ <b>Representative firm</b>——技术相同 ⇒ 加总成一家；<br>"
            "⑤ <b>Numeraire</b>：物价每期都归一为 1。",
      lr=[dict(name="为什么可以把物价定为 1（numeraire）",
               lhs="P_t\\equiv 1",
               lhs_t="每期的物价水平，人为规定等于 1",
               rhs="\\text{all prices in units of the final good}",
               rhs_t="所有价格都用「单位的最终品」表示",
               why_t="为什么这不是假设而是记账约定",
               why="模型里只有<b>一种</b>商品，没有货币，也没有两种商品之间的相对价格问题。<b>能标价的只有这一种东西，于是「价格」这个维度是空的</b>——把它定为 1 只是选定计量单位，就像用「米」而不是「厘米」量长度，不影响任何实质结论。<br>"
                   "注意：这里的 <span class='mj'>P_t\\equiv 1</span> 与第十讲的 <b>价格粘性</b>完全不是一回事。第十讲有货币、有多种决定名义量的因素，P 是内生的；这里根本没有名义量。")],
      tip="一句话：<b>这一讲没有「钱」，只有「东西」。</b>所有变量都是实际量（real），所以你在这张讲里找不到通胀、找不到名义利率——那是 Topic 9 之后的事。",
      warn="「离散时间」不是技术细节。它直接决定两件事：① 冲击当期 <span class='mj'>k_t</span> 是<b>预定</b>的（因为它是上一期就定下来的），所以不会跳；② 收敛图是<b>阶梯式</b>逼近（一期一步），而不是平滑曲线。")

add(5, kp="家庭<b>不做最优化</b>：按固定比例 s 储蓄、剩余消费；劳动<b>无弹性</b>供给。",
      plain="这是 Solow 模型最「不讲道理」的地方，也是它好用的原因：家庭不做什么跨期最优决策，只是机械地按一个固定比例存钱——挣 100 块就存 20 块、花 80 块。劳动也不挑工资高低，有多少人上多少人。家庭拥有全国的机器，租给企业收租金；也拥有全部劳动，卖给企业拿工资。",
      note="课件四句：<br>"
            "① <b>Households will not be optimizing</b>——<b>不优化</b>。这一句要划重点：它把 Topic 4 那套欧拉方程整个砍掉了；<br>"
            "② 每期把可支配收入的固定比例 <span class='mj'>s</span> 存起来，剩下 <span class='mj'>1-s</span> 消费掉；<br>"
            "③ <b>Current saving becomes productive capital in the next period</b>——<b>本期储蓄变成下期资本</b>。这一句是资本积累方程的种子，也是「k<sub>t</sub> 预定」的来源；<br>"
            "④ 家庭拥有资本存量，按 <span class='mj'>r_t</span> 租给企业；拥有全部劳动，<b>无弹性地</b>（inelastically）供给，<b>不管工资多少</b>。",
      lr=[dict(name="储蓄规则（模型的「行为方程」）",
               lhs="S_t=s\\,(Y_t-G_t)",
               lhs_t="本期储蓄 = 储蓄率 × 本期可支配收入",
               rhs="I_t",
               rhs_t="本期投资（在封闭经济里，储蓄必然全部转化为投资）",
               why_t="为什么储蓄等于投资",
               why="因为<b>封闭经济、没有别的资产</b>。家庭不消费的那部分产出，如果不买机器，就只能在仓库里堆着——而堆着的产出在模型里等同于「投资」形成的资本。所以 <span class='mj'>S_t=I_t</span> 是<b>核算恒等</b>，不是均衡条件。<br>"
                   "另外注意课件在 Part I 的主线里把 G 设为零（没有政府），所以储蓄就是收入的 s 倍；<b>这里写 <span class='mj'>Y_t-G_t</span> 是为后面 Topic 6 财政政策留的位置</b>。")],
      dec=[
          ("<span class='mj'>s</span>", "储蓄率。<b>外生常数</b>。它同时是「行为参数」和「政策工具」——第 30 页拿它做实验，第 39 页问「它应该是多少」。"),
          ("<span class='mj'>1-s</span>", "消费率。注意它<b>不是</b>由最优化得出的，只是 1 减 s。所以 Solow 里没有「消费函数」这种带边际消费倾向的东西。"),
          ("<span class='mj'>r_t</span>", "资本租赁价格（rental price）。<b>是租金，不是利率</b>——机器是租的，不是买的，所以 r 的单位是「每单位资本每期的最终品」。"),
          ("<span class='mj'>w_t</span>", "实际工资。因为劳动供给无弹性，<b>w 由需求单独决定</b>，家庭对 w 没有反应。"),
      ],
      tip="把这条规则想成「一刀切」：<b>不管利率多高、不管明天怎样，我就存 20%。</b>代价是不能讨论「储蓄是否最优」（除了第 38–41 页用黄金律从外部判断），好处是模型只有一个状态变量、一条方程、能画图。",
      warn="两个常见错误：① 说「家庭选择 s」——<b>s 是外生给定的，家庭没有选择</b>；② 说「劳动供给曲线向上倾斜」——<b>这里它是一条垂直线</b>，正是这一点让 Solow 里的就业不波动，也正是 RBC（Topic 9 提到）要改的地方。")

add(6, kp="生产函数 <span class='mj'>Y_t=A_tF(K_t,L_t)</span>：<b>技术乘在函数外面</b>，两种投入进去，产出出来。",
      plain="企业用机器和人工生产。生产函数就是说「给定多少机器、多少人、什么技术，能产出多少」。课件的写法把技术 A 摆在函数外面，意思是：技术好，等于同样的机器和人手能多产出几成。最常见的具体形式是柯布-道格拉斯：产出 = 技术 × 机器^α × 人工^(1-α)。",
      note="课件给的是<b>总量</b>形式 <span class='mj'>Y_t=A_tF(K_t,L_t)</span>，五个符号：<br>"
            "<span class='mj'>Y_t</span> 产出、<span class='mj'>K_t</span> 资本投入、<span class='mj'>L_t</span> 劳动投入、<span class='mj'>F(\\cdot)</span> 生产函数、<span class='mj'>A_t</span> 生产率。<br>"
            "例子是 Cobb-Douglas：<span class='mj'>F(K_t,L_t)=K_t^{\\alpha}L_t^{1-\\alpha}</span>，<span class='mj'>0&lt;\\alpha&lt;1</span>。<br><br>"
            "第 7–8 页的七条假设都是为了<b>让后面每一步推导成立</b>：<br>"
            "· 没有 CRTS（第 2 条）就<b>不能人均化</b>（推不出 <span class='mj'>y=Af(k)</span>）；<br>"
            "· 没有边际报酬递减（第 4 条）就<b>没有稳态</b>（资本会一直积累）；<br>"
            "· 没有 Inada 条件（第 6–7 条）就<b>不能保证稳态唯一</b>。",
      lr=[dict(name="总量生产函数",
               lhs="Y_t",
               lhs_t="本期总产出（用最终品的单位衡量）",
               rhs="A_tF(K_t,L_t)",
               rhs_t="技术 × 把 K、L 变成产出的函数",
               why_t="这条式子说了什么",
               why="它把「增长从哪来」拆成三个可数的来源：<b>K 变多、L 变多、A 变高</b>。第 2 页已经排除了 L（无趋势），所以只剩 K 与 A——<b>整个模型的全部戏剧性，就在这两项之间展开</b>。<br>"
                   "另外注意 A 的位置：写在 F 外面（Hicks 中性）。这意味着 A 提高时，<b>资本与劳动的边际产品同比例提高</b>——所以它不会改变两种要素的相对价格，只改变总量。Part II 要把 A 挪到 L 旁边（劳动增强型），正是因为只有那样才能让模型产生<b>平衡增长</b>。")],
      dec=[
          ("<span class='mj'>A_t</span>", "生产率 / TFP（全要素生产率）。<b>它不是一个真实的投入</b>，而是「用现有的 K 和 L 解释不了的那部分产出」——所以又叫「索洛剩余」（Solow residual）。"),
          ("<span class='mj'>F(\\cdot)</span>", "生产函数。它<b>只描述技术可行性</b>，不描述价格；同样的 F，配上不同的价格就得到不同的要素需求。"),
          ("<span class='mj'>\\alpha</span>", "资本份额。在 Cobb-Douglas 下，<b>α 恰好等于资本收入占产出的比例</b>，也等于资本的产出弹性。所以它可以被国民收入账户直接量出来（约 1/3）。"),
      ],
      tip="柯布-道格拉斯为什么要记？因为它是<b>唯一能让 k* 写出闭式解</b>的形式（第 25 页）。考试只要给 α，就要能立刻写出 <span class='mj'>y=Ak^{\\alpha}</span>、<span class='mj'>r=\\alpha Ak^{\\alpha-1}</span>、<span class='mj'>w=(1-\\alpha)Ak^{\\alpha}</span> 这三个式子。",
      warn="<b>A 与 F 位置不能随手换。</b>写成 <span class='mj'>Y=F(AK,L)</span> 是「资本增强型」，写成 <span class='mj'>Y=F(K,AL)</span> 是「劳动增强型」，三者在增长性质上完全不同：只有<b>劳动增强型</b>才与平衡增长相容（Part II 第 49 页会讲）。")

add(7, kp="生产函数前四条假设：<b>两种投入缺一不可、规模报酬不变、边际产出为正、边际产出递减</b>。",
      plain="这四条是在给生产函数「定形状」。缺一不可：没有机器或没有人都生产不出来。规模报酬不变：所有投入同时翻倍，产出也翻倍（不是翻两倍，也不是一点五倍）。边际产出为正：多给一点机器总归多产一点。边际产出递减：但每多给一点，多产出的那点会越来越少。",
      note="课件第 1–4 条：<br>"
            "① <b>Both inputs are essential</b>：<span class='mj'>F(0,L)=0</span>、<span class='mj'>F(K,0)=0</span>——<b>缺一不可</b>。经济含义：不能只靠机器生产，也不能只靠人。技术上这意味着等产量线不与坐标轴相交。<br>"
            "② <b>CRTS</b>：<span class='mj'>F(\\gamma K,\\gamma L)=\\gamma F(K,L)</span>，任何 <span class='mj'>\\gamma&gt;0</span>。<b>一次齐次</b>。这条是<b>人均化的许可证</b>，也是零利润（第 11 页）的前提。<br>"
            "③ <b>Positive marginal products</b>：<span class='mj'>F_K&gt;0</span>、<span class='mj'>F_L&gt;0</span>——多投入一定多产出。所以要素需求曲线在正象限。<br>"
            "④ <b>Diminishing marginal products</b>：<span class='mj'>F_{KK}&lt;0</span>、<span class='mj'>F_{LL}&lt;0</span>——二阶导为负。<b>这条是稳态存在的根本原因</b>：资本的回报越积越少，所以不会无限积累。",
      lr=[dict(name="规模报酬不变（CRTS）",
               lhs="F(\\gamma K,\\gamma L)",
               lhs_t="两种投入同时放大 γ 倍后的产出",
               rhs="\\gamma F(K,L)",
               rhs_t="原产出的 γ 倍",
               why_t="为什么这条特别重要",
               why="它等价于说「生产函数是<b>一次齐次</b>」的，于是<b>产出可以被「平均」到每个工人头上</b>：<span class='mj'>F(K,L)/L=F(K/L,1)=f(k)</span>。没有这一条，人均产出就同时依赖 K 和 L 两个数，模型没法画在二维平面上。<br>"
                   "第二条用途在第 11 页：一次齐次 ⇒ 欧拉定理 ⇒ <b>总产出恰好等于总要素报酬，利润为零</b>。所以「CRTS」这一个假设同时买了两样东西：<b>人均化</b>与<b>零利润</b>。")],
      dec=[
          ("<span class='mj'>F_K,\\ F_L</span>", "偏导数 = <b>边际产品</b>。经济含义：其他投入不变时，多加一单位该要素能多产出多少。均衡时它等于该要素的价格（第 10 页）。"),
          ("<span class='mj'>F_{KK},\\ F_{LL}</span>", "二阶偏导 = <b>边际产品的斜率</b>，为负 ⇒ 边际报酬递减。这就是「凹函数」。"),
          ("<span class='mj'>\\gamma</span>", "任意正数。<b>注意是对所有投入同比例放大</b>——只放大一种投入不叫规模变化。"),
      ],
      tip="三条假设的分工要能一句话说清：<b>CRTS 让你能「除以 L」；递减报酬让你「有稳态」；缺一不可让你「不会退化到零」。</b>",
      warn="「规模报酬不变」与「边际报酬递减」<b>不矛盾</b>，这是最常被问的概念题。前者说<b>所有</b>投入同比例放大时产出同比例放大（沿射线看）；后者说<b>只</b>增加一种投入时增量递减（沿水平线看）。柯布-道格拉斯同时满足两者。")

add(8, kp="后三条：<b>资本与劳动互补、零投入时边际产出无穷、无穷投入时边际产出为零</b>。后两条合称 Inada 条件。",
      plain="第 5 条说机器和人要配套：人多了机器不变，多一个人能干的活反而更多一点（因为分工）。第 6、7 条是一对「边界条件」：资本几乎为零时，第一台机器极其有用（边际产出无穷大）；资本已经极多时，再加机器几乎没用（边际产出趋于零）。这两条合起来保证曲线两头的样子是对的。",
      note="课件第 5–7 条：<br>"
            "① <b>Capital and labor are complementary</b>：<span class='mj'>F_{KL}=F_{LK}&gt;0</span>——<b>交叉偏导为正</b>。经济含义：资本多了，劳动的边际产出也变高（互补）。这一条决定了「劳动需求曲线会随 K 上升而右移」（Topic 8 用到）。<br>"
            "② <b>Infinite marginal products at zero</b>：<span class='mj'>\\lim_{K\\to 0}F_K=\\infty</span>，<span class='mj'>\\lim_{L\\to 0}F_L=\\infty</span>——<b>从零起步时，第一单位投入的边际产出无穷大</b>。<br>"
            "③ <b>Zero marginal products at infinity</b>：<span class='mj'>\\lim_{K\\to\\infty}F_K=0</span>，<span class='mj'>\\lim_{L\\to\\infty}F_L=0</span>——<b>投入无穷多时，边际产出趋于零</b>。<br>"
            "②③ 合起来叫 <b>Inada Conditions</b>（稻田条件）。",
      tip="Inada 条件的作用<b>只有一件事</b>：保证储蓄曲线与 45° 线<b>在 (0,∞) 内恰好相交一次</b>。<br>"
          "· <span class='mj'>f'(0)=\\infty</span> ⇒ 曲线在原点处<b>无限陡</b> ⇒ 一定<b>从 45° 线上方出发</b>（所以不会卡在 k=0）；<br>"
          "· <span class='mj'>f'(\\infty)=0</span> ⇒ 曲线最终<b>平于</b> <span class='mj'>(1-\\delta)k</span> 这条直线 ⇒ 一定<b>落到 45° 线下方</b> ⇒ 必有交点；<br>"
          "· 再加上 <span class='mj'>f</span> 严格凹 ⇒ 交点<b>唯一</b>。<b>这就是「稳态存在且唯一」的完整证明思路。</b>",
      warn="Inada 条件是<b>充分条件</b>，不是必要条件：有些函数不满足 Inada 也仍有唯一稳态。但考试里「为什么需要 Inada」的标准答案是上面那三条（出发在上方、最终在下方、凹 ⇒ 唯一）。<b>不要背成「保证边际产出为正」——那是第 3 条，不是 Inada。</b>")

add(9, kp="图形上的 Inada 条件：<b>凹且从垂直开始、最终趋于水平</b>（A 面板）；直线（B 面板）不满足。",
      plain="这张图就是同一个生产函数的两种画法。左边那条曲线：一开始几乎垂直往上冲，然后越来越平，最后接近水平——这是「边际产出从无穷大降到零」。右边是一条直线：斜率始终不变，既不会在起点无穷陡，也不会在远处变平。所以右边那个不满足 Inada 条件。",
      note="图的背景：<b>劳动固定</b>，只让资本变化，所以画的是 <span class='mj'>F(K,\\bar L)</span> 关于 K 的曲线。<b>曲线的斜率就是 MPK</b>（资本的边际产出）。<br>"
            "· <b>Panel A</b>：凹凸形，<span class='mj'>K\\to 0</span> 时斜率 → ∞，<span class='mj'>K\\to\\infty</span> 时斜率 → 0。<b>满足 Inada</b>，也满足第 3、4 条（斜率为正且递减）。<br>"
            "· <b>Panel B</b>：<b>直线</b>，斜率恒定。<span class='mj'>K\\to 0</span> 时斜率有限（不是 ∞），<span class='mj'>K\\to\\infty</span> 时斜率仍是那个常数（不是 0）。<b>两条 Inada 都不满足</b>，而且<b>第 4 条（递减报酬）也不满足</b>。",
      fig=[dict(name="Inada 条件：两个对照面板（A 满足、B 不满足）",
                axes=[("横轴", "K", "资本投入（<b>劳动固定</b>在 L̄，所以这是一条截面曲线，不是整个生产函数）"),
                      ("纵轴", "F(K,L)", "产出"),
                      ("斜率", "F_K=\\partial F/\\partial K", "<b>曲线的斜率就是 MPK</b>——这张图的全部信息都在斜率上")],
                marks=[("Panel A：凹曲线", "从原点<b>垂直起步</b>（斜率 ∞）→ 一路变平 → 远处<b>近乎水平</b>（斜率 → 0）。<b>两个 Inada 条件都满足</b>，递减报酬也满足"),
                       ("Panel B：直线", "<b>斜率恒定</b>。起点斜率有限（违反第 6 条），远处斜率仍是那个数（违反第 7 条），<b>也没有递减报酬</b>（违反第 4 条）"),
                       ("0 点", "两个面板都过原点——这是第 1 条「缺一不可」：<span class='mj'>F(0,L)=0</span>")],
                read="<b>只看两头的斜率。</b>左端斜率是不是无穷（陡不陡）、右端斜率是不是零（平不平）。<b>两个都是「是」才是 Inada。</b>中间那段是不是递减，是第 4 条的事——A 面板满足、B 面板不满足。",
                exam="考法有两种：① 给一个具体函数（如 <span class='mj'>F=K+aL</span>、<span class='mj'>F=\\sqrt{K}L</span>、<span class='mj'>F=K^{1/3}L^{2/3}</span>）判断是否满足七条；② 问「如果生产函数是线性的（B 面板），Solow 模型还有稳态吗」——<b>没有</b>，因为储蓄曲线是直线且斜率可能大于 1，会与 45° 线永不相交或处处相交，资本无限积累（这正是内生增长模型的起点）。")],
      tip="课件留了一道 <b>Exercise</b>：验证 Cobb-Douglas 满足 1–7 条。做法固定：<span class='mj'>F=K^{\\alpha}L^{1-\\alpha}</span> → <span class='mj'>F_K=\\alpha K^{\\alpha-1}L^{1-\\alpha}&gt;0</span>、<span class='mj'>F_{KK}=\\alpha(\\alpha-1)K^{\\alpha-2}L^{1-\\alpha}&lt;0</span>（因为 α&lt;1）、<span class='mj'>F_{KL}=\\alpha(1-\\alpha)K^{\\alpha-1}L^{-\\alpha}&gt;0</span>、<span class='mj'>K\\to 0</span> 时 <span class='mj'>F_K\\to\\infty</span>、<span class='mj'>K\\to\\infty</span> 时 <span class='mj'>F_K\\to 0</span>。七条逐条对上，就是满分答案。",
      warn="B 面板那个「直线」不是随便画的——它对应 <span class='mj'>F=AK</span>（AK 模型）。<b>它没有稳态</b>，而这恰恰是内生增长理论要的性质：只要资本的报酬不递减，资本积累就能带来持续增长。考试如果问「Solow 为什么需要递减报酬」，答案就是这张图的对比。")

add(10, kp="企业租机器、雇工人，<b>边际成本 = 边际收益</b>：工资等于劳动的边际产品、租金等于资本的边际产品。",
      plain="企业要决定雇多少人、租多少机器，才能让利润最大。办法很朴素：多雇一个人，他带来的产出得够付他的工资；多租一台机器，它带来的产出得够付它的租金。所以最终一定是「工资 = 劳动的边际产出」「租金 = 资本的边际产品」。这个「边际产品 = 价格」的条件，就是所有要素需求的来源。",
      note="课件先写最优化问题（<b>取价格 r<sub>t</sub>、w<sub>t</sub> 为给定</b>，企业是价格接受者）：<br>"
            "<span class='mj'>\\max_{K^d_t,L^d_t}\\ \\Pi_t=A_tF(K^d_t,L^d_t)-w_tL^d_t-r_tK^d_t</span><br>"
            "一阶条件（FOC）：<br>"
            "① <span class='mj'>w_t=A_tF_L(K^d_t,L^d_t)</span><br>"
            "② <span class='mj'>r_t=A_tF_K(K^d_t,L^d_t)</span><br><br>"
            "两个条件的推导都是「求导等于零」：对 <span class='mj'>L^d</span> 求导得 <span class='mj'>A_tF_L-w_t=0</span>；对 <span class='mj'>K^d</span> 求导得 <span class='mj'>A_tF_K-r_t=0</span>。<b>因为 F 是凹的（递减报酬），一阶条件同时也是充分条件</b>——不用担心是最大值还是最小值。",
      lr=[dict(name="劳动的一阶条件（要素需求）",
               lhs="w_t",
               lhs_t="实际工资：多雇一个工人要付的成本",
               rhs="A_tF_L(K^d_t,L^d_t)",
               rhs_t="多雇一个工人带来的<b>产出增量</b>（劳动的边际产品，乘上技术）",
               why_t="为什么两边相等（「边际成本 = 边际收益」）",
               why="这是<b>利润最大化的一阶条件</b>，不是恒等式。逻辑：如果 <span class='mj'>w&lt;AF_L</span>，多雇一个人赚的比付的多，企业会继续雇；如果 <span class='mj'>w&gt;AF_L</span>，雇一个人亏一个，企业会裁员。<b>只有两边相等时企业才停手</b>。<br>"
                   "注意右边是 <b>AF<sub>L</sub></b> 而不是 F<sub>L</sub>：因为价格归一为 1，A 直接放大实物产出，而工资也是以最终品计价的，所以「多产出的实物量 × 技术」直接就是「多产出的价值」。"),
           dict(name="资本的一阶条件",
               lhs="r_t",
               lhs_t="资本租赁价格：多租一台机器一期的成本",
               rhs="A_tF_K(K^d_t,L^d_t)",
               rhs_t="多租一台机器带来的产出增量（资本的边际产品）",
               why_t="为什么两边相等",
               why="同样是一阶条件。这条式子<b>后面会被翻译成人均形式</b>：<span class='mj'>r=A f'(k)</span>（第 20 页）。<br>"
                   "它有一个直接推论，考试常考：<b>r 只取决于 k，不取决于规模</b>——因为 CRTS 下边际产品是零次齐次的，把 K 和 L 同比例放大不改变 <span class='mj'>F_K</span>。所以「两个国家资本/劳动比相同，利率就相同」，与大小无关。")],
      dec=[
          ("<span class='mj'>K^d_t,\\ L^d_t</span>", "企业的<b>要素需求</b>（不是供给）。上标 d = demand。<b>企业的需求就是市场的需求</b>（因为只有一家代表性企业）。"),
          ("<span class='mj'>\\Pi_t</span>", "利润。<b>均衡时等于零</b>（下一页证明）——所以模型里没有「利润收入」这一项，家庭收入就是 Y。"),
          ("<span class='mj'>A_tF_L</span>", "劳动的<b>边际产品价值</b>（value of marginal product）。价格归一时，「价值」与「实物」同单位，所以不用再乘 P。"),
      ],
      tip="一句话记住两个 FOC：<b>「工资 = 劳动的边际产品、租金 = 资本的边际产品」</b>。这两个式子后面被反复使用：第 20 页变成 <span class='mj'>w=Af-kAf'</span> 与 <span class='mj'>r=Af'</span>，第 28 页用来判断 w、r 的跳变方向，第 54 页用来判断增长路径上谁不变。",
      warn="<b>r 是「租赁价格」不是「利率」。</b>严格说，如果资本价格是 1、折旧率是 δ，那么利率 <span class='mj'>i=r-\\delta</span>（净回报）。Solow 模型里通常直接把 r 当回报率用，考试按课件的写法来，但要能说清这个区别——第十讲讨论货币时利率才会正式出现。")

add(11, kp="CRTS ⇒ 欧拉定理 ⇒ <b>总产出恰好被要素报酬分光，利润为零</b>。",
      plain="这条结论很漂亮：在规模报酬不变的技术下，企业把「该给工人的工资」和「该给机器主人的租金」都付完之后，一分钱利润都不剩。所以整个产出都变成了家庭收入。这也意味着模型里没有「资本家拿走利润」这回事。",
      note="课件：<span class='mj'>A_tF(K^d_t,L^d_t)=w_tL^d_t+r_tK^d_t</span>，即<b>总产出 = 总要素报酬</b>。<br>"
            "证明在附录（第 44 页）：一次齐次函数满足欧拉定理 <span class='mj'>F=F_KK+F_LL</span>，两边乘 A、把 FOC 代进去就得到。<br><br>"
            "这条结论有两个直接后果，都很重要：<br>"
            "① <b>家庭的可支配收入就是 Y<sub>t</sub></b>（他们拥有全部要素，又没有利润可拿）；<br>"
            "② <b>模型里不存在「利润驱动的投资」</b>——投资只由储蓄率 s 决定，与利润率无关。这一条是 Solow 与托宾 q 理论的分水岭。",
      lr=[dict(name="零利润（欧拉定理的直接结果）",
               lhs="A_tF(K^d_t,L^d_t)",
               lhs_t="总产出（左边整块）",
               rhs="w_tL^d_t+r_tK^d_t",
               rhs_t="总要素报酬：工资总额 + 租金总额（右边整块）",
               why_t="为什么恰好相等（不是「大致相等」）",
               why="因为 CRTS（一次齐次）+ 欧拉定理。把 <span class='mj'>w=AF_L</span>、<span class='mj'>r=AF_K</span> 代进右边：<span class='mj'>AF_LL+AF_KK=A(F_KK+F_LL)=AF</span>。<b>最后一步用的就是欧拉定理</b>——一次齐次函数的值恰好等于「各偏导 × 各投入」之和。<br>"
                   "换句话说：<b>CRTS 意味着「按边际产品分配」恰好把产出分完</b>，既不会不够分（留下正利润），也不会分过头（亏损）。这也解释了为什么完全竞争 + CRTS 是「零利润」的标准组合。")],
      tip="零利润不是「企业很惨」，而是<b>会计恒等式</b>：任何正利润都会吸引新企业进入，直到利润被竞争掉。在 CRTS 下，一家企业和一百家企业一样有效率，所以价格必须压到成本线。",
      warn="零利润<b>依赖 CRTS</b>。如果规模报酬递减（<span class='mj'>\\rho&lt;1</span>），欧拉定理给的是 <span class='mj'>\\rho F=F_KK+F_LL</span>，右边<b>小于</b>总产出，剩下的就是利润——这部分归谁，模型必须另作假设。所以「零利润」是 CRTS 的副产品，不能无条件使用。")

add(12, kp="劳动市场出清：<b>劳动供给无弹性（垂直线）</b>，所以 <span class='mj'>\\bar L_t=L^d_t</span>，工资由需求单独决定。",
      plain="劳动市场这一页几乎是「自动出清」的。因为家庭不管工资多少都提供同样多的劳动（全国有 100 个人就上 100 个人），供给是一条垂直线。企业想要多少人，就在这条垂直线上找一个点——工资自动调整到企业正好想雇满这 100 人。所以就业永远等于人口，永远不会失业。",
      note="课件：设 <span class='mj'>\\bar L_t</span> 是劳动禀赋（工人数）。出清条件：<span class='mj'>\\bar L_t=L^d_t</span>，且 <span class='mj'>w_t&gt;0</span>。<br><br>"
            "三件事必须理解：<br>"
            "① <b>为什么是「等于」而不是「小于等于」</b>：工资可以自由调整，只要 <span class='mj'>w&gt;0</span>，供给方愿意提供全部禀赋，需求方按 <span class='mj'>w=AF_L</span> 决定雇多少；价格一调，两者必然相等；<br>"
            "② <b>w 由谁定</b>：因为供给是垂直的，w 完全由<b>需求曲线</b>决定——把 <span class='mj'>L=\\bar L</span> 代进 FOC 就得到 <span class='mj'>w_t=A_tF_L(K_t,\\bar L_t)</span>；<br>"
            "③ <b>就业不波动</b>：<span class='mj'>L_t\\equiv\\bar L</span> 永远成立。所以 Solow 模型<b>根本无法产生就业波动</b>。",
      lr=[dict(name="劳动市场出清条件",
               lhs="\\bar L_t",
               lhs_t="劳动禀赋：经济里有多少工人（外生给定）",
               rhs="L^d_t",
               rhs_t="企业想雇的人数（由 <span class='mj'>w=AF_L</span> 决定）",
               why_t="为什么必然相等，以及代价是什么",
               why="因为<b>工资是完全弹性的</b>：如果 <span class='mj'>L^d&lt;\\bar L</span>（想雇的人少于有的工人），工资就会往下掉，直到企业愿意雇满；反之则往上飙。所以均衡处必然相等。<br>"
                   "<b>代价</b>：这个模型里不存在「非自愿失业」。所有波动都体现在<b>工资</b>上，而不是<b>就业量</b>上。这一点在 Topic 10（新凯恩斯）会被彻底推翻——那里工资/价格粘住，就业才会波动。")],
      tip="把这条和第 8 页的第 5 条假设连起来看：<span class='mj'>F_{KL}&gt;0</span> 意味着<b>K 上升会让劳动需求右移</b>，于是 w 上升。这就是第 28 页「↑A ⇒ w 跳升、之后继续涨」的微观基础。<b>K 或者 A 一动，w 就动，但 L 不动。</b>",
      warn="「劳动供给无弹性」是<b>Solow 的简化</b>，不是普遍事实。它的后果非常强：<b>产出波动只能来自供给侧的技术与资本，不能来自劳动投入</b>。RBC 文献（Topic 9 提到的批判）正是把这条换成「劳动供给有弹性」，才能让技术冲击解释就业波动。")

add(13, kp="商品市场出清：<span class='mj'>Y_t=C_t+I_t</span>，且 <span class='mj'>I_t=sY_t</span>、<span class='mj'>C_t=(1-s)Y_t</span>。",
      plain="生产出来的东西只有两个去处：吃掉或者存起来（变成机器）。家庭拿到的收入是全部产出，按固定比例分：s 存起来投资，1-s 消费掉。所以「产出 = 消费 + 投资」自动成立，不需要价格来出清——这是「只有一种商品」的好处。",
      note="课件三行：<br>"
            "① 家庭收入是 <span class='mj'>Y_t</span>（因为零利润，见第 11 页）；<br>"
            "② 按固定比例储蓄：<span class='mj'>I_t=sY_t</span>；<br>"
            "③ 其余消费：<span class='mj'>C_t=(1-s)Y_t</span>；<br>"
            "④ 于是 <span class='mj'>Y_t=C_t+I_t</span>。<br><br>"
            "注意这里的逻辑方向：<b>不是「价格调整使供需相等」，而是「收入按固定比例分配」直接给出了 C 和 I</b>。所以商品市场在 Solow 里没有「价格」，只有「分配规则」。",
      lr=[dict(name="资源约束 / 商品市场出清",
               lhs="Y_t",
               lhs_t="本期生产出来的全部最终品",
               rhs="C_t+I_t",
               rhs_t="被消费掉的部分 + 被投资（变成资本）的部分",
               why_t="这是恒等式还是均衡条件",
               why="在只有一种商品、没有政府、没有贸易的世界里，它是<b>核算恒等</b>（资源约束）：产出不能凭空消失，只能被吃掉或用掉。<br>"
                   "但在<b>多部门或多商品</b>模型里，同样的式子就变成<b>均衡条件</b>了——需要价格调整才能成立。「Solow 里它自动成立」这件事，是单一商品的特殊便利，<b>考试如果问「为什么 Solow 不需要解商品市场价格」，答案就在这里</b>。")],
      tip="这条式子后面会反复变形：<span class='mj'>I_t=sY_t</span> 代入资本积累方程，得到<b>整个模型唯一的动态方程</b>（第 16 页）。所以「商品市场出清」在 Solow 里的真正作用是：<b>提供投资函数</b>。",
      warn="<s>别把它写成 <span class='mj'>Y=C+I+G</span></s>：Part I <b>没有政府</b>，G=0。只有到了 Topic 6（财政政策）才会出现 G，那时储蓄率作用在 <span class='mj'>Y-G</span> 上。")

add(14, kp="资本市场的「供给」是一条运动规律：<b>下期资本 = 本期未折旧的资本 + 本期投资</b>。",
      plain="机器是攒出来的：今年剩下的机器（扣掉磨损），加上今年新造的机器，就是明年的机器总量。初始的机器数量是给定的。资本市场的均衡就是「家庭愿意持有的机器」等于「企业想租的机器」。",
      note="课件三步：<br>"
            "① <b>初始资本 K<sub>0</sub> 给定</b>——这是模型的「起点」，也是所有动态分析的初始条件；<br>"
            "② 资本供给的演化：<span class='mj'>K^s_{t+1}=(1-\\delta)K^s_t+I_t=(1-\\delta)K^s_t+sY_t</span>；<br>"
            "③ 出清条件：<span class='mj'>K^s_t=K^d_t</span>，且 <span class='mj'>r_t&gt;0</span>。<br><br>"
            "第 ② 步是整个模型的心脏：<b>它是一个「存量」的更新方程</b>，而不是「流量」的均衡条件。所以 Solow 模型是一个<b>动态</b>模型，它的解是一条<b>路径</b> <span class='mj'>\\{K_t\\}</span>，不是一组数。",
      lr=[dict(name="资本积累（存量更新）",
               lhs="K^s_{t+1}",
               lhs_t="下一期可供使用的资本存量（<b>存量</b>）",
               rhs="(1-\\delta)K^s_t+I_t",
               rhs_t="本期资本折旧之后剩下的 + 本期新造出来的（<b>流量</b>）",
               why_t="为什么是这个形式（而不是「K 加 I」）",
               why="因为资本会<b>磨损</b>。<span class='mj'>\\delta</span> 是每期折旧掉的比例，所以剩下的比例是 <span class='mj'>1-\\delta</span>。<b>如果 δ=0</b>，式子退化成 <span class='mj'>K_{t+1}=K_t+I_t</span>——资本只增不减，那时模型就没有稳态了（资本会一直涨）。<br>"
                   "<b>正是 δ&gt;0 让「稳态」成为可能</b>：投资要先把折旧补上，才能让存量增加。第 36 页会把这句话写成 <span class='mj'>\\Delta k=sAf(k)-\\delta k</span>。")],
      dec=[
          ("<span class='mj'>\\delta</span>", "折旧率。<b>注意它作用在存量 K 上</b>（比例），所以折旧总量是 <span class='mj'>\\delta K</span>，是一条<b>过原点的直线</b>——这是第 37 页那张图的关键。"),
          ("<span class='mj'>K^s_t</span>", "资本<b>供给</b>：家庭愿意持有的资本量。它等于历史投资的累积（扣折旧），<b>在当期是定死的</b>。"),
          ("<span class='mj'>K^d_t</span>", "资本<b>需求</b>：企业想租的量，由 <span class='mj'>r=AF_K</span> 决定。它可以在当期调整。"),
      ],
      tip="这一页最重要的一句话是<b>时序</b>：<b>本期的投资，下一期才变成资本</b>。所以 <span class='mj'>K_t</span> 是「预定」（predetermined）的——它由过去的决策决定，今天的外生冲击改不了它。这直接决定了第 28、31 页的图形：<b>k 连续、不跳</b>。",
      warn="别把「资本供给」理解成「家庭今天决定持有多少资本」。在 Solow 里家庭不做资产组合选择，<b>储蓄自动变成资本</b>。所谓「资本市场出清」只是记账：家庭存下来的钱买的机器，正好是企业要租的机器。")

add(15, kp="均衡的定义：给定 <span class='mj'>\\{\\bar L_t,A_t\\},K_0,s,\\delta</span>，一条均衡路径是<b>六个变量</b>的序列，满足<b>六个方程</b>。",
      plain="这一页是把前面所有零件组装成一台机器。它说：给我初始的机器数量、给定的人口和技术、给定储蓄率和折旧率，我就能一路算下去——每一期的资本、产出、消费、投资、工资、租金都唯一确定。六个方程、六个未知数，刚好。",
      note="课件六条（<b>这就是全模型的「方程组」</b>）：<br>"
            "① <span class='mj'>K_{t+1}=(1-\\delta)K_t+I_t</span>　资本积累（动态）<br>"
            "② <span class='mj'>Y_t=A_tF(K_t,\\bar L_t)</span>　生产函数<br>"
            "③ <span class='mj'>C_t=(1-s)Y_t</span>　消费<br>"
            "④ <span class='mj'>I_t=sY_t</span>　投资<br>"
            "⑤ <span class='mj'>w_t=A_tF_L(K_t,\\bar L_t)</span>　工资<br>"
            "⑥ <span class='mj'>r_t=A_tF_K(K_t,\\bar L_t)</span>　租金<br><br>"
            "<b>解的顺序是「一层一层剥」的</b>：给定 <span class='mj'>K_t</span> → ② 得 <span class='mj'>Y_t</span> → ④ 得 <span class='mj'>I_t</span> → ① 得 <span class='mj'>K_{t+1}</span> → ③ 得 <span class='mj'>C_t</span>；而 ⑤⑥ 与动态无关，随时可算。<b>所以只要知道 K<sub>0</sub>，整条路径就唯一确定</b>。",
      dec=[
          ("<span class='mj'>K_{t+1}=(1-\\delta)K_t+I_t</span>", "<b>唯一的动态方程</b>。它把今天和明天连起来——其余五条都是「同一个 t 内部」的关系，只有它跨期。"),
          ("<span class='mj'>Y_t=A_tF(K_t,\\bar L_t)</span>", "注意这里已经用出清条件把 <span class='mj'>L^d</span> 换成了 <span class='mj'>\\bar L</span>。<b>模型里从此没有「就业」这个变量，只有人口。</b>"),
          ("<span class='mj'>C_t=(1-s)Y_t</span>", "消费不是最优化来的，是<b>剩余</b>。所以 Solow 里讨论福利必须从外部引入标准（黄金律）。"),
          ("<span class='mj'>I_t=sY_t</span>", "投资也不是最优化来的。<b>利率不影响投资</b>——这是 Solow 最不「宏观」的地方。"),
      ],
      tip="这六条要能默写。默写的技巧是<b>按「生产—分配—积累」三组记</b>：生产（②）、分配（③④⑤⑥）、积累（①）。<b>①在最前面还是最后面都行，但它是唯一跨期的，这一点必须说出来。</b>",
      warn="「均衡路径」这个词的意思是<b>一整条序列</b>，不是「一个均衡点」。答题时如果说「均衡是 K*」，那只是<b>稳态</b>这个特例；一般情况下均衡是 <span class='mj'>\\{K_t,Y_t,C_t,I_t,w_t,r_t\\}_{t=0}^{\\infty}</span>。")

add(16, kp="把六条压成<b>一条</b>：<span class='mj'>K_{t+1}=(1-\\delta)K_t+sA_tF(K_t,\\bar L_t)</span>——索洛模型的基本运动方程。",
      plain="既然投资等于储蓄、储蓄等于产出的一部分，那就把投资替换掉。于是只剩一条式子：明年的机器 = 今年没坏的机器 + 今年存下来的那部分产出。这一条式子就包含了整个模型的动态——其他所有变量都是它的「附属品」。",
      note="推导只有两步：<br>"
            "① 从 <span class='mj'>K_{t+1}=(1-\\delta)K_t+I_t</span> 出发；<br>"
            "② 把 <span class='mj'>I_t=sY_t=sA_tF(K_t,\\bar L_t)</span> 代进去。<br><br>"
            "结果就是课件的「fundamental law of motion for capital accumulation」：<br>"
            "<span class='mj'>K_{t+1}=(1-\\delta)K_t+sA_tF(K_t,\\bar L_t)</span><br><br>"
            "<b>为什么这一步很重要？</b>因为它把「六个方程的系统」变成了「<b>一个一阶非线性差分方程</b>」。一阶差分方程可以用图形分析（第 22 页）、可以求闭式解（第 25 页）、可以谈稳定性（第 23–24 页）。<b>整个 Solow 模型的可解性，全在这条式子上。</b>",
      lr=[dict(name="基本运动方程（本讲的核心）",
               lhs="K_{t+1}",
               lhs_t="下一期的资本存量",
               rhs="(1-\\delta)K_t+sA_tF(K_t,\\bar L_t)",
               rhs_t="本期未折旧的资本 + 本期储蓄转化成的投资",
               why_t="它其实在说一件很朴素的事",
               why="<b>「明年的机器 = 今年剩下的机器 + 今年新造的机器」，而新造的机器 = 存下来的产出。</b><br>"
                   "把它看成一个<b>映射</b>：给一个 <span class='mj'>K_t</span>，它就吐出一个 <span class='mj'>K_{t+1}</span>。反复迭代就得到整条路径。这个映射的形状决定了模型的一切：<b>它与 45° 线的交点就是稳态，它在 45° 线上方还是下方决定了资本是增加还是减少</b>。")],
      tip="这条式子有三个「读法」，都要会：<br>"
          "① <b>账本读法</b>：剩下的 + 新造的；<br>"
          "② <b>映射读法</b>：<span class='mj'>K_t\\mapsto K_{t+1}</span>，画在 (K<sub>t</sub>, K<sub>t+1</sub>) 平面上（第 22 页）；<br>"
          "③ <b>增长读法</b>：两边减 <span class='mj'>K_t</span> 得 <span class='mj'>\\Delta K=sAF-\\delta K</span>（第 36 页）——<b>「净投资 = 储蓄 − 折旧」</b>。",
      warn="注意这条式子里<b>没有 r</b>。利率在 Solow 里是被动变量：它由 <span class='mj'>r=AF_K</span> 决定，但<b>不影响</b>投资决策（投资由 s 决定）。这一点在 Topic 8 里会变——那里利率通过 <span class='mj'>I^d(r)</span> 影响投资。考试如果问「Solow 与 Topic 8 的投资函数有什么不同」，答案就是这一条。")

add(17, kp="两个简化：<b>人口不增长</b>（<span class='mj'>\\bar L_t=L</span>）、<b>技术不进步</b>（<span class='mj'>A_t=A</span>）。",
      plain="为了让模型能画在二维图上，先把两个「一直在变」的东西按住不动：人口不变、技术不变。这样全国的工人数就是常数，技术也是常数，于是所有变化都来自「攒机器」这一条路。等这条路的极限看清了（Part II），再把人口和技术放开。",
      note="课件一句话：<b>For simplification, we assume there is no population growth and no technological progress over time</b>，即 <span class='mj'>\\bar L_t=L</span>、<span class='mj'>A_t=A</span> 对所有 t 成立。<br><br>"
            "<b>这两条假设的作用完全不同，要分清</b>：<br>"
            "· <b>人口不增长</b>：让「人均」与「总量」只差一个常数倍，于是 <span class='mj'>K_{t+1}/L=k_{t+1}</span> 可以直接写出来（否则要处理 <span class='mj'>L_{t+1}/L_t</span>，见第 19 页的推导）；<br>"
            "· <b>技术不进步</b>：让 A 不进动态，于是 <span class='mj'>y=Af(k)</span> 这条曲线固定不动——<b>稳态才可能存在</b>。<br><br>"
            "Part II 会把这两条同时放开（<span class='mj'>n&gt;0</span>、<span class='mj'>z&gt;0</span>），代价是「人均量不再收敛到常数，而是收敛到一条匀速增长的路径」。",
      tip="为什么要先按住不动？因为<b>「资本积累单独能走多远」这个问题必须先单独回答</b>。如果一开始就放进技术进步，你就分不清增长里哪部分来自攒机器、哪部分来自技术。<b>先关掉技术，才能证明「攒机器有上限」。</b>",
      warn="这两条不是「Solow 模型的假设」，而是<b>Part I 这个版本</b>的假设。写答案时要说「在 Part I 的简化假设下」，否则会被问「那增长怎么来的」——答案就在 Part II。")

add(18, kp="人均化：<span class='mj'>k_t=K_t/\\bar L_t</span>，且由 CRTS 得 <span class='mj'>y_t=Af(k_t)</span>。",
      plain="把「总量」换成「人均」：总共有多少机器除以工人数，就是人均资本；总产出除以工人数，就是人均产出。因为规模报酬不变，人均产出只取决于人均资本这一个数——这一句话就是整张图能画出来的原因。",
      note="课件两步：<br>"
            "① 定义人均资本 <span class='mj'>k_t=K_t/\\bar L_t</span>；<br>"
            "② 用 CRTS 把人均产出写成 k 的函数：<br>"
            "<span class='mj'>y_t=\\dfrac{AF(K_t,\\bar L_t)}{\\bar L_t}=AF\\left(\\dfrac{K_t}{\\bar L_t},\\dfrac{\\bar L_t}{\\bar L_t}\\right)=AF(k_t,1)=Af(k_t)</span><br><br>"
            "<b>关键的一步是「把 L 提进函数里」</b>：因为 CRTS，<span class='mj'>F(K,L)/L=F(K/L,1)</span>。这需要先把 L 写成 <span class='mj'>\\gamma</span> 的倒数——<b>取 <span class='mj'>\\gamma=1/L</span></b>，则 <span class='mj'>F(K,L)=L\\cdot F(K/L,1)</span>，两边除 L 即得。",
      lr=[dict(name="人均生产函数（本讲最常用的式子）",
               lhs="y_t=\\dfrac{AF(K_t,\\bar L_t)}{\\bar L_t}",
               lhs_t="人均产出：总产出除以工人数",
               rhs="Af(k_t)",
               rhs_t="技术 × 只看人均资本的一元函数",
               why_t="为什么可以「除以 L」并把它变成一个自变量的函数",
               why="因为<b>规模报酬不变</b>。<span class='mj'>F</span> 是一次齐次的，所以「所有投入同时缩小 L 倍，产出也缩小 L 倍」：<span class='mj'>F(K,L)=L\\,F(K/L,1)</span>。两边同除 L 就得到 <span class='mj'>F(K,L)/L=F(k,1)\\equiv f(k)</span>。<br>"
                   "<b>这一步的意义极大</b>：它把「两个自变量的函数」压成了「一个自变量的函数」，于是模型可以画在二维平面 (k, y) 上，稳态可以用两条线的交点表示。<b>如果规模报酬递减或递增，这一步就做不了，Solow 模型的整个图形分析也就没有了。</b>")],
      dec=[
          ("<span class='mj'>k_t</span>", "人均资本（capital-labor ratio）。<b>它是模型唯一的状态变量</b>——知道它就知道了全部。"),
          ("<span class='mj'>f(k)</span>", "<b>小写 f</b>：每单位劳动的产出。<span class='mj'>f(k)\\equiv F(k,1)</span>。注意 <span class='mj'>f</span> 不含 A，A 在外面乘。"),
          ("<span class='mj'>f'(k)</span>", "<span class='mj'>f'(k)&gt;0</span>、<span class='mj'>f''(k)&lt;0</span>。第 7–8 页那七条假设，在人均形式上就是这两条 + Inada。"),
      ],
      tip="记牢这个换算：<b>总量层面的一切，除以 L 就变成人均层面的一切</b>；反过来乘 L 就回去。考试里最常见的低级错误是「<span class='mj'>r=AF_K</span> 里代入了 <span class='mj'>K/L</span> 却忘了 A」，或者把 <span class='mj'>Af(k)</span> 写成 <span class='mj'>AF(k)</span>。",
      warn="<b><span class='mj'>y=Af(k)</span> 里的 f 与 <span class='mj'>F</span> 不是同一个函数</b>：F 有两个自变量，f 只有一个。因为 f 的定义已经把「L=1」代进去了，所以 f 的形状只由技术决定。<b>写答案时两个符号不能混用。</b>")

add(19, kp="人均资本的运动方程：<span class='mj'>k_{t+1}=sAf(k_t)+(1-\\delta)k_t</span>。",
      plain="把上一条总量方程两边都除以工人数，就得到人均版本：明年的人均机器 = 今年存下来的人均产出 + 今年没坏的人均机器。这一步能做成，靠的是「人口不变」——否则分母变了，除法就不干净。",
      note="课件推导（<b>这一步的细节考试常考</b>）：<br>"
            "① 从 <span class='mj'>K_{t+1}=sAF(K_t,\\bar L_t)+(1-\\delta)K_t</span> 出发，两边除以 <span class='mj'>\\bar L_t</span>：<br>"
            "<span class='mj'>\\dfrac{K_{t+1}}{\\bar L_t}=sAf(k_t)+(1-\\delta)k_t</span><br>"
            "② 但左边是「下一期资本 ÷ <b>本期</b>人口」，不是我们要的 <span class='mj'>k_{t+1}</span>。于是乘一个 <span class='mj'>\\bar L_{t+1}/\\bar L_{t+1}</span>：<br>"
            "<span class='mj'>\\dfrac{K_{t+1}}{\\bar L_t}=\\dfrac{K_{t+1}}{\\bar L_{t+1}}\\cdot\\dfrac{\\bar L_{t+1}}{\\bar L_t}=k_{t+1}\\cdot 1</span><br>"
            "③ 因为假设 <span class='mj'>\\bar L_{t+1}=\\bar L_t</span>（人口不变），所以倍数正好是 1，左边就是 <span class='mj'>k_{t+1}</span>。<br><br>"
            "<b>结论</b>：<span class='mj'>k_{t+1}=sAf(k_t)+(1-\\delta)k_t</span>。",
      lr=[dict(name="人均资本积累方程",
               lhs="k_{t+1}",
               lhs_t="下一期的人均资本",
               rhs="sAf(k_t)+(1-\\delta)k_t",
               rhs_t="人均储蓄（=人均投资）+ 未折旧的人均资本",
               why_t="为什么右边两项都是「人均」而左边已经是「下一期」",
               why="右边两项都<b>在本期决定</b>：<span class='mj'>sAf(k_t)</span> 是本期产出的 s 比例，<span class='mj'>(1-\\delta)k_t</span> 是本期资本扣除折旧。它们加起来就是下一期的资本总量（人均）。<br>"
                   "<b>注意这里藏着一个陷阱</b>：严格说右边除以的是 <span class='mj'>\\bar L_t</span>，左边却是 <span class='mj'>\\bar L_{t+1}</span>。只有当 <span class='mj'>\\bar L_{t+1}=\\bar L_t</span> 时两者才相等。所以<b>这条式子是「无人口增长」假设的直接产物</b>——Part II 一旦让 n&gt;0，右边就要除以 <span class='mj'>(1+n)</span>（第 50 页）。")],
      tip="这条式子就是<b>整个 Solow 模型的那一条</b>。后面所有图（第 22–24、27、30、37、40 页）画的都是它的两个部分：<b>右边第一项</b>（储蓄曲线）与<b>右边第二项</b>（折旧直线）。看懂这条，五十页就都通了。",
      warn="别丢掉 <span class='mj'>(1-\\delta)k_t</span> 这一项。常见错误是写 <span class='mj'>k_{t+1}=sAf(k_t)</span>——那等于假设资本<b>一期全部折旧完</b>（δ=1）。这个错误的后果是：模型仍然有稳态，但稳态资本会小得多，而且 <span class='mj'>k</span> 的收敛路径会完全不同。")

add(20, kp="人均形式的六个均衡条件：<b><span class='mj'>r=Af'(k)</span>、<span class='mj'>w=A[f(k)-kf'(k)]</span></b>。",
      plain="把六个方程全部改写成人均版。前四条很直接（人均消费、人均投资都是人均产出的一部分）。有意思的是后两条：租金等于「人均资本的边际产出」，而工资等于「人均产出减去资本拿走的那部分」——工资是剩下的。",
      note="课件六条（<b>这一组要能默写</b>）：<br>"
            "① <span class='mj'>k_{t+1}=sAf(k_t)+(1-\\delta)k_t</span>　资本积累<br>"
            "② <span class='mj'>y_t=Af(k_t)</span>　生产<br>"
            "③ <span class='mj'>c_t=(1-s)Af(k_t)</span>　消费<br>"
            "④ <span class='mj'>i_t=sAf(k_t)</span>　投资<br>"
            "⑤ <span class='mj'>r_t=Af'(k_t)</span>　资本租金<br>"
            "⑥ <span class='mj'>w_t=Af(k_t)-k_tAf'(k_t)</span>　工资<br><br>"
            "⑤⑥ 的推导在附录（第 45 页）：一次齐次函数的偏导是<b>零次齐次</b>的，所以 <span class='mj'>F_K(K,L)=F_K(K/L,1)=f'(k)</span>；再由欧拉定理 <span class='mj'>f(k)=f'(k)k+F_L</span> 解出 <span class='mj'>F_L=f(k)-kf'(k)</span>。",
      lr=[dict(name="工资的「剩余」表达式",
               lhs="w_t",
               lhs_t="实际工资（每单位劳动的报酬）",
               rhs="Af(k_t)-k_t\\,Af'(k_t)",
               rhs_t="人均产出 − 人均资本 × 资本的边际产品 = 资本拿走之后剩下的那一块",
               why_t="为什么工资是「剩下的」",
               why="因为 CRTS 下产出被分光（第 11 页），<b>资本先按边际产品拿走 <span class='mj'>k\\cdot Af'(k)</span>，剩下的全归劳动</b>。<br>"
                   "把它写成比例形式会更直观：<span class='mj'>\\dfrac{w}{y}=1-\\dfrac{kf'(k)}{f(k)}</span>。在 Cobb-Douglas 下 <span class='mj'>kf'(k)/f(k)=\\alpha</span>，所以 <b>工资份额恒为 <span class='mj'>1-\\alpha</span></b>——这就是「劳动收入份额约 2/3」的理论来源。<br>"
                   "<b>注意 <span class='mj'>w</span> 里有两个渠道受 k 影响</b>：<span class='mj'>f(k)</span> 上升（产出多了）与 <span class='mj'>f'(k)</span> 下降（资本边际产品下降 ⇒ 资本拿走的份额下降）。<b>两个渠道同向，所以 w 一定随 k 上升</b>。")],
      dec=[
          ("<span class='mj'>r_t=Af'(k_t)</span>", "<b>只依赖 k</b>，不依赖规模。所以「资本深化」会让 r 下降——这是第 28 页「r 最终回落到原水平」以及第 34 页「反复提高 s 会让 r 一直跌」的根源。"),
          ("<span class='mj'>f'(k)</span>", "资本的边际产品。<b>它是 <span class='mj'>f</span> 曲线的斜率</b>——第 37、40 页两张图都在用这个斜率做文章。"),
          ("<span class='mj'>k_tAf'(k_t)</span>", "资本拿走的总报酬（人均）。在 Cobb-Douglas 下恰好是 <span class='mj'>\\alpha y</span>，所以 <b>α 就是资本份额</b>。"),
      ],
      tip="这六条里只有第 ① 条是动态的，其余五条都是「给定 <span class='mj'>k_t</span> 就能算出来」的静态关系。<b>这就是为什么「稳态一确定，所有变量都确定」</b>——把 <span class='mj'>k^*</span> 代进 ②–⑥ 即可（第 21 页最后一句正是这个意思）。",
      warn="<b><span class='mj'>w</span> 的式子里那个减号不能漏。</b>如果只写 <span class='mj'>w=Af(k)</span>，就等于说「全部产出都归劳动」，与零利润矛盾。检验办法：把 Cobb-Douglas 代进去，应得 <span class='mj'>w=(1-\\alpha)Ak^{\\alpha}</span>，工资份额 <span class='mj'>1-\\alpha</span>；漏掉减号会得到 <span class='mj'>w=Ak^{\\alpha}</span>，份额为 1，明显不对。")

add(21, kp="稳态（steady state）：<b><span class='mj'>k_t=k^*</span> 对所有 t 成立</b>；且从任意 <span class='mj'>k_0\\neq 0</span> 出发都会收敛到它。",
      plain="稳态就是这个模型的「终点站」：人均机器数量不再变化，每年新增的机器刚好补上磨损的机器。到了这里，产出、消费、投资、工资、租金全都不再变。而且这个终点站很「稳」——不管你从哪里出发（只要不是零），最后都会走到这里。",
      note="课件三句：<br>"
            "① <b>定义</b>：<span class='mj'>k_t=k^*</span> 对所有 t 成立；<br>"
            "② <b>稳定性</b>：对任何初始值 <span class='mj'>k_0\\neq 0</span>，<span class='mj'>k_t</span> 都会收敛到 <span class='mj'>k^*</span>。<b>这叫「全局稳定」（globally stable）</b>——不只是「附近收敛」，而是从任何起点都收敛；<br>"
            "③ <b>到了就不动</b>：<span class='mj'>k_t=k^*</span> ⇒ <span class='mj'>k_{t+1}=k^*</span>，经济「坐在」那里。<br>"
            "④ <b>其余变量随之确定</b>：把 <span class='mj'>k^*</span> 代进第 20 页的 ②–⑥，就得到 <span class='mj'>y^*,c^*,i^*,r^*,w^*</span>。",
      lr=[dict(name="稳态的定义式",
               lhs="k_{t+1}",
               lhs_t="下一期的人均资本",
               rhs="k_t=k^*",
               rhs_t="本期的人均资本，且等于常数 k*",
               why_t="稳态不是「不投资」，而是「投资刚好等于折旧」",
               why="把定义代进运动方程：<span class='mj'>k^*=sAf(k^*)+(1-\\delta)k^*</span>，两边减 <span class='mj'>(1-\\delta)k^*</span> 得 <span class='mj'>\\delta k^*=sAf(k^*)</span>。<br>"
                   "<b>这句话是整个模型最重要的一句：稳态时，总投资恰好等于总折旧。</b>投资没有停——它一直在发生，只是全部用来「补窟窿」，所以存量不变。<br>"
                   "第 36–37 页会把这句话画成图（<span class='mj'>\\Delta k=sAf(k)-\\delta k=0</span>），第 25 页会解出 <span class='mj'>k^*</span> 的闭式解。")],
      tip="为什么一定收敛？<b>因为 Inada 条件</b>（第 8 页）：<span class='mj'>f'(0)=\\infty</span> 保证曲线从左上方进入，<span class='mj'>f'(\\infty)=0</span> 保证它最终落到 45° 线下方。<b>一个连续函数从上方穿到下方，必然穿过</b>——那就是 <span class='mj'>k^*</span>；再加上凹性 ⇒ 只穿一次 ⇒ 唯一。</b>",
      warn="「稳态」不等于「最优」。<b>稳态是模型自己走到的地方，黄金律（第 39 页）才是「应该去的地方」。</b>两者通常不重合：Solow 模型里储蓄率外生，所以稳态消费一般不是最大。<b>这是期末考试最爱设的一个对比题。</b>")

add(22, kp="图形：<b>储蓄曲线与 45° 线的交点即 k*</b>；曲线在上方则 k 上升，下方则 k 下降。",
      plain="把「明年的机器」画在竖轴、「今年的机器」画在横轴。45° 线上每一点都表示「明年 = 今年」，也就是不动。另一条曲线是「按公式算出来的明年的机器」。两条线的交点就是稳态。曲线在 45° 线上方，说明明年比今年多，资本就增长；在下方说明明年比今年少，资本就缩水。",
      note="图的构造：横轴 <span class='mj'>k_t</span>，纵轴 <span class='mj'>k_{t+1}</span>。两条线：<br>"
            "① <b>45° 线</b> <span class='mj'>k_{t+1}=k_t</span>——「不动」的参照系；<br>"
            "② <b>储蓄曲线</b> <span class='mj'>k_{t+1}=sAf(k_t)+(1-\\delta)k_t</span>——模型的运动方程。<br><br>"
            "两线交点即 <span class='mj'>k^*</span>。<b>判断方向只看相对位置</b>：<br>"
            "· <span class='mj'>k_t&lt;k^*</span> 时，曲线在 45° 线上方 ⇒ <span class='mj'>k_{t+1}&gt;k_t</span> ⇒ k 上升；<br>"
            "· <span class='mj'>k_t&gt;k^*</span> 时，曲线在下方 ⇒ <span class='mj'>k_{t+1}&lt;k_t</span> ⇒ k 下降。",
      fig=[dict(name="稳态 k*：储蓄曲线与 45° 线的交点",
                axes=[("横轴", "k_t", "本期人均资本——<b>今天已经定下的存量</b>"),
                      ("纵轴", "k_{t+1}", "下一期人均资本——<b>由今天的决策决定</b>"),
                      ("45° 线", "k_{t+1}=k_t", "<b>「不动」的参照线</b>。它没有经济含义，只是一把尺子：与它比较才知道资本是在增还是在减")],
                marks=[("k_{t+1}=sAf(k_t)+(1-\\delta)k_t（凹曲线）", "模型的运动方程。<b>过原点</b>（k=0 时既无产出也无折旧）、<b>起点极陡</b>（Inada：<span class='mj'>f'(0)=\\infty</span>）、<b>越来越平</b>（<span class='mj'>f''&lt;0</span>），最终斜率趋近 <span class='mj'>1-\\delta</span>"),
                       ("交点 k*", "两条线相交 ⇒ <span class='mj'>k_{t+1}=k_t</span> ⇒ <b>稳态</b>。图中用虚线把 <span class='mj'>k^*</span> 投到两个轴上"),
                       ("交点左侧", "曲线<b>在 45° 线上方</b> ⇒ <span class='mj'>k_{t+1}&gt;k_t</span> ⇒ 资本<b>增长</b>"),
                       ("交点右侧", "曲线<b>在 45° 线下方</b> ⇒ <span class='mj'>k_{t+1}&lt;k_t</span> ⇒ 资本<b>减少</b>")],
                read="<b>只看「曲线在 45° 线哪一边」。</b>上方 = 攒得比磨损多 = k 上升；下方 = 磨损比攒得多 = k 下降；交点上 = 正好打平。<b>把这条规则记成一句话：曲线与 45° 线的「上下关系」就是 k 的「增减方向」。</b>",
                exam="三种考法：① 画出这张图并标出 <span class='mj'>k^*</span>；② 用这张图说明<b>稳态唯一</b>（要提 Inada + 凹性）；③ 把 A 或 s 变大，问曲线怎么动、<span class='mj'>k^*</span> 怎么动（第 27、30 页）。<b>答第②问时一定要说「曲线从原点上方的无穷陡处出发、最终落到 45° 线下方 ⇒ 至少一个交点；严格凹 ⇒ 至多一个交点」。</b>")],
      tip="这张图的「坐标系」很特别：<b>两个轴都是 k，只是不同期</b>。所以它不是「供给-需求」图，而是「差分方程的相图」。<b>45° 线的作用相当于「相位基准」</b>——凡是画「<span class='mj'>x_{t+1}</span> 对 <span class='mj'>x_t</span>」的图，都要先画它。",
      warn="别把这张图的纵轴写成 <span class='mj'>\\Delta k</span> 或 <span class='mj'>y</span>。<b>纵轴必须是 <span class='mj'>k_{t+1}</span></b>，否则 45° 线就没有意义。第 37 页那张图才是「产出/投资对 k」的画法——两张图长得像，但坐标系完全不同，考试特别容易混。")

add(23, kp="<span class='mj'>k_t&lt;k^*</span> 时的收敛：<b>阶梯式上升</b>，每期一步，越靠近越慢。",
      plain="这张图演示「从穷开始怎么变富」。从今年的资本出发，往上找到曲线的高度，那就是明年的资本；然后横着走到 45° 线上，再往下回到横轴，就是明年的起点。重复这个过程，就得到一串越来越高的值，但每步的涨幅越来越小，最后停在稳态上。",
      note="课件的作图法（<b>四步一循环</b>）：<br>"
            "① 从横轴上的 <span class='mj'>k_t</span> 竖直向上，碰到<b>曲线</b>，读纵坐标 ⇒ 得到 <span class='mj'>k_{t+1}</span>；<br>"
            "② 从该点<b>水平</b>走到 45° 线上；<br>"
            "③ 从 45° 线上的点<b>竖直向下</b>回到横轴 ⇒ 这就是下一期的起点；<br>"
            "④ 重复。<br><br>"
            "因为曲线在 45° 线上方，所以每一轮的 <span class='mj'>k_{t+1}&gt;k_t</span>，阶梯<b>单调上升</b>。而曲线越来越平（<span class='mj'>f''&lt;0</span>），所以<b>每步的涨幅递减</b>——这就是「收敛速度递减」的图形表达。",
      fig=[dict(name="从 k_t < k* 出发：阶梯式收敛（单调上升）",
                axes=[("横轴", "k_t", "各期的人均资本。图上标了 <span class='mj'>k_t,k_{t+1},k_{t+2},k_{t+3}</span> 一路到 <span class='mj'>k^*</span>"),
                      ("纵轴", "k_{t+1}", "下一期的人均资本。纵轴上也对应标了 <span class='mj'>k_{t+1},k_{t+2},k_{t+3}</span>"),
                      ("两条线", "45° 线与储蓄曲线", "与第 22 页相同。<b>曲线在左段位于 45° 线上方</b>，这是本图的全部动力")],
                marks=[("红色箭头 Initial point in period t", "从 <span class='mj'>k_t</span> 处指向曲线：<b>「今年在这里，明年到那里」</b>。四支箭头对应 t、t+1、t+2、t+3 四期"),
                       ("竖直虚线", "把每一期的 <span class='mj'>k</span> 投到横轴。<b>虚线的间距就是每期的增幅</b>——越来越窄 ⇒ 增长越来越慢"),
                       ("水平虚线", "把曲线上的点投到纵轴，读出下一期的值；也是「水平走到 45° 线」的那一步"),
                       ("k*", "阶梯的终点。<b>到了这里箭头就停了</b>：曲线与 45° 线相交，明年 = 今年")],
                read="<b>跟着阶梯走一遍，注意两件事：方向朝上（因为曲线在上方）、步长变短（因为曲线变平）。</b>前者说明「穷国会追赶」，后者说明「追赶会减速」——这两个结论合起来就是「条件收敛」的几何来源（Topic 3 会用）。",
                exam="常考两问：① 在图上画出收敛路径（<b>必须画阶梯，不能画一条平滑曲线</b>——这是离散时间模型）；② 问「为什么越靠近 k* 增长越慢」——因为 <span class='mj'>f'(k)</span> 递减，同样的储蓄率带来的 <span class='mj'>\\Delta k</span> 越来越小，<b>用数学说就是 <span class='mj'>\\Delta k=sAf(k)-\\delta k</span> 对 k 的导数在 <span class='mj'>k^*</span> 处为负</b>。")],
      tip="阶梯的<b>疏密</b>就是「收敛速度」。曲线在 <span class='mj'>k^*</span> 附近的斜率越接近 1，收敛越慢。<b>定量结论：Cobb-Douglas 下收敛速度约为 <span class='mj'>(1-\\alpha)(n+z+\\delta)</span>，α=1/3 时每年约 4–5%（半程收敛约 15 年）</b>——这个数在 Topic 3 会用来对比「现实中收敛太慢」的谜题。",
      warn="图是从<b>下面</b>逼近的（单调上升，不超调）。<b>这是 Solow 的一个性质：一阶差分方程 + 单调映射 ⇒ 不会越过稳态。</b>如果模型里加了「预期」或「资本调整成本」，就可能在稳态附近震荡（Topic 7 的投资理论）。考试如果问「会不会超调」，答案是「Solow 里不会」。")

add(24, kp="<span class='mj'>k_t&gt;k^*</span> 时的收敛：<b>阶梯式下降</b>，同样越靠近越慢。",
      plain="反过来：如果一开始机器太多（比如战后资本被炸毁前的富裕国家，或者被过度投资的经济），磨损比新增的多，人均机器会逐年减少。同样是每期一步，最后也停在同一个稳态上——<b>从上面下来，从下面上去，终点是同一个</b>。这就是「全局稳定」。",
      note="作图法与第 23 页完全一样，只是方向相反：曲线在 45° 线<b>下方</b>，所以 <span class='mj'>k_{t+1}&lt;k_t</span>，阶梯<b>单调下降</b>。<br><br>"
            "<b>这一页和第 23 页合起来才构成完整的稳定性论证</b>：<br>"
            "· 第 23 页证明「在左边会往右走」；<br>"
            "· 第 24 页证明「在右边会往左走」；<br>"
            "· 两页合起来 ⇒ <b>无论从哪里出发都收敛到同一个 <span class='mj'>k^*</span> ⇒ 全局稳定</b>。<br><br>"
            "课件在这里没有文字说明，只有图——<b>但它传达的信息比文字更重要：稳态是「吸引子」（attractor）。</b>",
      fig=[dict(name="从 k_t > k* 出发：阶梯式收敛（单调下降）",
                axes=[("横轴", "k_t", "各期人均资本，从较大的 <span class='mj'>k_t</span> 开始，向 <span class='mj'>k^*</span> 靠近"),
                      ("纵轴", "k_{t+1}", "下一期人均资本，逐期下降"),
                      ("两条线", "45° 线与储蓄曲线", "<b>这一次曲线在右段位于 45° 线下方</b>——因为折旧 <span class='mj'>\\delta k</span> 随 k 线性增长，而储蓄 <span class='mj'>sAf(k)</span> 增长越来越慢")],
                marks=[("红色箭头 Initial point in period t", "从 <span class='mj'>k_t</span> 指向曲线：<b>明年比今年少</b>。箭头方向朝左下方"),
                       ("k_t 与 k* 的相对位置", "<span class='mj'>k_t</span> 在最右，然后 <span class='mj'>k_{t+1}</span>、<span class='mj'>k_{t+2}</span> 依次向左靠近 <span class='mj'>k^*</span>"),
                       ("竖直虚线", "间距逐期变窄 ⇒ <b>收缩速度也在递减</b>（离稳态越近，调整越慢）")],
                read="<b>与第 23 页对照着看：一张是「从穷往上爬」，一张是「从富往下滑」，终点同一个点。</b>两张图合起来才是「全局稳定」。",
                exam="常考：「证明 Solow 模型的稳态是全局稳定的」。<b>标准答法</b>：① 写出 <span class='mj'>\\Delta k=sAf(k)-\\delta k</span>；② 说明 <span class='mj'>\\Delta k</span> 在 <span class='mj'>k^*</span> 左侧为正、右侧为负（因为 <span class='mj'>sAf(k)</span> 凹、<span class='mj'>\\delta k</span> 线性）；③ 由 Inada 条件保证 <span class='mj'>k^*</span> 存在且唯一；④ 故 <span class='mj'>k_t</span> 单调收敛到 <span class='mj'>k^*</span>。")],
      tip="为什么会有「资本过多」这种情形？现实中：<b>战后资本被毁（从左边开始）、或者某段时期过度投资（从右边开始）</b>。Solow 说这两种情形都会自动纠正——<b>不需要任何政策</b>。这也正是它被批评的地方：它太「自动」了，解释不了为什么有些国家长期陷在低资本状态。",
      warn="「从右边收敛」<b>不代表</b>「资本过多是坏事」。要判断好坏必须比黄金律（第 39 页）：<b>如果 <span class='mj'>k^*&gt;k^*_{GR}</span>，那才是真的过度积累（动态无效）。</b>Solow 的稳态本身没有效率含义。")

add(25, kp="Cobb-Douglas 下可以解出<b>闭式稳态</b>：<span class='mj'>k^*=(sA/\\delta)^{1/(1-\\alpha)}</span>。",
      plain="如果生产函数是柯布-道格拉斯，那么稳态可以写成一条明确的公式。这条公式极有用：给你储蓄率、技术、折旧率和资本份额，你就能直接算出稳态的人均资本、产出、消费、投资、工资、租金，一个都不用画图。",
      note="推导（<b>三步，要会</b>）：<br>"
            "① <span class='mj'>y=Ak^{\\alpha}</span>，代入稳态条件 <span class='mj'>\\delta k^*=sA(k^*)^{\\alpha}</span>；<br>"
            "② 两边除以 <span class='mj'>(k^*)^{\\alpha}</span>：<span class='mj'>\\delta (k^*)^{1-\\alpha}=sA</span>；<br>"
            "③ 解出 <span class='mj'>k^*=\\left(\\dfrac{sA}{\\delta}\\right)^{\\frac{1}{1-\\alpha}}</span>。<br><br>"
            "其余五个稳态值直接代入：<br>"
            "<span class='mj'>y^*=A(k^*)^{\\alpha}</span>、<span class='mj'>c^*=(1-s)A(k^*)^{\\alpha}</span>、<span class='mj'>i^*=sA(k^*)^{\\alpha}</span>、"
            "<span class='mj'>r^*=\\alpha A(k^*)^{\\alpha-1}</span>、<span class='mj'>w^*=(1-\\alpha)A(k^*)^{\\alpha}</span>。",
      lr=[dict(name="稳态人均资本（闭式解）",
               lhs="k^*",
               lhs_t="稳态人均资本",
               rhs="\\left(\\dfrac{sA}{\\delta}\\right)^{\\frac{1}{1-\\alpha}}",
               rhs_t="储蓄率 × 技术 ÷ 折旧率，再开 <span class='mj'>1-\\alpha</span> 次方",
               why_t="这条公式怎么读（每个参数的方向）",
               why="<b>四个参数，方向都能一眼看出</b>：<br>"
                   "· <span class='mj'>s\\uparrow</span> ⇒ <span class='mj'>k^*\\uparrow</span>（存得多）；<br>"
                   "· <span class='mj'>A\\uparrow</span> ⇒ <span class='mj'>k^*\\uparrow</span>（产出多）；<br>"
                   "· <span class='mj'>\\delta\\uparrow</span> ⇒ <span class='mj'>k^*\\downarrow</span>（磨损快）；<br>"
                   "· <span class='mj'>\\alpha\\uparrow</span> ⇒ 指数 <span class='mj'>\\frac{1}{1-\\alpha}</span> 变大 ⇒ <b>同样的 s 变化带来更大的 k* 变化</b>（资本越重要，积累越有效）。<br>"
                   "<b>特别注意 α 只在指数上</b>——这说明 α 影响的是「弹性」（<span class='mj'>s</span> 变化 1% 带来 k* 变化 <span class='mj'>\\frac{1}{1-\\alpha}</span>%），而不是水平。")],
      dec=[
          ("<span class='mj'>(k^*)^{1-\\alpha}=sA/\\delta</span>", "把稳态条件整理成「k 的幂 = 参数」的形式。<b>这一步是解题的关键技巧</b>：先化成幂函数，再开方。"),
          ("<span class='mj'>r^*=\\alpha A(k^*)^{\\alpha-1}</span>", "代进 <span class='mj'>k^*</span> 后可以化简为 <b><span class='mj'>r^*=\\alpha\\delta/s</span></b>——<b>与 A 无关！</b>这是本讲最漂亮的一个结论，第 28 页会用到。"),
          ("<span class='mj'>w^*=(1-\\alpha)A(k^*)^{\\alpha}</span>", "等于 <span class='mj'>(1-\\alpha)y^*</span>。<b>工资份额恒为 <span class='mj'>1-\\alpha</span></b>，与 k 无关——这就是「劳动份额长期稳定」这个事实的模型版本。"),
      ],
      tip="<b>记住这个化简：<span class='mj'>r^*=\\alpha\\delta/s</span>。</b>推导：<span class='mj'>r^*=\\alpha A(k^*)^{\\alpha-1}</span>，而 <span class='mj'>(k^*)^{1-\\alpha}=sA/\\delta</span> ⇒ <span class='mj'>(k^*)^{\\alpha-1}=\\delta/(sA)</span> ⇒ 代回得 <span class='mj'>r^*=\\alpha A\\cdot\\delta/(sA)=\\alpha\\delta/s</span>。<br>"
          "<b>它的含义：在 Cobb-Douglas 下，稳态利率只由 α、δ、s 决定，与生产率 A 无关。</b>所以 <b>↑A 长期不改变 r</b>——这正是第 28 页「r 跳升后回落到原水平」的数学根据。<b>考试如果给数值让你算「A 提高后的 r」，别急着算 k，先看这条。</b>",
      warn="这条闭式解<b>只对 Cobb-Douglas 成立</b>。一般函数下 <span class='mj'>k^*</span> 只能隐式定义（<span class='mj'>\\delta k=sAf(k)</span>），解不出显式表达式。<b>答题时如果题目没说生产函数形式，就不能写这个开方公式。</b>")

add(26, kp="实验协议：<b>从稳态出发 → 参数永久性变化 → 看新稳态与转型路径</b>。只做 A 与 s。",
      plain="接下来要做两个「如果」实验：如果技术变好了会怎样？如果大家更爱存钱了会怎样？做法有讲究：先让经济待在原来的稳态上，然后某一天参数突然变、并且一直保持新的水平，再看它怎么一步步走到新的稳态。",
      note="课件四句：<br>"
            "① 外生给定的有五个：<span class='mj'>A,\\bar L,K_0,s,\\delta</span>；<br>"
            "② 但<b>值得做的只有 A 与 s</b>——因为 <span class='mj'>\\bar L</span> 在长期不变、<span class='mj'>K_0</span> 只影响起点不影响终点、<span class='mj'>\\delta</span> 是技术参数；<br>"
            "③ 实验设计：<b>经济从稳态出发</b>；<b>在 t 期发生永久性（permanent）变化</b>；<br>"
            "④ 看两件事：<b>新稳态在哪</b>（比较静态）＋<b>怎么从旧稳态走到新稳态</b>（转型动态，transitional dynamics）。",
      tip="「稳态比较」与「转型路径」是<b>两个不同的问题</b>，考试经常分开问：<br>"
          "· <b>比较静态</b>：只问 <span class='mj'>k^*</span> 从多少变成多少——用第 25 页的公式或第 22 页的图；<br>"
          "· <b>转型动态</b>：问每一期怎么变、哪些变量跳、哪些连续——用第 28、31 页的六面板图。<br>"
          "<b>最容易的失分点是把两者混在一起答。</b>",
      warn="「永久性变化」这个前提不能省。如果是<b>暂时</b>的冲击（比如只有一期 A 高），结论完全不同：<span class='mj'>k</span> 会稍微上升一点，然后随着 A 回落而慢慢退回原稳态，<b>最终什么都没变</b>。Solow 没有预期机制，所以「暂时」与「永久」的差别只体现在路径长度上，但结论差别很大。")

add(27, kp="↑A：<b>储蓄曲线整体上移</b> ⇒ 交点右上移 ⇒ <span class='mj'>k^*</span> 上升。",
      plain="技术变好，等于同样的机器和人工能产出更多，于是同样储蓄率下存下来的东西也更多。图上表现为整条储蓄曲线往上抬。它和 45° 线的交点就跑到右上方去了——新稳态的人均资本更高。注意：今天（冲击当期）的资本还是老样子，变的是「明年会有多少」。",
      note="机制链条（<b>要能一口气说完</b>）：<br>"
            "<span class='mj'>A\\uparrow</span> ⇒ 同一个 <span class='mj'>k</span> 下 <span class='mj'>Af(k)\\uparrow</span> ⇒ 储蓄 <span class='mj'>sAf(k)\\uparrow</span> ⇒ 运动方程给出的 <span class='mj'>k_{t+1}</span> 变大 ⇒ 曲线整体上移。<br><br>"
            "图上关键的三条竖线：<br>"
            "· <span class='mj'>k_t=k^*_0</span>：<b>今天的起点</b>（旧稳态，资本没变）；<br>"
            "· <span class='mj'>k_{t+1}</span>：<b>下一期</b>的位置（已经高于起点）；<br>"
            "· <span class='mj'>k^*_1</span>：<b>新稳态</b>（最终目的地）。<br><br>"
            "注意纵轴上也标了 <span class='mj'>k_{t+1},k_{t+2},k^*_1</span>——<b>这三个值说明「路径是从旧稳态出发、一期一期爬向新稳态」</b>。",
      fig=[dict(name="↑A 对 k* 的影响（曲线整体上移）",
                axes=[("横轴", "k_t", "本期人均资本。标了 <span class='mj'>k_t=k^*_0</span>（起点）、<span class='mj'>k_{t+1}</span>（下一期）、<span class='mj'>k^*_1</span>（新稳态）"),
                      ("纵轴", "k_{t+1}", "下一期人均资本。对应标了 <span class='mj'>k_{t+1},k_{t+2},k^*_1</span>"),
                      ("45° 线", "k_{t+1}=k_t", "<b>不动的那条线</b>——A 变了它不动，所以交点只能沿着它移动")],
                marks=[("黑色曲线 k_{t+1}=sA_0f(k_t)+(1-\\delta)k_t", "<b>原稳态的曲线</b>（A<sub>0</sub>）"),
                       ("蓝色曲线 k_{t+1}=sA_1f(k_t)+(1-\\delta)k_t", "<b>冲击后的曲线</b>（A<sub>1</sub>&gt;A<sub>0</sub>）。<b>整条上移</b>，不是平移——因为 <span class='mj'>sAf(k)</span> 是被乘上去的，k 越大抬得越多"),
                       ("蓝色向上箭头", "标在两条曲线之间，<b>表示「同一 k 下 <span class='mj'>k_{t+1}</span> 变高了」</b>——这就是上移的方向"),
                       ("原交点", "<span class='mj'>k^*_0</span>：A<sub>0</sub> 时的稳态"),
                       ("新交点", "<span class='mj'>k^*_1</span>：A<sub>1</sub> 时的稳态，<b>在右上方</b>")],
                read="<b>先看哪条线动了（蓝线）、再看交点往哪跑（右上）。</b>但要记住：<b>交点的移动是「最终结果」，不是「当期结果」</b>——当期 k 还停在原处，只是下一期开始变大。",
                exam="考法：① 画出这张图并说明 <span class='mj'>k^*</span> 上升；② 问「为什么当期 k 不动」——<b>因为 k 是存量、预定</b>；③ 结合第 25 页公式，问 <span class='mj'>k^*</span> 上升多少（<span class='mj'>k^*=(sA/\\delta)^{1/(1-\\alpha)}</span>，A 提高 10% ⇒ k* 提高 <span class='mj'>1.1^{1/(1-\\alpha)}</span> 倍，α=1/3 时约 15%）。")],
      tip="<b>↑A 与 ↑s 在这张图上「看起来一模一样」，这是本讲最大的视觉陷阱。</b>两者都是乘性放大（一个乘 A、一个乘 s），所以曲线形状相同、只是高点。区别要到「转型动态」里才看得出来：<b>A↑ 让 c 跳升，s↑ 让 c 跳降</b>（第 28、31 页）。",
      warn="曲线的移动<b>不是平行移动</b>。因为 <span class='mj'>sAf(k)</span> 表示「每一单位 k 的产出都乘以 A」，所以 k 越大、上移的幅度越大。<b>考试如果画成平行上移，会被扣分。</b>")

add(28, kp="↑A 的六面板：<b>k 连续上升；y、c、i、w 当期跳升后继续涨；r 当期跳升后回落</b>。",
      plain="这张图是本讲的「全家福」：六个变量在同一个冲击下的时间路径。规律很清楚——机器数量（k）不能跳，只能慢慢涨；产量、消费、投资、工资都可以立刻跳；利率会先跳高，然后慢慢退回原来的水平。为什么利率会退回去？因为机器越攒越多，每台机器的用处就越来越小。",
      note="六个面板，逐个说（<b>这是必考的一张图</b>）：<br>"
            "① <b><span class='mj'>k_t</span></b>：<b>连续</b>（t 期无跳变），从 <span class='mj'>k^*_0</span> 单调爬向 <span class='mj'>k^*_1</span>。<b>因为 k 是存量、预定</b>；<br>"
            "② <b><span class='mj'>y_t</span></b>：<b>t 期跳升</b>（<span class='mj'>y=Af(k)</span>，A 变大 ⇒ 同一 k 产出更多），然后<b>继续上升</b>（k 也在涨）；<br>"
            "③ <b><span class='mj'>c_t</span></b>：同 y（<span class='mj'>c=(1-s)y</span>，比例不变）——跳升 + 继续涨；<br>"
            "④ <b><span class='mj'>i_t</span></b>：同 y（<span class='mj'>i=sy</span>）——跳升 + 继续涨；<br>"
            "⑤ <b><span class='mj'>w_t</span></b>：<b>跳升</b>（<span class='mj'>w=AF_L</span>，A 直接放大劳动的边际产品），然后继续涨（k 上升使 <span class='mj'>F_L</span> 上升——因为 <span class='mj'>F_{KL}&gt;0</span>）；<br>"
            "⑥ <b><span class='mj'>r_t</span></b>：<b>跳升</b>（<span class='mj'>r=Af'(k)</span>，A↑），然后<b>逐步回落</b>到原来的水平（k 上升使 <span class='mj'>f'(k)</span> 下降）。",
      fig=[dict(name="↑A 的六个动态响应（2 列 × 3 行）",
                axes=[("横轴（六个面板共用）", "时间（time）", "时间。每条竖虚线标出冲击时点 <span class='mj'>t</span>"),
                      ("纵轴", "k_t,\\ y_t,\\ c_t,\\ i_t,\\ w_t,\\ R_t", "六个变量各自的时间路径。虚线是各自的稳态水平（下标 0 = 原稳态，1 = 新稳态）"),
                      ("颜色", "蓝色曲线 = 冲击后", "t 之前是黑色水平线（旧稳态），t 之后是蓝色曲线")],
                marks=[("k_t 面板", "<b>唯一「不跳」的面板</b>：在 t 处只是<b>折了一个弯</b>（斜率从 0 变成正），然后在 <span class='mj'>k^*_1</span> 处重新变平"),
                       ("y_t / c_t / i_t 面板", "三者<b>形状几乎相同</b>：t 处<b>竖直跳升</b>，然后继续向上弯，趋近新高稳态。<b>因为三者都是 y 的固定比例</b>"),
                       ("w_t 面板", "同样跳升 + 继续涨。<b>跳升来自 A，继续涨来自 k</b>"),
                       ("R_t 面板", "<b>唯一「先跳高、再回落」的面板</b>：t 处跳到最高，然后<b>单调下降回到 <span class='mj'>R^*_0</span></b>（图上的虚线就是原水平）")],
                read="<b>把六个面板分成三类看</b>：① <b>连续型</b>（k）；② <b>跳升 + 继续涨型</b>（y、c、i、w）；③ <b>跳升 + 回落型</b>（r）。<b>分类的依据是「这个变量的公式里谁是预定的、谁是当场决定的」。</b>",
                exam="这是<b>最常考的一张图</b>，问法有三种：① 「哪些变量在冲击当期跳变？」——除 k 外全部；② 「为什么 r 最终回到原水平？」——<b>因为 Cobb-Douglas 下 <span class='mj'>r^*=\\alpha\\delta/s</span>，与 A 无关</b>（第 25 页）；③ 「为什么 w 一直不回落而 r 回落？」——<b>w 的公式里有 <span class='mj'>f(k)</span>（随 k 涨），r 的公式里只有 <span class='mj'>f'(k)</span>（随 k 跌）</b>。")],
      tip="判断「跳不跳」的<b>通用口诀</b>：<b>看这个变量在 t 期的公式里，有没有「预定量」k<sub>t</sub> 之外的东西变了。</b>k<sub>t</sub> 不变，但 A 变了 ⇒ 凡是公式里有 A 的当期都会跳；k 要到 t+1 才变 ⇒ 凡是只通过 k 起作用的，只能慢慢变。<b>r 同时受两者影响，所以先跳后落。</b>",
      warn="注意 <span class='mj'>r</span> 面板的虚线在原水平上——<b>不是新水平</b>。这说明 <b>r 的长期水平没变</b>。这一点很多人画错，画成「r 跳到新稳态的更高水平」。<b>只有 s 变化才会改变长期 r（第 31 页是下降的）。</b>")

add(29, kp="五句话解释图形：<b>k 预定、y 当期跳、c/i 随 y、r 跳后回落、w 一路涨</b>。",
      plain="这一页是把上面那张图用文字说一遍，每句都在回答「为什么」。最值得记的是关于利率的那句：它一开始跳高，是因为技术变好让机器更值钱；后来慢慢回落，是因为机器越攒越多，多到每台机器的稀缺性回到原样。",
      note="课件五句，逐句解释：<br><br>"
            "① <b>「当 A 在 t 期上升时，k<sub>t</sub> 当期不变——因为它是预定的；但未来各期会上升，直到达到一个永久更高的水平。」</b><br>"
            "→ 关键词 <b>predetermined</b>：k 是上一期决策的结果，今天改不了。<br><br>"
            "② <b>「y<sub>t</sub> 当期跳升（因为 y=Af(k)），之后还因 A 更高与 k 上升而继续上升。」</b><br>"
            "→ <b>两个渠道叠加</b>：A 的<b>直接</b>效应（当期）+ k 的<b>间接</b>效应（后续）。<br><br>"
            "③ <b>「c 与 i 的动态与 y 类似，因为各自都是 y 的一个固定比例。」</b><br>"
            "→ <span class='mj'>c=(1-s)y</span>、<span class='mj'>i=sy</span>，<b>比例不变 ⇒ 形状相同，只差一个倍数</b>。<br><br>"
            "④ <b>「r<sub>t</sub> 一开始跳升（因为 r=Af'(k)），但最终会回落到原水平（见代数例子）。」</b><br>"
            "→ 这是<b>两个反向效应</b>：A↑ 推高 r，k↑ 压低 r（<span class='mj'>f''&lt;0</span>）。长期里 k 涨到把 A 的效果完全抵消——<b>第 25 页的 <span class='mj'>r^*=\\alpha\\delta/s</span> 说明这不是巧合，而是 Cobb-Douglas 的必然</b>。<br><br>"
            "⑤ <b>「w<sub>t</sub> 当期跳升（w=AF<sub>L</sub>），之后继续上升，因为 A 更高且 K 上升。」</b><br>"
            "→ 两个渠道<b>同向</b>：<span class='mj'>A↑</span> 与 <span class='mj'>K↑</span>（通过 <span class='mj'>F_{KL}&gt;0</span>）都提高劳动的边际产品。所以 <b>w 不会回落</b>。",
      lr=[dict(name="为什么 r 会回落而 w 不会（关键对比）",
               lhs="r_t=Af'(k_t)",
               lhs_t="资本租金：技术 × 资本的边际产品",
               rhs="w_t=A\\left[f(k_t)-k_tf'(k_t)\\right]",
               rhs_t="工资：技术 × 劳动的边际产品（= 产出减资本报酬）",
               why_t="同一次冲击，为什么两个价格走势相反",
               why="看两个公式里 <span class='mj'>k</span> 出现的位置：<br>"
                   "· <span class='mj'>r</span> 只依赖 <span class='mj'>f'(k)</span>，而 <span class='mj'>f'</span> <b>随 k 递减</b> ⇒ k 越涨，r 越被压低。<b>长期里 k 的上升正好抵消 A 的上升</b>（Cobb-Douglas 下精确抵消）。<br>"
                   "· <span class='mj'>w</span> 依赖 <span class='mj'>f(k)-kf'(k)</span>，这一项<b>随 k 递增</b>（因为 <span class='mj'>f</span> 上升、<span class='mj'>kf'</span> 下降，两者同向）⇒ k 越涨，w 越高。<b>与 A 的效应同向，所以 w 一路涨到底。</b><br>"
                   "一句话：<b>资本变多对资本是坏事（租金跌）、对劳动是好事（工资涨）</b>。这就是「资本深化」的分配含义。")],
      tip="把这五句压缩成一句口诀：<b>「存量慢、流量跳、资本价格回原点、劳动价格一路上。」</b>考试时先写这句，再逐条展开，条理分就拿到了。",
      warn="第①句里「k<sub>t</sub> 不变」<b>只针对冲击当期</b>。很多人误答成「k 永远不变」——那等于说没有转型。正确说法是：<b>当期不变、之后逐期上升、最终停在新稳态</b>。")

add(30, kp="↑s：<b>储蓄曲线按比例上移</b> ⇒ <span class='mj'>k^*</span> 上升（与 ↑A 图形几乎相同）。",
      plain="储蓄率提高，等于在同样的产出里存下更大的一块。图上也是整条曲线上抬、交点右上移，看起来和上一张一模一样。但含义不同：技术变好是「饼变大了」，储蓄率提高是「存的比例变大了」——饼没变大，只是分法变了。",
      note="机制：<span class='mj'>s\\uparrow</span> ⇒ <span class='mj'>sAf(k)\\uparrow</span>（同一个 k 下储蓄更多）⇒ 曲线整体上移 ⇒ <span class='mj'>k^*</span> 上升。<br><br>"
            "<b>与 ↑A 的图形差别只有一处</b>：曲线上的标签从 <span class='mj'>sA_1f(k)</span> 换成了 <span class='mj'>s_1Af(k)</span>。<b>数学上是同一个乘法</b>（都是乘一个常数），所以形状完全一样。<br><br>"
            "<b>经济含义的差别很大</b>：<br>"
            "· <span class='mj'>A\\uparrow</span>：<b>同样的投入产出更多</b>——饼变大了，<b>y 当期就跳升</b>；<br>"
            "· <span class='mj'>s\\uparrow</span>：<b>产出没变</b>，只是把更多产出拿去投资——<b>y 当期一点都不跳</b>（因为 <span class='mj'>y=Af(k)</span>，A 和 k 都没变），只有 i 跳。<b>这是两张图「看起来一样、结论不同」的关键。</b>",
      fig=[dict(name="↑s 对 k* 的影响（与 ↑A 图形同形、含义不同）",
                axes=[("横轴", "k_t", "本期人均资本。同样标了 <span class='mj'>k_t=k^*_0</span>、<span class='mj'>k_{t+1}</span>、<span class='mj'>k^*_1</span>"),
                      ("纵轴", "k_{t+1}", "下一期人均资本"),
                      ("45° 线", "k_{t+1}=k_t", "不动。<b>s 变化不改变它</b>")],
                marks=[("黑色曲线 k_{t+1}=s_0Af(k_t)+(1-\\delta)k_t", "原储蓄率下的运动方程"),
                       ("蓝色曲线 k_{t+1}=s_1Af(k_t)+(1-\\delta)k_t", "<b>s<sub>1</sub>&gt;s<sub>0</sub></b>：整条曲线<b>按比例</b>上移。<b>注意 k=0 处两条曲线仍然都过原点</b>——没有资本就没有产出，也就没有储蓄"),
                       ("蓝色向上箭头", "「同一 k，k<sub>t+1</sub> 更高」"),
                       ("新交点 k^*_1", "在右上方。<b>s 提高 ⇒ 长期资本更多</b>，但注意 <b>k* 的上升幅度小于 s 的上升幅度</b>（因为递减报酬）")],
                read="<b>与第 27 页逐条对照：曲线动的方向一样、交点动的方向一样，只有「哪条曲线是新的」不一样。</b>真正的区别在下一页的时间路径里。",
                exam="考法：① 画图；② <b>对比题</b>「↑A 与 ↑s 对 k* 的影响有何异同」——<b>同：曲线都上移、k* 都上升；异：A 提高当期产出、s 不提高当期产出，且 s 会压低长期 r 而 A 不会</b>；③ 结合公式问「s 从 0.2 提到 0.4，k* 变几倍」——<span class='mj'>k^*\\propto s^{1/(1-\\alpha)}</span> ⇒ 提高 <span class='mj'>2^{1.5}\\approx 2.83</span> 倍。")],
      tip="记住这个对称性：<b><span class='mj'>k^*=\\left(\\frac{sA}{\\delta}\\right)^{\\frac{1}{1-\\alpha}}</span> 里 s 与 A 是「对称」的</b>——它们以乘积形式出现，所以「s 翻倍」与「A 翻倍」对 <span class='mj'>k^*</span> 的影响完全相同。<b>但对 <span class='mj'>y^*</span> 就不对称了</b>：A 翻倍使 <span class='mj'>y^*</span> 提高 <span class='mj'>2\\cdot 2^{\\alpha/(1-\\alpha)}</span> 倍，s 翻倍只提高 <span class='mj'>2^{\\alpha/(1-\\alpha)}</span> 倍。",
      warn="↑s 一定能提高 <span class='mj'>k^*</span>，但<b>不一定提高 <span class='mj'>c^*</span></b>。<span class='mj'>c^*=(1-s)y^*</span> 里 <span class='mj'>1-s</span> 在降、<span class='mj'>y^*</span> 在升，<b>净效应取决于 s 是否超过黄金律</b>（第 39–40 页）。<b>这是「储蓄率越高越好」这个直觉的反例，考试常设陷阱。</b>")

add(31, kp="↑s 的六面板：<b>k、y 连续上升；c 当期<b>跳降</b>；i 当期跳升；r 当期<b>跳降</b>并继续下降</b>。",
      plain="这张图与第 28 页的六面板几乎一样，只有两处不同，而这两处正是全部考点：<b>消费在冲击当期是往下跳的</b>（因为要存更多，当期就得少花），<b>利率在冲击当期是往下跳的</b>（因为机器变多，租金变便宜）。而且利率不会回来，会一直待在更低的水平。",
      note="逐面板：<br>"
            "① <b><span class='mj'>k_t</span></b>：连续上升（同 ↑A）；<br>"
            "② <b><span class='mj'>y_t</span></b>：<b>连续上升，当期不跳</b>（<span class='mj'>y=Af(k)</span>，A 与 k 都没变）——<b>这是与 ↑A 的第一处根本差别</b>；<br>"
            "③ <b><span class='mj'>c_t</span></b>：<b>当期跳降</b>（<span class='mj'>c=(1-s)y</span>，y 不变而 <span class='mj'>1-s</span> 变小），之后随 y 上升而回升，<b>最终可能高于或低于原水平</b>（图上画的是略高）；<br>"
            "④ <b><span class='mj'>i_t</span></b>：<b>当期跳升</b>（<span class='mj'>i=sy</span>，y 不变而 s 变大），之后随 y 继续上升；<br>"
            "⑤ <b><span class='mj'>w_t</span></b>：<b>当期不跳</b>（<span class='mj'>w=Af(k)-kAf'(k)</span>，A、k 都没变），之后随 k 上升；<br>"
            "⑥ <b><span class='mj'>r_t</span></b>：<b>当期跳降</b>（<span class='mj'>r=Af'(k)</span> 里 k 没变——等等，k 没变，r 为什么跳？）<br>"
            "→ <b>关键细节</b>：r 在 t 期跳降，是因为「储蓄意愿上升 ⇒ 资本供给增加 ⇒ 租金被压低」，这是<b>资本市场出清的即时效应</b>（<span class='mj'>K^s</span> 在模型中由储蓄决定）。之后随 k 继续上升，r 一路降到 <span class='mj'>r^*_1</span>。",
      fig=[dict(name="↑s 的六个动态响应（与 ↑A 对照着看）",
                axes=[("横轴（共用）", "时间（time）", "时间，竖虚线是冲击时点 t"),
                      ("纵轴", "k_t,\\ y_t,\\ c_t,\\ i_t,\\ w_t,\\ R_t", "六个变量。虚线标出 <span class='mj'>c^*_0/c^*_1</span>、<span class='mj'>R^*_0/R^*_1</span> 等"),
                      ("颜色", "蓝色 = 冲击后", "t 之前黑色水平，t 之后蓝色")],
                marks=[("k_t 与 y_t 面板", "<b>都不跳</b>，只是斜率变化（k 和 y 同时开始爬升）。<b>与 ↑A 面板对比：那里 y 是跳升的</b>"),
                       ("c_t 面板", "<b>唯一「先向下跳」的面板</b>：t 处竖直下降，然后回升。图上 <span class='mj'>c^*_1</span> 略高于 <span class='mj'>c^*_0</span>——<b>但这取决于 s 是否小于黄金律，不是必然</b>"),
                       ("i_t 面板", "<b>t 处跳升</b>（s 变大，投资份额变大），然后随 y 上升"),
                       ("R_t 面板", "<b>t 处跳降</b>，然后继续下降，停在 <span class='mj'>R^*_1&lt;R^*_0</span>。<b>注意与 ↑A 的 r 面板相反：那里是跳升后回到原水平</b>")],
                read="<b>把这张图的六个面板与第 28 页一一对照，只看两处差异：c（这里跳降、那里跳升）与 r（这里跳降并长期更低、那里跳升并回到原水平）。</b>其余四个面板形状相同。",
                exam="必考对比题：「↑A 与 ↑s 的动态响应有何不同？」<b>标准答案四点</b>：① y 在 ↑A 时当期跳升、在 ↑s 时不跳；② c 在 ↑A 时跳升、在 ↑s 时跳降；③ r 在 ↑A 时先升后回原水平、在 ↑s 时先降并长期更低；④ k、i、w 的方向相同（都上升）。",
                )],
      tip="记忆锚点：<b>「A 变，当期产出就变；s 变，当期只有『分配』变。」</b>所以 ↑A 时 y 跳、c 跳、w 跳、r 跳（全部是价格与流量）；↑s 时只有 c 与 i 反向跳（分配变了），y、w 都不动，而 r 因为资本供给变化而跳。",
      warn="<b>c 的最终水平不确定</b>——这是本页最容易答错的地方。图上画的是 <span class='mj'>c^*_1&gt;c^*_0</span>，但那只是「这个 s 还没超过黄金律」的情形。<b>正确表述：短期内 c 一定下降；长期 c 可能上升也可能下降；若 s 已超过 <span class='mj'>s_{GR}</span>，则长期 c 一定下降。</b>")

add(32, kp="五句话解释 ↑s 的图形，重点是<b>c 的模糊性</b>与<b>r 的永久下降</b>。",
      plain="同样是把图翻译成文字。最需要理解的是消费那一条：储蓄率上升当期一定少消费，但长期呢？产出变多了，可你只拿其中更小的比例——两个力量方向相反，所以最终高低说不准。除非用黄金律来判断。",
      note="课件五句：<br><br>"
            "① <b>「s 在 t 期上升时，k<sub>t</sub> 当期不变（预定），之后逐期上升到永久更高的水平。」</b>——同 ↑A；<br>"
            "② <b>「y<sub>t</sub> 同理，因为 y=Af(k)。」</b>——<b>注意：这里 y 不跳</b>，与 ↑A 不同；<br>"
            "③ <b>「i<sub>t</sub> 立刻跳升，因为 i=sy；之后因 s 更高与 y 上升继续上升。」</b>——两个渠道同向；<br>"
            "④ <b>「c<sub>t</sub>=(1-s)y<sub>t</sub>，所以初期必然下降。之后 y 上升，c 最终高于还是低于起点是模糊的（ambiguous），尽管图上画的是更高的稳态 c*。」</b>——<b>本页的核心</b>；<br>"
            "⑤ <b>「r<sub>t</sub> 逐步降到永久更低的水平，因为 k 逐步上升，而 r=Af'(k) 且 f' 递减。」</b><br>"
            "→ 与 ↑A 的对比：那里 r <b>回到</b>原水平，这里 r <b>永久更低</b>。<b>原因：<span class='mj'>r^*=\\alpha\\delta/s</span>，s 在分母 ⇒ s↑ ⇒ r*↓</b>。",
      lr=[dict(name="c 为什么「模糊」",
               lhs="c^*=(1-s)\\,Af(k^*(s))",
               lhs_t="稳态消费 = 消费比例 × 稳态产出",
               rhs="\\text{两个方向相反的效应}",
               rhs_t="<span class='mj'>(1-s)</span> 下降 vs <span class='mj'>f(k^*(s))</span> 上升",
               why_t="为什么不能直接判断符号",
               why="对 s 求导：<span class='mj'>\\dfrac{dc^*}{ds}=-Af(k^*)+(1-s)Af'(k^*)\\dfrac{dk^*}{ds}</span>。<b>第一项为负</b>（比例变小）、<b>第二项为正</b>（产出变大），符号取决于两者大小。<br>"
                   "第 46 页的证明会把它化简成 <span class='mj'>\\dfrac{dc^*}{ds}=[Af'(k^*)-\\delta]\\dfrac{dk^*}{ds}</span>。<b>因为 <span class='mj'>dk^*/ds&gt;0</span>，所以符号完全由 <span class='mj'>Af'(k^*)</span> 与 <span class='mj'>\\delta</span> 的大小决定</b>——这正好就是黄金律条件（第 39 页）。<br>"
                   "<b>结论：<span class='mj'>Af'(k^*)&gt;\\delta</span>（资本还不够多）⇒ c 上升；<span class='mj'>Af'(k^*)&lt;\\delta</span>（资本已过多）⇒ c 下降。</b>")],
      tip="「模糊」不是「不知道」，而是<b>「要看不等于哪个参数」</b>。答题时这样写最稳：<b>「短期 c 必然下降；长期方向不确定，取决于 <span class='mj'>s</span> 与 <span class='mj'>s_{GR}</span> 的相对大小：若 <span class='mj'>s&lt;s_{GR}</span> 则长期 c 上升，若 <span class='mj'>s&gt;s_{GR}</span> 则下降。」</b>",
      warn="不要写「储蓄率上升一定提高消费，因为产出增加了」——<b>这是把两个效应中的一个当成全部</b>。也不要写「一定降低」——那是把短期结论当长期结论。<b>「先降后升、最终不定」才是完整答案。</b>")

add(33, kp="数值练习：<span class='mj'>A=1,s=0.2,\\alpha=1/3,\\delta=0.1</span> ⇒ <span class='mj'>k^*\\approx 2.83</span>；A 升到 1.1 后在 Excel 里走路径。",
      plain="课件给了一组具体数字，让你把整个模型算一遍，还要在 Excel 里画出每一期的路径。它的用意是：让你看到「收敛」不是一句空话，而是可以一期一期算出来的。",
      note="给定：<span class='mj'>A=1</span>、<span class='mj'>s=0.2</span>、<span class='mj'>\\alpha=1/3</span>、<span class='mj'>\\delta=0.1</span>；经济从 <span class='mj'>t-N</span> 到 <span class='mj'>t-1</span> 处于稳态（N=5）；t 期 A 升到 1.1。<br><br>"
            "<b>先算初始稳态</b>（用第 25 页公式）：<br>"
            "· <span class='mj'>k^*=\\left(\\dfrac{0.2\\times 1}{0.1}\\right)^{1/(1-1/3)}=2^{1.5}\\approx 2.828</span><br>"
            "· <span class='mj'>y^*=(k^*)^{1/3}\\approx 1.414</span><br>"
            "· <span class='mj'>c^*=0.8\\times 1.414\\approx 1.131</span>　<span class='mj'>i^*=0.2\\times 1.414\\approx 0.283</span><br>"
            "· <span class='mj'>r^*=\\alpha y^*/k^*=\\dfrac{1}{3}\\cdot\\dfrac{1.414}{2.828}\\approx 0.167</span>　（也可直接用 <span class='mj'>\\alpha\\delta/s=0.1/0.6\\approx 0.167</span> 验证）<br>"
            "· <span class='mj'>w^*=(1-\\alpha)y^*\\approx 0.943</span><br><br>"
            "<b>A 升到 1.1 后的新稳态</b>：<span class='mj'>k^*=(0.22/0.1)^{1.5}=2.2^{1.5}\\approx 3.263</span>，<span class='mj'>y^*\\approx 1.632</span>，<span class='mj'>c^*\\approx 1.305</span>，<span class='mj'>w^*\\approx 1.088</span>，<b><span class='mj'>r^*</span> 仍是 0.167</b>。",
      lr=[dict(name="路径怎么迭代（Excel 一列就够）",
               lhs="k_{t+1}",
               lhs_t="下一期人均资本（下一行的格子）",
               rhs="0.2\\times 1.1\\times k_t^{1/3}+0.9\\,k_t",
               rhs_t="当期数值公式：s·A·k<sup>α</sup> + (1−δ)k",
               why_t="为什么这样一列就能画出全部六个变量",
               why="因为<b>只要 k 的路径出来，其余五个都是它的静态函数</b>（第 20 页六条）：<br>"
                   "<span class='mj'>y=A k^{\\alpha}</span>、<span class='mj'>c=(1-s)y</span>、<span class='mj'>i=sy</span>、<span class='mj'>r=\\alpha Ak^{\\alpha-1}</span>、<span class='mj'>w=(1-\\alpha)Ak^{\\alpha}</span>。<br>"
                   "<b>操作</b>：第一格放 <span class='mj'>k_0=2.828</span>，第二格写上面这条公式并往下拖。前 5 行用 A=1（稳态），第 6 行起把 A 换成 1.1，就得到「t 期冲击」的路径。")],
      tip="<b>这组数字有三个「用来检验答案」的漂亮性质，考试很好用</b>：<br>"
          "① <span class='mj'>k^*=2^{1.5}=2.828</span> 是整数指数，好算；<br>"
          "② <span class='mj'>r^*=\\alpha\\delta/s=0.167</span> 与 A 无关 ⇒ <b>A 提高后 r* 不变</b>，可以直接验证第 28 页那句「r 回到原水平」；<br>"
          "③ <span class='mj'>y^*=(k^*)^{1/3}</span> 与 <span class='mj'>k^*</span> 的关系是「开三次方」，所以 <span class='mj'>k^*</span> 涨 15% 只让 <span class='mj'>y^*</span> 涨约 5%——<b>这就是「资本深化收益递减」的数值感受</b>。",
      warn="Excel 里不要用「求解稳态」的迭代法去找 <span class='mj'>k^*</span>——<b>直接套闭式解</b>。另外注意：<b>第 5 行到第 6 行之间 k 不能跳</b>（预定），<b>但 y 要跳</b>（因为 A 变了）。如果 Excel 里画出来 k 也跳了，一定是把 <span class='mj'>k_{t+1}</span> 的公式错写成了当期 A 乘当期 k 的另一种形式。")

add(34, kp="关键结论：<b>A 与 s 都不带来持续增长</b>——都只有「转型期加速」，长期增长率为零。",
      plain="做完两个实验，结论有点扫兴：不管你把技术一次性提高多少、把储蓄率提高多少，经济最终都会停在一个新的稳态上，然后增长归零。参数变化只能让经济「更快地跑到新水平」，不能让它「一直跑下去」。所以模型必须回答：那现实中的持续增长是哪来的？答案只能是生产率不断提高——但为什么它会不断提高，这个模型没说。",
      note="课件四句，逻辑链很紧：<br><br>"
            "① <b>「A 与 s 的变化都不会触发增长率的持续上升。」</b>——它们只改变<b>水平</b>，不改变<b>长期增长率</b>（长期都是 0）；<br>"
            "② <b>「每一个都只带来暂时的更快增长，同时经济向新稳态过渡。」</b>——这叫<b>转型动态</b>（transitional dynamics）；<br>"
            "③ <b>「长期中，这个模型里增长为零——经济收敛到稳态！」</b>——<b>这是模型的「尴尬」：它为了研究增长而建，结论却是没有增长</b>；<br>"
            "④ <b>「但模型意味着持续增长必须来自生产率提高」</b>，理由有两条：<br>"
            "　· <b>A 可以无限增长，而 s 有上界 1</b>；<br>"
            "　· <b>反复提高 s 会导致 r 持续下降，与事实不符</b>（<span class='mj'>r^*=\\alpha\\delta/s</span>，s 一路升 ⇒ r 一路降；而现实中 r 大致稳定）。",
      lr=[dict(name="为什么「s 有上界」就足以否定「靠储蓄增长」",
               lhs="\\text{sustained growth}",
               lhs_t="持续的（人均）增长：增长率长期为正",
               rhs="s\\le 1\\ \\Rightarrow\\ k^*<\\infty",
               rhs_t="储蓄率封顶 ⇒ 稳态资本有限 ⇒ 增长终将停止",
               why_t="两条论证，一条比一条硬",
               why="<b>论证一（上限）</b>：<span class='mj'>k^*=\\left(\\frac{sA}{\\delta}\\right)^{1/(1-\\alpha)}</span>，<span class='mj'>s</span> 最大只能到 1，所以 <span class='mj'>k^*</span> 有上限。到了上限就没有增长了。<b>而 A 没有上界</b>——它可以一直涨，所以只有它能支撑持续增长。<br>"
                   "<b>论证二（利率）</b>：就算你不断把 s 往上推（0.2→0.3→0.4…），<span class='mj'>r^*=\\alpha\\delta/s</span> 会一路下降。现实中资本的回报率长期大致稳定（Kaldor 事实之一），<b>这说明现实中的增长不是靠不断加储蓄实现的</b>。<br>"
                   "两条合起来：<b>「你不能靠储蓄变富」——不是道德劝告，而是模型的算术结论。</b>")],
      tip="这一页是全讲的<b>转折点</b>：前面三十页都在讲「资本积累能做到什么」，这一页说「它就到此为止了」。<b>后面七页（36–41）处理两个遗留问题</b>：稳态的另一种画法（更直观）、以及「储蓄率应该多少」（黄金律）。<b>Part II 才是真正的解法</b>：让 A（更准确说是 Z）自己增长。",
      warn="别说「Solow 模型认为资本积累不重要」。<b>它认为资本积累对「水平」很重要、对「长期增长率」不重要。</b>这个区分是本题的得分点：<b>水平效应（level effect）vs 增长效应（growth effect）</b>。Solow 只有前者，内生增长模型才有后者。")

add(35, kp="一句话总结：<b>持续增长只能来自生产率，不能来自资本积累——因为资本报酬递减。</b>",
      plain="课件的最后一句大白话：你没法靠存钱变富。原因很简单：机器越攒越多，每多一台带来的额外产出就越少，最后新攒的机器只够补上磨损的，增长就停了。要一直富下去，只能靠「同样的机器能生产更多」——也就是技术进步。",
      note="课件两句（<b>可以直接背下来当结论句</b>）：<br>"
            "① <b>「Sustained growth must come from productivity growth, not capital accumulation.」</b><br>"
            "② <b>「You cannot save your way to more growth, because of diminishing returns to capital.」</b><br><br>"
            "第②句里的 <b>because</b> 是全部要害：<b>递减报酬</b>。<b>如果资本报酬不递减（线性技术 <span class='mj'>y=Ak</span>），储蓄就能带来持续增长</b>——这正是内生增长模型（AK 模型）的做法，也是第 9 页 B 面板那个「直线」的意义。",
      tip="把这句话与 Topic 1 的增长核算接起来：<b>增长核算把增长拆成「资本深化 + 劳动 + 生产率」，Solow 模型解释了为什么中间两项都不能撑起长期增长</b>（劳动无趋势、资本报酬递减），于是<b>「索洛剩余」就成了唯一的嫌疑犯</b>——这就是为什么 TFP 在实证里那么重要。",
      warn="「不能靠储蓄变富」<b>不等于</b>「储蓄无用」。储蓄决定<b>稳态水平</b>（<span class='mj'>k^*</span>、<span class='mj'>y^*</span>），只是不能决定<b>长期增长率</b>。<b>对穷国来说，提高储蓄率能把人均收入水平抬高一大截——这是水平效应，不是增长效应，但对福利仍然重要。</b>")

add(36, kp="换一种写法：<b><span class='mj'>\\Delta k_{t+1}=sAf(k_t)-\\delta k_t</span></b>——净投资 = 储蓄 − 折旧。",
      plain="把方程两边都减去「今年的资本」，左边就变成「资本的变化量」。右边自动分成两块：一块是今年存下来的新机器，一块是今年磨损掉的机器。两者相减，就是净增加的机器。稳态就是「净增加等于零」——新造的正好的补上磨掉的。",
      note="推导：从 <span class='mj'>k_{t+1}=sAf(k_t)+(1-\\delta)k_t</span> 两边减 <span class='mj'>k_t</span>，令 <span class='mj'>\\Delta k_{t+1}=k_{t+1}-k_t</span>：<br>"
            "<span class='mj'>\\Delta k_{t+1}=sAf(k_t)-\\delta k_t</span><br><br>"
            "稳态条件变成 <span class='mj'>\\Delta k_{t+1}=0</span>，即 <b><span class='mj'>sAf(k^*)=\\delta k^*</span></b>——<b>「总投资 = 总折旧」</b>。<br><br>"
            "<b>为什么要换这种写法？</b>因为它把「投资」与「折旧」分离成了两个可以直接画在同一张图上的对象（第 37 页）：一个是凹曲线、一个是直线，<b>交点就是稳态</b>。这比第 22 页那张「45° 线」图更直观，也更容易看出 <span class='mj'>s</span>、<span class='mj'>A</span>、<span class='mj'>\\delta</span> 各自怎么影响稳态。",
      lr=[dict(name="净资本积累",
               lhs="\\Delta k_{t+1}=k_{t+1}-k_t",
               lhs_t="人均资本的<b>净增加</b>（这一期比上一期多了多少）",
               rhs="\\underbrace{sAf(k_t)}_{\\text{total investment}}-\\underbrace{\\delta k_t}_{\\text{total depreciation}}",
               rhs_t="人均储蓄（=人均投资，<b>补进来</b>）− 人均折旧（<b>漏出去</b>）",
               why_t="为什么这个形式更好用",
               why="因为它把稳态条件说成了一句<b>「流入 = 流出」</b>的话：<span class='mj'>sAf(k^*)=\\delta k^*</span>。<br>"
                   "这也直接给出<b>三条比较静态</b>，不用画 45° 线就能判断：<br>"
                   "· <span class='mj'>s\\uparrow</span> 或 <span class='mj'>A\\uparrow</span> ⇒ 流入曲线抬高 ⇒ <span class='mj'>k^*\\uparrow</span>；<br>"
                   "· <span class='mj'>\\delta\\uparrow</span> ⇒ 流出直线变陡 ⇒ <span class='mj'>k^*\\downarrow</span>。<br>"
                   "<b>而且它告诉你怎么算「收敛速度」</b>：<span class='mj'>\\Delta k</span> 有多快归零，取决于两条线在 <span class='mj'>k^*</span> 附近的斜率差。"),
           dict(name="稳态条件（两种等价写法）",
               lhs="sAf(k^*)=\\delta k^*",
               lhs_t="总投资恰好补上总折旧",
               rhs="k_{t+1}=k_t",
               rhs_t="资本不再变化",
               rel="⇔",
               why_t="两种写法完全等价，但用途不同",
               why="<b>左边这种</b>（投资 = 折旧）适合<b>画图</b>与<b>判断比较静态</b>（第 37 页）；<br>"
                   "<b>右边这种</b>（k 不变）适合<b>代数求解</b>（第 25 页：<span class='mj'>\\delta k^*=sA(k^*)^{\\alpha}</span>）。<br>"
                   "<b>考试时两种都要会写</b>：题目说「求稳态」，用右边；题目说「画图说明稳态」，用左边。")],
      dec=[
          ("<span class='mj'>sAf(k_t)</span>", "<b>总投资</b>（total investment）。注意它是<b>产出的一部分</b>，所以随 k 凹增。"),
          ("<span class='mj'>\\delta k_t</span>", "<b>总折旧</b>（total depreciation）。它正比于存量，所以是<b>过原点的直线</b>。"),
          ("<span class='mj'>\\Delta k_{t+1}</span>", "下标写 <span class='mj'>t+1</span> 是课件的习惯（表示「到下一期为止的变化」）。<b>有些教材写 <span class='mj'>\\Delta k_t</span>，含义相同，别被符号绕晕。</b>"),
      ],
      tip="这条式子是<b>所有增长模型的通用起点</b>。到了 Topic 3（跨国收入差异）会加上人力资本；内生增长模型会把 <span class='mj'>f(k)</span> 换成线性（<span class='mj'>\\Delta k=sAk-\\delta k</span>，只要 <span class='mj'>sA&gt;\\delta</span> 就永不收敛）。<b>会写这一条，后面几讲的增长部分就都有抓手。</b>",
      warn="<b>「总投资 = 总折旧」说的是稳态，不是每期。</b>转型期里两者不等：<span class='mj'>sAf(k)&gt;\\delta k</span> 时 k 上升（在 <span class='mj'>k^*</span> 左边），反之下降。<b>把稳态条件当成恒等式是常见错误。</b>")

add(37, kp="三线图：<b>产出 <span class='mj'>Af(k)</span>、储蓄 <span class='mj'>sAf(k)</span>、折旧 <span class='mj'>\\delta k</span></b>，后两者交点即 k*。",
      plain="这张图把三样东西画在一起：上面那条是「能生产多少」，中间那条是「存下来多少」（就是上面那条按 s 缩小），那条直线是「磨损掉多少」。磨损线和储蓄线的交点就是稳态。而上面那条与储蓄线之间的竖直距离，就是「吃掉多少」——消费。",
      note="三条线（<b>纵轴是「产出/投资的量」，不是 <span class='mj'>k_{t+1}</span></b>）：<br>"
            "① <span class='mj'>Af(k_t)</span>：<b>产出</b>。凹、过原点、起点陡；<br>"
            "② <span class='mj'>sAf(k_t)</span>：<b>储蓄 = 投资</b>。<b>就是产出曲线按 s 缩小</b>（形状完全一样）；<br>"
            "③ <span class='mj'>\\delta k_t</span>：<b>折旧</b>。<b>过原点的直线</b>，斜率 δ。<br><br>"
            "②③ 的交点给出 <span class='mj'>k^*</span>（因为交点处 <span class='mj'>sAf(k)=\\delta k</span>）。<br>"
            "在 <span class='mj'>k^*</span> 处向左作水平线，可以把左轴分成两段：<b>0 到 <span class='mj'>sAf(k^*)</span> 是投资</b>，<b><span class='mj'>sAf(k^*)</span> 到 <span class='mj'>Af(k^*)</span> 是消费</b>。课件用蓝色箭头标出了这两段。",
      fig=[dict(name="三线图：产出、投资、折旧（稳态的第二种画法）",
                axes=[("横轴", "k_t", "人均资本。<b>注意：这里的横轴是 k，纵轴是「量」，不是上一张图的 <span class='mj'>k_{t+1}</span></b>"),
                      ("纵轴", "产出量（output）", "产出（及投资、折旧）的量。<b>三条线共用同一把尺子</b>，所以可以直接比较高低与差距"),
                      ("稳态位置", "k^*", "由 <span class='mj'>sAf(k)</span> 与 <span class='mj'>\\delta k</span> 的交点确定，虚线投到横轴")],
                marks=[("Af(k_t)（最上面的曲线）", "<b>产出曲线</b>。凹、递增、过原点"),
                       ("sAf(k_t)（中间曲线）", "<b>投资曲线</b>。<b>产出曲线按 s 缩小</b>，所以形状与上面那条完全一样，只是更低"),
                       ("\\delta k_t（最陡的直线）", "<b>折旧直线</b>。过原点、斜率 δ。<b>它在 k 小时低于投资曲线、k 大时高于投资曲线</b>——这个「交叉」就是稳态"),
                       ("左侧蓝色箭头：investment", "从 0 到 <span class='mj'>sAf(k^*)</span> 的竖直距离 ⇒ <b>投资</b>"),
                       ("左侧蓝色箭头：consumption", "从 <span class='mj'>sAf(k^*)</span> 到 <span class='mj'>Af(k^*)</span> 的竖直距离 ⇒ <b>消费</b>。<b>这一段就是黄金律要最大化的对象</b>（第 40 页）")],
                read="<b>三步读图</b>：① 找 <span class='mj'>sAf(k)</span> 与 <span class='mj'>\\delta k</span> 的交点（稳态）；② 该点往上的竖直距离到 <span class='mj'>Af(k)</span> 就是消费；③ 交点左边投资 &gt; 折旧（k 上升），右边反之。<b>把「两条曲线之间的竖直距离 = 消费」这一句记住，第 40 页的黄金律就是「让这个距离最大」。</b>",
                exam="三种考法：① 用这张图解释稳态（<b>比 45° 线图更直观，答题时可以二选一，但要说明纵轴不同</b>）；② 在图上标出消费与投资（<b>常考</b>）；③ 说明 ↑s 时哪条线动、消费怎么变（<b>sAf 整条上移，<span class='mj'>Af</span> 不动 ⇒ 在旧 <span class='mj'>k^*</span> 处消费立刻变小</b>）。")],
      tip="<b>这张图与第 22 页那张的区别，是本讲最容易被问倒的地方</b>：<br>"
          "· <b>第 22 页</b>：横轴 <span class='mj'>k_t</span>、纵轴 <span class='mj'>k_{t+1}</span>——是「映射图」，用来谈<b>动态与收敛</b>；<br>"
          "· <b>第 37 页</b>：横轴 <span class='mj'>k_t</span>、纵轴 <b>产出量</b>——是「流量图」，用来谈<b>稳态位置与消费分解</b>。<br>"
          "<b>两张图都能求 <span class='mj'>k^*</span>，但只有第 22 页能画收敛路径。</b>",
      warn="<b>投资曲线是 <span class='mj'>sAf(k)</span>，不是 <span class='mj'>sAf(k)+(1-\\delta)k</span>。</b>后者是第 22 页那张图里的「<span class='mj'>k_{t+1}</span>」，两者差一个 <span class='mj'>(1-\\delta)k</span>。<b>把这两条搞混，稳态会算错、图也画错。</b>")

add(38, kp="储蓄率该是多少？<b>效用来自消费，而 s 对 c* 有两个方向相反的效应</b>。",
      plain="前面一直把储蓄率当成给定的。但它其实可以选择——那么选多少好？判断标准不是「产出最大」（产出当然越多越好，但产出多不等于过得好），而是「消费最大」。问题是：多存钱能让饼变大，但你自己吃的比例变小了。两个力量打架，所以一定存在一个「刚刚好」的储蓄率。",
      note="课件三句：<br>"
            "① <b>「Household utility comes from consumption, not output.」</b>——<b>福利看消费，不看产出</b>。这一句把评价标准从 <span class='mj'>y^*</span> 换成了 <span class='mj'>c^*</span>；<br>"
            "② <b>效应一（规模效应）</b>：<span class='mj'>s\\uparrow</span> ⇒ 资本更多 ⇒ 产出更多 ⇒ <b>饼更大</b> ⇒ 消费更多；<br>"
            "③ <b>效应二（份额效应）</b>：<span class='mj'>s\\uparrow</span> ⇒ <b>自己能吃的比例 <span class='mj'>1-s</span> 变小</b> ⇒ 消费更少。<br><br>"
            "两个效应方向相反 ⇒ <span class='mj'>c^*(s)</span> 是一条<b>倒 U 形</b>曲线 ⇒ 存在一个使 <span class='mj'>c^*</span> 最大的 s。这就是下一页的黄金律。<br><br>"
            "<b>注意这里的方法论转变</b>：前面都是「给定 s，问经济会怎样」（实证）；现在是「给定目标，问 s 该是多少」（规范）。<b>Solow 模型本身不能回答这个问题，必须外接一个福利标准。</b>",
      tip="为什么不用「产出最大」当标准？因为<b>产出最大要求 s=1</b>——全部产出都拿去投资，消费为零。这样的经济产出增长率最高（转型期），但人全饿死了。<b>「效用来自消费」这一句就是排除这种荒谬答案的依据。</b>",
      warn="<b>不要写「储蓄率越高越好，因为资本越多产出越多」。</b>这句话在 Solow 里是错的：产出确实随 s 上升，但消费不一定。<b>只有 s &lt; s<sub>GR</sub> 时提高 s 才同时提高长期消费。</b>")

add(39, kp="黄金律：<b>使稳态消费最大的 s</b>，其特征条件是 <span class='mj'>Af'(k^*_{GR})=\\delta</span>。",
      plain="黄金律就是那个「刚刚好」的储蓄率。条件很漂亮：在最优的那一点上，「多一台机器能多产出的东西」正好等于「多一台机器的磨损」。如果多产出的比磨损多，说明还该多存；如果少，说明存过头了。",
      note="定义：<span class='mj'>s_{GR}</span> 是使 <span class='mj'>c^*</span> 最大的储蓄率，<span class='mj'>k^*_{GR}</span> 是对应的稳态资本。<br><br>"
            "<b>条件</b>：<span class='mj'>Af'(k^*_{GR})=\\delta</span>。<br><br>"
            "<b>直觉（务必理解，考试常问「为什么是 δ 而不是 0」）</b>：多积累一单位资本，能多产出 <span class='mj'>Af'(k)</span>；但要维持这一单位资本，得补上折旧 <span class='mj'>\\delta</span>。<br>"
            "· 若 <span class='mj'>Af'(k)&gt;\\delta</span>：多产出的比磨损多 ⇒ <b>还有净收益</b> ⇒ 应该多存；<br>"
            "· 若 <span class='mj'>Af'(k)&lt;\\delta</span>：多产出的还不够补磨损 ⇒ <b>净亏损</b> ⇒ 应该少存；<br>"
            "· 相等 ⇒ <b>恰好</b>，此时消费最大。<br><br>"
            "证明在第 46 页：把 <span class='mj'>c^*(s)</span> 对 s 求导并令其为零。",
      lr=[dict(name="黄金律条件",
               lhs="Af'(k^*_{GR})",
               lhs_t="多一单位资本的<b>毛产出</b>（资本的边际产品）",
               rhs="\\delta",
               rhs_t="多一单位资本的<b>维持成本</b>（折旧率）",
               why_t="为什么「边际产出 = 折旧」就最优",
               why="因为稳态下<b>每多维持一单位资本，就要每期付出 δ 的折旧</b>。所以「多一单位资本的净回报」是 <span class='mj'>Af'(k)-\\delta</span>。<br>"
                   "如果这个净回报为正，把一单位产出从消费转成投资，未来能带来更多消费——<b>今天少吃的可以用明天多吃的补回来还有余</b>；如果为负，反过来做更好。<b>所以最优处净回报必须为零。</b><br>"
                   "<b>注意这不是「利率 = 折旧率」的巧合，而是「资本的净收益率 = 0」</b>——在黄金律上，资本的净回报被完全用于补偿时间偏好之外的折旧，没有剩余。")],
      dec=[
          ("<span class='mj'>s_{GR}</span>", "黄金律储蓄率。<b>它是「应该选哪个 s」的答案</b>，不是模型推出来的结果（模型只能告诉你「给定 s 会怎样」）。"),
          ("<span class='mj'>k^*_{GR}</span>", "黄金律资本。<b>注意它一般不等于实际稳态 <span class='mj'>k^*</span></b>——除非恰好选了 <span class='mj'>s=s_{GR}</span>。"),
          ("<span class='mj'>Af'(k)</span>", "资本的边际产品。<b>它随 k 递减</b> ⇒ <span class='mj'>Af'(k)=\\delta</span> 这个方程有唯一解 ⇒ <b>黄金律资本唯一</b>。"),
      ],
      tip="<b>三个「k*」要分清</b>（考试最爱的陷阱）：<br>"
          "① <span class='mj'>k^*</span>：给定 s 的实际稳态——<b>模型的结果</b>；<br>"
          "② <span class='mj'>k^*_{GR}</span>：使 c* 最大的资本——<b>规范标准</b>；<br>"
          "③ 动态有效区间：<span class='mj'>k^*&lt;k^*_{GR}</span>。<br>"
          "<b>判断「储蓄过多还是过少」的唯一办法是比较①②，不能凭感觉。</b>",
      warn="条件是 <span class='mj'>Af'(k)=\\delta</span>，<b>不是</b> <span class='mj'>f'(k)=0</span>（那是「产出最大」的条件，对应 s=1），也<b>不是</b> <span class='mj'>Af'(k)=0</span>。<b>把 δ 漏掉是最常见的错误。</b>漏掉 δ 的经济含义是「资本不需要维护」，那当然越多越好——明显不对。")

add(40, kp="黄金律的图形：<b>产出曲线的切线与折旧线平行</b>处就是 <span class='mj'>k^*_{GR}</span>。",
      plain="在图上找那个「刚刚好」的点：产出曲线的斜率（多一台机器能多产多少）等于折旧线的斜率（多一台机器要磨损多少）。这两条线平行的地方，就是黄金律。此时产出与投资之间的竖直距离（消费）达到最大。",
      note="图的构造：绿线 <span class='mj'>y_t=Af(k_t)</span>、黑线 <span class='mj'>\\delta k_t</span>、黑线 <span class='mj'>i_t=sAf(k_t)</span>。<br><br>"
            "<b>关键在于那条切于绿线的虚线</b>：它画在 <span class='mj'>k^*</span> 处，<b>与 <span class='mj'>\\delta k_t</span> 平行</b>——也就是说该点的斜率 <span class='mj'>Af'(k)</span> 恰好等于 δ。<b>这就是黄金律条件的几何表达。</b><br><br>"
            "此时 <span class='mj'>c^*</span> 是绿线与投资曲线之间的竖直距离（图上用一个竖直的小括号 + <span class='mj'>c^*</span> 标出），<b>这个距离在这一点的所有可能 s 中最大</b>。<br><br>"
            "注意图上 <span class='mj'>i_t=sAf(k_t)</span> 与 <span class='mj'>\\delta k_t</span> 的交点也正好在 <span class='mj'>k^*</span>——<b>这不是巧合</b>：黄金律的 s 就是这样定义的，使得它的稳态恰好落在 <span class='mj'>Af'(k)=\\delta</span> 那一点。",
      fig=[dict(name="黄金律的图形直觉（切线平行于折旧线）",
                axes=[("横轴", "k_t", "人均资本。标出 <span class='mj'>k^*</span>（此处即 <span class='mj'>k^*_{GR}</span>）"),
                      ("纵轴", "y_t,\\ i_t,\\ \\delta k_t", "三个量共用一把尺子：产出、投资、折旧"),
                      ("绿色线", "y_t=Af(k_t)", "<b>产出曲线</b>。它是「饼」的大小")],
                marks=[("绿色切线（虚线）", "<b>本图的灵魂</b>：在 <span class='mj'>k^*</span> 处与绿线相切，<b>且与 <span class='mj'>\\delta k_t</span> 平行</b> ⇒ 该点 <span class='mj'>Af'(k)=\\delta</span>。虚线画到了曲线右上方，用来显示「如果继续加资本，斜率会更小」"),
                       ("黑线 \\delta k_t", "<b>折旧线</b>，斜率 δ。它是切线平行的<b>参照对象</b>"),
                       ("黑线 i_t=sAf(k_t)", "<b>投资曲线</b>（储蓄曲线）。它与折旧线交于 <span class='mj'>k^*</span>，给出稳态"),
                       ("竖直小括号 c*", "<b>产出与投资之间的差距 = 消费</b>。在 <span class='mj'>k^*</span> 处这个差距<b>最大</b>——这就是黄金律的定义"),
                       ("y* 与 i* 的水平虚线", "把产出与投资两个水平投影到纵轴，方便读出 <span class='mj'>c^*=y^*-i^*</span>")],
                read="<b>先找切线、再找交点。</b>切线平行于折旧线 ⇒ 边际产出等于折旧 ⇒ 消费最大。<b>如果实际储蓄率偏低，投资曲线就会在 <span class='mj'>k^*</span> 下方，竖直差距变小 ⇒ 可以增储蓄来提高消费；偏高则相反。</b>",
                exam="考法：① 在图上标出黄金律点并说明条件；② <b>问「为什么消费最大对应两条线平行」</b>（答：斜率相等 ⇒ 净回报为零 ⇒ 再多/再少资本都会降低消费）；③ 给出具体的 Cobb-Douglas 参数，让算 <span class='mj'>s_{GR}</span>：<span class='mj'>Af'(k)=\\alpha A k^{\\alpha-1}=\\delta</span> ⇒ <span class='mj'>k_{GR}=(\\alpha A/\\delta)^{1/(1-\\alpha)}</span>，再由 <span class='mj'>s_{GR}=\\delta k_{GR}/(Ak_{GR}^{\\alpha})</span> 得 <b><span class='mj'>s_{GR}=\\alpha</span></b>——<b>这是一个极漂亮的结论：Cobb-Douglas 下黄金律储蓄率就等于资本份额！</b>")],
      tip="<b>Cobb-Douglas 下 <span class='mj'>s_{GR}=\\alpha</span></b>，这个结论值得单独记：α≈1/3 意味着黄金律储蓄率约 33%。<b>而现实中各国的储蓄率常在 20% 上下——说明多数国家在黄金律左边（资本不足），而不是右边。</b>第 41 页正是讲这件事。",
      warn="图上那个 <span class='mj'>k^*</span> <b>同时</b>是「黄金律资本」与「某个 s 下的稳态」，这是因为画图时<b>已经假定选了 <span class='mj'>s=s_{GR}</span></b>。<b>如果 <span class='mj'>s\neq s_{GR}</span>，那么 <span class='mj'>k^*</span>（投资与折旧的交点）与 <span class='mj'>k^*_{GR}</span>（切线平行点）就不在同一个位置</b>——这是读图时最容易搞错的地方。")

add(41, kp="动态无效：<b>在黄金律右边一定不是最优</b>（减少储蓄能同时增加今天与未来的消费）。",
      plain="如果储蓄率太高、资本太多（超过黄金律），那么减少储蓄是「双赢」——今天能多消费（少存），未来也能多消费（因为过度积累的资本回报还不够补磨损）。这种状态叫动态无效。反过来，如果储蓄率偏低，减少储蓄只是「今天多一点、明天少一点」，划不划算取决于你多看重今天。",
      note="课件四层（<b>逻辑非常严密，值得逐层记</b>）：<br><br>"
            "① <b>「低于黄金律 ≠ 储蓄不足。」</b>——因为存在<b>跨期权衡</b>：<span class='mj'>s\\uparrow</span> 今天少消费、未来多消费。<b>是否值得，取决于「未来相对于今天被如何估值」</b>（即贴现率/偏好）。<b>Solow 模型里没有偏好参数，所以它无法判断「低于黄金律」是好是坏。</b><br><br>"
            "② <b>「但高于黄金律一定不是最优。」</b>——因为减少 s 能<b>同时</b>提高今天与未来的消费：今天少吃的那部分不用存了 ⇒ 今天 c↑；资本减少到黄金律水平 ⇒ 未来 c↑。<b>两个方向都改善，所以一定不是最优。</b><br><br>"
            "③ <b>「这就是动态无效（dynamic inefficiency）。」</b>——名字的含义：这个配置<b>在动态意义上浪费了资源</b>，即使每一期都在技术上「有效」（在生产可能性边界上），仍然是浪费的，因为可以永远地提高每一期的消费。<br><br>"
            "④ <b>「几乎没有证据表明任何现代经济是动态无效的。」</b>——现实中资本积累通常<b>不足</b>而非过度。",
      lr=[dict(name="「双赢」的机制（为什么高于黄金律一定不好）",
               lhs="\\text{reduce } s\\ \\text{when } k^*&gt;k^*_{GR}",
               lhs_t="把储蓄率降下来",
               rhs="c\\uparrow\\ \\text{today and } c\\uparrow\\ \\text{in the future}",
               rhs_t="今天与未来的消费<b>同时</b>提高",
               why_t="为什么这是「一定」而不是「可能」",
               why="分两段看：<br>"
                   "<b>今天</b>：<span class='mj'>c=(1-s)y</span>，s 下降 ⇒ <b>今天消费直接上升</b>（产出没变）。<br>"
                   "<b>未来</b>：资本太多 ⇒ <span class='mj'>Af'(k)&lt;\\delta</span> ⇒ 每多一单位资本的净回报为负 ⇒ <b>把资本减少到 <span class='mj'>k_{GR}</span> 会让稳态消费上升</b>（因为 c* 在 <span class='mj'>k&gt;k_{GR}</span> 区间是递减的）。<br>"
                   "<b>两段同号 ⇒ 一定变好 ⇒ 现状一定不是最优。</b><br>"
                   "对比「低于黄金律」：今天 c↓、未来 c↑，<b>符号相反 ⇒ 需要偏好才能判断</b>。这就是两者不对称的根本原因。")],
      tip="<b>「动态无效」这个词的用法</b>：它专门指「资本过度积累到可以永久性提高消费」的状态。<b>判断标准：<span class='mj'>Af'(k^*)&lt;\\delta</span>（等价地 <span class='mj'>s&gt;s_{GR}</span>，Cobb-Douglas 下即 <span class='mj'>s&gt;\\alpha</span>）。</b>",
      warn="<b>不要把「低于黄金律」说成「储蓄不足」。</b>这是本页最核心的一句。正确说法：低于黄金律<b>只是说「再存多一点能让未来消费更高」</b>，但代价是今天消费更低——是否划算取决于时间偏好，<b>模型本身不能判断</b>。<b>只有高于黄金律的情形才有明确结论。</b>")

add(42, kp="收尾：<b>为了研究增长而建的模型，稳态里没有增长</b>——但它的「失败」恰好指出了方向（生产率）。",
      plain="课件的最后一页自问自答：我们明明是来研究增长的，为什么写了这样一个「长期不增长」的模型？答案是：正因为它在资本积累这条路上走到了尽头，我们才知道增长必须来自别处。下一讲就把技术进步正式装进来。",
      note="课件四句：<br>"
            "① <b>「We set out to study economic growth, but why write down a model whose steady state has no growth?」</b>——这是<b>自我质疑</b>，也是最好的复习问题；<br>"
            "② <b>「The basic Solow model yields important insights about sources of sustained economic growth.」</b>——它的价值不在「解释增长」，而在<b>「排除错误答案」</b>；<br>"
            "③ <b>「Sustained growth must ultimately stem from productivity improvements (technology), not just capital deepening.」</b>——<b>资本深化（capital deepening）</b>只能到稳态，<b>技术进步</b>才能持续；<br>"
            "④ <b>「Next lecture: extend the basic model to allow for sustained growth.」</b>——这就是 Part II。",
      tip="把这一页当成<b>「本讲的答辩稿」</b>：如果题目问「Solow 模型既然预测零增长，为什么还重要？」，标准答案是<b>「它用严格的框架证明了资本积累不能带来持续增长，从而把解释力集中到生产率上——这正是增长核算与 TFP 研究的起点」</b>。",
      warn="不要答「Solow 模型过时了」。<b>它的三个结论至今仍是基准</b>：① 条件收敛；② 资本积累的水平效应；③ 生产率是长期增长唯一来源。<b>后续模型（含内生增长）都是在它的框架上加东西，而不是推翻它。</b>")

add(43, kp="附录三页：<b>零利润的证明、<span class='mj'>r</span> 与 <span class='mj'>w</span> 的推导、黄金律的证明</b>。",
      plain="接下来三页是附录，也就是正文里三个「Proof」的详细过程。它们不影响主线，但如果考试要你「证明」而不是「说明」，就得靠这三页。",
      note="三页对应正文的三个「Proof」：<br>"
            "① <b>第 10 页的「Proof」</b> → 附录第 44 页：用<b>欧拉定理</b>证明零利润；<br>"
            "② <b>第 20 页的「Deriving r<sub>t</sub> and w<sub>t</sub>」</b> → 附录第 45 页：证明 <span class='mj'>F_K=f'(k)</span> 与 <span class='mj'>F_L=f(k)-kf'(k)</span>；<br>"
            "③ <b>第 39 页的「Proof」</b> → 附录第 46 页：对 <span class='mj'>c^*(s)</span> 求导，导出 <span class='mj'>Af'(k_{GR})=\\delta</span>。<br><br>"
            "<b>三页都用同一个工具：一次齐次函数的性质（欧拉定理）。</b>所以复习时只要把欧拉定理记牢，三页是一件事。",
      tip="<b>考试策略</b>：如果题目只要求「说明/解释」，正文的直觉就够了；如果写「证明/derive」，就必须写出这三页的式子。<b>判断依据是动词，不是分值。</b>",
      warn="附录页在 PDF 里的页码是 42–44（正文编号），但<b>幻灯片总数是 46</b>（含封面与附录封面）。<b>引用页码时要说清是「课件编号」还是「PDF 页序」</b>，两者差 2–3 页——这一点在与同学对答案时特别容易混。")

add(44, kp="零利润的证明：<b>欧拉定理</b>——一次齐次函数满足 <span class='mj'>F=F_KK+F_LL</span>。",
      plain="这一页给出上一页那条「产出被分光」的严格证明。工具叫欧拉定理，说的是：如果一个函数是规模报酬不变的，那么它的值正好等于「每个投入乘以它自己的边际产出」之和。把边际产出换成价格，就得到零利润。",
      note="课件三步：<br>"
            "① <b>齐次函数的定义</b>：若 <span class='mj'>F(\\gamma K,\\gamma L)=\\gamma^{\\rho}F(K,L)</span>，则称 F 是 <b>ρ 次齐次</b>。CRTS 就是 <span class='mj'>\\rho=1</span>；<br>"
            "② <b>欧拉定理</b>：对 ρ 次齐次函数，<span class='mj'>\\rho F(K,L)=F_K(\\cdot)K+F_L(\\cdot)L</span>；<br>"
            "③ <b>取 ρ=1</b>：<span class='mj'>F=F_KK+F_LL</span>，两边乘 A 并把 FOC（<span class='mj'>w=AF_L</span>、<span class='mj'>r=AF_K</span>）代进去，得 <span class='mj'>AF=wL+rK</span>——<b>产出恰好等于要素报酬</b>。",
      lr=[dict(name="欧拉定理（ρ = 1 的情形）",
               lhs="F(K,L)",
               lhs_t="总产出",
               rhs="F_K(K,L)\\,K+F_L(K,L)\\,L",
               rhs_t="资本的边际产品 × 资本 + 劳动的边际产品 × 劳动",
               why_t="为什么这条式子成立（证明思路）",
               why="<b>证明的关键技巧：对 <span class='mj'>\\gamma</span> 求导。</b><br>"
                   "把 <span class='mj'>F(\\gamma K,\\gamma L)=\\gamma F(K,L)</span> 两边对 γ 求导（左边用链式法则）：<br>"
                   "<span class='mj'>F_K(\\gamma K,\\gamma L)K+F_L(\\gamma K,\\gamma L)L=F(K,L)</span><br>"
                   "然后令 <span class='mj'>\\gamma=1</span>，就得到定理。<b>这个「对 γ 求导再令 γ=1」是欧拉定理的标准证法，考试如果要你证，就写这两步。</b><br>"
                   "<b>经济含义</b>：CRTS 下「按边际产品分配」恰好把产出分完，既不多也不少。")],
      tip="欧拉定理的<b>第二个用途</b>（下一页要用）：它还能推出「偏导是 <span class='mj'>\\rho-1</span> 次齐次」——即 <span class='mj'>F_K(\\gamma K,\\gamma L)=\\gamma^{\\rho-1}F_K(K,L)</span>。<b>取 ρ=1 就得到「偏导零次齐次」，这是把 <span class='mj'>F_K</span> 写成 <span class='mj'>f'(k)</span> 的依据。</b>",
      warn="欧拉定理<b>只对「齐次函数」成立</b>。规模报酬递减（ρ&lt;1）时得到的是 <span class='mj'>\\rho F=F_KK+F_LL</span>，右边<b>小于</b> F，差额是利润。<b>所以「零利润」是 CRTS 的结论，不是普适定理。</b>")

add(45, kp="推导稳态的 r 与 w：<b><span class='mj'>F_K=f'(k)</span>、<span class='mj'>F_L=f(k)-kf'(k)</span></b>。",
      plain="这一页解释为什么「总量层面的边际产出」可以写成「人均函数」的导数与剩余。用到的还是欧拉定理的推论：规模报酬不变时，边际产出只取决于人均资本，与规模无关。",
      note="课件三步：<br>"
            "① <b>偏导的齐次性</b>：若 F 是 ρ 次齐次，则 <span class='mj'>F_K</span> 是 <span class='mj'>\\rho-1</span> 次齐次，即 <span class='mj'>F_K(\\gamma K,\\gamma L)=\\gamma^{\\rho-1}F_K(K,L)</span>；<br>"
            "② <b>取 ρ=1、<span class='mj'>\\gamma=1/L</span></b>：<span class='mj'>F_K(K,L)=F_K(K/L,L/L)=F_K(k,1)=f'(k)</span>——<b>边际产出只依赖 k</b>；<br>"
            "③ <b>再对 <span class='mj'>F=F_KK+F_LL</span> 两边除以 L</b>：<span class='mj'>F(K,L)/L=F_K\\cdot(K/L)+F_L</span>，即 <span class='mj'>f(k)=f'(k)k+F_L</span>，解出 <b><span class='mj'>F_L=f(k)-f'(k)k</span></b>。",
      lr=[dict(name="劳动的边际产品（剩余形式）",
               lhs="F_L(K,L)",
               lhs_t="劳动的边际产品（总量层面）",
               rhs="f(k)-f'(k)\\,k",
               rhs_t="人均产出 − 人均资本 × 资本边际产品",
               why_t="为什么劳动的边际产品可以这样「减出来」",
               why="从欧拉定理 <span class='mj'>F=F_KK+F_LL</span> 出发，两边除以 L：<br>"
                   "<span class='mj'>\\dfrac{F}{L}=F_K\\dfrac{K}{L}+F_L</span> ⇒ <span class='mj'>f(k)=f'(k)k+F_L</span>（用了 ② 的 <span class='mj'>F_K=f'(k)</span>）。<br>"
                   "移项即得 <span class='mj'>F_L=f(k)-f'(k)k</span>。<b>这条推导的漂亮之处在于：它不需要知道 F 的具体形式，只要 CRTS 就够了。</b><br>"
                   "<b>经济含义</b>：产出里「资本按边际产品拿走 <span class='mj'>kf'(k)</span>」之后，<b>剩下的全归劳动</b>——这就是「工资是残差」的严格来源。")],
      tip="这两个式子是<b>后面所有「w 与 r 怎么变」的判断依据</b>：<span class='mj'>r</span> 只看 <span class='mj'>f'</span>（随 k 递减 ⇒ r 随 k 下降），<span class='mj'>w</span> 看 <span class='mj'>f-kf'</span>（随 k 递增 ⇒ w 随 k 上升）。<b>第 28、29、31、32 页的结论全部从这里出来。</b>",
      warn="<span class='mj'>F_K=f'(k)</span> 里的 <b>k 是 <span class='mj'>K/L</span></b>，不是 K。<b>常见错误是写成 <span class='mj'>F_K=f'(K)</span></b>——那等于假设 L=1，只在人均化之后才成立。<b>写答案时要保持下标一致。</b>")

add(46, kp="黄金律的证明：<b><span class='mj'>\\partial c^*/\\partial s=[Af'(k^*)-\\delta]\\,\\partial k^*/\\partial s=0</span></b>。",
      plain="这一页把「消费最大」这个条件算出来。技巧是先把稳态消费写成「产出减折旧」，这样就不必分别处理「储蓄率变化」和「资本变化」两个渠道——折旧项会把它们自动合并。",
      note="课件四步：<br>"
            "① 从 <span class='mj'>c^*(s)=(1-s)Af(k^*(s))</span> 出发；<br>"
            "② 拆开：<span class='mj'>=Af(k^*)-sAf(k^*)</span>；<br>"
            "③ <b>用稳态条件 <span class='mj'>sAf(k^*)=\\delta k^*</span> 替换第二项</b>：<span class='mj'>=Af(k^*(s))-\\delta k^*(s)</span>；<br>"
            "④ 对 s 求导（注意 k* 依赖 s）：<span class='mj'>\\dfrac{\\partial c^*}{\\partial s}=[Af'(k^*)-\\delta]\\dfrac{\\partial k^*}{\\partial s}</span>。<br><br>"
            "<b>令其为零</b>：因为 <span class='mj'>\\partial k^*/\\partial s&gt;0</span>（s 提高 ⇒ 稳态资本提高），所以只能是 <b><span class='mj'>Af'(k^*)-\\delta=0</span></b>，即 <span class='mj'>Af'(k^*_{GR})=\\delta</span>。",
      lr=[dict(name="第 ③ 步的替换（本证明的关键技巧）",
               lhs="c^*=(1-s)Af(k^*)",
               lhs_t="稳态消费 = 消费比例 × 稳态产出",
               rhs="Af(k^*)-\\delta k^*",
               rhs_t="稳态产出 − 稳态折旧",
               why_t="为什么可以这样换（这一步最容易看不懂）",
               why="因为稳态下 <b><span class='mj'>sAf(k^*)=\\delta k^*</span></b>（投资 = 折旧，第 36 页）。所以 <span class='mj'>c^*=Af(k^*)-\\underbrace{sAf(k^*)}_{=\\delta k^*}=Af(k^*)-\\delta k^*</span>。<br>"
                   "<b>这个替换的好处极大</b>：原来 <span class='mj'>c^*</span> 里有两个地方依赖 s（<span class='mj'>1-s</span> 与 <span class='mj'>k^*(s)</span>），换过之后只剩<b>一个地方</b>（<span class='mj'>k^*(s)</span>）——求导时不会漏项。<br>"
                   "<b>经济含义</b>：稳态消费 = 「总产出 − 维持资本存量所需的折旧」。<b>要最大化它，就要让「多一单位资本的产出」等于「多一单位资本的折旧」</b>——这正是黄金律。")],
      tip="<b>这个证明还有一个副产品</b>：<span class='mj'>\\partial c^*/\\partial s</span> 的符号完全由 <span class='mj'>Af'(k^*)-\\delta</span> 决定（因为 <span class='mj'>\\partial k^*/\\partial s&gt;0</span>）。<b>于是「s 提高是否提高长期消费」等价于「当前资本是否低于黄金律」</b>——这正好补上了第 32 页那个「c 的模糊性」的答案。",
      warn="求导时<b>不能把 <span class='mj'>k^*</span> 当常数</b>。如果写成 <span class='mj'>\\partial c^*/\\partial s=-Af(k^*)</span>，就漏掉了「s 通过 k* 影响产出」这个渠道，会得到「c* 一定随 s 下降」的错误结论。<b>链式法则那一项 <span class='mj'>\\partial k^*/\\partial s</span> 必须写出来。</b>")

add(47, kp="Part II：<b>让技术自己增长</b>——人均量才能长期增长。",
      plain="第一部分证明了一件事：光靠攒机器，经济最终会停下来。那现实中人均收入为什么能一直涨？第二部分给模型打一个补丁：让技术以固定速度不断进步。这样稳态就不再是「人均资本不变」，而是「人均资本按固定速度增长」。",
      note="Part II 只有 9 页（正文 8 页），结构极简：<br>"
            "① <b>改生产函数</b>（第 49 页）：加入劳动增强型技术 <span class='mj'>Z_t</span>，并让 Z 与 L 都按固定速度增长；<br>"
            "② <b>改人均化</b>（第 50 页）：从「除以 L」改成「除以 <span class='mj'>Z_tL_t</span>」（效率单位），于是稳态又能画成两条线的交点；<br>"
            "③ <b>看结论</b>（第 51–55 页）：效率单位下一切照旧，但<b>换算回人均量之后，所有变量都以 z 的速度增长</b>——这就得到了持续增长。<br><br>"
            "<b>一句话总结 Part II：把「人口增长」和「技术进步」当成两个「稀释因子」放进分母，模型的形式完全不变。</b>",
      tip="Part II 的数学难度<b>比 Part I 低</b>，因为所有推导都只是「在分母上多乘一个 <span class='mj'>(1+z)(1+n)</span>」。<b>但它解决的问题是本讲的核心</b>：为什么模型能同时有「稳态」和「持续增长」？答案是<b>稳态是对「效率单位」而言的，人均量在稳态里仍然增长</b>。",
      warn="别把 Part II 当成「另一个模型」。<b>它就是 Part I 加了两条增长假设</b>（<span class='mj'>n&gt;0</span>、<span class='mj'>z&gt;0</span>），方程结构、图形逻辑、比较静态方法全部照用。<b>复习时应该把两部分对照着看，而不是分别记两套。</b>")

add(48, kp="Part II 的动机：<b>基本模型收敛到零增长，但数据显示人均收入持续增长</b>。",
      plain="开场就把矛盾摆出来：第一部分的结论是「长期增长为零」，但现实中人均收入一百多年来一直在涨。所以必须引入一个能持续进步的东西——技术。这一讲的做法是让技术「增强劳动」：技术进步等于让每个工人变得更有效率。",
      note="课件三句：<br>"
            "① <b>「Key insight from the Solow model: productivity is key to generating long-run growth.」</b>——回扣 Part I 的结论；<br>"
            "② <b>「But basic model converges to a steady state with no growth.」</b>——<b>矛盾所在</b>；<br>"
            "③ <b>「In this lecture, we extend by introducing labor-augmenting technology, which enables sustained per capita growth.」</b>——<b>解法</b>。<br><br>"
            "<b>为什么必须是「劳动增强型」（labor-augmenting）而不是「资本增强型」？</b>因为只有这种形式才能让模型存在<b>平衡增长路径</b>（balanced growth path）：所有变量按同一速度增长、比率保持不变。<b>这是 Uzawa 定理的结论，考试只要记住「只有劳动增强型技术才与平衡增长相容」即可。</b>",
      tip="三种技术形式要能区分：<br>"
          "· <b>Hicks 中性</b>：<span class='mj'>Y=AF(K,L)</span>——Part I 用的，技术提高时两种要素的边际产品同比例上升；<br>"
          "· <b>劳动增强型（Harrod 中性）</b>：<span class='mj'>Y=F(K,ZL)</span>——Part II 用的，<b>只有它产生平衡增长</b>；<br>"
          "· <b>资本增强型（Solow 中性）</b>：<span class='mj'>Y=F(ZK,L)</span>——<b>不能</b>产生平衡增长（除非生产函数是 Cobb-Douglas）。",
      warn="别把 <span class='mj'>Z</span> 与 <span class='mj'>A</span> 混为一谈。课件的分工很明确：<b>A 管「水平的乘数」（当期生产率高低），Z 管「增长的斜率」（每期提高多少）</b>。<b>写答案时要保持这个分工，否则第 51 页 w 里那个 <span class='mj'>Z_t</span> 就解释不清。</b>")

add(49, kp="改造生产函数：<b><span class='mj'>Y_t=AF(K_t,Z_tL_t)</span></b>，且 <span class='mj'>Z_t=(1+z)^t</span>、<span class='mj'>L_t=(1+n)^t</span>。",
      plain="新的生产函数把技术放进「劳动」里面：不是让机器和人都变得更厉害，而是让「一个工人」等于「一点几个工人」。Z 就是那个放大倍数，叫效率单位。同时让 Z 和人口 L 都按固定百分比每年增长。如果两个增长率都是零，就退回第一部分的模型。",
      note="课件四句：<br>"
            "① <b><span class='mj'>Y_t=AF(K_t,Z_tL_t)</span></b>：<span class='mj'>Z_t</span> 是<b>劳动增强型生产率</b>，<span class='mj'>Z_tL_t</span> 是<b>效率单位劳动</b>（efficiency units of labor）；<br>"
            "② <b><span class='mj'>Z_t=(1+z)^t</span></b>、<b><span class='mj'>L_t=(1+n)^t</span></b>，初值在 t=0 归一为 1；<br>"
            "③ <b>「When z=n=0: back to basic Solow model.」</b>——<b>这两条假设是「增量」，不是「替代」</b>；<br>"
            "④ <b>「Z<sub>t</sub> not fundamentally different from A, but convenient to use Z<sub>t</sub> to capture growth, while A captures the level of productivity.」</b><br>"
            "→ <b>这句话是理解 A 与 Z 分工的关键</b>：A 是「截距」（水平），Z 是「斜率」（增长）。",
      lr=[dict(name="劳动增强型生产函数",
               lhs="Y_t",
               lhs_t="总产出",
               rhs="AF(K_t,\\ Z_tL_t)",
               rhs_t="技术水平 A × 用「效率单位劳动」计量的生产函数",
               why_t="为什么技术要「贴在 L 上」而不是「乘在外面」",
               why="因为只有这种形式才能让经济存在<b>平衡增长路径</b>：<span class='mj'>K/Y</span> 不变、<span class='mj'>r</span> 不变、<span class='mj'>w</span> 与 <span class='mj'>y</span> 同速增长。<b>如果技术乘在外面（Hicks 中性），那么随着 A 上升，资本的边际产品也会同比例上升，资本就会不断积累得比产出更快——比率就无法稳定。</b><br>"
                   "<b>一个直观的读法</b>：<span class='mj'>Z_tL_t</span> 是「有效劳动」的总量。技术进步相当于「工人数不变，但每个工人相当于 1.05 个人」——所以产出能一直涨，而<b>每个人的工作时间没变</b>。这与第 2 页那个「人均工时无趋势」的事实完全吻合。")],
      dec=[
          ("<span class='mj'>Z_t</span>", "劳动增强型技术。<b>以 (1+z) 的速度指数增长</b>。<b>它是本讲唯一能带来持续增长的项。</b>"),
          ("<span class='mj'>Z_tL_t</span>", "效率单位劳动（efficiency units of labor）。<b>Z 上升等于「劳动变多」</b>——所以技术进步在这个模型里等价于「人口增长」，只是不体现在人数上。"),
          ("<span class='mj'>n</span>", "人口增长率。<b>它的作用与 z 类似</b>：都会稀释人均资本（第 50 页的分母）。"),
          ("<span class='mj'>z</span>", "技术进步率。<b>稳态时所有人均变量的增长率都等于它</b>（第 53 页）。"),
      ],
      tip="一个数字直觉：<b>z=2%、n=1%</b> 时，总量增长率约 <span class='mj'>(1+z)(1+n)-1\\approx 3\\%</span>，人均增长率 = 2%。<b>这就是为什么「长期人均增长 2%」这个数字在宏观里到处出现——它就是被校准出来的 z。</b>",
      warn="<b><span class='mj'>Z_t</span> 是「劳动增强」不是「劳动增加」</b>：它不改变就业人数（<span class='mj'>L_t</span> 仍按 n 增长），只改变「每个工人相当于多少效率单位」。<b>如果写成 <span class='mj'>Y=AF(ZK,ZL)</span>，那就变成「规模报酬递增」了，模型完全不同。</b>")

add(50, kp="效率单位化：<b><span class='mj'>\\hat k_t=K_t/(Z_tL_t)</span></b>，运动方程多了一个分母 <span class='mj'>(1+z)(1+n)</span>。",
      plain="现在人均量不再是稳定的了（因为它一直在涨），所以要再除一次：不只是「每人多少机器」，而是「每单位有效劳动多少机器」。这个量在稳态下才是不变的。代价是方程右边要除以一个「增长率因子」——人口和技术都在稀释人均资本。",
      note="两类变量（<b>记号一定要分清</b>）：<br>"
            "· <span class='mj'>x_t=X_t/L_t</span>：<b>人均</b>（per worker）；<br>"
            "· <span class='mj'>\\hat x_t=X_t/(Z_tL_t)</span>：<b>每效率单位</b>（per efficiency unit）。<b>帽子 = 效率单位。</b><br><br>"
            "<b>改造后的中心方程</b>：<br>"
            "<span class='mj'>\\hat k_{t+1}=\\dfrac{1}{(1+z)(1+n)}\\left[sAf(\\hat k_t)+(1-\\delta)\\hat k_t\\right]</span><br><br>"
            "<b>推导</b>：从 <span class='mj'>K_{t+1}=sAF(K_t,Z_tL_t)+(1-\\delta)K_t</span> 两边除以 <span class='mj'>Z_{t+1}L_{t+1}</span>，注意 <span class='mj'>Z_{t+1}L_{t+1}=(1+z)(1+n)Z_tL_t</span>，就得到上面的式子。<br><br>"
            "课件评价：<b>「Practically the same as before, though in per efficiency units.」</b>——<b>形式上几乎一样，只是多了一个压缩因子。</b>",
      lr=[dict(name="效率单位下的资本积累",
               lhs="\\hat k_{t+1}",
               lhs_t="下一期的<b>每效率单位</b>资本",
               rhs="\\dfrac{1}{(1+z)(1+n)}\\left[sAf(\\hat k_t)+(1-\\delta)\\hat k_t\\right]",
               rhs_t="本期的（储蓄 + 未折旧资本），<b>再按「效率单位增长」摊薄</b>",
               why_t="为什么要除以 (1+z)(1+n)",
               why="因为分母在变大。<b>下一期的分母是 <span class='mj'>Z_{t+1}L_{t+1}=(1+z)(1+n)Z_tL_t</span></b>，而分子（资本）只增加了 <span class='mj'>sAf+(1-\\delta)\\hat k</span> 那么多。<b>如果分子涨得比分母慢，人均（效率单位）资本就会下降。</b><br>"
                   "<b>经济含义</b>：人口增长与技术进步都会<b>稀释</b>资本——同样的资本要分给更多人、更多「有效劳动」。所以 <span class='mj'>n</span> 或 <span class='mj'>z</span> 越大，稳态的 <span class='mj'>\\hat k^*</span> 越小。<b>这一点在 Topic 3 讨论跨国差异时很重要：高人口增长率的国家人均资本更低。</b>")],
      dec=[
          ("<span class='mj'>\\hat k_t</span>", "每效率单位资本。<b>Part II 里唯一的状态变量</b>（代替 Part I 的 <span class='mj'>k_t</span>）。"),
          ("<span class='mj'>(1+z)(1+n)</span>", "<b>效率单位劳动的增长率</b>。它是「稀释因子」，出现在分母上。<b>z=n=0 时它等于 1，整套式子退回 Part I。</b>"),
          ("<span class='mj'>f(\\hat k)</span>", "注意这里的 f 作用在 <b>效率单位</b>资本上，不是人均资本——<b>这是最容易写错下标的地方</b>。"),
      ],
      tip="<b>做 Part II 的题，只要记住一个动作：把 Part I 所有式子里的 <span class='mj'>k</span> 换成 <span class='mj'>\\hat k</span>，再在「跨期」的式子（只有运动方程）分母上乘 <span class='mj'>(1+z)(1+n)</span>。</b>其余五条静态式子形式完全不变。",
      warn="<b>不要把 <span class='mj'>1/((1+z)(1+n))</span> 放到稳态条件的外面去。</b>稳态条件是 <span class='mj'>\\hat k_{t+1}=\\hat k_t</span>，直接得到 <span class='mj'>sAf(\\hat k^*)+ (1-\\delta)\\hat k^*=(1+z)(1+n)\\hat k^*</span>，即 <b><span class='mj'>sAf(\\hat k^*)=[\\delta+z+n+zn]\\hat k^*</span></b>。<b>这个「有效折旧率」<span class='mj'>\\delta+z+n</span> 是 Part II 的必考式。</b>")

add(51, kp="效率单位的六个均衡条件：<b>形式与 Part I 完全相同</b>，只有 <span class='mj'>\\hat w</span> 里多一个 <span class='mj'>Z_t</span>。",
      plain="把六个方程全部戴上帽子。前五个和第一部分长得一模一样，只有工资那条多了一个 Z：因为技术变好，同样的劳动按效率单位算更值钱，所以名义工资会随 Z 一起涨。",
      note="课件六条：<br>"
            "① <span class='mj'>\\hat k_{t+1}=\\dfrac{1}{(1+z)(1+n)}[sAf(\\hat k_t)+(1-\\delta)\\hat k_t]</span>　资本积累<br>"
            "② <span class='mj'>\\hat y_t=Af(\\hat k_t)</span>　生产<br>"
            "③ <span class='mj'>\\hat c_t=(1-s)\\hat y_t</span>　消费<br>"
            "④ <span class='mj'>\\hat i_t=s\\hat y_t</span>　投资<br>"
            "⑤ <span class='mj'>r_t=Af'(\\hat k_t)</span>　资本租金<br>"
            "⑥ <span class='mj'>w_t=Z_t\\left[Af(\\hat k_t)-Af'(\\hat k_t)\\hat k_t\\right]</span>　工资<br><br>"
            "<b>稳态定义</b>：<span class='mj'>\\hat k_t=\\hat k_{t+1}=\\hat k^*</span> 对所有 t 成立。",
      lr=[dict(name="工资为什么会随 Z 增长（唯一形式有变化的式子）",
               lhs="w_t",
               lhs_t="实际工资（每<b>实际工人</b>的报酬）",
               rhs="Z_t\\left[Af(\\hat k_t)-Af'(\\hat k_t)\\hat k_t\\right]",
               rhs_t="效率单位劳动的价格 × <b>每个工人相当于多少效率单位</b>",
               why_t="为什么这里要乘 Z<sub>t</sub>，而 r 不用",
               why="因为<b>工资是按「人」付的，而产出是按「效率单位」算的</b>。一个效率单位的劳动值 <span class='mj'>Af-Af'\\hat k</span>（括号里那一项），而一个实际工人相当于 <span class='mj'>Z_t</span> 个效率单位，所以工资要乘上去。<br>"
                   "<b>对比 r</b>：资本没有「效率单位」的概念（K 就是 K），所以 <span class='mj'>r</span> 里不需要 Z。<b>这就是「技术进步的好处全部落到劳动身上」的模型表达</b>——因为技术进步是劳动增强型的。<br>"
                   "<b>推论（第 54、55 页要用）</b>：稳态时 <span class='mj'>\\hat k</span> 不变 ⇒ 括号里是常数 ⇒ <b><span class='mj'>w</span> 以 z 的速度增长</b>，而 <b><span class='mj'>r</span> 完全不增长</b>。")],
      dec=[
          ("<span class='mj'>\\hat y_t,\\ \\hat c_t,\\ \\hat i_t</span>", "每效率单位的产出、消费、投资。<b>稳态时它们都是常数</b>——但换算回人均量之后就会增长（第 53 页）。"),
          ("<span class='mj'>r_t=Af'(\\hat k_t)</span>", "<b>没有 Z</b>。<b>这是「r 在增长路径上不变」的直接原因</b>——因为 <span class='mj'>\\hat k</span> 在稳态不变。"),
          ("<span class='mj'>w_t=Z_t[\\cdots]</span>", "<b>有 Z</b>。<b>这是「w 与人均产出同速增长」的直接原因。</b>"),
      ],
      tip="这六条要能<b>与 Part I 的第 20 页一一对应着默写</b>：把 <span class='mj'>k</span> 换成 <span class='mj'>\\hat k</span>、在第①条分母加 <span class='mj'>(1+z)(1+n)</span>、在第⑥条前面乘 <span class='mj'>Z_t</span>。<b>三处改动，其余照抄。</b>",
      warn="<b><span class='mj'>\\hat k</span> 稳定 ≠ <span class='mj'>k</span> 稳定。</b>稳态时 <span class='mj'>\\hat k^*</span> 是常数，但 <span class='mj'>k_t=K_t/L_t=\\hat k_t\\cdot Z_t</span> <b>以 z 的速度增长</b>。<b>把「稳态」理解成「人均量不变」是 Part II 最常见的错误。</b>")

add(52, kp="效率单位的稳态 <span class='mj'>\\hat k^*</span>：<b>还是两条线交点，只是曲线被压低了</b>。",
      plain="图画法和第一部分一模一样：45 度线加一条曲线。不同的是这条曲线被「增长率因子」压了一下，所以它跟 45 度线的交点更靠左——效率单位的稳态资本比第一部分的人均稳态资本小。",
      note="图的结构（<b>与第 22 页同构</b>）：<br>"
            "· 横轴 <span class='mj'>\\hat k_t</span>，纵轴 <span class='mj'>\\hat k_{t+1}</span>；<br>"
            "· 45° 线 <span class='mj'>\\hat k_{t+1}=\\hat k_t</span>；<br>"
            "· 曲线 <span class='mj'>\\hat k_{t+1}=\\dfrac{1}{(1+z)(1+n)}[sAf(\\hat k_t)+(1-\\delta)\\hat k_t]</span>。<br><br>"
            "<b>与第 22 页的唯一区别</b>：整条曲线被乘以 <span class='mj'>1/((1+z)(1+n))&lt;1</span>，所以<b>它更低、更平</b>，与 45° 线的交点更靠左。<br><br>"
            "<b>经济含义</b>：人口增长与技术进步都会稀释资本，所以「每效率单位」的稳态资本比「每人」的稳态资本小。<b>但注意：这不代表生活水平更低</b>——因为每个工人相当于 <span class='mj'>Z</span> 个效率单位，人均产出是 <span class='mj'>\\hat y\\cdot Z</span>，反而更高（第 53 页）。",
      fig=[dict(name="效率单位稳态 k̂*（与第 22 页同构、曲线更低）",
                axes=[("横轴", "\\hat k_t", "本期每效率单位资本"),
                      ("纵轴", "\\hat k_{t+1}", "下一期每效率单位资本"),
                      ("45° 线", "\\hat k_{t+1}=\\hat k_t", "同 Part I：不动 > 增、不动 = 平、不动 &lt; 减")],
                marks=[("曲线（较低的那条）", "<span class='mj'>\\dfrac{1}{(1+z)(1+n)}[sAf(\\hat k_t)+(1-\\delta)\\hat k_t]</span>。<b>它比 Part I 的曲线低，因为前面乘了一个小于 1 的因子</b>"),
                       ("交点 \\hat k^*", "稳态。<b>比 Part I 的 <span class='mj'>k^*</span> 更靠左</b>——增长率越高，稳态效率单位资本越低"),
                       ("与第 22 页的对比", "<b>形状完全一样、只是整体被压下来</b>。所以 Inada 条件仍然保证存在唯一交点，收敛逻辑也完全照搬")],
                read="<b>把它当成第 22 页的「复制品」来读</b>：交点 = 稳态、曲线上方 = 增长、下方 = 减少。<b>唯一要额外注意的是「这里的 k 是效率单位，不是人均」。</b>",
                exam="常考：① 画出两张图（Part I 与 Part II）并说明差别（<b>曲线被压低</b>）；② 问「z 或 n 上升后 <span class='mj'>\\hat k^*</span> 怎么变」——<b>都下降</b>；③ 由稳态条件导出 <b><span class='mj'>sAf(\\hat k^*)=(\\delta+z+n+zn)\\hat k^*</span></b>，并说明 <span class='mj'>\\delta+z+n</span> 可视为「有效折旧率」。")],
      tip="稳态条件可以整理成一个很好记的形式：<b><span class='mj'>\\hat k^*=\\left(\\dfrac{sA}{\\delta+z+n+zn}\\right)^{\\frac{1}{1-\\alpha}}</span></b>（Cobb-Douglas）。<b>与 Part I 的 <span class='mj'>k^*=(sA/\\delta)^{1/(1-\\alpha)}</span> 相比，只是把 δ 换成了 <span class='mj'>\\delta+z+n+zn</span>。</b>所以「人口增长快、技术进步快的国家，稳态人均资本低」——<b>这一条在 Topic 3 解释跨国差异时是核心机制之一。</b>",
      warn="<b>不要在图上把两条曲线画成「一样高只是更平」。</b>真实情形是<b>整条曲线被乘性压低</b>（每一点都按同一比例下降），所以它在所有 k 处都低于 Part I 的曲线，且在 k→∞ 时也<b>不会</b>趋近 45° 线。<b>如果画成「在高 k 处与 45° 线相交」，就错了。</b>")

add(53, kp="稳态时<b>所有人均变量都以 z 的速度增长</b>：<span class='mj'>k_{t+1}/k_t=1+z</span>。",
      plain="这是 Part II 的核心结论。效率单位的资本不变，但每个工人对应的效率单位在变多（每年多 z），所以人均资本每年也涨 z。产出、消费、投资都一样。于是模型终于有了「持续增长」，而且这个增长率是外生给定的 z。",
      note="课件推导（<b>三步，考试常考</b>）：<br>"
            "① 稳态 ⇒ <span class='mj'>\\dfrac{K_{t+1}}{Z_{t+1}L_{t+1}}=\\dfrac{K_t}{Z_tL_t}</span>；<br>"
            "② 两边乘 <span class='mj'>Z_{t+1}L_{t+1}</span>、再除以 <span class='mj'>L_{t+1}</span>，整理得 <span class='mj'>\\dfrac{K_{t+1}}{L_{t+1}}=\\dfrac{Z_{t+1}}{Z_t}\\cdot\\dfrac{K_t}{L_t}</span>；<br>"
            "③ 即 <span class='mj'>k_{t+1}=(1+z)k_t</span>，所以 <b><span class='mj'>\\dfrac{k_{t+1}}{k_t}=1+z</span></b>。<br><br>"
            "课件补充：<b>「Similar expressions hold true for per-worker output, consumption, and investment.」</b>——<span class='mj'>y,c,i</span> 同样以 <span class='mj'>1+z</span> 增长。<br>"
            "<b>「Per-worker variables all grow at the same rate as Z<sub>t</sub>.」</b>——<b>这就是平衡增长路径（balanced growth path）。</b>",
      lr=[dict(name="人均资本的增长率",
               lhs="\\dfrac{k_{t+1}}{k_t}",
               lhs_t="人均资本的增长率（<b>不是</b>效率单位）",
               rhs="1+z",
               rhs_t="技术进步率 + 1",
               why_t="为什么人均量恰好以 z 增长（而不是 z+n）",
               why="因为 <span class='mj'>k_t=\\dfrac{K_t}{L_t}=\\hat k_t\\cdot Z_t</span>。<b>稳态时 <span class='mj'>\\hat k_t</span> 是常数</b>，所以 <span class='mj'>k_t</span> 的增长率完全等于 <span class='mj'>Z_t</span> 的增长率，即 <span class='mj'>z</span>。<br>"
                   "<b>为什么不是 z+n</b>：人口增长 n 只影响<b>总量</b>的增长率。总量 <span class='mj'>K_t=\\hat k^*Z_tL_t</span> 以 <span class='mj'>(1+z)(1+n)</span> 增长，而人均 <span class='mj'>K_t/L_t</span> 只以 <span class='mj'>1+z</span> 增长。<b>这个区分是本题的得分点：总量增长 = z+n，人均增长 = z。</b>")],
      tip="<b>一张表记住三个增长率</b>（稳态时）：<br>"
          "· <b>效率单位量</b>（<span class='mj'>\\hat k,\\hat y,\\hat c,\\hat i</span>）：<b>0</b>（不变）；<br>"
          "· <b>人均量</b>（<span class='mj'>k,y,c,i,w</span>）：<b>z</b>；<br>"
          "· <b>总量</b>（<span class='mj'>K,Y,C,I</span>）：<b>z+n</b>（更准确是 <span class='mj'>(1+z)(1+n)-1</span>）。<br>"
          "<b>r</b>：<b>0</b>（不变）。<b>这四行是第 54–55 页「六个典型事实」的骨架。</b>",
      warn="<b>「人均增长 = z」不是「人均增长 = z+n」。</b>常见错误是把总量增长率当人均。<b>检验办法：如果 n=1%、z=2%，那么总量涨约 3%、人均涨 2%。</b>如果答成 3%，就说明把人口增长也算进了人均。")

add(54, kp="要素价格的稳态行为：<b>r* 不变、w* 以 z 增长</b>。",
      plain="这一页回答「技术进步的果实被谁拿走了」。结论很清楚：租金（资本的回报）完全不变，工资跟产出一样一直涨。原因是技术进步是「增强劳动」的——它让劳动更值钱，而资本的相对稀缺性没有改变。",
      note="课件两句：<br>"
            "① <b><span class='mj'>r^*=Af'(\\hat k^*)</span></b>，因为 <span class='mj'>\\hat k^*</span> 是常数 ⇒ <b>r* 不随时间变化</b>；<br>"
            "② <b><span class='mj'>w^*=Z_t\\left[Af(\\hat k^*)-Af'(\\hat k^*)\\hat k^*\\right]</span></b>，方括号里是常数 ⇒ <b>w* 以 Z<sub>t</sub> 的速度（即 z）增长</b>。<br><br>"
            "<b>两者对比的意义</b>：<b>资本回报率长期不变、实际工资长期增长</b>——这正是 Kaldor 提出的「典型事实」中的两条。<b>模型能同时解释这两条，是它成功的关键。</b>",
      lr=[dict(name="为什么 r 不变、w 涨",
               lhs="r^*=Af'(\\hat k^*)",
               lhs_t="稳态资本租金：<b>只依赖效率单位资本</b>",
               rhs="w^*=Z_t\\cdot[\\text{constant}]",
               rhs_t="稳态工资：<b>常数 × 增长的技术</b>",
               why_t="同一个技术进步，为什么一个涨一个不涨",
               why="关键在于<b>技术进步是「增强劳动」的</b>：它让每个工人相当于更多效率单位，所以<b>劳动的报酬（按人计）上升</b>；而资本没有「效率单位」的概念，<b>资本的相对稀缺性（<span class='mj'>\\hat k^*</span>）在稳态不变</b>，所以租金不变。<br>"
                   "<b>换个说法</b>：技术进步让「有效劳动」越来越多，资本要追着它跑；稳态时资本追上了（<span class='mj'>\\hat k^*</span> 恒定），所以资本的边际产品不再上升——<b>但劳动的边际产品（按人算）仍然随 Z 上升</b>。<br>"
                   "<b>如果技术进步是资本增强型的，结论会反过来</b>——这也是为什么模型必须选劳动增强型（第 48 页）。")],
      tip="<b>这条结论的现实对应</b>：过去一百多年，实际工资随生产率一起涨，而资本的回报率（利率）没有趋势性上升或下降。<b>Solow 模型用一句话解释了这两件事：技术进步增强劳动，不增强资本。</b>",
      warn="<b>「r 不变」是稳态（平衡增长路径）的性质，不是每时每刻。</b>转型期里 <span class='mj'>\\hat k</span> 在变，r 也在变。<b>考试如果问「技术进步会不会提高利率」，正确回答是「短期会（<span class='mj'>r=Af'(\\hat k)</span> 里 A 上升），长期不会（<span class='mj'>\\hat k</span> 上升抵消）」</b>——这与第 28–29 页的结论完全一致。")

add(55, kp="六条典型事实：<b>y、k、w 以 1+z 增长；K/Y、wL/Y 不变；r 不变</b>。",
      plain="最后一页把模型在稳态下的性质列成六条，然后说：这六条正好就是现实中观察到的六个长期规律。也就是说，加了一个技术进步项之后，模型终于能「对上数据」了。",
      note="课件六条（<b>这是全讲的落点，也是 Topic 1 那六个事实的模型版本</b>）：<br>"
            "① <span class='mj'>\\dfrac{y_{t+1}}{y_t}=1+z</span>　人均产出同速增长<br>"
            "② <span class='mj'>\\dfrac{k_{t+1}}{k_t}=1+z</span>　人均资本同速增长<br>"
            "③ <span class='mj'>\\dfrac{K_{t+1}}{Y_{t+1}}=\\dfrac{K_t}{Y_t}</span>　<b>资本-产出比不变</b>（因为分子分母都按 <span class='mj'>(1+z)(1+n)</span> 增长）<br>"
            "④ <span class='mj'>\\dfrac{w_{t+1}L_{t+1}}{Y_{t+1}}=\\dfrac{w_tL_t}{Y_t}</span>　<b>劳动收入份额不变</b>（因为 w 与 y 同速、L 与 Y 同速）<br>"
            "⑤ <span class='mj'>r_{t+1}=r_t</span>　<b>资本回报率不变</b><br>"
            "⑥ <span class='mj'>\\dfrac{w_{t+1}}{w_t}=1+z</span>　实际工资同速增长<br><br>"
            "课件结语：<b>「These are the six time-series stylized facts!」</b>——<b>模型第一次与数据对上。</b>",
      lr=[dict(name="为什么 K/Y 不变（最有名的一条）",
               lhs="\\dfrac{K_{t+1}}{Y_{t+1}}",
               lhs_t="下一期的资本-产出比",
               rhs="\\dfrac{K_t}{Y_t}",
               rhs_t="本期的资本-产出比",
               why_t="为什么它能不变",
               why="因为 <span class='mj'>K</span> 与 <span class='mj'>Y</span> 在稳态下<b>以同一个速度增长</b>：<br>"
                   "<span class='mj'>K_t=\\hat k^*Z_tL_t</span>、<span class='mj'>Y_t=Af(\\hat k^*)Z_tL_t</span>，两式相除，<b><span class='mj'>Z_tL_t</span> 全部约掉</b>，剩下 <span class='mj'>K_t/Y_t=\\hat k^*/(Af(\\hat k^*))</span>——<b>一个常数</b>。<br>"
                   "<b>这一条为什么重要</b>：它是「平衡增长」的定义性特征，也是<b>现实中观察到的 K/Y 大致稳定（约 3 倍）</b>这个事实的模型解释。<b>同时它也是判定一个模型能否解释长期增长的「试金石」</b>——任何让 K/Y 有趋势的模型都通不过。")],
      tip="<b>把这六条与 Topic 1 的「六个增长事实」对照记</b>：Topic 1 说的是「数据显示什么」，这里说的是「模型预测什么」。<b>两者对上了，这就是 Solow 模型最大的成功。</b>考试如果问「Solow 模型为什么重要」，答「因为它能同时解释这六条」比答「因为它讲资本积累」高一个层次。",
      warn="这六条<b>只在稳态（平衡增长路径）成立</b>。转型期里 <span class='mj'>y</span> 的增长率高于 z（追赶效应）、<span class='mj'>K/Y</span> 在变、<span class='mj'>r</span> 在变。<b>「收敛」与「平衡增长」是两件事：前者是转型期，后者是稳态。</b>")

# ============================ 公式速查 ============================
FORMULA_ROWS = [
    ("总量生产函数",
     "<span class='mj'>Y_t=A_tF(K_t,L_t)</span>",
     "技术乘在外面（Hicks 中性）；Cobb-Douglas：<span class='mj'>F=K^{\\alpha}L^{1-\\alpha}</span>"),
    ("规模报酬不变（CRTS）",
     "<span class='mj'>F(\\gamma K,\\gamma L)=\\gamma F(K,L)</span>",
     "<b>人均化的许可证</b>；也是零利润（欧拉定理）的前提"),
    ("Inada 条件",
     "<span class='mj'>F_K(0)=\\infty,\\ \\lim_{K\\to\\infty}F_K=0</span>",
     "保证稳态<b>存在且唯一</b>（曲线从 45° 上方进、落到下方出 + 凹）"),
    ("要素需求（FOC）",
     "<span class='mj'>w_t=A_tF_L,\\quad r_t=A_tF_K</span>",
     "边际成本 = 边际收益；<b>价格归一 ⇒ 不用乘 P</b>"),
    ("零利润（欧拉定理）",
     "<span class='mj'>A_tF=w_tL_t+r_tK_t</span>",
     "CRTS ⇒ 产出被要素报酬分光 ⇒ <b>家庭收入 = Y</b>"),
    ("商品市场 / 资源约束",
     "<span class='mj'>Y_t=C_t+I_t,\\quad I_t=sY_t,\\quad C_t=(1-s)Y_t</span>",
     "单一商品 ⇒ 自动成立；Part I <b>没有 G</b>"),
    ("资本积累（总量）",
     "<span class='mj'>K_{t+1}=(1-\\delta)K_t+I_t</span>",
     "<b>唯一的动态方程</b>；k<sub>t</sub> 因此是「预定」的"),
    ("基本运动方程",
     "<span class='mj'>K_{t+1}=(1-\\delta)K_t+sA_tF(K_t,\\bar L_t)</span>",
     "六条方程压成一条一阶非线性差分方程"),
    ("人均生产函数",
     "<span class='mj'>y_t=Af(k_t),\\quad f(k)\\equiv F(k,1)</span>",
     "靠 CRTS：<span class='mj'>F(K,L)/L=F(K/L,1)</span>"),
    ("人均资本积累 ★",
     "<span class='mj'>k_{t+1}=sAf(k_t)+(1-\\delta)k_t</span>",
     "<b>全讲核心</b>；后面每一张图都在画它的两边"),
    ("净积累形式",
     "<span class='mj'>\\Delta k_{t+1}=sAf(k_t)-\\delta k_t</span>",
     "稳态 ⇔ <span class='mj'>sAf(k^*)=\\delta k^*</span>（投资 = 折旧）"),
    ("要素价格（人均）",
     "<span class='mj'>r_t=Af'(k_t),\\quad w_t=A[f(k_t)-k_tf'(k_t)]</span>",
     "<b>w 是残差</b>：资本按边际产品拿走，剩下归劳动"),
    ("稳态（隐式）",
     "<span class='mj'>\\delta k^*=sAf(k^*)</span>",
     "一般函数只能隐式定义；Cobb-Douglas 才有闭式解"),
    ("稳态（Cobb-Douglas）★",
     "<span class='mj'>k^*=\\left(\\dfrac{sA}{\\delta}\\right)^{\\frac{1}{1-\\alpha}}</span>",
     "<b>s 与 A 对称</b>：都以乘积出现 ⇒ 翻倍效果相同"),
    ("稳态利率（CD 专用）★",
     "<span class='mj'>r^*=\\dfrac{\\alpha\\delta}{s}</span>",
     "<b>与 A 无关</b> ⇒ ↑A 后 r* 回到原水平（第 28 页的根据）"),
    ("黄金律条件 ★",
     "<span class='mj'>Af'(k^*_{GR})=\\delta</span>",
     "边际产出 = 折旧；<b>CD 下 <span class='mj'>s_{GR}=\\alpha</span></b>"),
    ("黄金律的微分证明",
     "<span class='mj'>\\dfrac{\\partial c^*}{\\partial s}=[Af'(k^*)-\\delta]\\dfrac{\\partial k^*}{\\partial s}</span>",
     "符号由括号决定 ⇒ 与「是否低于黄金律」等价"),
    ("劳动增强型技术",
     "<span class='mj'>Y_t=AF(K_t,Z_tL_t),\\quad Z_t=(1+z)^t,\\ L_t=(1+n)^t</span>",
     "<b>只有这种形式才有平衡增长</b>；z=n=0 退回 Part I"),
    ("效率单位运动方程 ★",
     "<span class='mj'>\\hat k_{t+1}=\\dfrac{1}{(1+z)(1+n)}[sAf(\\hat k_t)+(1-\\delta)\\hat k_t]</span>",
     "分母 = 「稀释因子」；稳态条件见下一行"),
    ("效率单位稳态条件 ★",
     "<span class='mj'>sAf(\\hat k^*)=(\\delta+z+n+zn)\\hat k^*</span>",
     "<b>有效折旧率 <span class='mj'>\\delta+z+n</span></b>（必考）"),
    ("效率单位稳态（CD）",
     "<span class='mj'>\\hat k^*=\\left(\\dfrac{sA}{\\delta+z+n+zn}\\right)^{\\frac{1}{1-\\alpha}}</span>",
     "把 Part I 的 δ 换成 <span class='mj'>\\delta+z+n+zn</span>"),
    ("稳态增长率 ★",
     "<span class='mj'>\\dfrac{k_{t+1}}{k_t}=1+z,\\quad r^*=Af'(\\hat k^*)\\ \\text{constant}</span>",
     "<b>人均 = z、总量 = z+n、r = 0</b>"),
    ("稳态工资",
     "<span class='mj'>w^*=Z_t[Af(\\hat k^*)-Af'(\\hat k^*)\\hat k^*]</span>",
     "方括号是常数 ⇒ <b>w 以 z 增长</b>"),
]

# ============================ 总表 ============================
POS, NEG, ZERO, UP_DOWN = "<b>+</b>", "<b>−</b>", "0", "—"

EXTRA_TABLES = [
    {
        "title": "生产函数七条假设：式子、含义、为什么需要",
        "sub": "对应第 7–8 页。<b>这七条不是「技术要求」，每一条都在为后面的某一步服务</b>——最后一列就是它在模型里的用途。考试若问「为什么需要某条假设」，直接查最后一列。",
        "table_class": "ctr",
        "first_col_bold": True,
        "header": ["#", "假设", "式子", "经济含义", "在模型里的用途"],
        "rows": [
            ["1", "两种投入缺一不可", "<span class='mj'>F(0,L)=F(K,0)=0</span>", "没有机器或没有人都生产不出来", "保证等产量线不与坐标轴相交；k=0 时 y=0（曲线过原点）"],
            ["2", "规模报酬不变", "<span class='mj'>F(\\gamma K,\\gamma L)=\\gamma F(K,L)</span>", "所有投入同比例放大，产出同比例放大", "<b>人均化的许可证</b>（<span class='mj'>y=Af(k)</span>）+ <b>零利润</b>（欧拉定理）"],
            ["3", "边际产出为正", "<span class='mj'>F_K&gt;0,\\ F_L&gt;0</span>", "多投入一定多产出", "要素需求曲线在正象限；<span class='mj'>f'(k)&gt;0</span>"],
            ["4", "边际产出递减", "<span class='mj'>F_{KK}&lt;0,\\ F_{LL}&lt;0</span>", "多给一点，多产出的增量越来越少", "<b>稳态存在的根本原因</b>（否则资本无限积累）"],
            ["5", "资本与劳动互补", "<span class='mj'>F_{KL}=F_{LK}&gt;0</span>", "资本多了，劳动的边际产出也变高", "K↑ ⇒ 劳动需求右移 ⇒ <b>w 上升</b>（第 12、28 页）"],
            ["6", "零点处边际产出无穷", "<span class='mj'>\\lim_{K\\to 0}F_K=\\infty</span>", "第一台机器极其有用", "曲线<b>从 45° 线上方出发</b> ⇒ 不会卡在 k=0"],
            ["7", "无穷远处边际产出为零", "<span class='mj'>\\lim_{K\\to\\infty}F_K=0</span>", "机器极多时再加几乎无用", "曲线<b>最终落到 45° 线下方</b> ⇒ 必有交点"],
            "第 6、7 条合称 <b>Inada 条件</b>：二者相合，保证储蓄曲线与 45° 线在 (0, ∞) 内<b>至少相交一次</b>；再加上第 4 条的严格凹性 ⇒ <b>恰好一次</b> ⇒ 稳态存在且唯一。",
        ],
        "note": "验证技巧：Cobb-Douglas 逐条代进去即可。其中第 4 条最容易算错——<span class='mj'>F_{KK}=\\alpha(\\alpha-1)K^{\\alpha-2}L^{1-\\alpha}</span>，因为 <span class='mj'>\\alpha&lt;1</span> 所以 <span class='mj'>\\alpha(\\alpha-1)&lt;0</span>，<b>负号来自「α 减 1」这一项，不是来自 α</b>。",
    },
    {
        "title": "↑A 与 ↑s 全对比（六个变量 × 当期 / 长期）",
        "sub": "对应第 26–33 页。「当期」＝冲击那一期，「长期」＝新稳态。<b>这张表把两个实验的全部差别一次列清</b>：注意 <span class='mj'>k</span> 永远不跳、<span class='mj'>y</span> 只在 ↑A 时跳、<span class='mj'>r</span> 的方向完全相反。",
        "table_class": "ctr",
        "first_col_bold": True,
        "header": ["变量", "↑A 当期", "↑A 长期（相对原水平）", "↑s 当期", "↑s 长期（相对原水平）"],
        "rows": [
            ["k<sub>t</sub>", "0（<b>预定，不跳</b>）", "更高（<b>水平↑</b>，增长率回 0）", "0（<b>预定，不跳</b>）", "更高（<b>水平↑</b>，增长率回 0）"],
            ["y<sub>t</sub>", "<b>+</b>（跳升，A 直接放大）", "更高", "0（y=Af(k)，A、k 都没变）", "更高"],
            ["c<sub>t</sub>", "<b>+</b>（同 y，比例不变）", "更高", "<b>−</b>（跳降，份额变小）", "<b>?</b> 不定（取决于 s 与 s<sub>GR</sub>）"],
            ["i<sub>t</sub>", "<b>+</b>（同 y）", "更高", "<b>+</b>（份额变大）", "更高"],
            ["w<sub>t</sub>", "<b>+</b>（AF<sub>L</sub> 里 A↑）", "更高（一路上涨，<b>不回落</b>）", "0（A、k 都没变）", "更高"],
            ["r<sub>t</sub>", "<b>+</b>（Af′(k) 里 A↑）", "<b>回到原水平</b>（Cobb-Douglas 下 r*=αδ/s）", "<b>−</b>（资本供给增加压低租金）", "<b>永久更低</b>（r*=αδ/s，s 在分母）"],
            "★ <b>一句话总结</b>：<b>「A 变 ⇒ 当期产出与所有价格都跳；s 变 ⇒ 当期只有分配（c 与 i 反向）跳，产出不动。」</b>长期唯一方向相反的是 <b>r</b>：A 让它回原点，s 让它永久下降。",
        ],
        "note": "记忆口诀：<b>「存量慢、流量跳、资本价格回原点、劳动价格一路上」</b>（↑A）；<b>「s 变只动分配、r 一路下台阶」</b>（↑s）。",
    },
    {
        "title": "三种口径与三种增长率（Part II 的核心）",
        "sub": "对应第 49–55 页。<b>帽子 = 效率单位</b>，这一栏是 Part II 的稳态；中间一栏是「人」看到的量（考试问的通常是这一栏）；最后一栏是总量。<b>把三栏的增长率分开记，是这一讲最后的得分点。</b>",
        "table_class": "ctr",
        "first_col_bold": True,
        "header": ["变量族", "每效率单位（带帽）", "人均（per worker）", "总量（aggregate）"],
        "rows": [
            ["资本", "<span class='mj'>\\hat k^*</span>：<b>常数</b>", "<span class='mj'>k_t=\\hat k^*Z_t</span>：以 <b>z</b> 增长", "<span class='mj'>K_t=\\hat k^*Z_tL_t</span>：以 <b>z+n</b> 增长"],
            ["产出", "<span class='mj'>\\hat y^*=Af(\\hat k^*)</span>：<b>常数</b>", "以 <b>z</b> 增长", "以 <b>z+n</b> 增长"],
            ["消费 / 投资", "常数（都是 <span class='mj'>\\hat y</span> 的固定比例）", "以 <b>z</b> 增长", "以 <b>z+n</b> 增长"],
            ["工资 w", "—", "以 <b>z</b> 增长（<span class='mj'>w=Z_t[\\cdots]</span>）", "以 <b>z+n</b> 增长（<span class='mj'>wL</span> 与 Y 同速）"],
            ["资本租金 r", "<span class='mj'>r^*=Af'(\\hat k^*)</span>：<b>常数</b>", "<b>常数</b>（<b>不增长</b>）", "<b>常数</b>"],
            ["比率", "—", "<b>K/Y 不变</b>、<b>wL/Y 不变</b>", "同左"],
            "★ <b>为什么这些是「六个典型事实」</b>：① y 增长；② k 增长；③ K/Y 不变；④ wL/Y 不变；⑤ r 不变；⑥ w 增长——<b>与 Topic 1 的数据一一对应，这就是模型最大的成功。</b>下表是第 33 页那组参数的数值版。",
        ],
        "note": "数值校验（第 33 页）：<span class='mj'>s=0.2,\\alpha=1/3,\\delta=0.1,A=1</span> ⇒ <span class='mj'>k^*=2^{1.5}\\approx 2.83</span>、<span class='mj'>y^*\\approx 1.41</span>、<span class='mj'>r^*=\\alpha\\delta/s\\approx 0.167</span>。A 升到 1.1 后 <span class='mj'>k^*\\approx 3.26</span>、<span class='mj'>y^*\\approx 1.63</span>，<b>而 r* 仍是 0.167</b>——这就是「↑A 不改变长期利率」的数值证据。",
    },
]

# ============================ 概念速查 ============================
SUMMARY_ROWS = [
    ("本讲要回答", "各国为什么贫富悬殊、长期增长从哪来", "T1 事实 → T2 模型"),
    ("模型的两句结论", "<b>生产率决定长期增长</b>；<b>生产率决定跨国差异</b>（都不是资本）", "第 3 页"),
    ("五个建模约定", "封闭、单一最终品、离散时间、代表性个体、物价归一", "≠ 有货币"),
    ("家庭的「退化」", "<b>不优化</b>：固定比例 s 储蓄；劳动<b>无弹性</b>供给", "与 T4 的根本差别"),
    ("厂商", "价格接受者；<b>CRTS</b>；Cobb-Douglas 是常用具体形式", "<span class='mj'>F=K^{\\alpha}L^{1-\\alpha}</span>"),
    ("七条假设的分工", "CRTS 管人均化；递减报酬管稳态；Inada 管唯一性", "见 xt1"),
    ("要素需求", "<b>w = AF<sub>L</sub>、r = AF<sub>K</sub></b>（边际成本 = 边际收益）", "价格归一 ⇒ 不乘 P"),
    ("零利润", "CRTS + 欧拉定理 ⇒ 产出被报酬分光 ⇒ <b>家庭收入 = Y</b>", "第 11 / 44 页"),
    ("劳动市场", "供给垂直 ⇒ <b>L ≡ L̄，就业不波动，w 由需求定</b>", "RBC 要改的地方"),
    ("资本市场的时序", "<b>本期投资 → 下期资本</b> ⇒ k<sub>t</sub> 是<b>预定</b>的", "决定「k 不跳」"),
    ("唯一的动态方程", "<b>k<sub>t+1</sub> = sAf(k<sub>t</sub>) + (1−δ)k<sub>t</sub></b>", "其余五条是静态附属"),
    ("稳态", "<b>投资 = 折旧</b>（sAf(k*)=δk*）；k* 由 s、A、δ 决定", "无「最优」含义"),
    ("稳态唯一性", "Inada ⇒ 曲线从上方进、下方出；凹 ⇒ 只穿一次", "第 22 页论证"),
    ("收敛", "<b>全局稳定</b>：从任何 k<sub>0</sub>≠0 都收敛；<b>单调不超调</b>", "阶梯图"),
    ("收敛速度", "越近越慢；CD 下约 (1−α)(n+z+δ) ≈ 每年 4–5%", "T3 会用来对比现实"),
    ("CD 闭式解", "<b>k* = (sA/δ)<sup>1/(1−α)</sup></b>；s 与 A 对称", "第 25 页"),
    ("CD 稳态利率", "<b>r* = αδ/s</b>，<b>与 A 无关</b>", "↑A 后 r 回原点的根据"),
    ("工资份额", "w/y = 1−α（CD 下恒定）⇒ 劳动份额约 2/3", "第 20 页"),
    ("↑A 的效应", "曲线<b>非平行</b>上移；k*↑；<b>y、c、i、w 当期跳升</b>；<b>r 跳升后回落</b>", "第 27–29 页"),
    ("↑s 的效应", "曲线上移；k*↑；<b>y 当期不跳</b>；<b>c 跳降</b>；<b>r 跳降且永久更低</b>", "第 30–32 页"),
    ("c 的模糊性", "s↑：短期 c 必降，长期<b>不定</b>（看 s 与 s<sub>GR</sub>）", "第 32 / 46 页"),
    ("为什么没有持续增长", "<b>边际报酬递减</b>；s 有上界 1；反复加 s 会让 r 一路跌", "第 34–35 页"),
    ("黄金律", "<b>Af′(k<sub>GR</sub>) = δ</b>；CD 下 <b>s<sub>GR</sub> = α</b>", "第 39–40 页"),
    ("动态无效", "<b>只在 k* > k<sub>GR</sub> 时有确定结论</b>：减储蓄可双赢", "低于黄金律 ≠ 储蓄不足"),
    ("Part II 的补丁", "劳动增强型技术 <b>Z<sub>t</sub>=(1+z)<sup>t</sup></b>；效率单位化", "只有它能平衡增长"),
    ("有效折旧率", "<b>δ + z + n + zn</b>（稳态条件里代替 δ）", "必考式"),
    ("稳态增长率", "<b>效率单位 0；人均 z；总量 z+n；r 不变</b>", "第 53–54 页"),
    ("六个典型事实", "y、k、w 涨 z；K/Y、wL/Y 不变；r 不变", "第 55 页 = T1 的事实"),
]

# ============================ 易错清单 ============================
PITFALLS = [
    ("把 <span class='mj'>s</span> 当成「家庭的选择」",
     "<b>s 是外生参数</b>，家庭不优化。只有第 38–41 页的黄金律才讨论「它应该是多少」——那是<b>规范问题</b>，不是模型的结果"),
    ("说劳动供给曲线向上倾斜",
     "<b>Solow 里劳动供给是垂直线</b>（无弹性）。所以就业恒等于人口、<b>不产生就业波动</b>——这是它被 RBC 批评的核心"),
    ("把 <span class='mj'>F_K</span> 与 <span class='mj'>f'(k)</span> 混用",
     "<span class='mj'>F_K(K,L)=f'(k)</span> 只在 <b>CRTS</b> 下成立（偏导零次齐次）。写成 <span class='mj'>F_K=f'(K)</span> 等于假设 L=1"),
    ("人均化时忘记 CRTS",
     "<span class='mj'>y=Af(k)</span> 的推导<b>完全依赖一次齐次</b>。规模报酬递减时 <span class='mj'>F(K,L)/L</span> 还依赖 L，模型画不成二维图"),
    ("稳态条件写成「投资=0」",
     "<b>稳态是「投资 = 折旧」</b>（<span class='mj'>sAf(k^*)=\\delta k^*</span>），不是「不投资」。投资一直在发生，只是全部用来补折旧"),
    ("把 k<sub>t</sub> 当成可以跳的变量",
     "<b>k<sub>t</sub> 是存量、预定</b>：冲击当期不动，只能从下一期开始变。<b>「哪些变量跳」的答案永远是「除 k 外全部」</b>"),
    ("把 ↑A 的曲线画成平行上移",
     "<span class='mj'>sAf(k)</span> 是<b>乘性</b>放大，<b>k 越大抬得越多</b>。画成平行上移要扣分"),
    ("说 ↑A 会永久提高利率",
     "<b>CD 下 <span class='mj'>r^*=\\alpha\\delta/s</span> 与 A 无关</b>。当期 r 跳升，长期<b>回到原水平</b>（只有 ↑s 才让 r 永久下降）"),
    ("说 ↑s 一定提高长期消费",
     "<b>短期 c 必降</b>；长期取决于 s 与 s<sub>GR</sub>。<b>s &gt; s<sub>GR</sub> 时长期 c 反而更低</b>——这就是动态无效"),
    ("把「低于黄金律」说成「储蓄不足」",
     "<b>低于黄金律只说明「多存能让未来消费更高」</b>，但代价是今天更低；<b>是否值得取决于偏好，模型不能判断</b>。<b>只有高于黄金律才有确定结论</b>"),
    ("黄金律条件写成 <span class='mj'>f'(k)=0</span>",
     "正确的是 <b><span class='mj'>Af'(k)=\\delta</span></b>。写成 <span class='mj'>f'=0</span> 是「产出最大」的条件（对应 s=1，人会饿死）"),
    ("把 <span class='mj'>k^*</span> 与 <span class='mj'>k^*_{GR}</span> 混为一谈",
     "<b><span class='mj'>k^*</span> 是模型的结果</b>（给定 s 收敛到哪），<b><span class='mj'>k^*_{GR}</span> 是规范标准</b>（哪个 s 让 c 最大）。<b>两者一般不重合</b>"),
    ("第 22 页与第 37 页两张图搞混",
     "第 22 页：横轴 k<sub>t</sub>、<b>纵轴 k<sub>t+1</sub></b>（映射图，能画收敛）；第 37 页：横轴 k<sub>t</sub>、<b>纵轴产出量</b>（流量图，能看消费分解）"),
    ("把投资曲线写成 <span class='mj'>sAf(k)+(1-\\delta)k</span>",
     "第 37 页的投资曲线是 <b><span class='mj'>sAf(k)</span></b>；<span class='mj'>sAf+(1-\\delta)k</span> 是第 22 页的「下一期资本」，两者差一个 <span class='mj'>(1-\\delta)k</span>"),
    ("说 Part II 里人均资本在稳态不变",
     "<b>不变的是「效率单位」资本 <span class='mj'>\\hat k^*</span></b>；<b>人均 <span class='mj'>k</span> 以 z 增长</b>、总量以 z+n 增长"),
    ("把人均增长率写成 z+n",
     "<b>人均 = z，总量 = z+n</b>。n 只稀释总量，不改变人均增长率"),
    ("稳态条件里漏掉 <span class='mj'>(1+z)(1+n)</span>",
     "正确：<b><span class='mj'>sAf(\\hat k^*)=(\\delta+z+n+zn)\\hat k^*</span></b>。<b>把 n、z 当成「额外折旧」</b>是最好记的说法"),
    ("以为技术进步在任何形式下都能带来平衡增长",
     "<b>只有劳动增强型</b> <span class='mj'>Y=F(K,ZL)</span> 才行；Hicks 中性或资本增强型都<b>不能</b>让 K/Y 稳定（CD 是例外）"),
]

# ============================ 自测 ============================
QUIZ = [
    ("（热身）为什么说「人均工时无趋势」这个事实，直接把问题逼到了「资本 or 生产率」这个岔路口？",
     "因为增长核算把人均产出的增长拆成三项：<b>资本深化 + 劳动投入 + 生产率</b>。<br>"
     "«人均工时无趋势» 意味着<b>第二项长期近似为零</b>——人们并没有越干越多（也没有越干越少）。"
     "于是「为什么越来越富」就只剩两种解释：<b>每人配的机器更多</b>（资本深化），或<b>同样机器产出更多</b>（生产率）。<br>"
     "<b>Solow 模型的任务就是判这两条路谁走得通</b>，结论是前者有上限、后者没有。"),

    ("CRTS 这一个假设，在模型里被用了<u>两次</u>，分别是什么？",
     "<b>第一次：人均化</b>。<span class='mj'>F(K,L)=L\\,F(K/L,1)</span> ⇒ <span class='mj'>y=Af(k)</span>，"
     "把两个自变量的函数压成一个，才能画在 (k, y) 平面上。<b>没有它，整讲的图形分析都不存在。</b><br>"
     "<b>第二次：零利润</b>。一次齐次 ⇒ 欧拉定理 ⇒ <span class='mj'>AF=wL+rK</span> ⇒ 产出恰好被要素报酬分光 ⇒ <b>家庭收入就是 Y</b>，"
     "模型里不存在利润收入。<br>"
     "答题时把这两次分开写，才算完整。"),

    ("（重点）用图形说明稳态存在且唯一，并说明 Inada 条件在其中扮演什么角色。",
     "<b>三条论证，缺一不可</b>：<br>"
     "① <b>存在性</b>：Inada 的 <span class='mj'>f'(0)=\\infty</span> 使曲线在原点处<b>无限陡</b> ⇒ 一定从 45° 线<b>上方</b>出发；"
     "<span class='mj'>f'(\\infty)=0</span> 使曲线最终斜率只剩 <span class='mj'>1-\\delta&lt;1</span> ⇒ 一定<b>落到 45° 线下方</b>。"
     "连续函数从上方穿到下方 ⇒ <b>至少一个交点</b>。<br>"
     "② <b>唯一性</b>：<span class='mj'>f</span> 严格凹 ⇒ 曲线与 45° 线的差 <span class='mj'>sAf(k)-\\delta k</span> 严格递减 ⇒ <b>至多一个交点</b>。<br>"
     "③ <b>稳定性</b>：交点左侧曲线在上方（k 上升）、右侧在下方（k 下降）⇒ <b>全局稳定</b>。<br>"
     "<b>Inada 的作用就是「保证交点不会被推到 0 或无穷」</b>——如果 <span class='mj'>f'(0)</span> 有限，曲线可能一出发就在 45° 下方（k=0 成为稳态，经济起不来）；"
     "如果 <span class='mj'>f'(\\infty)&gt;0</span>，曲线可能永远追不上 45° 线（资本无限积累，无稳态）。"),

    ("（重点）↑A 与 ↑s 在图上看起来几乎一样，为什么动态却完全不同？请用「当期能跳什么」来解释。",
     "<b>关键在「谁当场决定」。</b><br>"
     "<b>↑A</b>：A 出现在生产函数里，<b>当期就变</b>。所以 <span class='mj'>y=Af(k)</span> 在 t 期立刻跳升（k 没变但 A 变了），"
     "<span class='mj'>c=(1-s)y</span>、<span class='mj'>i=sy</span> 随之跳，<span class='mj'>w=AF_L</span>、<span class='mj'>r=Af'(k)</span> 也跳。<b>除 k 外全部跳。</b><br>"
     "<b>↑s</b>：s 只出现在<b>分配</b>里，不进入生产函数。所以 <span class='mj'>y=Af(k)</span> 当期<b>一点不动</b>；"
     "只有 <span class='mj'>c=(1-s)y</span> 与 <span class='mj'>i=sy</span> 反向跳（分配变了）；<span class='mj'>w</span> 也不动。<br>"
     "<b>长期差别只有一个方向相反</b>：<span class='mj'>r^*=\\alpha\\delta/s</span>——A 不在这个式子里，所以 ↑A 后 r 回原水平；s 在分母，所以 ↑s 后 r 永久更低。<br>"
     "一句话：<b>「A 变，产出当场变；s 变，只是分配当场变。」</b>"),

    ("（计算）给定 <span class='mj'>y=Ak^{1/3}</span>、<span class='mj'>s=0.2</span>、<span class='mj'>\\delta=0.1</span>、<span class='mj'>A=1</span>。求 <span class='mj'>k^*,y^*,c^*,i^*,r^*,w^*</span>；再求 <span class='mj'>s_{GR}</span> 并判断是否过度储蓄。",
     "<b>稳态</b>：<span class='mj'>\\delta k^*=sA(k^*)^{1/3}</span> ⇒ <span class='mj'>(k^*)^{2/3}=sA/\\delta=2</span> ⇒ <span class='mj'>k^*=2^{1.5}\\approx 2.83</span>。<br>"
     "<span class='mj'>y^*=(k^*)^{1/3}=\\sqrt{2}\\approx 1.41</span>，<span class='mj'>c^*=0.8\\times 1.41\\approx 1.13</span>，<span class='mj'>i^*=0.2\\times 1.41\\approx 0.28</span>。<br>"
     "<span class='mj'>r^*=\\alpha y^*/k^*=\\tfrac13\\cdot\\tfrac{1.41}{2.83}\\approx 0.167</span>（<b>也可直接用 <span class='mj'>\\alpha\\delta/s=0.1/0.6\\approx 0.167</span> 秒算</b>），"
     "<span class='mj'>w^*=(1-\\alpha)y^*\\approx 0.94</span>。<br>"
     "<b>黄金律</b>：<span class='mj'>Af'(k)=\\alpha k^{-2/3}=\\delta</span> ⇒ <span class='mj'>k_{GR}=(\\alpha/\\delta)^{1.5}=(10/3)^{1.5}\\approx 6.09</span>；"
     "对应 <span class='mj'>s_{GR}=\\delta k_{GR}/y_{GR}</span>。更快的办法：<b>Cobb-Douglas 下 <span class='mj'>s_{GR}=\\alpha=1/3</span></b>。<br>"
     "<b>结论</b>：<span class='mj'>s=0.2&lt;s_{GR}=0.33</span> ⇒ <b>资本不足</b>（不是过度储蓄，<b>没有</b>动态无效）；提高 s 会同时提高长期消费。"),

    ("（重点）为什么说「黄金律的 s 就是 α」，这个结论依赖什么？",
     "<b>推导</b>：黄金律 <span class='mj'>Af'(k_{GR})=\\delta</span>，而 <span class='mj'>Af'(k)=\\alpha Ak^{\\alpha-1}=\\alpha y/k</span>。"
     "所以 <span class='mj'>\\alpha y_{GR}/k_{GR}=\\delta</span> ⇒ <span class='mj'>\\delta k_{GR}=\\alpha y_{GR}</span>。<br>"
     "而黄金律的稳态也满足 <span class='mj'>s_{GR}Af(k_{GR})=\\delta k_{GR}</span>，即 <span class='mj'>s_{GR}y_{GR}=\\delta k_{GR}</span>。<br>"
     "两式相比：<b><span class='mj'>s_{GR}y_{GR}=\\alpha y_{GR}</span> ⇒ <span class='mj'>s_{GR}=\\alpha</span>。</b><br>"
     "<b>依赖两个条件</b>：① <b>Cobb-Douglas</b>（否则 <span class='mj'>Af'(k)\\cdot k/y</span> 不是常数 α）；② <b>没有人口增长与技术进步</b>（Part II 里会变成 <span class='mj'>s_{GR}=\\alpha(z+n+\\delta)/(\\delta+...)</span> 之类的形式，<b>不再等于 α</b>）。<br>"
     "<b>经济直觉</b>：α 是资本份额。黄金律要求「资本拿到它该拿的、剩下的全归劳动」，而 CD 下资本份额恒为 α——<b>所以 s 必须恰好等于资本份额。</b>"),

    ("（辨析）「低于黄金律」与「动态无效」是同一个意思吗？为什么这两件事不对称？",
     "<b>不是。</b><br>"
     "<b>低于黄金律</b>：再提高 s，未来消费会更高，但<b>今天消费更低</b>——<b>符号相反</b>，是否划算取决于「未来相对于今天值多少」（时间偏好）。"
     "Solow 模型里<b>没有偏好参数</b>，所以它<b>无法判断</b>这种情形好不好。只能说「还有空间」，不能说「应该多存」。<br>"
     "<b>高于黄金律（动态无效）</b>：降低 s，<b>今天与未来的消费同时提高</b>——<b>符号相同、双赢</b>。所以<b>无论偏好如何，现状都不是最优</b>。<br>"
     "<b>不对称的根源</b>：一边是「跨期权衡」，另一边是「帕累托改进」。<b>只有后者能给出无条件的结论。</b><br>"
     "补充：现实中几乎没有经济体被证明处在黄金律右边（<span class='mj'>s&gt;\\alpha\\approx 1/3</span> 的国家很少，且证据不强）。"),

    ("（重点）Part II 只改了两件事，为什么就能产生持续增长？「效率单位」到底解决了什么问题？",
     "<b>改的两件事</b>：① 生产函数加上劳动增强型技术 <span class='mj'>Y=AF(K,ZL)</span>；② 人均化从「除以 L」改成「除以 <span class='mj'>ZL</span>」。<br>"
     "<b>解决的问题</b>：Part I 里「稳态」与「增长」是矛盾的——稳态的定义就是「不变」，所以模型无法产生增长。"
     "Part II 的做法是<b>换一把尺子</b>：用「每效率单位」计量时，<b>稳态照旧存在</b>（<span class='mj'>\\hat k^*</span> 不变）；"
     "而换算回「每人」时，因为 <span class='mj'>Z_t</span> 一直在涨，<b>人均量就以 z 增长</b>。<br>"
     "<b>所以「稳态」与「持续增长」并不矛盾——它们量的不是同一个东西。</b><br>"
     "<b>代价</b>：z 是<b>外生给定</b>的。模型解释了「有技术进步会怎样」，但没解释「技术进步从哪来」——这是内生增长理论要补的洞。"),

    ("（计算）把 <span class='mj'>n=0.01</span>、<span class='mj'>z=0.02</span>、<span class='mj'>\\delta=0.1</span>、<span class='mj'>\\alpha=1/3</span>、<span class='mj'>s=0.2</span>、<span class='mj'>A=1</span> 代入 Part II，求有效折旧率与 <span class='mj'>\\hat k^*</span>，并说明它比 Part I 的 <span class='mj'>k^*</span> 小多少。",
     "<b>有效折旧率</b>：<span class='mj'>\\delta+z+n+zn=0.1+0.02+0.01+0.0002\\approx 0.130</span>（比 0.1 大 30%）。<br>"
     "<b><span class='mj'>\\hat k^*=\\left(\\dfrac{sA}{\\delta+z+n+zn}\\right)^{1.5}=\\left(\\dfrac{0.2}{0.130}\\right)^{1.5}\\approx 1.538^{1.5}\\approx 1.91</span></b>，"
     "而 Part I 的 <span class='mj'>k^*=2^{1.5}\\approx 2.83</span>。<b>小约 32%</b>。<br>"
     "<b>为什么</b>：分母从 δ 变成 <span class='mj'>\\delta+z+n</span>——<b>人口与技术增长都在「稀释」资本</b>（同样的机器要分给更多有效劳动）。<br>"
     "<b>注意别误读</b>：<span class='mj'>\\hat k^*</span> 更小<b>不代表生活水平更低</b>，因为它衡量的是「每效率单位」，而人均产出是 <span class='mj'>\\hat y\\cdot Z_t</span>——<b>Z 在增长，所以人均产出会一路上升。</b>"),

    ("（综合）如果要用一句话向别人解释「Solow 模型最重要的贡献」，你会怎么说？请给出两层理由。",
     "<b>一句话</b>：<b>它用最少的假设证明了「资本积累不能带来持续增长」，从而把长期增长的解释力逼到生产率上。</b><br>"
     "<b>第一层（排除法）</b>：递减报酬 + s 有上界 1 ⇒ 任何参数变化都只有<b>水平效应</b>、没有<b>增长效应</b>；"
     "反复提高 s 还会让 r 一路下降，与「r 长期稳定」的事实矛盾。<b>于是「靠储蓄变富」这条路被彻底堵死。</b><br>"
     "<b>第二层（建设性）</b>：加上劳动增强型技术后，模型<b>同时</b>给出六个典型事实（y、k、w 涨 z；K/Y、wL/Y 不变；r 不变），"
     "<b>第一次让增长模型与长期数据对上</b>；而且它给出的「条件收敛」与「收敛速度约 4–5%」成为后续所有增长研究（含 Topic 3 的跨国核算）的基准。<br>"
     "<b>所以它的价值不在「算得准」，而在「把问题问对了」。</b>"),
]


# ===== 考点标注：供 build_notes.py 渲染「页首徽标 + 本讲考点一览」=====
# k: final = 期末练习 Key Concepts（老师亲手划）／mid = 期中练习 Key Concepts
#    must  = 我横向整理判断的必背项（没有老师名录背书）
EXAM = {
    4:  [{"k": "mid", "t": "代表性个体／代表性家庭：五个建模约定的第一条"}],
    7:  [{"k": "mid", "t": "前四条假设：缺一不可、规模报酬不变、边际产出为正、递减"}],
    8:  [{"k": "mid", "t": "Inada 条件：零投入边际产出无穷、无穷投入边际产出为零"}],
    10: [{"k": "mid", "t": "要素价格＝边际产品（<span class='mj'>w=AF_{N}</span>、<span class='mj'>r=AF_{K}</span>）"}],
    11: [{"k": "mid", "t": "规模报酬不变 ⇒ 欧拉定理 ⇒ 产出被分光、利润为零"}],
    20: [{"k": "must", "t": "要素价格：<span class='mj'>r=Af'(k)</span> 与 <span class='mj'>w=A[f(k)-kf'(k)]</span>"}],
    21: [{"k": "mid", "t": "稳态的定义：<span class='mj'>k_{t}=k^{*}</span> 对所有 t 成立"}],
    22: [{"k": "mid", "t": "稳态的图形：储蓄曲线与 45° 线的交点"}],
    23: [{"k": "mid", "t": "收敛：落在 <span class='mj'>k^{*}</span> 左边就一定往上走"}],
    25: [{"k": "must", "t": "Cobb-Douglas 的闭式稳态 <span class='mj'>k^{*}=(sA/\\delta)^{1/(1-\\alpha)}</span>"}],
    34: [{"k": "must", "t": "↑A 与 ↑s 都只有水平效应，长期增长率仍为零"}],
    35: [{"k": "must", "t": "全讲最重要一句：持续增长只能来自生产率"}],
    39: [{"k": "mid", "t": "黄金律的特征条件 <span class='mj'>Af'(k^{*}_{GR})=\\delta</span>"}],
    40: [{"k": "mid", "t": "黄金律的图：切线与折旧线平行"}],
    41: [{"k": "mid", "t": "动态无效：黄金律右边减少储蓄能同时增加两期消费"}],
    49: [{"k": "mid", "t": "劳动增强型技术 <span class='mj'>Y=AF(K,ZL)</span>，<span class='mj'>Z_{t}=(1+z)^{t}</span>"}],
    53: [{"k": "mid", "t": "稳态时人均量以 z 增长（模型的增长率为 z，不是零）"}],
}
