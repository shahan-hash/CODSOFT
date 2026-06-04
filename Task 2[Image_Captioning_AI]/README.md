# 🖼️ Image Captioning AI

## Overview

Image Captioning AI is a deep learning project that combines Computer Vision and Natural Language Processing to automatically generate captions for images.

The system uses:

* ResNet50 for image feature extraction
* LSTM (Recurrent Neural Network) for custom caption generation
* BLIP Transformer for advanced caption generation
* Streamlit for the user interface

---

## Features

* Upload any image
* Generate image captions automatically
* Custom trained ResNet50 + LSTM model
* BLIP Transformer caption comparison
* Interactive Streamlit web application

---

## Dataset

Flickr8k Dataset

* Total Images: 8091
* Total Captions: 40455

---

## Technologies Used

* Python
* TensorFlow
* Streamlit
* ResNet50
* LSTM
* Transformers
* BLIP
* NumPy
* Pillow

---

## Project Structure

```text
Image_Captioning_AI
│
├── app
├── src
├── models
├── dataset
├── outputs
├── requirements.txt
└── README.md
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Run Project

```bash
python -m streamlit run app/app.py
```

---
## Note

The trained model file (caption_model.keras) is not included in this repository due to file size limitations.

The project code, training pipeline, and Streamlit application are fully included.

## Author

Shahan Ahmad

