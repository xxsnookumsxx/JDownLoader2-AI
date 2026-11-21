import re
from pathlib import Path

base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")

# Fix AbstractBrowserSolver.java - List<CAPTCHA_TYPE> return type mismatch
filepath = base_path / r"org\jdownloader\captcha\v2\solver\browser\AbstractBrowserSolver.java"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

old = 'public List<CAPTCHA_TYPE> getSupportedCaptchaTypes()'
new = 'public Set<CAPTCHA_TYPE> getSupportedCaptchaTypes()'
if old in content:
    content = content.replace(old, new)
    print(f"Fixed AbstractBrowserSolver.java return type")
    
    # Need to add Set import
    if 'import java.util.Set;' not in content:
        lines = content.split('\n')
        insert_pos = 0
        for i, line in enumerate(lines):
            if line.startswith('import java.util.'):
                insert_pos = i + 1
        lines.insert(insert_pos, 'import java.util.Set;')
        content = '\n'.join(lines)
        print(f"Added Set import to AbstractBrowserSolver.java")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Fix DialogClickCaptchaSolver.java - List<CAPTCHA_TYPE> return type mismatch
filepath = base_path / r"org\jdownloader\captcha\v2\solver\gui\DialogClickCaptchaSolver.java"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

old = 'public List<CAPTCHA_TYPE> getSupportedCaptchaTypes()'
new = 'public Set<CAPTCHA_TYPE> getSupportedCaptchaTypes()'
if old in content:
    content = content.replace(old, new)
    print(f"Fixed DialogClickCaptchaSolver.java return type")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done fixing type mismatches.")
