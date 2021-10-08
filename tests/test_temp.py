from starlette.testclient import TestClient
from ward import fixture, test

from app.main import app


@fixture
def client():
    return TestClient(app)


@test('Teste temporário')
def _(client=client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensagem":"Olá Pessoas"}
