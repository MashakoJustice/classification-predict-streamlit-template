import streamlit as st

def add_sidebar_image():
    sidebar_image_path = "path/to/your/image.png"
    st.sidebar.image(sidebar_image_path, use_container_width=True)