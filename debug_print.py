import re
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
        message = parts[1].strip()
        
        print(f"path_line: {repr(path_line)}")
        print(f"message: {repr(message)}")
        
        # Split path_line by ':' to get parts
        path_parts = path_line.split(':')
        print(f"path_parts: {path_parts}")
        print(f"Length of path_parts: {len(path_parts)}")
        
        # Try to find the line number
        line_num = None
        file_path_str = None
        for i, part in enumerate(path_parts):
            print(f"  Part {i}: {repr(part)}")
            if part.isdigit():
                line_num = int(part)
                print(f"  Found line number: {line_num} at index {i}")
                file_path_str = ':'.join(path_parts[:i])
                print(f"  File path: {repr(file_path_str)}")
                break
        
        if file_path_str and line_num is not None:
            filepath = Path(file_path_str.replace('\\', '/'))
            print(f"Final file path: {filepath}")
            print(f"Final line number: {line_num}")
            return filepath, line_num, message
            
    return None, None, None

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
        message = parts[1].strip()
        
        print(f"path_line: {repr(path_line)}")
        print(f"message: {repr(message)}")
        
        # Split path_line by ':' to get parts
        path_parts = path_line.split(':')
        print(f"path_parts: {path_parts}")
        print(f"Length of path_parts: {len(path_parts)}")
        
        # Try to find the line number
        line_num = None
        file_path_str = None
        for i, part in enumerate(path_parts):
            print(f"  Part {i}: {repr(part)}")
            if part.isdigit():
                line_num = int(part)
                print(f"  Found line number: {line_num} at index {i}")
                file_path_str = ':'.join(path_parts[:i])
                print(f"  File path: {repr(file_path_str)}")
                break
        
        if file_path_str and line_num is not None:
            filepath = Path(file_path_str.replace('\\', '/'))
            print(f"Final file path: {filepath}")
            print(f"Final line number: {line_num}")
            return filepath, line_num, message
            
    return None, None, None

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
        message = parts[1].strip()
        
        print(f"path_line: {repr(path_line)}")
        print(f"message: {repr(message)}")
        
        # Split path_line by ':' to get parts
        path_parts = path_line.split(':')
        print(f"path_parts: {path_parts}")
        print(f"Length of path_parts: {len(path_parts)}")
        
        # Try to find the line number
        line_num = None
        file_path_str = None
        for i, part in enumerate(path_parts):
            print(f"  Part {i}: {repr(part)}")
            if part.isdigit():
                line_num = int(part)
                print(f"  Found line number: {line_num} at index {i}")
                file_path_str = ':'.join(path_parts[:i])
                print(f"  File path: {repr(file_path_str)}")
                break
        
        if file_path_str and line_num is not None:
            filepath = Path(file_path_str.replace('\\', '/'))
            print(f"Final file path: {filepath}")
            print(f"Final line number: {line_num}")
            return filepath, line_num, message
            
    return None, None, None

def debug_print_errors():
    errors = parse_errors()
    print(f"Total errors: {len(errors)}")
    for i, err in enumerate(errors[:10]):
        print(f"{i+1:2d}: {err['file']} - line {err['line']} - {err['message']}")

if __name__ == "__main__":
    debug_parse_line("svn_trunk\\src\\jd\\plugins\\hoster\\AnonServices.java:241: error: cannot find symbol")
    print("---")
    debug_parse_line("svn_trunk\\src\\jd\\plugins\\hoster\\AnonServices.java:244: error: cannot find symbol")