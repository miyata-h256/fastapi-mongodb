from http.client import HTTPException
from fastapi import APIRouter
from beanie import PydanticObjectId
from app.server.models.todolist import ToDoList

router = APIRouter(
    prefix='/todolist',
    tags=['todolist']
)

@router.get('/all',response_description="All ToDoList")
async def read_all() -> ToDoList:
    all_todolist = await ToDoList.find_all().to_list()
    return all_todolist

@router.get('/id/{id}',response_description="One ToDoList")
async def read_one(id: PydanticObjectId) -> ToDoList:
    todolist = await ToDoList.get(id)
    return todolist

@router.get('/date/{regist_date}',response_description="One ToDoList")
async def read_one_by_regist_date(regist_date: str) -> ToDoList:
    todolist = await ToDoList.find_one({"regist_date":regist_date})
    return todolist

@router.post('/',response_description="create todolist")
async def create_todolist(todolist:ToDoList) -> dict:
    await todolist.create()
    return {"message":"success post todolist!!!"}

@router.delete('/delete/{id}',response_description="delete todolist")
async def delete_todolist_by_id(id:PydanticObjectId):
    todolist = await ToDoList.get(id)
    
    if not todolist:
        raise HTTPException(
            status_code=404,
            detail="Review todolist not found!"
        )

    await todolist.delete()
    return {
        "message": "Record deleted successfully"
    }

# @router.put('')
# def update_post(body=Body(...)):
#     """postの更新(id)

#     ----------
#     Parameters:

#     body: body
#         任意のjson
#     """
#     post = body['payload']
#     _id = post['_id']
#     list = post['list']
#     regist_date = post['regist_date']
#     db.todolist.update_one(
#         {'_id': ObjectId(_id)},
#         {'$set':
#             {
#                 "list": list, 'regist_date': regist_date
#             }
#         }
#     )
#     return {'update': "ok"}

