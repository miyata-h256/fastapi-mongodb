from fastapi import APIRouter

from app.server.models.note import Note


router = APIRouter(
    prefix='/note',
    tags=['note']
)


@router.get('/all',response_description="All Note")
async def read_all():
    all_note = await Note.find_all().to_list()
    return all_note