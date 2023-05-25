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
        "grade": 4.5
    }
