FROM python:latest

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    #
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.1.13

# Install poetry
RUN pip install "poetry==$POETRY_VERSION"

# Copy backend stuff
WORKDIR /elta
COPY ./backend/ /elta/

# Install dependencies
RUN poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi

# Migrations
RUN python manage.py makemigrations \
    && python manage.py migrate \
