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
    page_title="FAQ",
    page_icon=":seedling:",  # You can use emojis as icons
    layout="wide",  # Use "wide" for a wider layout
    initial_sidebar_state="auto",  # "expanded" or "collapsed"
)

# Main content
add_sidebar_image()

# Create a layout with two columns
col1, col2 = st.columns([1, 3])

# Display logo in the first column
col1.image("https://cdn.discordapp.com/attachments/1168555810721382481/1181147881302937641/Green_Data_Dynamics_smaller.png?ex=658000af&is=656d8baf&hm=29e6071e4e2510f83dbbe910ab837534bae9a843248f9e3ad603eb41413a5715&", width=100)

# Display company name in the second column with green color
col2.markdown("<h1 style='color: green;'>Green Data Dynamics</h1>", unsafe_allow_html=True)
col2.write("A Greener Tomorrow")

st.subheader("Climate Change Tweet Classification")

# Building out the "Information" page
st.info("'The Earth does not belong to us: we belong to the Earth.' - Marlee Matlin")
# You can read a markdown file from supporting resources folder
st.markdown("Climate change, characterized by shifts in Earth's climate patterns, is a topic of extensive scientific research and observation. The rise in global temperatures, alterations in precipitation patterns, and the increase in extreme weather events are widely attributed to human activities, particularly the emission of greenhouse gases. However, some individuals may still question the validity of global warming. In the face of compelling evidence, including temperature records, glacial melt, and changes in ecosystems, a lingering question persists: Is there genuine doubt about the reality of global warming, or is it crucial for society to collectively acknowledge and address the scientific consensus on the urgent need for climate action? This app helps us find out if one believes in the theory of climate change or not using information given to us from Twitter, see information below.")
    
# Adding FAQ section
st.subheader("Frequently Asked Questions (FAQ)")

# FAQ 1
st.markdown("#### Q: What is the purpose of this app?")
st.markdown("A: This app, named **Green Data Dynamics**, aims to classify tweets related to climate change based on sentiment. It helps users understand public opinions on climate change through data sourced from Twitter.")

# FAQ 2
st.markdown("#### Q: How is the data processed before classification?")
st.markdown("A: The data undergoes a cleaning process, including removing URLs, converting characters to lowercase, eliminating stop words, and lemmatizing words. Various methods like CountVectorizer and n-grams are used for data cleaning.")

# FAQ 3
st.markdown("#### Q: What do the sentiment labels represent?")
st.markdown("A: Sentiment labels indicate the stance of a tweet regarding climate change. Labels include 2 (News: factual news about climate change), 1 (Pro: supports man-made climate change), 0 (Neutral: neither supports nor refutes), and -1 (Anti: does not believe in man-made climate change).")

# FAQ 4
st.markdown("#### Q: Can I see the raw Twitter data used for classification?")
st.markdown("A: Yes, you can explore the raw Twitter data by checking the 'Show raw data' checkbox. It displays columns with sentiment labels and corresponding messages.")

# FAQ 5
st.markdown("#### Q: How accurate is the sentiment classification?")
st.markdown("A: The accuracy of sentiment classification is influenced by the quality and diversity of the training data. The model is trained on labeled data, and its performance is subject to the variability of Twitter language.")

# FAQ 6
st.markdown("#### Q: Can I use this app to analyze my own Twitter data?")
st.markdown("A: Currently, the app is designed to analyze pre-collected Twitter data. Extending it to analyze individual Twitter accounts or custom datasets requires further development and customization.")

# Adding a message about contacting for more questions
st.subheader("For More Questions, See Our Contact Page. We Would Like To Hear From You.")
contact_link = "[Contact Page](http://localhost:8501/Contacts)"  # Replace with the actual URL of your contacts page
st.markdown(f"Feel free to reach out to us on our {contact_link} for any additional questions or inquiries.")

# Required to let Streamlit instantiate our web app.
if __name__ == '__main__':
    st.write("App is running.")