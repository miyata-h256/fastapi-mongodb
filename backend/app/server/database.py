import os
from motor.motor_asyncio import AsyncIOMotorClient
from app.server.models.todolist import ToDoList
from app.server.models.note import Note
from beanie import init_beanie

uri = os.environ.get("MONGO_URI")

async def init_db():
    client = AsyncIOMotorClient(uri)
    
    await init_beanie(database=client.app,document_models=[ToDoList,Note])