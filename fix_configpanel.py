import re
from pathlib import Path

filepath = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src\jd\gui\swing\jdgui\views\settings\panels\anticaptcha\AbstractCaptchaSolverConfigPanel.java")

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all _GUI.T.captcha_settings_*() calls with literal strings
replacements = {
    '_GUI.T.captcha_settings_black_whitelist_header()': '"Black/Whitelist Settings"',
    '_GUI.T.captcha_settings_black_whitelist_description()': '"Configure blacklist and whitelist settings"',
    '_GUI.T.captcha_settings_blacklist_enabled()': '"Enable Blacklist"',
    '_GUI.T.captcha_settings_blacklist()': '"Blacklist"',
    '_GUI.T.captcha_settings_whitelist()': '"Whitelist"',
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed AbstractCaptchaSolverConfigPanel.java")
