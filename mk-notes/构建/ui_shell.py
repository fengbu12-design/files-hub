# -*- coding: utf-8 -*-
"""
ui_shell.py —— 四个页面共用的「外壳」：常驻导航、阅读进度条、页码跳转、上次位置。

为什么要单独一个模块：四套页面（十讲笔记 / 总复习 / 练习 / 主页）是四个独立引擎
生成的，以前每加一个公共部件就要改四处、还容易改漏。这里只写一份，各自 import。

提供的三样东西：
  CSS   —— 样式（含宽屏左列、窄屏右下角圆钮两套布局）
  html(current, order, paged) —— 导航骨架
  JS    —— 进度条、页码跳转、上次位置

用法：
    import ui_shell as U
    U.html(current="Topic 3 笔记.html", order=ORDER, paged=True)
"""
import html as _html
import os
import re
import urllib.parse

_TT = re.compile(r'^TOPIC_TITLE\s*=\s*"Topic\s*(\d+)\s*·\s*(.+?)"\s*$', re.M)


def titles(here=None):
    """只读各 content 文件前 4KB 抓 TOPIC_TITLE，不 import（import 十个大文件太慢）。"""
    here = here or os.path.dirname(os.path.abspath(__file__))
    out = {}
    for n in range(1, 11):
        p = os.path.join(here, f"content_topic{n}.py")
        if not os.path.exists(p):
            continue
        with open(p, encoding="utf-8") as f:
            head = f.read(4096)
        m = _TT.search(head)
        if m:
            out[int(m.group(1))] = m.group(2)
    return out


def order(here=None):
    return order_from_titles(titles(here))


# ---------- 全站顺序（上一份 / 下一份 按这个走） ----------
def order_from_titles(titles):
    """titles: {1: "增长事实与宏观核算", ...} → 有序的 (href, 简称, 全名) 列表"""
    out = [("index.html", "总台", "期末复习总台")]
    for n in sorted(titles):
        out.append((f"Topic {n} 笔记.html", f"T{n}", f"Topic {n} · {titles[n]}"))
    out.append(("期末总复习.html", "总复习", "期末总复习（横向重组）"))
    out.append(("期末练习.html", "练习", "期末练习精做"))
    return out


def _q(name):
    return urllib.parse.quote(name)


# 12 个内容页都在 网页/ 里，主页 index.html 在上一层；从内容页回主页要走出子目录。
# （目录约定统一写在 paths.py，这里重复一个字面量是为了让 ui_shell 能单独 import）
HOME = "../index.html"


def _u(name):
    """order 里的文件名 → 从 网页/ 出发的真实链接。只有主页需要加 ../"""
    return HOME if name == "index.html" else name


def _neigh(current, order):
    idx = None
    for i, it in enumerate(order):
        if it[0] == current:
            idx = i
            break
    prev = order[idx - 1] if idx not in (None, 0) else None
    nxt = order[idx + 1] if idx is not None and idx + 1 < len(order) else None
    return prev, nxt


CSS = """
/* ============ 共用外壳（ui_shell.py） ============ */
.rprog{position:fixed;left:0;top:0;height:3px;width:100%;z-index:1300;pointer-events:none;}
.rprog i{display:block;height:100%;width:0;background:linear-gradient(90deg,var(--accent,#2563eb),var(--accent2,#7c3aed));
 border-radius:0 3px 3px 0;transition:width .1s linear;}

.rail{position:fixed;left:max(14px,calc(50% - 620px));top:50%;transform:translateY(-50%);z-index:1100;
 display:flex;flex-direction:column;gap:6px;width:78px;}
.rail.bare{left:max(14px,calc(50% - 678px));width:78px;}
.tocbtn{display:none;}
/* 窄屏目录抽屉：1366/1440 这类笔记本以前根本看不到目录，现在点了就有 */
#toc.show{display:block!important;z-index:1250;right:12px;top:64px;width:min(280px,calc(100vw - 24px));
 max-height:min(72vh,560px);overflow:auto;box-shadow:0 12px 40px rgba(15,23,42,.25);}
.rbtn{display:flex;align-items:center;justify-content:center;gap:5px;height:34px;padding:0 6px;
 border-radius:10px;background:var(--card);border:1px solid var(--line);color:var(--ink2);
 font-size:12px;font-weight:700;text-decoration:none;cursor:pointer;font-family:inherit;
 box-shadow:0 1px 3px rgba(15,23,42,.07);transition:background .14s,color .14s,border-color .14s;}
.rbtn i{font-style:normal;font-size:14px;line-height:1;}
.rbtn:hover{background:#2563eb;border-color:#2563eb;color:#fff;text-decoration:none;}
.rsep{height:1px;background:var(--line);margin:1px 8px;}
.rjump input{width:100%;height:30px;text-align:center;border-radius:9px;border:1px dashed var(--line);
 background:var(--card2);color:var(--ink);font-size:12px;font-family:inherit;font-weight:700;
 box-shadow:0 1px 3px rgba(15,23,42,.07);}
.rjump input::placeholder{color:var(--muted);font-weight:600;}
.rjump input:focus{outline:none;border-color:var(--accent);box-shadow:0 0 0 2px rgba(37,99,235,.18);}
.rlast{display:block;text-align:center;font-size:11.5px;font-weight:800;color:var(--orange-ink,#b45309);
 background:var(--card);border:1px dashed var(--orange,#b45309);border-radius:9px;padding:5px 2px;
 text-decoration:none;letter-spacing:.2px;}
.rlast:hover{background:#b45309;color:#fff;border-style:solid;text-decoration:none;}
[hidden]{display:none!important;}

@media (max-width:1419px){
 .rail{left:auto;right:14px;bottom:16px;top:auto;transform:none;width:auto;align-items:flex-end;}
 .rail .rbtn{width:40px;height:40px;border-radius:999px;padding:0;opacity:.94;
   background:var(--card);box-shadow:0 3px 12px rgba(15,23,42,.18);}
 .rail .rbtn span{display:none;}
 .rail .rsep,.rail .rjump,.rail .rprev,.rail .rnext,.rail .rlast{display:none!important;}
}
/* 1420–1519 这一段最尴尬：右侧目录被收起了，所以侧栏要给个目录按钮 */
@media (max-width:1519px){ .rail .tocbtn{display:flex;} }
@media (min-width:1520px){ .rail .tocbtn{display:none!important;} }
/* 页底「上一份 / 下一份」：读到最底下的人下一步一定是这个 */
.nextnav{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:40px 0 6px;}
.nextnav a{display:block;background:var(--card);border:1px solid var(--line);border-radius:12px;
 padding:14px 18px;text-decoration:none;color:var(--ink);transition:.15s;box-shadow:0 1px 3px rgba(15,23,42,.06);}
.nextnav a:hover{border-color:var(--accent);box-shadow:0 4px 14px rgba(37,99,235,.15);text-decoration:none;}
.nextnav .nl{display:block;font-size:12px;font-weight:700;color:var(--muted);margin-bottom:4px;letter-spacing:.3px;}
.nextnav .nt{display:block;font-size:14.5px;font-weight:800;line-height:1.5;}
.nextnav a.nx{text-align:right;background:var(--card);}
.nextnav a.nx .nl{color:var(--accent-ink,#1d4ed8);}
.nextnav a.nx .nt{color:var(--accent-ink,#1d4ed8);}
.nextnav a.pv .nt{color:var(--ink2);}
.nextnav a.solo{grid-column:1 / -1;text-align:left;}
@media (max-width:720px){ .nextnav{grid-template-columns:1fr;} .nextnav a.nx{text-align:left;} }
@media print{
 .rail,.rprog,.nextnav{display:none!important;}
}
"""


def html(current, order, paged=False, bare=False, toc=False):
    """current: 本页文件名（用来定位上一份/下一份）；order: order_from_titles 的返回；
    paged: 是否有 #p1..#pN 这种页锚点（只有十讲笔记有）；
    bare: 只出进度条 + 回顶按钮（主页用，主页自己就是导航）；
    toc: 本页右侧有 #toc 目录（窄屏时给一个展开抽屉的按钮）。"""
    prev, nxt = _neigh(current, order)
    # 首页由上面的「总台」按钮负责，不再重复一个「‹ 总台」
    if prev and prev[0] == "index.html":
        prev = None
    parts = ['<div class="rprog"><i id="rprogbar"></i></div>']
    if bare:
        parts.append('<nav class="rail bare" aria-label="页面导航">')
        parts.append('<a class="rbtn" href="#tagtable" title="跳到 99 条考点总表"><i>⌕</i><span>考点表</span></a>')
        parts.append('<button class="rbtn" type="button" onclick="window.scrollTo({top:0,behavior:\'smooth\'})" '
                     'title="回到页面顶部"><i>↑</i><span>顶部</span></button>')
        parts.append('</nav>')
        return "\n".join(parts)
    parts.append('<nav class="rail" aria-label="页面导航">')

    if current != "index.html":
        parts.append(f'<a class="rbtn rhome" href="{HOME}" title="回到复习总台（⌂）">'
                     '<i>⌂</i><span>总台</span></a>')

    if prev:
        parts.append(f'<a class="rbtn rprev" href="{_q(_u(prev[0]))}" title="上一份：{_html.escape(prev[2])}">'
                     f'<i>‹</i><span>{_html.escape(prev[1])}</span></a>')
    if nxt:
        parts.append(f'<a class="rbtn rnext" href="{_q(_u(nxt[0]))}" title="下一份：{_html.escape(nxt[2])}">'
                     f'<span>{_html.escape(nxt[1])}</span><i>›</i></a>')

    if paged:
        parts.append('<div class="rsep"></div>')
        parts.append('<form class="rjump" onsubmit="return window.__jumpPage(this)">'
                     '<input id="pgjump" type="text" inputmode="numeric" autocomplete="off" '
                     'placeholder="页码↵" title="输入页码回车，直接跳到那一页（如 37）" maxlength="3">'
                     '</form>')
        parts.append('<a class="rlast" id="rlast" href="#" hidden title="上次读到这里，点一下接着看"></a>')

    if toc:
        parts.append('<button class="rbtn tocbtn" type="button" '
                     'onclick="document.getElementById(\'toc\').classList.toggle(\'show\')" '
                     'title="展开 / 收起目录（窗口较窄时右侧目录是收起的）">'
                     '<i>☰</i><span>目录</span></button>')

    parts.append('<div class="rsep"></div>')
    parts.append('<button class="rbtn" type="button" onclick="window.scrollTo({top:0,behavior:\'smooth\'})" '
                 'title="回到页面顶部"><i>↑</i><span>顶部</span></button>')
    parts.append('</nav>')
    return "\n".join(parts)


def bottom(current, order):
    """页底的上一份 / 下一份导航。只有一份时返回空串。"""
    prev, nxt = _neigh(current, order)
    if prev and prev[0] == "index.html":
        prev = (prev[0], "复习总台", "回到复习总台")
    if not prev and not nxt:
        return ""
    out = ['<div class="nextnav">']
    if prev:
        out.append(f'<a class="pv" href="{_q(_u(prev[0]))}"><span class="nl">← 上一份</span>'
                   f'<span class="nt">{_html.escape(prev[2])}</span></a>')
    if nxt:
        out.append(f'<a class="nx" href="{_q(_u(nxt[0]))}"><span class="nl">下一份 →</span>'
                   f'<span class="nt">{_html.escape(nxt[2])}</span></a>')
    if prev and not nxt:
        out.append(f'<a class="nx solo" href="{HOME}"><span class="nl">全部读完了 →</span>'
                   '<span class="nt">回到复习总台，用考点总表再筛一遍</span></a>')
    out.append('</div>')
    return "".join(out)


def JS(paged=False):
    s = r"""
// ===== 外壳脚本（ui_shell.py）=====
(function(){
  // 1) 阅读进度条
  var bar=document.getElementById('rprogbar');
  function prog(){
    var h=document.documentElement.scrollHeight-window.innerHeight;
    var y=window.pageYOffset||document.documentElement.scrollTop;
    if(bar) bar.style.width=(h>0?Math.min(100,y/h*100):0)+'%';
  }
  // 2) 页码跳转：输入 37 → 跳到 #p37
  window.__jumpPage=function(f){
    var v=(f.querySelector('#pgjump')||{}).value||'';
    var n=parseInt(String(v).replace(/[^0-9]/g,''),10);
    if(!n) return false;
    var el=document.getElementById('p'+n);
    if(el){el.scrollIntoView({behavior:'smooth',block:'start'});history.replaceState(null,'','#p'+n);}
    else{alert('本讲只有 1 到 '+window.__PGMAX+' 页');}
    f.querySelector('#pgjump').value='';
    f.querySelector('#pgjump').blur();
    return false;
  };
  // 3) 记住读到哪一页（只对逐页笔记启用）
  var KEY='af5638_pos_'+encodeURIComponent(location.pathname.split('/').pop());
  var last=document.getElementById('rlast');
  function pageIds(){
    var a=[],i=1,el;
    while((el=document.getElementById('p'+i))){a.push(el);i++;}
    return a;
  }
  function savePos(){
    if(!window.__PAGED) return;
    var ps=pageIds(),cur=0;
    // 用 offsetTop（文档坐标）而不是 getBoundingClientRect：
    // 后者在滚动后可能读到旧布局，导致记错页码
    var y=(window.pageYOffset||document.documentElement.scrollTop)+160;
    for(var i=0;i<ps.length;i++){if(ps[i].offsetTop<=y)cur=i+1;}
    if(cur>1){try{localStorage.setItem(KEY,cur);}catch(e){}}
  }
  if(window.__PAGED){
    try{
      var saved=parseInt(localStorage.getItem(KEY)||'0',10);
      if(last&&saved>1&&document.getElementById('p'+saved)){
        last.textContent='上次 p'+saved;
        last.href='#p'+saved;
        last.hidden=false;
      }
    }catch(e){}
  }
  // 4) 窄屏目录抽屉：点条目后自动收起，点空白处也收起
  var tocEl=document.getElementById('toc');
  if(tocEl){
    tocEl.addEventListener('click',function(e){
      var a=e.target.closest?e.target.closest('a'):null;
      if(a) tocEl.classList.remove('show');
    });
    document.addEventListener('click',function(e){
      if(!tocEl.classList.contains('show')) return;
      if(tocEl.contains(e.target)) return;
      var b=e.target.closest?e.target.closest('.tocbtn'):null;
      if(b) return;
      tocEl.classList.remove('show');
    });
  }
  var t=null;
  window.addEventListener('scroll',function(){
    if(t) return;
    t=setTimeout(function(){prog();savePos();t=null;},90);
  },{passive:true});
  prog();
})();
"""
    return s
