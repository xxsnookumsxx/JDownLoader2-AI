import os
from pathlib import Path

# Define paths
file2btc_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src\jd\plugins\hoster\File2btcCom.java")

# Read file
with open(file2btc_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Add import if not present
import_added = False
for i, line in enumerate(lines):
    if 'import jd.plugins.filesharing.FILENAME_SOURCE;' in line:
        import_added = True
        break

if not import_added:
    # Find where to insert import (after other jd.plugins imports)
    insert_pos = 0
    for i, line in enumerate(lines):
        if line.startswith('import jd.plugins.'):
            insert_pos = i + 1
    lines.insert(insert_pos, 'import jd.plugins.filesharing.FILENAME_SOURCE;\n')
    import_added = True
    print("Added FILENAME_SOURCE import to File2btcCom.java")

# Fix String to long conversion issues (lines 124 and 276)
# We'll search for patterns and replace
fixed_lines = []
for i, line in enumerate(lines):
    line_stripped = line.strip()
    
    # Check for "String" assignment to long variable
    if ' = ' in line_stripped and 'long' in line_stripped and 'String' in line_stripped:
        # Replace String with Long.parseLong
        new_line = re.sub(r'(\w+)\s*=\s*String', r'\1 = Long.parseLong(\2)', line_stripped)
        lines[i] = new_line
        print(f"Fixed String to long conversion at line {i+1}")
        fixed_lines.append(True)
    
    # Check for FILENAME_SOURCE issues (lines around 124 and 276)
    if 'cannot be converted to FILENAME_SOURCE' in str(script_lines[i]):
        # Ensure import is present (already handled)
        pass
        
print(f"Total lines: {len(lines)}")
print(f"Import added: {import_added}")

# Write back
with open(file2btc_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)
    
print("File2btcCom.java updated")