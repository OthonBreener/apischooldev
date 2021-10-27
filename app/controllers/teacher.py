from sqlmodel import Session, select
from app.db import engine
from app.models.teacher import Teacher

def add_teacher(teacher):

    with Session(engine) as session:
        session.add(teacher)
        session.commit()
        session.refresh(teacher)

def read_teacher():

    with Session(engine) as session:
        statement = select(Teacher)
        results = session.exec(statement)

    return results.all()
