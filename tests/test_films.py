from myfilms.database import Database
from tests.data import films


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
    assert response.json() == {
        "length": 1,
        "films": [{
            "id": 1,
            "title": "Titanic",
            "description": "A story of a boat and its love for icecream"
        }]
    }


def test__get_films__when_more_than_5_films__return_only_5(client):
    # Given
    Database().films = films

    # When
    response = client.get("/")

    # Then
    assert response.status_code == 200
    assert response.json() == {
        "length":
            6,
        "films": [{
            "id": 1,
            "title": "Titanic",
            "description": "A story of a boat and its love for icecream",
        }, {
            "id": 2,
            "title": "Dragon",
            "description": "Un boiteux et son chat noir volant",
        }, {
            "id": 3,
            "title": "Joker",
            "description": "Biographie d'un schizophrène en chasse d'une chauve-souris",
        }, {
            "id": 4,
            "title": "Your name",
            "description": "Des enfants qui ne veulent pas voir le feu d'artifice",
        }, {
            "id": 5,
            "title": "Le prestige",
            "description": "c'est l'histoire de 2 magiciens",
        }]
    }


def test__get_films__when_more_than_5_films_and_second_page__ok(client):
    # Given
    Database().films = films

    # When
    response = client.get("/?page=2")

    # Then
    assert response.status_code == 200
    assert response.json() == {
        "length": 6,
        "films": [{
            "id": 6,
            "title": "Le grand bleu",
            "description": "3h de bloup bloup",
        }]
    }
