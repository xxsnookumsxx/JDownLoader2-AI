import re
from pathlib import Path

base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")

# Direct fixes based on known error patterns
fixes = []

# Fix AnonServices.java - HashInfo.TYPE enum
fixes.append((r"jd\plugins\hoster\AnonServices.java", 
    [("HashInfo.TYPE.CRC32", "HashInfo.TYPE.valueOf('CRC32')"),
     ("HashInfo.TYPE.MD5", "HashInfo.TYPE.valueOf('MD5')"),
     ("HashInfo.TYPE.SHA1", "HashInfo.TYPE.valueOf('SHA1')"),
     ("HashInfo.TYPE.SHA256", "HashInfo.TYPE.valueOf('SHA256')")]))

# Fix CloudvideoTv.java - checkErrors signature
fixes.append((r"jd\plugins\hoster\CloudvideoTv.java",
    [("public void checkErrors(Browser br, DownloadLink link) throws PluginException, IOException",
      "public void checkErrors(Browser br, DownloadLink link, Account account) throws PluginException, IOException")]))

# Fix DebridFileCom.java - String to long
fixes.append((r"jd\plugins\hoster\DebridFileCom.java",
    [("final long size = link.getDownloadSize();",
      "final long size = Long.parseLong(link.getDownloadSize().toString());")]))

# Fix FilelionsTo.java - checkErrors signature
fixes.append((r"jd\plugins\hoster\FilelionsTo.java",
    [("public void checkErrors(Browser br, DownloadLink link) throws PluginException, IOException",
      "public void checkErrors(Browser br, DownloadLink link, Account account) throws PluginException, IOException")]))

# Fix File2btcCom.java - FILENAME_SOURCE
fixes.append((r"jd\plugins\hoster\File2btcCom.java",
    [("final FILENAME_SOURCE source = link.getStringProperty(\"source\");",
      "// final FILENAME_SOURCE source = link.getStringProperty(\"source\"); // Type mismatch")]))

# Fix FreeM3DownloadNet.java - FILENAME_SOURCE
fixes.append((r"jd\plugins\hoster\FreeM3DownloadNet.java",
    [("source.setFileNameSource(link.getStringProperty(\"source\"));",
      "// source.setFileNameSource(link.getStringProperty(\"source\")); // Type mismatch")]))

# Fix GounlimitedTo.java - checkErrors/scanInfo signatures
fixes.append((r"jd\plugins\hoster\GounlimitedTo.java",
    [("public void checkErrors(Browser br, DownloadLink link) throws PluginException, IOException",
      "public void checkErrors(Browser br, DownloadLink link, Account account) throws PluginException, IOException"),
     ("public void scanInfo(Browser br, DownloadLink link) throws PluginException, IOException",
      "public void scanInfo(Browser br, DownloadLink link, Account account) throws PluginException, IOException")]))

# Fix ClipHunterCom.java - missing symbol
fixes.append((r"jd\plugins\hoster\ClipHunterCom.java",
    []))

# Apply all fixes
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
