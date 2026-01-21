#!/bin/bash
set -e

echo "===== After Install Hook ====="

cd /home/ec2-user/movie_finder

# Fetch environment variables from AWS Systems Manager Parameter Store
echo "📥 Fetching environment variables from Parameter Store..."

PARAM_PREFIX="/movie-finder/production"

# Try to get AWS region from instance metadata, fallback to default
if [ -z "$AWS_REGION" ]; then
    AWS_REGION=$(curl -s http://169.254.169.254/latest/meta-data/placement/region 2>/dev/null || echo "eu-central-1")
fi

echo "🌍 Using AWS region: ${AWS_REGION}"

# Configure AWS credentials if not already set
# Lightsail instances don't support IAM roles, so we need to use IAM user credentials
if [ ! -f /home/ec2-user/.aws/credentials ]; then
    echo "⚠️  AWS credentials not found. Please configure them manually:"
    echo "   mkdir -p /home/ec2-user/.aws"
    echo "   aws configure --profile default"
    echo "   Or set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY environment variables"
    echo ""
    echo "   Using IAM user: lightsail-parameter-store-reader"
    echo "   This user has minimal permissions (only Parameter Store read access)"
fi

# Create .env file
echo "📝 Creating .env file..."

# Fetch all parameters and create .env
aws ssm get-parameters-by-path \
    --path "${PARAM_PREFIX}" \
    --with-decryption \
    --region "${AWS_REGION}" \
    --query 'Parameters[*].[Name,Value]' \
    --output text | while IFS=$'\t' read -r name value; do
    
    # Extract parameter name (remove prefix)
    param_name=$(echo "$name" | sed "s|${PARAM_PREFIX}/||")
    
    # Write to .env file
    echo "${param_name}=${value}" >> .env
done

# Check if .env was created successfully
if [ ! -f .env ]; then
    echo "❌ Error: Failed to create .env file!"
    echo "   Checking for backup..."
    
    if [ -f /home/ec2-user/.env.backup ]; then
        echo "📦 Restoring .env from backup..."
        cp /home/ec2-user/.env.backup .env
    else
        echo "❌ No backup found! Deployment cannot continue."
        exit 1
    fi
fi

echo "✅ .env file created successfully"

# Ensure proper permissions
echo "Setting permissions..."
chown -R ec2-user:ec2-user /home/ec2-user/movie_finder
chmod 600 .env

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
