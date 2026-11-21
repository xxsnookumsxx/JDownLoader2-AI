import re

path = r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src\jd\captcha\CaptchaSolverSettingsMigration.java"

with open(path, 'r') as f:
    content = f.read()

# Replace all uncommented setDomainWhitelist calls with commented versions
# Only match lines where setDomainWhitelist is NOT already commented
lines = content.split('\n')
new_lines = []
for line in lines:
    if 'cfgNew.setDomainWhitelist(' in line and not line.strip().startswith('//'):
        # Comment out this line
        new_lines.append(line.replace('cfgNew.setDomainWhitelist(', '// cfgNew.setDomainWhitelist(  // Method does not exist on CaptchaSolverPluginConfig'))
    else:
        new_lines.append(line)

with open(path, 'w') as f:
    f.write('\n'.join(new_lines))

print("Done. Replaced all uncommented setDomainWhitelist calls.")
