#!/bin/bash
set -e

echo "===== Validate Service Hook ====="

cd /home/ec2-user/movie_finder

# Use same compose set as application_start.sh
COMPOSE_FILES="-f docker-compose.lightsail.yml"
if [ -f docker-compose.monitoring.yml ]; then
  COMPOSE_FILES="-f docker-compose.lightsail.yml -f docker-compose.monitoring.yml"
fi

# Check if main app containers (web, db) are running
echo "Validating Docker containers..."
if ! docker-compose $COMPOSE_FILES ps | grep -q "Up"; then
    echo "ERROR: Containers are not running!"
    exit 1
fi

# Wait a bit for application to be fully ready
echo "Waiting for application to be ready..."
sleep 5

# Health check - try to connect to the application
echo "Running health check..."
MAX_RETRIES=10
RETRY_COUNT=0

while [ $RETRY_COUNT -lt $MAX_RETRIES ]; do
    if curl -f http://localhost:80 > /dev/null 2>&1; then
        echo "✅ Health check passed! Application is responding."
        exit 0
    fi
    
    RETRY_COUNT=$((RETRY_COUNT + 1))
    echo "Health check attempt $RETRY_COUNT/$MAX_RETRIES failed, retrying in 3 seconds..."
    sleep 3
done

echo "❌ Health check failed after $MAX_RETRIES attempts"
echo "Container logs:"
docker-compose $COMPOSE_FILES logs --tail=50 web
exit 1
