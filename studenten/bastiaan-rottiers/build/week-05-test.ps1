param([ValidateSet('prepare','smoke','foutmarge','modellen','all')][string]$Mode = 'prepare')
$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
$local = Join-Path $root 'week-05-lokaal'
$null = New-Item -ItemType Directory -Force -Path $local
$utf8 = New-Object System.Text.UTF8Encoding($false)
function Save-Text($path,$value) { [IO.File]::WriteAllText($path,$value,$utf8) }
$testPath = Join-Path $root 'test-set.md'
$testText = [IO.File]::ReadAllText($testPath)
$cases = @()
foreach ($line in ($testText -split "`n")) {
  if ($line -match '^\| (T0[6-9]|T10) \| \*\*Titel:') {
    $parts = $line.Split('|')
    $cases += [pscustomobject]@{id=$parts[1].Trim();input=($parts[2].Trim() -replace '<br\s*/?>',"`n");expected=($parts[3].Trim() -replace '<br\s*/?>',"`n")}
  }
}
if ($cases.Count -ne 5) { throw 'Verwacht vijf testgevallen T06-T10.' }
Add-Type -AssemblyName System.IO.Compression.FileSystem
function Read-Docx($name) {
  $zip = [IO.Compression.ZipFile]::OpenRead((Join-Path $root $name))
  try {
    $reader = New-Object IO.StreamReader($zip.GetEntry('word/document.xml').Open())
    try { [xml]$xml = $reader.ReadToEnd() } finally { $reader.Dispose() }
    $ns = New-Object Xml.XmlNamespaceManager($xml.NameTable)
    $ns.AddNamespace('w','http://schemas.openxmlformats.org/wordprocessingml/2006/main')
    $paragraphs = foreach ($p in $xml.SelectNodes('//w:body//w:p',$ns)) {
      ($p.SelectNodes('.//w:t',$ns) | ForEach-Object InnerText) -join ''
    }
    return ($paragraphs -join "`n")
  } finally { $zip.Dispose() }
}
foreach ($case in $cases) {
  if ($case.id -eq 'T09') {
    foreach ($doc in @('leidraad-businessplan.docx','wattzak-businessplan-huidige-stand.docx')) { $case.input += "`n`n## Bijlage: $doc`n" + (Read-Docx $doc) }
  }
  if ($case.id -eq 'T10') { $case.input += "`n`n## Bijlage: sustainable-business-model-canvas.docx`n" + (Read-Docx 'sustainable-business-model-canvas.docx') }
}
$v7 = [IO.File]::ReadAllText((Join-Path $root 'prompt.md'))
$v6 = ($v7 -replace '^# Prompt v7','# Prompt v6 (gereconstrueerd op 27 oktober 2026)') -replace '(?m)^- Bij een voortgangsvergelijking geldt hetzelfde:.*\r?\n',''
Save-Text (Join-Path $root 'prompt-v6-gereconstrueerd.md') $v6
Save-Text (Join-Path $root 'prompt-v7.md') $v7
Save-Text (Join-Path $local 'cases.json') (ConvertTo-Json -InputObject $cases -Depth 5)
Save-Text (Join-Path $local 'testset.sha256') (Get-FileHash $testPath -Algorithm SHA256).Hash
$jobs = @()
foreach ($version in @('v6','v7')) {
  foreach ($run in 1..3) {
    foreach ($case in $cases) { $jobs += [pscustomobject]@{key="foutmarge-$version-r$run-$($case.id)";version=$version;run=$run;id=$case.id;model='gpt-6.1-sol';effort='medium';input=$case.input} }
  }
}
foreach ($setup in @(@{key='A';model='gpt-6.1-sol';effort='medium'},@{key='B';model='gpt-6-luna';effort='low'},@{key='C';model='gpt-6-astra';effort='medium'})) {
  foreach ($case in $cases) { $jobs += [pscustomobject]@{key="model-$($setup.key)-$($case.id)";version='v7';run=1;id=$case.id;model=$setup.model;effort=$setup.effort;input=$case.input} }
}
if ($Mode -eq 'prepare') { Write-Output "Voorbereid: $($jobs.Count) afzonderlijke tests; verwachte antwoorden blijven lokaal en worden niet meegestuurd."; exit }
if ($Mode -eq 'smoke') { $jobs = @($jobs[0]) }
if ($Mode -eq 'foutmarge') { $jobs = @($jobs | Where-Object { $_.key -like 'foutmarge-*' }) }
if ($Mode -eq 'modellen') { $jobs = @($jobs | Where-Object { $_.key -like 'model-*' }) }
$codex = (Get-Command codex.exe).Source
$active = New-Object Collections.ArrayList
$queue = New-Object Collections.Queue
foreach ($job in $jobs) { $queue.Enqueue($job) }
while ($queue.Count -or $active.Count) {
  while ($queue.Count -and $active.Count -lt 3) {
    $job = $queue.Dequeue()
    $metaPath = Join-Path $local ($job.key + '.meta.json')
    if (Test-Path $metaPath) {
      $prior = Get-Content $metaPath -Raw | ConvertFrom-Json
      if ($prior.exit_code -eq 0) { Write-Output "Bestaand: $($job.key)"; continue }
    }
    $work = Join-Path $local ($job.key + '-workspace')
    $null = New-Item -ItemType Directory -Force -Path $work
    $psi = New-Object Diagnostics.ProcessStartInfo
    $psi.FileName = $codex
    $psi.WorkingDirectory = $work
    $psi.Arguments = 'exec --ignore-user-config --ephemeral --skip-git-repo-check --json --color never -s read-only --disable shell_tool -c features.apply_patch_freeform=false -c features.multi_agent=false -c features.apps=false -c web_search="disabled" -c project_doc_max_bytes=0 -c model_reasoning_effort="' + $job.effort + '" -m ' + $job.model + ' -'
    $psi.UseShellExecute = $false
    $psi.CreateNoWindow = $true
    $psi.RedirectStandardInput = $true
    $psi.RedirectStandardOutput = $true
    $psi.RedirectStandardError = $true
    $psi.StandardOutputEncoding = $utf8
    $psi.StandardErrorEncoding = $utf8
    $process = New-Object Diagnostics.Process
    $process.StartInfo = $psi
    $null = $process.Start()
    $stdout = $process.StandardOutput.ReadToEndAsync()
    $stderr = $process.StandardError.ReadToEndAsync()
    $prompt = if ($job.version -eq 'v6') { $v6 } else { $v7 }
    $payload = $prompt + "`n`n## Ingevulde Input voor deze run`n" + $job.input + "`n`nBeantwoord alleen deze input. Gebruik geen tools, bestanden of internet. Geef uitsluitend de gevraagde uitvoer."
    Save-Text (Join-Path $local ($job.key + '.input.txt')) $payload
    $inputWriter = New-Object IO.StreamWriter($process.StandardInput.BaseStream,$utf8)
    $inputWriter.Write($payload)
    $inputWriter.Dispose()
    $null = $active.Add([pscustomobject]@{job=$job;process=$process;stdout=$stdout;stderr=$stderr;started=[DateTime]::UtcNow;metaPath=$metaPath})
    Write-Output "Gestart: $($job.key), $($job.model), $($job.effort)"
  }
  foreach ($entry in @($active.ToArray())) {
    if ($entry.process.HasExited) {
      $raw = $entry.stdout.GetAwaiter().GetResult()
      $err = $entry.stderr.GetAwaiter().GetResult()
      Save-Text (Join-Path $local ($entry.job.key + '.jsonl')) $raw
      Save-Text (Join-Path $local ($entry.job.key + '.stderr.txt')) $err
      $meta = [ordered]@{key=$entry.job.key;version=$entry.job.version;run=$entry.job.run;id=$entry.job.id;model=$entry.job.model;effort=$entry.job.effort;exit_code=$entry.process.ExitCode;seconds=([DateTime]::UtcNow-$entry.started).TotalSeconds;date_utc=$entry.started.ToString('o')}
      Save-Text $entry.metaPath ($meta | ConvertTo-Json)
      Write-Output "Afgerond: $($entry.job.key), exit $($entry.process.ExitCode)"
      $entry.process.Dispose()
      $active.Remove($entry)
    } elseif (([DateTime]::UtcNow-$entry.started).TotalSeconds -gt 240) {
      $entry.process.Kill()
      Write-Output "Tijdslimiet: $($entry.job.key)"
    }
  }
  if ($active.Count) { Start-Sleep -Milliseconds 400 }
}
if ((Get-FileHash $testPath -Algorithm SHA256).Hash -ne [IO.File]::ReadAllText((Join-Path $local 'testset.sha256'))) { throw 'Testset is veranderd.' }
