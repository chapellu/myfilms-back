from myfilms.models import FilmDetailsModel, FilmUpdateModel, FilmsModel
from statistics import mean


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    instance = None
    films = []
    actors = []
    reviews = []

    async def get_films(self, page: int = 1) -> FilmsModel:
        bottom = 5 * (page - 1)
        top = 5 * page
        return {"films": self.films[bottom:top], "length": len(self.films)}

    async def get_film(self, film_id: int) -> FilmDetailsModel:
        film = list(filter(lambda film: film["id"] == film_id, self.films))[0]
        actors = list(filter(lambda actor: actor["id"] in film["actors"], self.actors))
        reviews = list(filter(lambda grade: grade["movie"] == film["id"], self.reviews))

        return {
            "id": film["id"],
            "title": film["title"],
            "description": film["description"],
            "actors": actors,
            "grade": round(mean(map(lambda grade: grade["grade"], reviews)), 1)
        }

    async def put_film(self, movie_id: int, update: FilmUpdateModel):
        film = next(filter(lambda film: film["id"] == movie_id, self.films))
        if update.description:
            film["description"] = update.description
        if update.actors:
            film["actors"] = [actor.id for actor in update.actors]
        if update.grade:
            self.reviews.append({"id": len(self.reviews), "grade": update.grade, "movie": movie_id})
