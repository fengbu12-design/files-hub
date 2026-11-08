# -*- coding: utf-8 -*-
"""
AF5638 Macroeconomics · Topic 7 内容文件
Equilibrium in a Production Economy（GLS Ch. 12）

写作原则（与 Topic 1/2/3/4/5/6/8/9/10 一致）：
  1) 每页先给「白话」；
  2) 再给「讲解」，把推导的每一步摊开；
  3) 凡有公式的页，「等式两边」说清左右各是什么、为什么相等；
  4) 凡有图的页，「这张图怎么看」说清坐标轴、每条线、怎么读、会怎么考。

本讲特点：它是 Topic 5 的「解锁版」。
  Topic 5：产出固定、劳动固定、投资 = 0 ⇒ 储蓄必须为 0，利率只能让储蓄归零。
  Topic 7：企业要雇人、要投资 ⇒ 储蓄有了「出口」⇒ 利率的任务变了：
          不再是把储蓄逼回 0，而是让储蓄 = 投资。
  三个新零件：生产函数、劳动需求、投资需求；一个技术性假设：GHH 偏好。
"""

COURSE      = "AF5638 宏观经济学 · Macroeconomics"
TOPIC       = 7
TOPIC_TITLE = "Topic 7 · 生产经济中的均衡"
SUBTITLE    = "储蓄终于有了出口：利率不再是把储蓄逼回零，而是让它等于投资"
INSTRUCTOR  = "讲师：Elaine Liu（PolyU）· Fall 2026"
SOURCES     = "课件：Topic 7 - Production Economy（24 页）· 教材：GLS Ch. 12"
SLIDE_COUNT = 24

MAP_CHIPS = [
    ("Topic 1 · 增长事实", False, False),
    ("Topic 2–3 · Solow", False, False),
    ("Topic 4–7 · 跨期模型", True, True),
    ("Topic 8 · 新古典实物侧", False, False),
    ("Topic 9 · 新古典名义侧", False, False),
    ("Topic 10 · 新凯恩斯", False, False),
]

SECTIONS = [
    ("① 从禀赋经济到生产经济", 2),
    ("② 企业：生产、投资、股息", 3),
    ("③ 企业最优化：三个一阶条件", 6),
    ("④ 三条曲线与三张图", 9),
    ("⑤ 家庭：效用与 GHH 偏好", 12),
    ("⑥ 家庭最优化：约束与一阶条件", 14),
    ("⑦ 劳动供给与银行", 19),
    ("⑧ 市场出清与均衡定义", 22),
    ("⑨ 小结：这一讲解锁了什么", 24),
]

TLDR = [
    "<b>这一讲只做两个扩展</b>：① <b>生产内生</b>——加一个企业，它雇人 <span class='mj'>N_{t}</span>、投资 <span class='mj'>I_{t}</span>；② <b>劳动供给内生</b>——家庭在「消费」与「闲暇」之间选。<b>产出不再从天而降</b>，而是 <span class='mj'>Y_{t}=A_{t}F(K_{t},N_{t})</span>。",
    "<b>企业只给三条一阶条件</b>：<span class='mj'>w_{t}=A_{t}F_{N}(K_{t},N_{t})</span>（今天雇人）、<span class='mj'>w_{t+1}=A_{t+1}F_{N}(K_{t+1},N_{t+1})</span>（明天雇人）、<span class='mj'>1+r_{t}=A_{t+1}F_{K}(K_{t+1},N_{t+1})+1-\\delta</span>（投资），最后一条可写成 <b><span class='mj'>r_{t}=\\mathrm{MPK}_{t+1}-\\delta</span></b>。",
    "<b>三张图要能默画</b>：劳动需求<b>下斜</b>（<span class='mj'>w\\uparrow\\Rightarrow N^{d}\\downarrow</span>）、投资需求<b>下斜</b>（<span class='mj'>r\\uparrow\\Rightarrow I^{d}\\downarrow</span>）、劳动供给<b>上斜</b>（<span class='mj'>w\\uparrow\\Rightarrow N^{s}\\uparrow</span>）。<b>注意 <span class='mj'>K_{t}</span> 在劳动需求里是正号、在投资需求里是负号</b>——这是两张图最大的对照考点。",
    "<b>GHH 偏好是本讲唯一的技术性假设</b>：<span class='mj'>u=\\ln[C_{t}+\\theta_{t}\\ln(1-N_{t})]</span>。它让劳动供给的一阶条件化简成 <b><span class='mj'>\\frac{\\theta_{t}}{1-N_{t}}=w_{t}</span></b>——<b>消费 <span class='mj'>C</span> 整个消失</b>，所以劳动供给<b>只看工资，不看收入</b>（<b>无财富效应</b>）。<b>这就是 Topic 8 里 <span class='mj'>Y^{s}</span> 竖直的微观基础。</b>",
    "<b>三个市场、两个价格、六个方程、六个未知数</b>。市场是劳动、可贷资金、商品；价格是 <span class='mj'>w_{t}</span> 与 <span class='mj'>r_{t}</span>；未知数是 <span class='mj'>C_{t},I_{t},N_{t},Y_{t},w_{t},r_{t}</span>。<b>外生只有四个</b>：<span class='mj'>A_{t},A_{t+1},K_{t},\\theta_{t}</span>。",
    "<b>与 Topic 5 最关键的差别：<span class='mj'>S_{t}</span> 不必为 0</b>。家庭想多储蓄，<b>只要 <span class='mj'>r</span> 下降、激励企业多投资，就能实现</b>——<b>投资是储蓄的出口</b>。禀赋经济只是「<span class='mj'>N</span> 与 <span class='mj'>I</span> 都固定」的特例（那时 <span class='mj'>I=0</span>，所以 <span class='mj'>S</span> 只能停在 0）。",
]

# ==================== 符号表 ====================
NOTATION = [
    ("一、企业这一侧（本讲新加的全部符号）", [
        ("<span class='mj'>Y_{t}=A_{t}F(K_{t},N_{t})</span>", "生产函数", "<b>产出 ＝ 技术 × 要素组合</b>。<b>这是「产出从哪来」的答案</b>——Topic 5 里它是一句「<span class='mj'>Y</span> 给定」，这里终于有了来源。"),
        ("<span class='mj'>K_{t}</span>", "期初资本（<b>预定</b>）", "<b>本讲最容易被忽略的一个词</b>：<span class='mj'>K_{t}</span> 是 <b>predetermined</b>——今天已经在那儿了，今天动不了。<b>今天能决定的只有 <span class='mj'>K_{t+1}</span>。</b>"),
        ("<span class='mj'>I_{t},\\ B^{I}_{t}</span>", "投资、投资借款", "<b>两者恒等</b>（<span class='mj'>I_{t}=B^{I}_{t}</span>）：投资的钱<b>全部来自借</b>。<b>这是「企业不进资本市场的例外」——它只借钱，不存钱。</b>"),
        ("<span class='mj'>D_{t}</span>", "股息（dividend）", "<b>企业利润交给家庭</b>。因为<b>企业是家庭拥有的</b>，所以 <span class='mj'>D</span> 是家庭的<b>非劳动收入</b>。<b>家庭收入 = 工资 + 股息。</b>"),
        ("<span class='mj'>V_{t}</span>", "公司价值", "<b>未来股息的现值</b>。<b>企业的目标函数就是它</b>——企业不最大化「当期利润」，而是最大化<b>整个未来现金流的折现</b>。"),
    ]),
    ("二、家庭这一侧（与 Topic 4 的区别）", [
        ("<span class='mj'>N_{t}</span>", "劳动供给（0 到 1）", "<b>新变量</b>。Topic 4/5 里劳动是「给定的」，<b>这里家庭要选它</b>。<b>选了 <span class='mj'>N</span> 就拿不到闲暇。</b>"),
        ("<span class='mj'>1-N_{t}</span>", "闲暇（leisure）", "<b>时间禀赋标准化为 1</b>，所以「不工作的时间」就是 <span class='mj'>1-N</span>。<b>效用从这里来</b>，而不是从「不工作」这个状态本身来。"),
        ("<span class='mj'>\\theta_{t}</span>", "闲暇偏好参数", "<b>「闲暇相对于消费值多少」</b>。<b><span class='mj'>\\theta\\uparrow</span> ＝ 更爱休息 ＝ 同样工资下工作更少</b>。<b>它是本讲第二个外生冲击源</b>（第一个是 <span class='mj'>A</span>）。"),
        ("<span class='mj'>w_{t}</span>", "实际工资", "<b>用最终产品计价</b>（不是名义工资）。<b>它是劳动市场的价格</b>——和 <span class='mj'>r</span> 并列的第二个价格。"),
    ]),
    ("三、价格与市场（本讲的骨架）", [
        ("三个市场", "labor / loanable funds / goods", "<b>劳动</b>（价格 <span class='mj'>w</span>）、<b>可贷资金</b>（价格 <span class='mj'>r</span>）、<b>商品</b>（价格被标准化为 1）。<b>商品市场的「价格」不用解</b>——它被当计价物了。"),
        ("<span class='mj'>N^{d},\\ N^{s}</span>", "劳动需求 / 劳动供给", "<b>两条曲线的交点定 <span class='mj'>w</span> 与 <span class='mj'>N</span></b>。<b>供给来自家庭、需求来自企业</b>。<b>这是本讲唯一「两条曲线都有斜率」的市场。</b>"),
        ("<span class='mj'>I^{d},\\ S</span>", "投资需求 / 储蓄", "<b>可贷资金的需求与供给</b>。<b>交点定 <span class='mj'>r</span></b>。<b>注意：储蓄是「供给」，投资是「需求」</b>——<b>与 Topic 5 只有一个 <span class='mj'>S=0</span> 完全不同了。</b>"),
        ("<span class='mj'>Y_{t}=C_{t}+I_{t}</span>", "商品市场出清", "<b>产出分成消费与投资</b>。<b>注意这里<b>没有 <span class='mj'>G</span></b></b>——本讲先不加政府（加了就是 <span class='mj'>Y=C+I+G</span>，Topic 6 已经做过）。"),
    ]),
    ("四、两个「同名不同号」的陷阱（先记下来，第 4 节会讲）", [
        ("<span class='mj'>K_{t}</span> 进劳动需求：<b>正号</b>", "<span class='mj'>N^{d}(w^{-},A^{+},K^{+})</span>", "<b>资本多 ⇒ 劳动的边际产品高 ⇒ 企业更想雇人</b>。<b>因为 <span class='mj'>F_{KN}&gt;0</span>。</b>"),
        ("<span class='mj'>K_{t}</span> 进投资需求：<b>负号</b>", "<span class='mj'>I^{d}(r^{-},A_{t+1}^{+},K_{t}^{-})</span>", "<b>资本多 ⇒ 距目标只差一点点 ⇒ 新投资少</b>。<b>因为 <span class='mj'>I_{t}=K_{t+1}-(1-\\delta)K_{t}</span>，<span class='mj'>K_{t}</span> 在减号后面。</b>"),
    ]),
]

HOWTO_READ = [
    ("① 先分清「谁在决策」", "本讲有<b>两个决策者</b>：<b>企业</b>选 <span class='mj'>N_{t},N_{t+1},K_{t+1}</span>（等价于选 <span class='mj'>I_{t}</span>）；<b>家庭</b>选 <span class='mj'>C_{t},N_{t},N_{t+1}</span>。<b>看到一阶条件，先问「这是谁对谁求导」。</b><b>企业的约束是技术，家庭的约束是预算</b>——这是两组 FOC 长得不一样的根本原因。"),
    ("② 再看「约束长什么样」", "企业有<b>两条</b>：技术 <span class='mj'>Y=AF(K,N)</span>、资本积累 <span class='mj'>K_{t+1}=I_{t}+(1-\\delta)K_{t}</span>。<b>家庭只有一条</b>：跨期预算（IBC）。<b>企业是「两期都要生产」，家庭是「两期都要消费」</b>——<b>这个对称性是理解全讲的钥匙。</b>"),
    ("③ 遇到一阶条件，先问「放掉了什么」", "<b>每一个 FOC 都是「多要一单位，收益 = 成本」</b>。<b>雇人多一个：多产出的价值 <span class='mj'>A F_{N}</span> ＝ 多付的工资 <span class='mj'>w</span></b>。<b>投资多一块：明年的总回报 <span class='mj'>\\mathrm{MPK}+1-\\delta</span> ＝ 还款 <span class='mj'>1+r</span></b>。<b>把这句话说出来，公式就不用背。</b>"),
    ("④ 最后看「市场怎么接上」", "<b>三条曲线两两相交</b>：<span class='mj'>N^{d}=N^{s}</span> 定 <span class='mj'>w</span> 与 <span class='mj'>N</span>；<span class='mj'>S=I^{d}</span> 定 <span class='mj'>r</span>；<span class='mj'>Y=C+I</span> 定 <span class='mj'>Y</span> 怎么分。<b>但注意：三个市场只有两个独立</b>（瓦尔拉斯定律，第 22 页会讲）。<b>所以「三条曲线」实际只需要解两条。</b>"),
]

# ============================ 逐页讲解 ============================
C = {}
def add(p, **kw):
    C[p] = kw


# ==================== ① 从禀赋经济到生产经济 ====================

add(1,
    kp="本讲把 Topic 5 的<b>禀赋经济</b>升级成<b>生产经济</b>：<b>加一个企业</b>（内生生产、内生投资）＋ <b>让家庭选劳动</b>（内生劳动供给）。<b>产出不再给定，而是 <span class='mj'>Y_{t}=A_{t}F(K_{t},N_{t})</span> 生产出来的。</b>",
    plain="前两讲里，产出是天上掉下来的一块饼，大家只分它。这一讲开始，饼要自己烤：企业租机器、雇工人、把原料变成产品；工人还得决定今天上不上班、上几个小时。于是「利率」这个价格的任务也变了——以前它只负责让大家别多存钱，现在它还得负责让企业愿意借钱去投资。",
    note=(
        "先看这页的三个层次：<br><br>"
        "<b>① 它明确说「我们之前做的是禀赋经济」</b>。禀赋经济 ＝ <b>产出 <span class='mj'>Y_{t}</span> 是外生的</b>，家庭只是「把它在消费与储蓄之间分」。<b>Topic 5 的全部结论都建立在这个简化上</b>（所以那里乘数为零）。<br><br>"
        "<b>② 它说这一讲要「extend to a full-fledged general equilibrium model」</b>。<b>「full-fledged」（完整的、正式的）这个词很关键</b>——意思是<b>该内生的都内生掉</b>：产出、劳动、投资、工资、利率，全部由模型解出来。<b>只留四个外生量</b>（第 24 页会列）。<br><br>"
        "<b>③ 扩展只有两个维度</b>：<br>"
        "· <b>内生生产 ＋ 企业问题</b>：企业选劳动与投资，最大化公司价值。<br>"
        "· <b>内生劳动供给</b>：家庭把时间在「工作」与「闲暇」之间分配。<br><br>"
        "<b>这两个扩展各自带来一组新方程，而它们最终要在劳动市场上碰头</b>——<b>这就是本讲的全部结构</b>。"
    ),
    tip="<b>记住「两条腿」</b>：<b>企业给供给侧的曲线（劳动需求、投资需求），家庭给需求侧的曲线（劳动供给、储蓄）</b>。<b>每一组曲线都是一个最优化问题的产物，而不是假设出来的形状</b>。<b>这是本讲与「画个下斜线说它是需求」最大的区别。</b>",
    warn="<b>别把这一讲当成「Topic 5 加了几页」。</b>Topic 5 的核心结论<b>乘数为零</b>，在生产经济里<b>会变</b>（政府支出能增加产出，因为劳动与资本能重新配置）。<b>[[T8#p18|Topic 8 第 18 页]]会正面讲这件事。</b><b>所以本讲不是「补充」，而是「换了一个世界」。</b>"
)

add(2,
    kp="<b>两个扩展</b>：① <b>内生生产与企业问题</b>——企业按 <span class='mj'>Y_{t}=A_{t}F(K_{t},N_{t})</span> 生产，并决定投资；② <b>内生劳动供给</b>——家庭在消费与闲暇之间选。<b>生产侧与 Solow 模型相似</b>，但<b>投资决策被内生化</b>了。",
    plain="这一页是「施工图」。左边是企业：它有什么技术、怎么攒资本、赚了钱给谁。右边是家庭：它怎么在花钱和休息之间权衡。中间是两个市场：劳动和钱。",
    note=(
        "把这一页的两句话拆开看，它们各自对应后面的一大块内容：<br><br>"
        "<b>①「Endogenous production and firm problem」</b><br>"
        "· <b>生产函数</b>（第 3 页）：<span class='mj'>Y_{t}=A_{t}F(K_{t},N_{t})</span>，七条假设。<br>"
        "· <b>资本积累</b>（第 4 页）：<span class='mj'>K_{t+1}=I_{t}+(1-\\delta)K_{t}</span>，<b>注意这里和 Solow 长得一样，但决策者变了</b>——<b>Solow 里是「储蓄自动变成投资」，这里是「企业借钱投资」</b>。<br>"
        "· <b>企业目标</b>（第 5–6 页）：最大化公司价值 <span class='mj'>V_{t}</span>，不是最大化当期利润。<br>"
        "· <b>三个一阶条件</b>（第 7 页）：两条劳动、一条资本。<br><br>"
        "<b>②「Endogenous labor supply of the household」</b><br>"
        "· <b>效用函数</b>（第 12–13 页）：<span class='mj'>u(C,1-N)</span>，<b>再加 GHH 的具体形式</b>。<br>"
        "· <b>一阶条件</b>（第 16–17 页）：<b>多工作一小时的收益（工资）＝ 少休息一小时的损失</b>。<br>"
        "· <b>劳动供给函数</b>（第 19 页）：<span class='mj'>N^{s}(w,\\theta)</span>。<br><br>"
        "<b>③ 课件特意说「生产侧与 Solow 相似」</b>：<b>生产函数、资本积累、甚至 <span class='mj'>r=\\mathrm{MPK}-\\delta</span> 都和 Solow 一样</b>。<b>区别只在「谁做决策、按什么目标做」</b>——<b>Solow 的储蓄率是外生参数，这里的投资由「跨期利润最大化」决定。</b>"
    ),
    dec=[
        ("endowment economy", "禀赋经济", "<b>产出外生</b>（天上掉下来）。<b>Topic 5 用的就是它</b>。<b>它的极端简化是「<span class='mj'>I=0</span>」，所以储蓄无处可去。</b>"),
        ("full-fledged", "完整的、正式的", "<b>该内生的都内生</b>。<b>这个词提示：后面每一讲都会在这套骨架上加东西（Topic 8 加货币、Topic 9 加粘性）。</b>"),
        ("two dimensions", "两个扩展维度", "<b>生产侧</b>（企业）＋ <b>劳动侧</b>（家庭）。<b>两组合起来才叫「一般均衡」</b>——<b>只加生产、不加劳动供给，就还是「部分均衡」。</b>"),
        ("similar to Solow", "与 Solow 相似", "<b>技术、积累方程都一样</b>。<b>差别是「决策」</b>：<b>Solow 的 <span class='mj'>s</span> 是参数，这里的 <span class='mj'>I</span> 是一阶条件。</b>"),
    ],
    tip="<b>这一讲可以画成一张两栏的表</b>：<b>左栏「企业」，右栏「家庭」，中间一列「市场」</b>。<b>左栏产出的东西（劳动需求、投资需求）正好是右栏要用价格去接的东西。</b><b>写作业时按这张表走，就不会漏方程。</b>",
    warn="<b>别把「生产侧与 Solow 相似」理解成「结论也一样」。</b><b>Solow 里储蓄率外生、劳动供给外生</b>；<b>这里两者都是内生的</b>。<b>所以 Solow 的「稳态」在这里没有对应物</b>——<b>这是两期模型，不是增长模型。</b>"
)


# ==================== ② 企业：生产、投资、股息 ====================

add(3,
    kp="<b>代表性企业按 <span class='mj'>Y_{t}=A_{t}F(K_{t},N_{t})</span> 生产</b>：<span class='mj'>K_{t}</span> 资本、<span class='mj'>N_{t}</span> 劳动、<span class='mj'>A_{t}</span> 外生技术。<b><span class='mj'>F</span> 满足七条假设</b>：两种要素都必需、<b>规模报酬不变</b>、单调递增、<b>边际递减</b>、<b>交叉偏导为正</b>。",
    plain="企业就是一台机器：给它机器和工人，它吐出产品。技术越好（A 大），同样的人手和机器能吐更多。给它加人加机器，产出按同样比例涨（规模报酬不变）。单独加一样，产出涨但越加越不涨（边际递减）。而「人多机器好使、机器多人好使」这一条（交叉偏导为正）是后面两张图对照的关键。",
    lr=[
        dict(name="生产函数：产出从哪来",
             lhs="Y_{t}",
             lhs_t="<b>本期产出</b>（流量，可消费可投资）",
             rhs="A_{t}F(K_{t},N_{t})",
             rhs_t="<b>技术 × 要素组合</b>（<span class='mj'>K</span> 是存量、<span class='mj'>N</span> 是流量）",
             why="<b>左边是「结果」，右边是「原因」。</b><b>这个式子的作用是「把 <span class='mj'>Y</span> 从外生变成内生」</b>——Topic 5 里 <span class='mj'>Y_{t}</span> 是给定的，这里它<b>由右边的三个东西决定</b>。<b>注意 <span class='mj'>A_{t}</span> 在括号外面</b>：<b>技术是「乘上去」的（Hicks 中性）</b>，<b>不是「加进去」的</b>。",
             why_t="为什么是「乘」不是「加」"),
    ],
    note=(
        "七条假设要分成三组来记，<b>每一组买来一个结论</b>：<br><br>"
        "<b>① <span class='mj'>F(0,N)=0,\\ F(K,0)=0</span>——两种要素都必需。</b><b>买来的是「生产必须有资本也要有劳动」</b>：<b>所以企业不能只雇人不买机器，也不能只买机器不雇人。</b><br><br>"
        "<b>② <span class='mj'>F(\\gamma K,\\gamma N)=\\gamma F(K,N)</span>——规模报酬不变（CRS）。</b><b>这条最有用</b>：它保证<b>「把工资付完之后，剩下的正好等于资本的报酬，经济利润为零」</b>（欧拉定理）。<b>所以「企业利润」<span class='mj'>D_{t}=Y_{t}-w_{t}N_{t}</span> 不是「垄断租金」，而是「资本所有者的收入」</b>。<b>这一条让「企业归家庭所有」这件事在逻辑上闭合了</b>：<b>利润最终是要素收入，不是额外的好处。</b><br><br>"
        "<b>③ <span class='mj'>F_{K}&gt;0,F_{N}&gt;0</span>（单调）＋ <span class='mj'>F_{KK}&lt;0,F_{NN}&lt;0</span>（递减）</b>：<b>买来的是「两条需求曲线向下」</b>。<b>第 8 页会说清这个因果链</b>：<span class='mj'>w\\uparrow</span> ⇒ 要恢复 <span class='mj'>w=AF_{N}</span> ⇒ <span class='mj'>F_{N}</span> 得上升 ⇒ 因为 <span class='mj'>F_{NN}&lt;0</span> ⇒ <span class='mj'>N</span> 必须下降。<b>没有 <span class='mj'>F_{NN}&lt;0</span>，劳动需求就是平的（甚至向上），整个模型就散了。</b><br><br>"
        "<b>④ <span class='mj'>F_{KN}&gt;0</span>——交叉偏导为正。</b><b>这一条最容易被跳过，但它是「资本存量影响劳动需求」的唯一依据</b>：<b>机器越多，工人越好使</b> ⇒ <b>同样工资下企业想雇更多人</b> ⇒ <b>劳动需求曲线右移</b>。<b>第 9 页那张图上「<span class='mj'>\\uparrow K_{t}</span>」那个箭头，全部来自这一条。</b>"
    ),
    dec=[
        ("<span class='mj'>Y_{t}</span>", "产出", "<b>流量</b>（每期生产多少）。<b>它有两个去处：消费与投资</b>（第 22 页的出清条件）。"),
        ("<span class='mj'>K_{t}</span>", "资本投入", "<b>存量</b>，且 <b>predetermined</b>——<b>今天已经在那儿，今天动不了。</b><b>这是「短期」的真正含义。</b>"),
        ("<span class='mj'>N_{t}</span>", "劳动投入", "<b>流量</b>，<b>今天可以调</b>。<b>所以「短期」里唯一能变的投入是劳动</b>——<b>这是 <span class='mj'>Y^{s}</span> 形状的来源。</b>"),
        ("<span class='mj'>A_{t}</span>", "外生生产率", "<b>TFP</b>（Topic 3 的主角）。<b>本讲把它当外生冲击源</b>。<b>注意有 <span class='mj'>A_{t}</span> 和 <span class='mj'>A_{t+1}</span> 两个</b>——<b>今天的技术与明天的技术可以不同，这一点很重要</b>（投资需求依赖于 <span class='mj'>A_{t+1}</span>）。"),
        ("<span class='mj'>F_{KK}&lt;0</span>", "资本边际递减", "<b>投资需求向下斜的原因</b>。<b>资本越多，再多一台机器的产出越少。</b>"),
        ("<span class='mj'>F_{KN}&gt;0</span>", "资本与劳动互补", "<b>「机器多人好使」</b>。<b>它是「<span class='mj'>K_{t}\\uparrow</span> 使劳动需求右移」的全部依据。</b><b>也是「<span class='mj'>N</span> 上升使 <span class='mj'>MPK</span> 上升」的依据。</b>"),
        ("CRS", "规模报酬不变", "<b><span class='mj'>F(\\gamma K,\\gamma N)=\\gamma F(K,N)</span></b>。<b>保证「欧拉定理成立、经济利润为零」</b>，<b>从而「股息 = 资本收入」</b>。"),
    ],
    tip="<b>把七条假设按「买来什么」记，比按顺序背强得多</b>：<b>必需性 ⇒ 不能只用一种要素；CRS ⇒ 利润是资本收入；单调＋递减 ⇒ 需求曲线向下；交叉为正 ⇒ 资本影响劳动需求。</b><b>答题时写「因为 <span class='mj'>F_{NN}&lt;0</span>，所以劳动需求向下」，比写「假设边际递减」得分高。</b>",
    warn="<b>别把 <span class='mj'>A_{t}</span> 和 <span class='mj'>K_{t}</span> 混成「都是投入」。</b><b><span class='mj'>K_{t}</span> 是模型内的状态变量（上一期投资的结果），<span class='mj'>A_{t}</span> 是模型外的技术</b>。<b>另一个高频错误：把 CRS 说成「利润为零所以企业无所谓」</b>——<b>企业仍然最大化 <span class='mj'>V_{t}</span>，只是均衡里「经济利润」为零，会计上的「资本收入」不为零。</b>"
)

add(4,
    kp="<b>与 Solow 不同：企业自己拥有资本、自己做投资决策。</b><span class='mj'>K_{t}</span> 是<b>预定</b>的；<span class='mj'>K_{t+1}=I_{t}+(1-\\delta)K_{t}</span>。<b>投资靠向金融中介借钱</b>（利率 <span class='mj'>r_{t}</span>，下期还）：<span class='mj'>I_{t}=B^{I}_{t}</span>。",
    plain="企业想扩产，得先买机器。买机器的钱从哪来？借。借了明年要还本付息。而今天的机器是去年就买好的，改不了——这就是「短期」的意思：你能决定的只有明年有多少机器。",
    lr=[
        dict(name="资本积累：明年的资本从哪来",
             lhs="K_{t+1}",
             lhs_t="<b>明天期初的资本</b>",
             rhs="I_{t}+(1-\\delta)K_{t}",
             rhs_t="<b>新买的（投资）＋ 剩下的（未折旧的旧资本）</b>",
             why="<b>左边是「明天的存量」，右边是「今天的存量怎么变成明天的存量」。</b><b>这是全书出现次数最多的方程之一</b>（Topic 2 的 Solow 也用它）。<b>搬动一下就是投资需求函数</b>：<span class='mj'>I_{t}=K_{t+1}-(1-\\delta)K_{t}</span>——<b>这一行是第 10 页那张图的全部来源</b>。<b>特别注意 <span class='mj'>K_{t}</span> 前面是负号</b>：<b>现有资本越多，需要新买的越少。</b>",
             why_t="为什么要写成这个方向"),
        dict(name="投资的融资约束：只借不存",
             lhs="I_{t}",
             lhs_t="<b>本期投资</b>",
             rhs="B^{I}_{t}",
             rhs_t="<b>本期投资借款</b>",
             why="<b>这是一个「简化的假设」，不是恒等式</b>：<b>企业不保留现金、不发行股票，投资全部靠银行借</b>。<b>为什么可以这样假设？</b>因为<b> Modigliani–Miller：融资结构不影响投资决策</b>。<b>它的好处是把「企业」和「家庭」的储蓄行为彻底分开</b>——<b>家庭是唯一的储蓄者，企业是唯一的借款者（用于投资）。</b>",
             why_t="为什么可以假设「只借不存」"),
    ],
    note=(
        "这一页有两个地方值得停下来：<br><br>"
        "<b>① 为什么说「与 Solow 稍有不同」？</b><br>"
        "· <b>Solow 模型里，储蓄率 <span class='mj'>s</span> 是外生参数</b>，<b>储蓄「自动」变成投资</b>，<b>没有「谁决定投资」这个问题</b>。<br>"
        "· <b>这里投资是一个最优化决策</b>：<b>企业比较「多买一台机器的回报」与「借钱的成本」</b>，<b>再决定买多少</b>。<b>这就是为什么本讲会出现 <span class='mj'>r=\\mathrm{MPK}-\\delta</span> 这个条件，而 Solow 里只有「<span class='mj'>sf(k)=(n+g+\\delta)k</span>」。</b><br><br>"
        "<b>②「<span class='mj'>K_{t}</span> is predetermined」这句话的重要性</b>：<br>"
        "· <b>它把「短期」定义清楚了</b>：<b>短期 ＝ 资本存量给定的时期</b>。<b>所以短期内产出只能靠调劳动来变</b>——<b>这是后面 <span class='mj'>Y^{s}</span> 曲线（Topic 8）的全部微观基础</b>。<br>"
        "· <b>它也让「投资」变成了「跨期决策」</b>：<b>今天花钱，明天才有产出</b>。<b>所以投资必须看 <span class='mj'>A_{t+1}</span> 而不是 <span class='mj'>A_{t}</span></b>（第 10 页会强调）。<br><br>"
        "<b>③ 为什么说「折旧剩下 <span class='mj'>(1-\\delta)K_{t}</span> 也算企业的」？</b><b>因为企业拥有资本</b>（<span class='mj'>the firm owns capital stock</span>）。<b>所以卖掉旧机器（或它的残值）也是企业的现金流入</b>——<b>这就是第 5 页股息里出现 <span class='mj'>+(1-\\delta)K_{t+1}</span> 的原因。</b>"
    ),
    dec=[
        ("predetermined", "预定的", "<b>今天改不了</b>。<b>整个「短期」概念都靠这个词</b>。<b><span class='mj'>K_{t}</span> 预定、<span class='mj'>N_{t}</span> 可变</b>——<b>这是短期与长期的分界。</b>"),
        ("<span class='mj'>\\delta</span>", "折旧率", "<b>每期损失的资本比例</b>。<b>与 Topic 2 同一个 <span class='mj'>\\delta</span></b>，<b>可以放心复用直觉（≈0.1/年这个量级的说法）。</b>"),
        ("<span class='mj'>B^{I}_{t}</span>", "投资借款", "<b>企业的「负债」</b>。<b>注意上标 <span class='mj'>I</span>：它是「为投资而借的」</b>，<b>与政府债券 <span class='mj'>B_{t}</span> 不是一回事。</b>"),
        ("owns capital", "拥有资本", "<b>与 Solow 的关键差别</b>：<b>那里资本是「社会的」，这里是「企业的」</b>。<b>后果：折旧残值、投资决策、利润归属全部落到企业账上。</b>"),
        ("financial intermediary", "金融中介", "<b>银行</b>。<b>第 21 页会证明它「没有主动决策、利润为零」</b>——<b>所以它的所有权不影响任何结论。</b>"),
    ],
    tip="<b>把这条积累方程「正着用、反着用」各记一次</b>：<b>正着用是「存量怎么演化」（第 4 页），反着用是「投资需求」（第 10 页：<span class='mj'>I_{t}=K_{t+1}-(1-\\delta)K_{t}</span>）。</b><b>同一个方程，两个用途，这是本讲最省力的一个记忆点。</b>",
    warn="<b>别把 <span class='mj'>I_{t}</span> 当成「资本」。</b><b><span class='mj'>I</span> 是流量（本期新买），<span class='mj'>K</span> 是存量（累积结果）。</b><b>另一个错误：把「投资」理解成「买股票／买理财」</b>——<b>宏观里的投资永远是「实物资本形成」（机器、厂房、设备）。</b>"
)

add(5,
    kp="<b>企业归家庭所有，利润以股息形式返还。</b><span class='mj'>D_{t}=Y_{t}-w_{t}N_{t}</span>；<span class='mj'>D_{t+1}=Y_{t+1}-w_{t+1}N_{t+1}+(1-\\delta)K_{t+1}-(1+r_{t})B^{I}_{t}</span>。<b>公司价值 ＝ 股息的现值</b>：<span class='mj'>V_{t}=D_{t}+\\frac{D_{t+1}}{1+r_{t}}</span>。",
    plain="企业赚了钱不算自己的，得交回给老板——也就是家庭。今年的股息是「卖的钱减去工资」。明年的股息还要多两项：卖掉旧机器的残值（加），还银行的贷款（减）。企业的「价值」就是把这两笔钱按利率折回今天。",
    lr=[
        dict(name="第 t+1 期股息：四个加项、一个减项",
             lhs="D_{t+1}",
             lhs_t="<b>明天分给家庭的钱</b>",
             rhs="\\underbrace{Y_{t+1}-w_{t+1}N_{t+1}}_{\\text{operating profit}}+\\underbrace{(1-\\delta)K_{t+1}}_{\\text{scrap value}}-\\underbrace{(1+r_{t})B^{I}_{t}}_{\\text{loan repayment}}",
             rhs_t="<b>经营利润 ＋ 资本残值 － 还本付息</b>",
             why="<b>四项各有出处，一个都不能少</b>：<b>① <span class='mj'>Y-wN</span> 是「卖货减去工资」，即经营利润</b>；<b>② <span class='mj'>+(1-\\delta)K_{t+1}</span> 是「期末还剩的机器」——因为企业拥有资本，残值也是它的现金流入</b>（<b>课件用大括号专门标了「remaining capital」</b>）；<b>③ <span class='mj'>-(1+r_{t})B^{I}_{t}</span> 是「还本付息」</b>（<b>课件标了「loan repayment」</b>）。<b>为什么第 <span class='mj'>t</span> 期没有后两项？</b>因为<b>第 <span class='mj'>t</span> 期是「期初」，旧资本与旧债务都已经处理完了</b>——<b>这是两期模型的记账惯例。</b>",
             why_t="四项各自是什么"),
        dict(name="公司价值：股息的现值",
             lhs="V_{t}",
             lhs_t="<b>企业今天值多少</b>",
             rhs="D_{t}+\\frac{D_{t+1}}{1+r_{t}}",
             rhs_t="<b>两期股息的折现值</b>",
             why="<b>这就是「企业的目标函数」</b>。<b>为什么不是最大化当期利润 <span class='mj'>D_{t}</span>？</b>因为<b>「少分一点、多买机器」可以抬高 <span class='mj'>D_{t+1}</span></b>。<b>只看当期利润，企业会永远不投资。</b><b>用 <span class='mj'>V_{t}</span> 做目标，投资与分红就有一个统一的尺度</b>——<b>折现率正是家庭的时间偏好（<span class='mj'>r_{t}</span>），所以「企业最大化 <span class='mj'>V</span>」与「家庭最大化效用」是一致的。</b>",
             why_t="为什么用现值而不是当期利润"),
    ],
    note=(
        "这一页最重要的<b>不是公式，而是「所有权」这件事</b>：<br><br>"
        "<b>① 为什么「企业归家庭所有」很重要？</b><b>因为它让整个模型闭合</b>：<b>家庭的收入 ＝ 工资 <span class='mj'>wN</span> ＋ 股息 <span class='mj'>D</span></b>，而<b><span class='mj'>D</span> 又等于 <span class='mj'>Y-wN</span></b>。<b>两者相加正好是 <span class='mj'>Y</span></b>：<br>"
        "<b><span class='mj'>w_{t}N_{t}+D_{t}=w_{t}N_{t}+(Y_{t}-w_{t}N_{t})=Y_{t}</span></b>。<br>"
        "<b>所以「家庭拿到了全部产出」——这就是商品市场出清 <span class='mj'>Y=C+I</span> 的微观来源。</b><b>如果企业不归家庭所有，<span class='mj'>D</span> 就「消失」了，<span class='mj'>Y=C+I</span> 就对不上。</b><br><br>"
        "<b>② 为什么第 <span class='mj'>t+1</span> 期要加回残值 <span class='mj'>(1-\\delta)K_{t+1}</span>？</b><b>这是最容易被漏掉的一项。</b><b>直觉：最后一期结束了，机器要「变现」</b>——<b>卖掉、或者拆了卖废铁，这笔钱归股东</b>。<b>如果漏掉它，企业会「过度投资」：反正最后一期机器都白扔，那不如少买点。</b><br><br>"
        "<b>③ 为什么股息里没有「利息收入」？</b>因为<b>企业只借不存</b>（第 4 页的假设）。<b>它只有利息支出 <span class='mj'>(1+r)B^{I}</span>，没有利息收入。</b>"
    ),
    dec=[
        ("<span class='mj'>D_{t}</span>", "股息", "<b>企业交给家庭的钱</b>。<b>它等于「经营利润」</b>。<b>在 CRS ＋ 完全竞争下，它正好等于资本收入 <span class='mj'>\\mathrm{MPK}\\cdot K</span></b>（欧拉定理）。"),
        ("remaining capital", "剩余资本（残值）", "<b><span class='mj'>(1-\\delta)K_{t+1}</span></b>。<b>最后一期「清算」的现金流入</b>。<b>漏掉它 = 让企业免费扔掉机器 = 投资激励全错。</b>"),
        ("loan repayment", "还本付息", "<b><span class='mj'>(1+r_{t})B^{I}_{t}</span></b>。<b>注意是「本＋息」</b>，<b>不是只还利息</b>——<b>因为借款是「一次性还清」的（两期模型没有分期）。</b>"),
        ("PDV", "现值（present discounted value）", "<b>把未来的钱按 <span class='mj'>1/(1+r)</span> 折回今天</b>。<b>折现率 <span class='mj'>r</span> 就是「今天一块钱值多少明天的钱」的价格。</b>"),
        ("企业目标", "maximize <span class='mj'>V_{t}</span>", "<b>不是 max <span class='mj'>D_{t}</span></b>。<b>这一句决定了投资方程长什么样</b>——<b>第 6、7 页全部由它推出。</b>"),
    ],
    tip="<b>用「一张现金流量表」记这一页</b>：<b>流入 = 卖货 <span class='mj'>Y</span> ＋ 卖旧机器 <span class='mj'>(1-\\delta)K</span>；流出 = 工资 <span class='mj'>wN</span> ＋ 还贷 <span class='mj'>(1+r)B^{I}</span>；差额 = 股息 <span class='mj'>D</span>。</b><b>四行一列，公式自然出来，不用背。</b>",
    warn="<b>三个高频错误</b>：<b>① 漏掉残值 <span class='mj'>(1-\\delta)K_{t+1}</span></b>（最常见）；<b>② 把还贷写成 <span class='mj'>r B^{I}</span></b>（那是只付利息，两期模型是<b>还本付息</b>）；<b>③ 说「企业最大化利润」</b>——<b>是最大化 <span class='mj'>V_{t}</span>（现值）</b>，<b>这两者在多期里不等价。</b>"
)


# ==================== ③ 企业最优化：三个一阶条件 ====================

add(6,
    kp="企业选 <span class='mj'>N_{t},N_{t+1},K_{t+1}</span>（等价于选 <span class='mj'>I_{t}</span>）<b>最大化 <span class='mj'>V_{t}</span></b>，<b>把 <span class='mj'>r_{t},w_{t},w_{t+1},K_{t}</span> 当作给定</b>。约束有三条：资本积累、两期股息定义。",
    plain="企业面对的问题很具体：今年雇多少人、明年雇多少人、明年要多少机器。它不能改今天有多少机器，也不能改工资和利率——只能在这些条件下选一个最赚钱的组合。",
    note=(
        "把这个问题<b>逐项拆开</b>，会看到它其实很「干净」：<br><br>"
        "<b>① 决策变量只有三个：<span class='mj'>N_{t},N_{t+1},K_{t+1}</span>。</b><br>"
        "· <b>为什么没有 <span class='mj'>K_{t}</span>？</b>因为它是 <b>predetermined</b>——<b>今天已经在那儿了</b>。<br>"
        "· <b>为什么没有 <span class='mj'>I_{t}</span>？</b>因为<b>它被资本积累方程钉死了</b>：<span class='mj'>I_{t}=K_{t+1}-(1-\\delta)K_{t}</span>。<b>选 <span class='mj'>K_{t+1}</span> 就等于选 <span class='mj'>I_{t}</span></b>——课件专门写了（or equivalently <span class='mj'>K_{t+1}</span>）。<b>这句话很重要：<b>投资不是独立变量，是「资本存量的变化」</b>。</b><br><br>"
        "<b>② 「给定」的东西里有 <span class='mj'>K_{t}</span>，没有 <span class='mj'>A_{t+1}</span>？</b><b>其实 <span class='mj'>A_{t+1}</span> 也在函数里</b>，课件只列了 <span class='mj'>r_{t},w_{t},K_{t}</span>，<b>但 <span class='mj'>D_{t+1}</span> 里含 <span class='mj'>A_{t+1}</span></b>。<b>它是外生参数（企业知道它，但不决定它）</b>——<b>这一点在第 10 页会变成「投资需求依赖于 <span class='mj'>A_{t+1}</span>」。</b><br><br>"
        "<b>③ 为什么把 <span class='mj'>D_{t}</span> 与 <span class='mj'>D_{t+1}</span> 都代进去，而不先化简？</b><b>因为要看清「哪个变量影响哪一项」</b>：<b><span class='mj'>N_{t}</span> 只进 <span class='mj'>D_{t}</span></b>；<b><span class='mj'>N_{t+1}</span> 与 <span class='mj'>K_{t+1}</span> 只进 <span class='mj'>D_{t+1}</span></b>。<b>所以三个一阶条件可以「一个变量一个」地解出来</b>——<b>这是为什么第 7 页那三个条件那么干净。</b>"
    ),
    dec=[
        ("决策变量", "choice variables", "<b><span class='mj'>N_{t},N_{t+1},K_{t+1}</span></b>。<b>三个</b>，<b>对应三个一阶条件</b>。<b>数量对得上，说明没有遗漏。</b>"),
        ("给定", "taking as given", "<b><span class='mj'>r_{t},w_{t},w_{t+1},K_{t},A_{t},A_{t+1}</span></b>。<b>企业是「价格接受者」</b>——<b>它不能影响工资和利率</b>。<b>这是完全竞争的假设。</b>"),
        ("等价", "or equivalently", "<b>选 <span class='mj'>K_{t+1}</span> ＝ 选 <span class='mj'>I_{t}</span></b>。<b>因为 <span class='mj'>I_{t}=K_{t+1}-(1-\\delta)K_{t}</span> 是一个「一一对应」</b>。<b>这句话让「投资需求」可以写成「资本需求」。</b>"),
        ("<span class='mj'>s.t.</span>", "subject to（受约束于）", "<b>三条约束</b>：一条资本积累 ＋ 两条股息定义。<b>它们的作用是「消掉中间变量」</b>——<b>把 <span class='mj'>I</span> 与 <span class='mj'>D</span> 都换成 <span class='mj'>N</span> 与 <span class='mj'>K</span>。</b>"),
    ],
    tip="<b>做这类「多期最优化」的题，先把目标函数「摊平成只含决策变量」</b>：<b>把 <span class='mj'>D_{t},D_{t+1},I_{t}</span> 全部代掉，只剩 <span class='mj'>N_{t},N_{t+1},K_{t+1}</span>。</b><b>摊平之后，每个变量只出现在一项里，求导就变成「一项一项来」，几乎不会错。</b>",
    warn="<b>别把 <span class='mj'>K_{t+1}</span> 和 <span class='mj'>I_{t}</span> 都当决策变量</b>——<b>那会多出一个方程，而且两个方程互相矛盾。</b><b>另一个坑：把 <span class='mj'>\\delta</span> 的残值忘在目标函数外面</b>（<b>它必须进 <span class='mj'>D_{t+1}</span>，不然投资的一阶条件会算错 <span class='mj'>\\delta</span> 那一项</b>）。"
)

add(7,
    kp="<b>三个一阶条件</b>：<span class='mj'>w_{t}=A_{t}F_{N}(K_{t},N_{t})</span>、<span class='mj'>w_{t+1}=A_{t+1}F_{N}(K_{t+1},N_{t+1})</span>、<span class='mj'>1+r_{t}=A_{t+1}F_{K}(K_{t+1},N_{t+1})+1-\\delta</span>。<b>最后一条可写成 <span class='mj'>r_{t}=\\mathrm{MPK}_{t+1}-\\delta</span></b>。<b>直觉都是「边际成本 ＝ 边际收益」</b>。",
    plain="三个条件其实是三句大白话：① 雇最后一个人带来的产出，正好等于他的工资；② 明天雇人也是这个道理；③ 借钱买机器的总成本（1 加利率），正好等于机器明年带来的总回报（多产的货加上剩下的机器）。",
    lr=[
        dict(name="劳动（今天）：雇最后一个人的账",
             lhs="w_{t}",
             lhs_t="<b>多雇一个人的成本</b>（实际工资）",
             rhs="A_{t}F_{N}(K_{t},N_{t})",
             rhs_t="<b>多雇一个人的产出</b>（劳动的边际产品 <span class='mj'>\\mathrm{MPN}_{t}</span>）",
             why="<b>多雇一个人：多付 <span class='mj'>w_{t}</span>，多产 <span class='mj'>A_{t}F_{N}</span>。</b><b>只要前者小于后者，企业就一直雇下去</b>；<b>因为 <span class='mj'>F_{NN}&lt;0</span>，<span class='mj'>\\mathrm{MPN}</span> 会随 <span class='mj'>N</span> 递减，最终追平 <span class='mj'>w</span></b>——<b>这就是「为什么均衡存在且唯一」。</b><b>注意左边是「成本」、右边是「收益」</b>，<b>和通常「左边收益右边成本」的习惯相反，读的时候留意。</b>",
             why_t="为什么两边相等"),
        dict(name="投资：买机器的跨期账",
             lhs="1+r_{t}",
             lhs_t="<b>借一块钱的总成本</b>（本金 1 ＋ 利息 <span class='mj'>r</span>）",
             rhs="A_{t+1}F_{K}(K_{t+1},N_{t+1})+1-\\delta",
             rhs_t="<b>买一单位资本的总回报</b>（边际产品 ＋ 未折旧残值）",
             why="<b>两边都按「明年的钱」计价</b>：<b>左边是「明年要还的」，右边是「明年能收回的」</b>。<b>右边两项的来源：① <span class='mj'>A_{t+1}F_{K}</span> ＝ 多一台机器多产的货（<span class='mj'>\\mathrm{MPK}</span>）；② <span class='mj'>1-\\delta</span> ＝ 这台机器明年还剩多少（残值）</b>。<b>两边同时减 1，就得到 <span class='mj'>r_{t}=\\mathrm{MPK}_{t+1}-\\delta</span></b>——<b>「利率 ＝ 资本的净回报」，这是全书最常用的一个式子。</b>",
             why_t="为什么两边都是「总」回报"),
    ],
    note=(
        "这一页的<b>信息密度最高</b>。三个要点：<br><br>"
        "<b>① 「Intuition: MC = MB」——但注意谁是 MC 谁是 MB。</b><br>"
        "· <b>劳动条件里：<span class='mj'>w</span> 是 MC，<span class='mj'>\\mathrm{MPN}</span> 是 MB。</b><br>"
        "· <b>投资条件里：<span class='mj'>1+r</span> 是 MC，<span class='mj'>\\mathrm{MPK}+1-\\delta</span> 是 MB。</b><br>"
        "<b>统一成一句话：<b>「多要一单位投入，它的价格 ＝ 它带来的边际产品（加上残值）」</b>。</b><b>这一个句式能推出全部三个条件，不用背。</b><br><br>"
        "<b>② 为什么工资条件「与 Solow 完全相同」？</b><b>因为 Solow 里也有 <span class='mj'>w=\\mathrm{MPN}</span></b>（<b>劳动市场完全竞争、企业最大化利润</b>）。<b>那本讲的「新东西」是什么？</b><b>是第二条和第三条</b>：<b>Solow 里没有「投资的一阶条件」，因为储蓄率是外生的</b>。<b>所以看到「same as Solow」这句，要知道它在说「旧的部分没变，新的部分在后面」。</b><br><br>"
        "<b>③ <span class='mj'>r_{t}=\\mathrm{MPK}_{t+1}-\\delta</span> 的三个读法</b>：<br>"
        "· <b>读法一（企业视角）</b>：<b>资本的净回报必须等于利率，否则企业会无限投（或完全不投）。</b><br>"
        "· <b>读法二（市场视角）</b>：<b>这是「投资需求曲线」的方程</b>——<b>给定 <span class='mj'>r</span>，它能反解出 <span class='mj'>K_{t+1}</span></b>（第 10 页）。<br>"
        "· <b>读法三（增长视角）</b>：<b>这就是 Solow 的「黄金律」条件的「市场版」</b>——<b>黄金律是「<span class='mj'>\\mathrm{MPK}=\\delta+n+g</span>」，这里是「<span class='mj'>\\mathrm{MPK}=\\delta+r</span>」</b>，<b>把 <span class='mj'>n+g</span> 换成 <span class='mj'>r</span></b>。<b>两者是同一个逻辑（资本的边际产品要补偿「等待的代价」与「磨损」）。</b>"
    ),
    dec=[
        ("<span class='mj'>F_{N}</span>", "劳动的边际产品（MPN）", "<b>多雇一个人多产的货</b>。<b>它随 <span class='mj'>N</span> 递减（<span class='mj'>F_{NN}&lt;0</span>）</b>——<b>这是劳动需求向下的原因。</b>"),
        ("<span class='mj'>F_{K}</span>", "资本的边际产品（MPK）", "<b>多一台机器多产的货</b>。<b>它随 <span class='mj'>K</span> 递减（<span class='mj'>F_{KK}&lt;0</span>）</b>——<b>这是投资需求向下的原因。</b>"),
        ("<span class='mj'>1+r_{t}</span>", "总利率（gross rate）", "<b>借一块、还 <span class='mj'>1+r</span></b>。<b>注意是「总」不是「净」</b>——<b>与右边的 <span class='mj'>+1-\\delta</span> 对称。</b><b>两边都减 1 才得到「净」的版本。</b>"),
        ("<span class='mj'>\\mathrm{MPK}-\\delta</span>", "资本的净回报", "<b>扣掉折旧后，一单位资本一年净赚多少</b>。<b>它必须等于 <span class='mj'>r</span></b>。<b>这是「无套利」条件。</b>"),
        ("<span class='mj'>N_{t+1}</span> 的条件", "明天的劳动需求", "<b>与今天形式完全一样，只是下标加一</b>。<b>这说明「劳动需求每一期都成立」，不是「只有今天成立」。</b>"),
        ("MC = MB", "边际成本 ＝ 边际收益", "<b>三个条件的统一说法</b>。<b>不要只记住字母，要能说出「哪边是成本、哪边是收益」。</b>"),
    ],
    tip="<b>面试／考试最常被问的一句</b>：<b>「为什么投资条件里是 <span class='mj'>1+r</span> 和 <span class='mj'>1-\\delta</span>，而不是 <span class='mj'>r</span> 和 <span class='mj'>\\delta</span>？」</b><b>标准答案</b>：<b>因为两边都按「明年的总金额」计价</b>——<b>借一块明年还 <span class='mj'>1+r</span>；买一单位资本明年收回「边际产品 ＋ 剩下的 <span class='mj'>1-\\delta</span>」</b>。<b>两边同时减 1，就是净值版本。</b><b>把「总／净」这个区分说清楚，答案就完整了。</b>",
    warn="<b>三个高频错误</b>：<b>① 把 <span class='mj'>r=\\mathrm{MPK}-\\delta</span> 写成 <span class='mj'>r=\\mathrm{MPK}</span></b>（漏折旧）；<b>② 在劳动条件里加了 <span class='mj'>\\beta</span></b>（<b>今天雇人是「同一期内」的决策，不折现</b>）；<b>③ 把 <span class='mj'>F_{K}</span> 当成「资本的产出」</b>（<b>它是「多一单位资本的产出」，即斜率</b>）。"
)

add(8,
    kp="<b>劳动需求函数</b>：<span class='mj'>w_{t}=A_{t}F_{N}(K_{t},N_{t})</span> 隐式地定义 <span class='mj'>N_{t}=N^{d}(w_{t}^{-},A_{t}^{+},K_{t}^{+})</span>。<b><span class='mj'>w\\uparrow</span> ⇒ 需要更高的 <span class='mj'>\\mathrm{MPN}</span> ⇒ 因为 <span class='mj'>F_{NN}&lt;0</span> ⇒ <span class='mj'>N\\downarrow</span></b>。",
    plain="工资越高，企业越舍不得多雇人。因为人多手杂、边际产出下滑，只有当工资也低时才划算。反过来，技术越好、机器越多，同样工资下企业愿意多雇人。",
    note=(
        "这一页只有<b>一个符号要推</b>，但推法值得学：<br><br>"
        "<b>① 为什么 <span class='mj'>w\\uparrow</span> 会让 <span class='mj'>N\\downarrow</span>？三步走</b>：<br>"
        "· <b>第一步（均衡被破坏）</b>：<span class='mj'>w</span> 上升后，原来的 <span class='mj'>N_{t}</span> 处出现 <span class='mj'>w&gt;AF_{N}</span>——<b>「雇人亏了」</b>。<br>"
        "· <b>第二步（要恢复等式）</b>：<b>必须让 <span class='mj'>F_{N}</span> 上升</b>，才能追上更高的 <span class='mj'>w</span>。<br>"
        "· <b>第三步（怎么让 <span class='mj'>F_{N}</span> 上升）</b>：<b>因为 <span class='mj'>F_{NN}&lt;0</span>，减少 <span class='mj'>N</span> 才能抬高 <span class='mj'>F_{N}</span>。</b><b>所以 <span class='mj'>N</span> 下降。</b><br><br>"
        "<b>这个「三步走」是全讲所有比较静态的模板</b>：<b>先看原均衡怎么被破坏 → 再看等式要求什么 → 最后看哪个变量能实现它。</b><b>答题时照这三步写，比直接说「因为边际递减」得分高得多。</b><br><br>"
        "<b>② 课件留了一个问题：「Can you work out the math and intuition for <span class='mj'>A_{t}</span> and <span class='mj'>K_{t}</span>?」——这就是作业题，答案必须会给</b>：<br>"
        "· <b><span class='mj'>A_{t}\\uparrow</span></b>：<b>同一 <span class='mj'>N</span> 下，<span class='mj'>A F_{N}</span> 上升</b> ⇒ <b>出现 <span class='mj'>AF_{N}&gt;w</span></b>（<b>「雇人赚了」</b>）⇒ <b>企业多雇人</b> ⇒ <b><span class='mj'>N\\uparrow</span></b>。<b>直觉：技术好，人多有用。</b><br>"
        "· <b><span class='mj'>K_{t}\\uparrow</span></b>：<b>因为 <span class='mj'>F_{KN}&gt;0</span>，同一 <span class='mj'>N</span> 下 <span class='mj'>F_{N}</span> 上升</b> ⇒ <b>同样 <span class='mj'>AF_{N}&gt;w</span></b> ⇒ <b><span class='mj'>N\\uparrow</span></b>。<b>直觉：机器多，工人好使。</b><br><br>"
        "<b>③ 严格说这两个符号怎么来？</b><b>对 <span class='mj'>w=AF_{N}(K,N)</span> 全微分</b>：<br>"
        "<b><span class='mj'>dw=A F_{NN}\\,dN+A F_{NK}\\,dK+F_{N}\\,dA</span></b>。<br>"
        "<b>令 <span class='mj'>dw=0</span>，解出 <span class='mj'>\\frac{\\partial N}{\\partial A}=-\\frac{F_{N}}{AF_{NN}}&gt;0</span></b>（<b>因为 <span class='mj'>F_{NN}&lt;0</span>，负负得正</b>）；<b><span class='mj'>\\frac{\\partial N}{\\partial K}=-\\frac{F_{NK}}{F_{NN}}&gt;0</span></b>（<b>因为 <span class='mj'>F_{NK}&gt;0,F_{NN}&lt;0</span></b>）。<b>两个符号都靠假设「买」来</b>——<b>这就是第 3 页那七条假设的用处。</b>"
    ),
    dec=[
        ("<span class='mj'>N^{d}(\\cdot)</span>", "劳动需求函数", "<b>企业「愿意雇多少」</b>。<b>它不是「需要多少」，而是「在给定价格下最优地要多少」</b>——<b>这个区别在多讲比较静态时很重要。</b>"),
        ("implicitly defines", "隐式定义", "<b>没有显式解</b>（除非给 <span class='mj'>F</span> 的具体形式）。<b>但有隐函数定理，函数存在且可微</b>——<b>所以可以画图、可以求符号。</b>"),
        ("<span class='mj'>w^{-}</span> 的负号", "需求法则", "<b>价格越高、需求越少</b>。<b>三个自变量里唯一带负号的</b>（另外两个是正号）。"),
        ("<span class='mj'>A_{t}^{+}</span>", "技术对劳动需求", "<b>正号</b>。<b>技术上升 ⇒ 劳动的边际产品上升 ⇒ 同一工资下多雇人。</b>"),
        ("<span class='mj'>K_{t}^{+}</span>", "资本对劳动需求", "<b>正号，且只靠 <span class='mj'>F_{KN}&gt;0</span></b>。<b>注意与投资需求里的负号对照</b>——<b>这是本讲最容易搞混的一对。</b>"),
    ],
    tip="<b>把「隐函数 ＋ 全微分」这条路练一遍</b>：<b>要问「某个外生变量上升，内生变量怎么变」，就把 FOC 全微分、让 <span class='mj'>dw=0</span>、解出偏导的符号。</b><b>这条路对劳动需求、投资需求、劳动供给三张图通用</b>——<b>学会一次，三张图都不用背。</b>",
    warn="<b>别说「工资上升企业雇不起人所以少雇」——那是「预算」直觉，不是这里的机制。</b><b>这里的机制是「边际产品必须追上工资」</b>。<b>另一个错误：把 <span class='mj'>K_{t}</span> 的符号记成负</b>（<b>负号是投资需求那边的，劳动需求这边是正号</b>）。"
)


# ==================== ④ 三条曲线与三张图 ====================

add(9,
    kp="<b>劳动需求曲线：纵轴 <span class='mj'>w_{t}</span>、横轴 <span class='mj'>N_{t}</span>，向下倾斜</b>。<b>沿曲线移动</b>＝工资变；<b>整条线移动</b>＝<span class='mj'>A_{t}</span> 或 <span class='mj'>K_{t}</span> 变，<b>方向都是「右上」（同一工资下雇更多）</b>。",
    plain="这张图就是把「工资越高、雇人越少」画出来。注意它跟普通的供需图一样：价格在纵轴、数量在横轴。所以「企业想多雇人」在图上表现为整条线往右推，而不是「沿着线往上走」。",
    fig=[
        dict(name="图：劳动需求函数 <span class='mj'>N_{t}=N^{d}(w_{t},A_{t},K_{t})</span>（纵轴工资、横轴劳动）",
             axes=[("横轴", "N_{t}", "<b>劳动投入（雇多少人／多少小时）</b>——<b>注意是「数量」</b>"),
                   ("纵轴", "w_{t}", "<b>实际工资</b>——<b>注意是「价格」</b>。与微观供需图同一套习惯：<b>价在纵、量在横</b>")],
             marks=[("黑色实线（<b>向下倾斜</b>）", "<b>原状的劳动需求</b>，标注 <span class='mj'>N_{t}=N^{d}(w_{t},A_{t},K_{t})</span>。<b>斜率来自 <span class='mj'>F_{NN}&lt;0</span></b>：<b>工资高 ⇒ 要更高的 <span class='mj'>MPN</span> 才划算 ⇒ 少雇人</b>"),
                    ("淡蓝色线（在黑线<b>右上方</b>，与原线平行）", "<b>冲击后的劳动需求</b>。<b>平行位移说明「斜率没变、位置变了」</b>——<b>技术或资本只改变「每个工资下雇多少」，不改变「工资涨一块少雇几个」</b>"),
                    ("淡蓝色<b>水平箭头</b>（黑线 → 蓝线）", "<b>位移方向</b>。<b>本质是「右移」</b>（<b>同一工资下 <span class='mj'>N</span> 更大</b>）；<b>画成「右上」只是因为工资在纵轴、而两条线都下斜</b>。<b>别被视觉上的「向上」骗了——它不是「工资变高」，是「同样工资下雇更多」</b>"),
                    ("淡蓝色小字 <span class='mj'>\\uparrow A_{t}</span> or <span class='mj'>\\uparrow K_{t}</span>", "<b>两个触发条件，都使线右移</b>：<b><span class='mj'>A_{t}\\uparrow</span>（技术更好）</b>、<b><span class='mj'>K_{t}\\uparrow</span>（机器更多，靠 <span class='mj'>F_{KN}&gt;0</span>）</b>。<b>两个都是「劳动的边际产品上升」</b>")],
             read="<b>读图三步：① 先分辨「沿着线走」还是「线在动」</b>——<b>只有 <span class='mj'>w</span> 变 ⇒ 沿曲线；<span class='mj'>A</span> 或 <span class='mj'>K</span> 变 ⇒ 整条线动</b>。<b>② 看线往哪边动</b>——<b>右 ＝ 同一工资下雇更多</b>。<b>③ 回到方程核对</b>——<b>把新 <span class='mj'>A</span> 或 <span class='mj'>K</span> 代进 <span class='mj'>w=AF_{N}</span>，看 <span class='mj'>N</span> 该变大还是变小</b>。",
             exam="必考三问：<b>① 为什么向下斜？</b>答：<span class='mj'>w\\uparrow</span> ⇒ 需要更高的 <span class='mj'>F_{N}</span> 才恢复 <span class='mj'>w=AF_{N}</span> ⇒ 因 <span class='mj'>F_{NN}&lt;0</span> 必须 <span class='mj'>N\\downarrow</span>。<b>② 技术进步是「沿曲线」还是「移动曲线」？</b>答：<b>移动曲线</b>（右移），因为 <span class='mj'>A</span> 不在纵轴上。<b>③ 资本存量增加会怎样？</b>答：<b>右移</b>，因为 <span class='mj'>F_{KN}&gt;0</span>。<b>这是本题唯一的「陷阱项」——很多人会答「左移」。</b>"),
    ],
    note=(
        "这张图有三个地方要特别留意：<br><br>"
        "<b>① 为什么把 <span class='mj'>w</span> 放纵轴、<span class='mj'>N</span> 放横轴？</b><b>因为要把它当「需求曲线」用</b>——<b>需求曲线永远是「价格在纵、数量在横」</b>。<b>这样「工资变化」就是「沿曲线移动」，「其他变量变化」就是「整条线移动」</b>，<b>与微观的价格／非价格区分一致。</b><b>如果反过来放，「沿曲线」和「移曲线」在视觉上会混。</b><br><br>"
        "<b>② 「右上方」其实是「右移」——这一点极易误读。</b><b>判断方法只有一个：看「同一工资下 <span class='mj'>N</span> 变多还是变少」。</b><b>在图上取一条水平线（固定 <span class='mj'>w</span>），看它与黑线、蓝线的交点</b>——<b>蓝线的交点更靠右 ⇒ 右移 ⇒ 同一工资下雇更多</b>。<b>「往上」只是因为在纵轴上位置更高，不代表「工资变高」</b>——<b>工资是坐标，不是被移动的对象。</b><br><br>"
        "<b>③ 为什么两条线「平行」？</b><b>因为技术 <span class='mj'>A_{t}</span> 是 Hicks 中性的（乘在 <span class='mj'>F</span> 外面）</b>——<b>它按同一比例抬高所有 <span class='mj'>N</span> 上的 <span class='mj'>\\mathrm{MPN}</span></b>，<b>所以「斜率」（<span class='mj'>F_{NN}</span> 决定的弯曲程度）不变</b>。<b>如果换成「劳动增强型」技术进步（<span class='mj'>Y=F(K,AN)</span>），曲线的形状会变</b>——<b>这是本题的一个进阶答点。</b>"
    ),
    dec=[
        ("<span class='mj'>N^{d}</span> 上的负号", "需求法则", "<b>价格越高、需求越少</b>。<b>这是「沿曲线移动」的方向。</b>"),
        ("<span class='mj'>A_{t}</span> 的冲击", "技术冲击", "<b>右移</b>。<b>直觉：技术进步 ⇒ 同样的人能产更多 ⇒ 企业想多雇人</b>。<b>注意它<b>不是</b>「沿曲线」。</b>"),
        ("<span class='mj'>K_{t}</span> 的冲击", "资本存量冲击", "<b>右移，靠 <span class='mj'>F_{KN}&gt;0</span></b>。<b>注意 <b>与投资需求里 <span class='mj'>K_{t}</span> 的负号相反</b>。</b>"),
        ("平行位移", "parallel shift", "<b>斜率不变、位置变</b>。<b>因为 <span class='mj'>A</span> 是 Hicks 中性的</b>。<b>如果曲线不平行，说明技术进步改变了「边际递减的速度」。</b>"),
        ("沿曲线 vs 移曲线", "movement along vs shift", "<b>本图最常考的一句</b>：<b>只有纵轴变量变才「沿曲线」；其余变量变都是「移曲线」。</b>"),
    ],
    tip="<b>把这张图和微观的「劳动需求」对照记</b>：<b>形状一样（下斜）、理由不同</b>。<b>微观说「因为边际产出递减」；这里说「因为 <span class='mj'>F_{NN}&lt;0</span>，且企业按 <span class='mj'>w=AF_{N}</span> 定价」</b>——<b>是同一件事的「微观版」与「宏观版」。</b><b>答题时可以两边都提一句，显得有层次。</b>",
    warn="<b>三个高频错误</b>：<b>① 说「技术进步使劳动需求沿曲线向上移动」</b>（错，是<b>右移</b>）；<b>② 说「资本增加使劳动需求左移」</b>（错，<b>右移</b>，<span class='mj'>F_{KN}&gt;0</span>）；<b>③ 把横纵轴弄反</b>（<b>横轴是 <span class='mj'>N</span>、纵轴是 <span class='mj'>w</span></b>，说反了整道题的符号都会错）。"
)

add(10,
    kp="<b>投资需求函数有两层</b>：先由 <span class='mj'>r_{t}+\\delta=A_{t+1}F_{K}(K_{t+1},N_{t+1})</span> 定出目标资本 <span class='mj'>K_{t+1}=K^{d}(r_{t}^{-},A_{t+1}^{+})</span>；再由 <span class='mj'>I_{t}=K_{t+1}-(1-\\delta)K_{t}</span> 得 <b><span class='mj'>I_{t}=I^{d}(r_{t}^{-},A_{t+1}^{+},K_{t}^{-})</span></b>。<b><span class='mj'>K_{t}</span> 是负号！</b>",
    plain="企业先想「明年我要多少机器」，这取决于利率（借钱贵不贵）和明年的技术（机器值不值钱）。想好了目标，再减去手里还剩的旧机器，差额就是今年要新买的。所以旧机器越多，今年买得越少——这就是那个负号。",
    lr=[
        dict(name="第一层：目标资本存量",
             lhs="r_{t}+\\delta",
             lhs_t="<b>「用资本」的总成本</b>（利息 ＋ 折旧）",
             rhs="A_{t+1}F_{K}(K_{t+1},N_{t+1})",
             rhs_t="<b>资本的边际产品</b>（<span class='mj'>\\mathrm{MPK}_{t+1}</span>）",
             why="<b>这是第 7 页那个条件移项得到的</b>。<b>读法：一单位资本一年要「花掉」<span class='mj'>r</span>（利息）与 <span class='mj'>\\delta</span>（磨损），<b>所以它的边际产品必须至少补偿这两项</b>。</b><b>这个式子的用处是「反解」</b>：<b>给定 <span class='mj'>r</span> 与 <span class='mj'>A_{t+1}</span>，唯一确定一个 <span class='mj'>K_{t+1}</span></b>——<b>因为 <span class='mj'>F_{KK}&lt;0</span>，左边给定、右边单调，解唯一。</b>",
             why_t="为什么能反解出资本"),
        dict(name="第二层：从「目标资本」到「投资」",
             lhs="I_{t}",
             lhs_t="<b>今年要新买的机器</b>（流量）",
             rhs="K_{t+1}-(1-\\delta)K_{t}",
             rhs_t="<b>目标资本 － 手里还剩的旧资本</b>",
             why="<b>这就是 <span class='mj'>K_{t}</span> 带负号的唯一原因</b>：<b>它出现在减号后面</b>。<b>直觉：目标是 100 台，手里还有 90 台（未折旧部分），那只用买 10 台</b>；<b>手里还有 99 台，就只用买 1 台</b>。<b>所以「存量越多、流量越少」——这不是「资本抑制投资」这种奇怪的经济学，而只是记账。</b>",
             why_t="负号从哪来"),
    ],
    note=(
        "这一页是<b>本讲最容易考、也最容易错的一页</b>。三个要点：<br><br>"
        "<b>① 为什么要分成「两层」？</b><b>因为 <span class='mj'>r</span> 只影响「目标」，<span class='mj'>K_{t}</span> 只影响「差额」。</b><b>把两层分开，符号就不会混</b>：<br>"
        "· <b><span class='mj'>r_{t}\\uparrow</span></b> ⇒ <b>目标 <span class='mj'>K_{t+1}\\downarrow</span></b>（<b>借钱贵，少买机器</b>）⇒ <b><span class='mj'>I_{t}\\downarrow</span></b>。<b>负号。</b><br>"
        "· <b><span class='mj'>A_{t+1}\\uparrow</span></b> ⇒ <b><span class='mj'>\\mathrm{MPK}</span> 上升</b> ⇒ <b>目标 <span class='mj'>K_{t+1}\\uparrow</span></b> ⇒ <b><span class='mj'>I_{t}\\uparrow</span></b>。<b>正号。</b><br>"
        "· <b><span class='mj'>K_{t}\\uparrow</span></b> ⇒ <b>目标不变，但旧的多</b> ⇒ <b><span class='mj'>I_{t}\\downarrow</span></b>。<b>负号。</b><br><br>"
        "<b>② 为什么投资需求依赖 <span class='mj'>A_{t+1}</span> 而不是 <span class='mj'>A_{t}</span>？</b><b>因为投资是「为明天买机器」</b>——<b>今天买的机器明天才产出</b>，<b>所以决定它值不值的是明天的技术</b>。<b>这是「前瞻性」在投资上的体现</b>，<b>也是为什么「预期」在宏观里那么重要</b>。<b>答题时写「投资看未来」比写「投资看 <span class='mj'>A_{t+1}</span>」更有分。</b><br><br>"
        "<b>③ 注意这里用的是 <span class='mj'>K_{t+1}</span> 作为「目标」，而 <span class='mj'>N_{t+1}</span> 出现在 <span class='mj'>F_{K}</span> 里</b>——<b>这意味着「投资决策」和「明天的雇人决策」是联立的</b>。<b>严格说要一起解</b>；<b>但在部分均衡里，通常把 <span class='mj'>N_{t+1}</span> 当给定，只看 <span class='mj'>K_{t+1}</span> 怎么随 <span class='mj'>r</span> 变。</b><b>课件这里做了「部分均衡」的简化，第 23 页的一般均衡里两者同时解出来。</b>"
    ),
    dec=[
        ("<span class='mj'>K^{d}(\\cdot)</span>", "资本需求函数", "<b>「目标资本」</b>。<b>注意它是「存量」的需求</b>——<b>与「投资」这个流量需求差一个 <span class='mj'>(1-\\delta)K_{t}</span></b>。"),
        ("<span class='mj'>I^{d}(\\cdot)</span>", "投资需求函数", "<b>「今年新买多少」</b>。<b>它才是画在图上的那条线</b>（第 11 页）。"),
        ("<span class='mj'>r_{t}^{-}</span>", "利率的负号", "<b>「用资本」的成本上升 ⇒ 目标资本下降 ⇒ 投资下降</b>。<b>投资需求向下的原因。</b>"),
        ("<span class='mj'>A_{t+1}^{+}</span>", "未来技术的正号", "<b>未来更能产 ⇒ 机器更值 ⇒ 多买</b>。<b>注意下标是 <span class='mj'>t+1</span></b>——<b>本页最容易写错的下标。</b>"),
        ("<span class='mj'>K_{t}^{-}</span>", "现有资本的负号", "<b>本页的「陷阱符号」</b>。<b>与劳动需求里 <span class='mj'>K_{t}</span> 的正号正好相反</b>。<b>来源：<span class='mj'>I=K_{t+1}-(1-\\delta)K_{t}</span> 的减号。</b>"),
        ("<span class='mj'>r+\\delta</span>", "资本的使用成本", "<b>利息 ＋ 折旧</b>。<b>有时叫「user cost of capital」</b>——<b>这个名字一旦记住，<span class='mj'>\\mathrm{MPK}=r+\\delta</span> 就不用背了。</b>"),
    ],
    tip="<b>「两层法」在考试里非常吃香</b>：<b>先写「目标资本由 <span class='mj'>\\mathrm{MPK}=r+\\delta</span> 定」，再写「投资 ＝ 目标 － 剩余」</b>。<b>两行字把三个符号全部说清</b>（<span class='mj'>r</span> 负、<span class='mj'>A'</span> 正、<span class='mj'>K</span> 负），<b>而且不会把「资本需求」与「投资需求」混淆。</b><b>如果只写最终那个 <span class='mj'>I^{d}(\\cdot)</span>，很容易漏掉 <span class='mj'>K_{t}</span> 这一项。</b>",
    warn="<b>四个高频错误</b>：<b>① 把 <span class='mj'>K_{t}</span> 写成正号</b>（<b>最常错，一定要与劳动需求对照记</b>）；<b>② 把 <span class='mj'>A_{t+1}</span> 写成 <span class='mj'>A_{t}</span></b>（<b>投资看未来</b>）；<b>③ 混淆 <span class='mj'>K^{d}</span> 与 <span class='mj'>I^{d}</span></b>（<b>一个是存量目标，一个是流量需求</b>）；<b>④ 忘记 <span class='mj'>\\delta</span></b>（<b>写成 <span class='mj'>r=A'F_{K}</span>——应该是 <span class='mj'>r+\\delta=\\mathrm{MPK}</span></b>）。"
)

add(11,
    kp="<b>投资需求曲线：纵轴 <span class='mj'>r_{t}</span>、横轴 <span class='mj'>I_{t}</span>，向下倾斜</b>。<b>右移的两个触发</b>：<b><span class='mj'>A_{t+1}\\uparrow</span></b>（<b>机器更值</b>）与 <b><span class='mj'>K_{t}\\downarrow</span></b>（<b>旧机器少、需要多买</b>）。<b>注意两个方向都是「右」。</b>",
    plain="这张图跟劳动需求那张是「同一个模子」：价格在纵轴（这里的价格是利率）、数量在横轴。利率越高，企业越不想借钱买机器。而如果明年技术变好，或者手里的旧机器变少，同样的利率下企业都想多买——线往右推。",
    fig=[
        dict(name="图：投资需求函数 <span class='mj'>I_{t}=I^{d}(r_{t},A_{t+1},K_{t})</span>（纵轴利率、横轴投资）",
             axes=[("横轴", "I_{t}", "<b>投资（新买的机器）</b>——<b>是流量</b>"),
                   ("纵轴", "r_{t}", "<b>实际利率</b>——<b>借钱的价格</b>。<b>注意是 <span class='mj'>r</span> 不是 <span class='mj'>r+\\delta</span></b>：<b><span class='mj'>\\delta</span> 被并进曲线位置里了</b>")],
             marks=[("黑色实线（<b>向下倾斜</b>）", "<b>原状的投资需求</b>，标注 <span class='mj'>I_{t}=I^{d}(r_{t},A_{t+1},K_{t})</span>。<b>斜率来自 <span class='mj'>F_{KK}&lt;0</span></b>：<b>利率高 ⇒ 目标资本少 ⇒ 投资少</b>"),
                    ("淡蓝色线（在黑线<b>右上方</b>，与原线平行）", "<b>冲击后的投资需求</b>。<b>平行位移＝斜率不变</b>——<b><span class='mj'>A_{t+1}</span> 与 <span class='mj'>K_{t}</span> 只改位置、不改「利率敏感度」</b>"),
                    ("淡蓝色<b>水平箭头</b>（黑线 → 蓝线）", "<b>位移方向：右移</b>（<b>同一利率下投资更多</b>）。<b>与第 9 页同一个道理</b>：<b>别把「右上」读成「利率上升」</b>"),
                    ("淡蓝色小字 <span class='mj'>\\uparrow A_{t+1}</span> or <span class='mj'>\\downarrow K_{t}</span>", "<b>注意这两个箭头的方向写反了！</b><b><span class='mj'>A_{t+1}</span> 是「上升」、<span class='mj'>K_{t}</span> 是「下降」</b>。<b>与第 9 页的「<span class='mj'>\\uparrow A_{t}</span> or <span class='mj'>\\uparrow K_{t}</span>」只差一个符号</b>——<b>这是本讲最容易看漏的一处</b>")],
             read="<b>读图三步：① 看纵轴是什么价格</b>——<b><span class='mj'>r</span>：利率变则沿曲线，<span class='mj'>A'</span> 或 <span class='mj'>K</span> 变则移曲线</b>。<b>② 看箭头上的符号</b>——<b><span class='mj'>\\uparrow A_{t+1}</span> 右移；<span class='mj'>\\downarrow K_{t}</span> 也右移</b>。<b>两个不同的方向（一升一降）导致同一个结果（右移），因为它们在公式里的符号相反</b>。<b>③ 回到公式核对</b>——<b>看 <span class='mj'>I^{d}</span> 的三个符号</b>。",
             exam="必考三问：<b>① 为什么向下斜？</b>答：<span class='mj'>r\\uparrow</span> ⇒ 资本使用成本上升 ⇒ <span class='mj'>\\mathrm{MPK}=r+\\delta</span> 要求更高的 <span class='mj'>\\mathrm{MPK}</span> ⇒ 因 <span class='mj'>F_{KK}&lt;0</span> 必须 <span class='mj'>K_{t+1}\\downarrow</span> ⇒ <span class='mj'>I\\downarrow</span>。<b>② 为什么 <span class='mj'>\\downarrow K_{t}</span> 使投资需求右移？</b>答：<b>目标资本不变、旧资本变少 ⇒ 差额（新投资）变大</b>。<b>③ 它与劳动需求图的区别是什么？</b>答：<b><span class='mj'>K_{t}</span> 的符号相反</b>——<b>劳动需求里 <span class='mj'>K_{t}</span> 是正号（<span class='mj'>F_{KN}&gt;0</span>）、投资需求里是负号（<span class='mj'>I=K'-（1-\\delta)K</span>）</b>。"),
    ],
    note=(
        "这张图最值得琢磨的是<b>那行小字</b>：<br><br>"
        "<b>① 为什么 <span class='mj'>A_{t+1}</span> 要「升」、<span class='mj'>K_{t}</span> 要「降」，才能得到同一个右移？</b><br>"
        "<b>因为它们在 <span class='mj'>I^{d}</span> 里的符号相反</b>：<b><span class='mj'>I^{d}(r^{-},A_{t+1}^{+},K_{t}^{-})</span></b>。<b>所以「使投资增加」的两条路是</b>：<b>让正号的变量上升（<span class='mj'>A_{t+1}\\uparrow</span>）</b> 或 <b>让负号的变量下降（<span class='mj'>K_{t}\\downarrow</span>）</b>。<b>这一行小字其实是「符号表」的图形版</b>——<b>能读懂它，就说明三个符号都记住了。</b><br><br>"
        "<b>② 为什么 <span class='mj'>K_{t}\\downarrow</span> 会「增加投资」？这不违反直觉吗？</b><b>不违反，但要小心表述</b>：<b>这不是「资本少所以经济更好」，而是「要维持同样的目标资本，旧机器少了就得多买」</b>。<b>它是一个「重置投资」（replacement investment）效应。</b><b>战争摧毁资本后投资激增、就是这个道理。</b><b>答题时一定要说「给定目标资本 <span class='mj'>K_{t+1}</span>」——否则会被认为不懂「存量 vs 流量」。</b><br><br>"
        "<b>③ 这张图与第 9 页「长得一样」，那能不能只记一张？</b><b>不能。</b><b>两张图的「陷阱符号」不同</b>（<span class='mj'>K_{t}</span> 一正一负），<b>而且纵轴的「价格」不同</b>（<span class='mj'>w</span> 与 <span class='mj'>r</span>）。<b>考试最常见的题型就是「两个冲击分别使哪条线动、往哪动」</b>——<b>两张图必须各自记清。</b>"
    ),
    dec=[
        ("投资需求", "investment demand", "<b>「给定利率，企业想投多少」</b>。<b>它是可贷资金市场的「需求」侧</b>（第 22 页）。"),
        ("<span class='mj'>\\downarrow K_{t}</span>", "现有资本减少", "<b>右移</b>。<b>「重置投资」效应</b>。<b>灾难后投资上升，就是这个机制。</b>"),
        ("<span class='mj'>\\uparrow A_{t+1}</span>", "未来技术上升", "<b>右移</b>。<b>「机器更值钱」</b>。<b>注意下标是 <span class='mj'>t+1</span>：投资看未来。</b>"),
        ("平行位移", "parallel shift", "<b>斜率不变</b>。<b>因为 <span class='mj'>A</span> 是 Hicks 中性、<span class='mj'>K</span> 只进常数项</b>。<b>所以「利率敏感度」不变，只有「水平位置」变。</b>"),
        ("与第 9 页对照", "compare with labor demand", "<b>唯一的实质差别是 <span class='mj'>K_{t}</span> 的符号</b>。<b>其余结构（下斜、右移、平行）完全一样</b>——<b>所以可以「一套记法、两处套用」，但必须改那个符号。</b>"),
    ],
    tip="<b>把两张图并排画在一张纸上，只圈出三个差别</b>：<b>① 纵轴 <span class='mj'>w</span> vs <span class='mj'>r</span>；② 横轴 <span class='mj'>N</span> vs <span class='mj'>I</span>；③ <span class='mj'>K_{t}</span> 正号 vs 负号。</b><b>圈完这三个，两张图就都记住了</b>——<b>因为剩下的（下斜、右移、平行、怎么读）是同一套。</b>",
    warn="<b>三个高频错误</b>：<b>① 把 <span class='mj'>\\downarrow K_{t}</span> 说成左移</b>（错，<b>右移</b>）；<b>② 说「资本少所以经济差、投资少」</b>（<b>混淆了「存量水平」与「重置需求」</b>）；<b>③ 把纵轴写成 <span class='mj'>r+\\delta</span></b>（<b>纵轴是 <span class='mj'>r</span>；<span class='mj'>\\delta</span> 已并进曲线的位置</b>）。"
)


# ==================== ⑤ 家庭：效用与 GHH 偏好 ====================

add(12,
    kp="<b>代表性家庭的效用来自「消费」与「闲暇」</b>，闲暇 ＝ <span class='mj'>1-N</span>（<b>时间禀赋标准化为 1</b>）。<b>终生效用</b> <span class='mj'>U=u(C_{t},1-N_{t})+\\beta u(C_{t+1},1-N_{t+1})</span>。<b>四个符号假设</b>：<span class='mj'>u_{C}&gt;0,u_{L}&gt;0,u_{CC}&lt;0,u_{LL}&lt;0</span>。",
    plain="一个人一天有 24 小时（这里标准化成 1）。工作了就少了休息，休息了就少了工资。所以他的快乐来自两样东西：买的东西，和闲下来的时间。两样都「越多越好，但增幅越来越小」。",
    note=(
        "这一页看着简单，但<b>三个设置决定了后面全部结论</b>：<br><br>"
        "<b>① 为什么闲暇写成 <span class='mj'>1-N</span> 而不是一个新符号 <span class='mj'>L</span>？</b><b>因为「时间禀赋固定为 1」</b>——<b>这是一个「约束」而不是「偏好」</b>。<b>写成 <span class='mj'>1-N</span> 的好处是：<b>模型里只有 <span class='mj'>N</span> 一个决策变量</b>，<b>不用再额外加一条 <span class='mj'>N+L=1</span> 的约束。</b><b>如果写成两个变量，就要多一个乘子，多一组方程。</b><br><br>"
        "<b>② 为什么效用是「可加可分」的（<span class='mj'>u(C,1-N)</span> 而不是 <span class='mj'>u(C,N,C',N')</span>）？</b><b>因为要让「期内」与「跨期」两个决策分开</b>：<b>期内是「消费 vs 闲暇」，跨期是「今天 vs 明天」</b>。<b>这是本书所有模型的通用简化</b>（Topic 4 也是可加可分）。<b>代价是「消费与闲暇的边际替代率不随另一期变化」</b>——<b>这正好让劳动供给可以「逐期」决定。</b><br><br>"
        "<b>③ <span class='mj'>\\beta</span> 在哪、为什么不在劳动项上？</b><b><span class='mj'>\\beta</span> 乘的是「整个第二期效用」</b>——<b>包括第二期的消费与闲暇</b>。<b>所以明天的闲暇也被折现了</b>。<b>这一点在第 16 页的一阶条件里会体现：<b>今天的劳动条件里没有 <span class='mj'>\\beta</span>，明天的也没有</b>（<b>因为两边的 <span class='mj'>\\beta</span> 都约掉了</b>）。</b>"
    ),
    dec=[
        ("<span class='mj'>u(C,1-N)</span>", "期内效用", "<b>消费与闲暇的「组合」</b>。<b>具体函数形式见第 13 页（GHH）</b>。"),
        ("<span class='mj'>u_{C}&gt;0</span>", "消费的边际效用为正", "<b>多一点消费更快乐</b>。<b>这是「越多越好」。</b>"),
        ("<span class='mj'>u_{CC}&lt;0</span>", "消费边际效用递减", "<b>越吃越不香</b>。<b>它保证「消费平滑」有意义</b>——<b>否则家庭会把所有消费堆在一期。</b>"),
        ("<span class='mj'>u_{L}&gt;0</span>", "闲暇的边际效用为正", "<b>多休息更快乐</b>。<b>注意 <span class='mj'>L</span> 是闲暇、<span class='mj'>N</span> 是劳动</b>——<b><span class='mj'>u_{L}</span> 为正等价于「<span class='mj'>u</span> 对 <span class='mj'>N</span> 的偏导为负」</b>，<b>这个符号转换是本讲最常算错的一步。</b>"),
        ("<span class='mj'>\\beta</span>", "折现因子", "<b>耐心的程度</b>。<b><span class='mj'>\\beta</span> 越接近 1 越耐心</b>。<b>与 Topic 4 的 <span class='mj'>\\beta</span> 完全同义。</b>"),
        ("<span class='mj'>1-N</span>", "闲暇", "<b>时间禀赋为 1</b>。<b>所以 <span class='mj'>N\\in[0,1]</span></b>——<b>这个边界在求 FOC 时要留意（内点解假设）。</b>"),
    ],
    tip="<b>把「<span class='mj'>u_{L}&gt;0</span>」翻译成「<span class='mj'>\\partial u/\\partial N&lt;0</span>」这件事练三遍</b>：<b>因为 <span class='mj'>L=1-N</span>，<span class='mj'>\\frac{\\partial u}{\\partial N}=\\frac{\\partial u}{\\partial L}\\cdot\\frac{\\partial L}{\\partial N}=u_{L}\\cdot(-1)=-u_{L}&lt;0</span></b>。<b>这个「链式法则里的负号」在后面每一次求 FOC 都会出现</b>，<b>提前练熟能省很多错。</b>",
    warn="<b>别把 <span class='mj'>N</span> 当成「劳动供给的对数」或「就业率」</b>——<b>它是「劳动时间占比」，取值 0 到 1</b>。<b>另一个错误：把 <span class='mj'>\\beta</span> 写进劳动条件</b>（<b>第 16 页会说明它约掉了</b>）。"
)

add(13,
    kp="<b>GHH 偏好</b>：<span class='mj'>u(C_{t},1-N_{t})=\\ln\\left[C_{t}+\\theta_{t}\\ln(1-N_{t})\\right]</span>。<b><span class='mj'>\\theta_{t}</span> 衡量「闲暇相对于消费值多少」</b>。<b>出处：Greenwood, Hercowitz &amp; Huffman (1988)</b>。<b>作用：消掉劳动供给里的财富效应</b>。",
    plain="这是一个很特别的效用函数：两层对数套在一起。它的妙处不在「长什么样」，而在「求导之后会变成什么样」——消费会整个消失，只剩工资和闲暇参数。这就是为什么宏观模型里到处都用它：它让「劳动供给」变成一个只跟工资有关的简单式子。",
    lr=[
        dict(name="GHH 流量效用：为什么是「加」而不是「乘」",
             lhs="u(C_{t},1-N_{t})",
             lhs_t="<b>本期的快乐</b>",
             rhs="\\ln\\left[C_{t}+\\theta_{t}\\ln(1-N_{t})\\right]",
             rhs_t="<b>外层对数</b>包着 <b>「消费 ＋ 闲暇的折算值」</b>",
             why="<b>关键在于括号里是「加号」而不是「乘号」</b>。<b>如果是 Cobb–Douglas（<span class='mj'>C^{\\alpha}(1-N)^{1-\\alpha}</span>），边际替代率会是 <span class='mj'>\\frac{\\alpha}{1-\\alpha}\\cdot\\frac{1-N}{C}</span>——<b>含 <span class='mj'>C</span></b>，<b>所以「越富越不想干活」（财富效应）</b>。<b>GHH 用「加」把 <span class='mj'>C</span> 和 <span class='mj'>\\ln(1-N)</span> 放进同一个线性组合，再套一个 <span class='mj'>\\ln</span></b>——<b>结果是「外层对数的导数」在求边际替代率时被约掉了，<span class='mj'>C</span> 整个消失。</b><b>这就是「消掉财富效应」的技术原理。</b>",
             why_t="「加」买来了什么"),
    ],
    note=(
        "这一页是<b>全讲最技术、也最关键</b>的一页。分三层看：<br><br>"
        "<b>① 先接受它的「怪」</b>：<b><span class='mj'>\\ln</span> 里套 <span class='mj'>\\ln</span></b>。<b>这确实不常见</b>。<b>它的经济含义是：闲暇以「对数」的方式进入，所以「从 8 小时工作减到 7 小时」带来的快乐，比「从 1 小时减到 0 小时」小</b>——<b>即闲暇的边际效用递减，但下降得比线性慢。</b><br><br>"
        "<b>② 注意括号里的符号问题（很多人在这里卡住）</b>：<b><span class='mj'>\\ln(1-N)\\le0</span></b>（<b>因为 <span class='mj'>1-N\\le1</span></b>），<b>所以 <span class='mj'>\\theta\\ln(1-N)</span> 是一个「减项」</b>。<b>因此括号里必须 <span class='mj'>C&gt;-\\theta\\ln(1-N)</span>，否则对数无定义</b>——<b>这就是「消费必须足够大」的隐含要求。</b><b>经济上它意味着：一个极度贫困的家庭无法「选择更多闲暇」，因为它必须工作才能活。</b><br><br>"
        "<b>③（最重要）为什么它能「消掉财富效应」？</b><b>财富效应 ＝ 「收入变了，劳动供给跟着变」</b>。<b>普通偏好下，如果家庭变富（<span class='mj'>C</span> 上升），闲暇是「正常品」，所以他想多休息、少工作。</b><b>GHH 下这件事不会发生</b>，<b>因为劳动的边际替代率只依赖 <span class='mj'>(1-N)</span>，与 <span class='mj'>C</span> 无关</b>。<b>下一页（第 19 页）会把它算出来：<span class='mj'>\\frac{\\theta}{1-N}=w</span>。</b><b>右边没有 <span class='mj'>C</span>、没有 <span class='mj'>Y</span>、没有 <span class='mj'>r</span></b>——<b>所以「工资给定，劳动供给就定了」。</b><br><br>"
        "<b>这一条的后果有多大？</b><b>Topic 8 里 <span class='mj'>Y^{s}</span> 为什么竖直？</b><b>因为 <span class='mj'>N</span> 只依赖 <span class='mj'>w</span>，而 <span class='mj'>w</span> 由劳动市场单独定、与 <span class='mj'>r</span> 无关</b> ⇒ <b><span class='mj'>N</span> 与 <span class='mj'>r</span> 无关</b> ⇒ <b><span class='mj'>Y=AF(K,N)</span> 与 <span class='mj'>r</span> 无关</b> ⇒ <b>供给曲线竖直。</b><b>整条因果链的起点，就是这一页这个「加号」。</b>"
    ),
    dec=[
        ("GHH", "Greenwood–Hercowitz–Huffman", "<b>1988 年的三个人</b>。<b>名字要会写</b>——<b>这是本讲唯一需要记文献的地方</b>。<b>考点常问「GHH 偏好解决了什么问题」</b>。"),
        ("<span class='mj'>\\theta_{t}</span>", "闲暇权重", "<b>「闲暇值多少」</b>。<b><span class='mj'>\\theta\\uparrow</span> ⇒ 更爱休息 ⇒ 同一工资下工作更少</b>（<b>第 19 页的 <span class='mj'>N^{s}</span> 上会体现为「左移」</b>）。"),
        ("外层 <span class='mj'>\\ln</span>", "对数效用", "<b>保证「消费的边际效用递减」且「相对风险厌恶为 1」</b>。<b>它的作用是让「消费」在求导后变成 <span class='mj'>1/(\\cdot)</span>，<b>从而与内层的项约掉</b>。"),
        ("财富效应", "wealth effect", "<b>「变富了想多休息」</b>。<b>GHH 把它消掉</b>。<b>后果：劳动供给只依赖工资</b>。<b>这是本讲最重要的一句话。</b>"),
        ("additively separable", "可加可分", "<b>括号里是「加」</b>。<b>这是「消掉 <span class='mj'>C</span>」的技术关键</b>。<b>换成「乘」就没有这个性质了。</b>"),
    ],
    tip="<b>用一句「口诀」记住它的作用</b>：<b>「GHH ＝ 工资一给定，劳动供给就定了。」</b><b>不管是收入变了、利率变了、还是财富变了，只要工资没变，工作时间就不变。</b><b>这句话能推出 Topic 8 的竖直供给曲线，也能解释为什么本讲的劳动市场可以「单独解」。</b>",
    warn="<b>三个高频错误</b>：<b>① 写成 <span class='mj'>\\ln C+\\theta\\ln(1-N)</span></b>（<b>错！那是「对数可加」，不是 GHH</b>；<b>GHH 是「先加再取对数」</b>）；<b>② 说「GHH 让劳动供给不依赖工资」</b>（<b>错，它照样依赖工资，只是不依赖收入</b>）；<b>③ 忘记括号内必须为正</b>（<b>所以 <span class='mj'>C</span> 不能太小，这是内点解的前提</b>）。"
)


# ==================== ⑥ 家庭最优化：约束与一阶条件 ====================

add(14,
    kp="<b>家庭的两条流量预算</b>：<span class='mj'>C_{t}+S_{t}=w_{t}N_{t}+D_{t}</span>；<span class='mj'>C_{t+1}=w_{t+1}N_{t+1}+D_{t+1}+(1+r_{t})S_{t}</span>。<b>消掉 <span class='mj'>S_{t}</span> 得 IBC</b>。<b>与之前唯一的区别：收入是内生的</b>（<span class='mj'>w_{t}N_{t}</span> 里 <span class='mj'>N_{t}</span> 是家庭自己选的）。",
    plain="家里的账很简单：今年的工资加分红，一部分花掉、一部分存起来。明年把存款连本带利取出来，加上明年的工资和分红，全部花掉。把两年的账合成一本，就是「一辈子花的钱等于一辈子赚的钱」。",
    lr=[
        dict(name="两条流量约束：每一期各一本账",
             lhs="C_{t}+S_{t}",
             lhs_t="<b>今年的去处</b>（消费 ＋ 储蓄）",
             rhs="w_{t}N_{t}+D_{t}",
             rhs_t="<b>今年的来源</b>（工资 ＋ 股息）",
             why="<b>这就是「收支平衡」</b>。<b>与 Topic 4 的版本相比，<b>只有收入变了</b></b>：<b>从外生的 <span class='mj'>Y_{t}</span> 变成「<span class='mj'>w_{t}N_{t}+D_{t}</span>」</b>。<b>但这两项加起来正好是 <span class='mj'>Y_{t}</span></b>（<b>第 5 页证过</b>）：<b><span class='mj'>w_{t}N_{t}+D_{t}=w_{t}N_{t}+(Y_{t}-w_{t}N_{t})=Y_{t}</span></b>。<b>所以「收入内生」并不改变「总量是 <span class='mj'>Y_{t}</span>」这件事</b>——<b>变的是「家庭怎么在工资与闲暇之间分配」，不是「总量有多少」。</b>",
             why_t="与 Topic 4 的差别在哪"),
        dict(name="跨期预算约束（IBC）：两本账合成一本",
             lhs="C_{t}+\\frac{C_{t+1}}{1+r_{t}}",
             lhs_t="<b>一生消费的现值</b>",
             rhs="w_{t}N_{t}+D_{t}+\\frac{w_{t+1}N_{t+1}+D_{t+1}}{1+r_{t}}",
             rhs_t="<b>一生收入的现值</b>（工资 ＋ 股息，两期）",
             why="<b>推导只有一步</b>：<b>把第一条的 <span class='mj'>S_{t}=w_{t}N_{t}+D_{t}-C_{t}</span> 代进第二条</b>：<br>"
                 "<b><span class='mj'>C_{t+1}=w_{t+1}N_{t+1}+D_{t+1}+(1+r_{t})\\left[w_{t}N_{t}+D_{t}-C_{t}\\right]</span></b><br>"
                 "<b>两边除以 <span class='mj'>(1+r_{t})</span>、把 <span class='mj'>C_{t}</span> 移过去，就得到上式。</b><b>「消掉 <span class='mj'>S</span>」这一步的意义是：<b>储蓄不是「目标」，只是「延后的消费」</b>——<b>所以可以从约束里彻底消掉，只在需要时再算回来。</b>",
             why_t="怎么消掉 <span class='mj'>S_{t}</span>"),
    ],
    note=(
        "这一页有两个细节值得停一下：<br><br>"
        "<b>① 为什么说「income is partly endogenous」——「部分」内生？</b><b>因为 <span class='mj'>w_{t}N_{t}</span> 里 <span class='mj'>w_{t}</span> 是市场给的（外生）</b>，<b>而 <span class='mj'>N_{t}</span> 是家庭自己选的（内生）</b>。<b>所以「劳动收入」是「价格 × 数量」的一半内生、一半外生</b>。<b>股息 <span class='mj'>D_{t}</span> 则是完全外生的</b>（<b>家庭是企业的小股东，单个家庭不影响企业决策</b>）。<b>这个区分在求一阶条件时很关键</b>：<b>对 <span class='mj'>N_{t}</span> 求导时，<span class='mj'>w_{t}</span> 当常数、<span class='mj'>N_{t}</span> 当变量。</b><br><br>"
        "<b>② 为什么「一生收入」里要加股息？</b><b>因为家庭的收入有两条腿</b>：<b>劳动（<span class='mj'>wN</span>）与资本（<span class='mj'>D</span>）</b>。<b>如果漏掉 <span class='mj'>D</span>，家庭的预算会「缺一块」</b>，<b>而这一块正好是产出中「没被工资吃掉」的部分</b>。<b>结果是：商品市场出清 <span class='mj'>Y=C+I</span> 会推不出来</b>（<b>因为家庭「没花完」的钱无处可去</b>）。<br><br>"
        "<b>③ 注意这里没有「政府」</b>：<b>没有 <span class='mj'>T</span>、没有 <span class='mj'>G</span></b>。<b>加进去就是 <span class='mj'>C_{t}+S_{t}=w_{t}N_{t}+D_{t}-T_{t}</span>，出清变成 <span class='mj'>Y=C+I+G</span></b>。<b>Topic 6 已经做过「加政府」的那一套</b>，<b>本讲先保持最干净的形式</b>——<b>但答题时要能说「加政府就是在收入里扣 <span class='mj'>T</span>、在出清里加 <span class='mj'>G</span>」。</b>"
    ),
    dec=[
        ("<span class='mj'>S_{t}</span>", "储蓄", "<b>可正可负</b>。<b>正的 ＝ 借钱给别人（买企业债、存银行）；负的 ＝ 借钱</b>。<b>本讲里它有了「去处」——变成投资（第 24 页）。</b>"),
        ("partly endogenous", "部分内生", "<b><span class='mj'>w</span> 外生、<span class='mj'>N</span> 内生</b>。<b>所以「劳动收入」是「价格 × 数量」的乘积</b>，<b>求导时只对 <span class='mj'>N</span> 动。</b>"),
        ("IBC", "跨期预算约束", "<b>两期合成一本账</b>。<b>它是「消费的现值 ＝ 收入的现值」</b>。<b>与 Topic 4 同构，只是右边换了内容。</b>"),
        ("<span class='mj'>D_{t}</span>", "股息（外生）", "<b>单个家庭不影响企业决策</b>，<b>所以把 <span class='mj'>D</span> 当常数</b>。<b>但均衡里 <span class='mj'>D</span> 会被 <span class='mj'>w,N,K</span> 决定</b>——<b>这是「个体视角」与「均衡视角」的区别。</b>"),
        ("没有 <span class='mj'>T</span> 与 <span class='mj'>G</span>", "本讲先不加政府", "<b>保持最干净</b>。<b>加进去只需两个改动</b>：<b>收入扣 <span class='mj'>T</span>、出清加 <span class='mj'>G</span></b>。"),
    ],
    tip="<b>「消 <span class='mj'>S</span>」这个动作在全书出现四次</b>（Topic 4、5、6、7）。<b>每次都是同一招：从流量约束解出 <span class='mj'>S</span>，代进下一期</b>。<b>记住这一招，四个 IBC 都不用背</b>——<b>只要记住「两边同除 <span class='mj'>1+r</span>」这一步。</b>",
    warn="<b>三个高频错误</b>：<b>① 忘记股息 <span class='mj'>D</span></b>（<b>导致后面 <span class='mj'>Y=C+I</span> 推不出来</b>）；<b>② 把 <span class='mj'>w_{t}N_{t}</span> 整块当外生</b>（<b>求 FOC 时 <span class='mj'>N</span> 是变量</b>）；<b>③ 忘记 <span class='mj'>(1+r_{t})S_{t}</span> 里的本金</b>（<b>写成 <span class='mj'>r_{t}S_{t}</span> 就变成「只取利息、不动本金」了</b>）。"
)

add(15,
    kp="家庭选 <span class='mj'>C_{t},N_{t},N_{t+1}</span>（<b><span class='mj'>C_{t+1}</span> 由 IBC 决定</b>）<b>最大化终生效用</b>，<b>把 <span class='mj'>r_{t},w_{t},w_{t+1},D_{t},D_{t+1}</span> 当给定</b>。<b>三个决策变量 ⇒ 三个一阶条件。</b>",
    plain="家庭的问题：今年花多少、今年干多少活、明年干多少活。明年花多少不用单独决定——因为钱一共就那么多，今年少花一点，明年就能多花一点。",
    note=(
        "这一页有两处「为什么这样设定」值得说清：<br><br>"
        "<b>① 为什么不把 <span class='mj'>C_{t+1}</span> 当决策变量？</b><b>因为 IBC 已经把它钉死了</b>：<b>给定 <span class='mj'>C_{t},N_{t},N_{t+1}</span>，<span class='mj'>C_{t+1}</span> 由「一生收支平衡」唯一确定</b>。<b>如果把它也当变量，就会多一个方程、而且与 IBC 重复</b>（<b>这就是「约束已经是等式」的模型里常见的处理方式：用约束消掉一个变量，而不是引入乘子。</b>）<br>"
        "<b>另一种等价做法</b>：<b>保留 <span class='mj'>C_{t+1}</span>，用拉格朗日乘子 <span class='mj'>\\lambda</span> 处理 IBC</b>——<b>会多出一个「<span class='mj'>\\lambda</span> ＝ 边际效用」的方程，最后仍然得到同样的三个条件</b>。<b>两种做法在考试里都可以，但「消变量法」更短。</b><br><br>"
        "<b>② 为什么 <span class='mj'>N_{t+1}</span> 可以「现在」就决定？</b><b>因为它出现在「一生收入」里</b>——<b>家庭今天就知道自己明年打算工作多少，并据此决定今天花多少</b>。<b>这是「完全预见」（perfect foresight）的假设</b>：<b>没有不确定性，所以「计划」与「实现」一致。</b><b>本讲全部内容都在这个假设下</b>；<b>引入不确定性是后面（比如 Topic 9 的预期）的事。</b><br><br>"
        "<b>③ 注意「给定 <span class='mj'>D_{t},D_{t+1}</span>」这句话</b>：<b>家庭把股息当外生</b>。<b>这在「代表性家庭」的设定下是自洽的</b>——<b>因为一个家庭「拥有整个企业」，但它「不影响企业决策」（企业按 <span class='mj'>V</span> 最大化，不看单个股东）</b>。<b>这个「股权分散、决策集中」的假设让「家庭不内部化企业决策」成立。</b>"
    ),
    dec=[
        ("决策变量", "choice variables", "<b><span class='mj'>C_{t},N_{t},N_{t+1}</span></b>。<b>三个</b>，<b>对应三个 FOC（第 16 页）</b>。<b>数量要对得上。</b>"),
        ("<span class='mj'>C_{t+1}</span> 由 IBC 决定", "residual", "<b>它是「余额」</b>。<b>不是不选，而是「被动决定」</b>。<b>所以只有一个跨期条件（欧拉方程），不是两个。</b>"),
        ("perfect foresight", "完全预见", "<b>没有不确定性</b>。<b>所以「明年打算工作多少」今天就能定</b>。<b>这是两期模型能「一次解完」的前提。</b>"),
        ("给定 <span class='mj'>D</span>", "拿股息当外生", "<b>家庭是企业股东但不决策</b>。<b>所以 <span class='mj'>D</span> 对家庭是「天上掉下来的」</b>。<b>均衡里它由 <span class='mj'>w,N,K</span> 决定。</b>"),
    ],
    tip="<b>数「决策变量个数 ＝ 一阶条件个数」这个习惯要养成</b>：<b>企业 3 个变量 → 3 个条件；家庭 3 个变量 → 3 个条件</b>。<b>如果数目不匹配，一定要停下来想「是不是漏了一个约束或者多算了一个变量」</b>——<b>这是检查作业最快的方法。</b>",
    warn="<b>别把 <span class='mj'>C_{t+1}</span> 也列进决策变量再「独立」求一个 FOC</b>——<b>那会得到两个欧拉方程，互相矛盾。</b><b>另一个坑：以为「家庭选 <span class='mj'>N_{t+1}</span>」意味着「明年还能改」</b>——<b>在完全预见下，今天定的就是明年实际发生的。</b>"
)

add(16,
    kp="<b>三个一阶条件</b>：① <span class='mj'>u_{C}(C_{t},1-N_{t})=\\beta(1+r_{t})u_{C}(C_{t+1},1-N_{t+1})</span>（<b>欧拉方程</b>）；② <span class='mj'>w_{t}u_{C}(C_{t},1-N_{t})=u_{L}(C_{t},1-N_{t})</span>；③ <span class='mj'>w_{t+1}u_{C}(C_{t+1},1-N_{t+1})=u_{L}(C_{t+1},1-N_{t+1})</span>。",
    plain="三句话：① 今天少花一块、留到明天花，两头得到的快乐要一样（不然就挪一挪）；② 今天多干一小时，赚的工资买来的快乐，要等于少休息一小时损失的快乐；③ 明天也是这个道理。",
    lr=[
        dict(name="① 跨期：欧拉方程",
             lhs="u_{C}(C_{t},1-N_{t})",
             lhs_t="<b>今天少花一块的损失</b>（边际效用）",
             rhs="\\beta(1+r_{t})u_{C}(C_{t+1},1-N_{t+1})",
             rhs_t="<b>存起来、明年多花的收益</b>（折现后的边际效用）",
             why="<b>今天少消费一块：损失 <span class='mj'>u_{C}</span>。</b><b>这一块存起来，明年变成 <span class='mj'>1+r</span>，多消费带来的效用是 <span class='mj'>(1+r)u_{C}'</span>，<b>再按耐心折现 <span class='mj'>\\beta</span></b>。<b>两者相等时，家庭「不想再挪了」。</b><b>注意它<b>没有 <span class='mj'>N</span> 的项</b></b>——<b>因为「今天少花一块」不影响「今天工作多少」</b>（<b>这是可加可分的好处</b>）。<b>形式与 Topic 4 完全一样</b>，<b>只是 <span class='mj'>u_{C}</span> 里多了 <span class='mj'>1-N</span>。</b>",
             why_t="为什么两边相等"),
        dict(name="② 期内：劳动与闲暇的取舍",
             lhs="w_{t}u_{C}(C_{t},1-N_{t})",
             lhs_t="<b>多工作一小时的收益</b>（工资 × 钱的边际效用）",
             rhs="u_{L}(C_{t},1-N_{t})",
             rhs_t="<b>少休息一小时的损失</b>（闲暇的边际效用）",
             why="<b>多工作一小时：多赚 <span class='mj'>w_{t}</span>，能多消费 <span class='mj'>w_{t}</span>，效用增加 <span class='mj'>w_{t}u_{C}</span>。</b><b>代价：少一小时闲暇，效用减少 <span class='mj'>u_{L}</span>。</b><b>两者相等时达到最优。</b><b>为什么左边要乘 <span class='mj'>u_{C}</span>？</b><b>因为工资是「钱」，效用是「快乐」——<b>要用 <span class='mj'>u_{C}</span> 把「钱」换算成「快乐」</b>。</b><b>这是本页最容易被问「为什么要乘 <span class='mj'>u_{C}</span>」的地方。</b>",
             why_t="为什么工资要乘 <span class='mj'>u_{C}</span>"),
    ],
    note=(
        "三个条件里，<b>第二个是本讲真正的「新东西」</b>——<b>另外两个在 Topic 4 都见过</b>。<br><br>"
        "<b>① 为什么第二个条件里没有 <span class='mj'>\\beta</span>？</b><b>因为「今天工作」的收益与成本都发生在今天</b>——<b>是「同一期内」的取舍，不用折现</b>。<b>第三个条件同理（都是明年的）</b>。<b>只有「今天 vs 明天」才需要 <span class='mj'>\\beta</span></b>。<b>这是判断「该不该乘 <span class='mj'>\\beta</span>」的唯一标准：<b>看两边是不是同一期</b>。</b><br><br>"
        "<b>② 三个条件的「层次」要分清</b>：<br>"
        "· <b>欧拉方程</b>：<b>跨期</b>（今天 vs 明天），管「消费的时序」。<br>"
        "· <b>劳动条件</b>：<b>期内</b>（消费 vs 闲暇），管「工作多少」，<b>且每一期各一条</b>。<br>"
        "<b>所以「跨期一个、期内两个」，一共三个</b>——<b>与「三个决策变量」对应。</b><br><br>"
        "<b>③ 为什么第二个条件能「单独解出 <span class='mj'>N_{t}</span>」？</b><b>因为它只含 <span class='mj'>N_{t}</span> 与 <span class='mj'>w_{t}</span>（还有 <span class='mj'>C_{t}</span>）</b>。<b>而 <span class='mj'>C_{t}</span> 会出现在两边</b>，<b>所以一般不能单独解</b>。<b>但 GHH 下 <span class='mj'>u_{C}</span> 与 <span class='mj'>u_{L}</span> 的结构会让 <span class='mj'>C_{t}</span> 约掉</b>——<b>这就是第 19 页会发生的事</b>。<b>「为什么本讲要特意假设 GHH」的答案，就在这一页与下一页之间。</b>"
    ),
    dec=[
        ("<span class='mj'>u_{C}</span>", "消费的边际效用", "<b>「多一块钱多快乐多少」</b>。<b>它在三个条件里出现三次</b>——<b>每次都在「把名义量换算成效用」。</b>"),
        ("<span class='mj'>u_{L}</span>", "闲暇的边际效用", "<b>「多一小时闲暇多快乐多少」</b>。<b>注意 <span class='mj'>L=1-N</span></b>：<b>对 <span class='mj'>N</span> 求导时它会变号。</b>"),
        ("<span class='mj'>\\beta(1+r)</span>", "跨期「价格」", "<b>折现因子 × 总利率</b>。<b><span class='mj'>\\beta(1+r)&gt;1</span> ⇒ 消费上升（明天更多）</b>；<b><span class='mj'>=1</span> ⇒ 完全平滑</b>；<b><span class='mj'>&lt;1</span> ⇒ 消费下降</b>。"),
        ("没有 <span class='mj'>\\beta</span>", "期内条件", "<b>劳动条件不含 <span class='mj'>\\beta</span></b>。<b>因为两边是同一期</b>。<b>这是判断「该不该折现」的标准。</b>"),
        ("每期各一条", "两个劳动条件", "<b><span class='mj'>N_{t}</span> 与 <span class='mj'>N_{t+1}</span> 各一个条件</b>。<b>它们形式完全一样，只是下标不同</b>。<b>所以「劳动供给函数每期都成立」。</b>"),
    ],
    tip="<b>写这三个条件时，先用「一句话翻译」再写公式</b>：<b>「今天少花一块的损失 ＝ 存到明年的收益」／「多工作一小时的收益 ＝ 少休息的损失」</b>。<b>翻译对了，公式里该乘什么、该不该加 <span class='mj'>\\beta</span> 就不会错</b>——<b>因为「话」里已经包含了「今天还是明天」。</b>",
    warn="<b>四个高频错误</b>：<b>① 劳动条件里加了 <span class='mj'>\\beta</span></b>；<b>② 把 <span class='mj'>u_{L}</span> 写成 <span class='mj'>u_{N}</span> 却忘了变号</b>（<b><span class='mj'>u_{N}=-u_{L}</span></b>）；<b>③ 欧拉方程漏掉 <span class='mj'>(1+r)</span> 的「本金 1」</b>（<b>写成 <span class='mj'>ru_{C}'</span> 就错了</b>）；<b>④ 忘记两边的 <span class='mj'>1-N</span> 下标</b>（<b>欧拉方程左边是 <span class='mj'>1-N_{t}</span>、右边是 <span class='mj'>1-N_{t+1}</span></b>）。"
)

add(17,
    kp="<b>三个条件的读法</b>：<span class='mj'>C_{t}</span> 条件是<b>常见的欧拉方程</b>，只是<b>效用里多了闲暇</b>；<span class='mj'>N_{t}</span> 条件是<b>「多要一单位闲暇的边际收益（右）＝ 放弃工资的边际成本（左）」</b>；<span class='mj'>N_{t+1}</span> 条件<b>与 <span class='mj'>N_{t}</span> 完全相同，只是日期加一</b>。",
    plain="这一页在解释上一页三个式子的意思。最关键的一句：左边是「不工作赚不到的钱，换成快乐」，右边是「多休息带来的快乐」。两者相等，就是「我愿意工作到这儿为止」。",
    note=(
        "这一页有两个<b>表述细节</b>值得逐字读：<br><br>"
        "<b>① 课件说 <span class='mj'>N_{t}</span> 条件是「marginal benefit of taking one more unit of leisure (RHS) is equal to marginal cost, captured by foregone wage income and evaluated in units of marginal utility of consumption (LHS)」</b>。<b>注意这里「右边是收益、左边是成本」</b>——<b>与「左边收益、右边成本」的常见写法相反</b>。<b>但数学上无所谓，只要两边相等。</b><b>这句话真正有价值的是「evaluated in units of marginal utility of consumption」</b>：<b>它在解释「为什么左边要乘 <span class='mj'>u_{C}</span>」</b>——<b>因为工资是「产品」，不是「效用」，必须换算。</b><b>答卷时写这半句，就是「理解」与「背公式」的分界。</b><br><br>"
        "<b>②「<span class='mj'>N_{t+1}</span> condition looks exactly the same as <span class='mj'>N_{t}</span>, only dated <span class='mj'>t+1</span>」</b>：<b>这句话说明「劳动供给是「逐期」决定的，不是「一次性」决定」</b>。<b>而且两期之间<b>没有通过「储蓄」连起来</b></b>——<b>因为可加可分 ＋ 时间禀赋固定，今天的劳动决策不影响明天的劳动决策</b>（<b>唯一的联系是通过 <span class='mj'>C</span>，而 GHH 又会把它切断</b>）。<b>这个「逐期独立」是后面 <span class='mj'>Y^{s}</span> 竖直的第二个支柱。</b>"
    ),
    dec=[
        ("foregone wage", "放弃的工资", "<b>工作的「机会成本」</b>。<b>休息一小时＝少赚 <span class='mj'>w</span></b>。<b>这是「闲暇的价格」。</b>"),
        ("in units of", "以…为单位", "<b>「换算成效用的单位」</b>。<b>这是「为什么要乘 <span class='mj'>u_{C}</span>」的答案。</b>"),
        ("only dated <span class='mj'>t+1</span>", "只是日期加一", "<b>两期劳动条件完全同构</b>。<b>所以「劳动供给函数」只需要写一次。</b>"),
        ("每期独立", "period-by-period", "<b>今天的劳动决策不影响明天的</b>。<b>这是 GHH ＋ 可加可分的结果</b>。<b>也是 <span class='mj'>Y^{s}</span> 竖直的第二个支柱。</b>"),
    ],
    tip="<b>把「<span class='mj'>u_{C}</span> 是换算率」这句话记住</b>：<b>所有「价格 × 边际效用」的形式，都是「把产品换算成效用」</b>。<b>比如 <span class='mj'>w u_{C}</span> ＝ 「工资的效用价值」</b>。<b>看到这种结构，能立刻说出它在干什么，比会推导更重要。</b>",
    warn="<b>别说「左边是收益、右边是成本」然后自己绕晕</b>——<b>课件是「右边收益、左边成本」</b>。<b>答卷时最好明确写「等价于：多工作一小时的收益（<span class='mj'>wu_{C}</span>）＝ 少休息一小时的损失（<span class='mj'>u_{L}</span>）」</b>，<b>把方向说清，避免被扣「概念混乱」。</b>"
)

add(18,
    kp="<b>从一阶条件可以推出与之前相同的消费函数</b>：<span class='mj'>C_{t}=C^{d}(Y_{t}^{+},Y_{t+1}^{+},r_{t}^{-})</span>。<b>若有政府且李嘉图等价成立</b>：<span class='mj'>C_{t}=C^{d}(Y_{t}-G_{t},\\ Y_{t+1}-G_{t+1},\\ r_{t})</span>。<b>课件说「cutting a few corners」——略过了推导。</b>",
    plain="绕了一大圈（先算企业、再算家庭、解三个一阶条件），最后发现：消费还是那个消费函数，跟第四讲一模一样。收入越高花得越多、利率越高花得越少。这不是白忙——因为现在我们知道「收入是从哪来的」了。",
    lr=[
        dict(name="消费函数：绕回来还是它",
             lhs="C_{t}",
             lhs_t="<b>本期消费</b>",
             rhs="C^{d}(Y_{t}^{+},\\ Y_{t+1}^{+},\\ r_{t}^{-})",
             rhs_t="<b>一生收入的现值越大越花、利率越高越少花</b>",
             why="<b>三个符号的来源</b>：<b><span class='mj'>Y_{t}\\uparrow</span> ⇒ 一生财富上升 ⇒ 消费上升</b>（<b>正</b>）；<b><span class='mj'>Y_{t+1}\\uparrow</span> ⇒ 同理</b>（<b>正</b>）；<b><span class='mj'>r_{t}\\uparrow</span> ⇒ 用欧拉方程看，<span class='mj'>\\beta(1+r)&gt;1</span> 时「明天更值钱」⇒ 今天少花</b>（<b>负，对储蓄者</b>）。<b>与 Topic 4 的 <span class='mj'>C^{d}(Y_{t},Y_{t+1},r_{t})</span> 完全一致</b>——<b>因为「跨期决策的结构」没变，变的只是「<span class='mj'>Y</span> 从哪来」。</b>",
             why_t="三个符号从哪来"),
    ],
    note=(
        "这一页短，但<b>值得讲清「cutting a few corners」略掉了什么</b>：<br><br>"
        "<b>① 略掉的是「从 FOC 解出闭式解」的过程。</b><b>完整做法是：给定 <span class='mj'>Y_{t},Y_{t+1},r_{t}</span>（进而 <span class='mj'>w,N,D</span>），联立欧拉方程与 IBC，解出 <span class='mj'>C_{t},C_{t+1}</span>。</b><b>Topic 4 做过这件事（对数效用下有闭式解）</b>，<b>这里因为 <span class='mj'>u</span> 还含闲暇，形式更复杂，所以课件直接给结论。</b><br><br>"
        "<b>② 为什么「结果一样」这件事值得强调？</b><b>因为它说明：<b>消费函数的形状不依赖于「收入怎么生产出来」</b>。</b><b>不管 <span class='mj'>Y</span> 是天上掉的（Topic 5）还是生产出来的（Topic 7），家庭的行为规则都是同一个 <span class='mj'>C^{d}</span></b>。<b>这是「模块化」的好处：<b>Topic 4 造的那个零件，在这里直接能用</b>。</b><br><br>"
        "<b>③ 为什么「有政府时」的自变量是 <span class='mj'>Y-G</span> 而不是 <span class='mj'>Y-T</span>？</b><b>因为李嘉图等价（Topic 6）已经证明了「<span class='mj'>T</span> 不重要」</b>——<b>家庭会看穿「今天的债就是明天的税」，所以真正影响消费的是「政府拿走了多少资源」（<span class='mj'>G</span>），而不是「用什么名义拿」（<span class='mj'>T</span> 还是 <span class='mj'>B</span>）。</b><b>这一句话把 Topic 6 与本讲接上了</b>——<b>两讲的消费函数是同一个，只是 Topic 6 在禀赋经济里用它、这里在生产经济里用它。</b>"
    ),
    dec=[
        ("cutting a few corners", "略去一些细节", "<b>跳过了「解闭式解」的代数</b>。<b>结论与 Topic 4 一致</b>，<b>所以可以直接搬过来用。</b>"),
        ("<span class='mj'>C^{d}</span>", "消费函数（决策规则）", "<b>「给一生收入与利率，最优消费多少」</b>。<b>它是「解完最优化之后」的结果</b>——<b>不是假设，是推导出来的。</b>"),
        ("<span class='mj'>Y_{t}</span> 的正号", "收入效应", "<b>一生收入上升 ⇒ 各期消费都上升</b>（<b>平滑</b>）。<b>这是「永久收入假说」的微观版。</b>"),
        ("<span class='mj'>r_{t}</span> 的负号", "跨期替代", "<b>利率上升 ⇒ 今天的消费变贵 ⇒ 少花</b>。<b>注意：对「储蓄者」成立；对「借款人」可能相反</b>（<b>Topic 4 讲过这个区别</b>）。"),
        ("<span class='mj'>Y-G</span>", "李嘉图等价的形式", "<b>政府拿走的是「资源」，不是「名义税」</b>。<b>所以自变量用 <span class='mj'>G</span> 不用 <span class='mj'>T</span></b>。"),
    ],
    tip="<b>答题时如果只写 <span class='mj'>C^{d}(Y,Y',r)</span> 会显得「跳步」</b>：<b>加一句「由欧拉方程与 IBC 联立得到，形式与 Topic 4 相同（<span class='mj'>\\rightarrow</span> Topic 4 第 13 页）」</b>，<b>既说明来源，又显示你知道它和前面接得上。</b><b>本讲的所有「结论」都应该这样「挂回」前面的讲次。</b>",
    warn="<b>三个高频错误</b>：<b>① 以为 <span class='mj'>C^{d}</span> 是「假设」</b>（<b>它是推导结果</b>）；<b>② 把有政府时的自变量写成 <span class='mj'>Y-T</span></b>（<b>在李嘉图等价下应写 <span class='mj'>Y-G</span></b>）；<b>③ 把 <span class='mj'>r</span> 的符号一律当负</b>（<b>对借款的家庭，收入效应可能压过替代效应</b>，<b>Topic 4 第 24/27 页讲过</b>）。"
)


# ==================== ⑦ 劳动供给与银行 ====================

add(19,
    kp="<b>一般情况下劳动供给很麻烦</b>（<span class='mj'>w</span> 有收入与替代两种相反效应、非劳动收入与预期也会影响）。<b>GHH 下一切化简成一句</b>：<span class='mj'>\\frac{\\theta_{t}}{1-N_{t}}=w_{t}</span>，于是 <b><span class='mj'>N_{t}=N^{s}(w_{t}^{+},\\theta_{t}^{-})</span></b>。<b>消费 <span class='mj'>C_{t}</span> 完全消失。</b>",
    plain="为什么普通情况下劳动供给难写？因为工资涨了有两股相反的力：工资高，休息变贵（少休息）；但工资高也变富了，想多休息。哪个大说不清。GHH 的妙处是把第二股力掐掉了——只剩「休息变贵」。于是「工资给定，工作时间就定了」，跟家里多有钱、利率多少都没关系。",
    lr=[
        dict(name="GHH 下的劳动供给：两步就得到",
             lhs="\\frac{\\theta_{t}}{1-N_{t}}",
             lhs_t="<b>闲暇的边际效用</b>（用消费的边际效用折算过）",
             rhs="w_{t}",
             rhs_t="<b>实际工资</b>（<b>闲暇的价格</b>）",
             why="<b>推导只需两步</b>。记 <span class='mj'>X=C_{t}+\\theta_{t}\\ln(1-N_{t})</span>，则 <span class='mj'>u=\\ln X</span>：<br>"
                 "<b>第一步（两个偏导）</b>：<br>"
                 "<b><span class='mj'>u_{C}=\\frac{1}{X}</span></b>；<br>"
                 "<b><span class='mj'>u_{L}=\\frac{\\theta_{t}}{X}\\cdot\\frac{1}{1-N_{t}}</span></b>（<b>链式法则：外层 <span class='mj'>1/X</span>，内层对 <span class='mj'>\\ln(1-N)</span> 求导得 <span class='mj'>1/(1-N)</span>，再乘系数 <span class='mj'>\\theta</span></b>）。<br>"
                 "<b>第二步（代进 FOC <span class='mj'>w u_{C}=u_{L}</span>）</b>：<br>"
                 "<b><span class='mj'>w\\cdot\\frac{1}{X}=\\frac{\\theta_{t}}{X}\\cdot\\frac{1}{1-N_{t}}</span></b><br>"
                 "<b>两边的 <span class='mj'>1/X</span> 直接约掉</b> ⇒ <b><span class='mj'>\\frac{\\theta_{t}}{1-N_{t}}=w_{t}</span></b>。<br>"
                 "<b>「<span class='mj'>X</span> 被约掉」就是「<span class='mj'>C</span> 消失」——<b>这是 GHH 全部魔力的所在</b>。</b>",
             why_t="为什么 C 会消失"),
    ],
    note=(
        "这一页是<b>全讲最值得反复看的一页</b>。四个层次：<br><br>"
        "<b>① 为什么「一般情况下麻烦」？</b><b>因为 <span class='mj'>w\\uparrow</span> 有两股相反的力</b>：<br>"
        "· <b>替代效应</b>：<b>休息变贵 ⇒ 少休息、多工作</b>（<b><span class='mj'>N\\uparrow</span></b>）。<br>"
        "· <b>收入效应</b>：<b>工资高等于变富 ⇒ 想多休息</b>（<b><span class='mj'>N\\downarrow</span></b>）。<br>"
        "<b>两者方向相反，谁大要看偏好</b>——<b>所以一般情况下的劳动供给曲线可能上斜、竖直、甚至向后弯</b>。<b>模型就没法算了。</b><br><br>"
        "<b>② GHH 做了什么？</b><b>它让「收入效应」完全消失</b>：<b>因为劳动的边际替代率 <span class='mj'>\\frac{u_{L}}{u_{C}}=\\frac{\\theta}{1-N}</span> 不含 <span class='mj'>C</span></b>。<b>所以「变富」不会改变「工作多少」</b>——<b>只剩替代效应。</b><b>于是劳动供给曲线<b>必然上斜</b>，而且形状完全由 <span class='mj'>\\theta</span> 定。</b><br><br>"
        "<b>③ 由 <span class='mj'>\\frac{\\theta}{1-N}=w</span> 可以解出显式函数</b>：<b><span class='mj'>N=1-\\frac{\\theta}{w}</span></b>。<b>这个式子太好用了，建议直接记住</b>：<br>"
        "· <b><span class='mj'>w\\uparrow</span> ⇒ <span class='mj'>N\\uparrow</span></b>（<b>正号</b>，<b>且是「趋近于 1」的上斜</b>）。<br>"
        "· <b><span class='mj'>\\theta\\uparrow</span> ⇒ <span class='mj'>N\\downarrow</span></b>（<b>负号</b>，<b>更爱休息</b>）。<br>"
        "· <b>而且 <span class='mj'>w\\to\\infty</span> 时 <span class='mj'>N\\to1</span>、<span class='mj'>w\\to\\theta</span> 时 <span class='mj'>N\\to0</span></b>——<b>「工资低于 <span class='mj'>\\theta</span> 就完全不工作」</b>，<b>这是一个「保留工资」（reservation wage）的含义。</b><br><br>"
        "<b>④ 这个结论对后面有多重要？</b><b>它是 Topic 8 里 <span class='mj'>Y^{s}</span> 竖直的<b>唯一原因</b></b>：<b><span class='mj'>N=1-\\theta/w</span> 只依赖 <span class='mj'>w</span></b> ⇒ <b>劳动市场单独定出 <span class='mj'>N</span> 与 <span class='mj'>w</span></b> ⇒ <b><span class='mj'>Y=AF(K,N)</span> 与 <span class='mj'>r</span> 无关</b> ⇒ <b>供给竖直线</b>。<b>换句话说：[[T8#p14|Topic 8 第 14 页]]那张图上那条竖线，站着的就是这一页这个式子。</b>"
    ),
    dec=[
        ("<span class='mj'>\\theta_{t}</span>", "闲暇权重", "<b>负号</b>：<b><span class='mj'>\\theta\\uparrow</span> ⇒ 同一工资下工作更少</b>。<b>它是「劳动力供给冲击」的载体</b>（比如疫情后更重视休闲）。"),
        ("<span class='mj'>\\frac{\\theta}{1-N}</span>", "闲暇的「价格」", "<b>它必须等于 <span class='mj'>w</span></b>。<b>直觉：<span class='mj'>N</span> 越大 ⇒ <span class='mj'>1-N</span> 越小 ⇒ 这一项越大 ⇒ 需要更高的工资才愿意</b>。<b>这就是上斜的来源。</b>"),
        ("<span class='mj'>N=1-\\frac{\\theta}{w}</span>", "显式解", "<b>建议直接背</b>。<b><span class='mj'>w=\\theta</span> 时 <span class='mj'>N=0</span></b>（<b>保留工资</b>）；<b><span class='mj'>w\\to\\infty</span> 时 <span class='mj'>N\\to1</span></b>。"),
        ("无财富效应", "no wealth effect", "<b>本页最重要的一句话</b>。<b>收入、股息、利率都不影响 <span class='mj'>N</span></b>。<b>只有 <span class='mj'>w</span> 与 <span class='mj'>\\theta</span> 影响。</b>"),
        ("sweep under the rug", "先搁置细节", "<b>课件原话</b>：<b>「We will sweep most of the details under the rug.」</b><b>意思是「先不管那些复杂的渠道，用一个假设把它们盖住」</b>——<b>这是建模的常规操作，答卷时可以说「本讲用 GHH 回避了收入效应」。</b>"),
    ],
    tip="<b>把推导压缩成三行，考试直接写</b>：<b>① <span class='mj'>u_{C}=1/X,\\ u_{L}=\\theta/(X(1-N))</span>；② 由 <span class='mj'>wu_{C}=u_{L}</span> 得 <span class='mj'>w/X=\\theta/(X(1-N))</span>；③ 约掉 <span class='mj'>X</span> 得 <span class='mj'>\\frac{\\theta}{1-N}=w</span>。</b><b>三行之内既有推导又有结论，而且「约掉 <span class='mj'>X</span>」这一步正好说明「为什么没有财富效应」</b>——<b>这是最划算的写法。</b>",
    warn="<b>四个高频错误</b>：<b>① 说「GHH 让劳动供给与工资无关」</b>（<b>错，只是与收入无关</b>）；<b>② 推导时把 <span class='mj'>u_{L}</span> 写成 <span class='mj'>\\theta/(1-N)</span></b>（<b>漏了 <span class='mj'>1/X</span></b>，<b>那是对 <span class='mj'>\\ln(1-N)</span> 求导、不是对 <span class='mj'>u</span> 求导</b>）；<b>③ 忘记 <span class='mj'>\\ln(1-N)</span> 对 <span class='mj'>N</span> 求导要变号</b>（<b>所以 <span class='mj'>u_{N}&lt;0</span>，最终 <span class='mj'>\\theta/(1-N)=w</span> 是正的</b>）；<b>④ 把 <span class='mj'>\\theta</span> 的符号说反</b>（<b><span class='mj'>\\theta\\uparrow</span> ⇒ <span class='mj'>N\\downarrow</span></b>）。"
)

add(20,
    kp="<b>劳动供给曲线：纵轴 <span class='mj'>w_{t}</span>、横轴 <span class='mj'>N_{t}</span>，向上倾斜</b>。<b>参数 <span class='mj'>\\theta_{t}</span> 上升使整条线右移</b>（<b>同一工资下愿意工作更少 ⇒ 曲线向右下</b>）。<b>与劳动需求曲线的斜率相反，这是「两条线能相交」的前提。</b>",
    plain="工资越高，愿意工作的人越多（因为休息变贵了）。但如果不那么爱工作了（θ 变大），同样的工资他只想干更少——整条线往右推，因为要让他在同一工资下干同样多，得给更高的工资。",
    fig=[
        dict(name="图：劳动供给函数 <span class='mj'>N_{t}=N^{s}(w_{t},\\theta_{t})</span>（纵轴工资、横轴劳动）",
             axes=[("横轴", "N_{t}", "<b>劳动供给（愿意工作多少）</b>"),
                   ("纵轴", "w_{t}", "<b>实际工资</b>——<b>与第 9 页同一套轴</b>，<b>所以两张图可以叠在一起看</b>")],
             marks=[("黑色实线（<b>向上倾斜</b>）", "<b>原状的劳动供给</b>，标注 <span class='mj'>N_{t}=N^{s}(w_{t},\\theta_{t})</span>。<b>斜率来自 <span class='mj'>\\frac{\\theta}{1-N}=w</span></b>：<b><span class='mj'>N</span> 越大 ⇒ <span class='mj'>1-N</span> 越小 ⇒ 需要更高工资</b>。<b>注意它「越往右越陡」</b>（<b>当 <span class='mj'>N\\to1</span> 时工资趋于无穷</b>）"),
                    ("淡蓝色线（在黑线<b>右下方</b>，与原线平行）", "<b>冲击后的劳动供给</b>。<b>还是「右移」</b>（<b>同一工资下供给更多</b>）——<b>但视觉上偏下，因为线是上斜的</b>"),
                    ("淡蓝色<b>水平箭头</b>（黑线 → 蓝线）", "<b>位移方向：右移</b>。<b>与第 9、11 页同一个道理</b>：<b>「右」＝ 同一价格下数量更大</b>；<b>「右下」只是上斜线右移时的视觉结果</b>"),
                    ("淡蓝色小字 <span class='mj'>\\downarrow\\theta</span>", "<b>唯一的触发条件，而且是「下降」</b>。<b><span class='mj'>\\theta\\downarrow</span>（更不爱休息）⇒ 同一工资下愿意多干 ⇒ 右移</b>。<b>注意：三张图里只有这一张的触发条件是「参数下降」</b>")],
             read="<b>读图三步：① 看纵轴</b>——<b><span class='mj'>w</span> 变则沿曲线（工资高多干）；<span class='mj'>\\theta</span> 变则移曲线</b>。<b>② 判断「右移还是左移」</b>——<b>只问「同一工资下，愿意干得更多还是更少」</b>，<b>不要看线的视觉位置</b>。<b>③ 与劳动需求叠在一起</b>——<b>交点就是均衡 <span class='mj'>(N_{t},w_{t})</span></b>（第 22 页）。",
             exam="必考三问：<b>① 为什么上斜？</b>答：<b>只有替代效应</b>——<span class='mj'>w\\uparrow</span> ⇒ 休息变贵 ⇒ 多工作。<b>（关键：要说明「因为没有财富效应，所以不会向后弯」。）</b><b>② <span class='mj'>\\theta\\uparrow</span> 是移动曲线还是沿曲线？</b>答：<b>移动曲线（左移）</b>。<b>③ 这张图与第 9 页能不能叠？</b>答：<b>能，轴完全相同</b>——<b>两条线的交点就是劳动市场均衡</b>。"),
    ],
    note=(
        "这张图有三个地方要盯住：<br><br>"
        "<b>① 为什么它「上斜」而劳动需求「下斜」？</b><b>因为一个是「买」、一个是「卖」</b>：<b>企业买劳动，价格越高买越少；家庭卖劳动，价格越高卖越多</b>。<b>这是供需图的基本逻辑</b>。<b>但要注意：劳动供给的上斜在这里<b>不是</b>「假设」出来的，而是 <span class='mj'>\\theta/(1-N)=w</span> 算出来的</b>——<b>而且它只在 GHH 下成立</b>。<b>一般偏好下它可能向后弯（工资高到一定程度反而少干）</b>，<b>这是本图最容易出的「辨析题」。</b><br><br>"
        "<b>② 为什么蓝线在「右下」而不是「右上」？</b><b>还是那个判断法：取一条水平线（固定 <span class='mj'>w</span>），看交点</b>——<b>蓝线的交点更靠右 ⇒ 供给更多</b>。<b>「右下」只是<b>上斜线右移</b>的视觉结果</b>。<b>第 9 页是下斜线右移，所以看起来「右上」</b>——<b>两张图的「右移」在视觉上方向不同，但含义完全相同。</b><b>这一点特别容易把人绕晕，考试时一定要用「固定价格看数量」来判断。</b><br><br>"
        "<b>③ 为什么三张图里只有这张的触发条件是「下降」？</b><b>因为 <span class='mj'>\\theta</span> 在 <span class='mj'>N^{s}</span> 里是负号</b>（<span class='mj'>N^{s}(w^{+},\\theta^{-})</span>）。<b>「让供给增加」要么让正号变量上升（<span class='mj'>w\\uparrow</span>），要么让负号变量下降（<span class='mj'>\\theta\\downarrow</span>）</b>。<b>这与第 11 页「<span class='mj'>\\downarrow K_{t}</span> 使投资需求右移」是同一个逻辑。</b>"
    ),
    dec=[
        ("<span class='mj'>N^{s}</span> 的正斜率", "供给法则", "<b>价格越高、供给越多</b>。<b>但这里它是「算出来的」，不是假设的。</b>"),
        ("<span class='mj'>\\downarrow\\theta</span>", "更不爱休息", "<b>右移</b>。<b>因为 <span class='mj'>\\theta</span> 在 <span class='mj'>N^{s}</span> 里是负号</b>。<b>「让负号变量下降」＝「供给增加」。</b>"),
        ("越往右越陡", "凸性", "<b><span class='mj'>N\\to1</span> 时 <span class='mj'>w\\to\\infty</span></b>。<b>因为时间上限是 1，最后那点时间「极其贵」</b>——<b>这是一个「资源约束」的表现。</b>"),
        ("与劳动需求叠图", "labor market", "<b>两条线交点 ＝ 均衡 <span class='mj'>(N,w)</span></b>。<b>这是本讲唯一「两条都有斜率」的市场</b>。<b>也是「工资由供需共同决定」的图形表达。</b>"),
    ],
    tip="<b>三张图放在一起看，只记一句判断法</b>：<b>「固定价格（纵轴变量），看横轴数量往哪边变」</b>。<b>数量变大 ＝ 右移</b>。<b>不管线是上斜还是下斜、蓝线画在右上还是右下</b>——<b>这一句能解决全部三张图的「移没移、往哪移」问题。</b>",
    warn="<b>三个高频错误</b>：<b>① 说「蓝线在右下所以是左移」</b>（<b>错，是右移</b>）；<b>② 说「劳动供给一定上斜」而不加限定</b>（<b>只在 GHH 下必然上斜；一般偏好可能向后弯</b>）；<b>③ 把 <span class='mj'>\\theta\\uparrow</span> 说成右移</b>（<b>错，左移</b>）。"
)

add(21,
    kp="<b>银行只做一件事</b>：把家庭的储蓄 <span class='mj'>S_{t}</span> 借给企业 <span class='mj'>B^{I}_{t}</span>。<b>借、贷同一个利率 <span class='mj'>r_{t}</span></b>，所以<b>利润恒为零</b>：<span class='mj'>r_{t}B^{I}_{t}-r_{t}S_{t}=0</span>。<b>结论：银行的所有权无关紧要</b>。",
    plain="银行就是个过路的：左手从储户那儿收钱，右手借给企业，两边利率一样，所以它一分钱不赚。既然不赚钱，谁拥有它都无所谓——所以模型里干脆不把它当决策者。",
    lr=[
        dict(name="银行的利润：为什么必然是零",
             lhs="r_{t}B^{I}_{t}-r_{t}S_{t}",
             lhs_t="<b>利息收入 － 利息支出</b>（<b>股息</b>）",
             rhs="0",
             rhs_t="<b>恒等于零</b>（<b>因为借、贷同利率</b>）",
             why="<b>关键在于「charges the same real interest rate on borrowing and saving」</b>。<b>银行借出去收 <span class='mj'>r</span>、借进来付 <span class='mj'>r</span></b>，<b>利差为零</b>。<b>所以只要 <span class='mj'>B^{I}_{t}=S_{t}</span>（<b>它把收到的钱全部贷出</b>），利润就是零。</b><b>注意这个式子同时也是「可贷资金市场出清」的一种写法</b>——<b>第 22 页会写成 <span class='mj'>S_{t}=B^{I}_{t}=I_{t}</span>。</b>",
             why_t="为什么是零"),
    ],
    note=(
        "这一页很短，但<b>它是「模型能闭合」的关键一步</b>：<br><br>"
        "<b>① 为什么「银行所有权无关」？</b><b>因为它的利润恒为零</b>——<b>零利润的资产，归谁所有都不影响任何人的预算</b>。<b>如果银行有正利润，就必须把「谁拥有银行」写进家庭预算</b>，<b>模型会多一项、多一个假设。</b><br><br>"
        "<b>② 这个「零利润」是假设还是结论？</b><b>是「假设 ＋ 结论」的混合</b>：<b>假设是「借贷同利率、无摩擦」</b>；<b>结论是「利润为零」</b>。<b>现实里银行有「存贷利差」（spread）</b>，<b>所以有正利润</b>。<b>引入 spread 会让模型出现「两个利率」</b>（<span class='mj'>r^{L}&gt;r^{S}</span>），<b>可贷资金市场就不再是「一个价格」，而是「一个区间」</b>——<b>这是「金融摩擦」文献的起点。</b><br><br>"
        "<b>③ 为什么说它「passively earns a dividend」？</b><b>因为它没有主动决策</b>——<b>不选利率、不选数量、不选资产组合</b>。<b>它只是一个「会计科目」</b>：<b>把家庭的 <span class='mj'>S</span> 和企业 <span class='mj'>B^{I}</span> 记账成同一笔钱。</b><b>这就是为什么「银行」这个部门在后面的分析里彻底消失了</b>——<b>它已经完成了它的任务：让「储蓄」能变成「投资」。</b>"
    ),
    dec=[
        ("financial intermediary", "金融中介", "<b>银行</b>。<b>它的功能是「把储蓄接到投资上」</b>。<b>没有它，家庭的 <span class='mj'>S</span> 和企业 <span class='mj'>B^{I}</span> 接不上。</b>"),
        ("same rate", "同一个利率", "<b>无摩擦的核心假设</b>。<b>现实里有存贷利差</b>，<b>那就会有「两个 <span class='mj'>r</span>」</b>。"),
        ("零利润", "zero profit", "<b>完全竞争的金融部门</b>。<b>所以「谁拥有银行」不重要</b>——<b>模型里可以直接忽略它。</b>"),
        ("<span class='mj'>B^{I}_{t}=S_{t}</span>", "中介的平衡", "<b>收到的钱全贷出去</b>。<b>它就是「可贷资金市场出清」的另一种写法。</b>"),
    ],
    tip="<b>答题时如果被问「银行的角色」</b>，<b>一句话答完</b>：<b>「银行把储蓄转成投资，借贷同利率 ⇒ 利润为零 ⇒ 不影响任何均衡量，只提供一个「储蓄＝投资」的通道。」</b><b>不要花篇幅写「银行如何配置资产」——本讲的银行没有这个功能。</b>",
    warn="<b>别把银行的零利润与企业的零利润混为一谈</b>：<b>企业（在 CRS 下）的「经济利润」为零，但「资本收入」<span class='mj'>D</span> 不为零</b>；<b>银行的利润是「真的一分钱都没有」</b>。<b>另一个错误：以为「银行不决策」＝「银行不存在」</b>——<b>它存在，只是没有选择变量。</b>"
)


# ==================== ⑧ 市场出清与均衡定义 ====================

add(22,
    kp="<b>三个市场出清</b>：劳动 <span class='mj'>N^{d}(w_{t},A_{t},K_{t})=N^{s}(w_{t},\\theta_{t})</span>；可贷资金 <span class='mj'>S_{t}=B^{I}_{t}=I_{t}</span>；商品 <span class='mj'>Y_{t}=C_{t}+I_{t}</span>（<b>有政府则加 <span class='mj'>G_{t}</span></b>）。<b>但三个里只有两个独立</b>——<b>瓦尔拉斯定律。</b>",
    plain="三个市场要同时「供需相等」：找工作的人和企业要雇的人一样多；家庭的存款和企业要借的钱一样多；生产出来的东西正好被消费和投资买光。但仔细算会发现，只要前两个平了，第三个自动就平——因为大家花的钱就是大家赚的钱。",
    lr=[
        dict(name="商品市场出清：产出怎么分",
             lhs="Y_{t}",
             lhs_t="<b>本期产出</b>（供给）",
             rhs="C_{t}+I_{t}",
             rhs_t="<b>消费 ＋ 投资</b>（需求）",
             why="<b>为什么它一定成立？</b><b>因为「家庭拿到了全部收入」</b>：<span class='mj'>w_{t}N_{t}+D_{t}=Y_{t}</span>（第 5 页）；<b>而家庭的支出是 <span class='mj'>C_{t}+S_{t}</span></b>。<b>两者相等 ⇒ <span class='mj'>Y_{t}-C_{t}=S_{t}</span></b>。<b>再由可贷资金出清 <span class='mj'>S_{t}=I_{t}</span> ⇒ <b><span class='mj'>Y_{t}=C_{t}+I_{t}</span></b>。</b><b>所以「商品出清」不是一条独立的条件，而是另外两条的推论</b>——<b>这就是瓦尔拉斯定律在本模型里的样子。</b>",
             why_t="为什么它是「自动成立」的"),
    ],
    note=(
        "这一页的关键是<b>「三个里只有两个独立」</b>：<br><br>"
        "<b>① 为什么三个市场只能定两个价格？</b><b>因为经济里只有两个价格需要解</b>：<span class='mj'>w_{t}</span> 与 <span class='mj'>r_{t}</span>。<b>而「商品的价格」被标准化为 1</b>（<b>计价物</b>）——<b>它不需要解</b>。<b>三个市场、两个未知价格 ⇒ 其中一个方程必然冗余。</b><b>这就是瓦尔拉斯定律：<b>「n 个市场里只有 n−1 个独立」</b>。</b><br><br>"
        "<b>② 具体冗余的是哪一个？</b><b>商品市场</b>。<b>因为它的「预算约束来源」已经被劳动市场与可贷资金市场用掉了</b>：<b>家庭的预算约束是「加总」出来的，而它等于「劳动收入 ＝ 消费 ＋ 储蓄」</b>。<b>所以只要劳动市场与可贷资金市场出清，商品市场自动出清。</b><b>这一点在本讲的证明里很干净（见左边「等式两边」）</b>，<b>但考试时容易忘，把三个都当独立条件去数方程，就会「多一个方程」。</b><br><br>"
        "<b>③「<span class='mj'>S_{t}=B^{I}_{t}=I_{t}</span>」为什么写成三段相等？</b><b>因为它是两件事叠在一起</b>：<b>银行把储蓄全贷出（<span class='mj'>S=B^{I}</span>）</b>，<b>企业把借到的全投出去（<span class='mj'>B^{I}=I</span>）</b>。<b>所以「储蓄 ＝ 投资」在本讲是「两个恒等式的传递」</b>，<b>不是「一个新的均衡条件」</b>。<b>这一点与 Topic 5 的 <span class='mj'>S=0</span> 形成鲜明对照</b>——<b>那里「<span class='mj'>S=0</span>」是均衡条件（因为 <span class='mj'>I=0</span> 是设定），这里「<span class='mj'>S=I</span>」是设定的直接结果。</b>"
    ),
    dec=[
        ("劳动市场", "labor market", "<b><span class='mj'>N^{d}=N^{s}</span></b>。<b>解出 <span class='mj'>w_{t}</span> 与 <span class='mj'>N_{t}</span></b>。<b>注意是「一个方程定两个未知数」吗？</b><b>不是——<span class='mj'>N^{d}</span> 与 <span class='mj'>N^{s}</span> 各是一个函数，联立后是一个方程、两个未知数（<span class='mj'>N,w</span>）</b>，<b>但它们都是「同一条 <span class='mj'>N</span>」⇒ 实际上「一个方程、一个未知数（<span class='mj'>w</span>）」</b>，<b>解出 <span class='mj'>w</span> 后 <span class='mj'>N</span> 由任一条曲线给出。</b>"),
        ("可贷资金市场", "loanable funds", "<b><span class='mj'>S=I^{d}</span></b>。<b>解出 <span class='mj'>r_{t}</span></b>。<b>这是本讲的「利率决定」方程</b>——<b>与 Topic 5 的「利率让 <span class='mj'>S=0</span>」完全不同的机制。</b>"),
        ("商品市场", "goods market", "<b><span class='mj'>Y=C+I</span></b>。<b>自动成立</b>（<b>瓦尔拉斯定律</b>）。<b>但它仍然是「产出怎么分」的答案</b>，<b>所以写均衡时不能漏。</b>"),
        ("瓦尔拉斯定律", "Walras' law", "<b>n 个市场只有 n−1 个独立</b>。<b>所以「三条出清条件」实际只提供两条信息</b>。<b>这是「数方程」时最容易多算的地方。</b>"),
        ("有政府", "with government", "<b><span class='mj'>Y=C+I+G</span></b>。<b>本讲不加</b>，<b>但答题时要会加</b>（<b>Topic 6 已做过</b>）。"),
    ],
    tip="<b>「数方程」的正确姿势</b>：<b>先数未知数（6 个）、再数「独立的」方程（5 条）＋ 1 条定义式</b>。<b>如果直接数出「7 条」，说明把「瓦尔拉斯冗余」算进去了</b>。<b>答卷时写一句「由瓦尔拉斯定律，商品市场出清是其余条件的推论」，就能避免这个问题。</b>",
    warn="<b>三个高频错误</b>：<b>① 把三个出清条件都当独立方程</b>（<b>会多算一个</b>）；<b>② 把 <span class='mj'>S=I</span> 当成「新的行为方程」</b>（<b>它是「银行平衡 ＋ 企业融资」的传递</b>）；<b>③ 忘记写「有政府时的 <span class='mj'>G</span>」</b>（<b>题目一旦加政府，出清就变 <span class='mj'>Y=C+I+G</span></b>）。"
)

add(23,
    kp="<b>均衡定义</b>：给定 <span class='mj'>K_{t},A_{t},A_{t+1},\\theta_{t}</span>，均衡是 <b>六个量 <span class='mj'>\\{C_{t},I_{t},N_{t},Y_{t},w_{t},r_{t}\\}</span></b> 满足<b>六个方程</b>：<span class='mj'>C^{d}</span>、<span class='mj'>N^{s}</span>、<span class='mj'>N^{d}</span>、<span class='mj'>I^{d}</span>、生产函数、商品出清。<b>注意 <span class='mj'>Y_{t+1}</span> 是「未来的内生量」，本讲先当给定。</b>",
    plain="把前面所有零件装成一台机器：六个未知数、六个条件。先由劳动市场定出工资和就业，再由生产函数定出产出，再由可贷资金定出利率与投资，最后消费由消费函数给出、产出被分完。",
    note=(
        "这一页是<b>「装配图」</b>，值得按顺序走一遍：<br><br>"
        "<b>① 解的顺序（虽然理论上联立，但直觉上可以这样走）</b>：<br>"
        "· <b>第一步：劳动市场</b>（<span class='mj'>N^{s}=N^{d}</span>）⇒ 定 <span class='mj'>w_{t}</span> 与 <span class='mj'>N_{t}</span>。<b>这是唯一「两条曲线都有斜率」的市场</b>，<b>所以它是「先解」的。</b><br>"
        "· <b>第二步：生产函数</b> ⇒ 定 <span class='mj'>Y_{t}=A_{t}F(K_{t},N_{t})</span>（<b><span class='mj'>K_{t}</span> 预定、<span class='mj'>N_{t}</span> 刚解出</b>）。<br>"
        "· <b>第三步：可贷资金</b>（<span class='mj'>S=I^{d}</span>）⇒ 定 <span class='mj'>r_{t}</span> 与 <span class='mj'>I_{t}</span>。<b>这里 <span class='mj'>S</span> 来自消费函数</b>（<span class='mj'>S=Y-C</span>），<b>而 <span class='mj'>C</span> 又依赖 <span class='mj'>r</span></b>——<b>所以这一步是「自解」的</b>（<b>一个方程一个未知数 <span class='mj'>r</span></b>）。<br>"
        "· <b>第四步：商品出清</b> ⇒ 核对 <span class='mj'>Y=C+I</span> 是否成立（<b>瓦尔拉斯定律保证它成立</b>）。<br><br>"
        "<b>②「<span class='mj'>Y_{t+1}</span> 是未来内生量」这句话的分量</b>：<b>消费函数 <span class='mj'>C^{d}(Y_{t},Y_{t+1},r_{t})</span> 里有 <span class='mj'>Y_{t+1}</span></b>，<b>但本讲的方程组里没有「<span class='mj'>Y_{t+1}</span> 的方程」</b>。<b>所以严格说，这六个方程是在「给定 <span class='mj'>Y_{t+1}</span>」的条件下解的</b>——<b>课件把这叫「future endogenous variable, and we'll talk about it later」。</b><br>"
        "<b>这个「留一个缺口」在方法论上很重要</b>：<b>它是「伪外生」（pseudo-exogenous）</b>——<b>把未来变量当参数，先做「当期」的分析</b>。<b>Topic 8 的两条曲线之所以能画出来，就是靠这个切断</b>（<b>→ [[T8#p8|Topic 8 第 8 页]]</b>）。<b>但代价是：一旦要让 <span class='mj'>Y_{t+1}</span> 也内生，就必须解「两期联立」，反馈回来了。</b><br><br>"
        "<b>③ 外生只有四个：<span class='mj'>K_{t},A_{t},A_{t+1},\\theta_{t}</span></b>。<b>这四个正好对应四种冲击</b>：<b>资本存量、当期技术、预期未来技术、劳动偏好</b>。<b>Topic 8 的「五个冲击」里，前四个就是它们</b>（<b>第五个是货币，Topic 9</b>）。"
    ),
    dec=[
        ("均衡", "equilibrium", "<b>「一组量与一组价格，使所有市场同时出清」</b>。<b>它的定义式就是那六个方程</b>——<b>写答案时按这个清单逐条写，不要漏。</b>"),
        ("<span class='mj'>Y_{t+1}</span>", "未来的产出", "<b>本讲当「给定」</b>。<b>它是「伪外生」</b>——<b>这处「缺口」是 Topic 8 的入口。</b>"),
        ("六个未知数", "six unknowns", "<b><span class='mj'>C,I,N,Y,w,r</span></b>。<b>与「六个方程」一一对应</b>。<b>数量对不上就是漏了条件。</b>"),
        ("四个外生", "four exogenous", "<b><span class='mj'>K_{t},A_{t},A_{t+1},\\theta_{t}</span></b>。<b>四种冲击的载体</b>。<b>答题时先问「题目动的是哪一个」，就知道该动哪条曲线。</b>"),
    ],
    tip="<b>把六个方程抄在一张卡片上，旁边写「各自定谁」</b>：<b><span class='mj'>C^{d}</span>→<span class='mj'>C</span>；<span class='mj'>N^{s},N^{d}</span>→<span class='mj'>N,w</span>；<span class='mj'>I^{d}</span>→<span class='mj'>I,r</span>；生产函数→<span class='mj'>Y</span>；出清→核对</b>。<b>这张卡片是 Topic 8 的全部基础</b>——<b>那里只是把这张卡片画成两条线。</b>",
    warn="<b>三个高频错误</b>：<b>① 漏写商品出清</b>（<b>虽然它冗余，但「均衡定义」里必须有</b>）；<b>② 把 <span class='mj'>Y_{t+1}</span> 当外生参数写进「外生变量清单」</b>（<b>它是「伪外生」，本质内生</b>）；<b>③ 数出「五个方程」</b>（<b>漏了哪条？通常是漏掉 <span class='mj'>N^{s}</span> 或 <span class='mj'>N^{d}</span> 中的一条</b>）。"
)


# ==================== ⑨ 小结：这一讲解锁了什么 ====================

add(24,
    kp="<b>内生六个</b>：<span class='mj'>C_{t},N_{t},I_{t},Y_{t},w_{t},r_{t}</span>；<b>外生四个</b>：<span class='mj'>A_{t},A_{t+1},K_{t},\\theta_{t}</span>。<b>三市场、两价格。</b><b>禀赋经济是「<span class='mj'>N</span> 与 <span class='mj'>I</span> 都固定」的特例</b>。<b>关键解锁：家庭想多储蓄时，只要 <span class='mj'>r</span> 下降激励更多投资就行</b>（<b>禀赋经济里 <span class='mj'>I=0</span>，所以 <span class='mj'>S</span> 只能停在 0</b>）。",
    plain="这一页是全讲的「结算单」。最重要的那一句在最后：以前家庭想多存钱，可存的钱没地方去（没有投资），所以利率只能把它逼回零。现在有了投资，家庭想存、企业想借，利率只要把两边对上就行——储蓄终于有了出口。",
    note=(
        "这一页的最后一段<b>是整讲的点睛</b>，值得逐句拆：<br><br>"
        "<b>①「Suppose household wants to increase <span class='mj'>S_{t}</span>. Can do so if <span class='mj'>r_{t}</span> falls to incentivize more <span class='mj'>I_{t}</span>」</b><br>"
        "<b>这句话说明「储蓄」不再是「必须归零的麻烦」，而是「有用途的资源」</b>。<b>机制</b>：<b>家庭想多存 ⇒ 可贷资金供给上升 ⇒ <span class='mj'>r</span> 下降 ⇒ 企业觉得借钱便宜、多投资 ⇒ 投资需求上升，正好吸收多出来的储蓄</b>。<b>所以 <span class='mj'>S</span> 可以大于零，而且它<b>决定</b>了 <span class='mj'>I</span> 与 <span class='mj'>r</span>。</b><br><br>"
        "<b>②「whereas in endowment economy <span class='mj'>I_{t}=0</span> so <span class='mj'>S_{t}</span> must remain fixed at 0」</b><br>"
        "<b>这是对 [[T5#p20|Topic 5 第 20 页]] 的「回望」</b>：<b>那里没有投资，所以「多存的钱」没有任何出口</b>，<b>唯一能让它消失的办法是让家庭「不想存」</b>——<b>而让家庭不想存的唯一工具就是利率</b>。<b>所以 Topic 5 的利率任务只有一个：把 <span class='mj'>S</span> 逼回零。</b><b>本讲的利率任务变了：让 <span class='mj'>S=I</span>。</b><b>一句话对照：<b>「Topic 5 的利率是「刹车」，Topic 7 的利率是「红娘」。」</b></b><br><br>"
        "<b>③ 为什么说「some consumption smoothing in equilibrium here」？</b><b>因为投资提供了一个「跨期转换技术」</b>：<b>今天少消费、变成资本、明天多产出</b>。<b>所以「平滑」不再受「禀赋固定」的限制</b>——<b>经济可以「今天忍一忍、明天多产一点」。</b><b>这是生产经济与禀赋经济最本质的差别：不只是「多了个市场」，而是「多了一条跨期转换的通道」。</b><br><br>"
        "<b>④ 这一讲给下一讲留下了什么？</b><b>两样东西</b>：<b>① 六个方程（[[T8#p9|Topic 8 第 9 页]]会把它们压成两条曲线）；② <span class='mj'>Y_{t+1}</span> 这个「伪外生」的缺口（Topic 8 会用它画出 <span class='mj'>Y^{s}</span>）。</b><b>所以 Topic 7 是「零件」、Topic 8 是「装配图」。</b>"
    ),
    dec=[
        ("内生 vs 外生", "endogenous vs exogenous", "<b>6 个内生、4 个外生</b>。<b>这个清单要能背</b>——<b>因为「冲击分析」就是「动外生、看内生」。</b>"),
        ("三市场两价格", "three markets, two prices", "<b>劳动（<span class='mj'>w</span>）、可贷资金（<span class='mj'>r</span>）、商品（价格 ＝ 1）</b>。<b>所以「只有两个价格要解」</b>——<b>这是瓦尔拉斯定律的另一种说法。</b>"),
        ("特例", "special case", "<b>禀赋经济 ＝ <span class='mj'>N,I</span> 固定</b>。<b>把这两个「关掉」，本讲就退回 Topic 5</b>。<b>这个「退化关系」是理解两讲关系的钥匙。</b>"),
        ("<span class='mj'>I=0</span> 的后果", "no investment outlet", "<b>储蓄没有出口 ⇒ 必须归零</b>。<b>这是 Topic 5 的「<span class='mj'>S=0</span>」的真正含义</b>——<b>不是「家庭不想存」，而是「存了没处放」。</b>"),
        ("consumption smoothing", "消费平滑", "<b>通过「投资」实现跨期转换</b>。<b>本讲第一次让「平滑」有了技术基础</b>（<b>生产可以把今天的资源变成明天的产出</b>）。"),
    ],
    tip="<b>用一句「对照」结束这一讲</b>：<b>「Topic 5：产出固定、投资为零 ⇒ 利率的任务是让储蓄归零。Topic 7：产出可生产、投资可变 ⇒ 利率的任务是让储蓄等于投资。」</b><b>把这句话写进笔记首页，两讲就再也不会混。</b>",
    warn="<b>三个高频错误</b>：<b>① 说「生产经济里储蓄也必须是零」</b>（<b>错，<span class='mj'>S=I</span> 可以不为零</b>）；<b>② 说「这一讲只是把 Topic 5 加上生产，结论不变」</b>（<b>错，<span class='mj'>S=0</span> 与 <span class='mj'>S=I</span> 是两种完全不同的均衡</b>）；<b>③ 把「三个市场」当成「三个独立方程」</b>（<b>只有两个独立</b>）。"
)


# ============================ 公式速查 ============================
FORMULA_ROWS = [
    ("生产函数",
     "<span class='mj'>Y_{t}=A_{t}F(K_{t},N_{t})</span>",
     "<b>产出从哪来</b>；<span class='mj'>A</span> 在括号外（Hicks 中性）"),
    ("资本积累",
     "<span class='mj'>K_{t+1}=I_{t}+(1-\\delta)K_{t}</span>",
     "正用＝存量演化；反用＝投资需求"),
    ("投资融资",
     "<span class='mj'>I_{t}=B^{I}_{t}</span>",
     "<b>企业只借不存</b>（无摩擦 ＋ MM）"),
    ("第 <span class='mj'>t</span> 期股息",
     "<span class='mj'>D_{t}=Y_{t}-w_{t}N_{t}</span>",
     "经营利润"),
    ("第 <span class='mj'>t+1</span> 期股息",
     "<span class='mj'>D_{t+1}=Y_{t+1}-w_{t+1}N_{t+1}+(1-\\delta)K_{t+1}-(1+r_{t})B^{I}_{t}</span>",
     "<b>四项</b>：经营利润 ＋ 残值 － 还本付息"),
    ("公司价值",
     "<span class='mj'>V_{t}=D_{t}+\\frac{D_{t+1}}{1+r_{t}}</span>",
     "<b>企业的目标函数</b>（不是当期利润）"),
    ("劳动一阶条件（今天）",
     "<span class='mj'>w_{t}=A_{t}F_{N}(K_{t},N_{t})</span>",
     "<b>与 Solow 相同</b>；<span class='mj'>\\mathrm{MPN}</span>"),
    ("劳动一阶条件（明天）",
     "<span class='mj'>w_{t+1}=A_{t+1}F_{N}(K_{t+1},N_{t+1})</span>",
     "形式完全一样，只是下标加一"),
    ("<b>投资一阶条件</b>",
     "<span class='mj'>1+r_{t}=A_{t+1}F_{K}(K_{t+1},N_{t+1})+1-\\delta</span>",
     "<b>两边都是「明年的总金额」</b>"),
    ("投资一阶条件（净形式）",
     "<span class='mj'>r_{t}=\\mathrm{MPK}_{t+1}-\\delta</span>",
     "<b>利率 ＝ 资本的净回报</b>"),
    ("劳动需求函数",
     "<span class='mj'>N_{t}=N^{d}(w_{t}^{-},A_{t}^{+},K_{t}^{+})</span>",
     "<b><span class='mj'>K_{t}</span> 是正号</b>（<span class='mj'>F_{KN}&gt;0</span>）"),
    ("资本需求函数",
     "<span class='mj'>K_{t+1}=K^{d}(r_{t}^{-},A_{t+1}^{+})</span>",
     "目标存量；<b>不含 <span class='mj'>K_{t}</span></b>"),
    ("<b>投资需求函数</b>",
     "<span class='mj'>I_{t}=I^{d}(r_{t}^{-},A_{t+1}^{+},K_{t}^{-})</span>",
     "<b><span class='mj'>K_{t}</span> 是负号！</b>（<span class='mj'>I=K'-（1-\\delta)K</span>）"),
    ("家庭终生效用",
     "<span class='mj'>U=u(C_{t},1-N_{t})+\\beta u(C_{t+1},1-N_{t+1})</span>",
     "消费 ＋ 闲暇；<span class='mj'>\\beta</span> 乘整个第二期"),
    ("<b>GHH 偏好</b>",
     "<span class='mj'>u(C_{t},1-N_{t})=\\ln\\left[C_{t}+\\theta_{t}\\ln(1-N_{t})\\right]</span>",
     "<b>「加」不是「乘」</b>——这是消掉财富效应的关键"),
    ("家庭 IBC",
     "<span class='mj'>C_{t}+\\frac{C_{t+1}}{1+r_{t}}=w_{t}N_{t}+D_{t}+\\frac{w_{t+1}N_{t+1}+D_{t+1}}{1+r_{t}}</span>",
     "两期合成一本账；<span class='mj'>S</span> 被消掉"),
    ("欧拉方程",
     "<span class='mj'>u_{C}(C_{t},1-N_{t})=\\beta(1+r_{t})u_{C}(C_{t+1},1-N_{t+1})</span>",
     "<b>跨期</b>；管消费的时序"),
    ("劳动—闲暇条件",
     "<span class='mj'>w_{t}u_{C}(C_{t},1-N_{t})=u_{L}(C_{t},1-N_{t})</span>",
     "<b>期内</b>；<span class='mj'>u_{C}</span> 是「钱→效用」的换算率"),
    ("消费函数",
     "<span class='mj'>C_{t}=C^{d}(Y_{t}^{+},Y_{t+1}^{+},r_{t}^{-})</span>",
     "<b>与 Topic 4 同一个函数</b>"),
    ("消费函数（有政府）",
     "<span class='mj'>C_{t}=C^{d}(Y_{t}-G_{t},\\ Y_{t+1}-G_{t+1},\\ r_{t})</span>",
     "李嘉图等价 ⇒ 自变量是 <span class='mj'>Y-G</span> 不是 <span class='mj'>Y-T</span>"),
    ("<b>GHH 劳动供给条件</b>",
     "<span class='mj'>\\frac{\\theta_{t}}{1-N_{t}}=w_{t}</span>",
     "<b><span class='mj'>C</span> 消失了</b>——本讲最重要的一行"),
    ("劳动供给函数",
     "<span class='mj'>N_{t}=N^{s}(w_{t}^{+},\\theta_{t}^{-})</span>",
     "<b>只依赖 <span class='mj'>w</span> 与 <span class='mj'>\\theta</span></b>（无财富效应）"),
    ("劳动供给（显式）",
     "<span class='mj'>N_{t}=1-\\frac{\\theta_{t}}{w_{t}}</span>",
     "<b>建议直接背</b>；<span class='mj'>w=\\theta</span> 时 <span class='mj'>N=0</span>"),
    ("银行的零利润",
     "<span class='mj'>r_{t}B^{I}_{t}-r_{t}S_{t}=0</span>",
     "<b>借贷同利率</b> ⇒ 所有权无关"),
    ("劳动市场出清",
     "<span class='mj'>N^{d}(w_{t},A_{t},K_{t})=N^{s}(w_{t},\\theta_{t})</span>",
     "定 <span class='mj'>w_{t}</span> 与 <span class='mj'>N_{t}</span>"),
    ("可贷资金出清",
     "<span class='mj'>S_{t}=B^{I}_{t}=I_{t}</span>",
     "<b>三段相等</b>；定 <span class='mj'>r_{t}</span>"),
    ("商品市场出清",
     "<span class='mj'>Y_{t}=C_{t}+I_{t}</span>",
     "<b>瓦尔拉斯冗余</b>，但必须写进均衡"),
]

# ============================ 总表 ============================
EXTRA_TABLES = [
    dict(
        title="总表 1 · 企业与家庭：两套最优化逐行对照",
        sub="本讲有两个最优化问题，<b>长得不一样，但结构完全对称</b>。<b>把这张表记住，六个方程就不用一条条背。</b>",
        header=["项目", "企业", "家庭"],
        rows=[
            ["<b>决策者身份</b>", "生产者（<b>买</b>劳动、<b>买</b>资本，<b>卖</b>产品）", "消费者 ＋ 劳动者 ＋ 股东（<b>拥有企业</b>）"],
            ["<b>目标函数</b>", "公司价值 <span class='mj'>V_{t}</span>（<b>现值</b>）", "终生效用 <span class='mj'>U</span>"],
            ["<b>约束</b>", "技术 <span class='mj'>Y=AF(K,N)</span> ＋ 资本积累", "跨期预算（<b>IBC</b>）"],
            ["<b>决策变量</b>", "<span class='mj'>N_{t},N_{t+1},K_{t+1}</span>", "<span class='mj'>C_{t},N_{t},N_{t+1}</span>"],
            ["<b>一阶条件个数</b>", "<b>3 个</b>", "<b>3 个</b>"],
            ["<b>劳动条件</b>", "<span class='mj'>w=AF_{N}</span>（<b>工资 ＝ 边际产品</b>）", "<span class='mj'>wu_{C}=u_{L}</span>（<b>工资的效用 ＝ 闲暇的效用</b>）"],
            ["<b>跨期条件</b>", "<span class='mj'>1+r=\\mathrm{MPK}+1-\\delta</span>（<b>资本的净回报 ＝ 利率</b>）", "<span class='mj'>u_{C}=\\beta(1+r)u_{C}'</span>（<b>消费的时序最优</b>）"],
            ["<b>劳动条件的「视角」</b>", "<b>技术侧</b>：多一个人能产多少", "<b>偏好侧</b>：多干一小时有多难受"],
            ["<b>均衡里谁决定 <span class='mj'>N</span> 与 <span class='mj'>w</span></b>", "<b>两条劳动条件联立</b>（<span class='mj'>N^{d}=N^{s}</span>）", "<b>同左</b>"],
            ["<b>谁决定 <span class='mj'>r</span></b>", "<b>投资条件</b>（<span class='mj'>I^{d}</span>）", "<b>欧拉方程</b>（<span class='mj'>S</span>）"],
            ["<b>「价格」的微观含义</b>", "<span class='mj'>w</span> ＝ 劳动的价格；<span class='mj'>r</span> ＝ 资本的价格", "<span class='mj'>w</span> ＝ 闲暇的机会成本；<span class='mj'>r</span> ＝ 今天的消费贵多少"],
        ],
        note="<b>两套条件在劳动市场上「碰头」</b>：<b>企业说「我要雇到 <span class='mj'>w=AF_{N}</span> 为止」，家庭说「我要干到 <span class='mj'>\\frac{\\theta}{1-N}=w</span> 为止」</b>。<b>两条一起解出 <span class='mj'>(N,w)</span>。</b><b>这就是「一般均衡」的第一次真正实现：不是「假设一个工资」，而是「两条独立的规则共同定出工资」。</b>",
        first_col_bold=True,
    ),
    dict(
        title="总表 2 · 三张图的对照（轴、斜率、移动、陷阱）",
        sub="三张图<b>长得像、含义不同</b>。<b>考试最爱考「哪个变量一动，线往哪边移」</b>——这张表就是为此准备的。",
        header=["", "劳动需求（第 9 页）", "投资需求（第 11 页）", "劳动供给（第 20 页）"],
        rows=[
            ["<b>横轴</b>", "<span class='mj'>N_{t}</span>（劳动）", "<span class='mj'>I_{t}</span>（投资）", "<span class='mj'>N_{t}</span>（劳动）"],
            ["<b>纵轴（价格）</b>", "<span class='mj'>w_{t}</span>（工资）", "<span class='mj'>r_{t}</span>（利率）", "<span class='mj'>w_{t}</span>（工资）"],
            ["<b>斜率</b>", "<b>下斜</b>", "<b>下斜</b>", "<b>上斜</b>"],
            ["<b>斜率的来源</b>", "<span class='mj'>F_{NN}&lt;0</span>", "<span class='mj'>F_{KK}&lt;0</span>", "<span class='mj'>\\frac{\\theta}{1-N}=w</span>（<b>只有替代效应</b>）"],
            ["<b>谁来「买卖」</b>", "<b>企业买</b>劳动", "<b>企业借</b>钱（需求）", "<b>家庭卖</b>劳动"],
            ["<b>右移的触发</b>", "<span class='mj'>A_{t}\\uparrow</span>；<span class='mj'>K_{t}\\uparrow</span>", "<span class='mj'>A_{t+1}\\uparrow</span>；<b><span class='mj'>K_{t}\\downarrow</span></b>", "<b><span class='mj'>\\theta_{t}\\downarrow</span></b>"],
            ["<b>陷阱符号</b>", "<span class='mj'>K_{t}</span> <b>正号</b>", "<span class='mj'>K_{t}</span> <b>负号</b>", "触发条件是<b>「下降」</b>"],
            ["<b>视觉位移方向</b>", "<b>右上</b>", "<b>右上</b>", "<b>右下</b>"],
            ["<b>正确的判断法</b>", "固定 <span class='mj'>w</span>，看 <span class='mj'>N</span> 变多吗", "固定 <span class='mj'>r</span>，看 <span class='mj'>I</span> 变多吗", "固定 <span class='mj'>w</span>，看 <span class='mj'>N</span> 变多吗"],
            ["<b>与谁相交</b>", "与<b>劳动供给</b>", "与<b>储蓄</b>（<span class='mj'>S</span>）", "与<b>劳动需求</b>"],
        ],
        note="<b>三张图只有一句通用判断法</b>：<b>「固定纵轴（价格），看横轴（数量）往哪边变：变多就是右移。」</b><b>不管线是上斜还是下斜、蓝线画在右上还是右下，含义都是「同一价格下数量更大」。</b><b>这一句能解决全部「移没移、往哪移」的题。</b>",
        first_col_bold=True,
    ),
    dict(
        title="总表 3 · 禀赋经济 vs 生产经济（Topic 5 vs Topic 7）",
        sub="<b>两讲只差两个设定，结论却完全不同。</b>这张表是本讲最该先看的一张——<b>它回答「为什么还要再学一讲」。</b>",
        header=["项目", "禀赋经济（Topic 5）", "生产经济（Topic 7）"],
        rows=[
            ["<b>产出 <span class='mj'>Y</span></b>", "<b>外生</b>（天上掉下来）", "<b>内生</b>（<span class='mj'>Y=AF(K,N)</span>）"],
            ["<b>劳动 <span class='mj'>N</span></b>", "<b>固定</b>", "<b>内生</b>（<span class='mj'>N^{d}=N^{s}</span>）"],
            ["<b>投资 <span class='mj'>I</span></b>", "<b>恒为零</b>", "<b>内生</b>（<span class='mj'>I^{d}</span>）"],
            ["<b>储蓄 <span class='mj'>S</span></b>", "<b>必须为零</b>（无处可去）", "<b>＝ 投资</b>（有出口）"],
            ["<b>利率的任务</b>", "<b>把储蓄逼回零</b>（「刹车」）", "<b>让储蓄 ＝ 投资</b>（「红娘」）"],
            ["<b>利率的决定</b>", "<span class='mj'>S=0</span>（<b>一个方程、一个未知数</b>）", "<span class='mj'>S=I^{d}</span>（<b>供需相交</b>）"],
            ["<b>价格个数</b>", "<b>1 个</b>（<span class='mj'>r</span>）", "<b>2 个</b>（<span class='mj'>w,r</span>）"],
            ["<b>市场个数</b>", "<b>1 个</b>（可贷资金）", "<b>3 个</b>（劳动／可贷资金／商品）"],
            ["<b>政府支出乘数</b>", "<b>0</b>（完全挤出）", "<b>为正</b>（<b>产出能变</b>）"],
            ["<b>消费平滑</b>", "<b>受禀赋限制</b>（不能跨期转换）", "<b>可通过投资实现</b>（今天少花→明天多产）"],
            ["<b>退化关系</b>", "—", "<b>把 <span class='mj'>N,I</span> 固定，就退回 Topic 5</b>"],
        ],
        note="<b>两讲的「物理差别」只有一条：有没有「投资」这个跨期转换技术。</b><b>没有它，储蓄是「无处安放的钱」，只能逼回零</b>；<b>有了它，储蓄变成「明天的产能」，<span class='mj'>S=I</span> 可以大于零。</b><b>所以 Topic 5 的所有「反直觉结论」（乘数为零、完全挤出）都来自「<span class='mj'>I=0</span>」这一个设定</b>——<b>而不是来自「家庭前瞻」。</b>",
        first_col_bold=True,
    ),
]

# ============================ 概念速查 ============================
SUMMARY_ROWS = [
    ("生产函数", "<span class='mj'>Y_{t}=A_{t}F(K_{t},N_{t})</span>", "<b>产出从哪来</b>；<span class='mj'>A</span> 乘在外面（Hicks 中性）"),
    ("七条假设", "必需性 / CRS / 单调 / 递减 / 交叉正", "<b>每组买来一个结论</b>（见第 3 页）"),
    ("CRS", "<span class='mj'>F(\\gamma K,\\gamma N)=\\gamma F(K,N)</span>", "<b>欧拉定理</b> ⇒ 经济利润为零 ⇒ <b>股息 ＝ 资本收入</b>"),
    ("<span class='mj'>F_{KK}&lt;0</span>", "资本边际递减", "<b>投资需求下斜</b>的原因"),
    ("<span class='mj'>F_{NN}&lt;0</span>", "劳动边际递减", "<b>劳动需求下斜</b>的原因"),
    ("<span class='mj'>F_{KN}&gt;0</span>", "资本—劳动互补", "<b><span class='mj'>K_{t}\\uparrow</span> ⇒ 劳动需求右移</b>的唯一依据"),
    ("predetermined", "预定", "<b><span class='mj'>K_{t}</span> 今天改不了</b> ⇒ 「短期」的定义"),
    ("资本积累", "<span class='mj'>K_{t+1}=I_{t}+(1-\\delta)K_{t}</span>", "正用＝演化；反用＝<b>投资需求</b>"),
    ("投资融资", "<span class='mj'>I_{t}=B^{I}_{t}</span>", "企业<b>只借不存</b>（无摩擦 ＋ MM）"),
    ("股息 <span class='mj'>D_{t}</span>", "<span class='mj'>Y_{t}-w_{t}N_{t}</span>", "经营利润；<b>归家庭</b>"),
    ("股息 <span class='mj'>D_{t+1}</span>", "经营利润 ＋ 残值 － 还本付息", "<b>四项，残值最易漏</b>"),
    ("公司价值 <span class='mj'>V_{t}</span>", "<span class='mj'>D_{t}+D_{t+1}/(1+r_{t})</span>", "<b>企业的目标</b>（不是当期利润）"),
    ("劳动 FOC", "<span class='mj'>w_{t}=A_{t}F_{N}</span>", "<b>与 Solow 相同</b>"),
    ("投资 FOC", "<span class='mj'>1+r_{t}=\\mathrm{MPK}+1-\\delta</span>", "<b>两边都是「明年的总金额」</b>"),
    ("净形式", "<span class='mj'>r_{t}=\\mathrm{MPK}-\\delta</span>", "<b>无套利</b>：资本净回报 ＝ 利率"),
    ("劳动需求", "<span class='mj'>N^{d}(w^{-},A^{+},K^{+})</span>", "<b><span class='mj'>K</span> 正号</b>"),
    ("投资需求", "<span class='mj'>I^{d}(r^{-},A'^{+},K^{-})</span>", "<b><span class='mj'>K</span> 负号</b>（重置效应）"),
    ("「右移」的判断", "固定价格、看数量", "<b>数量变多 ＝ 右移</b>（三张图通用）"),
    ("效用", "<span class='mj'>u(C_{t},1-N_{t})+\\beta u(C_{t+1},1-N_{t+1})</span>", "<b>时间禀赋标准化为 1</b>"),
    ("<span class='mj'>u_{L}&gt;0</span>", "闲暇边际效用为正", "<b>等价于 <span class='mj'>\\partial u/\\partial N&lt;0</span></b>（链式法则带负号）"),
    ("GHH", "<span class='mj'>\\ln[C+\\theta\\ln(1-N)]</span>", "<b>「加」不是「乘」</b>；<b>先加再取对数</b>"),
    ("GHH 的作用", "消掉劳动供给的财富效应", "<b>只剩替代效应</b> ⇒ 供给必然上斜"),
    ("<span class='mj'>\\theta_{t}</span>", "闲暇权重", "<b><span class='mj'>\\theta\\uparrow</span> ⇒ <span class='mj'>N\\downarrow</span></b>（劳动供给左移）"),
    ("GHH 下的劳动 FOC", "<span class='mj'>\\frac{\\theta}{1-N}=w</span>", "<b><span class='mj'>C</span> 约掉了</b>——本讲最重要一行"),
    ("劳动供给（显式）", "<span class='mj'>N=1-\\theta/w</span>", "<span class='mj'>w=\\theta</span> 时 <span class='mj'>N=0</span>（<b>保留工资</b>）"),
    ("欧拉方程", "<span class='mj'>u_{C}=\\beta(1+r)u_{C}'</span>", "<b>跨期</b>；管消费时序"),
    ("劳动—闲暇条件", "<span class='mj'>wu_{C}=u_{L}</span>", "<b>期内</b>；不含 <span class='mj'>\\beta</span>"),
    ("<span class='mj'>u_{C}</span> 的作用", "「钱 → 效用」的换算率", "<b>为什么工资要乘它</b>"),
    ("消费函数", "<span class='mj'>C^{d}(Y_{t},Y_{t+1},r_{t})</span>", "<b>与 Topic 4 同一个</b>"),
    ("银行", "<span class='mj'>rB^{I}-rS=0</span>", "<b>零利润</b> ⇒ 所有权无关"),
    ("三个市场", "劳动／可贷资金／商品", "<b>只有两个独立</b>（瓦尔拉斯）"),
    ("两个价格", "<span class='mj'>w_{t},r_{t}</span>", "<b>商品价格 ＝ 1</b>（计价物）"),
    ("六个内生", "<span class='mj'>C,I,N,Y,w,r</span>", "<b>六个方程</b>"),
    ("四个外生", "<span class='mj'>K_{t},A_{t},A_{t+1},\\theta_{t}</span>", "<b>四种冲击</b>的载体"),
    ("<span class='mj'>Y_{t+1}</span>", "「伪外生」", "<b>本讲当给定</b>；<b>Topic 8 的入口</b>"),
    ("与 Topic 5 的差别", "<span class='mj'>S=0</span> vs <span class='mj'>S=I</span>", "<b>储蓄有没有出口</b>"),
    ("利率的任务", "Topic 5「刹车」／Topic 7「红娘」", "<b>逼回零</b> vs <b>让 <span class='mj'>S=I</span></b>"),
]

# ============================ 易错清单 ============================
PITFALLS = [
    ("把企业 TFP <span class='mj'>A_{t}</span> 与资本 <span class='mj'>K_{t}</span> 混为「都是投入」",
     "<span class='mj'>A_{t}</span> 是<b>模型外</b>的技术；<span class='mj'>K_{t}</span> 是<b>模型内</b>的状态变量<b>判据：</b><b>问「冲击是什么」时，只有 <span class='mj'>A</span> 与 <span class='mj'>\\theta</span> 是「真外生」</b>"),
    ("说「CRS 意味着企业利润为零所以企业无所谓」",
     "<b>经济利润为零</b>，但<b>资本收入 <span class='mj'>D</span> 不为零</b><b>判据：</b><b>企业仍然最大化 <span class='mj'>V_{t}</span></b>；<b>零的是「超额利润」</b>"),
    ("漏掉 <span class='mj'>D_{t+1}</span> 里的残值 <span class='mj'>(1-\\delta)K_{t+1}</span>",
     "<b>最后一期要「清算」</b>，机器残值归股东<b>判据：</b><b>漏掉它 = 让企业免费扔机器 = 投资激励全错</b>"),
    ("把还贷写成 <span class='mj'>r_{t}B^{I}_{t}</span>",
     "<b>是「还本付息」<span class='mj'>(1+r_{t})B^{I}_{t}</span></b><b>判据：</b><b>两期模型没有分期还款</b>"),
    ("投资条件里丢了 <span class='mj'>\\delta</span>（写成 <span class='mj'>r=\\mathrm{MPK}</span>）",
     "<b><span class='mj'>r+\\delta=\\mathrm{MPK}</span></b>，或 <span class='mj'>r=\\mathrm{MPK}-\\delta</span><b>判据：</b><b>资本的「使用成本」＝ 利息 ＋ 折旧</b>"),
    ("把投资条件写成 <span class='mj'>r_{t}=A_{t+1}F_{K}+1-\\delta</span>",
     "<b>左边应是 <span class='mj'>1+r_{t}</span></b>（<b>两边都是总金额</b>）<b>判据：</b><b>减 1 之后才是 <span class='mj'>r=\\mathrm{MPK}-\\delta</span></b>"),
    ("劳动条件里加了 <span class='mj'>\\beta</span>",
     "<b>今天雇人／今天工作是「同一期内」</b>，不折现<b>判据：</b><b>只有「今天 vs 明天」才乘 <span class='mj'>\\beta</span></b>"),
    ("把 <span class='mj'>K_{t}</span> 在两张图里都写成同一符号",
     "<b>劳动需求：正号</b>；<b>投资需求：负号</b><b>判据：</b><b>原因不同</b>：<span class='mj'>F_{KN}&gt;0</span> vs <span class='mj'>I=K'-(1-\\delta)K</span> 的减号"),
    ("把 <span class='mj'>K^{d}</span> 与 <span class='mj'>I^{d}</span> 混为一谈",
     "<b><span class='mj'>K^{d}</span> 是「目标存量」，<span class='mj'>I^{d}</span> 是「本期流量」</b><b>判据：</b><b>二者差 <span class='mj'>(1-\\delta)K_{t}</span></b>"),
    ("把投资需求写成依赖 <span class='mj'>A_{t}</span>",
     "<b>依赖 <span class='mj'>A_{t+1}</span></b><b>判据：</b><b>今天买的机器明天才产 ⇒ 投资看未来</b>"),
    ("说「技术进步使劳动需求沿曲线向上移动」",
     "<b>移动曲线（右移）</b><b>判据：</b><b>只有纵轴变量变才「沿曲线」</b>"),
    ("把「<span class='mj'>\\downarrow K_{t}</span> 使投资需求右移」说成左移",
     "<b>右移</b>（<b>重置投资</b>效应）<b>判据：</b><b>判断法：固定 <span class='mj'>r</span>，看 <span class='mj'>I</span> 变多吗</b>"),
    ("把 GHH 写成 <span class='mj'>\\ln C+\\theta\\ln(1-N)</span>",
     "<b>GHH 是 <span class='mj'>\\ln[C+\\theta\\ln(1-N)]</span></b>（<b>先加再取对数</b>）<b>判据：</b><b>「对数可加」没有「消掉 <span class='mj'>C</span>」的性质</b>"),
    ("说「GHH 让劳动供给与工资无关」",
     "<b>只是与「收入」无关</b>，<b>仍然依赖工资</b><b>判据：</b><b><span class='mj'>N=1-\\theta/w</span> 里明明白白有 <span class='mj'>w</span></b>"),
    ("说「劳动供给一定上斜」而不加限定",
     "<b>只在 GHH 下必然上斜</b>；一般偏好可能「向后弯」<b>判据：</b><b>因为一般偏好有收入效应</b>"),
    ("把 <span class='mj'>\\theta\\uparrow</span> 说成劳动供给右移",
     "<b>左移</b>（<b>更爱休息 ⇒ 同一工资下干得更少</b>）<b>判据：</b><b><span class='mj'>\\theta</span> 在 <span class='mj'>N^{s}</span> 里是负号</b>"),
    ("把三个市场出清都当独立方程",
     "<b>只有两个独立</b>（<b>瓦尔拉斯定律</b>）<b>判据：</b><b>商品市场出清是其余条件的推论</b>"),
    ("说「生产经济里储蓄也必须是零」",
     "<b><span class='mj'>S=I</span>，可以大于零</b><b>判据：</b><b><span class='mj'>S=0</span> 只是「<span class='mj'>I=0</span>」这个特例的结果</b>"),
    ("把这一讲结论直接套到「有政府」的情形",
     "<b>加 <span class='mj'>G</span> 后乘数不为零</b>（<b>产出能变</b>）<b>判据：</b><b>Topic 6 的「乘数为零」是禀赋经济的结论，不是本讲的</b>"),
    ("忘记 <span class='mj'>u_{L}</span> 与 <span class='mj'>u_{N}</span> 的符号关系",
     "<span class='mj'>\\frac{\\partial u}{\\partial N}=-u_{L}</span><b>判据：</b><b>链式法则里 <span class='mj'>\\partial(1-N)/\\partial N=-1</span></b>"),
]

# ============================ 自测 ============================
QUIZ = [
    ("本讲相比 Topic 5 的两个扩展是什么？各带来哪条新方程？",
     "<b>① 内生生产 ＋ 企业问题</b>：带来<b>生产函数 <span class='mj'>Y=AF(K,N)</span></b>、<b>两条劳动需求条件</b>、<b>一条投资条件</b>（⇒ <span class='mj'>N^{d}</span> 与 <span class='mj'>I^{d}</span>）。<br>"
     "<b>② 内生劳动供给</b>：带来<b>效用函数</b>与<b>劳动—闲暇条件</b>（⇒ <span class='mj'>N^{s}</span>）。<br>"
     "<b>一句话</b>：<b>产出不再外生，劳动不再固定</b>——<b>所以从「一个市场一个价格」变成「三个市场两个价格」。</b>"),
    ("写出企业的三个一阶条件，并说明每个的「边际成本」与「边际收益」分别是什么。",
     "<b>① <span class='mj'>w_{t}=A_{t}F_{N}</span></b>：MC ＝ 工资 <span class='mj'>w</span>；MB ＝ 劳动的边际产品。<br>"
     "<b>② <span class='mj'>w_{t+1}=A_{t+1}F_{N}</span></b>：<b>明天的同一条</b>。<br>"
     "<b>③ <span class='mj'>1+r_{t}=A_{t+1}F_{K}+1-\\delta</span></b>：MC ＝ <b>借一块的总成本</b> <span class='mj'>1+r</span>；MB ＝ <b>买一单位资本的总回报</b>（<b>边际产品 ＋ 残值</b>）。<br>"
     "<b>要点</b>：<b>第三个条件的「总 vs 净」最容易错</b>——<b>两边都是「明年的总金额」，同时减 1 才得 <span class='mj'>r=\\mathrm{MPK}-\\delta</span></b>。"),
    ("为什么投资需求依赖于 <span class='mj'>A_{t+1}</span> 而不是 <span class='mj'>A_{t}</span>？为什么 <span class='mj'>K_{t}</span> 在投资需求里是负号、在劳动需求里是正号？",
     "<b>① 下标问题</b>：<b>今天买的机器明天才产出</b> ⇒ <b>决定它值不值的是「明天的技术」</b> ⇒ <b>依赖 <span class='mj'>A_{t+1}</span></b>。<b>这是「投资看未来」的形式化。</b><br>"
     "<b>② 符号问题</b>：<br>"
     "· <b>劳动需求</b>：<b><span class='mj'>K_{t}</span> 是「搭档」</b>——<b>机器多则工人好使（<span class='mj'>F_{KN}&gt;0</span>）</b> ⇒ <b>同一工资下多雇人</b> ⇒ <b>正号</b>。<br>"
     "· <b>投资需求</b>：<b><span class='mj'>K_{t}</span> 是「已有的存货」</b>——<b>目标 <span class='mj'>K_{t+1}</span> 定了，旧的多就少买（<span class='mj'>I=K'-(1-\\delta)K</span>）</b> ⇒ <b>负号</b>。<br>"
     "<b>一句话</b>：<b>同一个 <span class='mj'>K_{t}</span>，一处是「生产上的互补品」，一处是「账上的减项」。</b>"),
    ("完整推出 GHH 下的劳动供给条件 <span class='mj'>\\frac{\\theta}{1-N}=w</span>，并说明为什么「财富效应消失了」。",
     "记 <span class='mj'>X=C+\\theta\\ln(1-N)</span>，<span class='mj'>u=\\ln X</span>。<br>"
     "<b>① <span class='mj'>u_{C}=1/X</span></b>。<br>"
     "<b>② <span class='mj'>u_{L}=\\frac{\\theta}{X}\\cdot\\frac{1}{1-N}</span></b>（<b>外层 <span class='mj'>1/X</span>，内层对 <span class='mj'>\\ln(1-N)</span> 求导</b>）。<br>"
     "<b>③ 由 <span class='mj'>wu_{C}=u_{L}</span></b>：<span class='mj'>\\frac{w}{X}=\\frac{\\theta}{X(1-N)}</span>。<br>"
     "<b>④ 约掉 <span class='mj'>X</span></b> ⇒ <b><span class='mj'>\\frac{\\theta}{1-N}=w</span></b>。<br>"
     "<b>为什么没有财富效应</b>：<b>因为劳动的边际替代率 <span class='mj'>\\frac{u_{L}}{u_{C}}=\\frac{\\theta}{1-N}</span> 不含 <span class='mj'>C</span></b>。<b>「变富」不会改变「工作多少」</b> ⇒ <b>只剩替代效应</b>。<b>关键就在「括号里是加号」</b>。"),
    ("三张图（劳动需求、投资需求、劳动供给）的「右移」分别由什么触发？为什么图上有的画在右上、有的画在右下？",
     "<b>① 劳动需求右移</b>：<span class='mj'>A_{t}\\uparrow</span> 或 <span class='mj'>K_{t}\\uparrow</span>（<b>都是「劳动的边际产品上升」</b>）。<br>"
     "<b>② 投资需求右移</b>：<span class='mj'>A_{t+1}\\uparrow</span> 或 <b><span class='mj'>K_{t}\\downarrow</span></b>（<b>注意后者是「下降」</b>）。<br>"
     "<b>③ 劳动供给右移</b>：<b><span class='mj'>\\theta_{t}\\downarrow</span></b>（<b>更不爱休息</b>）。<br>"
     "<b>视觉差异的原因</b>：<b>「右移」的定义是「同一价格下数量更大」</b>。<b>在「价格纵、数量横」的图里，下斜线右移看起来偏右上、上斜线右移看起来偏右下</b>。<b>所以不能看线的位置，要「固定纵轴、看横轴」</b>。"),
    ("禀赋经济里「储蓄必须为零」，生产经济里「储蓄等于投资」。这两个结论的差别从哪里来？",
     "<b>从「有没有投资这个跨期转换技术」来</b>。<br>"
     "· <b>禀赋经济</b>：<b><span class='mj'>I=0</span></b> ⇒ <b>家庭想多存，钱没地方去</b> ⇒ <b>只能靠利率把它逼回零</b> ⇒ <b><span class='mj'>S=0</span></b>。<b>利率是「刹车」。</b><br>"
     "· <b>生产经济</b>：<b><span class='mj'>I^{d}</span> 存在</b> ⇒ <b>家庭想多存 ⇒ <span class='mj'>r</span> 下降 ⇒ 企业多借多投</b> ⇒ <b><span class='mj'>S=I</span> 且可以大于零</b>。<b>利率是「红娘」。</b><br>"
     "<b>所以结论的差别不是「家庭变不变聪明」，而是「经济里有没有第二条跨期通道」。</b>"),
    ("银行在本讲里做了什么？为什么说「它的所有权无关」？",
     "<b>它只做一件事：把家庭的 <span class='mj'>S_{t}</span> 借给企业 <span class='mj'>B^{I}_{t}</span>，借贷同利率 <span class='mj'>r_{t}</span>。</b><br>"
     "<b>于是利润 <span class='mj'>r_{t}B^{I}_{t}-r_{t}S_{t}=0</span></b>——<b>恒为零</b>。<br>"
     "<b>所有权无关的理由</b>：<b>零利润资产归谁所有，都不改变任何人的预算</b>。<b>如果银行有正利润，就必须把「谁拥有银行」写进家庭预算</b>，<b>模型会多一项、多一个假设</b>。<b>现实里有存贷利差 ⇒ 有正利润 ⇒ 就是「金融摩擦」的起点。</b>"),
    ("写出均衡的六个方程与六个未知数，并说明为什么「商品市场出清」不是独立条件。",
     "<b>六个方程</b>：<span class='mj'>C_{t}=C^{d}(Y_{t},Y_{t+1},r_{t})</span>；<span class='mj'>N_{t}=N^{s}(w_{t},\\theta_{t})</span>；<span class='mj'>N_{t}=N^{d}(w_{t},A_{t},K_{t})</span>；<span class='mj'>I_{t}=I^{d}(r_{t},A_{t+1},K_{t})</span>；<span class='mj'>Y_{t}=A_{t}F(K_{t},N_{t})</span>；<span class='mj'>Y_{t}=C_{t}+I_{t}</span>。<br>"
     "<b>六个未知数</b>：<span class='mj'>C_{t},I_{t},N_{t},Y_{t},w_{t},r_{t}</span>。<br>"
     "<b>商品出清为何冗余</b>：<b>由家庭预算 <span class='mj'>wN+D=Y</span> 与 <span class='mj'>C+S=wN+D</span> 得 <span class='mj'>Y-C=S</span></b>；<b>再由 <span class='mj'>S=I</span> 得 <span class='mj'>Y=C+I</span></b>。<b>所以它是「预算约束 ＋ 可贷资金出清」的推论</b>——<b>瓦尔拉斯定律：n 个市场只有 n−1 个独立。</b>"),
    ("「<span class='mj'>Y_{t+1}</span> 是未来的内生变量」这句话，对后面一讲（Topic 8）有什么用？",
     "<b>它意味着本讲的六个方程是在「给定 <span class='mj'>Y_{t+1}</span>」下解的</b>——<b>这是一种「伪外生」（pseudo-exogenous）处理</b>：<b>把未来变量当参数，先切断反馈</b>。<br>"
     "<b>Topic 8 正是靠这个切断，才画出两条静态曲线</b>：<b>IS 曲线（给定 <span class='mj'>Y_{t+1}</span>，看 <span class='mj'>r</span> 与 <span class='mj'>Y_{t}</span> 的关系）</b> 与 <b><span class='mj'>Y^{s}</span> 曲线（给定 <span class='mj'>K,A,\\theta</span>）</b>。<br>"
     "<b>代价</b>：<b>一旦要让 <span class='mj'>Y_{t+1}</span> 也内生，「当期分析」就不成立</b>——<b>反馈回来了，必须解两期联立。</b>"),
    ("如果题目问「本讲与 Topic 6 的乘数结论是否矛盾」，怎么答？",
     "<b>不矛盾，因为世界不同。</b><br>"
     "· <b>Topic 6（禀赋经济）</b>：<b>产出固定</b> ⇒ 政府多占一块，私人只能少一块 ⇒ <b>乘数为零、完全挤出</b>。<b>那里的「零」是「<span class='mj'>Y</span> 不能变」的功劳，<b>不是李嘉图等价</b>。</b><br>"
     "· <b>Topic 7（生产经济）</b>：<b>产出可以变</b>（<span class='mj'>N</span> 可调、<span class='mj'>K</span> 可积累）⇒ <b>政府支出能通过「多雇人、多投资」抬高产出</b> ⇒ <b>乘数为正</b>。<br>"
     "<b>所以答题顺序是</b>：<b>先声明「在哪个经济里」→ 再说「产出能不能变」→ 最后给乘数</b>。<b>漏掉第一步，结论就一定是错的。</b>"),
]









# ===== 考点标注：供 build_notes.py 渲染「页首徽标 + 本讲考点一览」=====
# k: final = 期末练习 Key Concepts（老师亲手划）／mid = 期中练习 Key Concepts
#    must  = 我横向整理判断的必背项（没有老师名录背书）
EXAM = {
    3:  [{"k": "final", "t": "企业的目标／选择／给定（对照家庭那张表背）", "ref": "q3b"}],
    6:  [{"k": "final", "t": "企业最大化现值 <span class='mj'>V_{t}</span>：三个决策变量", "ref": "q3b"}],
    7:  [{"k": "final", "t": "三个一阶条件：两个劳动需求 ＋ 一个投资需求", "ref": "q2d"}],
    8:  [{"k": "final", "t": "劳动需求 <span class='mj'>N^{d}</span> 的三个偏导符号", "ref": "q2c"}],
    10: [{"k": "final", "t": "投资需求 <span class='mj'>I^{d}</span>：<span class='mj'>K_{t}</span> 带负号（重置效应）", "ref": "q2c"}],
    15: [{"k": "final", "t": "家庭的目标／选择／给定（与企业的三行对照）", "ref": "q3b"}],
    16: [{"k": "final", "t": "家庭三个一阶条件：欧拉 ＋ 两个劳动条件", "ref": "q3d"}],
    17: [{"k": "final", "t": "三个一阶条件怎么读：左边＝右边各是什么", "ref": "q3d"}],
    18: [{"k": "final", "t": "消费函数 <span class='mj'>C^{d}</span> 的三个偏导符号", "ref": "q3c"}],
    19: [{"k": "final", "t": "GHH 让劳动供给只看工资、不看收入", "ref": "q3c"}],
    21: [{"k": "final", "t": "银行只做一件事：S 借给企业，利差为零", "ref": "q3b"}],
    22: [{"k": "final", "t": "三个市场出清 ⇒ 两个就够（Walras 定律）", "ref": "q3b"}],
    23: [{"k": "final", "t": "均衡定义：六个内生量的联立", "ref": "q3a"}],
    24: [{"k": "final", "t": "六个内生／六个外生，<span class='mj'>Y_{t+1}</span> 是伪外生", "ref": "q3a"}],
}
