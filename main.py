# main.py
# from flask import Flask, request, jsonify
# from services.chat_service import ChatService
# from controllers.conversation_controller import ConversationController

# app = Flask(__name__)

# # Replace with your actual MongoDB connection string
# mongo_connection_string = "your_mongo_connection_string"

# chat_service = ChatService(mongo_connection_string)
# conversation_controller = ConversationController(chat_service)


# @app.route('/chat', methods=['POST'])
# def chat():
#     data = request.json
#     user_id = data['user_id']
#     input_text = data['input_text']
#     response = conversation_controller.handle_user_input(user_id, input_text)
#     return jsonify({'response': response})


# if __name__ == "__main__":
#     app.run(debug=True)

import streamlit as st
from frontend import initialize_session, display_chat_interface

def main():
    initialize_session()
    display_chat_interface()

if __name__ == "__main__":
    main()