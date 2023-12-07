# privacy_policy.py
import streamlit as st
from shared_layout import add_sidebar_image

# Set custom Streamlit page configuration
st.set_page_config(
    page_title="Privacy Policy",
    page_icon=":lock:",
    layout="wide",
    initial_sidebar_state="auto"
)

# Main content
add_sidebar_image()

def display_privacy_policy(company_name, app_name, logo_url):
    st.header("Privacy Policy")

    st.image(logo_url, width=200)

    st.write(f"Last Updated: January 1, 2023\n\n")

    st.markdown(
        f"Welcome to {company_name}'s {app_name} (the 'App'). This Privacy Policy outlines the types of personal information we collect, how it is used, and your choices regarding your information. By using the App, you agree to the terms of this Privacy Policy.")

    st.subheader("1. Information We Collect")

    st.markdown("We may collect and process the following types of personal information:")
    st.markdown("- Information you provide voluntarily, such as when you use the app, contact us, or participate in surveys.")
    st.markdown("- Automatically collected information, including usage details, IP addresses, and device information.")

    st.subheader("2. How We Use Your Information")

    st.markdown("We use the information we collect for various purposes, including:")
    st.markdown("- Providing, maintaining, and improving the App.")
    st.markdown("- Understanding and analyzing user preferences.")
    st.markdown("- Responding to user inquiries and providing customer support.")

    st.subheader("3. Information Sharing and Disclosure")

    st.markdown("We may share your information with third parties under certain circumstances, such as:")
    st.markdown("- With your consent.")
    st.markdown("- To comply with legal obligations.")
    st.markdown("- To protect our rights, privacy, safety, or property.")

    st.subheader("4. Security")

    st.markdown("We take reasonable measures to protect your information from unauthorized access or disclosure.")

    st.subheader("5. Your Choices")

    st.markdown("You can make choices about the collection and use of your information.")
    st.markdown("- You may choose not to provide certain information.")
    st.markdown("- You can set your browser to refuse all or some browser cookies.")

    st.subheader("6. Contact Us")

    st.markdown(f"For questions or concerns regarding this Privacy Policy, please contact us at [Contacts](http://localhost:8501/Contacts).")

def main():
    # Company information
    company_name = "Green Data Dynamics"
    
    # App information
    app_name = "Climate Change Awareness App"
    
    # Image URL for the logo
    logo_url = "https://cdn.discordapp.com/attachments/1168555810721382481/1181147881302937641/Green_Data_Dynamics_smaller.png?ex=658000af&is=656d8baf&hm=29e6071e4e2510f83dbbe910ab837534bae9a843248f9e3ad603eb41413a5715&"

    # Display the Privacy Policy page
    display_privacy_policy(company_name, app_name, logo_url)

if __name__ == "__main__":
    main()
