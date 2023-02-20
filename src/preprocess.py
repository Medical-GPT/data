from concat import concat_raw_files
from constants import COMBINED_FILE, PREPROCESSED_FILE
from spellcheck import correct_mistakes
import copy
import random
import os


def write_object(object, file):
    query = object["patient"] if random.random() > 0.5 else object["description"]
    answer = object["doctor"]

    file.write(query)
    file.write(answer)
    file.write("\n")


def preprocess(input_file_path, output_file_path):
    object_default = {
        "description": "",
        "patient": "",
        "doctor": "",
    }
    curr_object = copy.copy(object_default)

    # fmt: off
    with open(input_file_path, "r") as input_file, \
        open(output_file_path, "w") as output_file:
    # fmt: on

        input_file.readline()
        input_file.readline()
        input_file.readline()

        setting = None

        for line in input_file:
            if "id=" in line:
                write_object(curr_object, output_file)
                curr_object = copy.copy(object_default)
                continue

            if line == "Description\n":
                setting = "description"
                continue
            if line == "Patient:\n":
                setting = "patient"
                continue
            if line == "Doctor:\n":
                setting = "doctor"
                continue
            if line in ['\n', "Dialogue\n"]:
                setting = None
                continue
            if setting is None:
                continue
            curr_object[setting] += line

        write_object(curr_object, output_file)


def main():
    if not os.path.isfile(COMBINED_FILE):
        concat_raw_files()

    preprocess(COMBINED_FILE, PREPROCESSED_FILE)


if __name__ == "__main__":
    main()
