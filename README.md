# files-hub · 我的跨设备文件库

把散落在本机各处的文件 / 文件夹集中托管到 GitHub，并通过 GitHub Pages 在任意设备的浏览器里查看、下载。

**网页入口**：<https://fengbu12-design.github.io/files-hub/>

## 两条硬规则

**1. 上传前必须过隐私检查。** `publish.ps1` 会先跑 `tools/scan-privacy.mjs`，扫描：

- 密钥：OpenAI/Anthropic `sk-…`、GitHub token、AWS/Google/Slack Key、私钥、JWT、`api_key = "…"`
- 个人信息：邮箱、手机号、身份证/学号格式、`姓名：xxx`、学校名（xx大学/xx学院/xx University）
- 文档属性：Word/Excel/PPT 里的「作者 / 最后修改人 / 公司」，PDF 里 XMP 的 `dc:creator`
- 文件名、目录名本身也会被检查

有发现就**停下**并列出原文，等人判断。确认没问题才加 `-Force` 继续。密钥一律打码显示。

正则和自定义词表放在 `_private/privacy-rules.json`（已 gitignore，不随仓库上传），把自己的姓名、学校、学号前缀填进去。

**2. 名字要低调。** 目录名用 `note-a1`、`hw-07` 这类别名，不要用「经济学笔记」「XX课程作业」这种一搜就中的描述。页面 `<meta name="robots" content="noindex">`，搜索引擎不索引。别名对应的真实来源和说明记在 `_private/map.json`（本地，不上传）。

## 目录结构

```
files-hub/
├─ index.html            # 自动生成的索引页（勿手改）
├─ _groups.json          # 可选：别名 -> 显示标题
├─ _previews/            # 自动生成的 PDF 预览（已抹掉元数据）
├─ tools/
│  ├─ build-site.mjs     # 扫描仓库，生成 index.html
│  ├─ publish.ps1        # 发布 / 下架 + 隐私检查 + 提交推送
│  ├─ scan-privacy.mjs   # 隐私扫描
│  └─ sanitize-pdf.mjs   # 抹掉 PDF 作者/标题元数据
├─ _private/             # 本地私密（规则、别名映射），已 gitignore
└─ <别名>/                # 每个来源一个顶层目录
```

## 发布一个文件夹

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File D:\deepseek\github-hub\tools\publish.ps1 `
  -Source "D:\某个位置\某作业" -Name "hw-07" -Title "作业 07"
```

| 参数 | 作用 |
| --- | --- |
| `-Name` | 仓库里的别名（默认取来源名，中文名会警告） |
| `-Title` | 网页上显示的标题，建议中性 |
| `-Force` | 隐私扫描有发现时仍然发布（人工已确认） |
| `-SkipScan` | 跳过隐私扫描（不建议） |
| `-NoPdf` | 跳过 Word/Excel/PPT 的 PDF 预览生成 |
| `-NoPush` | 只在本地准备，不推送 |

单个文件也可以发布，会落在仓库根目录。

## 下架

```powershell
...\publish.ps1 -Remove -Name "hw-07"
```

## 说明

- 仓库是**公开**的：拿到网址的人都能看。别名 + noindex 只是降低被搜到的概率，不是加密。
- 复制的源文件仍在原位置；改完源文件重新发布即可覆盖。
- 图片直接显示缩略图；`.docx/.xlsx/.pptx` 自动转 PDF，网页上多一个「在线阅读」按钮，PDF 元数据在转换后会被抹掉。
- 原 Office 文件里的作者属性不会自动清除（会破坏文件），扫描器会提醒，由人决定。
