#!/bin/bash
set -e

echo "===== Before Install Hook ====="

# Ensure CodeDeploy agent is running
echo "Checking CodeDeploy agent status..."
if ! sudo service codedeploy-agent status > /dev/null 2>&1; then
    echo "⚠️  CodeDeploy agent is not running. Starting agent..."
    sudo service codedeploy-agent start
    sleep 3
    if sudo service codedeploy-agent status > /dev/null 2>&1; then
        echo "✅ CodeDeploy agent started successfully"
    else
        echo "❌ Failed to start CodeDeploy agent. Continuing anyway..."
    fi
else
    echo "✅ CodeDeploy agent is running"
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
fi

# Backup existing .env file (if exists)
if [ -f /home/ec2-user/movie_finder/.env ]; then
    echo "Backing up existing .env file..."
    cp /home/ec2-user/movie_finder/.env /home/ec2-user/.env.backup
fi

# Clean up old deployment directory (CodeDeploy will create fresh one)
echo "Cleaning up old deployment..."
rm -rf /home/ec2-user/movie_finder/*

echo "Before Install completed successfully"
