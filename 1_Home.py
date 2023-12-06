import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
import re
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from shared_layout import add_sidebar_image

# Sample data (replace with your actual data)
train_df = pd.read_csv("https://raw.githubusercontent.com/MashakoJustice/Documentatio/main/Classification/train.csv")

# Set custom Streamlit page configuration
st.set_page_config(
    page_title="Green Data Dynamics",
    page_icon=":seedling:",  # You can use emojis as icons
    layout="wide",  # Use "wide" for a wider layout
    initial_sidebar_state="auto",  # "expanded" or "collapsed"
)

# Main content
add_sidebar_image()

# Function to remove URLs, convert to lowercase, remove punctuation, and remove numbers
all_stop = set(stopwords.words('english'))
def tweet_cleaning(tweet):
    def clean_text(tweet):
        text_no_urls = re.sub(r'https?://\S+|www\.\S+', '', str(tweet))
        text_lower = text_no_urls.lower()
        text_cleaned = ''.join([char for char in text_lower if char not in string.punctuation + '0123456789'])
        return text_cleaned

    def clean_stopwords(tweet):
        tweet_list = [ele for ele in tweet.split()]
        # Remove "rt" from the list of tokens
        clean_tokens = [t for t in tweet_list if re.match(r'https?:\/\/.*[\r\n]*', t) or t.lower() != 'rt']
        clean_s = ' '.join(clean_tokens)
        clean_mess = [word for word in clean_s.split() if word not in all_stop]
        return clean_mess

    def lemmaiser(tweet_list):
        lem = WordNetLemmatizer()
        normalized_tweet = [lem.lemmatize(word, 'v') for word in tweet_list]
        return normalized_tweet

    new_tweet = clean_text(tweet)
    no_punc_tweet = clean_stopwords(new_tweet)
    lemmatized_tweet = lemmaiser(no_punc_tweet)

    return lemmatized_tweet


# Check the actual column names in your CSV file
# If 'sentiment' doesn't exist, replace it with the correct column name
sentiment_column_name = 'sentiment'
text_column_name = 'message'

# Replace numeric sentiments with their labels
train_df[sentiment_column_name] = train_df[sentiment_column_name].map({-1: 'Anti', 0: 'Neutral', 1: 'Pro', 2: 'News'})

# Initialize wordcloud_data for each sentiment
wordcloud_data = {sentiment: "" for sentiment in train_df[sentiment_column_name].unique()}

# Fill wordcloud_data based on sentiment column
for sentiment in wordcloud_data.keys():
    text_data = " ".join(train_df[train_df[sentiment_column_name] == sentiment][text_column_name])
    cleaned_text_data = " ".join(tweet_cleaning(text_data))
    wordcloud_data[sentiment] = cleaned_text_data

# Get the absolute path to the directory of the script
script_directory = os.path.dirname(os.path.abspath(__file__))

col1, col2, col3 = st.columns([1, 3, 1])  # Adjust the ratio as needed

# App logo using the absolute path
logo_path = "https://cdn.discordapp.com/attachments/1168555810721382481/1181147881302937641/Green_Data_Dynamics_smaller.png?ex=658000af&is=656d8baf&hm=29e6071e4e2510f83dbbe910ab837534bae9a843248f9e3ad603eb41413a5715&width=200"
col1.image(logo_path, caption="A Greener Tomorrow", width=150)  # Adjust the width as needed

# Title and Subtitle
col2.title("Climate Change Awareness App")
col2.text("Let's Predict")  # Subtitle

# Welcome message or introduction
st.header("You are either part of the solution, or you're going to be part of the problem.")
st.write("Eldridge Cleaver - 1968")

# User Interface Elements
st.subheader("Key Words For Climate Change Sentiment")

# Buttons for each sentiment
selected_sentiment = st.radio("Select Sentiment:", list(wordcloud_data.keys()))

# Button to trigger sentiment-specific word cloud
if st.button(f"Show {selected_sentiment} Word Cloud"):
    # Display the sentiment-specific word cloud
    st.subheader(f"{selected_sentiment} Word Cloud Visualization")
    wordcloud_data_selected = wordcloud_data.get(selected_sentiment, "")

    # Check if there are words for the selected sentiment
    if wordcloud_data_selected:
        # Create and display the word cloud
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(wordcloud_data_selected)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        st.pyplot(plt)
    else:
        st.write(f"No data available for the '{selected_sentiment}' sentiment.")

# Add YouTube links to the home page
st.subheader("Watch And Learn, Change Your Perspective")
st.write("Check out our videos:")

# YouTube links on the left
st.subheader("Watch And Learn, Change Your Perspective")
st.write("Check out our videos:")
st.markdown("[The reality of climate change | David Puttnam | TEDxDublin](https://www.youtube.com/watch?v=SBjtO-0tbKU&t=145s)")
st.markdown("[Why I don't care about 'Climate Change' | David Saddington | TEDxTeen](https://www.youtube.com/watch?v=7vnzKPq390Q)")
st.markdown("[A Creative Approach To Climate Change | Finnegan Harries | TEDxTeen](https://www.youtube.com/watch?v=lIJOmd-sF-c)")
st.markdown("[Why renewables can’t save the planet | Michael Shellenberger | TEDxDanubia](https://www.youtube.com/watch?v=N-yALPEpV4w)")
st.markdown("[Climate Change Impact on Developing Countries | Linda Bouadjel-Zebian | TEDxLosGatosHighSchool](https://www.youtube.com/watch?v=EaA6WjARS9o)")
st.markdown("[A simple and smart way to fix climate change | Dan Miller | TEDxOrangeCoast](https://www.youtube.com/watch?v=0k2-SzlDGko)")
st.markdown("[Climate Expert Says Man-Made Climate Change Narrative Is A LIE, Just A Scheme To Make Money](https://www.youtube.com/watch?v=CFlogpQRHfQ)")

