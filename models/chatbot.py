from langchain_community.chat_models import BedrockChat
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

class Chatbot:
    def __init__(self,credentials_profile_name='default', model_id='anthropic.claude-3-haiku-20240307-v1:0'):
        self.llm = BedrockChat(
        credentials_profile_name=credentials_profile_name,
        model_id=model_id,
    )
        
    def set_memory(self):
        memory = ConversationBufferMemory(
            memory_key='history',
            input_key='input'
        )
        return memory
    
    def get_conversation(self,input_text, memory):
        llm_conversation = ConversationChain(llm=self.llm, memory=memory, verbose=True)
        chat_replay = llm_conversation.predict(input=input_text)
        return chat_replay
