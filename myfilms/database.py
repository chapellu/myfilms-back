class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    instance = None
    films = []

    async def get_films(self, page: int = 1):
        bottom = 5 * (page - 1)
        top = 5 * page
        return {"films": self.films[bottom:top], "length": len(self.films)}
