@echo off
cd /d D:\AI-Clients\Agents-Only\JDownLoader2-AI
rmdir /s /q tmp_build 2>nul
mkdir tmp_build

set FILELIST=svn_utils_java_only.txt
set COUNT=0
set BATCH=0
set BATCHFILE=batch_%BATCH%.txt
echo. > %BATCHFILE%

for /f "usebackq delims=" %%f in (%FILELIST%) do (
    echo %%f >> %BATCHFILE%
    set /a COUNT+=1
    if %COUNT% geq 300 (
        echo Compiling batch %BATCH%...
        javac -encoding UTF-8 -d tmp_build -sourcepath svn_utils/src @%BATCHFILE% 2>> svn_utils_errors.txt
        set BATCHFILE=batch_%BATCH%.txt
        set /a BATCH+=1
        set COUNT=0
        echo. > %BATCHFILE%
    )
)

if exist %BATCHFILE% (
    for %%f in (%BATCHFILE%) do if %%~zf gtr 0 (
        echo Compiling final batch %BATCH%...
        javac -encoding UTF-8 -d tmp_build -sourcepath svn_utils/src @%BATCHFILE% 2>> svn_utils_errors.txt
    )
)

echo DONE compiling svn_utils
type svn_utils_errors.txt | find /c /v "" > error_count.txt
echo Errors found:
type error_count.txt
