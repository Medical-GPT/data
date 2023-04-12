import tarfile
from constants import PRETRAINING_DIR

for gzip in PRETRAINING_DIR.glob("*.gz"):
    output_path = PRETRAINING_DIR

    print(f"Extracting {gzip} ...")

    # Open the gzipped file for reading
    with tarfile.open(gzip, "r:gz") as tar:
        # Extract all the files to the output folder
        tar.extractall(output_path)
