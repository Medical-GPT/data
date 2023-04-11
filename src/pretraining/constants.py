from pathlib import Path

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

PRETRAINING_DIR = DATA_DIR / "pretraining"
PRETRAINING_DIR.mkdir(exist_ok=True)

RAW_FILE_FOLDER = PRETRAINING_DIR / "raw"
RAW_FILE_FOLDER.mkdir(exist_ok=True)

PREPROCESSED_FILE = PRETRAINING_DIR / "preprocessed.txt"
