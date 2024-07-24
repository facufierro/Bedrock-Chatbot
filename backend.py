import json
from langchain_community.chat_models import BedrockChat
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

def load_json_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def demo_chatbot():
    demo_llm = BedrockChat(
        credentials_profile_name='default',
        model_id='anthropic.claude-3-haiku-20240307-v1:0',
    )
    return demo_llm

def demo_memory():
    # Load JSON data
    json_data = load_json_data('personal_information.json')
    
    # Convert JSON data to a string for memory initialization
    json_content = json.dumps(json_data)

    # Initialize the memory and add the JSON data
    memory = ConversationBufferMemory(
        memory_key='history',
        input_key='input',
        human_prefix="User",
        ai_prefix="Bot"
    )
    
    # Add the personal information to the memory
    memory.save_context({"input": "Here is my personal information."}, {"output": json_content})
    
    return memory

def demo_conversation(input_text, memory):
    llm_chain_data = demo_chatbot()
    llm_conversation = ConversationChain(llm=llm_chain_data, memory=memory, verbose=True)

    # Integrate memory into the input
    chat_replay = llm_conversation.predict(input=input_text)
    return chat_replay

if __name__ == "__main__":
    memory = demo_memory()
