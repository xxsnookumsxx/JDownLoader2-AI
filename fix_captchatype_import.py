import re
from pathlib import Path

base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")

# Files that need CAPTCHA_TYPE import added
files_needing_import = [
    r"org\jdownloader\captcha\v2\solver\antiCaptchaCom\AntiCaptchaComSolver.java",
    r"org\jdownloader\captcha\v2\solver\cheapcaptcha\CheapCaptchaSolver.java",
    r"org\jdownloader\captcha\v2\solver\dbc\DeathByCaptchaSolver.java",
    r"org\jdownloader\captcha\v2\solver\endcaptcha\EndCaptchaSolver.java",
    r"org\jdownloader\captcha\v2\solver\imagetyperz\ImageTyperzCaptchaSolver.java",
    r"org\jdownloader\captcha\v2\solver\solver9kw\Captcha9kwSolver.java",
    r"org\jdownloader\captcha\v2\solver\solver9kw\Captcha9kwSolverClick.java",
    r"org\jdownloader\captcha\v2\solver\solver9kw\Captcha9kwSolverMultiClick.java",
    r"org\jdownloader\captcha\v2\solver\solver9kw\Captcha9kwSolverPuzzle.java",
    r"org\jdownloader\captcha\v2\solver\twocaptcha\TwoCaptchaSolver.java",
    r"org\jdownloader\captcha\v2\challenge\keycaptcha\KeyCaptchaDialogSolver.java",
    r"org\jdownloader\captcha\v2\challenge\keycaptcha\jac\KeyCaptchaJACSolver.java",
    r"org\jdownloader\captcha\v2\solver\gui\DialogClickCaptchaSolver.java",
]

import_line = 'import jd.plugins.CaptchaType.CAPTCHA_TYPE;'

for rel_file in files_needing_import:
    filepath = base_path / rel_file
    if not filepath.exists():
        continue
    
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    if 'import jd.plugins.CaptchaType.CAPTCHA_TYPE;' in content:
        continue
    
    # Find position after last import line
    lines = content.split('\n')
    insert_pos = 0
    for i, line in enumerate(lines):
        if line.startswith('import '):
            insert_pos = i + 1
    
    lines.insert(insert_pos, import_line)
    content = '\n'.join(lines)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Added CAPTCHA_TYPE import to {rel_file}")

print("Done adding CAPTCHA_TYPE imports.")
