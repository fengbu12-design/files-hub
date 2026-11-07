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

  [Parameter(ParameterSetName = 'Unpublish', Mandatory = $true)]
  [switch]$Remove,

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

function Escape-Segment([string]$s) { [uri]::EscapeDataString($s) }


$isFile = $false
if ($Remove) {
    if (-not $Name) { throw '-Remove requires -Name' }
    $dest = Join-Path $HubRoot $Name
    if (-not (Test-Path $dest)) { throw "not published: $Name" }
    Remove-Item $dest -Recurse -Force
    Set-GroupTitle -Key $Name -Value $null
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

    if ($item.PSIsContainer) {
        if (Test-Path $dest) { Remove-Item $dest -Recurse -Force }
        New-Item -ItemType Directory -Path $dest -Force | Out-Null
        $rc = @($item.FullName, $dest, '/E', '/NFL', '/NDL', '/NJH', '/NJS', '/NP', '/R:1', '/W:1', '/XD') +
              $ExcludeDirs + @('/XF') + $ExcludeFiles
        & robocopy @rc | Out-Null
        if ($LASTEXITCODE -ge 8) { throw "copy failed (robocopy $LASTEXITCODE)" }
    }
    else {
        if (Test-Path $dest) { Remove-Item $dest -Recurse -Force }
        Copy-Item -LiteralPath $item.FullName -Destination $dest -Force
    }

    if ($Title) { Set-GroupTitle -Key $Name -Value $Title }
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
