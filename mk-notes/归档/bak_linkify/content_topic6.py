# -*- coding: utf-8 -*-
"""
AF5638 Macroeconomics · Topic 6 内容文件
Fiscal Policy and Ricardian Equivalence（GLS Ch. 13）

写作原则（与 Topic 1/2/3/4/5/8/9/10 一致）：
  1) 每页先给「白话」；
  2) 再给「讲解」，把推导的每一步摊开；
  3) 凡有公式的页，「等式两边」说清左右各是什么、为什么相等；
  4) 凡有图的页，「这张图怎么看」说清坐标轴、每条线、怎么读、会怎么考。

本讲特点：它只有<b>一个</b>新主角（政府），却衍生出<b>三个</b>容易混的数字——
  乘数 = 1（有李嘉图等价、r 固定）
  乘数 = 1/(1-MPC)（无李嘉图等价、r 固定）
  乘数 = 0（一般均衡、产出不能变）
  把这三个数字分清楚，这一讲就通了。
"""

COURSE      = "AF5638 宏观经济学 · Macroeconomics"
TOPIC       = 6
TOPIC_TITLE = "Topic 6 · 财政政策与李嘉图等价"
SUBTITLE    = "政府多花一块钱，私人消费就少一块钱：为什么「怎么融资」不重要，「花多少」才重要"
INSTRUCTOR  = "讲师：Elaine Liu（PolyU）· Fall 2026"
SOURCES     = "课件：Topic 6 - Fiscal Policy（20 页）· 教材：GLS Ch. 13"
SLIDE_COUNT = 20

MAP_CHIPS = [
    ("Topic 1 · 增长事实", False, False),
    ("Topic 2–3 · Solow", False, False),
    ("Topic 4–7 · 跨期模型", True, True),
    ("Topic 8 · 新古典实物侧", False, False),
    ("Topic 9 · 新古典名义侧", False, False),
    ("Topic 10 · 新凯恩斯", False, False),
]

SECTIONS = [
    ("① 这一讲要回答什么", 2),
    ("② 政府的两期预算", 3),
    ("③ 家庭：税进来之后", 5),
    ("④ 把政府塞进家庭（税消失）", 8),
    ("⑤ 直觉与李嘉图等价", 10),
    ("⑥ 一般均衡：出清与两条方程", 13),
    ("⑦ 乘数：三种口径", 15),
    ("⑧ 图形与挤出", 18),
]

TLDR = [
    "<b>财政政策 ＝ 政府支出 <span class='mj'>G</span> ＋ 税收／转移支付 <span class='mj'>T</span></b>。这一讲在<b>禀赋经济</b>里做，所以产出还是给定的。",
    "<b>李嘉图等价</b>：政府<b>怎么融资</b>（发债还是征税）<b>不影响均衡</b>。因为<b>今天的债 ＝ 明天的税</b>，而家庭是前瞻的。<b>只有 <span class='mj'>G</span> 的路径重要，<span class='mj'>T</span> 与 <span class='mj'>B</span> 都不重要。</b>",
    "技术上只有一步：<b>把政府 IBC 代进家庭 IBC</b>，<b>税就消失了</b>，消费函数变成 <span class='mj'>C_{t}=C^{d}(Y_{t}-G_{t},\\ Y_{t+1}-G_{t+1},\\ r_{t})</span>。",
    "<b>三个乘数必须分清</b>：有 RE ＋ <span class='mj'>r</span> 固定 ⇒ <b>1</b>；无 RE ＋ <span class='mj'>r</span> 固定 ⇒ <b><span class='mj'>1/(1-\\mathrm{MPC})</span></b>；<b>一般均衡（产出固定）⇒ 0</b>。",
    "<b>挤出（crowding out）</b>：<span class='mj'>G_{t}\\uparrow</span> ⇒ <span class='mj'>Y_{t}</span> 不变 ⇒ <b><span class='mj'>C_{t}</span> 一比一地下降</b>（<span class='mj'>dC_{t}=-dG_{t}</span>），同时 <b><span class='mj'>r</span> 上升</b>。",
    "<b>但「乘数为零」不是李嘉图等价的功劳</b>，而是<b>禀赋经济（产出不能变）</b>的功劳。<b>这两件事一定要分开说</b>——这是本讲最高频的扣分点。",
]

# ==================== 符号表 ====================
NOTATION = [
    ("一、政府这一侧（本讲新加的三个符号）", [
        ("<span class='mj'>G_{t},\\ G_{t+1}</span>", "政府支出", "<b>外生给定</b>（本讲不解释政府为什么这么花）。<b>它才是「财政政策」的主角</b>——所有结论都绕着它转。"),
        ("<span class='mj'>T_{t},\\ T_{t+1}</span>", "税收（可为负）", "<b><span class='mj'>T&gt;0</span> 是征税，<span class='mj'>T&lt;0</span> 是转移支付</b>。<b>它最终会被证明「不重要」</b>——但推导过程中必须先留着。"),
        ("<span class='mj'>B_{t}</span>", "政府债务（可为负）", "<b><span class='mj'>B_{t}&gt;0</span> 是发债，<span class='mj'>B_{t}&lt;0</span> 是政府储蓄</b>。<b>注意记号与家庭相反</b>：家庭 <span class='mj'>S&gt;0</span> 是存钱，政府 <span class='mj'>B&gt;0</span> 是借钱。"),
        ("<span class='mj'>B_{t+1}</span>", "第二期债务", "<b>不存在</b>。因为没有第三期，政府必须在 <span class='mj'>t+1</span> 期<b>还清全部债务</b>。<b>这就是「为什么不写 <span class='mj'>B_{t+1}</span>」的答案</b>。"),
    ]),
    ("二、家庭这一侧（与上一讲的区别只有一个）", [
        ("可支配收入", "disposable income", "<b><span class='mj'>Y_{t}-T_{t}</span></b>。<b>本讲唯一改动的地方</b>：家庭的约束从「收入」变成「税后收入」。<b>其余全部照搬 Topic 4/5。</b>"),
        ("<span class='mj'>C^{d}(\\cdot)</span>", "消费函数", "自变量从 <span class='mj'>Y</span> 变成 <b><span class='mj'>Y-T</span></b>；再往下会变成 <b><span class='mj'>Y-G</span></b>。<b>三次变形，一条主线。</b>"),
        ("<span class='mj'>h(G)</span>", "从政府支出得到的效用", "<b>「政府修路我也受益」的写法</b>。本讲<b>直接丢掉</b>，理由是可加可分（additively separable）。<b>丢掉的后果要知道</b>：G 不再直接进入偏好，只通过预算约束起作用。"),
        ("<span class='mj'>S_{t}</span>", "家庭储蓄", "<b>仍然是可正可负</b>。但本讲多了一个「对手方」——<b>政府也在借</b>。"),
    ]),
    ("三、市场出清（本讲最容易记错的一个式子）", [
        ("<span class='mj'>S_{t}-B_{t}=0</span>", "「总量储蓄」为零", "<b>家庭储蓄 ＝ 政府借款</b>。<b>注意不是 <span class='mj'>S_{t}=0</span></b>——上一讲没有政府，所以是 <span class='mj'>S=0</span>；<b>这一讲政府的赤字必须由家庭储蓄来吸收</b>。"),
        ("<span class='mj'>Y_{t}=C_{t}+G_{t}</span>", "商品市场出清", "<b>产出分成私人消费与政府消费</b>。<b>这是本讲所有结论的入口</b>——因为 <span class='mj'>Y_{t}</span> 固定，所以 <b><span class='mj'>G</span> 涨一块，<span class='mj'>C</span> 就得少一块</b>。"),
        ("乘数（multiplier）", "<span class='mj'>dY_{t}/dG_{t}</span>", "<b>政府多花一块，产出多多少</b>。<b>本讲有三个不同的答案</b>（1 / <span class='mj'>1/(1-\\mathrm{MPC})</span> / 0），取决于<b>两个开关</b>：有没有李嘉图等价、<span class='mj'>r</span> 动不动。"),
        ("挤出（crowding out）", "<span class='mj'>dC_{t}=-dG_{t}</span>", "<b>政府花的那一块，正好是私人少花的那一块</b>。<b>在产出固定的经济体里，这是恒等式级别的结论</b>。"),
    ]),
]

HOWTO_READ = [
    ("① 先分清「谁的钱」", "本讲有三个预算：<b>政府的</b>（<span class='mj'>G=T+B</span>）、<b>家庭的</b>（<span class='mj'>C+S=Y-T</span>）、<b>合起来的</b>（<span class='mj'>Y=C+G</span>）。<b>大部分错误来自把三者混用。</b>"),
    ("② 再盯住「哪个变量没了」", "推导的主线是<b>一路消元</b>：先消 <span class='mj'>B</span>（得政府 IBC），再消 <span class='mj'>T</span>（用政府 IBC 代进家庭 IBC）。<b>最后只剩 <span class='mj'>G</span></b>。看到「税消失了」这四个字，就知道走到本讲的核心了。"),
    ("③ 遇到乘数，先问两个开关", "<b>开关一：有没有李嘉图等价？</b>有 ⇒ 家庭把 <span class='mj'>G</span> 的上涨当成「自己要多交税」，消费先掉 <span class='mj'>\\mathrm{MPC}\\cdot dG</span>。<b>开关二：<span class='mj'>r</span> 动不动？</b>固定 ⇒ 局部均衡；会动 ⇒ 一般均衡（乘数变 0）。<b>两个开关组合出三个答案。</b>"),
    ("④ 最后看「谁被挤出去了」", "产出固定时，<span class='mj'>G</span> 多占一块，<span class='mj'>C</span> 必然少一块。<b>但价格（<span class='mj'>r</span>）必须动，才能让家庭「甘心」少花</b>——<span class='mj'>G_{t}\\uparrow</span> 抬利率，<span class='mj'>G_{t+1}\\uparrow</span> 压利率。<b>方向可以用「政府借得多不多」一句话判断。</b>"),
]

# ============================ 逐页讲解 ============================
C = {}
def add(p, **kw):
    C[p] = kw


# ==================== ① 这一讲要回答什么 ====================

add(1,
    kp="本讲把<b>政府</b>塞进上一讲的禀赋经济：政府要花 <span class='mj'>G</span>，钱从<b>征税 <span class='mj'>T</span></b> 或<b>发债 <span class='mj'>B</span></b> 来。核心结论是<b>李嘉图等价</b>——<b>怎么融资不影响均衡，只有花多少才影响</b>。",
    plain="政府要花钱，钱可以现在收税，也可以先借、以后再收税。这一讲要证明一件很反直觉的事：这两种做法对经济的影响<b>完全一样</b>。因为老百姓不傻——你今天少收我一块钱税、多借一块钱，我知道明天你还是要多收我一块（还要加利息），所以我今天就把这块省下来，一分钱都不多花。",
    note=(
        "先把这一讲的<b>地图</b>画出来，后面每一页都在这张图上：<br><br>"
        "<b>① 加一个主角</b>：政府。它有两个政策工具（<span class='mj'>G</span> 与 <span class='mj'>T</span>）和一个融资工具（<span class='mj'>B</span>）。<br>"
        "<b>② 加一个约束</b>：政府也要遵守跨期预算（它不能永远借新还旧）。<br>"
        "<b>③ 加一个出清条件</b>：家庭的储蓄必须等于政府的借款（<span class='mj'>S_{t}=B_{t}</span>，而不是上一讲的 <span class='mj'>S_{t}=0</span>）。<br><br>"
        "<b>结论只有两条</b>：<br>"
        "· <b>李嘉图等价</b>：<span class='mj'>T</span> 与 <span class='mj'>B</span> 怎么分配<b>无关紧要</b>，只有 <span class='mj'>G</span> 的路径重要。<br>"
        "· <b>乘数与挤出</b>：<span class='mj'>G</span> 上升会在一般均衡里把 <span class='mj'>C</span> <b>一比一地挤出去</b>，所以<b>均衡乘数为零</b>。<br><br>"
        "注意第二条<b>不是</b>李嘉图等价的推论，而是<b>禀赋经济（产出不能变）</b>的推论。<b>这两件事在答卷上必须分开说</b>——第 20 页会正面强调。"
    ),
    tip="这一讲的所有推导其实是<b>同一个动作</b>：消元。<b>先消 <span class='mj'>B</span>（得政府 IBC），再消 <span class='mj'>T</span>（代进家庭约束）。</b>消完之后，模型里只剩 <span class='mj'>G</span>。<b>「税消失了」就是这个动作的产物，不是额外假设。</b>",
    warn="别把「李嘉图等价」记成「财政政策没用」。它只说<b>融资方式没用</b>，<b>没说政府支出没用</b>。<span class='mj'>G</span> 上升<b>照样有影响</b>（挤出一比一的私人消费）。<b>「融资无关」与「支出无关」是两句话。</b>"
)

add(2,
    kp="<b>财政政策 ＝ 政府支出 ＋ 税收／转移支付</b>。在<b>禀赋经济</b>里研究，基本结论可推广到有生产的经济。核心结果是<b>李嘉图等价</b>（Ricardian equivalence），另加一个<b>政府支出乘数</b>。",
    plain="这一页在交代「我们要研究什么、在什么环境里研究、结论有多硬」。环境很简单：产出还是天上掉下来的（禀赋经济），所以能动的只有利率和消费的分配。",
    note=(
        "三句话把这页读透：<br><br>"
        "<b>① 为什么在禀赋经济里做？</b>因为<b>产出固定</b>，所以「政府多花一块、私人少花一块」这件事会被<b>逼到明面上</b>（<span class='mj'>Y=C+G</span>）。如果产出能变，政府支出会同时触发「产出上升」，挤出就被稀释，机制反而看不清。<b>先在最干净的设定里看清机制，是这门课一贯的做法。</b><br><br>"
        "<b>② 李嘉图等价说的到底是什么？</b>原文：<b>「政府如何为其支出融资（发债还是征税），对于理解支出变化的均衡效应是无关的。」</b>注意它<b>限定在「支出变化」</b>——不是「所有财政政策」，也不是「税收政策」。<b>它比较的是同一个 <span class='mj'>\\{G_{t},G_{t+1}\\}</span> 下的两种融资方式。</b><br><br>"
        "<b>③ 为什么说它「不是一般结论」？</b>因为它依赖四个强假设（第 12 页会逐条列）。<b>但即使假设不成立，它仍是一个极好的基准（benchmark）</b>——你先知道「如果家庭完全前瞻会怎样」，才能判断现实偏离了多少。<b>「基准 + 偏离」是宏观答题的标准句式。</b>"
    ),
    dec=[
        ("fiscal policy", "财政政策", "<b>政府的「收入」与「支出」</b>：<span class='mj'>G</span>（支出）与 <span class='mj'>T</span>（税收／转移）。<b>注意不包括货币政策（那是利率，Topic 9/10）。</b>"),
        ("Ricardian equivalence", "李嘉图等价", "<b>融资方式无关</b>。名字来自 David Ricardo，<b>由 Barro (1974) 正式化</b>。<b>两个人名都要会写。</b>"),
        ("multiplier", "乘数", "<b><span class='mj'>dY/dG</span></b>。<b>本讲要给出三个不同的值</b>——这是最容易混的地方。"),
        ("endowment economy", "禀赋经济", "<b>产出外生</b>。<b>这是「均衡乘数为零」的真正原因</b>，不是李嘉图等价。"),
    ],
    tip="这一讲可以看成<b>上一讲的「补丁包」</b>：只加了一个主体（政府）、改了一个约束（<span class='mj'>Y=C+G</span>）、改了一个出清条件（<span class='mj'>S=B</span>）。<b>凡是上一讲会的，这一讲只需要问「多了个 <span class='mj'>G</span> 会怎样」。</b>",
    warn="别把「李嘉图等价」当成「政府支出无效」。<b>它恰恰是关于「支出变化的效应与融资方式无关」</b>——支出本身当然有效应（挤出）。<b>答题时先复述这句原文，再展开，能避免九成的误答。</b>"
)


# ==================== ② 政府的两期预算 ====================

add(3,
    kp="政府支出 <span class='mj'>G_{t},G_{t+1}</span> <b>外生给定</b>。政府与家庭一样，面对<b>两条流量预算约束</b>：<span class='mj'>G_{t}=T_{t}+B_{t}</span>（今天：支出＝税收＋发债）、<span class='mj'>G_{t+1}+(1+r_{t})B_{t}=T_{t+1}</span>（明天：支出＋还本付息＝税收）。",
    plain="政府今天要花的钱，要么现在收税，要么先借。借的钱明年要连本带利还，而明年还钱只能靠明年收税——因为明年是最后一期，不能再借了。",
    lr=[
        dict(name="政府第 t 期的流量约束（今天）",
             lhs="G_{t}",
             lhs_t="今天要花的钱（<b>外生给定</b>）",
             rhs="T_{t}+B_{t}",
             rhs_t="<b>两个来源</b>：征税 ＋ 发债。<b><span class='mj'>B_{t}&gt;0</span> 是借钱，<span class='mj'>B_{t}&lt;0</span> 是政府存钱</b>",
             why="这就是「政府的钱包」：<b>花出去的必须等于收进来的加借来的</b>。它与家庭的 <span class='mj'>C_{t}+S_{t}=Y_{t}</span> 结构完全相同，<b>只是「储蓄」换成了「负的债务」</b>。",
             why_t="为什么相等"),
        dict(name="政府第 t+1 期的流量约束（明天）",
             lhs="G_{t+1}+(1+r_{t})B_{t}",
             lhs_t="明天的支出 ＋ <b>还本付息</b>（<span class='mj'>1</span> 是本金、<span class='mj'>r</span> 是利息）",
             rhs="T_{t+1}",
             rhs_t="<b>只能靠征税</b>——因为<b>没有第三期，不能再发 <span class='mj'>B_{t+1}</span></b>",
             why="<b>这就是「为什么不写 <span class='mj'>B_{t+1}</span>」的答案</b>：两期世界里的最后一期<b>必须清零债务</b>。这在一般情形下叫<b>横截条件／无庞氏条件</b>（no-Ponzi condition）——政府不能靠永远借新还旧活下去。",
             why_t="为什么右边没有 B"),
    ],
    note=(
        "两个符号的<b>正负号约定</b>要记牢，本讲后面会反复用：<br><br>"
        "<b><span class='mj'>B_{t}&gt;0</span>：政府债务（政府向家庭借钱）</b>；<span class='mj'>B_{t}&lt;0</span>：政府储蓄（政府借钱给家庭）。<br>"
        "<b><span class='mj'>T_{t}&gt;0</span>：征税</b>；<span class='mj'>T_{t}&lt;0</span>：转移支付（政府给家庭钱）。<br><br>"
        "<b>注意与家庭的记号「反着来」</b>：家庭 <span class='mj'>S_{t}&gt;0</span> 是<b>把钱借出去</b>，政府 <span class='mj'>B_{t}&gt;0</span> 是<b>把钱借进来</b>。<b>这不是笔误，而是因为它们是同一笔借贷的两端</b>——家庭存的钱正是政府借的钱。<b>记住这一点，第 13 页的出清条件就顺理成章：<span class='mj'>S_{t}=B_{t}</span>。</b>"
    ),
    dec=[
        ("<span class='mj'>G_{t}</span>", "政府支出", "<b>外生</b>。本讲<b>不解释</b>政府为什么这么花，只研究「它变了会怎样」。<b>这就是「政策冲击」的处理方式：把政策变量当外生。</b>"),
        ("<span class='mj'>T_{t}</span>", "税收", "<b>正 = 征税，负 = 转移支付</b>。<b>它是「融资工具」之一，不是「政策目标」</b>——因为李嘉图等价会说它最终会被抵消。"),
        ("<span class='mj'>B_{t}</span>", "政府债务", "<b>正 = 借，负 = 存</b>。<b>它与家庭储蓄是同一枚硬币的两面</b>。<b>不要独立地看它，要看「谁借给谁」。</b>"),
        ("<span class='mj'>(1+r_{t})B_{t}</span>", "还本付息", "<b>本利和</b>。<b>漏掉那个 1 是致命错误</b>——它意味着政府只还利息不还本金，债务永远滚下去。"),
    ],
    tip="把政府想成<b>「另一个家庭」</b>，只是它的「收入」是税收、「消费」是政府支出、「储蓄」是负的债务。<b>两套约束的结构一模一样</b>——这就是为什么下一页的 IBC 可以照抄家庭的做法。",
    warn="<b>第二期不能有 <span class='mj'>B_{t+1}</span>。</b>这是「两期模型」的硬约束，不是简化的偷懒。<b>如果题目给你三期，最后一期同样要清零债务</b>——<b>「最后一期不许借」是所有跨期模型的通用条件</b>。答「因为模型只有两期」要给分，答「因为政府不能永远借新还旧」给满分。"
)

add(4,
    kp="把 <span class='mj'>B_{t}</span> 从两条流量约束里<b>消掉</b>，得政府 IBC：<b><span class='mj'>G_{t}+\\frac{G_{t+1}}{1+r_{t}}=T_{t}+\\frac{T_{t+1}}{1+r_{t}}</span></b>。<b>与家庭 IBC 概念上完全相同</b>。",
    plain="把两期合成一条：政府一辈子花的钱的现值，等于一辈子收的税的现值。借钱只是把征税的时间往后挪，挪不动总量。",
    lr=[
        dict(name="政府跨期预算约束（政府 IBC）",
             lhs="G_{t}+\\frac{G_{t+1}}{1+r_{t}}",
             lhs_t="政府<b>一生支出的现值</b>",
             rhs="T_{t}+\\frac{T_{t+1}}{1+r_{t}}",
             rhs_t="政府<b>一生税收的现值</b>",
             why="<b>推导</b>：由第一期 <span class='mj'>B_{t}=G_{t}-T_{t}</span>，代入第二期 <span class='mj'>G_{t+1}+(1+r_{t})B_{t}=T_{t+1}</span>，得 <span class='mj'>G_{t+1}+(1+r_{t})(G_{t}-T_{t})=T_{t+1}</span>；两边同除 <span class='mj'>(1+r_{t})</span> 并移项即得。<b>注意 <span class='mj'>B_{t}</span> 被彻底消掉了——融资方式不进入这条式子，这就是李嘉图等价的代数根源。</b>",
             why_t="怎么推出来的"),
    ],
    note=(
        "三个要点：<br><br>"
        "<b>① 「消掉 <span class='mj'>B_{t}</span>」这个动作本身就是结论的一半。</b>它说明：<b>给定 <span class='mj'>G</span> 的路径，<span class='mj'>T</span> 的路径不能随便选</b>——必须满足现值相等。<b>也就是说，减税必须用未来的增税补回来，且要按 <span class='mj'>1+r</span> 补。</b><br><br>"
        "<b>② 它与家庭 IBC 结构完全相同</b>：左边「一生花掉的现值」，右边「一生资源的现值」。<b>唯一的区别是家庭可以「不花完」（留下遗产），而这里假设两期花完。</b><br><br>"
        "<b>③ 这条式子是「政府不能赖账」的数学表达</b>。如果政府想靠永远借新还旧（庞氏骗局）过日子，这条就不成立。<b>在有限期模型里，它必须成立；在无限期模型里，它作为一个「不能违反的极限条件」被加进去。</b>"
    ),
    dec=[
        ("<span class='mj'>\\frac{1}{1+r_{t}}</span>", "折现因子", "<b>把明年的钱折成今天的</b>。<b>为什么除而不是乘</b>：明年的 1 块等于今年的 <span class='mj'>1/(1+r)</span> 块——<b>未来的钱「更轻」</b>。"),
        ("现值（PDV）", "present discounted value", "把不同时点的钱换算到<b>同一个时点</b>再比较。<b>跨期模型里所有的「相等」都是现值相等</b>，不是名义值相等。"),
        ("消去 <span class='mj'>B_{t}</span>", "关键动作", "<b>融资方式从式子里消失了</b>。<b>这是李嘉图等价的第一层证据</b>——不是经济学直觉，而是代数事实。"),
    ],
    tip="政府 IBC 与家庭 IBC 是<b>同一个模板</b>：<b>左边「一生用途的现值」＝ 右边「一生来源的现值」</b>。家庭的用途是消费、来源是收入；政府的用途是支出、来源是税收。<b>把这个模板套熟，后面 Topic 7 的企业、开放经济都能直接用。</b>",
    warn="<b>别把政府 IBC 写成 <span class='mj'>G_{t}=T_{t}</span>（每期平衡）。</b>它只要求<b>一生</b>平衡，<b>完全允许某一年大赤字</b>。<b>「跨期」的全部意思就是把两期合成一条</b>——这一点与家庭 IBC 完全一样（Topic 4 的同一个坑）。"
)


# ==================== ③ 家庭：税进来之后 ====================

add(5,
    kp="代表性家庭的终身效用 <span class='mj'>U=u(C_{t})+\\beta u(C_{t+1})+h(G_{t})+\\beta h(G_{t+1})</span>。<b>只要偏好「可加可分」，<span class='mj'>h(\\cdot)</span> 那两项就可以丢掉</b>——<b>政府支出不直接影响消费决策</b>。",
    plain="政府修路、办学校，老百姓确实受益。所以我们「礼貌地」把这份好处写进效用函数里。但因为这个好处和「我今天吃多少」是分开的两块（没有互相影响），所以它对「我今天吃多少」的决定没有任何影响——于是我们就把它划掉了。",
    note=(
        "这一段是本讲<b>最容易讲不清、也最容易考</b>的地方，值得慢慢说：<br><br>"
        "<b>① <span class='mj'>h(G)</span> 是什么？</b>是「政府支出给我带来的效用」。课件称它为 <b>a cheap way to model usefulness of government spending</b>——<b>便宜</b>，因为它承认了「G 有用」，但又不至于让模型复杂到要讨论「公共品与私人品是替代还是互补」。<br><br>"
        "<b>② 为什么能丢？</b>因为<b>可加可分（additively separable）</b>：<span class='mj'>U</span> 里没有 <span class='mj'>C</span> 与 <span class='mj'>G</span> 的交叉项。<b>丢掉的后果是：<span class='mj'>\\partial U/\\partial C</span> 不依赖 <span class='mj'>G</span></b> ⇒ 欧拉方程里<b>不会出现 <span class='mj'>G</span></b> ⇒ <b><span class='mj'>G</span> 只能通过预算约束影响消费</b>。<br><br>"
        "<b>③ 如果不能丢会怎样？</b>如果 <span class='mj'>C</span> 与 <span class='mj'>G</span> 是<b>替代品</b>（政府多修路，我就少买车），那么 <span class='mj'>G</span> 上升会<b>直接压低消费的边际效用</b>，欧拉方程就变了，结论也会变。<b>课件明确说：只要可加可分，「家庭从 G 得到效用的方式」对均衡动态无关紧要。</b><br><br>"
        "<b>一句话：丢掉 <span class='mj'>h(\\cdot)</span> 不是「假设政府没用」，而是「假设它不与私人消费相互作用」。</b>"
    ),
    dec=[
        ("<span class='mj'>h(\\cdot)</span>", "政府支出的效用函数", "<b>「G 也有用」的写法</b>。<b>与 <span class='mj'>u(\\cdot)</span> 并列、互不影响</b>——这就是可加可分。"),
        ("additively separable", "可加可分", "<b>没有交叉项</b>。<b>它的作用是让「消费的边际效用」不依赖 <span class='mj'>G</span></b> ⇒ 欧拉方程干净。<b>这是丢掉 <span class='mj'>h</span> 的唯一理由。</b>"),
        ("为何可以忽略", "why ignore", "<b>不影响一阶条件</b>：<span class='mj'>h(G)</span> 对 <span class='mj'>C_{t}</span> 求导为零，所以最优化结果里不会出现它。<b>它是「常数项」，不影响选择。</b>"),
        ("代表性家庭", "representative household", "沿用上一讲：<b>所有人一样</b>，所以可以当成一个家庭。<b>代价仍然是没有异质性（借不到钱的人）</b>——第 12 页会用它来质疑李嘉图等价。"),
    ],
    tip="把 <span class='mj'>h(G)</span> 想成<b>「背景音乐」</b>：它让你更舒服，但不改变你「吃多少」的选择。<b>只有当音乐大到影响你吃饭的胃口（<span class='mj'>C</span> 与 <span class='mj'>G</span> 有交叉项）时，才会改变结论。</b>",
    warn="<b>别把「忽略 <span class='mj'>h</span>」理解成「政府支出没有福利价值」。</b>它在效用函数里存在过，只是<b>不影响边际决策</b>。<b>如果考试问「这个假设的经济含义」，答「公共品与私人品可加可分，因此政府支出不改变消费的边际效用」。</b>"
)

add(6,
    kp="有了税，家庭的流量约束变成 <b><span class='mj'>C_{t}+S_{t}=Y_{t}-T_{t}</span></b> 与 <b><span class='mj'>C_{t+1}=Y_{t+1}-T_{t+1}+(1+r_{t})S_{t}</span></b>；<b>家庭把 <span class='mj'>T_{t},T_{t+1},r_{t},Y_{t},Y_{t+1}</span> 全部当作给定</b>。",
    plain="跟上一讲比，只改一个地方：收入要扣掉税。家庭看到的是「税后收入」，税是外面给的——它改变不了，只能接受。",
    lr=[
        dict(name="家庭第 t 期流量约束（加入税收）",
             lhs="C_{t}+S_{t}",
             lhs_t="消费 ＋ 储蓄（<b>税后收入的两个去处</b>）",
             rhs="Y_{t}-T_{t}",
             rhs_t="<b>可支配收入</b>（disposable income）",
             why="与 Topic 4 的唯一区别：右边从 <span class='mj'>Y_{t}</span> 变成 <span class='mj'>Y_{t}-T_{t}</span>。<b>其余全部照搬</b>。<b>这个「减一个 T」的小改动，是整讲所有结论的入口。</b>",
             why_t="为什么相等"),
        dict(name="家庭 IBC（加入税收之后）",
             lhs="C_{t}+\\frac{C_{t+1}}{1+r_{t}}",
             lhs_t="一生消费的现值",
             rhs="(Y_{t}-T_{t})+\\frac{Y_{t+1}-T_{t+1}}{1+r_{t}}",
             rhs_t="<b>一生可支配收入的现值</b>",
             why="推导方式与 Topic 4 完全相同：由第二期解出 <span class='mj'>S_{t}</span> 代进第一期。<b>只是每一期的收入都减掉了那一期的税。</b>",
             why_t="怎么来的"),
    ],
    note=(
        "两个要点：<br><br>"
        "<b>① 「税」进入了两个地方，但只进入一次。</b>它进入第一期（<span class='mj'>Y_{t}-T_{t}</span>）和第二期（<span class='mj'>Y_{t+1}-T_{t+1}</span>），<b>但两处都是「减」，而它不进入利率、不进入价格</b>。<b>这说明税在这里的作用是纯粹的「收入转移」，不是「价格扭曲」</b>——因为它是<b>一次性总付税（lump-sum tax）</b>，不随行为变。<b>第 12 页会把这条列为李嘉图等价的关键假设。</b><br><br>"
        "<b>② 家庭把 <span class='mj'>T</span> 当给定，但它知道政府 IBC 必须成立。</b>这个区别是<b>整讲的关键</b>：单个家庭无法影响税收，但它<b>知道</b>「今天少收的税，明天一定要多收」。<b>所以它会把未来的税折现，算进今天的一生财富。</b><br><br>"
        "下一节（第 8 页）就是<b>把这个「知道」写进约束</b>。"
    ),
    dec=[
        ("<span class='mj'>Y_{t}-T_{t}</span>", "可支配收入", "<b>税后收入</b>。<b>家庭真正能支配的钱</b>。<b>注意税率不是比例税，而是「减一个数」</b>——这就是 lump-sum。"),
        ("lump-sum tax", "一次性总付税", "<b>不管你干什么都要交同样多</b>，所以<b>不扭曲行为</b>。<b>如果换成比例税 <span class='mj'>\\tau Y</span>，结论会变</b>（因为会扭曲劳动／储蓄）。"),
        ("「当作给定」", "take as given", "<b>单个家庭改变不了税</b>。但它<b>可以预判</b>税的未来路径——<b>「不能改变」≠「不知道」</b>。"),
    ],
    tip="家庭这边<b>只需要记住一句话</b>：<b>「约束里凡是 <span class='mj'>Y</span> 的地方，都换成 <span class='mj'>Y-T</span>」</b>。<b>欧拉方程完全不变</b>——因为税不进入边际条件（lump-sum）。",
    warn="<b>别在欧拉方程里加 <span class='mj'>T</span>。</b>欧拉方程只含边际量（<span class='mj'>u^{\\prime}</span>），税是「一次性拿走一笔」，<b>不改变消费的边际效用</b>，所以欧拉方程<b>一个字都不用改</b>。<b>这是 lump-sum 税最方便的地方</b>，也是它「不扭曲」的含义。"
)

add(7,
    kp="最优化：<b>欧拉方程与上一讲完全相同</b>（<span class='mj'>u^{\\prime}(C_{t})=\\beta(1+r_{t})u^{\\prime}(C_{t+1})</span>）；<b>消费函数只是把收入换成可支配收入</b>：<span class='mj'>C_{t}=C^{d}(Y_{t}-T_{t},\\ Y_{t+1}-T_{t+1},\\ r_{t})</span>。",
    plain="解法和上一讲一模一样，只是把「收入」替换成「税后收入」。所以税后收入涨，消费就涨；税后收入跌，消费就跌。",
    lr=[
        dict(name="消费函数（第三次变形，先换成可支配收入）",
             lhs="C_{t}",
             lhs_t="今天消费",
             rhs="C^{d}(Y_{t}-T_{t},\\ Y_{t+1}-T_{t+1},\\ r_{t})",
             rhs_t="三个自变量：<b>两期可支配收入</b> ＋ 利率",
             why="把 Topic 4 的结论<b>逐项替换</b>：<span class='mj'>Y_{t}\\to Y_{t}-T_{t}</span>、<span class='mj'>Y_{t+1}\\to Y_{t+1}-T_{t+1}</span>。<b>函数形式不变、欧拉方程不变</b>——因为税是一次性总付的。<b>这一步只是「换记号」，第 9 页才会真正变。</b>",
             why_t="为什么只是换记号"),
    ],
    note=(
        "这一页是<b>过渡页</b>，但它埋了一个非常重要的伏笔：<br><br>"
        "<b>消费对两个税都敏感</b>：<span class='mj'>\\partial C_{t}/\\partial T_{t}&lt;0</span>（今天多交税 ⇒ 今天少花）、<span class='mj'>\\partial C_{t}/\\partial T_{t+1}&lt;0</span>（明天多交税 ⇒ 今天也少花，<b>前瞻性</b>）。<br><br>"
        "<b>但这两个「敏感」会在第 9 页被一起消灭。</b>怎么消灭的？不是靠「家庭不敏感了」，而是靠<b>把 <span class='mj'>T</span> 换成 <span class='mj'>G</span></b>：<b>税变了，说明 <span class='mj'>G</span> 或 <span class='mj'>B</span> 变了；而给定 <span class='mj'>G</span>，税的路径被政府 IBC 完全钉死。</b><br><br>"
        "<b>所以「税消失」不是「税不重要」，而是「税被 <span class='mj'>G</span> 完全决定了，所以不该出现在最终的决策规则里」。</b>这句话是本讲的核心，值得抄在笔记上。"
    ),
    dec=[
        ("欧拉方程", "Euler equation", "<b>与 Topic 4 完全一样</b>。<b>为什么？因为税是 lump-sum，不改变边际效用。</b>"),
        ("<span class='mj'>\\partial C_{t}/\\partial T_{t}&lt;0</span>", "今天加税的效应", "<b>可支配收入↓ ⇒ 消费↓</b>。<b>这是「直觉版」</b>，第 9 页会看到它在均衡里被抵消。"),
        ("<span class='mj'>\\partial C_{t}/\\partial T_{t+1}&lt;0</span>", "明天加税的效应", "<b>前瞻性</b>：未来的税也压低今天的消费，因为一生财富变少。<b>李嘉图等价全靠这一条。</b>"),
    ],
    tip="<b>「欧拉方程不变」这件事本身就是一个结论</b>：它说明<b>一次性总付税不影响跨期的最优配置</b>，只影响「能花多少」。<b>如果税是比例税，欧拉方程就会带上税率</b>——那时候李嘉图等价就破了。",
    warn="<b>别把 <span class='mj'>\\partial C_{t}/\\partial T_{t}&lt;0</span> 当成最终结论。</b>它只在「其他不变」的偏导意义上成立。<b>在均衡里，减税同时意味着未来增税，两者正好抵消——净效应为零。</b>第 10 页会用数字算给你看。"
)


# ==================== ④ 把政府塞进家庭（税消失） ====================

add(8,
    kp="把家庭 IBC 里的税收项<b>单独括出来</b>，再用<b>政府 IBC</b> 把「税收的现值」换成「政府支出的现值」，得 <b><span class='mj'>C_{t}+\\frac{C_{t+1}}{1+r_{t}}=(Y_{t}-G_{t})+\\frac{Y_{t+1}-G_{t+1}}{1+r_{t}}</span></b>。",
    plain="家庭的约束本来是「一生消费的现值＝一生税后收入的现值」。现在做一步替换：因为政府欠的债迟早要用税来还，所以「一生要交的税的现值」其实就等于「一生政府支出的现值」。把这一项换成政府支出，家庭就只用关心政府花多少，不用关心它怎么收钱。",
    lr=[
        dict(name="第一步：把税收项括出来",
             lhs="C_{t}+\\frac{C_{t+1}}{1+r_{t}}",
             lhs_t="一生消费的现值",
             rhs="Y_{t}+\\frac{Y_{t+1}}{1+r_{t}}-\\left[T_{t}+\\frac{T_{t+1}}{1+r_{t}}\\right]",
             rhs_t="一生收入的现值 <b>减去</b> 一生税收的现值（方括号里就是税的现值）",
             why="只是把第 6 页的 <span class='mj'>(Y_{t}-T_{t})+\\frac{Y_{t+1}-T_{t+1}}{1+r_{t}}</span> 重新分组。<b>分组的目的，是让方括号里的东西恰好等于某个已知的量。</b>",
             why_t="为什么这样分组"),
        dict(name="第二步：用政府 IBC 替换方括号",
             lhs="C_{t}+\\frac{C_{t+1}}{1+r_{t}}",
             lhs_t="一生消费的现值",
             rhs="(Y_{t}-G_{t})+\\frac{Y_{t+1}-G_{t+1}}{1+r_{t}}",
             rhs_t="<b>一生「净产出」的现值</b>（产出减去政府占用）",
             why="因为政府 IBC 说 <span class='mj'>T_{t}+\\frac{T_{t+1}}{1+r_{t}}=G_{t}+\\frac{G_{t+1}}{1+r_{t}}</span>，<b>两个方括号相等，所以可以直接换掉</b>。<b>换了之后，<span class='mj'>T</span> 彻底不见了。</b>",
             why_t="为什么能直接换"),
    ],
    note=(
        "这一步的<b>逻辑跳跃</b>必须说清楚，否则会变成「魔术」：<br><br>"
        "<b>家庭凭什么「知道」政府 IBC？</b>因为它<b>看得见</b>：政府今天减税、发债，家庭知道这笔债到期要用税还。<b>课件原话：<span class='mj'>From the household's perspective, knowing that the government's IBC must hold…</span></b>——<b>「知道政府 IBC 成立」是李嘉图等价的核心假设</b>，不是数学技巧。<br><br>"
        "<b>如果家庭不知道／不相信会怎样？</b>那它就会把减税当成「天上掉下来的收入」，从而增加消费。<b>这就是第 16 页「无李嘉图等价」的情形，乘数会变成 <span class='mj'>1/(1-\\mathrm{MPC})</span>。</b><br><br>"
        "<b>所以这一页是全讲的分水岭</b>：<b>在它之前，「税」是家庭的外生变量；在它之后，「税」被 <span class='mj'>G</span> 完全替换掉了。</b>后面的所有结论（消费函数、乘数、挤出）都从这里长出来。"
    ),
    dec=[
        ("<span class='mj'>\\left[T_{t}+\\frac{T_{t+1}}{1+r_{t}}\\right]</span>", "税收的现值", "<b>被替换掉的那一块</b>。<b>它不是「不重要」，而是「被 <span class='mj'>G</span> 决定了」</b>。"),
        ("净产出", "<span class='mj'>Y-G</span>", "<b>产出里「没被政府占用」的部分</b>。<b>家庭真正能分配的资源</b>。<b>它是本讲最后消费函数的核心自变量。</b>"),
        ("「知道政府 IBC 成立」", "核心假设", "<b>家庭是前瞻的、且相信政府不会赖账</b>。<b>这条一破，李嘉图等价就倒。</b>"),
    ],
    tip="这一步可以想成<b>「合并报表」</b>：家庭和政府其实是<b>同一个经济体的两个账户</b>。家庭欠政府的税、政府欠家庭的债，<b>在合并报表里会互相抵消</b>，剩下的只有「总产出减总政府支出」。<b>李嘉图等价就是「合并报表」的经济学说法。</b>",
    warn="<b>别写成「每期都有 <span class='mj'>T_{t}=G_{t}</span>」。</b>政府 IBC 保证的是<b>现值相等</b>，<b>不是每期相等</b>。<b>某一年完全可能是「大赤字 + 低税」</b>。答题时说「现值相等」，不要写「每期相等」。"
)

add(9,
    kp="<b><span class='mj'>T_{t}</span> 与 <span class='mj'>T_{t+1}</span> 同时消失</b>。从家庭角度看，<b>就仿佛 <span class='mj'>T_{t}=G_{t}</span>、<span class='mj'>T_{t+1}=G_{t+1}</span></b>。于是消费函数改写为 <b><span class='mj'>C_{t}=C^{d}(Y_{t}-G_{t},\\ Y_{t+1}-G_{t+1},\\ r_{t})</span></b>——<b>不含任何税！</b>",
    plain="结果很干净：家庭做消费决定时，只关心「产出减掉政府花的」还剩多少，完全不关心政府是收税还是借钱。这就是李嘉图等价的算式版。",
    lr=[
        dict(name="消费函数（终极形态：税没了）",
             lhs="C_{t}",
             lhs_t="今天消费",
             rhs="C^{d}(Y_{t}-G_{t},\\ Y_{t+1}-G_{t+1},\\ r_{t})",
             rhs_t="三个自变量：<b>两期净产出</b> ＋ 利率。<b>没有 <span class='mj'>T</span>，也没有 <span class='mj'>B</span></b>",
             why="因为一生资源的现值只取决于 <span class='mj'>Y</span> 与 <span class='mj'>G</span> 的路径（第 8 页的结论），而 <span class='mj'>T</span> 的路径被政府 IBC 钉死了。<b>换句话说：给定 <span class='mj'>G</span>，不同的 <span class='mj'>T</span> 组合只改变「什么时候交税」，不改变「一生要交多少」——而家庭只在乎后者。</b>",
             why_t="为什么税不见了"),
    ],
    note=(
        "「就仿佛 <span class='mj'>T_{t}=G_{t}</span>」这句话要小心理解，它是<b>本讲最容易被误读的一句</b>：<br><br>"
        "<b>它不是「每期税收真的等于支出」</b>，而是：<b>对家庭的决策而言，把税收流替换成支出流，结果不变</b>。<b>原因是家庭只看现值，而两条流的现值相等。</b><br><br>"
        "<b>换个说法</b>：家庭面对的不是「今年的税单」，而是「一辈子要为政府掏多少钱」。<b>这个总数就是政府支出的现值</b>——政府花多少，家庭最终就得掏多少（因为它不能赖账、也不能凭空创造资源）。<b>至于什么时候掏，无所谓。</b><br><br>"
        "<b>这就是为什么「财政政策」在本讲的最终形态里只剩一个变量 <span class='mj'>G</span>。</b>"
    ),
    dec=[
        ("<span class='mj'>Y_{t}-G_{t}</span>", "净产出", "<b>「产出里政府拿走之后剩下的」</b>。<b>它是家庭真正能消费的上限</b>（加上跨期调配）。"),
        ("<span class='mj'>T</span> 消失", "taxes drop out", "<b>不是「税不存在」，而是「税被 <span class='mj'>G</span> 决定」</b>。<b>答题要写这一句，否则显得没懂。</b>"),
        ("「as though」", "就仿佛", "<b>课件的措辞很讲究</b>：<b>「仿佛」而不是「等于」</b>。<b>因为它只是「决策等价」，不是「预算恒等」。</b>"),
    ],
    tip="到这里，<b>本讲的经济学已经讲完了</b>，剩下的全是它的推论：<b>① 李嘉图等价（怎么融资无所谓）；② 乘数与挤出（<span class='mj'>G</span> 上升会怎样）。</b><b>后面每一页，你都可以问一句「这和第 9 页那条消费函数是什么关系」。</b>",
    warn="<b>别答「家庭不在乎税收」。</b>家庭非常在乎——<b>它在乎的是「一生要交多少」，而这个数由 <span class='mj'>G</span> 决定</b>。<b>准确表述：「税的时序不影响决策，税的现值才影响，而现值等于政府支出的现值。」</b>"
)

add(10,
    kp="直觉：家庭在意的只有<b>一生净收入的现值</b>。<b>不被支出下降所匹配的减税</b>，一定意味着<b>未来税收按现值等量上升</b>，而这一点<b>被家庭内部化了</b>。数字例子：<span class='mj'>T_{t}</span> 减 1 ⇒ 政府 IBC 要求 <span class='mj'>T_{t+1}</span> 增 <span class='mj'>(1+r_{t})</span> ⇒ <b>两边的现值都是 1，抵消</b>。",
    plain="举个具体数字：今天少收你 1 块钱的税。政府少了这 1 块，只能借。明年要还 1 块本金加利息，所以明年得多收你 1+r 块。你把这 1+r 块折回今天，正好还是 1 块。也就是说：今天多给你 1 块，明天又拿回去 1 块——你根本不会因此多花钱。",
    lr=[
        dict(name="减税 1 块的完整账（本讲最该会的算术）",
             lhs="\\underbrace{-\\Delta T_{t}}_{=+1}",
             lhs_t="今天少收 1 块（<b>家庭今天多 1 块</b>）",
             rhs="\\underbrace{\\frac{\\Delta T_{t+1}}{1+r_{t}}}_{=+1}",
             rhs_t="未来多收的税<b>折成今天的价值</b>，<b>正好也是 1 块</b>",
             rel="⟺",
             why="因为政府 IBC 必须成立：<span class='mj'>\\Delta T_{t}+\\frac{\\Delta T_{t+1}}{1+r_{t}}=0</span>（<span class='mj'>G</span> 不变）。所以 <span class='mj'>-\\Delta T_{t}=\\frac{\\Delta T_{t+1}}{1+r_{t}}</span>——<b>今天的减税，等于未来的增税，现值一比一</b>。<b>家庭的一生财富一点没变，所以消费一点也不变。</b>",
             why_t="为什么恰好抵消"),
    ],
    note=(
        "把<b>三个层次</b>分开，这段直觉就不会乱：<br><br>"
        "<b>① 政府这一侧</b>：<span class='mj'>G</span> 不变、<span class='mj'>T_{t}</span> 减 1 ⇒ 只能发债，<span class='mj'>B_{t}</span> 增 1。<br>"
        "<b>② 明年这一侧</b>：债务要还，<span class='mj'>G_{t+1}</span> 不变 ⇒ <span class='mj'>T_{t+1}</span> 必须增 <span class='mj'>(1+r_{t})</span>。<b>注意是「加利息」，不是「加 1」</b>——这是最容易漏的一步。<br>"
        "<b>③ 家庭这一侧</b>：今天多 1、明年少 <span class='mj'>(1+r)</span>。<b>折现后</b>：<span class='mj'>+1-\\frac{1+r}{1+r}=0</span>。<b>一生财富不变 ⇒ 消费不变 ⇒ 储蓄增加 1（正好买下政府新发的债）。</b><br><br>"
        "<b>最后一句是关键</b>：家庭把减税得到的 1 块钱<b>原封不动地存起来</b>，正好借给政府。<b>所以「减税」在总量上什么都没发生</b>——只是家庭的投资组合里多了一张国债。<b>这就是「李嘉图」的全部内容。</b>"
    ),
    dec=[
        ("不匹配的减税", "tax cut not matched by spending cut", "<b>只减税、不减支出</b>。<b>这是李嘉图等价唯一针对的情形</b>——如果同时减支出，那就是「财政紧缩」，另说。"),
        ("内部化", "internalize", "<b>家庭把「未来的税」算进今天的决策</b>。<b>这是「前瞻」的行为学含义</b>，也是四个假设之一。"),
        ("正好买下国债", "portfolio shift", "<b>减税的钱变成了储蓄，借给了政府</b>。<b>所以 <span class='mj'>S_{t}</span> 上升、<span class='mj'>B_{t}</span> 上升，<b>出清条件 <span class='mj'>S_{t}=B_{t}</span> 仍然成立</b>。"),
    ],
    tip="这个「减税 1 块」的算术，<b>考试几乎必出</b>。<b>标准答法三行</b>：① 政府 IBC ⇒ <span class='mj'>\\Delta T_{t+1}=(1+r)\\cdot1</span>；② 家庭一生财富变化 <span class='mj'>=+1-\\frac{1+r}{1+r}=0</span>；③ 所以 <span class='mj'>C_{t}</span> 不变、<span class='mj'>S_{t}</span> 增 1。<b>三行写完，满分。</b>",
    warn="<b>别忘了那个 <span class='mj'>(1+r)</span>。</b>很多人写成「明年多收 1 块」，那样现值就不等了，结论会变成「减税有效」——<b>正好推到反面去</b>。<b>「今天的 1 块 ≠ 明年的 1 块」是整门课的第一课。</b>"
)

add(11,
    kp="<b>李嘉图等价</b>（Ricardo 提出、Barro 1974 正式化）：<b>政府融资方式对「支出变化的均衡效应」无关</b>。<b>增税融资</b>与<b>赤字融资</b>效果相同。原因：<b>今天的债 ＝ 明天的税，而家庭是前瞻的</b>。",
    plain="一句话：政府是「现在收你钱」还是「先借着、以后再收你钱」，对经济没有区别。因为借的钱迟早要还，而还钱只能靠收税——老百姓算得清楚这笔账。",
    note=(
        "三句话把这页钉住：<br><br>"
        "<b>① 它比较的是「同一路径的 <span class='mj'>G</span>、两种融资方式」。</b>不是「减税 vs 不减税」，也不是「多花钱 vs 少花钱」。<b>是「同样多花，钱从哪来」。</b><b>这个限定词一定要写，否则整段作废。</b><br><br>"
        "<b>② 它为什么成立？</b>两个要素：<b>(a) 政府 IBC</b>（债必须还）；<b>(b) 家庭前瞻</b>（知道并算进今天）。<b>少任何一个，等价就破。</b><br><br>"
        "<b>③ 它为什么有用？</b>因为它<b>大大简化了模型</b>：均衡只需要知道 <span class='mj'>\\{Y_{t},Y_{t+1},G_{t},G_{t+1}\\}</span>，<b>完全不需要知道 <span class='mj'>B</span> 或 <span class='mj'>T</span></b>。<b>第 14 页会把这句话原样写进「外生变量」那一栏。</b>"
    ),
    dec=[
        ("David Ricardo", "李嘉图", "<b>提出者</b>（19 世纪初）。<b>但他自己并不完全相信</b>——这一点常被当作花絮考。"),
        ("Barro (1974)", "巴罗", "<b>正式化的人</b>。<b>他把「代际利他」引入，使等价在无限期也成立</b>。<b>年份要记。</b>"),
        ("tax finance", "增税融资", "<b>现在就加税</b>，用税收支付 <span class='mj'>G</span>。"),
        ("deficit finance", "赤字融资", "<b>现在发债</b>，以后再收税。<b>与上者等价</b>。"),
    ],
    tip="<b>一句话记住</b>：<b>「李嘉图等价 ＝ 融资方式无关」</b>。<b>再加一句防错</b>：<b>「它不说支出无关」</b>。这两句话一起背，能挡住大部分误答。",
    warn="<b>别写成「李嘉图等价说明财政政策无效」。</b>这是一个流传很广的错误。<b>它只说「怎么借钱不重要」，<span class='mj'>G</span> 上升照样把 <span class='mj'>C</span> 挤出去。</b>另外它<b>也不适用于「减税 + 减支出」的组合</b>——那是另一回事。"
)

add(12,
    kp="李嘉图等价依赖<b>四个可疑假设</b>：<b>① 税是一次性总付（不扭曲）</b>；<b>② 没有借贷约束</b>；<b>③ 家庭前瞻</b>；<b>④ 政府不比家庭活得久</b>（收税时点无关）。不过它的<b>基本直觉仍有解释力</b>。",
    plain="这个结论听起来太完美了，所以它一定是「有条件成立」的。四个条件分别是：税不能扭曲行为、老百姓想借钱就能借到、老百姓真的会算未来的账、以及政府不会「熬死」老百姓（否则可以把税推给下一代）。",
    note=(
        "四条逐一拆开，<b>每一条都要能说出「破了会怎样」</b>——这是考「批判」类题目的标准打法：<br><br>"
        "<b>① 税必须是一次性总付（lump-sum）。</b>如果是比例税，减税会改变<b>劳动／储蓄的相对价格</b>，产生替代效应 ⇒ <b>即使一生财富不变，行为也会变</b> ⇒ 等价破。<b>现实中的税几乎都是扭曲性的</b>，所以这是最要紧的一条。<br><br>"
        "<b>② 没有借贷约束。</b>如果家庭想借钱借不到（Topic 4 的 <span class='mj'>S_{t}\\ge0</span>），<b>减税就等于「把未来的钱提前给你」，而它恰恰是想要却拿不到的</b> ⇒ 消费会增加 ⇒ 等价破。<b>这一条最重要</b>，因为现实中有大量「月光族」。<br><br>"
        "<b>③ 家庭前瞻。</b>如果家庭是「短视」的（只看当期收入），减税就被当成收入 ⇒ 消费上升 ⇒ 等价破。<b>第 16 页的乘数模型就是这一条破了的情形。</b><br><br>"
        "<b>④ 政府不比家庭活得久。</b>如果政府可以「熬死」这一代人（把税推给还没出生的后代），那么<b>今天的债就不需要今天的家庭来还</b> ⇒ 一生财富真的增加了 ⇒ 等价破。<b>Barro 的反驳是「代际利他」：父母会为子女储蓄，所以等价仍然（近似）成立。</b><br><br>"
        "<b>最后一句课件说得很克制</b>：<b>「Nevertheless, basic intuition is potentially powerful」</b>——<b>它不是真理，但是基准</b>。<b>答题时先给「假设下成立」，再给「现实中为什么偏」，这就是完整的答案。</b>"
    ),
    dec=[
        ("lump-sum", "一次性总付", "<b>与行为无关的税</b>。<b>破了就产生替代效应</b> ⇒ 等价失效。<b>这是四条里最技术性的一条。</b>"),
        ("borrowing constraint", "借贷约束", "<b>想借借不到</b>。<b>破了等价就失效，而且是最现实的一条</b>——因为「想借钱的人」正是减税最能刺激的那批人。"),
        ("forward-looking", "前瞻", "<b>会算未来的账</b>。<b>破了就变成「短视的凯恩斯消费者」</b>，乘数变成 <span class='mj'>1/(1-\\mathrm{MPC})</span>。"),
        ("outlive", "政府不比家庭活得久", "<b>否则可以把税推给后代</b>。<b>Barro 用「代际利他」来修补</b>。"),
    ],
    tip="<b>答题模板</b>：「李嘉图等价在<b>四条件下</b>成立：……。<b>现实中至少有三条明显不成立</b>（扭曲性税收、借贷约束、短视），<b>所以它更像一个基准而非描述</b>；<b>但它的价值在于：它告诉我们「减税要有效，必须依赖某个摩擦」</b>。<b>这个「必须依赖摩擦」的句式，是宏观论述题的高分句。</b>",
    warn="<b>别说「李嘉图等价被现实否定了，所以没用」。</b>它的价值<b>正是</b>作为一个<b>零点</b>：<b>现实偏离它多远，就说明摩擦有多大</b>。<b>「基准 + 偏离」才是正确的评价方式。</b>"
)


# ==================== ⑥ 一般均衡：出清与两条方程 ====================

add(13,
    kp="市场出清要求<b>「总量储蓄」为零</b>：<b><span class='mj'>S_{t}-B_{t}=0</span></b>。代入 <span class='mj'>S_{t}=Y_{t}-T_{t}-C_{t}</span> 与 <span class='mj'>B_{t}=G_{t}-T_{t}</span>，得 <b><span class='mj'>Y_{t}=C_{t}+G_{t}</span></b>。",
    plain="上一讲没有政府，所以「家庭储蓄必须为零」。这一讲有了政府，家庭存的钱正好借给政府，所以是「家庭储蓄 ＝ 政府借款」。把两边的定义代进去，税就被消掉了，只剩下「产出 ＝ 私人消费 ＋ 政府支出」。",
    lr=[
        dict(name="本讲的出清条件（注意与上一讲不同）",
             lhs="S_{t}-B_{t}",
             lhs_t="<b>家庭储蓄 减去 政府借款</b>（可贷资金的净供给）",
             rhs="0",
             rhs_t="<b>可贷资金市场出清</b>：想借的 ＝ 想贷的",
             why="<b>上一讲是 <span class='mj'>S_{t}=0</span>，因为没有人借</b>；<b>这一讲政府会借，所以家庭的储蓄有了去处</b>。<b>这条式子的意思是：家庭存的每一块钱，正好被政府借走。</b>",
             why_t="为什么是 S 减 B"),
        dict(name="代入定义之后（税被消掉）",
             lhs="Y_{t}-T_{t}-C_{t}-(G_{t}-T_{t})",
             lhs_t="<span class='mj'>S_{t}</span> 的定义 <b>减去</b> <span class='mj'>B_{t}</span> 的定义",
             rhs="0\\ \\Longrightarrow\\ Y_{t}=C_{t}+G_{t}",
             rhs_t="<b>商品市场出清</b>：产出分成私人消费与政府支出",
             why="<b>两个 <span class='mj'>T_{t}</span> 正好抵消</b>——这是本页最漂亮的一步。<b>不管政府怎么收税，只要它花 <span class='mj'>G_{t}</span>，产出就必须分成 <span class='mj'>C_{t}</span> 与 <span class='mj'>G_{t}</span> 两块。</b>",
             why_t="为什么税会抵消"),
    ],
    note=(
        "这一页有一个<b>很容易记错、但极其重要</b>的对照，必须背下来：<br><br>"
        "<b>Topic 5（无政府）：<span class='mj'>S_{t}=0</span> ⇒ <span class='mj'>C_{t}=Y_{t}</span>。</b><br>"
        "<b>Topic 6（有政府）：<span class='mj'>S_{t}=B_{t}</span> ⇒ <span class='mj'>C_{t}=Y_{t}-G_{t}</span>。</b><br><br>"
        "<b>为什么从 <span class='mj'>S=0</span> 变成 <span class='mj'>S=B</span>？</b>因为多了一个借款人。<b>家庭的储蓄不再「无处可去」，而是正好变成政府债务</b>。<b>这是「多一个主体」带来的第一个结构性变化。</b><br><br>"
        "<b>而 <span class='mj'>Y=C+G</span> 这条式子，就是「挤出」的全部来源</b>：<b><span class='mj'>Y</span> 固定、<span class='mj'>G</span> 涨一块、<span class='mj'>C</span> 就必须少一块</b>。<b>不需要任何行为假设，这是会计恒等式。</b><br><br>"
        "<b>所以「完全挤出」在这个模型里是必然的</b>。真正需要解释的是：<b>为什么家庭会「甘心」少花这一块？</b>答案在利率——第 20 页。"
    ),
    dec=[
        ("<span class='mj'>S_{t}-B_{t}</span>", "可贷资金的净供给", "<b>家庭贷出的减去政府借入的</b>。<b>它为零，市场才清</b>。<b>注意这个组合量在上一讲是 <span class='mj'>S_{t}</span> 单独一个。</b>"),
        ("<span class='mj'>Y_{t}=C_{t}+G_{t}</span>", "商品市场出清", "<b>本讲所有结论的入口</b>。<b>它是恒等式，不是行为方程</b>——所以「挤出」不依赖偏好。"),
        ("<span class='mj'>T_{t}</span> 抵消", "关键一步", "<b>两个 <span class='mj'>T</span> 一正一负</b>。<b>这说明「怎么收税」连会计层面都不影响 <span class='mj'>C+G</span>。</b>"),
    ],
    tip="把 <span class='mj'>Y=C+G</span> 想成<b>「一块饼分成两半」</b>：饼的大小固定（禀赋经济），政府多吃一口，私人就少吃一口。<b>利率的作用不是改变饼的大小，而是让私人「愿意」少吃那口。</b><b>这句话是理解本讲图形的钥匙。</b>",
    warn="<b>别把出清条件写成 <span class='mj'>S_{t}=0</span>（照抄上一讲）。</b>这是本讲最常见的错误。<b>有政府时，<span class='mj'>S_{t}=B_{t}</span></b>。<b>如果题目里政府不发债（<span class='mj'>B=0</span>，即平衡预算），那两个式子才重合。</b>"
)

add(14,
    kp="均衡是两条：<b>① <span class='mj'>C_{t}=C^{d}(Y_{t}-G_{t},Y_{t+1}-G_{t+1},r_{t})</span></b>（个体最优）；<b>② <span class='mj'>Y_{t}=C_{t}+G_{t}</span></b>（市场出清）。<b>外生变量只有四个：<span class='mj'>Y_{t},Y_{t+1},G_{t},G_{t+1}</span></b>——<b>不需要知道债务或税收</b>。",
    plain="两条式子、两个未知数（今天消费和利率）。注意「外生变量」那一栏里没有税、没有债务——这正是李嘉图等价的好处：模型一下子简单了。",
    lr=[
        dict(name="均衡的第二条（市场出清）",
             lhs="Y_{t}",
             lhs_t="产出（<b>外生固定的禀赋</b>）",
             rhs="C_{t}+G_{t}",
             rhs_t="私人消费 ＋ 政府支出",
             why="这条<b>不含 <span class='mj'>r_{t}</span></b>，所以它可以<b>先把 <span class='mj'>C_{t}</span> 钉住</b>：<span class='mj'>C_{t}=Y_{t}-G_{t}</span>。<b>于是第一条就退化成一个只含 <span class='mj'>r_{t}</span> 的一元方程</b>——和上一讲完全一样的解法。",
             why_t="为什么它先被用掉"),
    ],
    note=(
        "几点必须说清：<br><br>"
        "<b>① 解法顺序与上一讲相同</b>：<b>出清定 <span class='mj'>C_{t}</span> → 消费函数定 <span class='mj'>r_{t}</span> → 家庭 IBC 定 <span class='mj'>C_{t+1}</span></b>。<b>三步，不要乱。</b><br><br>"
        "<b>② 外生变量只有四个，这是李嘉图等价的直接体现。</b>课件专门加了一句<b>「do not need to know debt or taxes」</b>。<b>这句话在答题里非常值钱</b>：它说明<b>模型的输入里根本没有 <span class='mj'>T</span> 和 <span class='mj'>B</span></b>，所以输出当然与它们无关。<br><br>"
        "<b>③ IS 与 <span class='mj'>Y^{s}</span> 与上一讲「概念上相同」，但现在 <span class='mj'>G_{t}</span> 与 <span class='mj'>G_{t+1}</span> 会移动 IS。</b>因为 <span class='mj'>G</span> 进入了消费函数，也直接进入支出。<b>这就是第 18、19 页那两张图的来源。</b><br><br>"
        "<b>④ <span class='mj'>Y^{s}</span> 仍然是竖线</b>——产出还是外生的，政府支出再大也变不出更多产出。<b>这一点没变。</b>"
    ),
    dec=[
        ("外生变量（四个）", "<span class='mj'>Y_{t},Y_{t+1},G_{t},G_{t+1}</span>", "<b>都是「天上掉下来的」</b>。<b>注意没有 <span class='mj'>T</span>、没有 <span class='mj'>B</span></b>——这是本讲的招牌结论。"),
        ("内生变量", "<span class='mj'>C_{t},r_{t}</span>", "<b>两个未知数、两条方程</b>。<span class='mj'>C_{t+1}</span> <b>由家庭 IBC 事后给出</b>，不是独立未知数。"),
        ("IS 会移动", "IS shifts with G", "<b>上一讲 IS 只随 <span class='mj'>Y_{t+1}</span> 动</b>；<b>这一讲 <span class='mj'>G_{t}</span> 与 <span class='mj'>G_{t+1}</span> 也会动它</b>。<b>因为 <span class='mj'>G</span> 同时进了「消费」和「支出」两处。</b>"),
    ],
    tip="<b>把这一页当成「施工图」</b>：<b>四个外生 → 两条方程 → 两个内生</b>。<b>考试让写模型，就照这个格式写</b>：先列外生、再列两条、再说解出什么。<b>比写一大堆文字清楚得多。</b>",
    warn="<b>别把 <span class='mj'>T</span> 写进外生变量里。</b>虽然推导过程中它出现过，<b>但最终的均衡系统里没有它</b>。<b>写进去就等于说「税还在影响决策」，与李嘉图等价矛盾。</b>"
)


# ==================== ⑦ 乘数：三种口径 ====================

add(15,
    kp="总意愿支出 <b><span class='mj'>Y^{d}_{t}=C^{d}(Y_{t}-G_{t},Y_{t+1}-G_{t+1},r_{t})+G_{t}</span></b>。令收入＝支出并<b>全微分（固定 <span class='mj'>r_{t},Y_{t+1},G_{t+1}</span>）</b>：<span class='mj'>dY_{t}=\\mathrm{MPC}(dY_{t}-dG_{t})+dG_{t}</span> ⇒ <b><span class='mj'>dY_{t}=dG_{t}</span></b>。<b>固定利率下乘数 ＝ 1</b>——这是<b>局部均衡</b>概念，也是 IS 曲线的<b>水平移动量</b>。",
    plain="先只算「需求这一侧」：政府多花一块钱，家庭因为要多交税而少花 MPC 块（不到一块），所以支出净增 1 减 MPC 块。这个净增会通过「支出变成别人的收入、别人再多花一点」放大，放大到最后正好是 1 块钱。所以政府花一块，支出也多一块。",
    lr=[
        dict(name="固定利率下的政府支出乘数（有李嘉图等价）",
             lhs="\\frac{dY_{t}}{dG_{t}}",
             lhs_t="乘数",
             rhs="1",
             rhs_t="<b>一比一</b>",
             why="<b>推导</b>：<span class='mj'>dY_{t}=\\mathrm{MPC}(dY_{t}-dG_{t})+dG_{t}</span> ⇒ <span class='mj'>dY_{t}(1-\\mathrm{MPC})=(1-\\mathrm{MPC})dG_{t}</span> ⇒ <span class='mj'>dY_{t}=dG_{t}</span>。<b>关键在第 <span class='mj'>-\\mathrm{MPC}\\cdot dG_{t}</span> 这一项</b>：<b>政府多花的那一块，家庭因为「税负上升」先少花了 MPC 块</b>。<b>没有这一项，就会得到 <span class='mj'>1/(1-\\mathrm{MPC})</span>。</b>",
             why_t="怎么推出来的"),
    ],
    note=(
        "这一页有<b>三件事</b>必须分开，否则一定混：<br><br>"
        "<b>① 这个「1」不是最终答案。</b>它是<b>「固定 <span class='mj'>r</span>」下的乘数</b>，课件原话是 <b>a partial equilibrium concept</b>。<b>它衡量的是 IS 曲线水平移动多远</b>：<span class='mj'>G</span> 上升使支出线上移 <span class='mj'>(1-\\mathrm{MPC})dG</span>，而支出线斜率是 <span class='mj'>1-\\mathrm{MPC}</span>，所以<b>交点右移 <span class='mj'>(1-\\mathrm{MPC})dG/(1-\\mathrm{MPC})=dG</span></b>。<b>「乘数 ＝ IS 的水平位移」这句话非常重要。</b><br><br>"
        "<b>② 为什么是 1 而不是更大？</b>因为<b>李嘉图等价让家庭先扣掉一块</b>。家庭知道政府多花的钱要自己交税，所以<b>先少花 <span class='mj'>\\mathrm{MPC}\\cdot dG</span></b>，只剩 <span class='mj'>(1-\\mathrm{MPC})dG</span> 的净注入。<b>然后这个净注入再走「乘数」的过程，正好放大成 <span class='mj'>dG</span>。</b>（第 17 页的轮次会算给你看。）<br><br>"
        "<b>③ 一般均衡里连这 1 也没有。</b>因为 <span class='mj'>Y^{s}</span> 是竖线，<b>产出根本不能变</b>。<b>所以「IS 右移 <span class='mj'>dG</span>」只体现为「<span class='mj'>r</span> 上升」，产出回到 <span class='mj'>Y_{0,t}</span>。</b><b>这就是第 18 页图上发生的事。</b>"
    ),
    dec=[
        ("<span class='mj'>Y^{d}_{t}</span>", "总意愿支出", "<b>＝ 私人消费 ＋ 政府支出</b>。<b>注意这里有两处 <span class='mj'>G</span></b>：一处在消费函数的自变量里（<span class='mj'>-G_{t}</span>），一处在加号后面（<span class='mj'>+G_{t}</span>）。<b>混掉其中任何一个，乘数就算错。</b>"),
        ("<span class='mj'>-\\mathrm{MPC}\\cdot dG_{t}</span>", "李嘉图项", "<b>家庭为「未来的税」先少花的钱</b>。<b>这一项是「1」与「1/(1-MPC)」的唯一区别。</b>"),
        ("partial equilibrium", "局部均衡口径", "<b>固定 <span class='mj'>r</span></b>。<b>只算需求侧，不管供给。</b><b>答题时必须标明口径</b>，否则「乘数到底是几」说不清。"),
        ("IS 的水平位移", "<span class='mj'>=dG_{t}</span>", "<b>「乘数 ＝ 1」在图形上的含义</b>。<b>上移 <span class='mj'>(1-\\mathrm{MPC})dG</span> ÷ 斜率 <span class='mj'>(1-\\mathrm{MPC})</span> ＝ <span class='mj'>dG</span>。</b>"),
    ],
    tip="<b>三个数字一次记清</b>：<b>① r 固定 + 有 RE ⇒ 1；② r 固定 + 无 RE ⇒ <span class='mj'>1/(1-\\mathrm{MPC})</span>；③ r 会动（一般均衡）⇒ 0。</b><b>记忆法：<span class='mj'>r</span> 一动，产出就被供给卡死；RE 一开，家庭先扣回一块。</b>",
    warn="<b>别把 <span class='mj'>dY=dG</span> 当成「均衡乘数」。</b>它是<b>固定利率</b>下的值。<b>均衡里 <span class='mj'>Y</span> 一点没变</b>（因为供给是竖线）。<b>答题写「乘数 ＝ 1」而不写「固定 r」，必扣分。</b>"
)

add(16,
    kp="若家庭<b>不前瞻</b>（无李嘉图等价），意愿支出为 <b><span class='mj'>Y_{t}=C^{d}(Y_{t}-T_{t},r_{t})+G_{t}</span></b>。设<b>赤字融资</b>（<span class='mj'>T_{t}</span> 不变），固定 <span class='mj'>r</span> 全微分：<span class='mj'>dY_{t}=\\mathrm{MPC}\\cdot dY_{t}+dG_{t}</span> ⇒ <b><span class='mj'>\\frac{dY_{t}}{dG_{t}}=\\frac{1}{1-\\mathrm{MPC}}&gt;1</span></b>。",
    plain="如果老百姓是「短视」的——政府减税、发债，他以为白得了一笔钱，就多花——那么政府多花一块，就会层层放大成 1/(1−MPC) 块。比如 MPC=0.6，乘数就是 2.5。",
    lr=[
        dict(name="无李嘉图等价、固定利率下的乘数",
             lhs="\\frac{dY_{t}}{dG_{t}}",
             lhs_t="乘数",
             rhs="\\frac{1}{1-\\mathrm{MPC}}&gt;1",
             rhs_t="<b>大于 1</b>。<span class='mj'>\\mathrm{MPC}=0.6</span> 时是 2.5",
             why="<b>推导</b>：<span class='mj'>Y_{t}=C^{d}(Y_{t}-T_{t},r_{t})+G_{t}</span>，<span class='mj'>T_{t}</span> 固定 ⇒ <span class='mj'>dY_{t}=\\mathrm{MPC}\\cdot dY_{t}+dG_{t}</span> ⇒ <span class='mj'>dY_{t}(1-\\mathrm{MPC})=dG_{t}</span>。<b>与上一页的唯一区别：消费函数的自变量里没有 <span class='mj'>G</span></b>——家庭<b>不把政府支出当成自己的税负</b>，所以<b>不会先扣掉那一块</b>。",
             why_t="怎么推出来的"),
    ],
    note=(
        "这一页是<b>「对照组」</b>，作用是把李嘉图等价的价值显出来：<br><br>"
        "<b>① 两个假设必须同时说明</b>：<b>(i) 没有李嘉图等价</b>；<b>(ii) 实际利率固定</b>。课件把这两条明确写在页末。<b>少写一条，答案就不完整。</b><br><br>"
        "<b>② 消费函数为什么写成 <span class='mj'>C^{d}(Y_{t}-T_{t},r_{t})</span>？</b>因为它假设家庭<b>只看当期可支配收入</b>（短视／拇指规则消费者）。<b>此时赤字融资（<span class='mj'>T_{t}</span> 不变）等于「白给一笔钱」</b>，所以消费上升 → 乘数被放大。<b>如果改成增税融资（<span class='mj'>T_{t}</span> 随 <span class='mj'>G_{t}</span> 一起涨），乘数会回到 1。</b><br><br>"
        "<b>③ 这个乘数仍然只是「固定 <span class='mj'>r</span>」的局部均衡值。</b>要注意<b>它与第 15 页的 1 是同一口径</b>（都是 IS 的水平位移），<b>只是家庭的反应不同</b>。<b>把两者放在一起比较才有意义。</b>"
    ),
    dec=[
        ("无李嘉图等价", "no Ricardian equivalence", "<b>家庭不把「未来的税」算进今天</b>。<b>行为上就是「短视」</b>。<b>这是本页的开关一。</b>"),
        ("赤字融资", "deficit finance", "<b><span class='mj'>T_{t}</span> 不变、<span class='mj'>B_{t}</span> 上升</b>。<b>乘数被放大的前提</b>——如果同时加税，就没有「白得的钱」了。"),
        ("<span class='mj'>\\mathrm{MPC}</span>", "边际消费倾向", "<b>乘数的核心参数</b>。<b>MPC 越大，乘数越大</b>（<span class='mj'>0.5\\to2</span>、<span class='mj'>0.8\\to5</span>、<span class='mj'>0.9\\to10</span>）。"),
        ("固定 <span class='mj'>r</span>", "fixed real interest rate", "<b>本页的开关二</b>。<b>一旦让 <span class='mj'>r</span> 调整，乘数会变</b>（在禀赋经济里直接变 0）。"),
    ],
    tip="<b>答题时把两个乘数并排放</b>：<b>有 RE：<span class='mj'>1/(1-\\mathrm{MPC})\\times(1-\\mathrm{MPC})=1</span>；无 RE：<span class='mj'>1/(1-\\mathrm{MPC})</span>。</b><b>差别就是「家庭有没有先把税扣掉」。</b><b>这一句话能把两页的内容压成一行。</b>",
    warn="<b>别把 <span class='mj'>1/(1-\\mathrm{MPC})</span> 当成「凯恩斯乘数」就完事。</b>必须补上<b>两个前提</b>：<b>无 RE、<span class='mj'>r</span> 固定</b>。<b>在一般均衡里（<span class='mj'>r</span> 内生、产出固定），这个乘数是 0。</b><b>「口径」比「数值」更重要。</b>"
)

add(17,
    kp="<b>「轮次」直觉</b>：第一轮政府支出 ＋1；在没有 RE 时，这一块变成收入 ⇒ 第二轮多消费 <span class='mj'>\\mathrm{MPC}</span> ⇒ 又变成收入 ⇒ 第三轮 <span class='mj'>\\mathrm{MPC}^{2}</span>……<b>合计 <span class='mj'>\\frac{1}{1-\\mathrm{MPC}}</span></b>。<b>有 RE 时，第一轮注水只有 <span class='mj'>(1-\\mathrm{MPC})</span></b>，合计 <b><span class='mj'>\\frac{1-\\mathrm{MPC}}{1-\\mathrm{MPC}}=1</span></b>。",
    plain="乘数不是魔法，是「同一笔钱被花了好几次」：政府修一条路，包工头拿钱去买菜，菜贩拿钱去理发……每一轮都留下一部分（因为大家都要存一点），所以总和是个等比数列。有李嘉图等价时，第一轮就少了一大块，数列加起来正好是一。",
    lr=[
        dict(name="无李嘉图等价：无穷轮次相加",
             lhs="\\frac{dY_{t}}{dG_{t}}",
             lhs_t="乘数",
             rhs="1+\\mathrm{MPC}+\\mathrm{MPC}^{2}+\\cdots=\\frac{1}{1-\\mathrm{MPC}}",
             rhs_t="<b>等比数列求和</b>（公比 <span class='mj'>\\mathrm{MPC}&lt;1</span>）",
             why="每一轮都把上一轮的收入按 <span class='mj'>\\mathrm{MPC}</span> 折一次。<b>因为 <span class='mj'>\\mathrm{MPC}&lt;1</span>，级数收敛</b>——<b>这就是「乘数有限」的原因</b>。<b>如果 <span class='mj'>\\mathrm{MPC}\\ge1</span>，级数发散，经济会无限膨胀。</b>",
             why_t="为什么收敛"),
        dict(name="有李嘉图等价：第一轮就打折",
             lhs="\\frac{dY_{t}}{dG_{t}}",
             lhs_t="乘数",
             rhs="(1-\\mathrm{MPC})+\\mathrm{MPC}(1-\\mathrm{MPC})+\\cdots=\\frac{1-\\mathrm{MPC}}{1-\\mathrm{MPC}}=1",
             rhs_t="<b>每轮都乘一个 <span class='mj'>(1-\\mathrm{MPC})</span></b>，正好约掉",
             why="<b>为什么第一轮只有 <span class='mj'>(1-\\mathrm{MPC})</span>？</b>因为政府多花 1 块，家庭同时知道自己要多交 1 块的税 ⇒ <b>立刻少花 <span class='mj'>\\mathrm{MPC}</span> 块</b>。<b>净注入只有 <span class='mj'>1-\\mathrm{MPC}</span>。</b><b>后面每轮照旧按 <span class='mj'>\\mathrm{MPC}</span> 递减。</b>",
             why_t="为什么正好是 1"),
    ],
    note=(
        "这个「轮次」推导有两个用处：<br><br>"
        "<b>① 它把「乘数」从公式变成图像</b>：<b>一笔钱在社会里转圈，每转一圈漏掉一部分</b>。<b>漏得越多（MPC 越小），乘数越小；漏得越少，乘数越大。</b><br><br>"
        "<b>② 它让「1」这个数字变得可以理解</b>：<b>不是「政府花一块、产出多一块」这么直白，而是「净注入只有 <span class='mj'>1-\\mathrm{MPC}</span>，但这一块又转了好几圈，正好转回 1」。</b><b>两个效应刚好抵消，是巧合吗？不是</b>——因为<b>「转圈」的放大倍数正好是 <span class='mj'>1/(1-\\mathrm{MPC})</span>，而净注入是 <span class='mj'>1-\\mathrm{MPC}</span>，两者互为倒数</b>。<b>这个「互为倒数」的结构值得记。</b><br><br>"
        "<b>③ 注意这一切仍然假设 <span class='mj'>r</span> 固定。</b><b>轮次讲的是「需求侧的连锁反应」，完全没有涉及供给。</b><b>在禀赋经济里，供给是竖线，所以这些轮次在一般均衡里全部被利率抵掉。</b>"
    ),
    dec=[
        ("轮次（rounds）", "spending rounds", "<b>钱在社会里转的圈数</b>。<b>每一圈都留下一部分消费、漏掉一部分储蓄。</b>"),
        ("<span class='mj'>\\mathrm{MPC}^{k}</span>", "第 k 轮的消费", "<b>公比</b>。<b>它小于 1，所以级数收敛</b>。<b>这是「乘数有限」的数学原因。</b>"),
        ("净注入 <span class='mj'>1-\\mathrm{MPC}</span>", "有 RE 的第一轮", "<b>李嘉图等价在图形上的样子</b>：<b>刺激还没开始，就先被家庭扣掉一块。</b>"),
        ("互为倒数", "reciprocal", "<b><span class='mj'>(1-\\mathrm{MPC})</span> 与 <span class='mj'>\\frac{1}{1-\\mathrm{MPC}}</span></b>。<b>一个缩小注入、一个放大连锁，正好抵消成 1。</b>"),
    ],
    tip="<b>这个「等比数列」的写法在考试里很吃香</b>：<b>它比全微分更直观，而且能同时讲清「为什么有限」与「为什么有 RE 时是 1」。</b><b>建议两种都写</b>：先全微分给结果，再用轮次给直觉。<b>两段加起来不到十行，分数很稳。</b>",
    warn="<b>别把轮次当成「跨期」的过程。</b>课件强调 <b>within a period</b>——<b>这些轮次都发生在同一个时期里</b>（一个人花钱变成另一个人的收入，同一期内完成）。<b>写成「今年一轮、明年一轮」就错了。</b>"
)


# ==================== ⑧ 图形与挤出 ====================

add(18,
    kp="<b><span class='mj'>G_{t}\\uparrow</span></b>：上图支出线<b>整体上移</b>（但只移 <span class='mj'>(1-\\mathrm{MPC})dG</span>，因为被家庭少花的 <span class='mj'>\\mathrm{MPC}\\cdot dG</span> 抵掉一部分）；下图 <b>IS 右移</b>、<span class='mj'>Y^{s}</span> 不动 ⇒ <b>均衡 <span class='mj'>Y_{t}</span> 不变、<span class='mj'>r</span> 上升</b>。",
    plain="政府多花钱，需求这条线整体往右推。可是产出是固定的（竖线），推不动。所以只能把利率顶上去——利率一高，家庭就觉得「今天花钱太贵」，于是乖乖把消费让出来给政府。",
    fig=[
        dict(name="图：<span class='mj'>G_{t}\\uparrow</span> 的图形效应（上：支出线上移；下：IS 右移、<span class='mj'>Y^{s}</span> 不动）",
             axes=[("上图横轴", "Y_{t}", "当期收入／产出"),
                   ("上图纵轴", "Y^{d}_{t}", "总意愿支出（＝私人消费 ＋ 政府支出）"),
                   ("下图横轴", "Y_{t}", "当期收入／产出（与上图对齐）"),
                   ("下图纵轴", "r_{t}", "实际利率")],
             marks=[("上图：45° 线（黑，<span class='mj'>Y^{d}_{t}=Y_{t}</span>）", "<b>不动</b>。<b>会计恒等式，任何冲击都改不了它</b>"),
                    ("上图：<b>黑色</b>支出线（较低）= 原状", "标注里带 <b><span class='mj'>G_{0,t}</span></b>。<b>这是冲击前的那条线</b>"),
                    ("上图：<b>蓝色</b>支出线（较高）= 冲击后", "标注里带 <b><span class='mj'>G_{1,t}</span></b>。<b>注意：它只上移了 <span class='mj'>(1-\\mathrm{MPC})dG</span>，而不是 <span class='mj'>dG</span></b>"),
                    ("上图：黑蓝两线之间的<b>一对反向小箭头</b>（绿向下、蓝向上）", "<b>本页最精细的一笔</b>：<b>把净移动拆成两块</b>——<b>蓝色向上 ＝ 政府直接多花的 <span class='mj'>dG</span></b>；<b>绿色向下 ＝ 家庭因税负上升而少花的 <span class='mj'>\\mathrm{MPC}\\cdot dG</span></b>。<b>净效果 <span class='mj'>(1-\\mathrm{MPC})dG</span></b>"),
                    ("上图绿色公式行（<span class='mj'>G_{1,t}</span> 与 <span class='mj'>G_{0,t+1}</span> 混排）", "<b>中间步骤</b>：<b>只让当期 <span class='mj'>G</span> 变</b>时的式子。<b>它说明「两期 <span class='mj'>G</span> 各自怎么进消费函数」</b>"),
                    ("下图：<b>黑色</b>竖线 <span class='mj'>Y^{s}</span>，位于 <span class='mj'>Y_{0,t}</span>", "<b>供给不动</b>。<b>政府多花也变不出更多产出</b>——这是禀赋经济"),
                    ("下图：<b>黑色</b> IS → <b>蓝色</b> IS′（<b>右移</b>，有向右箭头）", "<b>IS 右移 <span class='mj'>dG</span></b>（<b>这就是上一页的「乘数 ＝ 1」在图形上的含义</b>）"),
                    ("下图：新旧两个交点（<b>同一条竖线上</b>）", "<b>横坐标完全相同</b>（都是 <span class='mj'>Y_{0,t}</span>），<b>纵坐标更高</b>（<span class='mj'>r_{1,t}&gt;r_{0,t}</span>）。<b>一句话：只涨价、不涨量</b>")],
             read="<b>读图三步：① 先看下图</b>——<b>斜线右移、竖线不动</b>；<b>② 沿竖线找新交点</b>（<b>竖直向上 ⇒ <span class='mj'>Y</span> 不变、<span class='mj'>r\\uparrow</span></b>）；<b>③ 回上看那对反向箭头</b>——<b>上移 <span class='mj'>dG</span>、下压 <span class='mj'>\\mathrm{MPC}\\cdot dG</span>、净 <span class='mj'>(1-\\mathrm{MPC})dG</span></b>。",
             exam="必考三问：<b>① 为什么支出线只上移 <span class='mj'>(1-\\mathrm{MPC})dG</span>？</b>答：政府多花 1，家庭因税负上升少花 <span class='mj'>\\mathrm{MPC}</span>，净 <span class='mj'>1-\\mathrm{MPC}</span>。<b>② 为什么 <span class='mj'>Y_{t}</span> 不变？</b>答：供给是竖线，产出由禀赋决定。<b>③ 为什么 <span class='mj'>r</span> 上升？</b>答：政府多借 <span class='mj'>dG</span>，家庭只多存 <span class='mj'>\\mathrm{MPC}\\cdot dG</span>，<b>可贷资金供不应求 ⇒ 利率上升</b>。"),
        ],
    note=(
        "这张图上那<b>一对反向小箭头</b>是本讲最容易被忽略、也最能体现理解的一笔：<br><br>"
        "<b>它把「净上移 <span class='mj'>(1-\\mathrm{MPC})dG</span>」拆成了两块</b>：<br>"
        "· <b>向上 <span class='mj'>dG</span></b>：政府支出<b>直接</b>进入了总意愿支出（<span class='mj'>+G_{t}</span> 那一项）。<br>"
        "· <b>向下 <span class='mj'>\\mathrm{MPC}\\cdot dG</span></b>：同一笔钱要从家庭手里拿走（<span class='mj'>Y_{t}-G_{t}</span> 那一项），<b>家庭因此少花 MPC 块</b>。<br><br>"
        "<b>为什么要画成两个箭头而不是直接画一条新线？</b>因为<b>这两个效应来源不同、经济含义不同</b>：<b>一个是「政府多买」，一个是「私人少买」</b>。<b>如果只画净效果，你就看不出「挤出」已经在这里发生了一半。</b><br><br>"
        "<b>而在一般均衡里，剩下的那一半也被抵掉</b>：<span class='mj'>r</span> 上升再压掉 <span class='mj'>(1-\\mathrm{MPC})dG</span>，<b>最终 <span class='mj'>C</span> 正好下降 <span class='mj'>dG</span>，支出线回到原来的位置</b>（对应 <span class='mj'>Y</span> 回到 <span class='mj'>Y_{0,t}</span>）。<b>图上没画这一步——因为它发生在「利率变化之后」，属于下一张图（第 19 页）的套路。</b>"
    ),
    tip="<b>「上图两条线、下图一条线」这个模式</b>要熟悉：<b>上图是「需求侧的一族情形」，下图是「均衡点的轨迹」</b>。<b>G 改变的是「曲线位置」，而均衡点是「曲线与竖线的交点」</b>。<b>只要记住「竖线不动」，就永远不会得出「产出上升」的错误结论。</b>",
    warn="<b>别把图上的右移当成「产出增加」。</b>IS 右移 <span class='mj'>dG</span> 是<b>「若利率不变，需求会对应多少产出」</b>——<b>但利率必须变</b>。<b>两条线一夹，产出纹丝不动。</b><b>这是本讲与 Topic 8（有生产、IS 右移产出会增加）最大的区别，不要串。</b>"
)

add(19,
    kp="<b><span class='mj'>G_{t+1}\\uparrow</span></b>：上图支出线<b>下移</b>（未来净收入减少 ⇒ 今天少花）；下图 <b>IS 左移</b>、<span class='mj'>Y^{s}</span> 不动 ⇒ <b><span class='mj'>Y_{t}</span> 不变、<span class='mj'>r</span> 下降</b>。<b>方向与 <span class='mj'>G_{t}\\uparrow</span> 完全相反。</b>",
    plain="政府说明年要多花钱。家庭一想：那明年我交的税就得多，我明年就变穷了。所以今天就得开始省——多存一点。大家都想存、没人想借，利率就被压下去了。",
    fig=[
        dict(name="图：<span class='mj'>G_{t+1}\\uparrow</span> 的图形效应（上：支出线下移；下：IS 左移）",
             axes=[("上图横轴", "Y_{t}", "当期收入／产出"),
                   ("上图纵轴", "Y^{d}_{t}", "总意愿支出"),
                   ("下图横轴", "Y_{t}", "当期收入／产出（与上图对齐）"),
                   ("下图纵轴", "r_{t}", "实际利率")],
             marks=[("上图：45° 线（黑）", "<b>不动</b>"),
                    ("上图：<b>黑色</b>支出线（较高）= 原状", "标注带 <b><span class='mj'>G_{0,t+1}</span></b>。<b>冲击前</b>"),
                    ("上图：<b>蓝色</b>支出线（较低）= 冲击后", "标注带 <b><span class='mj'>G_{1,t+1}</span></b>。<b>整条下移</b>：因为<b>未来净收入 <span class='mj'>Y_{t+1}-G_{t+1}</span> 变小 ⇒ 一生财富下降 ⇒ 今天在每个收入水平上都少花</b>"),
                    ("上图：黑蓝两线之间的<b>一对反向小箭头</b>（绿向上、蓝向下）", "<b>同样是拆解</b>：<b>蓝色向下 ＝ 财富效应让今天少花</b>；<b>绿色向上 ＝ 利率下降后的「回补」</b>。<b>净效果：支出线回到原处、<span class='mj'>C_{t}</span> 不变</b>"),
                    ("上图中间那行绿色公式（混排下标）", "<b>中间步骤</b>：<b>只让未来 <span class='mj'>G</span> 变</b>时的式子。注意<b>它出现在两条线之间</b>，说明它只是过渡"),
                    ("下图：<b>黑色</b>竖线 <span class='mj'>Y^{s}</span>（位于 <span class='mj'>Y_{0,t}</span>）", "<b>供给不动</b>。<b>财政冲击（不管动哪一期的 <span class='mj'>G</span>）都改不了产出</b>"),
                    ("下图：<b>黑色</b> IS → <b>蓝色</b> IS′（<b>左移</b>，有向左箭头）", "<b>IS 左移</b>：<b>因为「给定 <span class='mj'>r</span>，出清收入更低」</b>。<b>方向与 <span class='mj'>G_{t}\\uparrow</span> 相反</b>"),
                    ("下图：新旧两个交点（<b>同一条竖线上</b>）", "<b>横坐标相同</b>，<b>纵坐标更低</b>（<span class='mj'>r_{1,t}&lt;r_{0,t}</span>）。<b>「只降利率、不动产量」</b>")],
             read="<b>读图三步：① 先判方向</b>——<b>是「今天」还是「明天」的 G 变了</b>？<b>今天 ⇒ 线向上、IS 右移、<span class='mj'>r\\uparrow</span></b>；<b>明天 ⇒ 线向下、IS 左移、<span class='mj'>r\\downarrow</span></b>。<b>② 看竖线</b>（不动）。<b>③ 看交点</b>（只在纵方向动）。",
             exam="必考两问：<b>① 为什么支出线<b>下移</b>？</b>答：未来净收入 <span class='mj'>Y_{t+1}-G_{t+1}</span> 下降 ⇒ 一生财富下降 ⇒ 各期消费都下降（平滑）⇒ 今天也少花。<b>② 为什么 <span class='mj'>r</span> <b>下降</b>？</b>答：家庭想多储蓄以应对未来的高税负，<b>可贷资金供过于求 ⇒ 利率下降</b>，直到家庭甘愿维持 <span class='mj'>C_{t}=Y_{t}-G_{t}</span>。"),
        ],
    note=(
        "这张图与上一张<b>完全对称</b>，把两者放一起记最省力：<br><br>"
        "<b><span class='mj'>G_{t}\\uparrow</span></b>：<b>家庭今天变穷</b>（可支配收入↓）⇒ 支出线上移（政府多买）但被扣掉一块 ⇒ <b>IS 右移 ⇒ <span class='mj'>r\\uparrow</span></b>。<br>"
        "<b><span class='mj'>G_{t+1}\\uparrow</span></b>：<b>家庭「觉得自己」明天变穷</b>（未来可支配收入↓）⇒ 今天就想多存 ⇒ <b>IS 左移 ⇒ <span class='mj'>r\\downarrow</span></b>。<br><br>"
        "<b>为什么方向相反？</b>因为<b>可贷资金的「供需」方向相反</b>：<br>"
        "· <span class='mj'>G_{t}\\uparrow</span> ⇒ <b>政府今天多借</b>（需求↑）⇒ <span class='mj'>r\\uparrow</span>。<br>"
        "· <span class='mj'>G_{t+1}\\uparrow</span> ⇒ <b>政府今天不多借</b>，但<b>家庭今天多存</b>（供给↑）⇒ <span class='mj'>r\\downarrow</span>。<br><br>"
        "<b>一句话记：政府「今天多借」抬利率，家庭「今天多存」压利率。</b><b>而 <span class='mj'>G_{t+1}\\uparrow</span> 恰好只触发后者。</b>"
    ),
    tip="<b>两张图对照记，比单独记两张省一半时间</b>：<b>动的是同一条竖线（不动）、同一条斜线（一个右移一个左移）、同一个结论（产量不变、只有利率变）</b>。<b>唯一要记的是「IS 往哪边移」，而它取决于「家庭今天变穷还是明天变穷」。</b>",
    warn="<b>别把 <span class='mj'>G_{t+1}\\uparrow</span> 的支出线画成上移。</b>它是<b>下移</b>——因为<b>税负上升让家庭变穷</b>，不是变富。<b>判断口诀：先问「谁的可支配收入变了、往哪变」，再决定线往哪动。</b>"
)

add(20,
    kp="<b><span class='mj'>G_{t}\\uparrow</span> 在均衡里对 <span class='mj'>Y_{t}</span> 没有影响</b>，所以私人消费被<b>完全挤出</b>：<b><span class='mj'>dC_{t}=-dG_{t}</span></b>。为了让这一点与出清相容，<b><span class='mj'>r</span> 必须上升</b>。<b><span class='mj'>G_{t+1}\\uparrow</span> 相反：<span class='mj'>r</span> 下降以阻止 <span class='mj'>C_{t}</span> 下滑</b>。<b>均衡乘数为零</b>——<b>这不是李嘉图等价的推论，而是禀赋经济的推论</b>。",
    plain="政府多花一块，产出没变，那这一块只能从私人消费里出。所以私人消费正好少一块——叫「完全挤出」。但老百姓不会自愿少花，所以利率必须涨，涨到他不情愿地少花为止。",
    lr=[
        dict(name="完全挤出（本讲的最终结论）",
             lhs="dC_{t}",
             lhs_t="私人消费的变化",
             rhs="-dG_{t}",
             rhs_t="<b>政府支出变化的相反数</b>（<b>一比一挤出</b>）",
             why="由 <span class='mj'>Y_{t}=C_{t}+G_{t}</span> 且 <span class='mj'>Y_{t}</span> 固定，两边微分即得。<b>这是恒等式级别的结论，不依赖任何偏好假设</b>——<b>只要产出不能变，挤出就是必然的。</b>",
             why_t="为什么必然"),
    ],
    note=(
        "这一页有三句话，<b>每一句都是高分点</b>，但也<b>每一句都容易被说错</b>：<br><br>"
        "<b>① 「完全挤出」是恒等式的推论，不是行为的推论。</b><b><span class='mj'>Y=C+G</span> 加 <span class='mj'>Y</span> 固定</b>，就得到 <span class='mj'>dC=-dG</span>。<b>它不需要「家庭不前瞻」，也不需要「利率如何」。这是本讲最硬的结论。</b><br><br>"
        "<b>② 利率的作用是「让家庭甘心」。</b>家庭本来不想少花（它想平滑）；<b><span class='mj'>r</span> 上升让「今天的消费」变贵，替代效应逼它少花</b>。<b>课件原话：<span class='mj'>r_{t}</span> adjusts so as to undo any desired smoothing behavior。</b>——<b>「利率的任务是抵消平滑意愿」这句话，上一讲（Topic 5）也出现过，是同一句。</b><br><br>"
        "<b>③ 「乘数为零」不是李嘉图等价的功劳。</b>课件专门写了一句：<b>Not a consequence of Ricardian equivalence, but rather due to assumption of endowment economy where output cannot respond.</b><b>这句是整讲最容易被扣分的地方</b>——<b>很多人一看到「财政政策无效」就往李嘉图等价上推，方向错了。</b><br><br>"
        "<b>正确的因果链是</b>：<b>产出固定（禀赋经济）⇒ 政府多占一块、私人就少一块 ⇒ 挤出 ⇒ 乘数为零。</b><b>李嘉图等价管的是另一件事：融资方式无关。</b><b>两件事都要说，但不能混为一谈。</b>"
    ),
    dec=[
        ("crowding out", "挤出", "<b>政府支出把私人支出「挤」出去</b>。<b>这里是「完全挤出」（一比一）</b>，因为产出固定。<b>在有生产的经济里通常只是「部分挤出」。</b>"),
        ("<span class='mj'>dC_{t}=-dG_{t}</span>", "完全挤出", "<b>恒等式推论</b>。<b>不要说成「家庭因为税负上升而少花」</b>——<b>那是机制的一半，不是原因的全部。</b>"),
        ("<span class='mj'>r</span> 的作用", "让家庭甘心", "<b>利率不是「挤出的原因」，而是「挤出的执行者」</b>。<b>挤出由会计恒等式决定，利率负责让它在行为上成立。</b>"),
        ("乘数为零", "zero multiplier", "<b>一般均衡里 <span class='mj'>dY/dG=0</span></b>。<b>原因是产出不能变，不是李嘉图等价。</b><b>这一条必须写准确。</b>"),
    ],
    tip="<b>把这句话背下来</b>：<b>「李嘉图等价说融资方式无关；禀赋经济说产出不能变、所以乘数为零。前者是关于「钱从哪来」，后者是关于「饼有多大」。」</b><b>两句话一分清，本讲的论述题就拿满了。</b>",
    warn="<b>三个高频错误</b>：<b>① 说「乘数为零是因为李嘉图等价」</b>（错，是禀赋经济）；<b>② 说「挤出是因为利率上升」</b>（错，挤出由 <span class='mj'>Y=C+G</span> 决定，利率只是执行者）；<b>③ 说「<span class='mj'>G_{t+1}\\uparrow</span> 也挤出」</b>（<b>不挤出</b>——它不占用今天的资源，只改变 <span class='mj'>r</span>）。"
)


# ============================ 公式速查 ============================
FORMULA_ROWS = [
    ("政府第 t 期流量约束",
     "<span class='mj'>G_{t}=T_{t}+B_{t}</span>",
     "支出 ＝ 税收 ＋ 发债"),
    ("政府第 t+1 期流量约束",
     "<span class='mj'>G_{t+1}+(1+r_{t})B_{t}=T_{t+1}</span>",
     "<b>没有 <span class='mj'>B_{t+1}</span></b>：最后一期必须还清"),
    ("<b>政府 IBC</b>",
     "<span class='mj'>G_{t}+\\frac{G_{t+1}}{1+r_{t}}=T_{t}+\\frac{T_{t+1}}{1+r_{t}}</span>",
     "<b>与家庭 IBC 同构</b>；<span class='mj'>B</span> 被消掉"),
    ("家庭第 t 期约束（含税）",
     "<span class='mj'>C_{t}+S_{t}=Y_{t}-T_{t}</span>",
     "收入换成<b>可支配收入</b>"),
    ("家庭 IBC（含税）",
     "<span class='mj'>C_{t}+\\frac{C_{t+1}}{1+r_{t}}=(Y_{t}-T_{t})+\\frac{Y_{t+1}-T_{t+1}}{1+r_{t}}</span>",
     "两期都减掉那一期的税"),
    ("欧拉方程",
     "<span class='mj'>u^{\\prime}(C_{t})=\\beta(1+r_{t})u^{\\prime}(C_{t+1})</span>",
     "<b>与上一讲完全相同</b>（lump-sum 不扭曲）"),
    ("消费函数（含税）",
     "<span class='mj'>C_{t}=C^{d}(Y_{t}-T_{t},\\ Y_{t+1}-T_{t+1},\\ r_{t})</span>",
     "过渡形态"),
    ("<b>家庭 IBC（换成 G）</b>",
     "<span class='mj'>C_{t}+\\frac{C_{t+1}}{1+r_{t}}=(Y_{t}-G_{t})+\\frac{Y_{t+1}-G_{t+1}}{1+r_{t}}</span>",
     "<b>用政府 IBC 替换税收项</b>"),
    ("<b>消费函数（终极形态）</b>",
     "<span class='mj'>C_{t}=C^{d}(Y_{t}-G_{t},\\ Y_{t+1}-G_{t+1},\\ r_{t})</span>",
     "<b>税彻底消失</b>——李嘉图等价的算式版"),
    ("减税 1 块的账",
     "<span class='mj'>-\\Delta T_{t}=\\frac{\\Delta T_{t+1}}{1+r_{t}}=1</span>",
     "<b>现值一比一抵消</b>；<span class='mj'>\\Delta T_{t+1}=1+r_{t}</span>"),
    ("<b>市场出清</b>",
     "<span class='mj'>S_{t}-B_{t}=0</span>",
     "<b>家庭储蓄 ＝ 政府借款</b>（上一讲是 <span class='mj'>S=0</span>）"),
    ("<b>商品市场出清</b>",
     "<span class='mj'>Y_{t}=C_{t}+G_{t}</span>",
     "<b>本讲所有结论的入口</b>；税在此抵消"),
    ("均衡系统",
     "<span class='mj'>C_{t}=C^{d}(Y_{t}-G_{t},Y_{t+1}-G_{t+1},r_{t})</span>；<span class='mj'>Y_{t}=C_{t}+G_{t}</span>",
     "外生四个：<span class='mj'>Y_{t},Y_{t+1},G_{t},G_{t+1}</span>"),
    ("总意愿支出",
     "<span class='mj'>Y^{d}_{t}=C^{d}(Y_{t}-G_{t},\\cdot)+G_{t}</span>",
     "<b>两处 <span class='mj'>G</span></b>：一处在消费里、一处直接相加"),
    ("<b>乘数（有 RE，<span class='mj'>r</span> 固定）</b>",
     "<span class='mj'>\\frac{dY_{t}}{dG_{t}}=1</span>",
     "<b>＝ IS 的水平位移</b>"),
    ("<b>乘数（无 RE，<span class='mj'>r</span> 固定）</b>",
     "<span class='mj'>\\frac{dY_{t}}{dG_{t}}=\\frac{1}{1-\\mathrm{MPC}}&gt;1</span>",
     "赤字融资时；<b>需注明两个前提</b>"),
    ("轮次（无 RE）",
     "<span class='mj'>1+\\mathrm{MPC}+\\mathrm{MPC}^{2}+\\cdots=\\frac{1}{1-\\mathrm{MPC}}</span>",
     "<b>公比 &lt;1 ⇒ 收敛</b>"),
    ("轮次（有 RE）",
     "<span class='mj'>(1-\\mathrm{MPC})(1+\\mathrm{MPC}+\\cdots)=1</span>",
     "<b>净注入与放大倍数互为倒数</b>"),
    ("<b>完全挤出</b>",
     "<span class='mj'>dC_{t}=-dG_{t}</span>",
     "<b>恒等式推论</b>；<b>乘数为零</b>"),
    ("价格方向",
     "<span class='mj'>G_{t}\\uparrow\\Rightarrow r\\uparrow</span>；<span class='mj'>G_{t+1}\\uparrow\\Rightarrow r\\downarrow</span>",
     "<b>政府多借抬利率、家庭多存压利率</b>"),
]


# ============================ 三张总表 ============================
EXTRA_TABLES = [
    dict(
        title="总表 1 · 政府 vs 家庭：两套预算逐项对照",
        sub="课件对政府 IBC 只给了一句 <b>「Conceptually the same as the household」</b>。<b>这句「同构」要能逐行摊开，才说明真的会了。</b>",
        header=["项目", "家庭", "政府"],
        rows=[
            ["<b>第 t 期流量约束</b>",
             "<span class='mj'>C_{t}+S_{t}=Y_{t}-T_{t}</span>",
             "<span class='mj'>G_{t}=T_{t}+B_{t}</span>"],
            ["<b>第 t+1 期流量约束</b>",
             "<span class='mj'>C_{t+1}=Y_{t+1}-T_{t+1}+(1+r_{t})S_{t}</span>",
             "<span class='mj'>G_{t+1}+(1+r_{t})B_{t}=T_{t+1}</span>"],
            ["<b>两期的联系</b>",
             "<span class='mj'>S_{t}</span>（储蓄，<b>正 = 借出</b>）",
             "<span class='mj'>B_{t}</span>（债务，<b>正 = 借入</b>）"],
            ["<b>跨期约束</b>",
             "<span class='mj'>C_{t}+\\frac{C_{t+1}}{1+r_{t}}=</span> 一生可支配收入现值",
             "<span class='mj'>G_{t}+\\frac{G_{t+1}}{1+r_{t}}=</span> 一生税收现值"],
            ["<b>为什么能消掉中间变量</b>",
             "消 <span class='mj'>S_{t}</span>：家庭不关心「怎么存」",
             "消 <span class='mj'>B_{t}</span>：家庭不关心「怎么借」"],
            ["<b>最后一期</b>",
             "<b>花光</b>（横截条件）",
             "<b>还清债务</b>（无庞氏条件）"],
            ["<b>谁被当作外生</b>",
             "<span class='mj'>Y,T,r</span> 全部给定",
             "<span class='mj'>G</span> 给定，<span class='mj'>T</span> 与 <span class='mj'>B</span> 由 IBC 决定"],
        ],
        note="<b>两套约束的唯一实质区别：谁是「决策者」。</b>家庭选择 <span class='mj'>C</span>（从而决定 <span class='mj'>S</span>）；政府选择 <span class='mj'>G</span>（从而决定 <span class='mj'>T</span> 与 <span class='mj'>B</span> 的组合）。<b>而李嘉图等价说的正是：政府那个「组合」怎么选，家庭根本不在乎。</b>",
        first_col_bold=True,
    ),
    dict(
        title="总表 2 · 三个乘数（其实是四个格子）",
        sub="这张表是本讲最该背的。<b>乘数不是一个数，而是「两个开关」的组合</b>：<b>有没有李嘉图等价？<span class='mj'>r</span> 动不动？</b>",
        header=["", "<span class='mj'>r_{t}</span> 固定（局部均衡）", "<span class='mj'>r_{t}</span> 内生（一般均衡）"],
        rows=[
            ["<b>有李嘉图等价</b>",
             "<b>乘数 ＝ 1</b><br>（IS 右移 <span class='mj'>dG</span>）",
             "<b>乘数 ＝ 0</b><br>（产出不变，只有 <span class='mj'>r</span> 上升）"],
            ["<b>无李嘉图等价</b>",
             "<b>乘数 ＝ <span class='mj'>\\frac{1}{1-\\mathrm{MPC}}</span></b><br>（IS 右移更多）",
             "<b>乘数 ＝ 0</b><br>（产出不变，只有 <span class='mj'>r</span> 上升）"],
            ["<b>为什么是这个值</b>",
             "有 RE 时家庭先扣掉 <span class='mj'>\\mathrm{MPC}\\cdot dG</span>；<br>无 RE 时没有这一扣",
             "<b>供给是竖线，产出不能变</b>；<br><span class='mj'>G</span> 多占一块、<span class='mj'>C</span> 就少一块"],
        ],
        note="<b>最重要的一格是右下角</b>：<b>在禀赋经济里，只要 <span class='mj'>r</span> 内生，乘数就是 0——与有没有李嘉图等价无关</b>。<b>所以「乘数为零」不能拿来当李嘉图等价的证据</b>。<b>李嘉图等价只影响「IS 移动多远」，不影响「最终产出变不变」。</b>",
        first_col_bold=True,
        table_class="ctr",
    ),
    dict(
        title="总表 3 · 李嘉图等价的四个假设：破了会怎样",
        sub="考「评述」类题目时，<b>每一条都要给出「假设 → 违反 → 后果」三件套</b>。只列假设不给后果，只能拿一半分。",
        header=["假设", "现实中的对应现象", "破了之后的后果"],
        rows=[
            ["<b>① 税是一次性总付</b><br>（不扭曲）",
             "所得税、增值税都是<b>比例／累进</b>的",
             "<b>减税改变相对价格 ⇒ 替代效应 ⇒ 即使一生财富不变，行为也变</b>"],
            ["<b>② 没有借贷约束</b>",
             "大量家庭<b>想借借不到</b>（信用卡额度、房贷首付）",
             "<b>减税 ＝ 把未来的钱提前给「最想花的人」 ⇒ 消费上升 ⇒ 等价破</b>。<b>这是最现实的一条</b>"],
            ["<b>③ 家庭前瞻</b>",
             "一部分人<b>只看当期收入</b>（拇指规则消费者）",
             "<b>减税被当成纯收入 ⇒ 消费上升 ⇒ 乘数变成 <span class='mj'>1/(1-\\mathrm{MPC})</span></b>"],
            ["<b>④ 政府不比家庭活得久</b>",
             "政府<b>可以</b>把债务留给下一代",
             "<b>今天的债不用今天的人还 ⇒ 一生财富真增加 ⇒ 等价破</b>。<b>Barro 用「代际利他」修补</b>"],
        ],
        note="<b>评价的标准句式</b>：<b>「李嘉图等价在四条件下成立；现实中至少三条明显不成立，因此它更像一个基准而非描述。但它的价值在于：它告诉我们——<b>减税要真的有效，必须依赖某一个摩擦（借贷约束／短视／扭曲税）</b>。」</b>",
        first_col_bold=True,
    ),
]


# ============================ 概念速查 ============================
SUMMARY_ROWS = [
    ("本讲加的东西", "<b>一个主体（政府）</b>", "两个工具 <span class='mj'>G,T</span>＋一个融资 <span class='mj'>B</span>"),
    ("为什么在禀赋经济里做", "产出固定，挤出被逼到明面上", "机制看得最清"),
    ("政府流量约束", "<span class='mj'>G_{t}=T_{t}+B_{t}</span>；<span class='mj'>G_{t+1}+(1+r)B_{t}=T_{t+1}</span>", "<b>第二期没有 <span class='mj'>B_{t+1}</span></b>"),
    ("为什么没有 <span class='mj'>B_{t+1}</span>", "最后一期必须还清（无庞氏条件）", "「政府不能永远借新还旧」"),
    ("<b>政府 IBC</b>", "<span class='mj'>G_{t}+\\frac{G_{t+1}}{1+r}=T_{t}+\\frac{T_{t+1}}{1+r}</span>", "<b>与家庭同构</b>"),
    ("符号约定", "<span class='mj'>B&gt;0</span> 政府借；<span class='mj'>S&gt;0</span> 家庭贷", "<b>两者是同一笔钱的两端</b>"),
    ("家庭侧唯一改动", "<span class='mj'>Y\\to Y-T</span>", "欧拉方程<b>不变</b>"),
    ("为什么欧拉方程不变", "lump-sum 税不改变边际效用", "税只影响「能花多少」"),
    ("忽略 <span class='mj'>h(G)</span> 的理由", "偏好<b>可加可分</b>", "<span class='mj'>G</span> 不改变消费的边际效用"),
    ("<b>关键一步</b>", "把政府 IBC 代进家庭 IBC", "<b>税消失</b>"),
    ("<b>终极消费函数</b>", "<span class='mj'>C_{t}=C^{d}(Y_{t}-G_{t},Y_{t+1}-G_{t+1},r_{t})</span>", "<b>不含 <span class='mj'>T</span>、不含 <span class='mj'>B</span></b>"),
    ("「仿佛 <span class='mj'>T=G</span>」的含义", "<b>决策等价</b>，不是预算恒等", "「仿佛」不等于「等于」"),
    ("减税 1 块的账", "<span class='mj'>\\Delta T_{t+1}=1+r</span>，现值抵消", "<b>三行写完即满分</b>"),
    ("<b>李嘉图等价</b>", "<b>融资方式对支出变化的效应无关</b>", "Ricardo 提出、Barro 1974 形式化"),
    ("它<b>不</b>说什么", "<b>不说政府支出无效</b>", "<span class='mj'>G</span> 照样挤出 <span class='mj'>C</span>"),
    ("四个假设", "lump-sum／无借贷约束／前瞻／政府不长寿", "<b>每条都要会说「破了怎样」</b>"),
    ("<b>出清条件</b>", "<span class='mj'>S_{t}-B_{t}=0</span>", "<b>不是 <span class='mj'>S=0</span></b>（有政府了）"),
    ("<b>商品市场出清</b>", "<span class='mj'>Y_{t}=C_{t}+G_{t}</span>", "税在此抵消；<b>挤出的来源</b>"),
    ("均衡系统", "两条方程、外生四个", "<b>不需要知道 <span class='mj'>T</span> 与 <span class='mj'>B</span></b>"),
    ("解法顺序", "出清定 <span class='mj'>C</span> → 消费函数定 <span class='mj'>r</span> → IBC 定 <span class='mj'>C_{t+1}</span>", "与上一讲相同"),
    ("乘数（有 RE，<span class='mj'>r</span> 固定）", "<b>1</b>", "＝ IS 水平位移"),
    ("乘数（无 RE，<span class='mj'>r</span> 固定）", "<span class='mj'>\\frac{1}{1-\\mathrm{MPC}}</span>", "<b>需注明两个前提</b>"),
    ("乘数（一般均衡）", "<b>0</b>", "<b>与 RE 无关</b>"),
    ("两个乘数差在哪", "家庭有没有先扣 <span class='mj'>\\mathrm{MPC}\\cdot dG</span>", "「净注入 vs 放大倍数」互为倒数"),
    ("轮次的收敛条件", "<span class='mj'>\\mathrm{MPC}&lt;1</span>", "否则级数发散"),
    ("轮次发生在什么时候", "<b>同一期内</b>", "不是跨期"),
    ("<b>完全挤出</b>", "<span class='mj'>dC_{t}=-dG_{t}</span>", "恒等式推论，不靠偏好"),
    ("挤出的执行者", "<b>利率</b>", "利率让家庭「甘心」少花"),
    ("<span class='mj'>G_{t}\\uparrow</span>", "支出线↑、IS 右移、<b><span class='mj'>r\\uparrow</span></b>", "政府今天多借"),
    ("<span class='mj'>G_{t+1}\\uparrow</span>", "支出线↓、IS 左移、<b><span class='mj'>r\\downarrow</span></b>", "家庭今天多存"),
    ("为什么 <span class='mj'>G_{t+1}</span> 不挤出", "它不占用今天资源", "只改变 <span class='mj'>r</span>"),
    ("乘数为零的真正原因", "<b>禀赋经济（产出不能变）</b>", "<b>不是李嘉图等价</b>"),
    ("与 Topic 8 的区别", "那里有生产，IS 右移<b>产出会增加</b>", "别把结论串了"),
]


# ============================ 易错清单 ============================
PITFALLS = [
    ("「李嘉图等价说明财政政策无效」",
     "<b>错。</b>它只说<b>融资方式</b>（税 vs 债）无关。<b>政府支出 <span class='mj'>G</span> 上升照样把 <span class='mj'>C</span> 挤出去。</b><b>「融资无关」≠「支出无关」。</b>"),
    ("「乘数为零是因为李嘉图等价」",
     "<b>本讲最高频的错误。</b>课件原话：<b>not a consequence of Ricardian equivalence, but rather due to the endowment economy</b>。<b>产出不能变才是原因。</b>"),
    ("「挤出是因为利率上升」",
     "<b>因果颠倒。</b>挤出由 <span class='mj'>Y=C+G</span> 决定（<b>恒等式</b>）；<b>利率只是执行者</b>，作用是让家庭「甘心」少花。<b>没有利率，<span class='mj'>dC=-dG</span> 照样成立。</b>"),
    ("出清条件写成 <span class='mj'>S_{t}=0</span>",
     "<b>照抄上一讲。</b>有政府时是 <b><span class='mj'>S_{t}=B_{t}</span></b>。<b>只有政府不发债（平衡预算）时两者才重合。</b>"),
    ("第二期也写「发债 <span class='mj'>B_{t+1}</span>」",
     "<b>两期模型里最后一期必须还清债务</b>，<b>不能有 <span class='mj'>B_{t+1}</span></b>。<b>理由：无庞氏条件。</b>"),
    ("减税例子忘掉 <span class='mj'>(1+r)</span>",
     "今天减 1 ⇒ 明年必须<b>多收 <span class='mj'>1+r</span></b>（<b>本金＋利息</b>）。<b>写成「多收 1」会让现值不等，结论直接反过来。</b>"),
    ("把「税消失」理解成「税不重要」",
     "<b>错。</b>税<b>被 <span class='mj'>G</span> 完全决定了</b>，所以不该出现在决策规则里。<b>准确说法：「给定 <span class='mj'>G</span>，税的时序不影响决策」。</b>"),
    ("「仿佛 <span class='mj'>T=G</span>」说成「每期都相等」",
     "<b>是现值相等，不是每期相等。</b>某一年完全可以是「大赤字＋低税」。<b>课件用的是 as though（仿佛），不是 equal（等于）。</b>"),
    ("在欧拉方程里加上 <span class='mj'>T</span>",
     "<b>错。</b>lump-sum 税不改变边际效用 ⇒ <b>欧拉方程一个字都不改</b>。<b>只有比例税才会进欧拉方程。</b>"),
    ("把 <span class='mj'>1/(1-\\mathrm{MPC})</span> 当成唯一乘数",
     "<b>必须补两个前提</b>：<b>无李嘉图等价 ＋ <span class='mj'>r</span> 固定</b>。<b>缺一个，数值就变（1 或 0）。</b>"),
    ("把「乘数 ＝ 1」当成均衡结论",
     "<b>那是固定 <span class='mj'>r</span> 的局部均衡值</b>。<b>均衡里 <span class='mj'>Y</span> 一点没变（供给竖线）。</b>"),
    ("说「<span class='mj'>G_{t+1}</span> 上升也挤出私人消费」",
     "<b>不挤出。</b>它不占用<b>今天</b>的资源，<b>只改变 <span class='mj'>r</span></b>。<b><span class='mj'>C_{t}</span> 仍等于 <span class='mj'>Y_{t}-G_{t}</span>，没变。</b>"),
    ("<span class='mj'>G_{t+1}\\uparrow</span> 时把支出线画成上移",
     "<b>是下移。</b>未来净收入减少 ⇒ 一生财富下降 ⇒ 今天少花。<b>口诀：先问「谁的可支配收入变了、往哪变」。</b>"),
    ("把「轮次」当成跨期过程",
     "<b>课件强调 within a period</b>——<b>所有轮次都发生在同一时期内</b>。<b>写成「今年一轮、明年一轮」就错了。</b>"),
    ("把政府 <span class='mj'>B</span> 与家庭 <span class='mj'>S</span> 的符号搞混",
     "<b>家庭 <span class='mj'>S&gt;0</span> 是贷出；政府 <span class='mj'>B&gt;0</span> 是借入。</b><b>两者是同一笔钱的两端</b>，所以出清是 <span class='mj'>S=B</span> 而不是 <span class='mj'>S=-B</span>。"),
    ("把本讲结论照搬到 Topic 8",
     "<b>Topic 8 有生产，<span class='mj'>Y^{s}</span> 上斜</b> ⇒ IS 右移会<b>同时提高产出与利率</b>，<b>不会有「完全挤出」</b>。<b>答题别忘了加「在禀赋经济中」。</b>"),
]


# ============================ 自测 ============================
QUIZ = [
    ("<b>【概念】</b>写出政府的两条流量约束与政府 IBC。为什么第二期不能再发债 <span class='mj'>B_{t+1}</span>？",
     "<b>流量约束</b>：<span class='mj'>G_{t}=T_{t}+B_{t}</span>；<span class='mj'>G_{t+1}+(1+r_{t})B_{t}=T_{t+1}</span>。<br>"
     "<b>IBC</b>：<span class='mj'>G_{t}+\\frac{G_{t+1}}{1+r_{t}}=T_{t}+\\frac{T_{t+1}}{1+r_{t}}</span>（消去 <span class='mj'>B_{t}</span>）。<br><br>"
     "<b>为什么没有 <span class='mj'>B_{t+1}</span></b>：<b>模型只有两期，<span class='mj'>t+1</span> 是最后一期</b>。<b>没有下一期可以还债，所以必须在 <span class='mj'>t+1</span> 期把债务清零。</b><br><br>"
     "<b>一般化的说法</b>：这叫<b>横截条件／无庞氏条件</b>（no-Ponzi condition）——<b>政府不能靠永远借新还旧活下去</b>。<b>答题时两句都写，得分更稳。</b>"),

    ("<b>【推导】</b>说明「税消失」的完整推理链条。哪一步是李嘉图等价的关键假设？",
     "<b>链条</b>：<br>"
     "① 家庭 IBC：<span class='mj'>C_{t}+\\frac{C_{t+1}}{1+r}=(Y_{t}-T_{t})+\\frac{Y_{t+1}-T_{t+1}}{1+r}</span>；<br>"
     "② 重新分组，把税收项括出来：<span class='mj'>=Y_{t}+\\frac{Y_{t+1}}{1+r}-\\left[T_{t}+\\frac{T_{t+1}}{1+r}\\right]</span>；<br>"
     "③ 用政府 IBC 把方括号替换成 <span class='mj'>G_{t}+\\frac{G_{t+1}}{1+r}</span>；<br>"
     "④ 得 <span class='mj'>C_{t}+\\frac{C_{t+1}}{1+r}=(Y_{t}-G_{t})+\\frac{Y_{t+1}-G_{t+1}}{1+r}</span>，<b>税消失</b>；<br>"
     "⑤ 消费函数写成 <span class='mj'>C_{t}=C^{d}(Y_{t}-G_{t},Y_{t+1}-G_{t+1},r_{t})</span>。<br><br>"
     "<b>关键假设在第 ③ 步</b>：<b>家庭「知道并相信」政府 IBC 必须成立</b>——<b>即家庭是前瞻的、且政府不会赖账</b>。<b>这一条破了，第 ③ 步就不成立，等价随之失效。</b>"),

    ("<b>【算术】</b>政府把 <span class='mj'>T_{t}</span> 减 1，<span class='mj'>G</span> 不变。求 <span class='mj'>T_{t+1}</span> 的变化、家庭一生财富的变化、<span class='mj'>C_{t}</span> 与 <span class='mj'>S_{t}</span> 的变化。",
     "<b>① 政府 IBC</b>：<span class='mj'>\\Delta T_{t}+\\frac{\\Delta T_{t+1}}{1+r}=0</span>，<span class='mj'>\\Delta T_{t}=-1</span> ⇒ <b><span class='mj'>\\Delta T_{t+1}=1+r</span></b>。<br>"
     "<b>② 一生财富</b>：<span class='mj'>+1-\\frac{1+r}{1+r}=0</span> ⇒ <b>不变</b>。<br>"
     "<b>③ 消费</b>：<b><span class='mj'>\\Delta C_{t}=0</span></b>。<br>"
     "<b>④ 储蓄</b>：<span class='mj'>S_{t}=Y_{t}-T_{t}-C_{t}</span> ⇒ <b><span class='mj'>\\Delta S_{t}=+1</span></b>——<b>正好买下政府新发的债</b>。<br><br>"
     "<b>一句话</b>：<b>减税的效果只是「家庭投资组合里多了一张国债」</b>，<b>消费与产出都不动</b>。"),

    ("<b>【概念】</b>李嘉图等价的四个假设是什么？各自被违反后会发生什么？",
     "<b>① 税是一次性总付</b>：破了 ⇒ 替代效应 ⇒ 即使一生财富不变行为也变。<br>"
     "<b>② 没有借贷约束</b>：破了 ⇒ 减税把未来的钱提前给「最想花的人」⇒ 消费上升。<b>最现实的一条</b>。<br>"
     "<b>③ 家庭前瞻</b>：破了 ⇒ 减税被当成收入 ⇒ 乘数变成 <span class='mj'>1/(1-\\mathrm{MPC})</span>。<br>"
     "<b>④ 政府不比家庭活得久</b>：破了 ⇒ 债可推给后代 ⇒ 一生财富真增加。<b>Barro 用代际利他修补</b>。<br><br>"
     "<b>评价</b>：<b>它更像基准而非描述</b>；<b>但它告诉我们「减税要有效，必须依赖某个摩擦」</b>。"),

    ("<b>【图形】</b>跑一遍 <span class='mj'>G_{t}\\uparrow</span>：支出线怎么动（移动多少）？IS 怎么动？均衡 <span class='mj'>Y</span> 与 <span class='mj'>r</span> 怎么变？",
     "<b>支出线</b>：<b>上移 <span class='mj'>(1-\\mathrm{MPC})dG</span></b>（<b>不是 <span class='mj'>dG</span></b>）。<b>因为政府直接多买 <span class='mj'>dG</span>，但家庭因税负上升少花 <span class='mj'>\\mathrm{MPC}\\cdot dG</span>。</b><br>"
     "<b>IS</b>：<b>右移 <span class='mj'>dG</span></b>（<b>＝ 上移量 ÷ 斜率 <span class='mj'>(1-\\mathrm{MPC})</span></b>）。<br>"
     "<b>均衡</b>：<span class='mj'>Y^{s}</span> 不动 ⇒ <b><span class='mj'>Y_{t}</span> 不变</b>、<b><span class='mj'>r</span> 上升</b>。<br>"
     "<b>为什么 <span class='mj'>r</span> 上升</b>：政府多借 <span class='mj'>dG</span>，家庭只多存 <span class='mj'>\\mathrm{MPC}\\cdot dG</span> ⇒ <b>可贷资金供不应求</b>。<br>"
     "<b>最终</b>：<b><span class='mj'>C_{t}</span> 下降 <span class='mj'>dG</span></b>（完全挤出）。"),

    ("<b>【图形】</b>跑一遍 <span class='mj'>G_{t+1}\\uparrow</span>。为什么方向与上题完全相反？",
     "<b>支出线</b>：<b>下移</b>（未来净收入 <span class='mj'>Y_{t+1}-G_{t+1}</span> 下降 ⇒ 一生财富下降 ⇒ 今天少花）。<br>"
     "<b>IS</b>：<b>左移</b>。<b>均衡</b>：<span class='mj'>Y_{t}</span> 不变、<b><span class='mj'>r</span> 下降</b>。<br><br>"
     "<b>为什么相反</b>：<b>可贷资金的供需方向相反</b>——<span class='mj'>G_{t}\\uparrow</span> 是<b>政府今天多借</b>（需求↑ ⇒ <span class='mj'>r\\uparrow</span>）；<span class='mj'>G_{t+1}\\uparrow</span> 是<b>家庭今天多存</b>（供给↑ ⇒ <span class='mj'>r\\downarrow</span>），<b>政府今天并不多借</b>。<br><br>"
     "<b>注意</b>：<b>它不挤出今天的消费</b>——<span class='mj'>C_{t}=Y_{t}-G_{t}</span> 里没有 <span class='mj'>G_{t+1}</span>。<b>它只改变 <span class='mj'>r</span>。</b>"),

    ("<b>【推导】</b>推导「有 RE、<span class='mj'>r</span> 固定」下的乘数，并用「轮次」给出同样的结论。为什么正好是 1？",
     "<b>全微分</b>：<span class='mj'>Y^{d}=C^{d}(Y_{t}-G_{t},\\cdot)+G_{t}</span> ⇒ <span class='mj'>dY_{t}=\\mathrm{MPC}(dY_{t}-dG_{t})+dG_{t}</span> ⇒ <span class='mj'>dY_{t}=dG_{t}</span>，<b>乘数 ＝ 1</b>。<br><br>"
     "<b>轮次</b>：净注入 <span class='mj'>(1-\\mathrm{MPC})dG</span>，再按 <span class='mj'>1/(1-\\mathrm{MPC})</span> 放大 ⇒ <b><span class='mj'>(1-\\mathrm{MPC})\\times\\frac{1}{1-\\mathrm{MPC}}=1</span></b>。<br><br>"
     "<b>为什么正好 1</b>：<b>「净注入」与「放大倍数」互为倒数</b>——<b>家庭先扣掉的比例，正好等于轮次放大的比例</b>。<b>这不是巧合，是同一个 <span class='mj'>\\mathrm{MPC}</span> 在两个地方出现。</b>"),

    ("<b>【对比】</b>为什么无 RE 时乘数是 <span class='mj'>1/(1-\\mathrm{MPC})</span>？写出它的两个前提。",
     "<b>推导</b>：<span class='mj'>Y_{t}=C^{d}(Y_{t}-T_{t},r_{t})+G_{t}</span>，<b>赤字融资下 <span class='mj'>T_{t}</span> 不变</b> ⇒ <span class='mj'>dY_{t}=\\mathrm{MPC}\\cdot dY_{t}+dG_{t}</span> ⇒ <span class='mj'>\\frac{dY_{t}}{dG_{t}}=\\frac{1}{1-\\mathrm{MPC}}</span>。<br><br>"
     "<b>两个前提</b>：<b>(i) 没有李嘉图等价</b>（家庭不把未来的税算进今天）；<b>(ii) 实际利率固定</b>。<br><br>"
     "<b>机制差别</b>：<b>无 RE 时消费函数的自变量是 <span class='mj'>Y_{t}-T_{t}</span>，没有 <span class='mj'>G_{t}</span></b> ⇒ <b>家庭不会先扣掉 <span class='mj'>\\mathrm{MPC}\\cdot dG</span></b> ⇒ 乘数被放大。<br><br>"
     "<b>提醒</b>：<b>这两个乘数都是「固定 <span class='mj'>r</span>」的局部均衡值</b>，<b>在一般均衡里都会变成 0</b>。"),

    ("<b>【综合】</b>为什么均衡乘数是零？这个「零」是李嘉图等价造成的吗？请把两件事分开说。",
     "<b>不是。</b>课件原话：<b>not a consequence of Ricardian equivalence, but rather due to the assumption of an endowment economy where output cannot respond</b>。<br><br>"
     "<b>零的来源</b>：<span class='mj'>Y^{s}</span> 是<b>竖线</b> ⇒ <span class='mj'>Y_{t}</span> 由禀赋决定 ⇒ <span class='mj'>G_{t}</span> 多占一块，<span class='mj'>C_{t}</span> 就少一块（<span class='mj'>dC=-dG</span>）⇒ <b>产出不变 ⇒ 乘数为零</b>。<br><br>"
     "<b>李嘉图等价管的是另一件事</b>：<b>融资方式（税 vs 债）无关</b>。它影响的是<b>「IS 移动多远」</b>（乘数 1 还是 <span class='mj'>1/(1-\\mathrm{MPC})</span>），<b>不影响「最终产出变不变」</b>。<br><br>"
     "<b>所以四个格子的表要记住</b>：<b>只要 <span class='mj'>r</span> 内生，不管有没有 RE，乘数都是 0。</b>"),

    ("<b>【延伸】</b>用本讲框架评价：「政府减税会刺激消费」。在什么条件下这句话成立？",
     "<b>本讲（李嘉图等价）下：不成立。</b>减税 1 ⇒ 未来增税 <span class='mj'>1+r</span> ⇒ 现值抵消 ⇒ <span class='mj'>C_{t}</span> 不变、<span class='mj'>S_{t}</span> 上升 1。<br><br>"
     "<b>要让它成立，必须破坏四个假设之一</b>：<br>"
     "① <b>借贷约束</b>：想借钱的人拿到减税的钱会立刻花掉（<b>最现实、也最有政策含义</b>）；<br>"
     "② <b>短视</b>：把减税当收入（乘数变成 <span class='mj'>1/(1-\\mathrm{MPC})</span>）；<br>"
     "③ <b>扭曲性税收</b>：减税改变劳动／储蓄的相对价格；<br>"
     "④ <b>代际转移</b>：税推给后代（但 Barro 用代际利他反驳）。<br><br>"
     "<b>结论句式</b>：<b>「在完全前瞻且无摩擦的世界里减税无效；现实中它的效果取决于受约束家庭的比例」</b>——<b>这句话把理论与政策连起来了，是论述题的高分收尾。</b>"),
]


# ===== 考点标注：供 build_notes.py 渲染「页首徽标 + 本讲考点一览」=====
# k: final = 期末练习 Key Concepts（老师亲手划）／mid = 期中练习 Key Concepts
#    must  = 我横向整理判断的必背项（没有老师名录背书）
EXAM = {
    3:  [{"k": "final", "t": "政府两期流量预算约束（含 <span class='mj'>B_{t}</span>）", "ref": "q2b"}],
    4:  [{"k": "final", "t": "政府跨期预算约束 IBC：支出与税收的现值相等", "ref": "q2b"}],
    11: [{"k": "final", "t": "李嘉图等价的定义：融资方式不影响均衡", "ref": "q2a"}],
    12: [{"k": "final", "t": "李嘉图等价依赖的四个假设（破一个就失效）", "ref": "q2a"}],
    15: [{"k": "final", "t": "总意愿支出包含 <span class='mj'>G_{t}</span>：<span class='mj'>Y^{d}=C^{d}+G</span>", "ref": "q2h"}],
    16: [{"k": "final", "t": "无李嘉图等价时乘数 <span class='mj'>1/(1-\\mathrm{MPC})</span> 从哪来", "ref": "q2h"}],
    18: [{"k": "final", "t": "↑<span class='mj'>G_{t}</span> 的图：支出线只上移 <span class='mj'>(1-\\mathrm{MPC})dG</span>", "ref": "q2g"}],
    20: [{"k": "final", "t": "完全挤出 <span class='mj'>dC=-dG</span> ⇒ 乘数为零", "ref": "q2g"}],
}
