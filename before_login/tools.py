# import streamlit as st
# from streamlit_extras.stylable_container import stylable_container
# import pathlib
# import base64

# def load_css(file_path):
#    with open(file_path) as f:
#       st.html(f"<style>{f.read()}</style")

# css_path = pathlib.Path("before_login/before_styles.css")
# load_css(css_path)

# # Function to calculate simple interest
# def calculate_simple_interest(principal, rate, time):
#   if principal == 0 or rate == 0 or time == 0:
#     return "Please enter valid values for all fields."
#   else:
#     interest = (principal * rate * time) / 100
#     return round(interest, 2)


# # Function to calculate compound interest
# def calculate_compound_interest(principal, rate, time, compounds_per_year):
#   if principal == 0 or rate == 0 or time == 0 or compounds_per_year == 0:
#     return "Please enter valid values for all fields."
#   else:
#     r = rate / 100
#     amount = principal * (1 + r / compounds_per_year) ** (compounds_per_year * time)
#     compound_interest = amount - principal
#     return round(compound_interest, 2)

# def get_base64_image(image_path):
#     with open(image_path, "rb") as img_file:
#         return base64.b64encode(img_file.read()).decode()

# encoded_logo = get_base64_image(r"C:\Users\USER\Desktop\Capstone Frontend\resources\logo.png")


# st.markdown(
#     f"""
#     <div style="display: flex; align-items: center; justify-content: center; background-color: #fffdd0; padding: 2px; border-radius: 20px;">
#         <img src="data:image/png;base64,{encoded_logo}" width="125" height="110" style="margin-right: 20px;">
#         <h3 style="margin: 0; color: black;">Wanna try out some of our Handy Tools?</h3>
#     </div>
#     """, 
#     unsafe_allow_html=True
# )

# st.write("\n\n")
# # Layout for the web app
# col1, col2, col3 = st.columns([2,1,2])

# with col1:
#     with stylable_container(
#         key="simple_interest_style",
#         css_styles="""
#             {
#                 background-color: #efebef;
#                 color: black;
#                 border-radius: 20px;
#                 padding: 20px; 
#                 text-align: center; 
#             }
#         """,
#     ):
#         st.header("Simple Interest Calculator")

#         # Container for the result
#         with stylable_container(
#             key="si_result_container",
#             css_styles="""
#                 {
#                     background-color: #D6FF58; 
#                     padding: 10px; 
#                     border-radius: 5px; 
#                     margin-bottom: 15px; 
#                     height: 50px;
#                 }
#             """,
#         ):
#             si_result_container = st.markdown("₹     \nTotal Simple Interest") 

#         principal = st.number_input("Principal Amount (₹)", min_value=0.0, key="si_p")
#         rate = st.number_input("Rate of Interest (% p.a.)", min_value=0.0, key="si_rate")
#         time = st.number_input("Time Period (Years)", min_value=0.0, key="si_time")
#         st.write("\n\n")
#         st.write("\n\n")
#         st.write("\n\n")
#         st.write("\n\n")
#         st.write("\n\n")
#         st.write("\n\n")
#         st.write("\n\n")
#         st.write("\n\n")
#         st.write("\n\n")
#         st.write("\n\n")

#         # Calculate button
#         with stylable_container(
#             key="si_button",
#             css_styles="""
#                 button {
#                     background-color: black;
#                     color: white;
#                     border-radius: 20px;
#                     padding: 10px 20px; 
#                 }
#             """,
#         ):
#             if st.button("Calculate", key="si_button"):
#                 result = calculate_simple_interest(principal, rate, time)
#                 si_result_container.write(f"₹{result}     \nTotal Simple Interest")

# with col3:   
#     # Container for the result
#     with stylable_container(
#         key="compound_interest_style",
#         css_styles="""
#             {
#                 background-color: #efebef;
#                 color: black;
#                 border-radius: 20px;
#                 padding: 20px; 
#                 text-align: center; 
#             }
#         """,
#     ):
#         st.header("Compound Interest Calculator")

#         # Container for the result
#         with stylable_container(
#             key="ci_result_container",
#             css_styles="""
#                 {
#                     background-color: #D6FF58; 
#                     padding: 10px; 
#                     border-radius: 5px; 
#                     margin-bottom: 15px; 
#                     height: 50px;
#                 }
#             """,
#         ):
#             ci_result_container = st.markdown("₹     \nTotal Compound Interest") 

#         principal = st.number_input("Principal Amount (₹)", min_value=0.0, key="ci_p")
#         st.write("\n")
#         rate = st.number_input("Rate of Interest (% p.a.)", min_value=0.0, key="ci_rate")
#         st.write("\n")
#         time = st.number_input("Time Period (Years)", min_value=0.0,key="ci_time")
#         st.write("\n")
#         compounds_per_year = st.number_input("Compounds per Year", min_value=1,key="ci_year")
#         st.write("\n")
#         st.write("\n")

#         # Calculate button
#         with stylable_container(
#             key="ci_button",
#             css_styles="""
#                 button {
#                     background-color: black;
#                     color: white;
#                     border-radius: 20px;
#                     padding: 10px 20px; 
#                 }
#             """,
#         ):
#             if st.button("Calculate", key="ci_button"):
#                 result = calculate_compound_interest(principal, rate, time, compounds_per_year)
#                 ci_result_container.write(f"₹{result}     \nTotal Compound Interest")


import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import pathlib
import base64 

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

encoded_logo = get_base64_image("resources\\logo.png")

def load_css(file_path):
   with open(file_path) as f:
      st.html(f"<style>{f.read()}</style")

css_path = pathlib.Path("before_login/before_styles.css")
load_css(css_path)

# Function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
  if principal == 0 or rate == 0 or time == 0:
    return "Please enter valid values for all fields."
  else:
    interest = (principal * rate * time) / 100
    return round(interest, 2)


# Function to calculate compound interest
def calculate_compound_interest(principal, rate, time, compounds_per_year):
  if principal == 0 or rate == 0 or time == 0 or compounds_per_year == 0:
    return "Please enter valid values for all fields."
  else:
    r = rate / 100
    amount = principal * (1 + r / compounds_per_year) ** (compounds_per_year * time)
    compound_interest = amount - principal
    return round(compound_interest, 2)

st.markdown(
    f"""
    <div style="display: flex; align-items: center; justify-content: center; background-color: #fffdd0; padding: 2px; border-radius: 20px;">
        <img src="data:image/png;base64,{encoded_logo}" width="125" height="110" style="margin-right: 20px;">
        <h3 style="margin: 0; color: black;">Wanna try out some of our Handy Tools?</h3>
    </div>
    """, 
    unsafe_allow_html=True
)

st.write("\n\n")
# Layout for the web app
col1, col2, col3 = st.columns([2,1,2])

with col1:
    with stylable_container(
        key="simple_interest_style",
        css_styles="""
            {
                background-color: #efebef;
                color: black;
                border-radius: 20px;
                padding: 20px; 
                text-align: center; 
                width: 350px;
            }
        """,
    ):
        st.header("Simple Interest Calculator")

        # Container for the result
        with stylable_container(
            key="si_result_container",
            css_styles="""
                {
                    background-color: #D6FF58; 
                    padding: 10px; 
                    border-radius: 5px; 
                    margin-bottom: 15px; 
                    height: 50px;
                }
            """,
        ):
            si_result_container = st.markdown("₹     \nTotal Simple Interest") 

        st.markdown(
            """
            <style>
            label {
                color: black !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        principal = st.number_input("Principal Amount (₹)", min_value=0.0, key="si_p")
        rate = st.number_input("Rate of Interest (% p.a.)", min_value=0.0, key="si_rate")
        time = st.number_input("Time Period (Years)", min_value=0.0, key="si_time")
        st.write("\n\n")
        st.write("\n\n")
        st.write("\n\n")
        st.write("\n\n")
        st.write("\n\n")
        st.write("\n\n")
        st.write("\n\n")
        st.write("\n\n")
        st.write("\n\n")
        st.write("\n\n")

        # Calculate button
        with stylable_container(
            key="si_button",
            css_styles="""
                button {
                    background-color: black;
                    color: white;
                    border-radius: 20px;
                    padding: 10px 20px; 
                }
            """,
        ):
            if st.button("Calculate", key="si_button"):
                result = calculate_simple_interest(principal, rate, time)
                si_result_container.write(f"₹{result}     \nTotal Simple Interest")

with col3:   
    # Container for the result
    with stylable_container(
        key="compound_interest_style",
        css_styles="""
            {
                background-color: #efebef;
                color: black;
                border-radius: 20px;
                padding: 20px; 
                text-align: center; 
                width: 350px;
            }
        """,
    ):
        st.header("Compound Interest Calculator")

        # Container for the result
        with stylable_container(
            key="ci_result_container",
            css_styles="""
                {
                    background-color: #D6FF58; 
                    padding: 10px; 
                    border-radius: 5px; 
                    margin-bottom: 15px; 
                    height: 50px;
                    color: black;
                }
            """,
        ):
            ci_result_container = st.markdown("₹     \nTotal Compound Interest") 

        principal = st.number_input("Principal Amount (₹)", min_value=0.0, key="ci_p")
        st.write("\n")
        rate = st.number_input("Rate of Interest (% p.a.)", min_value=0.0, key="ci_rate")
        st.write("\n")
        time = st.number_input("Time Period (Years)", min_value=0.0,key="ci_time")
        st.write("\n")
        compounds_per_year = st.number_input("Compounds per Year", min_value=1,key="ci_year")
        st.write("\n")
        st.write("\n")

        # Calculate button
        with stylable_container(
            key="ci_button",
            css_styles="""
                button {
                    background-color: black;
                    color: white;
                    border-radius: 20px;
                    padding: 10px 20px; 
                }
            """,
        ):
            if st.button("Calculate", key="ci_button"):
                result = calculate_compound_interest(principal, rate, time, compounds_per_year)
                ci_result_container.write(f"₹{result}     \nTotal Compound Interest")


st.write("\n")


import streamlit as st
import plotly.graph_objects as go
import pathlib

def load_css(file_path):
   with open(file_path) as f:
      st.html(f"<style>{f.read()}</style")

css_path = pathlib.Path("before_login/before_styles.css")
load_css(css_path)

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def calculate_total_amount(principal, interest):
    return principal + interest

st.markdown(
    """
    <style>
    .result-container {
        padding: 5px;
        border-radius: 5px;
        margin-bottom: 3px;
        text-align: center;
        font-size: 3em;
    }
    .slider-label {
        font-size: 1.5em;
        margin-bottom: 0.2px;
    }
    .code-style {  /* New class for code-like styling */
        background-color: #eee;
        border-radius: 3px;
        font-family: courier, monospace;
        padding: 0 3px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.header("EMI Calculator")

col3, col1, col2 = st.columns([0.3, 2, 3])

with col1:
    with st.container():
        total_amount_output = st.markdown("<div class='result-container'><span style='color: orange; font-weight: bold;'>₹0</span></div>", unsafe_allow_html=True)

    with st.container():
        chart_placeholder = st.empty()

with col2:
    st.write("\n")

    st.markdown("<div class='slider-label'>Loan Amount (₹)</div>", unsafe_allow_html=True)
    principal = st.slider("", min_value=0, max_value=1000000, value=1000, step=1, key="loan_amt")  # Default: 1000

    st.markdown("<div class='slider-label'>Rate of Interest (% p.a.)</div>", unsafe_allow_html=True)
    rate = st.slider("", min_value=0.0, max_value=30.0, value=3.0, step=0.1, key="interest")  # Default: 3.0

    st.markdown("<div class='slider-label'>Loan Tenure (Years)</div>", unsafe_allow_html=True)
    time = st.slider("", min_value=0, max_value=30, value=5, step=1, key="loan_emi_time")  # Default: 5

    interest = calculate_simple_interest(principal, rate, time)
    total_amount = calculate_total_amount(principal, interest)

    total_amount_output.markdown(f"<div class='result-container'><span style='color: orange; font-weight: bold;'>₹{total_amount:,.2f} </span></div>", unsafe_allow_html=True)

    fig = go.Figure(data=[go.Pie(labels=["Principal", "Interest"], values=[principal, interest], hole=.3)])
    fig.update_layout(title_text="Loan Breakdown", title_x=0.5)
    chart_placeholder.plotly_chart(fig)