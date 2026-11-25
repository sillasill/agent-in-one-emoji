from pathlib import Path

OUTPUT = Path("/output/entry.txt")

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text("🧑‍💻", encoding="utf-8")
