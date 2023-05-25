import logging

import uvicorn
from fastapi import FastAPI, Request, status

from myfilms.config import Config
from myfilms.database import Database
from myfilms.models import FilmDetailsModel, FilmUpdateModel, FilmsModel

app = FastAPI(title="My films reviews",
              description=f"A little application to list films and their reviews",
              version=Config.version() or "undefined")


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


if __name__ == "__main__":
    try:
        uvicorn.run("main:app", host="0.0.0.0", port=8000)
    except Exception as e:
        logging.exception(e, exc_info=True)
