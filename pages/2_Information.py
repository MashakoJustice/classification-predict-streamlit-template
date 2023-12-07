# Streamlit dependencies
import streamlit as st
import joblib
import os
import pandas as pd
from shared_layout import add_sidebar_image

# Data dependencies
news_vectorizer = open("resources/tfidfvect.pkl", "rb")
tweet_cv = joblib.load(news_vectorizer)  # loading your vectorizer from the pkl file

# Load your raw data
raw = pd.read_csv("https://raw.githubusercontent.com/MashakoJustice/Documentatio/main/Classification/train.csv")

# Set custom Streamlit page configuration
st.set_page_config(
    page_title="Information",
    page_icon=":seedling:",  # You can use emojis as icons
    layout="wide",  # Use "wide" for a wider layout
    initial_sidebar_state="auto",  # "expanded" or "collapsed"
)

# Main content
add_sidebar_image()

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
    st.info("“Climate change is the greatest threat to our existence in our short history on this planet. Nobody's going to buy their way out of its effects.” – Mark Ruffalo")
    # You can read a markdown file from supporting resources folder
    st.markdown("Climate change, characterized by shifts in Earth's climate patterns, is a topic of extensive scientific research and observation. The rise in global temperatures, alterations in precipitation patterns, and the increase in extreme weather events are widely attributed to human activities, particularly the emission of greenhouse gases. However, some individuals may still question the validity of global warming. In the face of compelling evidence, including temperature records, glacial melt, and changes in ecosystems, a lingering question persists: Is there genuine doubt about the reality of global warming, or is it crucial for society to collectively acknowledge and address the scientific consensus on the urgent need for climate action? This app helps us find out if one believes in the theory of climate change or not using information given to us from Twitter, see information below.")

    st.subheader("Data Cleaning Process")
    st.write("Our data was sourced from Twitter, and as we went through the data, we found that it had data like:")
    st.write("e.g. RT @StarTalkRadio: First: The public understands climate change better than Congress. Why? #JohnHoldren @CoryBooker @neiltyson explain: htt…")
    st.write("This data was challenging to use without any feature engineering. As a team, we agreed to clean the data by:")
    st.write("1. Removing all URLs (e.g., http://cdn....)")
    st.write("2. Converting all characters to lowercase (e.g., A to a)")
    st.write("3. Removing stop words (e.g., 'a,' 'the,' 'is,' 'are')")
    st.write("4. Lemmatizing all remaining words (e.g., 'walk' from 'walking,' 'walks' or 'walked')")
    st.write("We utilized various methods like CountVectorizer, n-grams, etc., to clean the data, resulting in a dataset suitable for modeling.")
    st.write("See Raw Data Below")

    st.subheader("Raw Twitter data and label")
    if st.checkbox('Show raw data'):  # data is hidden if the box is unchecked
        st.write(raw[['sentiment', 'message']])  # will write the df to the page

    # You can add more sections or functionality here

# Required to let Streamlit instantiate our web app.
if __name__ == '__main__':
    main()
