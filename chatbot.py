import os
from dotenv import load_dotenv

from IPython.display import Markdown, display
from openai import OpenAI
import streamlit as st


# client = OpenAI()

# load_dotenv(override=True)
# api_key = os.getenv('OPENAI_API_KEY')

# Create OpenAI client
client = OpenAI()

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI Chatbot")
st.write("Powered by OpenAI + Streamlit")


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("Ask something...")

if prompt:
    st.session_state.messages.append({"role" : "user" , "content" : prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response=client.chat.completions.create(model="gpt-5-nano",messages=st.session_state.messages)

    bot_reply = response.choices[0].message.content

    # Show assistant reply
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)







