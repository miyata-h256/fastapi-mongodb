from typing import Optional,List
from pydantic import BaseModel,Field
from beanie import Document,Link,Indexed,init_beanie


class Task(BaseModel):
    title: str = ""
    completed: bool = Field(default=False)
    changed: bool = Field(default=False)

class ToDoList(Document):
    regist_date: str = Field(default=None)
    list: Optional[List[Task]] = []
    
    class Settings:
        name = "todolist"

