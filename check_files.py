import os
from pathlib import Path

base_path = Path(r"D:\AI-Clients\Agents-Only\JDownLoader2-AI\svn_trunk\src")

print("Listing files in base_path:")
for item in base_path.iterdir():
    if item.is_dir():
        print(f"  [DIR] {item.name}")
    else:
        print(f"  [FILE] {item.name}")

print(f"\nTotal items: {len(list(base_path.iterdir()))}")

# Check if some specific files exist
test_files = [
    "jd/plugins/hoster/AnonServices.java",
    "jd/plugins/hoster/DebridFileCom.java", 
    "captcha/api/CaptchaForwarder.java"
]

for file_rel in test_files:
    file_path = base_path / file_rel.replace('/', os.sep)
    print(f"Checking {file_rel}: {'FOUND' if file_path.exists() else 'NOT FOUND'}")
    if file_path.exists():
        print(f"  Size: {file_path.stat().st_size} bytes")