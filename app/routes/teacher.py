from fastapi import APIRouter

router = APIRouter(
    prefix="/teachers",
    tags=['teachers'],
    responses={404: {"description": "Not Found"}},
)
