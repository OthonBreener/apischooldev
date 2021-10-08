from fastapi import APIRouter

router = APIRouter()

@router.get("/students")
async def read_students():
    ...

@router.get("/students/{id}")
async def read_one_student():
    ...

@router.post("/students"):
async def add_students():
    ...
