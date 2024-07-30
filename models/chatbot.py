# Chatbot class with model and memory management

from langchain_community.chat_models import BedrockChat
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain


class Chatbot:
    def __init__(self, credentials_profile_name='default', model_id='anthropic.claude-3-haiku-20240307-v1:0'):
        self.llm = BedrockChat(
            credentials_profile_name=credentials_profile_name,
            model_id=model_id,
        )
        self.memory = self.initialize_context()

    def initialize_context(self):
        memory = ConversationBufferMemory(
            memory_key='history',
            input_key='input',
            human_prefix="User",
            ai_prefix="Bot"
        )

        personal_info_text = (
            f"Here is some information about me: "
            f"My name is Facundo, "
            f"I am 37 years old, "
            f"and I live at Copenhagen."
        )

        memory.save_context({"input": f"Here is my personal information. {personal_info_text}, keep your answers short and to the point"}, {"output": "I'll remember that."})
        return memory

    def update_memory(self, input_text, output_text):
        self.memory.save_context({"input": input_text}, {"output": output_text})

    def generate_response(self, input_text):
        llm_conversation = ConversationChain(llm=self.llm, memory=self.memory, verbose=True)
        chat_replay = llm_conversation.predict(input=input_text)
        self.update_memory(input_text, chat_replay)
        return chat_replay
