import re
from pathlib import Path

base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")

# Files with imports before package declaration
files_to_fix = [
    r"jd\plugins\components\PremiumizeBrowseNode.java",
    r"jd\plugins\components\gopro\Media.java",
    r"jd\plugins\components\gopro\Variation.java",
    r"org\jdownloader\api\captcha\CaptchaJob.java",
    r"org\jdownloader\api\jdanywhere\api\storable\CaptchaJob.java",
    r"org\jdownloader\api\useragent\UserAgentInfo.java",
    r"org\jdownloader\controlling\ffmpeg\FFmpegMetaData.java",
    r"org\jdownloader\extensions\eventscripter\sandboxobjects\HTTPProxySandbox.java",
    r"org\jdownloader\plugins\components\realDebridCom\api\json\UserResponse.java",
    r"org\jdownloader\settings\UrlDisplayEntry.java",
]

for rel_file in files_to_fix:
    filepath = base_path / rel_file
    if not filepath.exists():
        print(f"NOT FOUND: {rel_file}")
        continue
    
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    lines = content.split('\n')
    
    # Find package line
    package_idx = -1
    import_lines = []
    other_lines = []
    
    for i, line in enumerate(lines):
        if line.strip().startswith('package '):
            package_idx = i
        elif line.strip().startswith('import '):
            import_lines.append(line)
        else:
            other_lines.append((i, line))
    
    if package_idx == -1:
        print(f"No package declaration found in {rel_file}")
        continue
    
    # Rebuild: package first, then imports, then rest
    new_lines = []
    
    # Add package declaration
    for i, line in enumerate(lines):
        if line.strip().startswith('package '):
            new_lines.append(line)
            break
    
    # Add blank line
    new_lines.append('')
    
    # Add imports
    for imp in import_lines:
        new_lines.append(imp)
    
    # Add blank line
    new_lines.append('')
    
    # Add remaining lines (everything between package and end, excluding imports we already moved)
    in_package_section = False
    for i, line in enumerate(lines):
        if line.strip().startswith('package '):
            in_package_section = True
            continue
        if in_package_section and line.strip().startswith('import '):
            continue  # Skip - already added
        if in_package_section:
            new_lines.append(line)
    
    content = '\n'.join(new_lines)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed {rel_file}")

print("Done fixing import ordering.")
