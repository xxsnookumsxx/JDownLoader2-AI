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
            # Split into file/path/line part and error message
            parts = line.split(' error: ', 1)
            if len(parts) >= 2:
                path_line = parts[0].strip()
                message = parts[1].strip()
                
                # Extract file path and line number
                try:
                    # Split path_line by ':' to get parts
                    path_parts = path_line.split(':')
                    if len(path_parts) >= 3:  # Need at least file, line, and empty part
                        # The line number is the second-to-last part (index -2)
                        line_num = int(path_parts[-2].rstrip(':'))  # Remove trailing colon if present
                        # File path is everything before the last two parts (file and line number)
                        file_path_str = ':'.join(path_parts[:-2])
                        
                        # Create full path
                        filepath = Path(file_path_str.replace('\\', '/'))
                        
                        errors.append({
                            'file': filepath,
                            'line': line_num,
                            'message': message
                        })
                except Exception as e:
                    print(f"Error parsing line: {line} - {e}")
                    continue
    
    return errors

def debug_print_file_errors():
    errors = parse_errors()
    print(f"Total errors: {len(errors)}")
    for i, err in enumerate(errors[:10]):
        print(f"{i+1}: {err['file']} - line {err['line']} - {err['message']}")