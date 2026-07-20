import streamlit as st


def show_login():

    st.markdown(
        "<h1 style='text-align:center;'>🌍 Disaster Management System</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h4 style='text-align:center;'>Disaster Relief Resource Management System</h4>",
        unsafe_allow_html=True
    )

    st.divider()

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        username = st.text_input(
            "👤 Username",
            placeholder="Enter your username"
        )

        password = st.text_input(
            "🔒 Password",
            type="password",
            placeholder="Enter your password"
        )

        remember = st.checkbox("Remember Me")

        if st.button("🔐 Login", use_container_width=True):

            st.success("Login button clicked!")

    st.divider()

    st.caption("Developed By Aman Yadav")
        
        