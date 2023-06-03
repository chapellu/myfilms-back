from fastapi.testclient import TestClient
import pytest
from myfilms.database import Database
from myfilms.main import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def clean_database():
    Database().films = []
    Database().actors = []
    Database().reviews = []
