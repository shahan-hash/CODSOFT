import pandas as pd

# Load captions file
captions = pd.read_csv("dataset/captions.txt")

print("Dataset Loaded Successfully")
print()

print("Shape:")
print(captions.shape)

print()

print("First 5 Rows:")
print(captions.head())

print()

print("Unique Images:")
print(captions["image"].nunique())