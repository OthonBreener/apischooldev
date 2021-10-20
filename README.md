## Iniciando o projeto
* Criando o ambiente virtual
1. virtualenv -p python3 venv

## Como rodar o projeto

* pip install fastapi[all]

1. uvicorn app.main:app --reload
2. No navegador: localhost/docs
3. Banco postgresql usado localmente:
```sh
docker run --name database_postgre -e POSTGRES_PASSWORD=senha -p 5432:5432 -d postgres:14
```
## Utilizando o pre-commit

1.
```sh
pre-commit install
```

2.
```sh
git add .
```

3.
```sh
git commit -m "algum commit"
```
