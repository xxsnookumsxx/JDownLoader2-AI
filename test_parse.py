import re
from pathlib import Path

base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")

def parse_errors():
    errors = []
    with open('sample_errors.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    
    for line in content.split('\n'):
        if ' error: ' in line:
            parts = line.split(' error: ', 1)
            if len(parts) >= 2:
                path_part = parts[0].strip()
                message = parts[1].strip()
                
                path_parts = path_part.split(':')
                if len(path_parts) >= 2:
                    file_path_str = ':'.join(path_parts[:-1])
                    line_num = int(path_parts[-1])
                    
                    filepath = base_path / file_path_str.replace('\\', '/')
                    
                    errors.append({
                        'file': filepath,
                        'line': line_num,
                        'message': message
                    })
    
    return errors

def main():
    errors = parse_errors()
    print(f"Parsed {len(errors)} errors")
    for err in errors:
        print(f"  {err['file']}:{err['line']} - {err['message']}")

if __name__ == "__main__":
    main()