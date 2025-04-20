import streamlit as st
from pathlib import Path
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

encoded_logo = get_base64_image("resources\\logo.png")


st.markdown(
    f"""
    <div style="display: flex; align-items: center; justify-content: center; background-color: #fffdd0; padding: 2px; border-radius: 20px;">
        <img src="data:image/png;base64,{encoded_logo}" width="125" height="110" style="margin-right: 20px;">
        <h3 style="margin: 0; color: black;">How we help in Managing your Finances?</h3>
    </div>
    """, 
    unsafe_allow_html=True
)

texts = [
"The AI-based chatbot is trained on personalized user data, which includes transaction history, categories of expenses, and financial goals. This data will allow the chatbot to provide tailored advice and insights (e.g., “How can I save more on groceries?” or “Can you suggest a savings plan for a vacation next year?",
"The statistical models are responsible for providing financial insights, recommendations, and predictions, such as forecasting future expenses, identifying areas to cut back on spending, or providing personalized financial plans etc.",
"The Butterfly Effect Model enables users to explore how small adjustments in financial habits could yield significant changes over time, often referred to as the “butterfly effect.” It puts up neural networks and LSTM models to track discretionary spending in patterns for alternative financial outcomes, which in turn is used to find more expression to compound effect of diverting funds for all these directions to investments",
"The Scenario Testing Model is an attempt to create a breakthrough in financial forecasting by integrating machine learning algorithms with Monte Carlo simulations. This hybrid technique allows for exact prediction of financial outcomes across various time periods, providing unique insights into personal financial planning and goal success likelihood.",
]

images = [
    "resources/aboutus.png",
    "resources/aboutus.png",
    "resources/aboutus.png"
]

col1, col2 = st.columns(2)

col1.write(f"<p style='font-size: 20px; margin-top:10%; '>{texts[0]}</p>", unsafe_allow_html=True)
#col1.write("\n")
col1.write(f"<p style='font-size: 20px; '>{texts[1]}</p>", unsafe_allow_html=True)
#col1.write("\n")
col1.write(f"<p style='font-size: 20px;  '>{texts[2]}</p>", unsafe_allow_html=True)
#col1.write("\n")
col1.write(f"<p style='font-size: 20px;  '>{texts[3]}</p>", unsafe_allow_html=True)


col2.write("\n")
col2.write("\n")
col2.write("\n")
col2.write("\n")
col2.write("\n")
col2.image(images[1])
