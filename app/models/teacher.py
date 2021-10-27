from typing import Optional
from sqlmodel import Field, SQLModel

class Teacher(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    last_name: str
    job: str
    age: int 
