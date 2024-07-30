# Data access layer for user messages
# from pymongo import MongoClient


# class MessageDAO:
#     def __init__(self, connection_string):
#         self.client = MongoClient(connection_string)
#         self.db = self.client['chatbot']
#         self.collection = self.db['messages']

#     def get_messages(self, user_id):
#         return self.collection.find({"user_id": user_id})

#     def save_message(self, message):
#         self.collection.insert_one(message)
