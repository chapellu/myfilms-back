from pydantic import BaseModel


class FilmModel(BaseModel):
    id: int
    title: str
    description: str


class AuthorModel(BaseModel):
    id: int
    first_name: str
    last_name: str


class FilmsModel(BaseModel):
    length: int
    films: list[FilmModel]


class FilmDetailsModel(FilmModel):
    actors: list[AuthorModel]
    grade: float


class FilmUpdateModel(BaseModel):
    description: str | None = None
    actors: list[AuthorModel] | None = None
    grade: int | None = None
