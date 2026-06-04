import os
import pickle
import numpy as np
from tqdm import tqdm

from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import Model

# Load pretrained ResNet50
model = ResNet50(weights='imagenet')

# Remove last classification layer
model = Model(
    inputs=model.inputs,
    outputs=model.layers[-2].output
)

print("ResNet50 Loaded Successfully")

image_folder = "dataset/Images"

features = {}

images = os.listdir(image_folder)

for image_name in tqdm(images):

    image_path = os.path.join(
        image_folder,
        image_name
    )

    try:
        image = load_img(
            image_path,
            target_size=(224, 224)
        )

        image = img_to_array(image)

        image = np.expand_dims(
            image,
            axis=0
        )

        image = preprocess_input(image)

        feature = model.predict(
            image,
            verbose=0
        )

        image_id = image_name.split(".")[0]

        features[image_id] = feature

    except Exception as e:
        print(f"Error: {image_name}")
        print(e)

print("\nTotal Features Extracted:",
      len(features))

# Save features
with open(
    "models/image_features.pkl",
    "wb"
) as f:
    pickle.dump(features, f)

print("Features Saved Successfully!")