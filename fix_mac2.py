f='svn_trunk/src/org/jdownloader/gui/GuiUtils.java'
s=open(f,encoding='utf-8').read()
s=s.replace('final com.apple.eawt.Application application = com.apple.eawt.Application.getApplication();','/* final Application application = null; */')
s=s.replace('if (application != null) {\n                    application.requestUserAttention(flashTray);\n                }','')
open(f,'w',encoding='utf-8').write(s)
print('done')
