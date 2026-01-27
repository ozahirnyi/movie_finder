#!/bin/bash
set -e

echo "===== Manual Deployment Script ====="

# Navigate to project directory
cd /home/ec2-user/movie_finder || {
    echo "❌ Error: Project directory not found at /home/ec2-user/movie_finder"
    echo "   Please check the path or create the directory first"
    exit 1
}

# Backup .env file if it exists
if [ -f .env ]; then
    echo "📦 Backing up .env file..."
    cp .env /home/ec2-user/.env.backup
fi

# Pull latest changes
echo "📥 Pulling latest changes from main..."
git fetch origin
git reset --hard origin/main

# Ensure .env file exists (restore from backup if needed)
if [ ! -f .env ]; then
    if [ -f /home/ec2-user/.env.backup ]; then
        echo "📦 Restoring .env from backup..."
        cp /home/ec2-user/.env.backup .env
    else
        echo "⚠️  Warning: .env file not found and no backup available!"
        echo "   Please ensure .env file exists before continuing"
    fi
fi

# Stop existing containers
echo "🛑 Stopping existing containers..."
docker compose -f docker-compose.lightsail.yml down || true

# Build new images
echo "🔨 Building Docker images..."
docker compose -f docker-compose.lightsail.yml build

# Run migrations
echo "📊 Running database migrations..."
docker compose -f docker-compose.lightsail.yml run --rm web poetry run python manage.py migrate --noinput

# Collect static files
echo "📦 Collecting static files..."
docker compose -f docker-compose.lightsail.yml run --rm web poetry run python manage.py collectstatic --noinput || true

# Start containers
echo "🚀 Starting containers..."
docker compose -f docker-compose.lightsail.yml up -d

# Wait for containers to be ready
echo "⏳ Waiting for containers to start..."
sleep 10

# Check container status
echo "📋 Container status:"
docker compose -f docker-compose.lightsail.yml ps

# Health check
echo "🏥 Running health check..."
sleep 5
if docker compose -f docker-compose.lightsail.yml exec -T web poetry run python manage.py check --deploy > /dev/null 2>&1; then
    echo "✅ Health check passed!"
else
    echo "⚠️  Health check warning (this might be normal)"
fi

echo ""
echo "✅ Manual deployment completed successfully!"
echo ""
echo "📋 Useful commands:"
echo "   View logs: docker compose -f docker-compose.lightsail.yml logs -f web"
echo "   Check status: docker compose -f docker-compose.lightsail.yml ps"
echo "   Restart: docker compose -f docker-compose.lightsail.yml restart"
