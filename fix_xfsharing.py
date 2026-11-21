import re
from pathlib import Path

base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")

# Direct file fixes based on known error patterns
fixes = []

# Fix BatoToCrawler - final variable already assigned
fixes.append((r"jd\plugins\decrypter\BatoToCrawler.java",
    [("String filenameFromURL = null;", "// String filenameFromURL = null; // Will be set below")]))

# Fix all XFileSharingProBasic checkErrors/scanInfo signatures
# These methods have changed to accept Account parameter
xfsharing_files = [
    "CloudvideoTv.java", "FilelionsTo.java", "GounlimitedTo.java", 
    "StreamhideCom.java", "StreamhubTo.java", "StreamsbNet.java",
    "UploadhubIo.java", "UplodNet.java", "UseruploadNet.java",
    "RacatyNet.java", "EgofilesNet.java", "FilericeCom.java",
    "SmoozedCom.java", "HighstreamTv.java", "EightTracksCom.java"
]

for f in xfsharing_files:
    fixes.append((rf"jd\plugins\hoster\{f}", 
        [("public void checkErrors(Browser br, DownloadLink link) throws PluginException, IOException",
          "public void checkErrors(Browser br, DownloadLink link, Account account) throws PluginException, IOException")]))

# Add scanInfo fix for GounlimitedTo
fixes.append((r"jd\plugins\hoster\GounlimitedTo.java",
    [("public void scanInfo(Browser br, DownloadLink link) throws PluginException, IOException",
      "public void scanInfo(Browser br, DownloadLink link, Account account) throws PluginException, IOException")]))

# Apply fixes
fixes_applied = []

for rel_file, replacements in fixes:
    filepath = base_path / rel_file
    if not filepath.exists():
        print(f"File not found: {rel_file}")
        continue
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        
        original = content
        
        for old_str, new_str in replacements:
            content = content.replace(old_str, new_str)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            fixes_applied.append(rel_file)
            print(f"Fixed: {rel_file}")
            
    except Exception as e:
        print(f"Error processing {rel_file}: {e}")

print(f"\nTotal files fixed: {len(fixes_applied)}")
