from pathlib import Path

files = list(Path(".").glob("*.png"))

if not files:
    print("No PNG files found")
    exit(1)

for f in files:
    print(f.name)
