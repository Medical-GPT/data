# data
A repository for downloading and preprocessing the training and validation data for the `chatbot` repo.

## Using the package
You need to have python3 and Java installed.
Afterwards run `make install` in the root directory to install all repository dependencies.

## Loading the pretraining dataset (Used for running pretraining of chatbot)
Run `make pretraining` to prepare the pretraining dataset. The file `data/pretraining.txt` will appear once the process completes.

Alternatively, you can run each of the preprocessing steps 1 by 1 in case one of them fails.

1. Run `make download_pretraining` to download the raw files (~3GB compressed)
2. Run `make decompress_pretraining` to decompress the raw files
3. Run `make preprocess_pretraining` to produce a preprocessed input file used in pretraining in *chatbot* repo

## Loading empathic finetuning dataset (Used for finetuning the chatbot)
Run `make finetuning` to prepare the empathic finetuning dataset. The file `data/empathic-finetuning.txt` will appear once the process completes.

## References
`data/medical-finetuning.txt`

Data generated from OpenAI's ChatGPT language model 12/02/2023. Source: OpenAI, [https://openai.com/].

Prompt used for generating data:
```
Can you generate similar conversational pairs as the ones below. They should be as unique as possible given the previously generated ones. You can start the prompt of the Patient as a question as well. Generate as much as the output can fit, after the message limit has been reached I will write "continue" and you will continue generating by starting from where you last left off:

Patient: Hi doctor, I've been experiencing a lot of dryness and itching in my eyes lately, and they feel very tired.
Doctor: I see. Have you noticed any changes in your vision, such as blurriness or difficulty focusing?

Patient: No, it's mostly just the dryness and itching.
Doctor: Based on your symptoms, it's possible that you have dry eye syndrome or an eye allergy. I would recommend a visit to an ophthalmologist to confirm the diagnosis and discuss treatment options.

Patient: Hi doctor, I've been experiencing a lot of pain and discomfort in my pelvic area lately, especially during sex.
Doctor: I see. Have you experienced any changes in your menstrual cycle or vaginal discharge?
```


`data/empathic-finetuning.txt`

@inproceedings{rashkin-etal-2019-towards,
    title = "Towards Empathetic Open-domain Conversation Models: A New Benchmark and Dataset",
    author = "Rashkin, Hannah  and
      Smith, Eric Michael  and
      Li, Margaret  and
      Boureau, Y-Lan",
    booktitle = "Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2019",
    address = "Florence, Italy",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/P19-1534",
    doi = "10.18653/v1/P19-1534",
    pages = "5370--5381",
}
