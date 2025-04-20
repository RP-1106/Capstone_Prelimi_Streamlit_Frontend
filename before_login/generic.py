'''
import streamlit as st
import random
import time


# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("Simple chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
'''



import json
import streamlit as st
import base64

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

encoded_logo = get_base64_image("resources\\logo.png")


def load_faq_data():
    with open('resources/finance.json', 'r') as file:
        return json.load(file)

def get_response(user_question, faq_data):
    user_keywords = user_question.lower().split()
    for question, answer in faq_data.items():
        question_keywords = question.lower().split()
        if any(word in question_keywords for word in user_keywords):
            return answer
    return "Sorry, I couldn't find an answer to your query."

st.markdown(
    f"""
    <div style="display: flex; align-items: center; justify-content: center; background-color: #fffdd0; padding: 2px; border-radius: 20px;">
        <img src="data:image/png;base64,{encoded_logo}" width="170" height="150" style="margin-right: 40px;">
        <h3 style="margin: 0; color: black;">Let our bot help you with your queries!</h3>
    </div>
    """, 
    unsafe_allow_html=True
)

st.write("\n")

faq_data = load_faq_data()

# Add a button to clear the chat history
if st.button("Clear Chat History"):
    st.session_state.messages = []  # Clear the messages list
    st.rerun()  # Force Streamlit to rerun the app

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How can I assist you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = get_response(prompt, faq_data)
    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})