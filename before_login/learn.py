import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

encoded_logo = get_base64_image("resources\\logo.png")


st.markdown(
    f"""
    <div style="display: flex; align-items: center; justify-content: center; background-color: #fffdd0; padding: 2px; border-radius: 20px;">
        <img src="data:image/png;base64,{encoded_logo}" width="125" height="110" style="margin-right: 20px;">
        <h3 style="margin: 0; color: black;">Learn More about Money Management!</h3>
    </div>
    """, 
    unsafe_allow_html=True
)

st.write("\n")
st.write("\n")
st.write("\n")

st.subheader("Featured articles and videos to 📝 yourselves ", divider="gray")

# Function to encode PNG image to base64
def img_to_b64(path):
    with open(path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return f"data:image/png;base64,{encoded_string}"

def centered_link_button(col, label, image_path, link, key):
    b64_image = img_to_b64(image_path)
    # Determine background color based on image name
    if "video.png" in image_path:
        bg_color = "#f08080 "  # Light red for YouTube
    elif "bill.png" in image_path:
        bg_color = "#CC99CC"  # Light yellow for bill
    else:
        bg_color = "#f0f0f0" # Default color

    with stylable_container(
        key=key + "_container",
        css_styles=f"""
            .button-wrapper {{
                width: 175px;
                height: 150px;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                border-radius: 10px;
                background-color: {bg_color};  /* Dynamic background color */
                margin: 8px;
                padding: 10px;
            }}
            .button-wrapper a {{
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                text-decoration: none;
                color: inherit;
            }}
            .button-wrapper img {{
                width: 50%; /* Smaller icon (was 80%) */
                height: auto;
                object-fit: contain;
                margin-bottom: 5px;
            }}
            .button-wrapper span {{
                font-size: 1.2em; /* Larger label (adjust as needed) */
                font-weight: bold; /* Bold label */
                text-align: center;
                color: black;
                
            }}
        """,
    ):
        st.markdown(f"""<div class="button-wrapper">
            <a href="{link}" target="_blank">
                <img src="{b64_image}">
                <span>{label}</span>
            </a>
        </div>""", unsafe_allow_html=True)
        if st.session_state.get(key):
            st.write(f"{label} button clicked!")
            del st.session_state[key]

# ... (rest of your code, including colors and columns)
one, two, left, middle, right, six, seven = st.columns([1, 1, 3, 3, 3, 1, 1])

button_data = {
    left: [
        ("What is Finance", "resources/icons-buttons/bill.png", "https://corporatefinanceinstitute.com/resources/wealth-management/what-is-finance-definition/?utm_source=morning_brew", "learn1_button"),  # Added link
        ("Financial Instruments", "resources/icons-buttons/bill.png", "https://marketbusinessnews.com/financial-glossary/financial-instrument/?utm_source=morning_brew", "learn2_button"),  # Added link
        ("Finance for Dummies", "resources/icons-buttons/video.png", "https://www.youtube.com/watch?v=DNYCgsyOAW4", "learn7_button"),  # Added link
    ],
    middle: [
        ("Financial Leverage", "resources/icons-buttons/video.png", "https://www.youtube.com/watch?v=GESzfA9odgE", "learn3_button"),  # Added link
        ("Equity vs Debt vs Security", "resources/icons-buttons/bill.png", "https://www.thebalancemoney.com/securities-definition-and-effect-on-the-u-s-economy-3305961?utm_source=morning_brew", "learn4_button"),  # Added link
        ("Complete Beginner's Guide", "resources/icons-buttons/medium.png", "https://medium.com/@TheFinancialRevolution/personal-finance-for-beginners-5d3e9720adb5", "learn8_button"),  # Added link
    ],
    right: [
        ("Risk vs Reward Ratio", "resources/icons-buttons/video.png", "https://www.youtube.com/watch?v=aKZsireNBIM", "learn5_button"),  # Added link
        ("Mutual Funds", "resources/icons-buttons/bill.png", "https://money.usnews.com/investing/funds/articles/best-guide-to-mutual-funds?utm_source=morning_brew", "learn6_button"),  # Added link
        ("Beginners Ultimate Guide", "resources/icons-buttons/medium.png", "https://medium.com/@rishabhshah330/basics-of-finance-beginners-ultimate-guide-0ea18a676311", "learn9_button"),  # Added link
    ],
}

for col, data in button_data.items():
    with col:
        for i, (label, image_path, link, key) in enumerate(data):
            centered_link_button(col, label, image_path, link, key)

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)