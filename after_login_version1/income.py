import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import base64

st.write("\n")
st.write("\n")
st.write("\n")

# Function to encode PNG image to base64
def img_to_b64(path):
    with open(path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return f"data:image/png;base64,{encoded_string}"

def centered_button(col, label, image_path, key, color="black"):
    b64_image = img_to_b64(image_path)
    with stylable_container(
        key=key + "_container",
        css_styles=f"""
            .button-wrapper {{
                width: 58%; /* Takes full column width */
                display: flex;
                align-items: center;
                justify-content: center;
                border-radius: 10px;
                background-color: #fffacd;
                margin: 8px;
                position: relative;
                overflow: hidden;
            }}
            .button-wrapper::before {{ /* Creates the square aspect ratio */
                content: "";
                display: block;
                padding-bottom: 100%; /* 100% width = 100% height for a square */
            }}
            .button-wrapper button {{
                position: absolute; /* Needed for proper positioning */
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 0;
                border: none;
                background: none;
            }}
            .button-wrapper img {{
                width: 100%;
                height: 100%;
                object-fit: cover;
                transition: opacity 0.3s ease;
            }}
            .button-wrapper:hover img {{
                opacity: 0;
            }}
            .button-wrapper span {{ /* Tooltip styles */
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                background-color: rgba(0, 0, 0, 0.7);
                color: white;
                padding: 5px 10px;
                border-radius: 5px;
                transition: opacity 0.3s ease;
                opacity: 0;
                font-size: 15px;
            }}
            .button-wrapper:hover span {{
                opacity: 1;
            }}
        """,
    ):
        st.markdown(f"""<div class="button-wrapper">
            <button type="button">
                <img src="{b64_image}">
                <span>{label}</span>
            </button>
        </div>""", unsafe_allow_html=True)
        if st.session_state.get(key):
            st.write(f"{label} button clicked!")
            del st.session_state[key]

# ... (rest of your code, including colors and columns)
one, two, left, middle, right, six, seven = st.columns([2, 2, 3, 3, 3, 2, 2])

colors = ["orange", "lavender", "pink", "blue", "orange", 
          "red", "green", "brown", "green", "lavender", 
          "purple", "orange", "dark green", "red", "green"]

button_data = {
    left: [
        ("Bills", "resources/icons-buttons/bill.png", "bills_button"),  # Example FA icon classes
        ("Communication", "resources/icons-buttons/communication.png", "communication_button"),
        ("Food", "resources/icons-buttons/food.png", "food_button"),
        ("House", "resources/icons-buttons/house.png", "house_button"),
        ("Taxi", "resources/icons-buttons/taxi.png", "taxi_button"),
    ],
    middle: [
        ("Car", "resources/icons-buttons/car.png", "car_button"),
        ("Eating Out", "resources/icons-buttons/eating-out.png", "eating_button"),  # Example FA icon classes
        ("Gifts", "resources/icons-buttons/gift.png", "gifts_button"),
        ("Pets", "resources/icons-buttons/pet.png", "pets_button"),
        ("Toiletry", "resources/icons-buttons/toilet.png", "toiletry_button"),
    ],
    right: [
        ("Clothes", "resources/icons-buttons/varsity-jacket.png", "clothes_button"),  # Example FA icon classes
        ("Entertainment", "resources/icons-buttons/entertainment.png", "entertainment_button"),
        ("Health", "resources/icons-buttons/healthcare.png", "healths_button"),
        ("Sports", "resources/icons-buttons/sports.png", "sports_button"),
        ("Education", "resources/icons-buttons/blackboard.png", "transport_button"),
    ],
}

j = 0
for col, data in button_data.items():
    with col:
        for i, (label, image_path, key) in enumerate(data):  # image_path now
            color = colors[j]
            j += 1
            centered_button(col, label, image_path, key, color)  # Pass image_path

st.markdown("<br><br>", unsafe_allow_html=True)