<#
.SYNOPSIS
  Publish any file or folder into the files-hub repo: copy it in, rebuild the
  index page, commit and push. Works with sources located anywhere on disk.

.EXAMPLE
  .\tools\publish.ps1 -Source "D:\Some\Folder" -Title "Statistics homework"

.EXAMPLE
  .\tools\publish.ps1 -Source "D:\Some\Folder" -Name "stats-hw" -NoPush

.EXAMPLE
  .\tools\publish.ps1 -Remove -Name "stats-hw"
#>
[CmdletBinding(DefaultParameterSetName = 'Publish')]
param(
  [Parameter(ParameterSetName = 'Publish', Mandatory = $true, Position = 0)]
  [string]$Source,

  [string]$Name,
  [string]$Title,

  # 不复制过去的文件名通配符，例如 -Exclude '*.zip','*.bak'
  [string[]]$Exclude,

  [Parameter(ParameterSetName = 'Unpublish', Mandatory = $true)]
  [switch]$Remove,

  [switch]$Force,
  [switch]$SkipScan,
  [switch]$NoPdf,
  [switch]$NoPush
)

$ErrorActionPreference = 'Stop'

$HubRoot = Split-Path -Parent $PSScriptRoot
$GitExe  = 'C:\Users\kkj2\AppData\Local\GitHubDesktop\app-3.6.11-beta1\resources\app\git\cmd\git.exe'
$env:GIT_TERMINAL_PROMPT = '0'
$env:GCM_INTERACTIVE = 'never'

$ExcludeDirs  = @('.git', 'node_modules', 'profile', 'state', 'failures', '__pycache__', '.venv', 'venv')
$ExcludeFiles = @('Thumbs.db', 'desktop.ini', '.DS_Store')


function Rebuild-Site {
    & node (Join-Path $HubRoot 'tools\build-site.mjs') $HubRoot
    if ($LASTEXITCODE -ne 0) { throw 'index build failed' }
}

# Word / Excel / PPT -> PDF so the page can offer in-browser reading.
function New-PdfPreviews {
    $LoCli  = 'D:\app\deepseek\resources\app.asar.unpacked\dsh\node_modules\@deepseek-ai\libreoffice-kit\lib\cli.js'
    $NodeExe = 'D:\app\deepseek\resources\runtime\primary-runtime\dependencies\node\bin\node.exe'
    if (-not (Test-Path $LoCli) -or -not (Test-Path $NodeExe)) {
        Write-Host 'pdf preview: converter not available, skipped'; return
    }
    $targets = Get-ChildItem -LiteralPath (Join-Path $HubRoot $Name) -Recurse -File -ErrorAction SilentlyContinue |
               Where-Object { $_.Extension -in @('.docx', '.xlsx', '.pptx') }
    foreach ($f in $targets) {
        $rel = $f.FullName.Substring($HubRoot.Length + 1).Replace('\', '/')
        $pdfRel  = '_previews/' + ($rel -replace '\.[^./]+$', '') + '.pdf'
        $pdfFull = Join-Path $HubRoot ($pdfRel.Replace('/', '\'))
        New-Item -ItemType Directory -Path (Split-Path $pdfFull) -Force | Out-Null
        try {
            & $NodeExe $LoCli convert --input $f.FullName --output $pdfFull 2>$null
        } catch { }
        if ((Test-Path $pdfFull) -and ((Get-Item $pdfFull).Length -gt 1000)) {
            # 转换会把文档作者写进 PDF 元数据，这里等长抹掉，保持 xref 偏移不变
            & node (Join-Path $HubRoot 'tools\sanitize-pdf.mjs') $pdfFull 2>$null | Out-Null
            Write-Host "pdf: $pdfRel"
        } else {
            Write-Host "pdf FAILED: $rel"
        }
    }
}

function Set-GroupTitle {
    param([string]$Key, [string]$Value)

    $p = Join-Path $HubRoot '_groups.json'
    $map = @{}
    if (Test-Path $p) {
        try {
            $obj = (Get-Content $p -Raw -Encoding UTF8).TrimStart([char]0xFEFF) | ConvertFrom-Json
            foreach ($prop in $obj.PSObject.Properties) { $map[$prop.Name] = [string]$prop.Value }
        } catch { $map = @{} }
    }

    if ($Value) { $map[$Key] = $Value } else { [void]$map.Remove($Key) }

    if ($map.Count -eq 0) {
        if (Test-Path $p) { Remove-Item $p -Force }
        return
    }
    $json = $map | ConvertTo-Json
    [System.IO.File]::WriteAllText($p, $json, (New-Object System.Text.UTF8Encoding($false)))
}

function Save-Map {
    param([string]$Key, [string]$SourcePath, [string]$Title)

    $dir = Join-Path $HubRoot '_private'
    if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }
    $p = Join-Path $dir 'map.json'
    $map = @{}
    if (Test-Path $p) {
        try {
            $obj = (Get-Content $p -Raw -Encoding UTF8).TrimStart([char]0xFEFF) | ConvertFrom-Json
            foreach ($prop in $obj.PSObject.Properties) { $map[$prop.Name] = $prop.Value }
        } catch { $map = @{} }
    }
    $old = $map[$Key]
    $entry = [ordered]@{
        source = if ($SourcePath) { $SourcePath } elseif ($old) { [string]$old.source } else { '' }
        title  = if ($Title) { $Title } elseif ($old) { [string]$old.title } else { '' }
        at     = (Get-Date).ToString('yyyy-MM-dd HH:mm')
    }
    $map[$Key] = [pscustomobject]$entry
    [System.IO.File]::WriteAllText($p, ($map | ConvertTo-Json -Depth 4), (New-Object System.Text.UTF8Encoding($false)))
}

function Escape-Segment([string]$s) { [uri]::EscapeDataString($s) }


$isFile = $false
if ($Remove) {
    if (-not $Name) { throw '-Remove requires -Name' }
    $dest = Join-Path $HubRoot $Name
    if (-not (Test-Path $dest)) { throw "not published: $Name" }
    Remove-Item $dest -Recurse -Force
    Set-GroupTitle -Key $Name -Value $null
    # 本地别名映射也一并删掉
    $mp = Join-Path $HubRoot '_private\map.json'
    if (Test-Path $mp) {
        try {
            $obj = (Get-Content $mp -Raw -Encoding UTF8).TrimStart([char]0xFEFF) | ConvertFrom-Json
            $map = @{}
            foreach ($prop in $obj.PSObject.Properties) { $map[$prop.Name] = $prop.Value }
            if ($map.ContainsKey($Name)) {
                [void]$map.Remove($Name)
                [System.IO.File]::WriteAllText($mp, ($map | ConvertTo-Json -Depth 4), (New-Object System.Text.UTF8Encoding($false)))
            }
        } catch { }
    }
    # 一并清掉该条目对应的 PDF 预览
    $prevDir = Join-Path $HubRoot ('_previews\' + $Name)
    if (Test-Path $prevDir) { Remove-Item $prevDir -Recurse -Force }
    Get-ChildItem -LiteralPath (Join-Path $HubRoot '_previews') -Filter "$Name.pdf" -File -ErrorAction SilentlyContinue |
        Remove-Item -Force
    Rebuild-Site
    $msg = "remove: $Name"
    Write-Host "unpublished: $Name"
}
else {
    if (-not (Test-Path -LiteralPath $Source)) { throw "source not found: $Source" }
    $item = Get-Item -LiteralPath $Source
    $isFile = -not $item.PSIsContainer
    if (-not $Name) { $Name = $item.Name }
    $dest = Join-Path $HubRoot $Name

    # 中文名字在公开仓库里太显眼，提醒换成中性别名
    if ($Name -match '[\u4e00-\u9fa5]') {
        Write-Warning "名称含中文「$Name」：别人一搜就到，建议用 -Name 换成 note-a1 这类别名"
    }

    # 隐私扫描：有发现就停下等人工判断；确认无碍后加 -Force 继续
    if (-not $SkipScan) {
        & node (Join-Path $HubRoot 'tools\scan-privacy.mjs') $item.FullName
        if ($LASTEXITCODE -eq 2) {
            if (-not $Force) {
                Write-Host ''
                Write-Host '已中止，没有上传任何文件。' -ForegroundColor Yellow
                Write-Host '  确认这些内容可以公开  -> 重跑并加 -Force' -ForegroundColor Yellow
                Write-Host '  确属误报 / 与该文件无关 -> 加 -SkipScan' -ForegroundColor Yellow
                exit 1
            }
            Write-Warning '隐私扫描有发现，按 -Force 继续发布'
        }
        elseif ($LASTEXITCODE -ne 0) { throw '隐私扫描执行失败' }
    }

    if ($item.PSIsContainer) {
        if (Test-Path $dest) { Remove-Item $dest -Recurse -Force }
        New-Item -ItemType Directory -Path $dest -Force | Out-Null
        $rc = @($item.FullName, $dest, '/E', '/NFL', '/NDL', '/NJH', '/NJS', '/NP', '/R:1', '/W:1', '/XD') +
              $ExcludeDirs + @('/XF') + $ExcludeFiles + @($Exclude | Where-Object { $_ })
        & robocopy @rc | Out-Null
        if ($LASTEXITCODE -ge 8) { throw "copy failed (robocopy $LASTEXITCODE)" }
    }
    else {
        if (Test-Path $dest) { Remove-Item $dest -Recurse -Force }
        Copy-Item -LiteralPath $item.FullName -Destination $dest -Force
    }

    # 复制进来的 PDF 同样洗掉作者/标题元数据（只改副本，源文件不动）
    $pdfs = @(Get-ChildItem -LiteralPath $dest -Recurse -File -Filter '*.pdf' -ErrorAction SilentlyContinue)
    if ($pdfs.Count) { & node (Join-Path $HubRoot 'tools\sanitize-pdf.mjs') @($pdfs.FullName) 2>$null | Out-Null }

    if ($Title) { Set-GroupTitle -Key $Name -Value $Title }
    Save-Map -Key $Name -SourcePath $item.FullName -Title $Title
    if (-not $NoPdf) { New-PdfPreviews }
    Rebuild-Site
    $msg = "add: $Name (from $($item.FullName))"
    Write-Host "published: $Name  <-  $($item.FullName)"
}

Push-Location $HubRoot
$prevEap = $ErrorActionPreference
# git 把进度和警告写到 stderr，在 EAP=Stop 下会被当成异常，这里降级后按退出码判断
$ErrorActionPreference = 'Continue'
try {
    & $GitExe add -A 2>$null
    $dirty = & $GitExe status --porcelain 2>$null
    if ($dirty) {
        & $GitExe commit -q -m $msg 2>$null
        Write-Host "committed: $msg"
        if (-not $NoPush) {
            & $GitExe push origin main 2>$null
            if ($LASTEXITCODE -ne 0) { throw 'git push failed' }
            Write-Host 'pushed to GitHub'
        }
        else { Write-Host 'skipped push (-NoPush)' }
    }
    else { Write-Host 'nothing changed' }
}
finally {
    $ErrorActionPreference = $prevEap
    Pop-Location
}

if (-not $Remove) {
    $seg = if ($isFile) { Escape-Segment $Name } else { (Escape-Segment $Name) + '/' }
    Write-Host ''
    Write-Host "Web: https://fengbu12-design.github.io/files-hub/$seg"
}
Write-Host "Repo: https://github.com/fengbu12-design/files-hub"
