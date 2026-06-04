import pandas as pd
import pickle
from tensorflow.keras.preprocessing.text import Tokenizer

# Load cleaned captions
df = pd.read_csv("outputs/cleaned_captions.csv")

captions = df["clean_caption"].tolist()

print("Total Captions:", len(captions))

# Create tokenizer
tokenizer = Tokenizer()
tokenizer.fit_on_texts(captions)

vocab_size = len(tokenizer.word_index) + 1

print("Vocabulary Size:", vocab_size)

# Save tokenizer
with open("models/tokenizer.pkl", "wb") as f:
    pickle.dump(tokenizer, f)

print("Tokenizer saved successfully!")

# Show sample words
sample_words = list(tokenizer.word_index.items())[:20]

print("\nFirst 20 Words:")
for word, index in sample_words:
    print(f"{word} -> {index}")