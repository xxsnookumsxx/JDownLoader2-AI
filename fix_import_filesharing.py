import re, glob
files = [
 "svn_trunk/src/jd/plugins/hoster/File2btcCom.java",
 "svn_trunk/src/jd/plugins/hoster/FreeM3DownloadNet.java",
 "svn_trunk/src/jd/plugins/hoster/Mp4playerSite.java",
 "svn_trunk/src/jd/plugins/hoster/PimpRollHostedTube.java",
 "svn_trunk/src/jd/plugins/hoster/RarcloudsCom.java",
 "svn_trunk/src/jd/plugins/hoster/XingyaodiskCom.java",
]
for f in files:
    s=open(f,encoding='utf-8').read()
    s=s.replace("import jd.plugins.filesharing.FILENAME_SOURCE;","import jd.plugins.PluginForHost.FILENAME_SOURCE;")
    open(f,'w',encoding='utf-8').write(s)
print("done")
