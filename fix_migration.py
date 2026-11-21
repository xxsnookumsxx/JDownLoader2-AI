import re
from pathlib import Path

filepath = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src\jd\captcha\CaptchaSolverSettingsMigration.java")

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Comment out all non-existent method calls on CaptchaSolverPluginConfig
# Methods that don't exist: setDomainBlacklist, setDomainBlacklistEnabled, setDomainWhitelist, setDomainWhitelistEnabled

# Fix setDomainBlacklist calls
content = content.replace(
    'cfgNew.setDomainBlacklist(listToCommaSeparatedDomains(blacklist));',
    '// cfgNew.setDomainBlacklist(listToCommaSeparatedDomains(blacklist)); // Method does not exist on CaptchaSolverPluginConfig'
)

# Fix setDomainBlacklistEnabled calls
content = content.replace(
    'cfgNew.setDomainBlacklistEnabled(false);',
    '// cfgNew.setDomainBlacklistEnabled(false); // Method does not exist on CaptchaSolverPluginConfig'
)

# Fix setDomainWhitelist calls  
content = content.replace(
    'cfgNew.setDomainWhitelist(listToCommaSeparatedDomains(whitelist));',
    '// cfgNew.setDomainWhitelist(listToCommaSeparatedDomains(whitelist)); // Method does not exist on CaptchaSolverPluginConfig'
)

# Fix setDomainWhitelistEnabled calls
content = content.replace(
    'cfgNew.setDomainWhitelistEnabled(false);',
    '// cfgNew.setDomainWhitelistEnabled(false); // Method does not exist on CaptchaSolverPluginConfig'
)

# Clean up any garbled lines from previous failed fixes
# Fix lines that have "// // cfgNew.setDomainWhitelist("
content = content.replace(
    '// // cfgNew.setDomainWhitelist(  // Method does not exist  // Method does not exist on CaptchaSolverPluginConfiglistToCommaSeparatedDomains(whitelist));',
    '// cfgNew.setDomainWhitelist(listToCommaSeparatedDomains(whitelist)); // Method does not exist on CaptchaSolverPluginConfig'
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed CaptchaSolverSettingsMigration.java")
