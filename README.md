# data
A repository for downloading and preprocessing the training and validation data for the `chatbot` repo.

## Using the package
You need to have python3 and Java installed.
Afterwards run `make install` in the root directory to install all repository dependencies.

## Loading the pretraining dataset (Used for running prerpocessing of chatbot)
Run `make download_pretraining` to download the raw files (~3GB compressed)
Run `make decompress_pretraining` to decompress the raw files
Run `make preprocess_pretraining` to produce a preprocessed input file used in pretraining in *chatbot* repo

## References
`medical-conversations.txt`
Data generated from OpenAI's ChatGPT language model 12/02/2023. Source: OpenAI, [https://openai.com/].