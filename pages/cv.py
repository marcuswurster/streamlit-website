import streamlit as st
from PIL import Image
import os

def run():
    # CV Page Template
    st.title("Curriculum Vitae")

    # Display Profile Picture in Top Right Corner
    col1, col2 = st.columns([3, 1])

    with col1:
        # Personal Information
        st.header("Personal Information")
        st.write("**Name:** Marcus Wurster")
        st.write("**Location:** Rostock, Germany")
        st.write("**LinkedIn:** [linkedin.com/in/marcuswurster](https://www.linkedin.com/in/marcuswurster/)")
        st.write("**GitHub:** [github.com/marcuswurster](https://github.com/marcuswurster)")

    with col2:
        # Load and display profile picture
        if os.path.exists("assets/profilpicture.jpg"):
            profile_pic = Image.open("assets/profilpicture.jpg")
            st.image(profile_pic, width=150)
        else:
            st.write("No profile picture found in 'assets/profile.jpg'")

    # Work Experience
    st.header("Work Experience")

    # Job 1
    st.subheader("Analytics Engineer")
    st.write("**sevDesk GmbH**")
    st.write("Offenburg, Germany")
    st.write("01.2022 - Today")
    st.write(
        """
        - Development and maintenance of scalable data pipelines for the integration, cleansing, and transformation of large datasets from various sources (dbt, SQL, Redshift, git).
        - Development and maintenance of a customized data infrastructure for the integration and synchronization of data between the data warehouse and CRM systems (Hightouch, SQL, HubSpot, Intercom).
        - Administration and maintenance of BI tools, including user management, access control, and system configurations, as well as support in the creation of analyses/dashboards (Looker, Metabase, Mixpanel).
        - Development and implementation of Python scripts to automate recurring processes such as archiving content in BI tools (Python, GitHub Actions).
        - Main point of contact for analysts and internal teams regarding data architecture, data modeling, and the use of BI tools and the data warehouse.
        """
    )

    # Job 2
    st.subheader("Working Student / Intern Customer Success Management")
    st.write("**Intershop Communications AG**")
    st.write("Jena, Germany")
    st.write("01.2021 - 12.2021")
    st.write(
        """
        - Retrieval and preparation of various data sources relevant for analysis (PowerBI).
        - Development of an automated reporting structure (PowerBI).
        - Creation and maintenance of content in the CRM tool (HubSpot).
        - Cross-departmental support for data-driven processes.
        """
    )

    # Job 3
    st.subheader("Student Assistant IT Services")
    st.write("**Friedrich Schiller University Jena**")
    st.write("Jena, Germany")
    st.write("02.2020 - 03.2021")

    # Job 4
    st.subheader("Intern Sales Planning")
    st.write("**Porsche AG**")
    st.write("Stuttgart, Germany")
    st.write("02.2019 - 08.2019")

    # Job 5
    st.subheader("Student Assistant Research Support Department")
    st.write("**University of Hohenheim**")
    st.write("Stuttgart, Germany")
    st.write("04.2018 - 01.2019")

    # Education
    st.header("Education")

    # Degree 1
    st.subheader("M.Sc. Business Information Systems")
    st.write("**Friedrich Schiller University Jena**")
    st.write("2022")

    # Degree 2 (Optional)
    st.subheader("B.Sc. Business Administration and Economics")
    st.write("**University of Hohenheim**")
    st.write("2019")

    # Skills
    st.header("Skills")
    st.write(
        """
        - **Languages:** German (Native Speaker), English (Advanced), French (Basic knowdledge)
        - **Programming languages:** SQL (Excellent), Python (Advanced beginner)
        - **Data warehouses:** Redshift, Snowflake
        - **BI tools:** Looker, Metabase, PowerBI
        - **ELT:** dbt, LookML, Stitch, Snowplow, Hightouch, Dagster
        - **Other tools:** HubSpot, Intercom, Jira, Confluence, Excel, AWS	
        """
    )

    # Volunteer Experience
    st.header("Volunteer Experience")

    # 1
    st.subheader("CorrelAid e.V. - Member & Organizer of Mentoring Program")
    st.write("04.2023 - Today")

    # 2
    st.subheader("AIESEC e.V. Jena - Member")
    st.write("10.2019 - 10.2020")

    # 3
    st.subheader("AIESEC e.V., Mandya, India - Global Volunteer")
    st.write("09.2019 - 10.2019")

    # 4
    st.subheader("ROCK YOUR LIFE! Hohenheim e.V. - Mentor & Network Coordinator")
    st.write("10.2017 - 08.2019")

    # Other
    st.header("Other")
    st.write("Certifications: Microsoft Certified: Data Analyst Associate")
    st.write("Hobbies: Football, fitness, tennis, reading")
    st.write("Interests: Minimalism, literature, nutrition, digitization")
