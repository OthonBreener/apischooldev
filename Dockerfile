FROM python:3.10.0-buster

RUN pip install poetry

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

RUN poetry config virtualenvs.create false
RUN poetry install

WORKDIR /code

COPY . .
