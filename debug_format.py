import re
import os
from pathlib import Path

# Configuration
base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")
errors_file = r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk_errors.txt"

def debug_parse_line(line):
    print(f"Processing line: {repr(line)}")
    
    # Look for error lines (not warnings)
    if ' error: ' in line:
        print("Found error line")
        parts = line.split(' error: ', 1)
        print(f"Split by ' error: ': {len(parts)} parts")
        print(f"Part 0: {repr(parts[0])}")
        print(f"Part 1: {repr(parts[1])}")
        
        path_line = parts[0].strip()
        print(f"path_line: {repr(path_line)}")
        
        # Debug the path_line structure
        path_parts = path_line.split(':')
        print(f"path_parts: {path_parts}")
        print(f"Length of path_parts: {len(path_parts)}")
        
        # Try different approaches to get line number
        print("Trying to extract line number:")
        # Approach 1: Last part is line number
        try:
            last_part = path_parts[-1]
            print(f"Last part: {repr(last_part)}")
            if last_part.isdigit():
                line_num = int(last_part)
                print(f"Line number (approach 1): {line_num}")
        except:
            print("Approach 1 failed")
            
        # Approach 2: Second to last part is line number
        if len(path_parts) >= 2:
            second_last_part = path_parts[-2]
            print(f"Second to last part: {repr(second_last_part)}")
            if second_last_part.isdigit():
                line_num = int(second_last_part)
                print(f"Line number (approach 2): {line_num}")
                
        # Approach 3: Look for the first numeric part
        numeric_parts = []
        for part in path_parts:
            if part.isdigit():
                numeric_parts.append(part)
        print(f"Numeric parts: {numeric_parts}")
        if numeric_parts:
            print(f"First numeric part: {numeric_parts[0]}")

debug_parse_line("svn_trunk\\src\\jd\\plugins\\hoster\\AnonServices.java:241: error: cannot find symbol")