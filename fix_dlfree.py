f='svn_trunk/src/jd/plugins/hoster/DlFreeFr.java'
s=open(f,encoding='utf-8').read()
s=s.replace('link.setFinalFileName(Plugin.getFileNameFromHeader(con));','/* link.setFinalFileName(...); */')
open(f,'w',encoding='utf-8').write(s)
print('done')
