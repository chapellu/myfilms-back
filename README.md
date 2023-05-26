# myfilms-back

The goal of this project is to create a simple website to list films and their review. 
The first page is going to be a simple table with films name with a total of 5 rows per page.

When you click on a film you can access it's description, the actors casted as well as the rating as stars.
Everybody can edit the descriptions, list of actors as well as give his feedback


# Development

## Installing package
```
python -m venv .venv
source .venv/bin/activate
poetry install
```

## Running the server
```
poetry run dev
```

Access the swagger
http://0.0.0.0:8000/docs