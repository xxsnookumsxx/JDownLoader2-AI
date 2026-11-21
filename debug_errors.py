with open(r'D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk_errors.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
for i, line in enumerate(lines[:20]):
    print(f"{i+1:3d}: {line.rstrip()}")