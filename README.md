# files-hub · 我的跨设备文件库

把散落在本机各处的文件 / 文件夹集中托管到 GitHub，并通过 GitHub Pages 在任意设备的浏览器里查看、下载。

**网页入口**：<https://fengbu12-design.github.io/files-hub/>

## 目录结构

```
files-hub/
├─ index.html            # 自动生成的索引页（勿手改）
├─ _groups.json          # 可选：目录名 -> 中文标题
├─ _previews/            # 自动生成的 PDF 预览（Word/Excel/PPT）
├─ tools/
│  ├─ build-site.mjs     # 扫描仓库，生成 index.html
│  └─ publish.ps1        # 发布 / 下架 + 提交推送
└─ <你的文件夹>/          # 每个来源文件夹一个顶层目录
```

## 发布一个文件夹

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File D:\deepseek\github-hub\tools\publish.ps1 `
  -Source "D:\某个位置\某作业" -Title "统计作业"
```

可选参数：

| 参数 | 作用 |
| --- | --- |
| `-Name` | 在仓库里用的目录名，默认取来源文件夹名 |
| `-Title` | 网页上显示的中文标题（写入 `_groups.json`） |
| `-NoPdf` | 跳过 Word/Excel/PPT 的 PDF 预览生成 |
| `-NoPush` | 只在本地准备，不推送 |

单个文件也可以发布，会落在仓库根目录。

## 下架

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File D:\deepseek\github-hub\tools\publish.ps1 -Remove -Name "某作业"
```

## 说明

- 仓库是**公开**的：任何拿到网址的人都能看到文件，敏感内容（密码、Cookie、浏览器 profile 等）不要放进来。
- 复制的源文件仍在原位置，本仓库是副本；改完源文件重新发布即可覆盖。
- 图片直接显示缩略图；`.docx/.xlsx/.pptx` 会自动转 PDF，网页上多一个「在线阅读」按钮。
