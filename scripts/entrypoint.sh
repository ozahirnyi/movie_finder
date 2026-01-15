#!/bin/sh
set -e

echo "Running migrations..."
poetry run python manage.py migrate --noinput

echo "Collecting static files..."
poetry run python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
exec poetry run gunicorn movie_finder_django.asgi:application -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:${PORT:-8000} --access-logfile - --error-logfile -
