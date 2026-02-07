#!/bin/bash
# Don't use set -e here - we want to handle errors gracefully
set +e

echo "===== Application Stop Hook ====="

# Check if CodeDeploy agent is running
if ! sudo service codedeploy-agent status > /dev/null 2>&1; then
    echo "⚠️  CodeDeploy agent is not running. Attempting to start..."
    sudo service codedeploy-agent start || true
    sleep 2
fi

# Stop running containers (if any)
if [ -f /home/ec2-user/movie_finder/docker-compose.lightsail.yml ]; then
    echo "Stopping existing containers..."
    cd /home/ec2-user/movie_finder
    if [ -f docker-compose.monitoring.yml ]; then
      docker-compose -f docker-compose.lightsail.yml -f docker-compose.monitoring.yml down || true
    else
      docker-compose -f docker-compose.lightsail.yml down || true
    fi
    echo "✅ Containers stopped"
else
    echo "ℹ️  No docker-compose.lightsail.yml found, skipping container stop"
fi

echo "Application Stop completed successfully"
exit 0
