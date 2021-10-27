SRC_DIRS := app

docker: down build up logs

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down --remove-orphans

logs:
	docker-compose logs --follow api

test:
	coverage run --source=$(SRC_DIRS) --module ward
	coverage report
	coverage html

install:
	pip install -U pip
	pip install poetry
	poetry install
	poetry run pre-commit install

format:
	isort $(SRC_DIRS)
	black $(SRC_DIRS)

check:
	isort --check --diff $(SRC_DIRS)
	black $(SRC_DIRS) --check
	flake8 $(SRC_DIRS)
