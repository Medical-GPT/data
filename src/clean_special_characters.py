import os

ALLOWED_CHARACTERS = "!\"#$%&'‘’()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]_`abcdefghijklmnopqrstuvwxyz{|}~ \n"
QUOTATIONS = "“”‘"


def clean_special_characters(file_path):
    parent_directory = "/".join(file_path.split("/")[:-1])
    temp_file = f"{parent_directory}/temp.txt"
    # fmt: off
    with \
        open(file_path, 'r') as in_file, \
        open(temp_file, 'w') as out_file:
    # fmt: on
        for line in in_file:
            for quotation in QUOTATIONS:
                line = line.replace(quotation, "\"")
            if any(c not in ALLOWED_CHARACTERS for c in line):
                continue
            out_file.write(line)

    os.remove(file_path)
    os.rename(temp_file, file_path)
