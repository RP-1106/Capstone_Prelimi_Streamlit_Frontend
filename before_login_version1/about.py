import streamlit as st
import plotly.express as px

# Define initial data
data = {
    "Category": [
        "Education",
        "Rent/Mortgage",
        "Dining",
        "Entertainment",
        "Transportation",
        "Groceries",
        "Utilities",
        "Healthcare",
        "Shopping"
    ],
    "Amount": [10, 25, 5, 2, 6, 14, 10, 18, 10]
}

st.write("\n")

# Create checkboxes for each category
selected_categories = st.multiselect(
    "Select Categories",
    options=data["Category"],
    default=data["Category"]  # Select all categories by default
)

# Filter data based on selected categories
filtered_data = {
    "Category": [category for category in data["Category"] if category in selected_categories],
    "Amount": [amount for category, amount in zip(data["Category"], data["Amount"]) if category in selected_categories]
}

# Create the pie chart using Plotly
fig = px.pie(
    filtered_data,
    names="Category",
    values="Amount",
    width=800,  # Set width of the chart
    height=600  # Set height of the chart
)

# Create columns with full width layout
col1, col2 = st.columns(2)

# Description in left column
with col1:
    st.write("\n")
    st.write("The AI Assisted Personal Finance Management System is an intelligent web application that streamlines personal financial planning through the integration of artificial intelligence and data science. Designed as a comprehensive platform, it enables users to manage income, track expenditures, set financial goals, and receive tailored insights, all within a compact and user-friendly dashboard. The application’s privacy-centric approach avoids linking with personal bank accounts, instead urging users to upload receipts and categorize transactions, creating a safe, centralized financial ecosystem. To deliver a holistic experience, the system uses technologies like NLP for personalized chatbot responses, and predictive analytics for trend forecasting and goal-setting.")

    st.write("Advanced data visualization tools present clear, actionable insights, while unique simulation features allow users to project the potential impacts of their spending habits over time. Additional features include custom settings to match user preferences, intelligent reminders for ensuring consistency, and financial education resources for aiding the users on a daily basis. Thus, our application prioritizes security and user privacy by operating independently from sensitive accounts, making it a safe, accessible tool for end-to-end financial management.")

    #st.write("The target audience for our budgeting application includes individuals and families looking for a secure, user-friendly, and comprehensive way to manage personal finances without linking sensitive financial accounts. This tool caters especially to users concerned with privacy who prefer manual entry or receipt-based tracking over direct bank integration, addressing the growing demand for data security in financial management. Additionally, it serves people with diverse spending habits—such as frequent online shoppers, cash spenders, and small business owners—who require a streamlined, customizable solution for tracking expenses. The application is also ideal for users seeking actionable insights into their spending patterns, thanks to the integration of advanced data analytics and a highly responsive chatbot. With features designed to enhance personal finance literacy, the app is accessible for users of all financial knowledge levels, providing straightforward tools for managing budgets, setting savings goals, and gaining better control over daily and long-term expenses.")

# Filters, chart, and photo in right column
with col2:
    
    #st.write(selected_categories)  # Display selected categories

    st.plotly_chart(fig)

    # Add a placeholder for the photo (you'll need to replace this with actual image loading)
    #st.image("before_login/money.jpg", width=300)
