$content = Get-Content -Encoding UTF8 svn_trunk_errors.txt -Raw
$lines = $content -split "`n" | Where-Object { $_ -like "*: error:*" }
$lines | Out-File -Encoding utf8 tmp_build\errors_only.txt
Write-Host ("Count: " + $lines.Count)
