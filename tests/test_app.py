from http import HTTPStatus

from fastapi.testclient import TestClient

from projeto_fastzero.app import app

client = TestClient(app)


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (ORGANIZAÇÃO)

    response = client.get('/')  # Act (AÇÃO)

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}
