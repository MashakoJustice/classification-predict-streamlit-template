# contacts_app.py

import streamlit as st

def display_contacts(company_address, company_phone, project_managers, project_team, location_url):
    st.header("Contacts Page")

    # Define a layout with two columns
    col1, col2= st.columns([1, 2])

    # Column 1: Display the company logo
    with col1:
        st.image("https://cdn.discordapp.com/attachments/1168555810721382481/1181147881302937641/Green_Data_Dynamics_smaller.png?ex=658000af&is=656d8baf&hm=29e6071e4e2510f83dbbe910ab837534bae9a843248f9e3ad603eb41413a5715&", width=200)
        st.image("https://cdn.discordapp.com/attachments/1176191997564964914/1180809226461917255/fcb84b01-106a-45ee-897e-bd5a82a4fd83.jpeg?ex=657ec549&is=656c5049&hm=897858b9358bd7c006d92f4b84f45f698fbbb7cd42289d6658f1ceb432c2c897&", width=200) 
        st.image("https://cdn.discordapp.com/attachments/1176191997564964914/1181162470707052574/Signature_Pad_Sigma.jpeg?ex=65800e45&is=656d9945&hm=d93ff2125f811fc1a6fabf13a8b11330687865c97774bca60855a78cca49c68c&", width=200)# Replace with the actual path to your second logo

    # Column 2: Display contact details
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
