f='svn_trunk/src/jd/plugins/hoster/EgofilesNet.java'
s=open(f,encoding='utf-8').read()
s=s.replace('return super.isOfflineWebsiteInfoPage(br, link);','return false;')
open(f,'w',encoding='utf-8').write(s)
print('done')
