import streamlit as st
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

MAILGUN_API_KEY = os.getenv('MAILGUN_API_KEY')
MAILGUN_DOMAIN = os.getenv('MAILGUN_DOMAIN')
PERSONAL_MAIL = os.getenv('PERSONAL_MAIL')

def send_email(name, email, message):
    """Send an email using Mailgun."""
    if not MAILGUN_API_KEY or not MAILGUN_DOMAIN:
        st.error("Mailgun API key or domain is not set.")
        return False

    from_email = f"no-reply@{MAILGUN_DOMAIN}"  # Replace with your Mailgun domain
    to_email = "{PERSONAL_MAIL}"  # Replace with your destination email

    subject = f"New Contact Form Submission from {name}"
    content = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

    return requests.post(
        f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
        auth=("api", MAILGUN_API_KEY),
        data={"from": from_email,
              "to": [to_email],
              "subject": subject,
              "text": content})

def run():
    """Display the contact page with a form."""
    st.title("Contact Me")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send Message")

        if submitted:
            response = send_email(name, email, message)
            if response.status_code == 200:
                st.success("Your message was sent successfully!")
            else:
                st.error(f"There was an error sending your message. Status code: {response.status_code}, Message: {response.json().get('message')}")
