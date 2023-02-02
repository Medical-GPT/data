from utils import create_folder, get_files, concat_files
from constants import COMBINED_FILE, RAW_FILE_FOLDER, PREPROCESSED_FILE_FOLDER


def concat_raw_files():
    create_folder(PREPROCESSED_FILE_FOLDER)
    raw_files = get_files(RAW_FILE_FOLDER)
    concat_files(raw_files, COMBINED_FILE)


if __name__ == "__main__":
    concat_raw_files()
