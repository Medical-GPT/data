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

## References
`data/medical-finetuning.txt`, `data/empathic-finetuning.txt`

Data generated from OpenAI's ChatGPT language model 12/02/2023. Source: OpenAI, [https://openai.com/].

### Prompt used for generating medical data:
```
Can you generate similar conversational pairs as the ones below. They should be as unique as possible given the previously generated ones. You can start the prompt of the Patient as a question as well. Generate as much as the output can fit, after the message limit has been reached I will write "continue" and you will continue generating by starting from where you last left off:

Patient: Hi doctor, I've been experiencing a lot of dryness and itching in my eyes lately, and they feel very tired.
Doctor: I see. Have you noticed any changes in your vision, such as blurriness or difficulty focusing?

Patient: No, it's mostly just the dryness and itching.
Doctor: Based on your symptoms, it's possible that you have dry eye syndrome or an eye allergy. I would recommend a visit to an ophthalmologist to confirm the diagnosis and discuss treatment options.
```

### Prompt used for generating epathical data
```
Can you generate similar conversational pairs as the ones below. They should be as unique as possible given the previously generated ones. You can start the prompt of the Patient as a question as well. Generate as much as the output can fit, after the message limit has been reached I will write "continue" and you will continue generating by starting from where you last left off:

Original: I'm feeling really frustrated with a lack of progress in improving my communication skills.
Empathic: It can be frustrating when progress in communication skills feels slow. Have you thought about seeking support from a communication coach or therapist, or finding ways to practice active listening and assertiveness in your personal and professional relationships?

Original: I'm feeling really disappointed with a missed opportunity to travel or take a vacation.
Empathic: It's tough when plans fall through for travel or vacation. Have you thought about finding new ways to experience new cultures or destinations, such as through virtual experiences or local activities, or planning for future travel opportunities?

Original: You have a vision impairment.
Empathic: I know that losing or having reduced vision can be very challenging, but please know that there are resources and support available to help you. We'll explore different treatment options, such as vision aids or surgery, and we'll connect you with resources and support groups to help you navigate this journey. And please know that I'm here to support you every step of the way.
```