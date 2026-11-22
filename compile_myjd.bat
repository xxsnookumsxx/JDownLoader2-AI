@echo off
cd /d D:\AI-Clients\Agents-Only\JDownLoader2-AI
set CP=tmp_build;svn_browser\libs\brotli.jar;svn_utils\dev_libs\jna.jar;svn_utils\dev_libs\jna-platform.jar;svn_utils\dev_libs\asm.jar;svn_utils\libs\miglayout-core.jar;svn_utils\libs\miglayout.jar;svn_utils\libs\jsvg.jar;svn_utils\libs\svgSalamander.jar;svn_utils\ant\joda-time-1.6.2.jar
javac -encoding UTF-8 --add-exports java.base/sun.security.x509=ALL-UNNAMED -cp "%CP%" -d tmp_build -sourcepath svn_utils/src;svn_browser/src;svn_MyJDownloaderClient/src @svn_myjd_relative.txt 2> svn_myjd_errors.txt
echo DONE
