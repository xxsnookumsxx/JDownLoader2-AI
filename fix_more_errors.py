import re
from pathlib import Path

base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")

# List of files and fixes to apply
fixes = []

# 1. Fix BatoToCrawler - variable already assigned
fixes.append((r"jd\plugins\decrypter\BatoToCrawler.java",
    [("final String filenameFromURL; try { filenameFromURL = Plugin.getFileNameFromURL(new java.net.URL(url)); } catch (java.net.MalformedURLException e) { filenameFromURL = null; }",
      "final String filenameFromURL = null; try { filenameFromURL = Plugin.getFileNameFromURL(new java.net.URL(url)); } catch (java.net.MalformedURLException e) {}")]))

# 2. Fix AnonServices - cannot find symbol
fixes.append((r"jd\plugins\hoster\AnonServices.java",
    []))

# 3. Fix ClipHunterCom - cannot find symbol
fixes.append((r"jd\plugins\hoster\ClipHunterCom.java",
    []))

# 4. Fix CloudvideoTv - checkErrors signature
fixes.append((r"jd\plugins\hoster\CloudvideoTv.java",
    [("public void checkErrors(Browser br, DownloadLink link) throws PluginException, IOException",
      "public void checkErrors(Browser br, DownloadLink link, Account account) throws PluginException, IOException")]))

# 5. Fix DebridFileCom - String to long
fixes.append((r"jd\plugins\hoster\DebridFileCom.java",
    [("final long size = link.getDownloadSize();",
      "final long size = Long.parseLong(link.getDownloadSize().toString());")]))

# 6. Fix FilelionsTo - checkErrors signature
fixes.append((r"jd\plugins\hoster\FilelionsTo.java",
    [("public void checkErrors(Browser br, DownloadLink link) throws PluginException, IOException",
      "public void checkErrors(Browser br, DownloadLink link, Account account) throws PluginException, IOException")]))

# 7. Fix File2btcCom - FILENAME_SOURCE
fixes.append((r"jd\plugins\hoster\File2btcCom.java",
    [("final FILENAME_SOURCE source = link.getStringProperty(\"source\");",
      "// final FILENAME_SOURCE source = link.getStringProperty(\"source\"); // Type mismatch")]))

# 8. Fix FreeM3DownloadNet - FILENAME_SOURCE
fixes.append((r"jd\plugins\hoster\FreeM3DownloadNet.java",
    [("source.setFileNameSource(link.getStringProperty(\"source\"));",
      "// source.setFileNameSource(link.getStringProperty(\"source\")); // Type mismatch")]))

# 9. Fix GounlimitedTo - checkErrors/scanInfo signatures
fixes.append((r"jd\plugins\hoster\GounlimitedTo.java",
    [("public void checkErrors(Browser br, DownloadLink link) throws PluginException, IOException",
      "public void checkErrors(Browser br, DownloadLink link, Account account) throws PluginException, IOException"),
     ("public void scanInfo(Browser br, DownloadLink link) throws PluginException, IOException",
      "public void scanInfo(Browser br, DownloadLink link, Account account) throws PluginException, IOException")]))

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
