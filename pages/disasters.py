import streamlit as st
from utils.db import connect_db


def show_disasters():

    st.title("🌪️ Disaster Management")

    st.write("Manage all disaster records in the system.")

    st.divider()

    # =====================================================
    # ADD DISASTER
    # =====================================================

    st.subheader("➕ Add New Disaster")

    with st.form("add_disaster_form"):

        col1, col2 = st.columns(2)

        with col1:
            disaster_name = st.text_input(
                "Disaster Name",
                placeholder="Example: Mumbai Flood"
            )

            disaster_type = st.selectbox(
                "Disaster Type",
                [
                    "Flood",
                    "Earthquake",
                    "Cyclone",
                    "Landslide",
                    "Drought",
                    "Fire",
                    "Tsunami",
                    "Other"
                ]
            )

            location = st.text_input(
                "Location",
                placeholder="Example: Mumbai"
            )

        with col2:

            severity = st.selectbox(
                "Severity",
                [
                    "Low",
                    "Medium",
                    "High",
                    "Critical"
                ]
            )

            start_date = st.date_input(
                "Start Date"
            )

            status = st.selectbox(
                "Status",
                [
                    "Active",
                    "Under Control",
                    "Resolved"
                ]
            )

        description = st.text_area(
            "Description",
            placeholder="Enter disaster details..."
        )

        submit = st.form_submit_button(
            "➕ Add Disaster",
            use_container_width=True
        )

        if submit:

            if not disaster_name or not location:

                st.error(
                    "Please enter the disaster name and location."
                )

            else:

                connection = connect_db()
                cursor = connection.cursor()

                query = """
                    INSERT INTO disasters
                    (
                        disaster_name,
                        disaster_type,
                        description,
                        location,
                        severity,
                        start_date,
                        status
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """

                values = (
                    disaster_name,
                    disaster_type,
                    description,
                    location,
                    severity,
                    start_date,
                    status
                )

                cursor.execute(query, values)

                connection.commit()

                cursor.close()
                connection.close()

                st.success(
                    "✅ Disaster added successfully!"
                )

                st.rerun()

    st.divider()

    # =====================================================
    # VIEW DISASTERS
    # =====================================================

    st.subheader("📋 Disaster Records")

    connection = connect_db()
    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT
            disaster_id,
            disaster_name,
            disaster_type,
            location,
            severity,
            start_date,
            status,
            description
        FROM disasters
        ORDER BY disaster_id DESC
        """
    )

    disasters = cursor.fetchall()

    cursor.close()
    connection.close()

    # =====================================================
    # SEARCH
    # =====================================================

    search = st.text_input(
        "🔍 Search Disaster",
        placeholder="Search by name, type, or location..."
    )

    if search:

        search_lower = search.lower()

        disasters = [
            disaster
            for disaster in disasters
            if (
                search_lower in disaster["disaster_name"].lower()
                or search_lower in disaster["disaster_type"].lower()
                or search_lower in disaster["location"].lower()
            )
        ]

    # =====================================================
    # DISPLAY
    # =====================================================

    if not disasters:

        st.info("No disaster records found.")

    else:

        for disaster in disasters:

            with st.container(border=True):

                col1, col2, col3 = st.columns([2, 2, 1])

                with col1:

                    st.subheader(
                        f"🌪️ {disaster['disaster_name']}"
                    )

                    st.write(
                        f"📍 **Location:** {disaster['location']}"
                    )

                    st.write(
                        f"🌋 **Type:** {disaster['disaster_type']}"
                    )

                with col2:

                    st.write(
                        f"⚠️ **Severity:** {disaster['severity']}"
                    )

                    st.write(
                        f"📅 **Start Date:** {disaster['start_date']}"
                    )

                    st.write(
                        f"📌 **Status:** {disaster['status']}"
                    )

                with col3:

                    if st.button(
                        "🗑️ Delete",
                        key=f"delete_{disaster['disaster_id']}"
                    ):

                        connection = connect_db()
                        cursor = connection.cursor()

                        cursor.execute(
                            """
                            DELETE FROM disasters
                            WHERE disaster_id = %s
                            """,
                            (disaster["disaster_id"],)
                        )

                        connection.commit()

                        cursor.close()
                        connection.close()

                        st.success(
                            "Disaster deleted successfully."
                        )

                        st.rerun()

                if disaster["description"]:

                    st.write(
                        f"📝 **Description:** "
                        f"{disaster['description']}"
                    )