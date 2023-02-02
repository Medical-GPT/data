import os
import shutil
from os import listdir
from os.path import isfile, join


def create_folder(name):
    if os.path.exists(name):
        shutil.rmtree(name)
    os.mkdir(name)


def get_files(directory):
    return [
        join(directory, f) for f in listdir(directory) if isfile(join(directory, f))
    ]


def concat_files(files, output_file):
    with open(output_file, "w") as outfile:
        for file in files:
            with open(file) as infile:
                for line in infile:
                    outfile.write(line)
