#!/bin/bash
set -e

echo "===== After Install Hook ====="

cd /home/ec2-user/movie_finder

# Ensure proper permissions
echo "Setting permissions..."
chown -R ec2-user:ec2-user /home/ec2-user/movie_finder

# Build Docker images
echo "Building Docker images..."
docker compose -f docker-compose.lightsail.yml build

# Run database migrations
echo "Running database migrations..."
docker compose -f docker-compose.lightsail.yml run --rm web poetry run python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
docker compose -f docker-compose.lightsail.yml run --rm web poetry run python manage.py collectstatic --noinput

echo "After Install completed successfully"
