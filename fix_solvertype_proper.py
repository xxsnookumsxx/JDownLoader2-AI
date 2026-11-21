import re
from pathlib import Path

base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")

# Files where getType() SHOULD return SolverType (implement SolverService or AbstractSolverService)
valid_gettype_files = [
    r"org\jdownloader\captcha\v2\solver\antiCaptchaCom\AntiCaptchaComSolverService.java",
    r"org\jdownloader\captcha\v2\solver\cheapcaptcha\CheapCaptchaSolverService.java",
    r"org\jdownloader\captcha\v2\solver\dbc\DeathByCaptchaSolverService.java",
    r"org\jdownloader\captcha\v2\solver\endcaptcha\EndCaptchaSolverService.java",
    r"org\jdownloader\captcha\v2\solver\imagetyperz\ImageTyperzSolverService.java",
    r"org\jdownloader\captcha\v2\solver\solver9kw\NineKwSolverService.java",
    r"org\jdownloader\captcha\v2\solver\captchasolutions\CaptchaSolutionsSolverService.java",
    r"org\jdownloader\captcha\v2\solver\twocaptcha\TwoCaptchaSolverService.java",
    r"org\jdownloader\captcha\v2\solver\service\BrowserSolverService.java",
    r"org\jdownloader\captcha\v2\solver\service\DialogSolverService.java",
    r"org\jdownloader\captcha\v2\solver\jac\JacSolverService.java",
    r"org\jdownloader\plugins\components\captchasolver\PluginForCaptchaSolverSolverService.java",
    r"org\jdownloader\api\captcha\CaptchaAPIManualRemoteSolverService.java",
]

# Also fix toolbar action files that use SolverType values
toolbar_action_files = [
    r"org\jdownloader\gui\toolbar\action\CaptchaToogle9KWAction.java",
    r"org\jdownloader\gui\toolbar\action\CaptchaToogleAntiCaptchaAction.java",
    r"org\jdownloader\gui\toolbar\action\CaptchaToogleCheapCaptchaAction.java",
    r"org\jdownloader\gui\toolbar\action\CaptchaToogleDBCAction.java",
    r"org\jdownloader\gui\toolbar\action\CaptchaToogleEndCaptchaAction.java",
    r"org\jdownloader\gui\toolbar\action\CaptchaToogleImageTyperzAction.java",
    r"org\jdownloader\gui\toolbar\action\CaptchaToogleMyJDRemoteAction.java",
    r"org\jdownloader\gui\toolbar\action\CaptchaToogleTwoCaptchaAction.java",
]

# Files that compare getType() to SolverType values (need SolverType import)
fix_comparison_files = toolbar_action_files + valid_gettype_files

for rel_file in fix_comparison_files:
    filepath = base_path / rel_file
    if not filepath.exists():
        continue
    
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    modified = False
    
    # If file uses SolverType but doesn't import it
    if 'SolverType' in content and 'import org.jdownloader.captcha.v2.ChallengeSolver.SolverType;' not in content:
        lines = content.split('\n')
        insert_pos = 0
        for i, line in enumerate(lines):
            if line.startswith('import ') and 'org.jdownloader' in line:
                insert_pos = i + 1
        lines.insert(insert_pos, 'import org.jdownloader.captcha.v2.ChallengeSolver.SolverType;')
        content = '\n'.join(lines)
        modified = True
        print(f"Added SolverType import to {rel_file}")
    
    # If file has getType() returning String but uses SolverType values
    if 'public String getType()' in content and 'SolverType' in content:
        content = content.replace('public String getType()', 'public SolverType getType()')
        modified = True
        print(f"Changed getType() return type to SolverType in {rel_file}")
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Done fixing SolverType issues.")
