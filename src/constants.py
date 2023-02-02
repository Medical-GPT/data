import os

FILE_IDS = [
    "10ZsJFpAQViVkJ2k-hm9E3rng9OTkH5kY",
    "1LqTkQV1NXfQqg8h0qdJEp1IA8zn0eK5x",
    "1dXdgfup9bUttktNDoM1lmv6pmpACnx1h",
    "14e0ad2CNqq2_8Z9yzuN1YApoOoi5unp5",
]

ROOT_DIR = "/".join(os.path.dirname(os.path.abspath(__file__)).split("/")[:-1])

DATA_FOLDER = f"{ROOT_DIR}/data"
RAW_FILE_FOLDER = f"{DATA_FOLDER}/raw"
PREPROCESSED_FILE_FOLDER = f"{DATA_FOLDER}/preprocessed"
COMBINED_FILE = f"{PREPROCESSED_FILE_FOLDER}/combined.txt"
PREPROCESSED_FILE = f"{PREPROCESSED_FILE_FOLDER}/preprocessed.txt"
