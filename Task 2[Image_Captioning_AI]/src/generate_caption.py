import pickle
import numpy as np

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

from config import MAX_LENGTH

# Load tokenizer
with open("models/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

# Fast index to word dictionary
index_word = {
    index: word
    for word, index in tokenizer.word_index.items()
}

# Load trained model
model = load_model("models/caption_model.keras")

# Load image features
with open("models/image_features.pkl", "rb") as f:
    features = pickle.load(f)


def clean_output_caption(caption):
    words = caption.split()

    # Remove startseq and endseq
    words = [
        word for word in words
        if word not in ["startseq", "endseq"]
    ]

    return " ".join(words)


def predict_caption(model, image_feature, tokenizer, max_length):
    caption = "startseq"
    used_words = []

    for _ in range(max_length):
        sequence = tokenizer.texts_to_sequences([caption])[0]

        sequence = pad_sequences(
            [sequence],
            maxlen=max_length
        )

        yhat = model.predict(
            [image_feature, sequence],
            verbose=0
        )

        yhat = np.argmax(yhat[0])

        word = index_word.get(yhat)

        if word is None:
            break

        if word == "endseq":
            caption += " " + word
            break

        # Stop if same word repeats too much
        if len(used_words) > 0 and word == used_words[-1]:
            break

        used_words.append(word)

        caption += " " + word

    return clean_output_caption(caption)


# Pick one image already in features
image_id = list(features.keys())[0]

caption = predict_caption(
    model,
    features[image_id],
    tokenizer,
    MAX_LENGTH
)

print("Image ID:")
print(image_id)

print("\nGenerated Caption:")
print(caption)