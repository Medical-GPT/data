from constants import PRETRAINING_DIR, PREPROCESSED_FILE
from tqdm import tqdm
import re

allowed_tokens = "\t\n !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
regex = re.compile("[^{}]+".format(allowed_tokens))

with open(PREPROCESSED_FILE, "w") as out_file:
    for txt_file in tqdm(PRETRAINING_DIR.glob("**/*.txt")):
        with open(txt_file, "r", encoding="iso-8859-1") as f:
            file_content = f.read()
        start_index = file_content.find("==== Body") + len("==== Body")
        end_index = (
            file_content.find("Acknowledgements")
            or file_content.find("Refs")
            or len(file_content)
        )

        body = file_content[start_index:end_index]
        body = regex.sub("", body)
        out_file.write(body)
