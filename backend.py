import os
from langchain_community.chat_models import BedrockChat
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# asd
def demo_chatbot():
    # Instantiate a BedrockChat object with the specified credentials profile and model ID
    demo_llm = BedrockChat(
        credentials_profile_name='default',  # Profile name for AWS credentials
        model_id='anthropic.claude-3-haiku-20240307-v1:0',  # ID of the language model to use
    )
    return demo_llm  # Return the instantiated BedrockChat object


def demo_memory():
    # Instantiate a ConversationBufferMemory object
    memory = ConversationBufferMemory(
        memory_key='history',  # Key to store conversation history
        input_key='input'  # Key for input data
    )
    return memory  # Return the instantiated ConversationBufferMemory object


def demo_conversation(input_text, memory):
    llm_chain_data = demo_chatbot()  # Instantiate a BedrockChat object
    llm_conversation = ConversationChain(llm=llm_chain_data, memory=memory, verbose=True)  # Instantiate a ConversationChain object

    chat_replay = llm_conversation.predict(input=input_text)  # Generate a response to the input text
    return chat_replay


if __name__ == "__main__":
    memory = demo_memory()
