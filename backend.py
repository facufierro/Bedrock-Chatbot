# backend.py
import json
from langchain_community.chat_models import BedrockChat
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def initialize_chatbot():
    chatbot = BedrockChat(
        credentials_profile_name='default',
        model_id='anthropic.claude-3-haiku-20240307-v1:0',
    )
    return chatbot

def setup_memory_with_personal_info():
    # Load JSON data
    json_data = read_json_file('personal_information.json')

    # Initialize the memory and add the JSON data
    memory = ConversationBufferMemory(
        memory_key='history',
        input_key='input',
        human_prefix="User",
        ai_prefix="Bot"
    )
    
    # Add the personal information to the memory in a natural conversation way
    personal_info_text = (
        f"Here is some information about me: "
        f"My name is {json_data['name']}, "
        f"I am {json_data['age']} years old, "
        f"and I live at {json_data['address']}."
    )
    
    memory.save_context({"input": "Here is my personal information."}, {"output": personal_info_text})
    
    return memory

def generate_conversation_response(input_text, memory):
    chatbot = initialize_chatbot()
    conversation_chain = ConversationChain(llm=chatbot, memory=memory, verbose=True)

    # Integrate memory into the input
    response = conversation_chain.predict(input=input_text)
    return response