with open(r'D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk_errors.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
print(f"Total lines: {len(lines)}")

# Find the first line with 'error:'
first_error_line = None
for i, line in enumerate(lines):
    if ' error: ' in line:
        first_error_line = i + 1  # 1-indexed
        print(f"First error line is line {i+1}: {repr(line)}")
        break
        
if first_error_line:
    print(f"Total error lines: {len(lines) - first_error_line + 1}")