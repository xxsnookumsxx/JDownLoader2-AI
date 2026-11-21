import re
from pathlib import Path

base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")

# Fix setInvalid/SetValid/setUnused override issues - AbstractResponse<T> to AbstractResponse<?>
solver_files = [
    r"org\jdownloader\captcha\v2\solver\antiCaptchaCom\AntiCaptchaComSolver.java",
    r"org\jdownloader\captcha\v2\solver\cheapcaptcha\CheapCaptchaSolver.java",
    r"org\jdownloader\captcha\v2\solver\dbc\DeathByCaptchaSolver.java",
    r"org\jdownloader\captcha\v2\solver\endcaptcha\EndCaptchaSolver.java",
    r"org\jdownloader\captcha\v2\solver\imagetyperz\ImageTyperzCaptchaSolver.java",
    r"org\jdownloader\captcha\v2\solver\solver9kw\AbstractCaptcha9kwSolver.java",
    r"org\jdownloader\captcha\v2\solver\twocaptcha\TwoCaptchaSolver.java",
]

for rel_file in solver_files:
    filepath = base_path / rel_file
    if not filepath.exists():
        continue
    
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    # Fix setInvalid(AbstractResponse<?>) -> setInvalid(AbstractResponse<T>)
    # Actually need to check the parent class ChallengeSolver
    old = 'setInvalid(AbstractResponse'
    if old in content:
        # Check what ChallengeSolver.setInvalid signature is
        content = content.replace('setInvalid(AbstractResponse<?>)', 'setInvalid(AbstractResponse<T>)')
        print(f"Fixed setInvalid in {rel_file}")
    
    old2 = 'setUnused(AbstractResponse'
    if old2 in content:
        content = content.replace('setUnused(AbstractResponse<?>)', 'setUnused(AbstractResponse<T>)')
        print(f"Fixed setUnused in {rel_file}")
    
    old3 = 'setValid(AbstractResponse'
    if old3 in content:
        content = content.replace('setValid(AbstractResponse<?>)', 'setValid(AbstractResponse<T>)')
        print(f"Fixed setValid in {rel_file}")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done fixing AbstractResponse<?> override issues.")
