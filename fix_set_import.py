import re
from pathlib import Path

base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")

# Files missing specific imports - based on error analysis
files_needing_set = [
    r"org\jdownloader\captcha\v2\solver\gui\DialogClickCaptchaSolver.java",
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
]

for rel_file in files_needing_set:
    filepath = base_path / rel_file
    if not filepath.exists():
        continue
    
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    if 'import java.util.Set;' not in content and 'Set<' in content:
        lines = content.split('\n')
        insert_pos = 0
        for i, line in enumerate(lines):
            if line.startswith('import java.util.'):
                insert_pos = i + 1
        lines.insert(insert_pos, 'import java.util.Set;')
        content = '\n'.join(lines)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added Set import to {rel_file}")

print("Done adding Set imports.")
