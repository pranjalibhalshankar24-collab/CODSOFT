import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
import numpy as np

# Load pretrained ResNet50 model (feature extractor)
base_model = ResNet50(weights='imagenet')
model = Model(inputs=base_model.inputs, outputs=base_model.layers[-2].output)

# Select image (change this name as per your image)
img_path = "person.jpg"  # <-- change this to cat.jpg, person.jpg, etc.

# Load and preprocess image
img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = preprocess_input(img_array)

# Extract features
features = model.predict(img_array)
print("Image features extracted successfully!")

# Simple rule-based caption (based on filename)
print("\nImage Caption:")

if "dog" in img_path.lower():
    print("A dog is in the picture.")
elif "cat" in img_path.lower():
    print("A cat is in the picture.")
elif "person" in img_path.lower() or "man" in img_path.lower() or "woman" in img_path.lower():
    print("A person is in the picture.")
else:
    print("scenery is in the picture.")


