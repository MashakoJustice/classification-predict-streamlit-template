# Streamlit dependencies
import streamlit as st
import joblib
import os

# Data dependencies
import pandas as pd

# Vectorizer
news_vectorizer = open("resources/tfidfvect.pkl", "rb")
tweet_cv = joblib.load(news_vectorizer)  # loading your vectorizer from the pkl file

# Load your raw data
raw = pd.read_csv("https://raw.githubusercontent.com/MashakoJustice/Documentatio/main/Classification/train.csv")

# Set custom Streamlit page configuration
st.set_page_config(
    page_title="Green Data Dynamics",
    page_icon=":seedling:",  # You can use emojis as icons
    layout="centered",  # "wide" for a wider layout
    initial_sidebar_state="auto",  # "expanded" or "collapsed"
)

# The main function where we will build the actual app
def main():
    """Tweet Classifier App with Streamlit """
    # Create a layout with two columns
    col1, col2 = st.columns([1, 3])

    # Display logo in the first column
    col1.image("https://cdn.discordapp.com/attachments/1168555810721382481/1181147881302937641/Green_Data_Dynamics_smaller.png?ex=658000af&is=656d8baf&hm=29e6071e4e2510f83dbbe910ab837534bae9a843248f9e3ad603eb41413a5715&", width=100)

    # Display company name in the second column with green color
    col2.markdown("<h1 style='color: green;'>Green Data Dynamics</h1>", unsafe_allow_html=True)
    col2.write("A Greener Tomorrow")

    st.subheader("Climate Change Tweet Classification")

    # Building out the "Information" page
    st.info("General Information")
    # You can read a markdown file from supporting resources folder
    st.markdown("Some information here")

    st.subheader("Raw Twitter data and label")
    if st.checkbox('Show raw data'):  # data is hidden if the box is unchecked
        st.write(raw[['sentiment', 'message']])  # will write the df to the page

    # You can add more sections or functionality here

# Required to let Streamlit instantiate our web app.
if __name__ == '__main__':
    main()
