from fastapi import FastAPI
from sqlmodel import SQLModel

from app.db import engine
from app.routes import students

app = FastAPI()
app.include_router(students.router)

SQLModel.metadata.create_all(engine)
