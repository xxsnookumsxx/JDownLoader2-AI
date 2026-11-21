import re
from pathlib import Path

base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")

# Fix missing SolverType import in EndCaptchaSolverService.java
filepath = base_path / r"org\jdownloader\captcha\v2\solver\endcaptcha\EndCaptchaSolverService.java"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

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
    print(f"Added SolverType import to EndCaptchaSolverService.java")

print("Done.")
