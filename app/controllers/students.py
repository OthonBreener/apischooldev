from sqlmodel import Session

from app.db import engine


def add_student(student):
    """
    Método que adiciona um novo estudante no banco de dados.
    """
    with Session(engine) as session:
        session.add(student)
        session.commit()
