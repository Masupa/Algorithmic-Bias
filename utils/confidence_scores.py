import numpy as np
import streamlit as st


def app(results):

    # Columns
    col1, col2, col3 = st.beta_columns([0.5, 1, 0.5])
    with col1:
        pass
    with col2:
        st.dataframe(results)
    with col3:
        pass

    st.header("")

    st.write("Model A")
    st.write("Predicted Class: {}".format(results['Class'][0]))
    st.slider("Confidence Interval", value=int((np.max(results['Probability'][0]))), min_value=0, max_value=100)

    st.write("___")
    st.write("Model B")
    st.write("Predicted Class: {}".format(results['Class'][1]))
    st.slider("Confidence Interval", value=int((np.max(results['Probability'][1]))), min_value=0, max_value=100)

    st.write("___")
    st.write("Model C")
    st.write("Predicted Class: {}".format(results['Class'][2]))
    st.slider("Confidence Interval", value=int((np.max(results['Probability'][2]))), min_value=0, max_value=100)
