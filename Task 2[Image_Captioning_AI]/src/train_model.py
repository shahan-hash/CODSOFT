import pickle

from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Embedding
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import add

from config import *
from data_generator import data_generator

# Load tokenizer
with open("models/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

# Load features
with open("models/image_features.pkl", "rb") as f:
    features = pickle.load(f)

# Load caption mapping
with open("models/captions_mapping.pkl", "rb") as f:
    mapping = pickle.load(f)

print("Files Loaded Successfully")

# Image feature branch
inputs1 = Input(shape=(2048,))
fe1 = Dropout(0.4)(inputs1)
fe2 = Dense(256, activation="relu")(fe1)

# Caption branch
inputs2 = Input(shape=(MAX_LENGTH,))
se1 = Embedding(
    VOCAB_SIZE,
    EMBEDDING_DIM,
    mask_zero=True
)(inputs2)

se2 = Dropout(0.4)(se1)
se3 = LSTM(LSTM_UNITS)(se2)

# Merge
decoder1 = add([fe2, se3])

decoder2 = Dense(
    256,
    activation="relu"
)(decoder1)

outputs = Dense(
    VOCAB_SIZE,
    activation="softmax"
)(decoder2)

model = Model(
    inputs=[inputs1, inputs2],
    outputs=outputs
)

model.compile(
    loss="categorical_crossentropy",
    optimizer="adam"
)

model.summary()

# Correct steps calculation
total_sequences = 0

for image_id, captions in mapping.items():
    for caption in captions:
        seq = tokenizer.texts_to_sequences([caption])[0]
        total_sequences += len(seq) - 1

steps = total_sequences // BATCH_SIZE

print("Total Training Sequences:", total_sequences)
print("Steps Per Epoch:", steps)

generator = data_generator(
    mapping,
    features,
    tokenizer,
    MAX_LENGTH,
    VOCAB_SIZE,
    BATCH_SIZE
)

model.fit(
    generator,
    epochs=EPOCHS,
    steps_per_epoch=steps
)

model.save(
    "models/caption_model.keras"
)

print("Model Saved Successfully!")