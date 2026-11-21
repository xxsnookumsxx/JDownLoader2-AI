import re
from pathlib import Path

base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")

fixes_applied = 0

# Read errors file and categorize
errors_file = r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk_errors.txt"

with open(errors_file, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Parse all errors
errors = []
for line in content.split('\n'):
    match = re.match(r'(svn_trunk\\src\\.+?\.java):(\d+):\s+error:\s+(.+)', line)
    if match:
        errors.append({
            'file': match.group(1),
            'line': int(match.group(2)),
            'message': match.group(3)
        })

print(f"Total errors: {len(errors)}")

# Fix "cannot find symbol" for CAPTCHA_TYPE
for err in errors:
    if 'CAPTCHA_TYPE' in err['message'] and 'cannot find symbol' in err['message']:
        filepath = base_path / err['file']
        if filepath.exists():
            with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
                fcontent = f.read()
            
            if 'import jd.plugins.CaptchaType.CAPTCHA_TYPE;' not in fcontent:
                lines = fcontent.split('\n')
                insert_pos = 0
                for i, line in enumerate(lines):
                    if line.startswith('import '):
                        insert_pos = i + 1
                
                lines.insert(insert_pos, 'import jd.plugins.CaptchaType.CAPTCHA_TYPE;')
                fcontent = '\n'.join(lines)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(fcontent)
                print(f"Added CAPTCHA_TYPE import to {err['file']}")

print("Done fixing CAPTCHA_TYPE imports.")
