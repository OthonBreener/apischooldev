from fastapi import APIRouter, HTTPException

from app.controllers.students import add_student
from app.models.students import Student

router = APIRouter(
    prefix="/students",
    tags=['students'],
    responses={404: {"description": "Not Found"}},
)


@router.get("/")
async def read_students():
    return {"student": "Igor"}


@router.get("/{id}")
async def read_one_student(id: int):
    items = [1]
    if id not in items:
        raise HTTPException(status_code=404, detail="Id não encontrado")

    return {"id": "Ok"}


@router.post("/", response_model=Student)
def add_students_routes(student: Student):
    params_copy = student.copy()
    add_student(student)
    return params_copy
