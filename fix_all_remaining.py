import re
from pathlib import Path

base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")

fixes_applied = []

# Fix all remaining "cannot find symbol" errors by adding missing imports
# Fix all "method does not override" errors
# Fix all "incompatible types" errors

# Common fixes:
# 1. Add missing imports for CAPTCHA_TYPE, SolverType, etc.
# 2. Fix method signatures to match parent classes
# 3. Comment out code that uses removed/renamed APIs
# 4. Fix type mismatches

# Fix all getType() methods that return String instead of SolverType
gettype_files = list(base_path.rglob("*SolverService.java")) + list(base_path.rglob("*Solver.java"))

for filepath in gettype_files:
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        
        modified = False
        
        # Fix getType() return type
        if 'public String getType()' in content:
            content = content.replace('public String getType()', 'public SolverType getType()')
            modified = True
        
        # Add SolverType import if needed
        if 'public SolverType getType()' in content and 'import org.jdownloader.captcha.v2.ChallengeSolver.SolverType;' not in content:
            lines = content.split('\n')
            insert_pos = 0
            for i, line in enumerate(lines):
                if line.startswith('import ') and 'org.jdownloader' in line:
                    insert_pos = i + 1
            lines.insert(insert_pos, 'import org.jdownloader.captcha.v2.ChallengeSolver.SolverType;')
            content = '\n'.join(lines)
            modified = True
        
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            fixes_applied.append(f"Fixed getType() in {filepath.name}")
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

print(f"Fixed {len(fixes_applied)} files with getType() issues.")

# Fix setInvalid/setValid/setUnused signatures
solver_files = list(base_path.rglob("*Solver.java"))

for filepath in solver_files:
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        
        modified = False
        
        # The parent ChallengeSolver methods take AbstractResponse<?>
        # Child classes should match
        old_patterns = [
            ('setInvalid(AbstractResponse<T>)', 'setInvalid(AbstractResponse<?>)'),
            ('setValid(AbstractResponse<T>)', 'setValid(AbstractResponse<?>)'),
            ('setUnused(AbstractResponse<T>)', 'setUnused(AbstractResponse<?>)'),
        ]
        
        for old, new in old_patterns:
            if old in content:
                content = content.replace(old, new)
                modified = True
        
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            fixes_applied.append(f"Fixed signatures in {filepath.name}")
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

print(f"Fixed solver method signatures.")
