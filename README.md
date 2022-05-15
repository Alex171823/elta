# Elta project

## Running using [docker](https://www.docker.com/) + [docker-compose](https://docs.docker.com/compose/)

In your projects directory:

```bash
git clone https://github.com/Alex171823/elta.git
cd elta
docker-compose up
```

To rebuild image:

```bash
docker-compose up --build
```

## Running only backend without docker

This requres [poetry](https://python-poetry.org/) + [python3](https://www.python.org/) + pip being installed on your computer

```bash
git clone https://github.com/Alex171823/elta.git
cd elta/backend

# create and activate .venv in backend directory
poetry shell
# install dependencies
poetry install
# run server
python3 manage.py runserver
```
