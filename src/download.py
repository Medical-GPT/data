from constants import FILE_IDS, DATA_FOLDER, RAW_FILE_FOLDER
from utils import create_folder
import gdown


def download_files():
    for index, file_id in enumerate(FILE_IDS):
        print(f"Downloading file {index+1}/4")
        gdown.download(id=file_id, output=f"{RAW_FILE_FOLDER}/file{index}.txt")


def main():
    create_folder(DATA_FOLDER)
    create_folder(RAW_FILE_FOLDER)
    download_files()


if __name__ == "__main__":
    main()
