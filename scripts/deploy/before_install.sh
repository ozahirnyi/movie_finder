#!/bin/bash
set -e

echo "===== Before Install Hook ====="

# Stop running containers (if any)
if [ -f /home/ec2-user/movie_finder/docker-compose.lightsail.yml ]; then
    echo "Stopping existing containers..."
    cd /home/ec2-user/movie_finder
    docker compose -f docker-compose.lightsail.yml down || true
fi

# Clean up old deployment directory (CodeDeploy will create fresh one)
echo "Cleaning up old deployment..."
rm -rf /home/ec2-user/movie_finder/*

echo "Before Install completed successfully"
