import re
from pathlib import Path

# Configuration
base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")
errors_file = r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk_errors.txt"

def parse_errors():
    """Parse the error file and extract error information"""
    errors = []
    with open(errors_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for line in content.split('\n'):
        # Look for error lines (not warnings)
        if ' error: ' in line:
            # Split by ' error: ' to separate file path/line info from the message
            parts = line.split(' error: ', 1)
            if len(parts) >= 2:
                path_part = parts[0].strip()
                message = parts[1].strip()
                
                # Extract file path and line number
                path_parts = path_part.split(':')
                print(f"Raw path_part: '{path_part}'")
                print(f"  Number of parts: {len(path_parts)}")
                for i, part in enumerate(path_parts):
                    print(f"  Part {i}: '{part}'")
                
                if len(path_parts) >= 3:  # Need at least file, line, and "error" parts
                    # The line number is the second-to-last part (index -2)
                    line_num = int(path_parts[-2])  # Second to last part is the line number
                    # The file path is everything except the last two parts
                    file_path_str = ':'.join(path_parts[:-2])
                    print(f"  Extracted file path: '{file_path_str}'")
                    print(f"  Extracted line number: {line_num}")
                    
                    # Create full path
                    filepath = base_path / file_path_str.replace('\\', '/')
                    print(f"  Full path: {filepath}")
                    
                    errors.append({
                        'file': filepath,
                        'line': line_num,
                        'message': message
                    })
    
    return errors

def main():
    print("Starting debug path parsing...")
    errors = parse_errors()
    print(f"Parsed {len(errors)} errors")

if __name__ == "__main__":
    main()