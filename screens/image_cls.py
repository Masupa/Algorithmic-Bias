import io
import keras
import numpy as np
import streamlit as st
import tensorflow as tf
import PIL.Image as Image
import streamlit.components.v1 as components
import utils.load_models as load_models
import utils.confidence_scores as conf_interval


# Catch Models
models = load_models.utils_model()


def predict(img_file):

    bytes_data = img_file.getvalue()
    target_size = (180, 180)

    # Process Image
    img = Image.open(io.BytesIO(bytes_data))
    img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)

    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch\

    # ================
    classes = list()
    probabilities = list()

    # Model names
    model_names = ['M_A', 'M_B', 'M_C']

    # Loop through all model names
    for model_name in model_names:
        # Make Prediction
        predictions = models[model_name].predict(img_array)
        score = tf.nn.softmax(predictions[0])  # Score Model
        class_names = ["Black", "White"]

        # Predicted Class
        class_ = class_names[np.argmax(score)]
        #
        class_names = ["Black", "White"]

        # Predicted Class
        class_ = class_names[np.argmax(score)]
        # Accuracy Score
        probability = (100 * np.max(score))

        classes.append(class_)
        probabilities.append(probability)

    return {
        "Models": ["Model A", "Model B", "Model C"],
        "Class": classes,
        "Probability": probabilities
    }


def app():
    # Headers
    components.html(
        """
        <font face = "courier" size = "5" color = "#000000" style="text-align:center;">
            BIAS IN FACIAL RECOGNITION
        </font>
        <br>
        <br>
        <font face = "courier" size = "2" color = "#000000">
            As AI is getting democratized, it's important to learn about how biased algorithms can be become. If
            you're building Facial-Recognition technology, you can use this system to test how different ms fair with varying representations of data.
         </font>
        """
    )

    uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        st.write("Classifying...")

        results = predict(img_file=uploaded_file)

        conf_interval.app(results=results)
