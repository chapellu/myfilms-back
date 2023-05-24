import logging

import uvicorn
from fastapi import FastAPI, status

from myfilms.config import Config
from myfilms.database import Database
from myfilms.models import FilmsModel

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


if __name__ == "__main__":
    try:
        uvicorn.run("main:app", host="0.0.0.0", port=8000)
    except Exception as e:
        logging.exception(e, exc_info=True)
