#!/bin/bash
set -e

echo "===== Application Stop Hook ====="

# Stop running containers (if any)
if [ -f /home/ec2-user/movie_finder/docker-compose.lightsail.yml ]; then
    echo "Stopping existing containers..."
    cd /home/ec2-user/movie_finder
    docker compose -f docker-compose.lightsail.yml down || true
    echo "✅ Containers stopped"
else
    echo "ℹ️  No docker-compose.lightsail.yml found, skipping container stop"
fi

echo "Application Stop completed successfully"
