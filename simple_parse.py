with open(r'D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk_errors.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
error_lines = []
for line in lines:
    if ' error: ' in line:
        error_lines.append(line.strip())

print(f"Found {len(error_lines)} error lines")

# Let's look at the first few
for i, line in enumerate(error_lines[:10]):
    print(f"{i+1:2d}: {line}")