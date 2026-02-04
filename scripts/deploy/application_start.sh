#!/bin/bash
set -e

echo "===== Application Start Hook ====="

cd /home/ec2-user/movie_finder

# Start Docker containers (app + optional monitoring)
echo "Starting Docker containers..."
if [ -f docker-compose.monitoring.yml ]; then
  docker compose -f docker-compose.lightsail.yml -f docker-compose.monitoring.yml up -d
else
  docker compose -f docker-compose.lightsail.yml up -d
fi

# Wait for containers to be ready
echo "Waiting for containers to start..."
sleep 10

# Check container status
echo "Checking container status..."
if [ -f docker-compose.monitoring.yml ]; then
  docker compose -f docker-compose.lightsail.yml -f docker-compose.monitoring.yml ps
else
  docker compose -f docker-compose.lightsail.yml ps
fi

echo "Application Start completed successfully"
