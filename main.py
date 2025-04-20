import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# Define navigation pages for before and after login
before_login_pages = [
    st.Page("before_login/about.py", title="About", icon="ℹ️"),
    st.Page("before_login/features.py", title="Features", icon="🚀"),
    st.Page("before_login/tools.py", title="Tools", icon="🛠️"),
    st.Page("before_login/generic.py", title="Bot", icon="🤖"),
    st.Page("before_login/learn.py", title="Learn", icon="📝"),
    st.Page("before_login/login.py", title="Log In", icon="✅"),
]

after_login_pages = [
    # st.Page("after_login/getting_started.py", title="Getting Started", icon="🏁"),
    st.Page("after_login/upload_data.py", title="Upload Data", icon="📤"),
    st.Page("after_login/overview.py", title="Overview", icon="🗺️"),
    # st.Page("after_login/income.py", title="Income", icon="💰"),
    st.Page("after_login/expense.py", title="Expense", icon="🧾"),
    # st.Page("after_login/savings.py", title="Goals & Savings", icon="🎯"),
    st.Page("after_login/bot.py", title="Custom Bot", icon="💬"),
    # st.Page("after_login/analysis.py", title="Performance Analysis", icon="🔍"),
    st.Page("after_login/finance.py", title="Financial Suggestions", icon="💡"),
    # st.Page("after_login/education.py", title="Education", icon="📚"),
    # st.Page("after_login/settings.py", title="Settings", icon="⚙️"),
    st.Page("after_login/logout.py", title="Log Out", icon="❌"),
]

# Additional pages for Financial Suggestions menu
financial_suggestions_pages = [
    st.Page("after_login/butterfly.py", title="Butterfly Effect", icon="🦋"),
    st.Page("after_login/scenario.py", title="Scenario Testing", icon="📊"),
]

st.set_page_config(layout="wide")

# Manage login session
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Track navigation state
if "menu_state" not in st.session_state:
    st.session_state.menu_state = "main"

# Choose pages based on login status
if st.session_state.logged_in:
    if st.session_state.menu_state == "main":
        pages = after_login_pages
    else:
        pages = financial_suggestions_pages  # Financial menu
else:
    pages = before_login_pages

# Sidebar Navigation
pg = st.navigation(pages, position="sidebar", expanded=True)
pg.run()

# Redirect logic for settings page to log out
if "logout" in st.query_params:
    st.session_state["logged_in"] = False
    switch_page("../before_login/login.py")

# **Fix: Checking which page is selected correctly**
if st.session_state.logged_in and pg.title == "Financial Suggestions":
    st.session_state.menu_state = "finance_menu"
    st.rerun()

# Back button for Financial Suggestions menu
if st.session_state.menu_state == "finance_menu":
    st.title("Financial Suggestions")

    if st.button("⬅ Back to Dashboard"):
        st.session_state.menu_state = "main"
        st.rerun()