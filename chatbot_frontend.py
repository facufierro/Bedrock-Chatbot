import streamlit as st
from chatbot_backend import demo_memory, demo_conversation

# Initialize memory for the chatbot
if 'memory' not in st.session_state:
    st.session_state.memory = demo_memory()

st.title("Chatbot Interface")

# Display the chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Clear Chat Text

# Clear chat history (red and with warning)

def clear_chat():
    st.session_state.chat_history = []
    st.session_state.memory = demo_memory()


st.button("Clear Chat", on_click=clear_chat)

# Form for the user input
with st.form(key='user_input_form', clear_on_submit=True):
    user_input = st.text_input("You:", key="input_text")
    submit_button = st.form_submit_button(label='Send')

if submit_button and user_input:
    # Get the chatbot response
    bot_response = demo_conversation(user_input, st.session_state.memory)

    # Save the chat history in the session state
    st.session_state.chat_history.append({"user": user_input, "bot": bot_response})

# Display updated chat history
for chat in st.session_state.chat_history:
    st.write(f"**User:** {chat['user']}")
    st.write(f"**Bot:** {chat['bot']}")
