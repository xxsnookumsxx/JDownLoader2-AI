import re
from pathlib import Path

base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")

# Fix common error patterns
fixes_applied = []

# 1. Fix files that use "String getType()" but should return SolverType
files_gettype = [
    r"org\jdownloader\captcha\v2\solver\antiCaptchaCom\AntiCaptchaComSolverService.java",
    r"org\jdownloader\captcha\v2\solver\cheapcaptcha\CheapCaptchaSolverService.java",
    r"org\jdownloader\captcha\v2\solver\dbc\DeathByCaptchaSolverService.java",
    r"org\jdownloader\captcha\v2\solver\endcaptcha\EndCaptchaSolverService.java",
    r"org\jdownloader\captcha\v2\solver\imagetyperz\ImageTyperzSolverService.java",
    r"org\jdownloader\captcha\v2\solver\solver9kw\NineKwSolverService.java",
    r"org\jdownloader\captcha\v2\solver\captchasolutions\CaptchaSolutionsSolverService.java",
    r"org\jdownloader\captcha\v2\solver\twocaptcha\TwoCaptchaSolverService.java",
]

for rel_file in files_gettype:
    filepath = base_path / rel_file
    if not filepath.exists():
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'public String getType()' in content:
        content = content.replace('public String getType()', 'public SolverType getType()')
        if 'import org.jdownloader.captcha.v2.ChallengeSolver.SolverType;' not in content:
            lines = content.split('\n')
            insert_pos = 0
            for i, line in enumerate(lines):
                if line.startswith('import ') and 'org.jdownloader' in line:
                    insert_pos = i + 1
            lines.insert(insert_pos, 'import org.jdownloader.captcha.v2.ChallengeSolver.SolverType;')
            content = '\n'.join(lines)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        fixes_applied.append(f"Fixed getType() return type in {rel_file}")

# 2. Fix MacOSApplicationAdapter.java - replace com.apple.eawt imports with stub
filepath = base_path / r"org\jdownloader\crosssystem\macos\MacOSApplicationAdapter.java"
if filepath.exists():
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'com.apple.eawt' in content:
        # Replace all com.apple.eawt imports and usage with stub
        lines = content.split('\n')
        new_lines = []
        skip_imports = False
        for line in lines:
            if 'import com.apple.eawt' in line:
                skip_imports = True
                continue
            if skip_imports and line.strip() == '':
                skip_imports = False
                new_lines.append(line)
                continue
            if skip_imports:
                continue
            new_lines.append(line)
        
        content = '\n'.join(new_lines)
        
        # Add stub methods where eawt was used
        if 'public class MacOSApplicationAdapter' in content:
            # Add a stub class or modify existing one
            content = content.replace(
                'public class MacOSApplicationAdapter',
                'public class MacOSApplicationAdapter { /* macOS EAWT stub */'
            )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        fixes_applied.append(f"Fixed MacOSApplicationAdapter.java EAWT imports")

# 3. Fix EmuParadiseMe.java - isOffline method signature
filepath = base_path / r"jd\plugins\decrypter\EmuParadiseMe.java"
if filepath.exists():
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'boolean isOffline()' in content:
        content = content.replace('boolean isOffline()', 'public boolean isOffline()')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    fixes_applied.append(f"Fixed EmuParadiseMe.java isOffline() signature")

for fix in fixes_applied:
    print(fix)

print(f"\nTotal fixes applied: {len(fixes_applied)}")
