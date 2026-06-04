import sys
import os
import pickle
import numpy as np
import streamlit as st

from PIL import Image

from tensorflow.keras.models import load_model, Model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input

from transformers import BlipProcessor, BlipForConditionalGeneration

sys.path.append(os.path.abspath("src"))
from config import MAX_LENGTH


st.set_page_config(
    page_title="Image Captioning AI",
    page_icon="🖼️",
    layout="centered"
)

st.title("🖼️ Image Captioning AI")
st.write("Custom ResNet50 + LSTM model with accurate BLIP transformer comparison.")


@st.cache_resource
def load_custom_models():
    with open("models/tokenizer.pkl", "rb") as f:
        tokenizer = pickle.load(f)

    caption_model = load_model("models/caption_model.keras")

    resnet = ResNet50(weights="imagenet")
    resnet = Model(
        inputs=resnet.inputs,
        outputs=resnet.layers[-2].output
    )

    index_word = {
        index: word
        for word, index in tokenizer.word_index.items()
    }

    return tokenizer, caption_model, resnet, index_word


@st.cache_resource
def load_blip_model():
    processor = BlipProcessor.from_pretrained(
        "Salesforce/blip-image-captioning-base"
    )

    model = BlipForConditionalGeneration.from_pretrained(
        "Salesforce/blip-image-captioning-base"
    )

    return processor, model


def extract_features(image, resnet_model):
    image = image.convert("RGB")
    image = image.resize((224, 224))

    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)

    return resnet_model.predict(image, verbose=0)


def clean_caption(caption):
    words = caption.split()

    words = [
        word for word in words
        if word not in ["startseq", "endseq"]
    ]

    return " ".join(words)


def predict_custom_caption(
        caption_model,
        image_feature,
        tokenizer,
        index_word,
        max_length):

    caption = "startseq"
    used_words = []

    for _ in range(max_length):
        sequence = tokenizer.texts_to_sequences([caption])[0]

        sequence = pad_sequences(
            [sequence],
            maxlen=max_length
        )

        yhat = caption_model.predict(
            [image_feature, sequence],
            verbose=0
        )

        yhat = np.argmax(yhat[0])

        word = index_word.get(yhat)

        if word is None:
            break

        if word == "endseq":
            break

        if len(used_words) > 0 and word == used_words[-1]:
            break

        used_words.append(word)
        caption += " " + word

    return clean_caption(caption)


def predict_blip_caption(image, processor, model):
    image = image.convert("RGB")

    inputs = processor(
        images=image,
        return_tensors="pt"
    )

    output = model.generate(
        **inputs,
        max_new_tokens=50
    )

    caption = processor.decode(
        output[0],
        skip_special_tokens=True
    )

    return caption


tokenizer, caption_model, resnet_model, index_word = load_custom_models()
blip_processor, blip_model = load_blip_model()

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    if st.button("Generate Caption"):
        with st.spinner("Generating captions..."):
            image_feature = extract_features(
                image,
                resnet_model
            )

            custom_caption = predict_custom_caption(
                caption_model,
                image_feature,
                tokenizer,
                index_word,
                MAX_LENGTH
            )

            blip_caption = predict_blip_caption(
                image,
                blip_processor,
                blip_model
            )

        st.subheader("BLIP Transformer Caption")
        st.success(blip_caption)

        st.subheader("Custom Trained Model Caption")
        st.info(custom_caption)