import re
import os
from pathlib import Path

# Configuration
base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")
errors_file = r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk_errors.txt"

def parse_errors():
    """Parse the error file and extract error information"""
    errors = []
    with open(errors_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for line_num, line in enumerate(content.split('\n'), 1):
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
                        line_num_str = path_parts[-2].rstrip(':')  # Remove trailing colon if present
                        line_num = int(line_num_str)
                        
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
                    print(f"Error parsing line {line_num}: {line} - {e}")
                    continue
    
    return errors

def apply_fixes(content, messages):
    """Apply fixes to the file content based on error messages"""
    original_content = content
    modified = False
    
    # Fix 1: Remove com.apple.eawt imports (Java 8 compatibility)
    if any('com.apple.eawt' in msg for msg in messages):
        lines = content.split('\n')
        new_lines = [line for line in lines if 'import com.apple.eawt' not in line]
        if len(new_lines) != len(lines):
            content = '\n'.join(new_lines)
            modified = True
            print("Applied fix: Removed com.apple.eawt imports")
    
    # Fix 2: Add missing FILENAME_SOURCE import
    if any('FILENAME_SOURCE' in msg and 'cannot be converted' in msg for msg in messages):
        if 'import jd.plugins.filesharing.FILENAME_SOURCE;' not in content:
            lines = content.split('\n')
            insert_pos = 0
            for i, line in enumerate(lines):
                if line.startswith('import jd.plugins.'):
                    insert_pos = i + 1
            lines.insert(insert_pos, 'import jd.plugins.filesharing.FILENAME_SOURCE;\n')
            content = '\n'.join(lines)
            modified = True
            print("Applied fix: Added FILENAME_SOURCE import")
    
    # Fix 4: Handle FileNameSource conversion issues
    if any('cannot be converted to FILENAME_SOURCE' in msg for msg in messages):
        lines = content.split('\n')
        new_lines = []
        for line in lines:
            # Handle assignments like "link.setFinalFileName(...);"
            if 'setFinalFileName(' in line and 'String' in str(line):
                new_line = re.sub(r'(link\.setFinalFileName\()([^)]+)\)',
                                 lambda m: f'{m.group(1)}Long.parseLong({m.group(2)});',
                                 line)
                new_lines.append(new_line)
            else:
                new_lines.append(line)
        if len(new_lines) != len(lines):
            content = '\n'.join(new_lines)
            modified = True
            print("Applied fix: Handled FILENAME_SOURCE conversion")
    
    # Fix 5: Handle generic type mismatches (List to Set)
    if any('cannot be converted to Set' in msg for msg in messages):
        lines = content.split('\n')
        new_lines = []
        for line in lines:
            # Handle List<CAPTCHA_TYPE> to Set<CAPTCHA_TYPE> conversion
            if 'List<CAPTCHA_TYPE>' in line and 'Set<CAPTCHA_TYPE>' in line:
                new_line = line.replace('List<CAPTCHA_TYPE>', 'Set<CAPTCHA_TYPE>')
                new_lines.append(new_line)
                print("Applied fix: Changed List to Set in generic type")
            else:
                new_lines.append(line)
        if len(new_lines) != len(lines):
            content = '\n'.join(new_lines)
            modified = True
    
    return content, modified

def main():
    print("Starting JDownloader error fix process...")
    
    # Parse errors
    errors = parse_errors()
    print(f"Parsed {len(errors)} errors")
    
    if not errors:
        print("No errors found to fix")
        return
    
    # Group errors by file
    file_errors = {}
    for err in errors:
        f = str(err['file'])  # Ensure string key
        if f not in file_errors:
            file_errors[f] = []
        file_errors[f].append(err)
    
    fixes_applied = []
    
    # Process each file
    for filepath_str, error_list in file_errors.items():
        filepath = Path(filepath_str)
        if not filepath.exists():
            print(f"File not found: {filepath}")
            continue
            
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            original_content = content
            messages = [e['message'] for e in error_list]
            
            # Apply fixes
            content, modified = apply_fixes(content, messages)
            
            if modified:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes_applied.append(str(filepath))
                print(f"Fixed {filepath}")
                
        except Exception as e:
            print(f"Error processing {filepath_str}: {e}")
    
    print(f"\nApplied fixes to {len(fixes_applied)} files")
    for f in fixes_applied:
        print(f"  {f}")

if __name__ == "__main__":
    main()