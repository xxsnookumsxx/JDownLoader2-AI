import re
from pathlib import Path
from collections import Counter

errors_file = r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk_errors.txt"

# Read all errors
with open(errors_file, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Group errors by file
file_errors = {}
for line in content.split('\n'):
    match = re.match(r'(svn_trunk\\src\\.+?\.java):(\d+):\s+error:\s+(.+)', line)
    if match:
        filepath = match.group(1)
        line_num = int(match.group(2))
        err_msg = match.group(3)
        if filepath not in file_errors:
            file_errors[filepath] = []
        file_errors[filepath].append((line_num, err_msg))

print(f"Total files with errors: {len(file_errors)}")
print(f"Total error lines: {sum(len(v) for v in file_errors.values())}")

# Print summary of error types per file
for fp, errors in sorted(file_errors.items()):
    print(f"\n{fp}:")
    for ln, msg in errors[:5]:  # Show first 5 errors per file
        print(f"  Line {ln}: {msg[:80]}")
    if len(errors) > 5:
        print(f"  ... and {len(errors) - 5} more")
