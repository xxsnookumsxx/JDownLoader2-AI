import re
from pathlib import Path

base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")

# Fix setInvalid/setValid/setUnused method signatures - should take AbstractResponse<T> not AbstractResponse<?>
files_to_fix = [
    r"org\jdownloader\captcha\v2\solver\antiCaptchaCom\AntiCaptchaComSolver.java",
    r"org\jdownloader\captcha\v2\solver\cheapcaptcha\CheapCaptchaSolver.java",
    r"org\jdownloader\captcha\v2\solver\dbc\DeathByCaptchaSolver.java",
    r"org\jdownloader\captcha\v2\solver\endcaptcha\EndCaptchaSolver.java",
    r"org\jdownloader\captcha\v2\solver\imagetyperz\ImageTyperzCaptchaSolver.java",
    r"org\jdownloader\captcha\v2\solver\solver9kw\AbstractCaptcha9kwSolver.java",
    r"org\jdownloader\captcha\v2\solver\twocaptcha\TwoCaptchaSolver.java",
]

for rel_file in files_to_fix:
    filepath = base_path / rel_file
    if not filepath.exists():
        continue
    
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    fixed = False
    
    # Fix setInvalid(AbstractResponse<?>) -> setInvalid(AbstractResponse<T>)
    old1 = 'setInvalid(AbstractResponse<?>)'
    new1 = 'setInvalid(AbstractResponse<T>)'
    if old1 in content:
        content = content.replace(old1, new1)
        fixed = True
    
    old2 = 'setUnused(AbstractResponse<?>)'
    new2 = 'setUnused(AbstractResponse<T>)'
    if old2 in content:
        content = content.replace(old2, new2)
        fixed = True
    
    old3 = 'setValid(AbstractResponse<?>)'
    new3 = 'setValid(AbstractResponse<T>)'
    if old3 in content:
        content = content.replace(old3, new3)
        fixed = True
    
    if fixed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed method signatures in {rel_file}")

print("Done fixing setInvalid/setValid/setUnused signatures.")
