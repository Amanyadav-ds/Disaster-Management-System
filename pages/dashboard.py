import streamlit as st


def show_dashboard():

    st.title("📊 Disaster Management Dashboard")

    st.success("Dashboard loaded successfully!")

    st.write("Welcome to the Disaster Management System 👋")

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🌪️ Disasters", 1)

    with col2:
        st.metric("👥 Victims", 0)

    with col3:
        st.metric("🏕️ Relief Camps", 1)

    col4, col5, col6 = st.columns(3)

    with col4:
        st.metric("🙋 Volunteers", 0)

    with col5:
        st.metric("📦 Resources", 1)

    with col6:
        st.metric("💰 Donations", 0)

    st.divider()

    st.subheader("🚨 Quick Actions")

    st.button("🌪️ Manage Disasters")
    st.button("👥 Manage Victims")
    st.button("📦 Manage Resources")