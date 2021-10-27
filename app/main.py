from fastapi import FastAPI
from sqlmodel import SQLModel

from app.db import engine
from app.routes import students, teacher

app = FastAPI()
app.include_router(students.router)
app.include_router(teacher.router)

SQLModel.metadata.create_all(engine)
