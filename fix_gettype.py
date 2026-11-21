import re
import os
from pathlib import Path

base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")

# Files with getType() that return String instead of SolverType
files_to_fix = [
    r"org\jdownloader\captcha\v2\solver\cheapcaptcha\CheapCaptchaSolverService.java",
    r"org\jdownloader\captcha\v2\solver\dbc\DeathByCaptchaSolverService.java",
    r"org\jdownloader\captcha\v2\solver\imagetyperz\ImageTyperzSolverService.java",
    r"org\jdownloader\captcha\v2\solver\solver9kw\NineKwSolverService.java",
    r"org\jdownloader\captcha\v2\solver\captchasolutions\CaptchaSolutionsSolverService.java",
]

for rel_file in files_to_fix:
    filepath = base_path / rel_file
    if not filepath.exists():
        print(f"NOT FOUND: {filepath}")
        continue
    
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    # Check if SolverType is already imported
    has_import = 'import org.jdownloader.captcha.v2.ChallengeSolver.SolverType;' in content
    
    # Replace getType() return type
    old_pattern = r'public String getType\(\s*\)\s*\{'
    new_text = 'public SolverType getType() {'
    
    if re.search(old_pattern, content):
        content = re.sub(old_pattern, new_text, content)
        print(f"Fixed getType() in {rel_file}")
    
    # Add import if not present
    if not has_import:
        # Find the import block and add after existing imports
        # Add after the last import line
        import_pattern = r'(^import [^\n]+\n)(?=\n|package|\s*class|\s*public|\s*interface|\s*enum)'
        # Find position after last import line
        lines = content.split('\n')
        insert_pos = 0
        for i, line in enumerate(lines):
            if line.startswith('import '):
                insert_pos = i + 1
        
        import_line = 'import org.jdownloader.captcha.v2.ChallengeSolver.SolverType;'
        lines.insert(insert_pos, import_line)
        content = '\n'.join(lines)
        print(f"Added SolverType import to {rel_file}")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("\nDone fixing getType() methods.")
