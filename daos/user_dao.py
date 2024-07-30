# Data access layer for user data
# from pymongo import MongoClient


# class UserDAO:
#     def __init__(self, connection_string):
#         self.client = MongoClient(connection_string)
#         self.db = self.client['chatbot']
#         self.collection = self.db['users']

#     def get_user(self, user_id):
#         return self.collection.find_one({"user_id": user_id})

#     def save_user(self, user):
#         self.collection.insert_one(user.__dict__)
