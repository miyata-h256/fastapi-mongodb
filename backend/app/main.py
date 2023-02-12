import uvicorn
from fastapi import FastAPI
from app.server.routers import todolist
from app.server.routers import todokind
from app.server.routers import note
from app.server.database import init_db


app = FastAPI(prefix="/")

app.include_router(todolist.router)
app.include_router(todokind.router)
app.include_router(note.router)

@app.on_event("startup")
async def start_db():
    await init_db()

@app.get("/",tags=["Root"])
async def root():
    return {"message":"Welcome to this fastapi!"}

if __name__ == '__main__':
    uvicorn.run(app,host="0.0.0.0",port=8000)

