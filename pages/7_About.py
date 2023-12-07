# about_app.py
import streamlit as st
from shared_layout import add_sidebar_image

# Set custom Streamlit page configuration
st.set_page_config(
    page_title="About",
    page_icon=":seedling:",
    layout="wide",
    initial_sidebar_state="auto"
)

# Main content
add_sidebar_image()

def display_about_page(company_name, app_name, company_description, image_url):
    st.header("About Us")
    st.subheader("Green Data Dynamics")

    # Create a layout with two columns
    col1, col2 = st.columns([1, 1])

    # Display the company logo in the first column
    col1.image("https://cdn.discordapp.com/attachments/1168555810721382481/1181147881302937641/Green_Data_Dynamics_smaller.png?ex=658000af&is=656d8baf&hm=29e6071e4e2510f83dbbe910ab837534bae9a843248f9e3ad603eb41413a5715&", width=200)

    # Display the company information in the second column
    col2.image(image_url, width=400)  # Add the new image on the right side

    # About the app information
    st.write(company_description.format(app_name))

    # Additional information with bullet points
    st.subheader("Advantages of Using Our App")
    st.markdown("- Gain insights into public sentiments on climate change.")
    st.markdown("- Classify and understand diverse opinions from social media.")
    st.markdown("- Tailor marketing strategies based on sentiment analysis.")
    st.markdown("- Contribute to effective and targeted environmental awareness campaigns.")

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

    # Image URL for the image on the right side
    image_url = "https://cdn.discordapp.com/attachments/1176191997564964914/1182332953653694616/download.jpeg?ex=6584505e&is=6571db5e&hm=c4b8a7b4078b67523ba2f76dcfc33f7c35e88c413662975d1c92cdf577b607e8&"

    # Display the About page
    display_about_page(company_name, app_name, company_description, image_url)

if __name__ == "__main__":
    main()
