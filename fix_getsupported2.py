import re
from pathlib import Path

base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")

files_to_fix = [
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

for rel_file in files_to_fix:
    filepath = base_path / rel_file
    if not filepath.exists():
        print(f"NOT FOUND: {rel_file}")
        continue
    
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    fixed = False
    
    # Fix List<CAPTCHA_TYPE> return type to Set<CAPTCHA_TYPE>
    old1 = 'public List<CAPTCHA_TYPE> getSupportedCaptchaTypes()'
    new1 = 'public Set<CAPTCHA_TYPE> getSupportedCaptchaTypes()'
    if old1 in content:
        content = content.replace(old1, new1)
        fixed = True
        print(f"Fixed List->Set return type in {rel_file}")
    
    # Fix missing getSupportedCaptchaTypes method - add a default implementation
    if not fixed:
        # Check if the file implements ChallengeSolver and lacks getSupportedCaptchaTypes
        if 'ChallengeSolver' in content and 'getSupportedCaptchaTypes' not in content:
            # Add import for Set if needed
            if 'import java.util.Set' not in content and 'import java.util.Set' not in content:
                lines = content.split('\n')
                insert_pos = 0
                for i, line in enumerate(lines):
                    if line.startswith('import java.util.'):
                        insert_pos = i + 1
                
                import_line = 'import java.util.Set;'
                lines.insert(insert_pos, import_line)
                content = '\n'.join(lines)
            
            # Add method before closing brace of class
            # Find a good place to add it - before the last }
            method = '''
    @Override
    public Set<CAPTCHA_TYPE> getSupportedCaptchaTypes() {
        return null;
    }
'''
            # Insert before last }
            last_brace_pos = content.rstrip().rfind('}')
            if last_brace_pos > 0:
                content = content[:last_brace_pos] + method + content[last_brace_pos:]
                fixed = True
                print(f"Added missing getSupportedCaptchaTypes() in {rel_file}")
    
    if fixed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Done fixing getSupportedCaptchaTypes.")
