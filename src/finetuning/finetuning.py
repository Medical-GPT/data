import pandas as pd
from datasets import load_dataset
from constants import PREPROCESSED_FILE

# Load the empathetic_dialogues dataset from Hugging Face
dataset = load_dataset("empathetic_dialogues")

# Extract the test dataset
test_data = dataset["test"]

# Create a pandas DataFrame from the test dataset
df = pd.DataFrame(test_data)

# Select the "prompt" and "utterance" columns
df = df[["prompt", "utterance"]]

# Replace '_comma_' with ','
df["prompt"] = df["prompt"].str.replace("_comma_", ",")
df["utterance"] = df["utterance"].str.replace("_comma_", ",")

# Save the dataset in the desired format
with open(PREPROCESSED_FILE, "w") as f:
    for index, row in df.iterrows():
        f.write(f"{row['prompt']}\n{row['utterance']}\n\n")
