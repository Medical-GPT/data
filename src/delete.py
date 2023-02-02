import shutil
import os
from constants import DATA_FOLDER

if __name__ == "__main__":
    if os.path.exists(DATA_FOLDER):
        shutil.rmtree(DATA_FOLDER)
