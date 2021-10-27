from fastapi import APIRouter

from app.controllers.students import StudentController
from app.models.students import Student

router = APIRouter(
    prefix="/students",
    tags=['Students'],
    responses={404: {"description": "Not Found"}},
)


@router.get("/")
async def read_students_routes():
    students_all = StudentController.read_student()
    return students_all


@router.get("/{id}", tags=['Id'])
async def read_one_student(id: int):
    student = StudentController.read_student_filter_with_get(id)
    return student


@router.post("/", response_model=Student)
async def add_students_routes(student: Student):
    StudentController.add_student(student)
    return student


@router.put("/", response_model=Student)
async def update_students_routes(id, name_father):
    return StudentController.update_student(id, name_father)


@router.delete("/")
async def delete_students_routes(id):
    return StudentController.delete_student(id)
