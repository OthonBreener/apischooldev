from sqlmodel import create_engine

postgre_url = "postgresql://postgres:senha@localhost:5432/postgres"

engine = create_engine(postgre_url, echo=True)