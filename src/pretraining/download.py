import requests
from tqdm import tqdm
from constants import PRETRAINING_DIR

"""
PMC Open Access Subset [Internet]. Bethesda (MD): National Library of Medicine.
2003 - 10.03.2023. Available from https://www.ncbi.nlm.nih.gov/pmc/tools/openftlist/.
"""
url = "https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/oa_noncomm/txt/"

files = [
    "oa_noncomm_txt.PMC001xxxxxx.baseline.2023-02-09.tar.gz",
    "oa_noncomm_txt.PMC002xxxxxx.baseline.2023-02-09.tar.gz",
    "oa_noncomm_txt.PMC003xxxxxx.baseline.2023-02-09.tar.gz",
]

for idx, file in tqdm(enumerate(files), total=len(files)):
    save_path = PRETRAINING_DIR / file
    file_url = url + file
    response = requests.get(file_url, stream=True)
    print(response)
    with open(save_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
