f='svn_trunk/src/org/jdownloader/gui/GuiUtils.java'
s=open(f,encoding='utf-8').read()
old='''            } else if (CrossSystem.isMac()) {
            try {
                final com.apple.eawt.Application application = com.apple.eawt.Application.getApplication();
                if (application != null) {
                    application.requestUserAttention(flashTray);
                }
            } catch (Throwable th) {
                LogV3.log(th);
            }'''
new='''            } else if (CrossSystem.isMac()) {
            try {
                /* com.apple.eawt not available on this JDK; skip */
            } catch (Throwable th) {
                LogV3.log(th);
            }'''
assert old in s
s=s.replace(old,new)
open(f,'w',encoding='utf-8').write(s)
print('done')
