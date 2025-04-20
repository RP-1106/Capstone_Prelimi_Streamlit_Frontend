import streamlit as st
from streamlit_extras.switch_page_button import switch_page

if "shared_df" not in st.session_state:
    st.session_state.shared_df = None
if "uploaded_file_name" not in st.session_state:
    st.session_state.uploaded_file_name = None
if "income_df" not in st.session_state:
    st.session_state.income_df = None
if "expense_df" not in st.session_state:
    st.session_state.expense_df = None
if "ID" not in st.session_state:
    st.session_state.ID = None

# Define navigation pages for before and after login
before_login_pages = [
    st.Page("before_login/about.py", title="About", icon="ℹ️"),
    st.Page("before_login/features.py", title="Features", icon="✨"),
    #st.Page("before_login/novelty.py", title="Novelty", icon="💡"),
    st.Page("before_login/tools.py", title="Tools", icon="🔧"),
    st.Page("before_login/generic_chatbot.py", title="Bot", icon="🤖"),
    st.Page("before_login/learn.py", title="Learn", icon="📚"),
    st.Page("before_login/login.py", title="Login", icon="🔑")
]

after_login_pages = [
    #st.Page("after_login/getting_started.py", title="Getting Started", icon="🚀"),
    st.Page("after_login/overview.py", title="Overview", icon="🏠"),
    st.Page("after_login/upload_data.py", title="Upload Data", icon="⬆️"),
    #st.Page("after_login/analysis.py", title="Analysis", icon="📊"),
    #st.Page("after_login/expense.py", title="Expense", icon="💸"),
    st.Page("after_login/expense.py", title="Expense", icon="💳"),
    st.Page("after_login/income.py", title="Income", icon="💰"),
    #st.Page("after_login/goals.py", title="Goals and Savings", icon="🚩"),
    st.Page("after_login/bot.py", title="Bot", icon="🤖"),
    st.Page("after_login/performance.py", title="Performance Analysis", icon="📊"),
    #st.Page("after_login/education.py", title="Education", icon="📝"),
    st.Page("after_login/settings.py", title="Settings", icon="⚙️"),
]

st.set_page_config(layout="wide")

# Session state to manage login status
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Choose pages based on login status
if st.session_state.logged_in:
    pages = after_login_pages
else:
    pages = before_login_pages

st.markdown("<h2 style='text-align: center; color: black; background-color: #fffdd0;'> 💸 PaisaVault 💸</h2>", unsafe_allow_html=True)

# Navigation setup
#pg = st.navigation(pages, position="sidebar", expanded=True)
pg = st.navigation(pages, expanded=True)
pg.run()


# Redirect logic for settings page to log out
if 'logout' in st.query_params:  # Use square brackets for query parameter check
    st.session_state["logged_in"] = False
    switch_page("../before_login/login.py")
