# Import Packages
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

sns.set_style("whitegrid")


def visual_compared_models(data):
    """
    :param data: DataFrame containing accuracy results of all models used on an image
    :return: a bar_plot visualizing the accuracy scores
    """

    fig, ax = plt.subplots()

    # Barplot
    ax = sns.barplot(data=data, x="Model Type", y="Accuracy Score",
                    facecolor=(1, 0.5, 0.5, 0),
                    errcolor=".2",
                    edgecolor=".2")

    # Visual Attributes
    plt.title("Model Probability", fontdict={'fontsize': 12})
    plt.xlabel("Model Type")
    plt.ylabel("Probability (%)")
    plt.xticks(rotation='vertical')

    # Visual Features
    plt.ylim((0, 100))

    # Plot Figure
    st.pyplot(fig=fig, width=10)


def visual_canvas(inputs):
    """
    :param inputs: Dictionary - Keys (Models) & Values (Scores)
    :return: Lineplot with three lines representing the scores
    """

    st.subheader("")
    st.write("_________________________________________________")

    st.text("Probability Summaries ~ Plots")

    # Line Plots
    line_plot(inputs=inputs)

    # Box Plots
    box_plot(inputs=inputs)

    # Bar Plots
    plot_stats(inputs=inputs)


# TODO: Adjust rbg values to find similar ones
# Refactor visual attributes
# Add legend to differentiate the two
def plot_stats(inputs):
    """
    :param inputs: Dictionary - Keys (Models) & Values (Scores)
    :return: Lineplot with three lines representing the scores
    """

    # Data ~ Images
    stats_data = pd.DataFrame(inputs).mean()

    # Data ~ Modules
    models_data = pd.DataFrame({
        'Model C': 86,
        'Model A': 78,
        'Model B': 84
    }, index=[0])

    fig, ax = plt.subplots(sharey=True)

    col1, col2 = st.beta_columns(2)
    with col1:
        sns.barplot(x=stats_data.index, y=stats_data.values,
                    facecolor=(0.4, 0.7, 0.4, 0),
                    errcolor=".2",
                    edgecolor=".2")

        # Visual Attributes
        plt.title("MEAN PROBABILITY PER MODEL ON IMAGES", fontdict={'fontsize': 12})
        plt.xlabel("Model Type")
        plt.ylabel("Probability (%)")

        plt.xticks(rotation='vertical')

        # Visual Features
        plt.ylim((0, 100))

    with col2:
        sns.barplot(x=models_data.columns, y=models_data.values[0],
                    facecolor=(1, 0.5, 0.5, 0),
                    errcolor=".2",
                    edgecolor=".2")

        # Visual Attributes
        plt.title("MEAN PROBABILITY PER MODEL ON IMAGES", fontdict={'fontsize': 12})
        plt.xlabel("Model Type")
        plt.ylabel("Probability (%)")

        plt.xticks(rotation='vertical')

        # Visual Features
        plt.ylim((0, 100))

    st.pyplot(fig=fig, figsize=(2, 2))


def line_plot(inputs):
    """
    :param inputs: Dictionary - Keys (Models) & Values (Scores)
    :return: Lineplot with three lines representing the scores
    """

    fig, ax = plt.subplots(figsize=(6, 4))

    # Line_plots
    ax = sns.lineplot(x=range(1, len(inputs['M_B']) + 1), y=inputs['M_B'], label='Model B - Biased towards black', linestyle='--', linewidth=0.75)
    ax = sns.lineplot(x=range(1, len(inputs['M_B']) + 1), y=inputs['M_C'], label='Model C - Biased towards white', linestyle='--', linewidth=0.75)
    ax = sns.lineplot(x=range(1, len(inputs['M_B']) + 1), y=inputs['M_A'], label='Model A - Balanced model', linestyle='--', linewidth=0.75)

    # Visual Features
    plt.ylim((0, 100))
    # plt.grid(linestyle='--')
    ax.grid(True, linestyle='--', linewidth=0.5)

    # Visual Attributes
    plt.title("PROBABILITY SCORES PER MODEL ON MULTIPLE IMAGES", fontdict={'fontsize': 12})
    plt.xlabel("Images ~ Each point represents an image")
    plt.ylabel("Probability (%)")

    # Display Chart
    st.pyplot(fig=fig, figsize=(6, 4))


def box_plot(inputs):
    """
    :param inputs: Dictionary - Keys (Models) & Values (Scores)
    :return:  Box_plot with two lines representing the scores
    """

    fig, ax = plt.subplots(figsize=(6, 4))

    # Boxplots
    ax = plt.boxplot([inputs['M_B'], inputs['M_C'], inputs['M_A']],
                     labels=['Model B', 'Model C', 'Model A'])

    # Visual Features
    plt.ylim((0, 100))
    # plt.grid(linestyle='--')
    plt.grid(True, linestyle='--', linewidth=0.5)

    # Visual Attributes
    plt.title("PROBABILITY MEASURE OF SPREAD PER MODEL", fontdict={'fontsize': 12})
    plt.xlabel("Model Type")
    plt.ylabel("Probability (%)")

    # Display Chart
    st.pyplot(fig=fig)
