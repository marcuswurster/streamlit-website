import streamlit as st
import importlib

st.set_page_config(page_title="Marcus Wurster", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "CV", "Contact"])

# Map the page names to the corresponding modules in the `pages` folder
page_mapping = {
    "Home": "pages.home",
    "Contact": "pages.contact",
    "CV": "pages.cv"
}

# Dynamically import and run the selected page module
if page in page_mapping:
    selected_module = importlib.import_module(page_mapping[page])
    if hasattr(selected_module, "run"):
        selected_module.run()
    else:
        st.write("This page does not have a `run` function defined.")
