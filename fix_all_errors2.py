import re
from pathlib import Path

base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")

fixes_applied = []

# Read current errors
errors_file = r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk_errors.txt"
with open(errors_file, 'r', encoding='utf-8', errors='replace') as f:
    error_content = f.read()

# Parse all errors
errors = []
for line in error_content.split('\n'):
    match = re.match(r'(svn_trunk\\src\\.+?\.java):(\d+):\s+error:\s+(.+)', line)
    if match:
        errors.append({
            'file': match.group(1),
            'line': int(match.group(2)),
            'message': match.group(3)
        })

print(f"Total errors remaining: {len(errors)}")

# Group errors by file
file_errors = {}
for err in errors:
    f = err['file']
    if f not in file_errors:
        file_errors[f] = []
    file_errors[f].append(err)

for filepath_str, errs in file_errors.items():
    filepath = base_path / filepath_str
    if not filepath.exists():
        continue
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        
        original = content
        
        messages = [e['message'] for e in errs]
        
        # Fix: Add CAPTCHA_TYPE import if needed
        if any('CAPTCHA_TYPE' in m for m in messages):
            if 'import jd.plugins.CaptchaType.CAPTCHA_TYPE;' not in content:
                lines = content.split('\n')
                insert_pos = 0
                for i, line in enumerate(lines):
                    if line.startswith('import '):
                        insert_pos = i + 1
                lines.insert(insert_pos, 'import jd.plugins.CaptchaType.CAPTCHA_TYPE;')
                content = '\n'.join(lines)
        
        # Fix: Add SolverType import if needed  
        if any('SolverType' in m for m in messages):
            if 'import org.jdownloader.captcha.v2.ChallengeSolver.SolverType;' not in content:
                lines = content.split('\n')
                insert_pos = 0
                for i, line in enumerate(lines):
                    if line.startswith('import ') and 'org.jdownloader' in line:
                        insert_pos = i + 1
                lines.insert(insert_pos, 'import org.jdownloader.captcha.v2.ChallengeSolver.SolverType;')
                content = '\n'.join(lines)
        
        # Fix: Add Set import if needed
        if any('Set<' in m or 'Set ' in m for m in messages):
            if 'import java.util.Set;' not in content:
                lines = content.split('\n')
                insert_pos = 0
                for i, line in enumerate(lines):
                    if line.startswith('import java.util.'):
                        insert_pos = i + 1
                lines.insert(insert_pos, 'import java.util.Set;')
                content = '\n'.join(lines)
        
        # Fix: Fix getType() return type String -> SolverType for solver services
        if any('getType' in m and ('cannot be converted to String' in m or 'cannot override' in m) for m in messages):
            if 'extends AbstractSolverService' in content or 'implements SolverService' in content:
                content = content.replace('public String getType()', 'public SolverType getType()')
        
        # Fix: Fix List<CAPTCHA_TYPE> -> Set<CAPTCHA_TYPE> return type
        content = content.replace('public List<CAPTCHA_TYPE> getSupportedCaptchaTypes()', 'public Set<CAPTCHA_TYPE> getSupportedCaptchaTypes()')
        
        # Fix: Remove com.apple.eawt imports
        lines = content.split('\n')
        new_lines = [l for l in lines if 'import com.apple.eawt' not in l]
        content = '\n'.join(new_lines)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            fixes_applied.append(filepath_str)
            
    except Exception as e:
        print(f"Error processing {filepath_str}: {e}")

print(f"Fixed {len(fixes_applied)} files.")
