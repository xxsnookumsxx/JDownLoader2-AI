import re
from pathlib import Path

base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")

fixes_applied = []

# 1. Fix all files that reference com.apple.eawt (macOS-specific)
java_files = list(base_path.rglob("*.java"))

for filepath in java_files:
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        
        original = content
        
        # Remove com.apple.eawt imports
        lines = content.split('\n')
        new_lines = []
        skip_next_blank = False
        
        for line in lines:
            if 'import com.apple.eawt' in line:
                continue
            if skip_next_blank and line.strip() == '':
                skip_next_blank = False
                continue
            skip_next_blank = False
            new_lines.append(line)
        
        content = '\n'.join(new_lines)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            fixes_applied.append(f"Removed EAWT imports from {filepath.name}")
    except:
        pass

print(f"Fixed {len(fixes_applied)} files with EAWT imports.")
