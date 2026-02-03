from pathlib import Path

def main():
    folder = Path("screenshots")
    if not folder.exists():
        raise SystemExit("screenshots/ folder not found")

    images = sorted([p for p in folder.iterdir() if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}])
    if not images:
        raise SystemExit("No screenshots found in screenshots/")

    for img in images:
        print(img.name)

if __name__ == "__main__":
    main()