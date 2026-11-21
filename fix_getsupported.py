import re
from pathlib import Path

base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")

# Fix AbstractBrowserSolver.getSupportedCaptchaTypes() return type
solver_service_files = [
    r"org\jdownloader\captcha\v2\solver\antiCaptchaCom\AntiCaptchaComSolverService.java",
    r"org\jdownloader\captcha\v2\solver\cheapcaptcha\CheapCaptchaSolverService.java",
    r"org\jdownloader\captcha\v2\solver\dbc\DeathByCaptchaSolverService.java",
    r"org\jdownloader\captcha\v2\solver\endcaptcha\EndCaptchaSolverService.java",
    r"org\jdownloader\captcha\v2\solver\imagetyperz\ImageTyperzSolverService.java",
    r"org\jdownloader\captcha\v2\solver\solver9kw\NineKwSolverService.java",
    r"org\jdownloader\captcha\v2\solver\captchasolutions\CaptchaSolutionsSolverService.java",
    r"org\jdownloader\captcha\v2\solver\twocaptcha\TwoCaptchaSolverService.java",
]

for rel_file in solver_service_files:
    filepath = base_path / rel_file
    if not filepath.exists():
        continue
    
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    # Fix getSupportedCaptchaTypes return type if needed
    if 'getSupportedCaptchaTypes' in content:
        # Check the signature
        old = 'public Set<CAPTCHA_TYPE> getSupportedCaptchaTypes()'
        if old not in content:
            # Try other patterns
            pass
    
    print(f"Checked {rel_file}")

print("Done checking solver services.")
