from concat import concat_raw_files
from constants import COMBINED_FILE, PREPROCESSED_FILE
import copy
import random
import os
from tqdm import tqdm
import language_tool_python
from utils import get_num_lines
from clean_special_characters import clean_special_characters

# Start a Java server for spelling correction
LANGUAGE_TOOL = language_tool_python.LanguageTool("en-US")


def correct_object(object):
    ret = {}
    for key, value in object.items():
        ret[key] = LANGUAGE_TOOL.correct(value)
    return ret


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

        for line in tqdm(input_file, total=get_num_lines(input_file_path)):
            if "id=" in line:
                corr_object = correct_object(curr_object)
                write_object(corr_object, output_file)
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

        corr_object = correct_object(curr_object)
        write_object(corr_object, output_file)


def main():
    if not os.path.isfile(COMBINED_FILE):
        concat_raw_files()

    preprocess(COMBINED_FILE, PREPROCESSED_FILE)
    clean_special_characters(PREPROCESSED_FILE)


if __name__ == "__main__":
    main()
