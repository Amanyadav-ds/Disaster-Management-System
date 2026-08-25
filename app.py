import streamlit as st

from auth.login import show_login
from pages.dashboard import show_dashboard


st.set_page_config(
    page_title="Disaster Management System",
    page_icon="🌍",
    layout="wide"
)


if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False


if "page" not in st.session_state:
    st.session_state["page"] = "dashboard"


if st.session_state["logged_in"]:

    show_dashboard()

else:

    show_login()