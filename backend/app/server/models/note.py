from enum import Enum
from typing import Optional, List

from beanie import Document
from pydantic import BaseModel


class TagColors(str, Enum):
    RED = "RED"
    BLUE = "BLUE"
    GREEN = "GREEN"


class Tag(BaseModel):
    name: str
    color: TagColors = TagColors.BLUE


class Note(Document):  # This is the document structure
    title: str
    text: Optional[str]
    tag_list: List[Tag] = []