$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$outDir = Join-Path $root "portfolio"
$runtimeDir = Join-Path $outDir "runtime"

if (Test-Path $runtimeDir) { Remove-Item -Path $runtimeDir -Recurse -Force }
New-Item -Path $runtimeDir -ItemType Directory | Out-Null

$unsupportedModules = @("tkinter", "turtle", "smtplib", "pyperclip")
$browserPackages = @{ pandas = "pandas"; requests = "requests" }
$stdlibAllow = @("random", "time", "math", "json", "datetime", "os", "sys", "csv", "re", "itertools", "string", "collections")
$assetExt = @(".txt", ".csv", ".json")

function Get-Imports([string]$filePath) {
  $imports = @()
  foreach ($line in Get-Content -Path $filePath) {
    if ($line -match '^\s*import\s+(.+)$') {
      ($Matches[1] -split ',') | ForEach-Object {
        $mod = (($_ -split '\s+as\s+')[0].Trim().Split('.')[0])
        if ($mod) { $imports += $mod }
      }
    } elseif ($line -match '^\s*from\s+([A-Za-z0-9_\.]+)\s+import\s+') {
      $mod = $Matches[1].Split('.')[0]
      if ($mod) { $imports += $mod }
    }
  }
  return ($imports | Select-Object -Unique)
}

$moduleIndex = @{}
Get-ChildItem -Path $root -Recurse -Filter *.py -File |
  Where-Object { $_.FullName -notmatch '\\__pycache__\\' -and $_.FullName -notmatch '\\portfolio\\' } |
  ForEach-Object {
    $name = [IO.Path]::GetFileNameWithoutExtension($_.Name)
    if (-not $moduleIndex.ContainsKey($name)) { $moduleIndex[$name] = New-Object System.Collections.Generic.List[object] }
    $moduleIndex[$name].Add($_)
  }

function Find-BundleCandidate([string]$moduleName, [string]$projectDir) {
  if (-not $moduleIndex.ContainsKey($moduleName)) { return $null }
  $candidates = $moduleIndex[$moduleName] | Where-Object { $_.DirectoryName -ne $projectDir }
  if (-not $candidates) { return $null }

  $projectParts = $projectDir.Split([IO.Path]::DirectorySeparatorChar)
  $scored = foreach ($c in $candidates) {
    $score = 0
    $cParts = $c.DirectoryName.Split([IO.Path]::DirectorySeparatorChar)
    $common = 0
    $limit = [Math]::Min($projectParts.Count, $cParts.Count)
    for ($i=0; $i -lt $limit; $i++) {
      if ($projectParts[$i] -eq $cParts[$i]) { $common += 1 } else { break }
    }
    $score += ($common * 10)
    $score -= ($c.FullName.Length / 100)
    [pscustomobject]@{ candidate = $c; score = $score }
  }
  return ($scored | Sort-Object score -Descending | Select-Object -First 1).candidate
}

$idx = 0
$projects = Get-ChildItem -Path $root -Recurse -Filter main.py -File |
  Where-Object { $_.DirectoryName -notmatch '\\__pycache__$' -and $_.FullName -notmatch '\\portfolio\\' } |
  ForEach-Object {
    $idx += 1
    $dir = $_.DirectoryName
    $rel = $dir.Substring($root.Length + 1)
    $parts = $rel -split '\\'
    $track = if ($parts[0] -eq 'Intermediate+') { 'Intermediate+' } elseif ($parts[0]) { $parts[0] } else { 'Other' }
    $name = $parts[-1]

    $projectPyFiles = Get-ChildItem -Path $dir -Recurse -Filter *.py -File | Where-Object { $_.FullName -notmatch '\\__pycache__\\' }
    $projectAssets = Get-ChildItem -Path $dir -Recurse -File | Where-Object { $assetExt -contains $_.Extension.ToLowerInvariant() }

    $localModules = @{}
    foreach ($f in $projectPyFiles) {
      $base = [IO.Path]::GetFileNameWithoutExtension($f.Name)
      if ($base -and $base -ne '__init__') { $localModules[$base] = $true }
    }

    $bundledFiles = New-Object System.Collections.Generic.List[object]
    $requiredPackages = New-Object System.Collections.Generic.List[string]
    $reasons = New-Object System.Collections.Generic.List[string]

    $toProcess = New-Object System.Collections.Generic.Queue[string]
    $seenImports = @{}
    foreach ($py in $projectPyFiles) {
      foreach ($mod in (Get-Imports $py.FullName)) {
        if (-not $seenImports.ContainsKey($mod)) { $toProcess.Enqueue($mod); $seenImports[$mod] = $true }
      }
    }

    while ($toProcess.Count -gt 0) {
      $mod = $toProcess.Dequeue()
      if ($unsupportedModules -contains $mod) { $reasons.Add("Uses desktop/runtime module: $mod"); continue }
      if ($stdlibAllow -contains $mod) { continue }
      if ($localModules.ContainsKey($mod)) { continue }

      if ($browserPackages.ContainsKey($mod)) {
        if (-not $requiredPackages.Contains($browserPackages[$mod])) { $requiredPackages.Add($browserPackages[$mod]) }
        continue
      }

      $candidate = Find-BundleCandidate -moduleName $mod -projectDir $dir
      if ($null -ne $candidate) {
        $base = [IO.Path]::GetFileNameWithoutExtension($candidate.Name)
        if (-not $localModules.ContainsKey($base)) {
          $localModules[$base] = $true
          $bundledFiles.Add([pscustomobject]@{ sourcePath = $candidate.FullName; targetPath = "$base.py" })
          foreach ($sub in (Get-Imports $candidate.FullName)) {
            if (-not $seenImports.ContainsKey($sub)) { $toProcess.Enqueue($sub); $seenImports[$sub] = $true }
          }
        }
      } else {
        $reasons.Add("Missing module for web runtime: $mod")
      }
    }

    $reasons = $reasons | Select-Object -Unique
    $webRunnable = $reasons.Count -eq 0

    $allImports = @()
    foreach ($py in $projectPyFiles) { $allImports += Get-Imports $py.FullName }
    $allImports = $allImports | Select-Object -Unique

    $tags = New-Object System.Collections.Generic.List[string]
    foreach($m in @('tkinter','pandas','turtle','smtplib','json','random','pyperclip','time','math','requests')){
      if($allImports -contains $m -and -not $tags.Contains($m)) { $tags.Add($m) }
    }

    $lower = $name.ToLowerInvariant()
    $type = if($tags.Contains('tkinter')){'Desktop GUI'} elseif($tags.Contains('turtle')){'Game / Visualization'} elseif($tags.Contains('pandas')){'Data Project'} elseif($lower -match 'email|mail'){'Automation'} elseif($lower -match 'game|hangman|blackjack|pong|snake|race'){'Game'} else {'CLI App'}

    $runtimeFile = $null
    if ($webRunnable) {
      $webFiles = @()
      foreach ($py in $projectPyFiles) {
        $target = $py.FullName.Substring($dir.Length + 1) -replace '\\','/'
        $webFiles += [pscustomobject]@{ path = $target; code = [IO.File]::ReadAllText($py.FullName) }
      }
      foreach ($a in $projectAssets) {
        $target = $a.FullName.Substring($dir.Length + 1) -replace '\\','/'
        $webFiles += [pscustomobject]@{ path = $target; code = [IO.File]::ReadAllText($a.FullName) }
      }
      foreach ($b in $bundledFiles) {
        $webFiles += [pscustomobject]@{ path = $b.targetPath; code = [IO.File]::ReadAllText($b.sourcePath) }
      }

      $slug = ($rel -replace '[^A-Za-z0-9\-_/ ]','') -replace '[ /]+','-' 
      $runtimeFile = "runtime/$slug-$idx.json"
      $webFiles | ConvertTo-Json -Depth 5 | Set-Content -Path (Join-Path $outDir $runtimeFile) -Encoding UTF8
    }

    [pscustomobject]@{
      name = $name
      path = $rel -replace '\\','/'
      track = $track
      kind = $type
      tags = $tags
      run = "cd `"$rel`" && py main.py"
      webRunnable = $webRunnable
      webReason = if ($webRunnable) { '' } else { ($reasons -join '; ') }
      webPackages = $requiredPackages
      bundleCount = $bundledFiles.Count
      runtimeFile = $runtimeFile
    }
  } | Sort-Object track, name

$projects | ConvertTo-Json -Depth 7 | Set-Content -Path (Join-Path $outDir 'projects.json') -Encoding UTF8
Write-Output "Generated projects.json. Total: $($projects.Count), web-runnable: $(($projects | Where-Object {$_.webRunnable}).Count)"

