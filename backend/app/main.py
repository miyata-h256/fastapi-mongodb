import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.server.routers import todolist
from app.server.routers import todokind
from app.server.routers import note
from app.server.database import init_db


app = FastAPI(prefix="/")

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

