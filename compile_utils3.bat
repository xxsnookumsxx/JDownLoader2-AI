@echo off
cd /d D:\AI-Clients\Agents-Only\JDownLoader2-AI
rmdir /s /q tmp_build 2>nul
mkdir tmp_build
set CP=svn_utils\dev_libs\jna.jar;svn_utils\dev_libs\jna-platform.jar;svn_utils\dev_libs\asm.jar;svn_utils\libs\miglayout-core.jar;svn_utils\libs\miglayout.jar;svn_utils\libs\jsvg.jar;svn_utils\libs\svgSalamander.jar;svn_utils\ant\joda-time-1.6.2.jar
javac -encoding UTF-8 --add-exports java.base/sun.security.x509=ALL-UNNAMED -cp "%CP%" -d tmp_build -sourcepath svn_utils/src @svn_utils_relative.txt 2> svn_utils_errors.txt
echo DONE
