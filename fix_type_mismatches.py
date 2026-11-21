import re
from pathlib import Path

base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")

# Fix DialogClickCaptchaSolver.java - List<CAPTCHA_TYPE> return type mismatch
filepath = base_path / r"org\jdownloader\captcha\v2\solver\gui\DialogClickCaptchaSolver.java"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('public List<CAPTCHA_TYPE> getSupportedCaptchaTypes()', 'public Set<CAPTCHA_TYPE> getSupportedCaptchaTypes()')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Fixed DialogClickCaptchaSolver.java")

# Fix AntiCaptchaComSolverService.java - getType() return type mismatch  
filepath = base_path / r"org\jdownloader\captcha\v2\solver\antiCaptchaCom\AntiCaptchaComSolverService.java"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Already fixed earlier, check again
content = content.replace('public String getType()', 'public SolverType getType()')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Fixed AntiCaptchaComSolverService.java getType()")

print("Done.")
