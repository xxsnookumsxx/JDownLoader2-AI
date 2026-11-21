import re
from pathlib import Path

base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")

fixes_applied = []

java_files = list(base_path.rglob("*.java"))

for filepath in java_files:
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        
        original = content
        
        # 1. Remove com.apple.eawt imports (macOS EAWT - not available in JDK 25)
        lines = content.split('\n')
        new_lines = []
        for line in lines:
            if 'import com.apple.eawt' in line:
                continue
            new_lines.append(line)
        content = '\n'.join(new_lines)
        
        # 2. Add missing CAPTCHA_TYPE import if used but not imported
        if 'CAPTCHA_TYPE' in content and 'import jd.plugins.CaptchaType.CAPTCHA_TYPE;' not in content:
            lines = content.split('\n')
            insert_pos = 0
            for i, line in enumerate(lines):
                if line.startswith('import '):
                    insert_pos = i + 1
            lines.insert(insert_pos, 'import jd.plugins.CaptchaType.CAPTCHA_TYPE;')
            content = '\n'.join(lines)
        
        # 3. Add missing SolverType import if used but not imported
        if 'SolverType' in content and 'import org.jdownloader.captcha.v2.ChallengeSolver.SolverType;' not in content:
            lines = content.split('\n')
            insert_pos = 0
            for i, line in enumerate(lines):
                if line.startswith('import ') and 'org.jdownloader' in line:
                    insert_pos = i + 1
            lines.insert(insert_pos, 'import org.jdownloader.captcha.v2.ChallengeSolver.SolverType;')
            content = '\n'.join(lines)
        
        # 4. Add missing Set import if used but not imported
        if 'java.util.Set' in content and 'import java.util.Set;' not in content:
            lines = content.split('\n')
            insert_pos = 0
            for i, line in enumerate(lines):
                if line.startswith('import java.util.'):
                    insert_pos = i + 1
            lines.insert(insert_pos, 'import java.util.Set;')
            content = '\n'.join(lines)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            fixes_applied.append(filepath.name)
            
    except:
        pass

print(f"Fixed {len(fixes_applied)} files with import issues.")
