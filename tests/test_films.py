from myfilms.database import Database
from tests.films import films


def test__get_films___when_no_film__ok(client):
    # Given

    # When
    response = client.get("/")

    # Then
    assert response.status_code == 200
    assert response.json() == {"length": 0, "films": []}


def test__get_films__when_less_than_5_films__ok(client):
    # Given
    Database().films = films[:1]

    # When
    response = client.get("/")

    # Then
    assert response.status_code == 200
    assert response.json() == {"length": 1, "films": films[:1]}


def test__get_films__when_more_than_5_films__return_only_5(client):
    # Given

    Database().films = films

    # When
    response = client.get("/")

    # Then
    assert response.status_code == 200
    assert response.json() == {"length": 6, "films": films[:5]}


def test__get_films__when_more_than_5_films_and_second_page__ok(client):
    # Given
    Database().films = films

    # When
    response = client.get("/?page=2")

    # Then
    assert response.status_code == 200
    assert response.json() == {"length": 6, "films": films[5:10]}
