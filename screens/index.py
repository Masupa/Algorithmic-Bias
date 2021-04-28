import streamlit as st
import streamlit.components.v1 as components
import utils.load_models as models


update_models = None


def app():

    global update_models

    # Page Loader
    current_ui = "Upload Models"

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

    st.text("")
    st.image('./assets/facial_recognition.jpeg')

    if update_models is None:
        # Process Models BTN
        col1, col2, col3 = st.beta_columns([1.5, 1, 1.5])
        with col1:
            pass
        with col2:
            btn = st.button("UPLOAD MODELS")
            if btn:
                update_models = "Upload Models"
        with col3:
            pass

    elif update_models == "Upload Models":
        # Upload Models
        model_a = st.file_uploader("Upload Model A")
        model_b = st.file_uploader("Upload Model B")
        model_c = st.file_uploader("Upload Model C")

        # Process Models BTN
        col1, col2, col3 = st.beta_columns([1.5, 1, 1.5])
        with col1:
            pass
        with col2:
            processed_models = st.button("PROCESS MODELS")
            if processed_models:
                update_models = "Disappear"
        with col3:
            pass

        if processed_models and model_c is not None:
            models.load_model(model_a=model_a, model_b=model_b, model_c=model_c)

    elif update_models == "Disappear":
        st.markdown("")
        components.html(
            """
            <font face = "courier" size = "5" color = "#000000" style="text-align:center;">
                MODELS UPLOADED - PROCEED TO CLASSIFICATION
            </font>
            """
        )
