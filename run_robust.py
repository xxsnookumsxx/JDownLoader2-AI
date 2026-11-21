import sys
sys.path.append('.')
from robust_parser import parse_errors

errors = parse_errors()
print(f"Found {len(errors)} errors")
for i, err in enumerate(errors[:5]):
    print(f"{i+1}: {err['file']}:{err['line']} - {err['message']}")