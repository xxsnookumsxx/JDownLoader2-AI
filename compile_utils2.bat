@echo off
cd /d D:\AI-Clients\Agents-Only\JDownLoader2-AI
rmdir /s /q tmp_build 2>nul
mkdir tmp_build

set CP=svn_utils\dev_libs\jna.jar;svn_utils\dev_libs\jna-platform.jar;svn_utils\dev_libs\asm.jar;svn_utils\libs\miglayout-core.jar;svn_utils\libs\miglayout.jar;svn_utils\libs\jsvg.jar;svn_utils\libs\svgSalamander.jar;svn_utils\ant\joda-time-1.6.2.jar;svn_trunk\ressourcen\libs\jna.jar;svn_trunk\ressourcen\libs\jna_platform.jar;svn_trunk\ressourcen\libs\bcpkix-jdk15on.jar;svn_trunk\ressourcen\libs\bcprov-jdk15on.jar;svn_trunk\ressourcen\libs\bctls-jdk15on.jar;svn_trunk\ressourcen\libs\bcutil-jdk15on.jar;svn_trunk\ressourcen\libs\htmlunit-core-js.jar;svn_trunk\ressourcen\libs\image4j.jar;svn_trunk\ressourcen\libs\irclib.jar;svn_trunk\ressourcen\libs\jsyntaxpane.jar;svn_trunk\ressourcen\libs\laf\flatlaf.jar;svn_trunk\ressourcen\libs\proxyVole.jar;svn_trunk\ressourcen\libs\sequence-library.jar;svn_trunk\ressourcen\libs\sevenzipjbinding.jar;svn_trunk\ressourcen\libs\sqljet.jar;svn_trunk\ressourcen\libs\svnkit.jar;svn_trunk\ressourcen\libs\zip4j.jar;svn_trunk\ressourcen\libs\UPNP\cling-core.jar;svn_trunk\ressourcen\libs\UPNP\cling-support.jar;svn_trunk\ressourcen\libs\UPNP\seamless-http.jar;svn_trunk\ressourcen\libs\UPNP\seamless-util.jar;svn_trunk\ressourcen\libs\UPNP\seamless-xml.jar;svn_trunk\ressourcen\libs\antlr-runtime.jar;svn_trunk\ressourcen\libs\Filters.jar

javac -encoding UTF-8 -cp "%CP%" -d tmp_build -sourcepath svn_utils/src @svn_utils_relative.txt 2> svn_utils_errors.txt
echo ERRORS:
type svn_utils_errors.txt | find /c /v ""
