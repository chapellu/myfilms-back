from myfilms.database import Database
from tests.data import films, actors, reviews


def test__get_film_by_id__with_a_good_id_and_1_review__ok(client):

    # Given
    film_id = 1
    Database().films = films
    Database().actors = actors
    Database().reviews = reviews

    # When
    response = client.get(f"/{film_id}")

    # Then
    assert response.status_code == 200
    assert response.json() == {
        "id": film_id,
        "title": films[0]["title"],
        "description": films[0]["description"],
        "actors": [{
            "id": 1,
            "first_name": "George",
            "last_name": "TuSaisQui"
        }, {
            "id": 3,
            "first_name": "Albert",
            "last_name": "Einstein"
        }],
        "grade": 1
    }


def test__get_film_by_id__with_a_good_id_and_3_reviews__ok(client):

    # Given
    film_id = 2
    Database().films = films
    Database().actors = actors
    Database().reviews = reviews

    # When
    response = client.get(f"/{film_id}")

    # Then
    assert response.status_code == 200
    assert response.json() == {
        "id": film_id,
        "title": films[1]["title"],
        "description": films[1]["description"],
        "actors": [{
            "id": 1,
            "first_name": "George",
            "last_name": "TuSaisQui"
        }, {
            "id": 2,
            "first_name": "David",
            "last_name": "Goodenough"
        }],
        "grade": 4.3
    }


def test__put_film_by_id__when_updating_description__ok(client):
    # Given
    film_id = 1
    Database().films = films

    # When
    response = client.put(f"/{film_id}", json={"description": "An heartbreaking love story"})

    # Then
    assert response.status_code == 202
    assert Database().films[0]["description"] == "An heartbreaking love story"


def test__put_film_by_id__when_updating_authors__ok(client):
    # Given
    film_id = 1
    Database().films = films
    Database().actors = actors

    # When
    response = client.put(f"/{film_id}", json={"actors": [{"id": 2, "first_name": "David", "last_name": "Goodenough"}]})

    # Then
    assert response.status_code == 202
    assert Database().films[0]["actors"] == [2]


def test__put_film_by_id__when_adding_review__ok(client):
    # Given
    film_id = 1
    Database().films = films
    Database().reviews = []

    # When
    response = client.put(f"/{film_id}", json={"grade": 5})

    # Then
    assert response.status_code == 202
    assert {"id": 0, "grade": 5, "movie": film_id} in Database().reviews
