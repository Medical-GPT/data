from pathlib import Path

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

PREPROCESSED_FILE = DATA_DIR / "empathic-finetuning.txt"
