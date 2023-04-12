from pathlib import Path

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

PRETRAINING_DIR = DATA_DIR / "pretraining"
PRETRAINING_DIR.mkdir(exist_ok=True)

PREPROCESSED_FILE = DATA_DIR / "pretraining.txt"
