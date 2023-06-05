# myfilms-back

The goal of this project is to create a simple website to list films and their review. 
The first page is going to be a simple table with films name with a total of 5 rows per page.

When you click on a film you can access it's description, the actors casted as well as the rating as stars.
Everybody can edit the descriptions, list of actors as well as give his feedback


## Development

### Installing package

```shell
python -m venv .venv
source .venv/bin/activate
poetry install
```

### Running the server

```shell
poetry run dev
```

Access the swagger
http://0.0.0.0:8000/docs

## Docker

### Building the docker image

```shell
docker build -t myfilms-back:alpha -f deploy/Dockerfile .
```

### Running the docker image

```shell
docker run -p 8000:8000 --name myfilms-back myfilms-back:alpha
```

## Docker compose

Before being able to run the docker compose you will need to build the docker for the two projets: myfilms-front and myfilms-back

```shell
docker-compose -f deploy/docker-compose.yml up
```
