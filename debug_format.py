with open(r'D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk_errors.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
print("First 10 lines:")
for i in range(10):
    print(f"{i+1:2d}: {repr(lines[i])}")

print("\nLines with 'error:' (first 10):")
for i in range(10):
    line = lines[i]
    if ' error: ' in line:
        print(f"{i+1:2d}: {repr(line)}")