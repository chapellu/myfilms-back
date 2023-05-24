from pydantic import BaseModel


class FilmModel(BaseModel):
    name: str
    description: str


class FilmsModel(BaseModel):
    length: int
    films: list[FilmModel]
