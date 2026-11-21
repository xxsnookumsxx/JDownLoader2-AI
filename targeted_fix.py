import re
from pathlib import Path

# Configuration
base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")
errors_file = r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk_errors.txt"

def main():
    print("Starting targeted fix process...")
    
    # Read all errors
    with open(errors_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse errors - simple approach
    error_lines = []
    for line in content.split('\n'):
        if ' error: ' in line:
            parts = line.split(' error: ', 1)
            if len(parts) >= 2:
                path_part = parts[0].strip()
                message = parts[1].strip()
                
                # Extract file path and line number
                path_parts = path_part.split(':')
                if len(path_parts) >= 2:
                    file_path_str = ':'.join(path_parts[:-1])
                    line_num = int(path_parts[-1])
                    
                    # Create full path
                    filepath = base_path / file_path_str.replace('\\', '/')
                    
                    error_lines.append((filepath, line_num, message))
    
    print(f"Found {len(error_lines)} error lines to process")
    
    # Group by file
    file_groups = {}
    for filepath, line_num, message in error_lines:
        if filepath not in file_groups:
            file_groups[filepath] = []
        file_groups[filepath].append((line_num, message))
    
    print(f"Errors grouped by {len(file_groups)} files")
    
    # Apply targeted fixes
    fixes_applied = 0
    for filepath, error_list in file_groups.items():
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            modified = False
            
            # Apply specific fixes based on error patterns
            for line_idx, (line_num, message) in enumerate(error_list):
                line = lines[line_num - 1]  # Convert to 0-based index
                
                # Pattern 1: Remove problematic com.apple.eawt imports
                if 'com.apple.eawt' in message and 'cannot find symbol' in message:
                    # Find and remove the import line
                    for i, line_content in enumerate(lines):
                        if 'import com.apple.eawt' in line_content:
                            lines[i] = '# ' + line_content  # Comment out the import
                            modified = True
                            print(f"  Commented out com.apple.eawt import in {filepath}:{line_num}")
                            break
                
                # Pattern 2: Handle String to long conversion
                if 'cannot be converted to long' in message:
                    # Look for assignment patterns and fix them
                    if ' = ' in line and 'long' in line and 'String' in str(line):
                        # Replace String with Long in assignments
                        lines[line_idx] = re.sub(r'(\w+)\s*=\s*String', r'\1 = Long', lines[line_idx])
                        modified = True
                        print(f"  Fixed String to Long conversion in {filepath}:{line_num}")
                
                # Pattern 3: Handle FILENAME_SOURCE issues
                if 'FILENAME_SOURCE' in message and 'cannot be converted' in message:
                    # Add the required import if missing
                    import_missing = True
                    for line in lines:
                        if 'import jd.plugins.filesharing.FILENAME_SOURCE' in line:
                            import_missing = False
                            break
                    
                    if import_missing:
                        # Find where to insert - after other jd.plugins imports
                        insert_pos = 0
                        for i, line_content in enumerate(lines):
                            if line_content.startswith('import jd.plugins.'):
                                insert_pos = i + 1
                        lines.insert(insert_pos, 'import jd.plugins.filesharing.FILENAME_SOURCE;\n')
                        modified = True
                        print(f"  Added FILENAME_SOURCE import in {filepath}")
                
                # Pattern 4: Handle generic type mismatches (List to Set)
                if 'cannot be converted to Set' in message:
                    # Replace List with Set in the line
                    if 'List<' in line and 'Set<' in line:
                        lines[line_idx] = line.replace('List<', 'Set<')
                        modified = True
                        print(f"  Changed List to Set in {filepath}:{line_num}")
            
            # Write back if modified
            if modified:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.writelines(lines)
                fixes_applied += 1
                print(f"  Saved fixes to {filepath}")
                
        except Exception as e:
            print(f"  Error processing {filepath}: {e}")
    
    print(f"\nCompleted. Applied fixes to {fixes_applied} files.")

if __name__ == "__main__":
    main()