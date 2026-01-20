#!/bin/bash
set -e

echo "===== Application Start Hook ====="

cd /home/ec2-user/movie_finder

# Start Docker containers
echo "Starting Docker containers..."
docker compose -f docker-compose.lightsail.yml up -d

# Wait for containers to be ready
echo "Waiting for containers to start..."
sleep 10

# Check container status
echo "Checking container status..."
docker compose -f docker-compose.lightsail.yml ps

echo "Application Start completed successfully"
