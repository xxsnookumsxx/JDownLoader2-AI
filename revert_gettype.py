import re
from pathlib import Path

base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")

# Files where getType() SHOULD return SolverType (captcha solver services)
valid_gettype_files = [
    r"org\jdownloader\captcha\v2\solver\antiCaptchaCom\AntiCaptchaComSolverService.java",
    r"org\jdownloader\captcha\v2\solver\cheapcaptcha\CheapCaptchaSolverService.java",
    r"org\jdownloader\captcha\v2\solver\dbc\DeathByCaptchaSolverService.java",
    r"org\jdownloader\captcha\v2\solver\endcaptcha\EndCaptchaSolverService.java",
    r"org\jdownloader\captcha\v2\solver\imagetyperz\ImageTyperzSolverService.java",
    r"org\jdownloader\captcha\v2\solver\solver9kw\NineKwSolverService.java",
    r"org\jdownloader\captcha\v2\solver\captchasolutions\CaptchaSolutionsSolverService.java",
    r"org\jdownloader\captcha\v2\solver\twocaptcha\TwoCaptchaSolverService.java",
]

# Revert getType() in all other files back to String
java_files = list(base_path.rglob("*.java"))

reverted = 0
for filepath in java_files:
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        
        rel_path = str(filepath.relative_to(base_path)).replace('/', '\\')
        
        # Only revert if NOT in valid list AND has SolverType return type
        if rel_path not in valid_gettype_files:
            if 'public SolverType getType()' in content:
                content = content.replace('public SolverType getType()', 'public String getType()')
                
                # Remove SolverType import if no longer needed
                if 'SolverType' not in content.replace('import org.jdownloader.captcha.v2.ChallengeSolver.SolverType;', ''):
                    lines = content.split('\n')
                    lines = [l for l in lines if 'import org.jdownloader.captcha.v2.ChallengeSolver.SolverType;' not in l]
                    content = '\n'.join(lines)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                reverted += 1
                print(f"Reverted getType() in {rel_path}")
    except Exception as e:
        pass

print(f"\nReverted {reverted} files.")
