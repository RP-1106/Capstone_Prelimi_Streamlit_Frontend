import streamlit as st
import pandas as pd
import os
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.switch_page_button import switch_page 
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

encoded_logo = get_base64_image("resources\\logo.png")


st.markdown(
    f"""
    <div style="display: flex; align-items: center; justify-content: center; background-color: #fffdd0; padding: 2px; border-radius: 20px; backdrop-filter: blur(10px);">
        <img src="data:image/png;base64,{encoded_logo}" width="125" height="110" style="margin-right: 20px;">
        <h3 style="margin: 0; color: black;">Ready to get Started?</h3>
    </div>
    """, 
    unsafe_allow_html=True
)


# Set up session state for toggling between forms
if 'create_account' not in st.session_state:
    st.session_state.create_account = False

def toggle_create_account():
    st.session_state.create_account = not st.session_state.create_account

# Define column widths
col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if not st.session_state.create_account:
        # Sign-in form
        st.markdown("<p style='text-align: center;font-size: 24px; margin-top:10%;'><b>Sign-in to account</b></p>", unsafe_allow_html=True)
        st.write("\n")
        st.markdown("<p style='text-align: center;margin-bottom: -100px; padding: 0px; font-size: 20px'>Enter Username</p>", unsafe_allow_html=True)
        username = st.text_input(" ", placeholder="Username", key="signin_username", label_visibility="hidden")
        #st.write("\n")
        st.markdown("<p style='text-align: center;margin-bottom:-100px; padding: 0px; font-size: 20px'>Enter Password</p>", unsafe_allow_html=True)
        password = st.text_input(" ", placeholder="Password", type="password", key="signin_password", label_visibility="hidden")
        st.write("\n")

        with stylable_container(
            key="submit_button",
            css_styles="""
                button {
                    background-color: green;
                    color: white;
                    border-radius: 20px;
                    margin-left: 43%;
                    text-align: center;  /* Added for centering */
                }
            """,
        ):
            if st.button("Submit", key="signin_submit"):
                # Check if the CSV exists
                if os.path.exists("Username-Password.csv"):
                    df = pd.read_csv("Username-Password.csv")
                    user_row = df[(df['Username'] == username) & (df['Password'] == password)]
                    if not user_row.empty:
                        st.success("Sign-in successful!")

                        if not st.session_state["logged_in"]:
                            st.session_state["logged_in"] = True
                            st.rerun()
                            switch_page("../after_login/home.py")
        
                    else:
                        st.error("Incorrect Username or Password")
                else:
                    st.error("No accounts exist. Please create an account first.")

        st.write("\n")
        with stylable_container(
            key="create_account_button",
            css_styles="""
                button {
                    background-color: blue;
                    color: white;
                    border-radius: 20px;
                    margin-left: 39%;
                    text-align: center;  /* Added for centering */
                }
            """,
        ):
            if st.button("Create Account", key="create_account_button"):
                toggle_create_account()

    else:
        # Create account form
        st.markdown("<p style='text-align: center;margin-top: 10%; padding: 0px; font-size: 24px'><b>Create account</b></p>", unsafe_allow_html=True)
        #st.write("\n")
        st.markdown("<p style='text-align: center;margin-bottom: -100px; padding: 0px; font-size: 20px'>Create Username</p>", unsafe_allow_html=True)
        new_username = st.text_input(" ", placeholder="Username", key="create_username",label_visibility="hidden")
        st.write("\n")
        st.markdown("<p style='text-align: center;margin-bottom: -100px; padding: 0px; font-size: 20px'>Create Password</p>", unsafe_allow_html=True)
        new_password = st.text_input(" ", placeholder="Password", type="password", key="create_password", label_visibility="hidden")
        st.write("\n")

        with stylable_container(
            key="submit_button",
            css_styles="""
                button {
                    background-color: green;
                    color: white;
                    border-radius: 20px;
                    margin-left: 42%;
                    text-align: center;  /* Added for centering */
                }
                """,
        ):
            if st.button("Submit", key="create_submit"):
                if os.path.exists("Username-Password.csv"):
                    df = pd.read_csv("Username-Password.csv")
                    if new_username in df['Username'].values:
                        st.error("Username is already taken, try again!")
                    else:
                        new_row = pd.DataFrame({"Username": [new_username], "Password": [new_password]})
                        df = pd.concat([df, new_row], ignore_index=True)
                        df.to_csv("Username-Password.csv", index=False)
                        st.success("Account created successfully!")
                else:
                    new_df = pd.DataFrame({"Username": [new_username], "Password": [new_password]})
                    new_df.to_csv("Username-Password.csv", index=False)
                    st.success("Account created successfully!")

            st.write("\n")
            with stylable_container(
                key="create_submit_button",
                css_styles="""
                    button {
                        background-color: blue;
                        color: white;
                        border-radius: 20px;
                        margin-left: 39%;
                        text-align: center;  /* Added for centering */
                    }
                    """,
            ):
                if st.button("Back to Sign-in", key="back_to_signin"):
                    toggle_create_account()
