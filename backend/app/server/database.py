from pymongo import MongoClient
import os
# import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
# from app.server.models import todolist
# from beanie import init_beanie

def connect_mongodb():
    host=os.environ.get('MONGODB_HOST')
    port=int(os.environ.get('MONGODB_PORT'))
    username=os.environ.get('MONGODB_USER')
    password=os.environ.get('MONGODB_PASSWORD')
    db_name=os.environ.get('MONGODB_DB')
    # uri = os.environ.get('MONGO_URI')
    
    
    # client = AsyncIOMotorClient(
    #     "mongodb://mongouser:mongopassword@mongodb:27017"
    # )
    
    # await init_beanie(database=client.app,document_models=[todolist.ToDoList])
    
    client = MongoClient(
        host=host,
        port=port,
        username=username,
        password=password
    )
    
    db = client[db_name]
    return db

db =connect_mongodb()
collection = db.todolist

# async def fetch_all_todolist():
#     todolists = []
#     cursor = collection.find()
#     async for document in cursor:
#         todolists.append(todolist.ToDoList(**document))
#     return todolists