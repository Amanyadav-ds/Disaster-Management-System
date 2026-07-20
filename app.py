import streamlit as st

from auth.login import show_login

st.set_page_config(
     page_title="Disaster Management System",
     page_icon="🌏",
     layout="centered"
 )
show_login()