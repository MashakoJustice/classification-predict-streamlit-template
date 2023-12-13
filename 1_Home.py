import streamlit as st
import pandas as pd
import os
from shared_layout import add_sidebar_image

# Sample data (replace with your actual data)
train_df = pd.read_csv("https://raw.githubusercontent.com/MashakoJustice/Documentatio/main/Classification/train.csv")

# Set custom Streamlit page configuration
st.set_page_config(
    page_title="Green Data Dynamics Home",
    page_icon=":seedling:",  # You can use emojis as icons
    layout="wide",  # Use "wide" for a wider layout
    initial_sidebar_state="auto",  # "expanded" or "collapsed"
)

# Main content
add_sidebar_image()

col1, col2, col3 = st.columns([1, 3, 1])  # Adjust the ratio as needed

# App logo using the absolute path
logo_path = "https://cdn.discordapp.com/attachments/1168555810721382481/1181147881302937641/Green_Data_Dynamics_smaller.png?ex=658000af&is=656d8baf&hm=29e6071e4e2510f83dbbe910ab837534bae9a843248f9e3ad603eb41413a5715&width=200"
col1.image(logo_path, caption="Klima-Tact", width=150)  # Adjust the width as needed

# Title and Subtitle
col2.title("Climate Change Awareness App")
col2.text("Let's Predict")  # Subtitle

# Welcome message or introduction
st.header("You are either part of the solution, or you're going to be part of the problem.")
st.write("Eldridge Cleaver - 1968")

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

# Adding a message about contacting for more questions
st.subheader("For More Information, See Next Page.")
Information_link = "[Information Page](http://localhost:8501/Information)"  # Replace with the actual URL of your contacts page
st.markdown(f"What Is This App About {Information_link} Find Out.")

# Required to let Streamlit instantiate our web app.
if __name__ == '__main__':
    st.write("App is running.")
