import re
from pathlib import Path

# Configuration
base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")
errors_file = r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk_errors.txt"

def main():
    print("Starting quick fix process...")
    
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
    
    # Apply simple fixes
    fixes_applied = 0
    for filepath, error_list in file_groups.items():
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            original_lines = lines.copy()
            modified = False
            
            # Check for common patterns and apply fixes
            for line_idx, (line_num, message) in enumerate(error_list):
                line = lines[line_num - 1]  # Convert to 0-based index
                
                # Fix 1: Add missing imports for common errors
                if 'cannot find symbol' in message and 'com.apple.eawt' in str(line):
                    # Remove com.apple.eawt import
                    if 'import com.apple.eawt' in line:
                        lines[line_idx] = line.replace('import com.apple.eawt', '# import com.apple.eawt (removed for Java 8)')
                        modified = True
                        print(f"  Removed com.apple.eawt import in {filepath}:{line_num}")
                
                # Fix 2: Handle String to long conversion
                if 'cannot be converted to long' in message:
                    # Look for assignment patterns
                    if ' = ' in line and 'long' in line:
                        # Simple replacement for common patterns
                        lines[line_idx] = line.replace('String', 'Long')
                        modified = True
                        print(f"  Modified long conversion in {filepath}:{line_num}")
                
                # Fix 3: Handle FILENAME_SOURCE issues
                if 'FILENAME_SOURCE' in message and 'cannot be converted' in message:
                    # Add import if missing
                    if 'import jd.plugins.filesharing.FILENAME_SOURCE' not in ''.join(lines):
                        insert_pos = 0
                        for i, l in enumerate(lines):
                            if l.startswith('import jd.plugins.'):
                                insert_pos = i + 1
                        lines.insert(insert_pos, 'import jd.plugins.filesharing.FILENAME_SOURCE;\n')
                        modified = True
                        print(f"  Added FILENAME_SOURCE import in {filepath}")
                
                # Fix 4: Handle generic type mismatches
                if 'cannot be converted to Set' in message:
                    # Replace List with Set in generic types
                    if 'List<' in line and 'Set<' in line:
                        lines[line_idx] = line.replace('List<', 'Set<')
                        modified = True
                        print(f"  Changed List to Set in {filepath}:{line_num}")
            
            # Write back if modified
            if modified:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.writelines(lines)
                fixes_applied += 1
                print(f"  Saved changes to {filepath}")
                
        except Exception as e:
            print(f"  Error processing {filepath}: {e}")
    
    print(f"\nApplied fixes to {fixes_applied} files")

if __name__ == "__main__":
    main()