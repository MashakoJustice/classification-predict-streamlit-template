# contacts_app.py

import streamlit as st
from shared_layout import add_sidebar_image

# Set custom Streamlit page configuration
st.set_page_config(
    page_title="Green Data Dynamics",
    page_icon=":seedling:",  # You can use emojis as icons
    layout="wide",  # Use "wide" for a wider layout
    initial_sidebar_state="auto",  # "expanded" or "collapsed"
)

# Main content
add_sidebar_image()

def display_contacts(company_address, company_phone, project_managers, project_team, location_url):
    st.header("Contacts Page")

    # Define a layout with two columns
    col1, col2= st.columns([1, 2])

    # Column 1: Display the company logo
    with col1:
        st.image("https://cdn.discordapp.com/attachments/1168555810721382481/1181147881302937641/Green_Data_Dynamics_smaller.png?ex=658000af&is=656d8baf&hm=29e6071e4e2510f83dbbe910ab837534bae9a843248f9e3ad603eb41413a5715&", width=200)
        st.image("https://cdn.discordapp.com/attachments/1176191997564964914/1181962948906860554/Protect_Earth_-_Blue_Green_Words_for_Earth__Sticker_for_Sale_by_jitterfly.jpeg?ex=6582f7c6&is=657082c6&hm=154ede3e7116b512ebbe3b003010c33f17f367239f4ec2b6eee939d5a785cadb&", width=200)# Replace with the actual path to your second logo

    # Column 2: Display contacstt details
    with col2:
        # Display a paragraph about the company
        st.write(
            "Welcome to our contacts page! Here, you can find information about our company, project managers, "
            "and individuals working on the project. Feel free to explore the details below."
        )

        # Display company address and phone
        st.subheader("Company Information:")
        st.write(f"Address: {company_address}")
        st.write(f"Phone: {company_phone}")
        
        # Display pin drop as a clickable link
        st.subheader("Pin Drop:")
        st.markdown(f"[{company_address}]({location_url})")

        # Display project managers
        st.subheader("Project Managers:")
        for manager in project_managers:
            name, email = manager.split(", ")
            st.write(f"- [{name}](mailto:{email})")

        # Display individuals working on the project with email links
        st.subheader("Project Team:")
        for team_member in project_team:
            name, email = team_member.split(", ")
            st.write(f"- [{name}](mailto:{email})")

def main():
    # Company information
    company_address = "18-20 Brakfontein Rd, The Reeds, Centurion, 0061"
    company_phone = "+234 806 785 8177"

    # Project managers
    project_managers = ["Mashako Manyelo, manelojustice@gmail.com",
                        "Boitumelo Lefophana, boitumelolefophana@gmail.com"]

    # Individuals working on the project with email addresses
    project_team = [
        "Prince Maponyane, kala33prince@gmail.com",
        "Shedrack Efienokwu, shedrackebele@yahoo.com",
        "Mutondi Tshivhase, tmutondi@gmail.com",
        "Janet Adeoye, adeoyejanet88@gmail.com"
    ]

    # Pin drop URL
    location_url = "https://maps.app.goo.gl/R8C4vR8PZwnsz3eA6"

    # Display the contacts page
    display_contacts(company_address, company_phone, project_managers, project_team, location_url)

if __name__ == "__main__":
    main()
