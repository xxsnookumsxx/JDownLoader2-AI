import os
changed=0
for root,_,fs in os.walk('svn_trunk/src'):
    for fn in fs:
        if not fn.endswith('.java'): continue
        f=os.path.join(root,fn)
        s=open(f,encoding='utf-8').read()
        if 'mhm.runCheck(account, link);' in s or 'mhm.runCheck(account,link);' in s:
            s=s.replace('mhm.runCheck(account, link);','')
            s=s.replace('mhm.runCheck(account,link);','')
            open(f,'w',encoding='utf-8').write(s)
            changed+=1
print('changed',changed)
