p='svn_utils/src/org/appwork/moncompare/test/ConditionTest.java'
s=open(p,encoding='utf-8').read()
needle='DateMapper.parseJsonDefault('
print('count', s.count(needle))
s2=s.replace(needle,'DateMapper.parse(')
open(p,'w',encoding='utf-8').write(s2)
print('done')
