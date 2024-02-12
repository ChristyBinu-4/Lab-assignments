import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.applications import InceptionV3
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

# Load the pre-trained InceptionV3 model (without the top classification layer)
inception_model = InceptionV3(weights='imagenet')
inception_model = Model(inception_model.input, inception_model.layers[-2].output)

# Load the tokenizers and the pre-trained LSTM model
tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(open('tokenizer.txt').readlines())
model = load_model('image_captioning_model.h5')

# Function to generate captions for given images
def generate_caption(image_path):
    img = image.load_img(image_path, target_size=(299, 299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    features = inception_model.predict(x)
    caption = 'startseq'
    for i in range(20):  # Maximum length of the caption
        sequence = tokenizer.texts_to_sequences([caption])[0]
        sequence = pad_sequences([sequence], maxlen=21)  # 20 + 1 (startseq)
        y_pred = model.predict([features, sequence], verbose=0)
        y_pred = np.argmax(y_pred)
        word = ''
        for word_, index in tokenizer.word_index.items():
            if index == y_pred:
                word = word_
                break
        if word == 'endseq':
            break
        caption += ' ' + word
    return caption

# Image captioning example
image_path = 'example_image.jpg'
caption = generate_caption(image_path)
print("Caption:", caption)

# Show the image
img = image.load_img(image_path)
plt.imshow(img)
plt.axis('off')
plt.show()
