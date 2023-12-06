# Streamlit dependencies
import streamlit as st
import joblib
import os

# Data dependencies
import pandas as pd

# Set custom Streamlit page configuration
st.set_page_config(
    page_title="Green Data Dynamics",
    page_icon=":seedling:",  # You can use emojis as icons
    layout="centered",  # "wide" for a wider layout
    initial_sidebar_state="auto",  # "expanded" or "collapsed"
)

# Vectorizer
news_vectorizer = open("resources/tfidfvect.pkl", "rb")
tweet_cv = joblib.load(news_vectorizer)  # loading your vectorizer from the pkl file

# The main function where we will build the actual app
def main(selection):
    """Tweet Classifier App with Streamlit """
    # Create a layout with two columns
    col1, col2 = st.columns([1, 3])

    # Display logo in the first column
    col1.image("https://cdn.discordapp.com/attachments/1168555810721382481/1181147881302937641/Green_Data_Dynamics_smaller.png?ex=658000af&is=656d8baf&hm=29e6071e4e2510f83dbbe910ab837534bae9a843248f9e3ad603eb41413a5715&", width=100)

    # Display company name in the second column with green color
    col2.markdown("<h1 style='color: green;'>Green Data Dynamics</h1>", unsafe_allow_html=True)
    col2.write("A Greener Tomorrow")

    st.subheader("Climate Change Tweet Classification")

    # Building out the prediction page
    if selection == "Prediction":
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

            # Map numeric predictions to labels and colors
            prediction_labels = {
                -1: "Anti Climate Change",
                0: "Neutral Climate Change",
                1: "Pro Climate Change",
                2: "News On Climate Change"
            }

            # Get the corresponding label from the mapping dictionary
            mapped_prediction = prediction_labels.get(prediction[0], "Unknown")

            # Display the mapped prediction result
            st.success("This Message Is: {}".format(mapped_prediction)) 

# Required to let Streamlit instantiate our web app.
if __name__ == '__main__':
    # Pass a default value for selection or get it from user input
    main("Prediction")