from typing import Optional

from pydantic import validator
from sqlmodel import Field, SQLModel


class Student(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    last_name: str
    age: str
    name_mother: str
    name_father: str

    teacher_id: Optional[int] = Field(default=None, foreign_key="teacher.id")

    @validator('name')
    def name_deve_ter_tamanho_limitado_para_5_caracters(cls, valor):

        if len(valor) > 5:
            raise ValueError("Nome deve ter 5 caracteres")
        return valor

    @validator('name_father', 'name_mother')
    def name_father_and_mother_must_be_bigger_seven_caracter(cls, valor):

        if len(valor) < 7:
            raise ValueError(
                "Nome do pai e da mãe deve ser maior que 7 caracteres"
            )
        return valor
