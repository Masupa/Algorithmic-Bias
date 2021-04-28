import keras
import numpy as np
import streamlit as st
import tensorflow as tf
import utils.visualization as viz
import streamlit.components.v1 as components
import utils.load_models as load_models

from PIL import Image
import io


# Catch Models
models = load_models.utils_model()


# Compute Accuracy
def classify_images(img_file):

    # Model names
    model_names = ['M_A', 'M_B', 'M_C']

    # List to store accuracies for both modules on the same images
    accuracies = dict()

    for model_name in model_names:

        append_scores = list()

        for img_ in img_file:
            bytes_data = img_.getvalue()
            target_size = (180, 180)

            # Process Image
            img = Image.open(io.BytesIO(bytes_data))
            img = img.convert('RGB')
            img = img.resize(target_size, Image.NEAREST)

            img_array = keras.preprocessing.image.img_to_array(img)
            img_array = tf.expand_dims(img_array, 0)  # Create a batch

            # Make Prediction
            predictions = models[model_name].predict(img_array)
            score = tf.nn.softmax(predictions[0])

            # Append Scores
            append_scores.append(100 * np.max(score))

        # Dictionary ~ Key: Model and Values: Scores from Model
        accuracies[model_name] = append_scores

    return accuracies
