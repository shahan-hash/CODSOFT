import pandas as pd
import pickle

# Load cleaned captions
df = pd.read_csv("outputs/cleaned_captions.csv")

mapping = {}

for _, row in df.iterrows():

    image_id = row["image"].split(".")[0]
    caption = row["clean_caption"]

    if image_id not in mapping:
        mapping[image_id] = []

    mapping[image_id].append(caption)

print("Total Images:", len(mapping))

# Save mapping
with open("models/captions_mapping.pkl", "wb") as f:
    pickle.dump(mapping, f)

print("captions_mapping.pkl saved successfully!")