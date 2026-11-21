import re
import os

errors_file = r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk_errors.txt"

# Read errors
with open(errors_file, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Extract file:line pairs
errors = []
for line in content.split('\n'):
    match = re.match(r'(svn_trunk\\src\\.+?\.java):(\d+):\s+error:', line)
    if match:
        errors.append((match.group(1), int(match.group(2))))

# Get unique files with error counts
from collections import Counter
file_errors = Counter([e[0] for e in errors])

print(f"Total error lines: {len(errors)}")
print(f"Unique files with errors: {len(file_errors)}")
print("\nTop files by error count:")
for f, count in file_errors.most_common(20):
    print(f"  {count:4d}  {f}")
