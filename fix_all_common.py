import re
from pathlib import Path

base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")

# Fix all remaining common error patterns:
# 1. Add missing imports for CAPTCHA_TYPE
# 2. Fix method signatures to match parent classes
# 3. Fix type mismatches
# 4. Comment out code that uses removed APIs

fixes_applied = []

java_files = list(base_path.rglob("*.java"))

for filepath in java_files:
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        
        original = content
        
        # Add CAPTCHA_TYPE import if used but not imported
        if 'CAPTCHA_TYPE' in content and 'import jd.plugins.CaptchaType.CAPTCHA_TYPE;' not in content:
            lines = content.split('\n')
            insert_pos = 0
            for i, line in enumerate(lines):
                if line.startswith('import '):
                    insert_pos = i + 1
            lines.insert(insert_pos, 'import jd.plugins.CaptchaType.CAPTCHA_TYPE;')
            content = '\n'.join(lines)
            fixes_applied += 1
        
        # Add SolverType import if used but not imported
        if 'SolverType' in content and 'import org.jdownloader.captcha.v2.ChallengeSolver.SolverType;' not in content:
            lines = content.split('\n')
            insert_pos = 0
            for i, line in enumerate(lines):
                if line.startswith('import ') and 'org.jdownloader' in line:
                    insert_pos = i + 1
            lines.insert(insert_pos, 'import org.jdownloader.captcha.v2.ChallengeSolver.SolverType;')
            content = '\n'.join(lines)
            fixes_applied += 1
        
        # Fix getType() return type - String -> SolverType for solver services
        if 'public String getType()' in content:
            # Check if this is a solver service class
            if 'extends AbstractSolverService' in content or 'implements SolverService' in content:
                content = content.replace('public String getType()', 'public SolverType getType()')
                fixes_applied += 1
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
                
    except:
        pass

print(f"Fixed {fixes_applied} files with common patterns.")
