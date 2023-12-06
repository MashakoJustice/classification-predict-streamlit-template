import streamlit as st

def add_sidebar_image():
    # Image link
    sidebar_image_path = "https://cdn.discordapp.com/attachments/1139658394798674051/1181971104353505420/Twitter-FeatureArt-1024x536.jpg?ex=6582ff5f&is=65708a5f&hm=7831677b4f2c7d5bdcacadd7e6f21fcb300ea55e4cd0294026edf01920872340&"

    # Display the image in the sidebar
    st.sidebar.image(sidebar_image_path)
