from typing import Optional,List
from pydantic import BaseModel,Field
from beanie import Document
from datetime import datetime,date

today = datetime.today()

class Task(BaseModel):
    title: str = ""
    completed: bool = Field(default=False)
    changed: bool = Field(default=False)

class ToDoList(Document):
    
    regist_date: str = today.strftime("'%Y-%m-%d")
    list: List[Task] = []
    
    class Settings:
        name = "todolist"
        

