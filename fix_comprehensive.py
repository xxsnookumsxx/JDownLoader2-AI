import re
from pathlib import Path

base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")

fixes_applied = 0

# Read all Java files and fix common issues
java_files = list(base_path.rglob("*.java"))

for filepath in java_files:
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        
        original = content
        
        # 1. Fix getType() return type - String -> SolverType
        if 'public String getType()' in content:
            content = content.replace('public String getType()', 'public SolverType getType()')
            
            # Add SolverType import if not present
            if 'import org.jdownloader.captcha.v2.ChallengeSolver.SolverType;' not in content:
                lines = content.split('\n')
                insert_pos = 0
                for i, line in enumerate(lines):
                    if line.startswith('import ') and 'org.jdownloader' in line:
                        insert_pos = i + 1
                lines.insert(insert_pos, 'import org.jdownloader.captcha.v2.ChallengeSolver.SolverType;')
                content = '\n'.join(lines)
        
        # 2. Fix setInvalid/setValid/setUnused signatures
        content = content.replace('setInvalid(AbstractResponse<T>)', 'setInvalid(AbstractResponse<?>)')
        content = content.replace('setValid(AbstractResponse<T>)', 'setValid(AbstractResponse<?>)')
        content = content.replace('setUnused(AbstractResponse<T>)', 'setUnused(AbstractResponse<?>)')
        
        # 3. Fix List<CAPTCHA_TYPE> return type to Set<CAPTCHA_TYPE>
        content = content.replace('public List<CAPTCHA_TYPE> getSupportedCaptchaTypes()', 'public Set<CAPTCHA_TYPE> getSupportedCaptchaTypes()')
        
        # 4. Add missing imports
        if 'Set<CAPTCHA_TYPE>' in content and 'import jd.plugins.CaptchaType.CAPTCHA_TYPE;' not in content:
            lines = content.split('\n')
            insert_pos = 0
            for i, line in enumerate(lines):
                if line.startswith('import '):
                    insert_pos = i + 1
            lines.insert(insert_pos, 'import jd.plugins.CaptchaType.CAPTCHA_TYPE;')
            content = '\n'.join(lines)
        
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
            fixes_applied += 1
            
    except Exception as e:
        pass

print(f"Fixed {fixes_applied} files with common patterns.")
