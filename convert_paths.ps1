Get-Content svn_utils_java_only.txt | ForEach-Object { $_.Replace("D:\AI-Clients\Agents-Only\JDownLoader2-AI\", "") } | Out-File -Encoding ASCII svn_utils_relative.txt
