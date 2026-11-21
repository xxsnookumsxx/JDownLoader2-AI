with open(r'D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk_errors.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
# Print first 20 error lines
count = 0
for line in lines:
    if ' error: ' in line:
        print(f"{count:3d}: {line.rstrip()}")
        count += 1
        if count >= 20:
            break