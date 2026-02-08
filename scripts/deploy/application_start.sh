#!/bin/bash
set -e

echo "===== Application Start Hook ====="

cd /home/ec2-user/movie_finder

# Start only app + db (no Grafana/observability stack — 512 MB instance would freeze).
# Logs are written to Docker; use: docker-compose -f docker-compose.lightsail.yml logs --tail=200 web
echo "Starting Docker containers (backend only, no monitoring)..."
docker-compose -f docker-compose.lightsail.yml -f docker-compose.monitoring.yml down 2>/dev/null || true
docker-compose -f docker-compose.lightsail.yml up -d

# Wait for containers to be ready
echo "Waiting for containers to start..."
sleep 10

echo "Checking container status..."
docker-compose -f docker-compose.lightsail.yml ps

echo "Application Start completed successfully"
