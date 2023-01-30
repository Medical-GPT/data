from drive import download_file_from_drive
from constants import FILE_IDS, RAW_FILE_FOLDER
import os
import shutil


def create_raw_file_folder():
    if os.path.exists(RAW_FILE_FOLDER):
        shutil.rmtree(RAW_FILE_FOLDER)
    os.mkdir(RAW_FILE_FOLDER)


def download_files():
    for index, file_id in enumerate(FILE_IDS):
        print(f"Downloading file {index+1}/4")
        download_file_from_drive(file_id, f"{RAW_FILE_FOLDER}/file{index}.txt")


def main():
    create_raw_file_folder()
    download_files()


if __name__ == "__main__":
    main()
