from constants import PREPROCESSED_FILE, PREPROCESSED_FILE_FOLDER
import os

assert os.path.exists(PREPROCESSED_FILE), "Make sure you have preprocessed data"

ALLOWED_CHARACTERS = "!\"#$%&'‘’()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]_`abcdefghijklmnopqrstuvwxyz{|}~ \n"
QUOTATIONS = "“”‘"


def clean():
    temp_file = f"{PREPROCESSED_FILE_FOLDER}/temp.txt"
    # fmt: off
    with \
        open(PREPROCESSED_FILE, 'r') as in_file, \
        open(temp_file, 'w') as out_file:
    # fmt: on
        for line in in_file:
            for quotation in QUOTATIONS:
                line = line.replace(quotation, "\"")
            if any(c not in ALLOWED_CHARACTERS for c in line):
                continue
            out_file.write(line)


if __name__ == "__main__":
    clean()
