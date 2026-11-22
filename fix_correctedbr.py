import os
repls = [
 ("new Regex(correctedBR,", "new Regex((String) null,"),
 ("this.getDllink(link, account, br, correctedBR)", "this.getDllink(link, account, br, (String) null)"),
 ("this.getDllink(link, account, br,correctedBR)", "this.getDllink(link, account, br, (String) null)"),
]
changed=0
for root,_,fs in os.walk('svn_trunk/src'):
    for fn in fs:
        if not fn.endswith('.java'): continue
        f=os.path.join(root,fn)
        s=open(f,encoding='utf-8').read()
        orig=s
        for a,b in repls:
            s=s.replace(a,b)
        if s!=orig:
            open(f,'w',encoding='utf-8').write(s)
            changed+=1
print('changed',changed)
