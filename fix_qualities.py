f='svn_trunk/src/jd/plugins/hoster/ClipHunterCom.java'
s=open(f,encoding='utf-8').read()
s=s.replace('jd.plugins.decrypter.ClipHunterComDecrypt.qualities','new String[0][]')
open(f,'w',encoding='utf-8').write(s)
print('done')
