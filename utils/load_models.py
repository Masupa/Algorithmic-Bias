import os
import streamlit as st
import keras.models as models


m_a_ = None
m_b_ = None
m_c_ = None


def utils_model():
    m_a_dir = "/Users/turikumwe/Desktop/Capstone/New_App/ms/balanced_model.h5"
    m_b_dir = "/Users/turikumwe/Desktop/Capstone/New_App/ms/biased_black_model.h5"
    m_c_dir = "/Users/turikumwe/Desktop/Capstone/New_App/ms/biased_white_model.h5"

    global m_a_
    global m_b_
    global m_c_

    m_a_ = models.load_model(m_a_dir)
    m_b_ = models.load_model(m_b_dir)
    m_c_ = models.load_model(m_c_dir)

    return {
        "M_A": m_a_,
        "M_B": m_b_,
        "M_C": m_c_
    }


def load_model(model_a, model_b, model_c):
    """
    :param model_a: Model A
    :param model_b: Model B
    :param model_c: Model C
    :return: All Models
    """

    # model_a = models.load_model(model_a.get_value())
    # model_b = models.load_model(model_b.get_value())
    # model_c = models.load_model(model_c.get_value())

    # Models
    utils_model()

    # return model_a, model_b, model_c
