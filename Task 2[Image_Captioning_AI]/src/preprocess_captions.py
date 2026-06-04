import pandas as pd
import string
import pickle

# Load captions dataset
captions_df = pd.read_csv("dataset/captions.txt")

print("Dataset Loaded Successfully")
print("Total Captions:", len(captions_df))


def clean_caption(caption):
    # convert to lowercase
    caption = caption.lower()

    # remove punctuation
    caption = caption.translate(
        str.maketrans('', '', string.punctuation)
    )

    # remove extra spaces
    caption = caption.split()

    # keep words longer than 1 character
    caption = [word for word in caption if len(word) > 1]

    # join back
    caption = " ".join(caption)

    # add start and end tokens
    caption = "startseq " + caption + " endseq"

    return caption


captions_df["clean_caption"] = captions_df["caption"].apply(
    clean_caption
)

print("\nOriginal Caption:")
print(captions_df["caption"].iloc[0])

print("\nClean Caption:")
print(captions_df["clean_caption"].iloc[0])

# Save cleaned captions
captions_df.to_csv(
    "outputs/cleaned_captions.csv",
    index=False
)

print("\nSaved:")
print("outputs/cleaned_captions.csv")