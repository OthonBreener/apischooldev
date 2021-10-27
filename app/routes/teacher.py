from fastapi import APIRouter
from app.controllers.teacher import *
from app.models.teacher import Teacher

router = APIRouter(
    prefix="/teachers",
    tags=['Teachers'],
    responses={404: {"description": "Not Found"}},
)

@router.post("/", response_model=Teacher)
async def add_new_teacher(teacher: Teacher):
    add_teacher(teacher)
    return teacher

@router.get("/")
async def route_read_teacher():
    return read_teacher()
