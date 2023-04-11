# data
A repository for downloading and preprocessing the training and validation data.

## Using the package
You need to have python3 and Java installed.
Afterwards run `make install` in the root directory to install all repository dependencies.

## Loading the pretraining dataset (Used for running prerpocessing of chatbot)
Run `make download_pretraining` to download the raw files (~3GB compressed)
Run `make decompress_pretraining` to decompress the raw files
Run `make preprocess_pretraining` to produce a preprocessed input file used in pretraining in *chatbot* repo

## Loading the dataset
Run `make download` to download the raw files used for training (~700MB)
Run `make preprocess` to preprocess the files

## References
URL to raw files in drive: https://drive.google.com/drive/folders/1g29ssimdZ6JzTST6Y8g6h-ogUNReBtJD


**MedDialog: a large-scale medical dialogue dataset**,
*Chen, Shu and Ju, Zeqian and Dong, Xiangyu and Fang, Hongchao and Wang, Sicheng and Yang, Yue and Zeng, Jiaqi and Zhang, Ruisi and Zhang, Ruoyu and Zhou, Meng and Zhu, Penghui and Xie, Pengtao*,

arXiv preprint arXiv:2004.03329,

2020

https://huggingface.co/datasets/medical_dialog
