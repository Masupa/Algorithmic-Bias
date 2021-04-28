import io
import keras
import numpy as np
import streamlit as st
import tensorflow as tf
import PIL.Image as Image
import utils.load_models as load_models
import streamlit.components.v1 as components
import utils.classifiers as classifiers
import utils.visualization as viz

# Catch Models
models = load_models.utils_model()


def app():

    class_type = ""

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

    uploaded_files = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

    # Buttons
    col1, col2, col3 = st.beta_columns([1.5, 1, 1.5])
    with col1:
        pass
    with col2:
        btn = st.button("PROCESS IMAGES")
    with col3:
        pass

    st.write("")
    st.write("")
    st.write("")
    st.write("")

    if btn:
        if uploaded_files is not None:
            img1, img2, img3, img4 = st.beta_columns(4)
            cols = [img1, img2, img3, img4]
            for i in range(4):
                print(i)
                with cols[i]:
                    img = Image.open(uploaded_files[i])
                    st.image(img, width=100, caption=uploaded_files[i].name)

                # Score Images
                accuracy_scores = classifiers.classify_images(img_file=uploaded_files)

                # Visualize Canvas
                viz.visual_canvas(accuracy_scores)
