# Orchestrates different components to provide chat service
# from models.chatbot import Chatbot
# from daos.user_dao import UserDAO
# from daos.message_dao import MessageDAO


# class ChatService:
#     def __init__(self, connection_string):
#         self.user_dao = UserDAO(connection_string)
#         self.message_dao = MessageDAO(connection_string)

#     def get_chatbot_for_user(self, user_id):
#         user_data = self.user_dao.get_user(user_id)
#         if not user_data:
#             raise ValueError("User not found")
#         chatbot = Chatbot()
#         return chatbot
