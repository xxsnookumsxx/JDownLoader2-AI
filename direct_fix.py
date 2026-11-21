import os
from pathlib import Path

# Configuration
base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")

# List of files to fix and what fixes to apply
fixes = [
    # Fix 1: Add missing FILENAME_SOURCE import to multiple files
    {
        'files': [
            'jd/plugins/hoster/File2btcCom.java',
            'jd/plugins/hoster/File2btcCom.java',
            'jd/plugins/hoster/Mp4playerSite.java',
            'jd/plugins/hoster/PimpRollHostedTube.java',
            'jd/plugins/hoster/RarcloudsCom.java',
            'jd/plugins/hoster/XingyaodiskCom.java',
            'jd/plugins/hoster/FreeM3DownloadNet.java'
        ],
        'import': 'import jd.plugins.filesharing.FILENAME_SOURCE;'
    },
    # Fix 2: Fix String to long conversion issues
    {
        'files': [
            'jd/plugins/hoster/DebridFileCom.java',
            'jd/plugins/hoster/File2btcCom.java'
        ],
        'pattern': 'String.*long',
        'replacement': 'Long.parseLong'
    },
    # Fix 3: Fix method signature issues (common in hoster files)
    {
        'files': [
            'jd/plugins/hoster/AnonServices.java',
            'jd/plugins/hoster/ClipHunterCom.java',
            'jd/plugins/hoster/CloudvideoTv.java',
            'jd/plugins/hoster/DebridFileCom.java',
            'jd/plugins/hoster/DebridLinkFr2.java',
            'jd/plugins/hoster/DlFreeFr.java',
            'jd/plugins/hoster/EgofilesNet.java',
            'jd/plugins/hoster/FilelionsTo.java',
            'jd/plugins/hoster/FilericeCom.java',
            'jd/plugins/hoster/GounlimitedTo.java',
            'jd/plugins/hoster/HighstreamTv.java',
            'jd/plugins/hoster/Mp4playerSite.java',
            'jd/plugins/hoster/PimpRollHostedTube.java',
            'jd/plugins/hoster/RarcloudsCom.java',
            'jd/plugins/hoster/SmoozedCom.java',
            'jd/plugins/hoster/StreamhideCom.java',
            'jd/plugins/hoster/StreamhubTo.java',
            'jd/plugins/hoster/StreamsbNet.java',
            'jd/plugins/hoster/SuperdownComBr.java',
            'jd/plugins/hoster/TransferChomikujPl.java',
            'jd/plugins/hoster/UploadbankCom.java',
            'jd/plugins/hoster/UplodNet.java',
            'jd/plugins/hoster/UseruploadNet.java',
            'jd/plugins/hoster/WyslijNet.java'
        ],
        'pattern': 'method .* cannot be applied to given types',
        'action': 'check method signature'
    },
    # Fix 5: Fix com.apple.eawt imports
    {
        'files': [
            'gui/GuiUtils.java',
            'gui/toolbar/ConvertCLRScriptAction.java',
            'gui/toolbar/action/CaptchaToogle9KWAction.java',
            'gui/toolbar/action/CaptchaToogleAntiCaptchaAction.java',
            'gui/toolbar/action/CaptchaToogleBrowserSolverAction.java',
            'gui/toolbar/action/CaptchaToogleBrowserSolverAction.java',
            'gui/toolbar/action/CaptchaToogleCheapCaptchaAction.java',
            'gui/toolbar/action/CaptchaToogleCheapCaptchaAction.java',
            'gui/toolbar/action/CaptchaToogleDBCAction.java',
            'gui/toolbar/action/CaptchaToogleDialogAction.java',
            'gui/toolbar/action/CaptchaToogleDialogAction.java',
            'gui/toolbar/action/CaptchaToogleEndCaptchaAction.java',
            'gui/toolbar/action/CaptchaToogleEndCaptchaAction.java',
            'gui/toolbar/action/CaptchaToogleImageTyperzAction.java',
            'gui/toolbar/action/CaptchaToogleImageTyperzAction.java',
            'gui/toolbar/action/CaptchaToogleJACAction.java',
            'gui/toolbar/action/CaptchaToogleMyJDRemoteAction.java',
            'gui/toolbar/action/CaptchaToogleTwoCaptchaAction.java'
        ],
        'pattern': 'package com.apple.eawt does not exist',
        'action': 'remove import'
    }
]

def apply_fix(file_path, fix_config):
    """Apply a specific fix to a file"""
    file_path = Path(file_path)
    if not file_path.exists():
        print(f"File not found: {file_path}")
        return False
        
    print(f"Applying fix to {file_path}")
    
    # Read file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    modified_content = content
    modified = False
    
    config = fix_config
    
    if 'import' in config:
        # Add or remove import
        lines = content.split('\n')
        import_line = config['import']
        
        if 'remove' in config.get('action', ''):
            # Remove import
            new_lines = [line for line in lines if 'import com.apple.eawt' not in line]
            if len(new_lines) != len(lines):
                content = '\n'.join(new_lines)
                modified = True
                print(f"  Removed com.apple.eawt import from {file_path}")
        else:
            # Add import
            if config['import'] not in content:
                lines = content.split('\n')
                insert_pos = 0
                for i, line in enumerate(lines):
                    if line.startswith('import jd.plugins.'):
                        insert_pos = i + 1
                lines.insert(insert_pos, config['import'])
                content = '\n'.join(lines)
                modified = True
                print(f"  Added FILENAME_SOURCE import to {file_path}")
    
    if 'pattern' in config:
        # Pattern matching fix
        if 'replacement' in config:
            # Simple string replacement
            if config['pattern'] in content:
                modified_content = content.replace(config['pattern'], config['replacement'])
                if modified_content != content:
                    content = modified_content
                    modified = True
                    print(f"  Applied pattern replacement in {file_path}")
        elif 'action' in config and config['action'] == 'check method signature':
            # For method signature issues, we'd need more complex logic
            print(f"  Would check method signature in {file_path} (not implemented)")
    
    # Write back if modified
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  Saved changes to {file_path}")
        return True
    
    return False

def main():
    print("Starting direct fix process...")
    
    # Apply all fixes
    total_fixed = 0
    for fix_config in fixes:
        for file_path in fix_config['files']:
            if apply_fix(file_path, fix_config):
                total_fixed += 1
    
    print(f"\nTotal files fixed: {total_fixed}")

if __name__ == "__main__":
    main()