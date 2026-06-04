import pandas as pd

df = pd.read_csv("outputs/cleaned_captions.csv")

captions = df["clean_caption"]

max_length = max(
    len(caption.split())
    for caption in captions
)

print("Maximum Caption Length:", max_length)