from fastapi import APIRouter

from app.server.models.todoKind import ToDoKind


router = APIRouter(
    prefix='/todokind',
    tags=['todokind']
)


@router.get('/all',response_description="All ToDoKind")
async def read_all():
    all_todokind = await ToDoKind.find()
    return all_todokind