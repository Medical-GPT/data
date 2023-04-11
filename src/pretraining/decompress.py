import tarfile
from constants import RAW_FILE_FOLDER

for gzip in RAW_FILE_FOLDER.glob("*.gz"):
    output_path = RAW_FILE_FOLDER

    print(f"Extracting {gzip} ...")

    # Open the gzipped file for reading
    with tarfile.open(gzip, "r:gz") as tar:
        # Extract all the files to the output folder
        tar.extractall(output_path)
