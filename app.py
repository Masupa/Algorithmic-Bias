import streamlit as st
import screens.index as home
import screens.image_cls as cls
import screens.multi_cls as multi_cls


def main():

    pages = {
        "Home": home,
        "Image Classifier": cls,
        "Multi-Image Classifier": multi_cls
    }

    st.sidebar.title('NAVIGATION BAR')
    selection = st.sidebar.radio("Go to...", list(pages.keys()))
    page = pages[selection]
    page.app()


if __name__ == '__main__':
    main()
