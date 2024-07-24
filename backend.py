import json
from pathlib import Path
from langchain_community.chat_models import BedrockChat
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

def load_json_data(file_path):
    # Load JSON data using the built-in json module
    with open(file_path, 'r') as file:
        return json.load(file)

def demo_chatbot():
    demo_llm = BedrockChat(
        credentials_profile_name='default',
        model_id='anthropic.claude-3-haiku-20240307-v1:0',
    )
    return demo_llm

def demo_memory():
    memory = ConversationBufferMemory(
        memory_key='history',
        input_key='input'
    )
    return memory

def demo_conversation(input_text, memory):
    llm_chain_data = demo_chatbot()
    llm_conversation = ConversationChain(llm=llm_chain_data, memory=memory, verbose=True)

    # Load JSON data
    json_data = load_json_data('personal_information.json')
    json_content = json.dumps(json_data)  # Convert JSON data to string

    # Integrate JSON data into the input
    input_with_data = f"{input_text}\n\nHere is some personal information to use in your response: {json_content}"

    chat_replay = llm_conversation.predict(input=input_with_data)
    return chat_replay

if __name__ == "__main__":
    memory = demo_memory()
