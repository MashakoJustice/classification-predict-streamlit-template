# about_app.py
import streamlit as st
from shared_layout import add_sidebar_image

# Set custom Streamlit page configuration
st.set_page_config(
    page_title="Green Data Dynamics",
    page_icon=":seedling:",
    layout="wide",
    initial_sidebar_state="auto"
)

# Main content
add_sidebar_image()

def display_about_page(company_name, app_name, company_description):
    st.header("About Us")

    # Display the company logo and information
    st.image("https://cdn.discordapp.com/attachments/1168555810721382481/1181147881302937641/Green_Data_Dynamics_smaller.png?ex=658000af&is=656d8baf&hm=29e6071e4e2510f83dbbe910ab837534bae9a843248f9e3ad603eb41413a5715&", width=200)
    st.write(company_description.format(app_name))

def main():
    # Company information
    company_name = "Green Data Dynamics"
    
    # App information
    app_name = "Climate Change Awareness App"
    
    company_description = (
        "As a dedicated non-governmental organization committed to addressing global warming issues, our mission is twofold. "
        "Firstly, we aim to amplify environmental awareness and advocate for sustainable practices. To achieve this, we've developed an "
        "innovative app, the **{0}**, utilizing advanced machine learning to analyze social media conversations and classify individual beliefs on climate change. "
        "Recognizing the growing trend of companies focusing on lessening their environmental impact, our app provides businesses with insights into "
        "consumer sentiments, spanning various demographics and geographic categories. We have created an app that helps classify sentiments on climate change, "
        "and companies can utilize this app to understand individual sentiments on global warming. This enables them to tailor marketing strategies based on "
        "the sentiments of their target audience, contributing to more effective and targeted outreach campaigns."
    )

    # Display the About page
    display_about_page(company_name, app_name, company_description)

if __name__ == "__main__":
    main()
