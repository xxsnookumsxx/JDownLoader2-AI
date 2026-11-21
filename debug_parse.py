import re
from pathlib import Path

base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")

# Read current errors
errors_file = r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk_errors.txt"
with open(errors_file, 'r', encoding='utf-8', errors='replace') as f:
    error_content = f.read()

# Parse all errors - try different pattern
errors = []
for line in error_content.split('\n'):
    match = re.match(r'(svn_trunk\\src\\.+?\.java):(\d+):\s+error:\s+(.+)', line)
    if match:
        errors.append({
            'file': match.group(1),
            'line': int(match.group(2)),
            'message': match.group(3)
        })

print(f"Total errors parsed: {len(errors)}")
print(f"First 5 errors:")
for e in errors[:5]:
    print(f"  {e['file']}:{e['line']}: {e['message'][:80]}")
