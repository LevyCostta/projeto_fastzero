import pytest
from fastapi.testclient import TestClient

from projeto_fastzero.app import app


@pytest.fixture
def client():
    return TestClient(app)
