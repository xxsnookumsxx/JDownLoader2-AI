import re, glob
pat = re.compile(r'super\.checkErrors\(([^)]*?),\s*checkAll\)')
# generic: remove trailing ", checkAll" inside super.checkErrors call
files = []
import os
for root,_,fs in os.walk('svn_trunk/src'):
    for fn in fs:
        if fn.endswith('.java'):
            files.append(os.path.join(root,fn))
changed=0
for f in files:
    s=open(f,encoding='utf-8').read()
    # remove ', checkAll' only within super.checkErrors(...) calls
    new = re.sub(r'(super\.checkErrors\([^)]*?),\s*checkAll\)', r'\1)', s)
    if new!=s:
        open(f,'w',encoding='utf-8').write(new)
        changed+=1
print('changed', changed)
