from pydantic import BaseModel
from beanie import Document

class ToDoKind(BaseModel):
    kind: str
    detail: str
    
    class Setting:
        name="todoKind"