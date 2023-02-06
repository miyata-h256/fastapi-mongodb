import uvicorn
from fastapi import FastAPI
from app.server.routers import todolist


app = FastAPI(prefix="/")

app.include_router(todolist.router)

@app.get("/")
def root():
    return {"message":"Welcome to this fastapi!"}

if __name__ == '__main__':
    uvicorn.run(app,host="0.0.0.0",port=8000)

