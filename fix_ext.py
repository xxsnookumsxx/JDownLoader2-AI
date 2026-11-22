f='svn_trunk/src/jd/plugins/hoster/File2btcCom.java'
s=open(f,encoding='utf-8').read()
s=s.replace('filetitle = this.correctOrApplyFileNameExtension(filetitle, ".mp4");','filetitle = filetitle;')
open(f,'w',encoding='utf-8').write(s)
print('done')
