import logging

import uvicorn
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from myfilms.config import Config
from myfilms.database import Database
from myfilms.models import FilmDetailsModel, FilmUpdateModel, FilmsModel

app = FastAPI(title="My films reviews",
              description=f"A little application to list films and their reviews",
              version=Config.version() or "undefined")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/",
         status_code=status.HTTP_200_OK,
         responses={200: {
             "description": "List of films"
         }},
         response_model=FilmsModel,
         description="Get all films")
async def film_list(page: int = 1):
    return await Database().get_films(page)


@app.get("/{movie_id}",
         status_code=status.HTTP_200_OK,
         responses={200: {
             "description": "Full details of the specific film"
         }},
         response_model=FilmDetailsModel,
         description="Get the full details of the specific film")
async def film(movie_id: int):
    return await Database().get_film(movie_id)


@app.put("/{movie_id}",
         status_code=status.HTTP_202_ACCEPTED,
         responses={202: {
             "description": "Update accepted"
         }},
         description="You can update the description, authors and also add a review to a movie")
async def film(movie_id: int, update: FilmUpdateModel):
    await Database().put_film(movie_id, update)


def main():
    try:
        Database().films = [{
            "id": 1,
            "title": "Titanic",
            "description": "A story of a boat and its love for icecream",
            "actors": [1, 3]
        }, {
            "id": 2,
            "title": "Dragon",
            "description": "Un boiteux et son chat noir volant",
            "actors": [1, 2]
        }, {
            "id": 3,
            "title": "Joker",
            "description": "Biographie d'un schizophrène en chasse d'une chauve-souris",
            "actors": []
        }, {
            "id": 4,
            "title": "Your name",
            "description": "Des enfants qui ne veulent pas voir le feu d'artifice",
            "actors": []
        }, {
            "id": 5,
            "title": "Le prestige",
            "description": "c'est l'histoire de 2 magiciens",
            "actors": []
        }, {
            "id": 6,
            "title": "Le grand bleu",
            "description": "3h de bloup bloup",
            "actors": []
        }]

        Database().actors = [{
            "id": 1,
            "first_name": "George",
            "last_name": "TuSaisQui"
        }, {
            "id": 2,
            "first_name": "David",
            "last_name": "Goodenough"
        }, {
            "id": 3,
            "first_name": "Albert",
            "last_name": "Einstein"
        }]

        Database().reviews = [{
            "id": 1,
            "grade": 1,
            "movie": 1
        }, {
            "id": 2,
            "grade": 4,
            "movie": 2
        }, {
            "id": 3,
            "grade": 5,
            "movie": 2
        }, {
            "id": 4,
            "grade": 4,
            "movie": 2
        }]
        uvicorn.run("myfilms.main:app", host="0.0.0.0", port=8000)
    except Exception as e:
        logging.exception(e, exc_info=True)


if __name__ == "__main__":
    main()
