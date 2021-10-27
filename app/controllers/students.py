from sqlmodel import Session, select
from sqlmodel import col
from app.db import engine
from app.models.students import Student


class StudentController:

    @staticmethod
    def add_student(student):
        """
        Método que adiciona um novo estudante no banco de dados.
        """
        with Session(engine) as session:
            session.add(student)
            session.commit()

            session.refresh(student)

    @staticmethod
    def read_student():
        """
        Método que faz uma query no banco de dados e retorna os usuários
        cadastrados lá.
        """

        with Session(engine) as session:
            statement = select(Student)
            results = session.exec(statement)

        return results.all()

    @staticmethod
    def read_student_filter_by_id(id):
        """
        Método que faz uma query no banco de dados e retorna os usuários
        cadastrados lá.
        """

        with Session(engine) as session:
            statement = select(Student).where(Student.id == id)
            results = session.exec(statement)

        return results.all()

    @staticmethod
    def read_student_filter_by_name_and_age(name, age):
        """
        Método que faz uma query no banco de dados e retorna os usuários
        cadastrados lá.
        """

        with Session(engine) as session:
            statement = (select(Student).where(Student.name == name).where(Student.age == age))
            results = session.exec(statement)

        return results.all()

    @staticmethod
    def read_student_filter_by_age_more_than(age):
        """
        Método que faz uma query no banco de dados e retorna os usuários
        cadastrados lá.
        """

        with Session(engine) as session:
            statement = select(Student).where(col(Student.age) > int(age))
            results = session.exec(statement)

        return results.all()

    @staticmethod
    def read_student_filter_with_get(id):
        """
        Método que faz uma query no banco de dados e retorna os usuários
        cadastrados lá.
        """

        with Session(engine) as session:
            student = session.get(Student, id)

        return student

    @staticmethod
    def read_student_filter_with_limit():
        """
        Método que faz uma query no banco de dados e retorna os três
        primeiros usuários cadastrados lá.
        """

        with Session(engine) as session:
            statement = select(Student).limit(3)
            results = session.exec(statement)

        return results.all()

    @staticmethod
    def read_student_filter_with_limit_and_offset():
        """
        Método que faz uma query no banco de dados e retorna três
        usuários pulando os três primeiros(pulando com offset).
        """

        with Session(engine) as session:
            statement = select(Student).offset(3).limit(3)
            results = session.exec(statement)

        return results.all()

    @staticmethod
    def update_student(id, data):
        """
        Método que atualiza uma tabela do banco de dados pelo id.
        """
        with Session(engine) as session:
            statement = select(Student).where(Student.id == id)
            results = session.exec(statement)
            student = results.one()
            student.name_father = data
            session.add(student)
            session.commit()
            session.refresh(student)

        return student

    @staticmethod
    def delete_student(id):

        with Session(engine) as session:
            statement = select(Student).where(Student.id == id)
            results = session.exec(statement)
            student = results.one()
            session.delete(student)
            session.commit()

        return "Student deleted successfully!"
