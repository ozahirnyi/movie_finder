#!/bin/sh
set -e

poetry run python manage.py migrate --noinput

exec poetry run gunicorn movie_finder_django.asgi:application -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:${PORT:-8000}
