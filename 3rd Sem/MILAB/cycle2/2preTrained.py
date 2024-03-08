import numpy as np
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.models import Model

# Load pre-trained ResNet50 model
resnet50_model = ResNet50(weights='imagenet', include_top=False)

# Define a new model with ResNet50 base
model = Model(inputs=resnet50_model.input, outputs=resnet50_model.get_layer('conv5_block3_out').output)

# Function to extract features from images using ResNet50
def extract_features(img_path):
    img = image.load_img(img_path, target_size=(224, 224))  # ResNet50 expects images of size 224x224
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)  # Preprocess the input data to align with the way ResNet50 was trained
    features = model.predict(x)
    return features.flatten()  # Flatten the features to use them as input to another classifier

# Example usage
img_path = 'path_to_your_image.jpg'
features = extract_features(img_path)
print("Shape of extracted features:", features.shape)
