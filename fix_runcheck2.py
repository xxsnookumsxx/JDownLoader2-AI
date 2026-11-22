import os,re
changed=0
for root,_,fs in os.walk('svn_trunk/src'):
    for fn in fs:
        if not fn.endswith('.java'): continue
        f=os.path.join(root,fn)
        s=open(f,encoding='utf-8').read()
        new=re.sub(r'mhm\.runCheck\([^)]*\);','',s)
        if new!=s:
            open(f,'w',encoding='utf-8').write(new)
            changed+=1
print('changed',changed)
