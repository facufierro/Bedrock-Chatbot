# frontend.py
import streamlit as st
from backend import setup_memory_with_personal_info, generate_conversation_response

def initialize_session():
    if 'memory' not in st.session_state:
        st.session_state.memory = setup_memory_with_personal_info()
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

def clear_chat_history():
    st.session_state.chat_history = []
    st.session_state.memory = setup_memory_with_personal_info()

def display_chat_interface():
    st.title("Chatbot Interface")
    st.button("Clear Chat", on_click=clear_chat_history)

    with st.form(key='user_input_form', clear_on_submit=True):
        user_input = st.text_input("You:", key="input_text")
        submit_button = st.form_submit_button(label='Send')

    if submit_button and user_input:
        bot_response = generate_conversation_response(user_input, st.session_state.memory)
        st.session_state.chat_history.append({"user": user_input, "bot": bot_response})

    for chat in st.session_state.chat_history:
        st.write(f"**User:** {chat['user']}")
        st.write(f"**Bot:** {chat['bot']}")