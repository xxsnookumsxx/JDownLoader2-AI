with open(r'D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk_errors.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
error_lines = []
for line in lines:
    if ' error: ' in line:
        error_lines.append(line.strip())
        
for i, line in enumerate(error_lines[:20]):
    print(f"{i+1:3d}: {line}")