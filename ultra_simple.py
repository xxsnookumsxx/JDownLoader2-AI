import re
from pathlib import Path

# Configuration
base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")
errors_file = r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk_errors.txt"

def main():
    print("Reading errors file...")
    with open(errors_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all lines with "error:" 
    error_lines = [line for line in content.split('\n') if ' error: ' in line]
    print(f"Found {len(error_lines)} error lines")
    
    # Parse each error line
    errors = []
    for line in error_lines[:10]:  # Test with first 10
        print(f"Processing: {line}")
        parts = line.split(' error: ')
        if len(parts) >= 2:
            path_part = parts[0].strip()
            message = parts[1].strip()
            
            # Split by colon to get file and line number
            path_parts = path_part.split(':')
            if len(path_parts) >= 2:
                # Last part is line number
                line_num = int(path_parts[-1])
                # Everything before that is file path
                file_path_str = ':'.join(path_parts[:-1])
                
                print(f"  Parsed: {path_part} -> file: {file_path_str}, line: {line_num}")
                # Create path object
                filepath = path_parts[0].replace('\\', '/')  # Simplified
                print(f"  Full path would be: {filepath}")
                
    print("Done with sample parsing")

if __name__ == "__main__":
    main()