from fastapi.testclient import TestClient
import pytest
from myfilms.main import app


@pytest.fixture
def client():
    return TestClient(app)
