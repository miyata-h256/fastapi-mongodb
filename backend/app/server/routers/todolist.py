from fastapi import APIRouter,Body

from bson.objectid import ObjectId
from bson.json_util import dumps,loads

from app.server.database import db

router = APIRouter(
    prefix='/todolist',
    tags=['todolist']
)

@router.post('')
def create_post(body=Body(...)):
    post = body['payload']
    db.todolist.insert_one(post)
    return {'post':'ok'}

@router.get('')
def read_post():
    """postの取得

    ----------
    Parameters:

    なし
    """
    db_todolist = db.todolist.find_one()
    return {'Today\'s Task': dumps(db_todolist)}

@router.get('/all')
def read_all():
    db_all = db.todolist.find()
    return dumps(db_all)

@router.get('/{id}')
def get_todolist_by_id(id: int):
    return {"id": f"blog number is {id}"}

@router.put('')
def update_post(body=Body(...)):
    """postの更新(id)

    ----------
    Parameters:

    body: body
        任意のjson
    """
    post = body['payload']
    _id = post['_id']
    list = post['list']
    regist_date = post['regist_date']
    db.todolist.update_one(
        {'_id': ObjectId(_id)},
        {'$set':
            {
                "list": list, 'regist_date': regist_date
            }
        }
    )
    return {'update': "ok"}

@router.delete('/')
def delete_post_by_id(id: str):
    """postの削除(id)

    ----------
    Parameters:

    id: str
        オブジェクトID
    """
    db.todolist.delete_one(
        {'_id': ObjectId(id)}
    )
    return {'delete': "ok"}    
