import streamlit as st

from utils.db import get_count
from pages.disasters import show_disasters


def show_dashboard():

    # =====================================================
    # SIDEBAR
    # =====================================================

    with st.sidebar:

        st.title("🌍 Disaster Management")

        st.caption("Disaster Relief Resource System")

        st.divider()

        st.subheader("Navigation")

        # Dashboard
        if st.button(
            "📊 Dashboard",
            use_container_width=True
        ):
            st.session_state["page"] = "dashboard"
            st.rerun()

        # Disasters
        if st.button(
            "🌪️ Disasters",
            use_container_width=True
        ):
            st.session_state["page"] = "disasters"
            st.rerun()

        # Victims
        if st.button(
            "👥 Victims",
            use_container_width=True
        ):
            st.session_state["page"] = "victims"
            st.rerun()

        # Relief Camps
        if st.button(
            "🏕️ Relief Camps",
            use_container_width=True
        ):
            st.session_state["page"] = "camps"
            st.rerun()

        # Volunteers
        if st.button(
            "🙋 Volunteers",
            use_container_width=True
        ):
            st.session_state["page"] = "volunteers"
            st.rerun()

        # Resources
        if st.button(
            "📦 Resources",
            use_container_width=True
        ):
            st.session_state["page"] = "resources"
            st.rerun()

        # Donations
        if st.button(
            "💰 Donations",
            use_container_width=True
        ):
            st.session_state["page"] = "donations"
            st.rerun()

        # Reports
        if st.button(
            "📈 Reports",
            use_container_width=True
        ):
            st.session_state["page"] = "reports"
            st.rerun()

        st.divider()

        # Logout
        if st.button(
            "🚪 Logout",
            use_container_width=True
        ):

            st.session_state["logged_in"] = False

            if "user" in st.session_state:
                del st.session_state["user"]

            st.session_state["page"] = "dashboard"

            st.rerun()

    # =====================================================
    # PAGE CONTROL
    # =====================================================

    page = st.session_state.get(
        "page",
        "dashboard"
    )

    # =====================================================
    # DISASTER PAGE
    # =====================================================

    if page == "disasters":

        show_disasters()

        return

    # =====================================================
    # OTHER MODULES - TEMPORARY
    # =====================================================

    if page == "victims":

        st.title("👥 Victim Management")

        st.info(
            "Victim Management module will be added next."
        )

        return

    if page == "camps":

        st.title("🏕️ Relief Camp Management")

        st.info(
            "Relief Camp Management module will be added next."
        )

        return

    if page == "volunteers":

        st.title("🙋 Volunteer Management")

        st.info(
            "Volunteer Management module will be added next."
        )

        return

    if page == "resources":

        st.title("📦 Resource Management")

        st.info(
            "Resource Management module will be added next."
        )

        return

    if page == "donations":

        st.title("💰 Donation Management")

        st.info(
            "Donation Management module will be added next."
        )

        return

    if page == "reports":

        st.title("📈 Reports")

        st.info(
            "Reports module will be added later."
        )

        return

    # =====================================================
    # MAIN DASHBOARD
    # =====================================================

    st.title("📊 Disaster Management Dashboard")

    # =====================================================
    # USER INFORMATION
    # =====================================================

    user = st.session_state.get("user")

    if user:

        st.write(
            f"Welcome, **{user['full_name']}** 👋"
        )

        st.caption(
            f"Role: {user['role']}"
        )

    st.divider()

    # =====================================================
    # LIVE DATABASE COUNTS
    # =====================================================

    try:

        disasters = get_count("disasters")

        victims = get_count("victims")

        camps = get_count("relief_camps")

        volunteers = get_count("volunteers")

        resources = get_count("resources")

        donations = get_count("donations")

    except Exception as e:

        st.error(
            "Unable to retrieve dashboard statistics."
        )

        st.error(str(e))

        return

    # =====================================================
    # STATISTICS ROW 1
    # =====================================================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            label="🌪️ Disasters",
            value=disasters
        )

    with col2:

        st.metric(
            label="👥 Victims",
            value=victims
        )

    with col3:

        st.metric(
            label="🏕️ Relief Camps",
            value=camps
        )

    # =====================================================
    # STATISTICS ROW 2
    # =====================================================

    col4, col5, col6 = st.columns(3)

    with col4:

        st.metric(
            label="🙋 Volunteers",
            value=volunteers
        )

    with col5:

        st.metric(
            label="📦 Resources",
            value=resources
        )

    with col6:

        st.metric(
            label="💰 Donations",
            value=donations
        )

    st.divider()

    # =====================================================
    # QUICK ACTIONS
    # =====================================================

    st.subheader("🚨 Quick Actions")

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button(
            "🌪️ Manage Disasters",
            use_container_width=True
        ):

            st.session_state["page"] = "disasters"

            st.rerun()

    with col2:

        if st.button(
            "👥 Manage Victims",
            use_container_width=True
        ):

            st.session_state["page"] = "victims"

            st.rerun()

    with col3:

        if st.button(
            "📦 Manage Resources",
            use_container_width=True
        ):

            st.session_state["page"] = "resources"

            st.rerun()