import re
from collections import Counter

errors_file = r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk_errors.txt"

with open(errors_file, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Categorize errors
categories = {
    'cannot find symbol': 0,
    'incompatible types': 0,
    'method does not override': 0,
    'constructor cannot be applied': 0,
    'package does not exist': 0,
    'other': 0
}

error_categories = Counter()

for line in content.split('\n'):
    match = re.search(r'error:\s+(.+)', line)
    if match:
        msg = match.group(1).strip()
        if 'cannot find symbol' in msg:
            error_categories['cannot find symbol'] += 1
        elif 'incompatible types' in msg:
            error_categories['incompatible types'] += 1
        elif 'does not override' in msg:
            error_categories['method does not override'] += 1
        elif 'constructor' in msg and 'cannot be applied' in msg:
            error_categories['constructor cannot be applied'] += 1
        elif 'package .* does not exist' in msg:
            error_categories['package does not exist'] += 1
        else:
            error_categories['other'] += 1
            print(f"  OTHER: {msg}")

print("\nError Categories:")
for cat, count in error_categories.most_common():
    print(f"  {cat}: {count}")
