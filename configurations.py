# Documentation : https://www.mongodb.com/docs/drivers/python-drivers/#introduction

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


# Use this connection string in your application known as database URL Endpoint : 

uri = " { Use this connection string in your application known as database URL Endpoint } "

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# let's create the database and its collection :
db = client.todo_db
collection = db["todo_data"]