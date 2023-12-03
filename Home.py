"""

    Simple Streamlit webserver application for serving developed classification
	models.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within this directory for guidance on how to use this script
    correctly.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend the functionality of this script
	as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
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


# Add custom HTML and CSS for background image
st.markdown(
    """
    <style>
        body {
            background-image: url('https://cdn.discordapp.com/attachments/1176191997564964914/1180655124880834560/Stills_Christian_A__Schaffer.jpeg?ex=657e35c5&is=656bc0c5&hm=b7b3334cc6feb552bcb97bb5c345d8d15c01fb9828a2aaec06be04393d1c2483&');
            background-size: cover;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# The main function where we will build the actual app
def main():
    """Tweet Classifier App with Streamlit """
    # Create a layout with two columns
    col1, col2 = st.columns([1, 3])

    # Display logo in the first column
    col1.image("https://cdn.discordapp.com/attachments/1176191997564964914/1180646243156897854/Untitled_design.png?ex=657e2d7f&is=656bb87f&hm=94277fe06fd3d9eb44ffbd9ba13585719999593ae6b2144500300ff89037307c&", width=100)

    # Display company name in the second column with green color
    col2.markdown("<h1 style='color: green;'>Green Data Dynamics</h1>", unsafe_allow_html=True)
    col2.write("This app allows you to predict the sentiment of a given text using machine learning models.")

    st.subheader("Climate Change Tweet Classification")

    # Creating sidebar with selection box -
    # you can create multiple pages this way
    options = ["Prediction", "Information"]
    selection = st.sidebar.selectbox("Choose Option", options)

    if selection == "Home":
        Home()
    
    # Building out the "Information" page
    elif selection == "Information":
        st.info("General Information")
        # You can read a markdown file from supporting resources folder
        st.markdown("Some information here")

        st.subheader("Raw Twitter data and label")
        if st.checkbox('Show raw data'):  # data is hidden if the box is unchecked
            st.write(raw[['sentiment', 'message']])  # will write the df to the page

    # Building out the prediction page
    elif selection == "Prediction":
        st.info("Prediction with ML Models")
        # Creating a text box for user input
        tweet_text = st.text_area("Enter Text", "")

        if st.button("Submit"):
            # Transforming user input with vectorizer
            vect_text = tweet_cv.transform([tweet_text]).toarray()
            # Load your .pkl file with the model of your choice + make predictions
            # Try loading in multiple models to give the user a choice
            predictor = joblib.load(open(os.path.join("resources/Logistic_regression.pkl"), "rb"))
            prediction = predictor.predict(vect_text)

            # When the model has successfully run, will print prediction
            # You can use a dictionary or similar structure to make this output
            # more human interpretable.
            st.success("Text Categorized as: {}".format(prediction))
            
    elif selection == "Contacts":
        contacts()

# Required to let Streamlit instantiate our web app.
if __name__ == '__main__':
    main()
