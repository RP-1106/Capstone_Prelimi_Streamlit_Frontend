import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.switch_page_button import switch_page

# Define column widths
col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    # Sign-out button with confirmation
    with stylable_container(
        key="signout_button",
        css_styles="""
            button {
                background-color: red;
                color: white;
                border-radius: 20px;
                margin-top:5%;
                margin-left: 40%;
                text-align: center;
            }
        """,
    ):
        if st.button("Sign Out"):
            # Confirmation buttons in separate columns
            confirm_col, cancel_col = st.columns(2)
            with confirm_col:
                with stylable_container(
                    key="confirm_button",
                    css_styles="""
                        button {
                            background-color: blue;
                            color: white;
                            border-radius: 20px;
                            margin-left: 40%;
                            text-align: center;
                        }
                        """,
                    ):
                        if st.button("Confirm"):
                            #st.session_state.logged_in = False
                            if st.session_state["logged_in"]:
                                st.session_state["logged_in"] = False
                                st.rerun()
                                switch_page("../after_login/home.py")

            with cancel_col:
                with stylable_container(
                    key="cancel_button",
                    css_styles="""
                        button {
                            background-color: blue;
                            color: white;
                            border-radius: 20px;
                            margin-left: 40%;
                            text-align: center;
                        }
                        """,
                    ):
                        if st.button("Cancel"):
                            st.empty()  # Hide buttons on cancel

