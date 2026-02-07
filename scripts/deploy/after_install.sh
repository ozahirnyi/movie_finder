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
if [ ! -f /home/ec2-user/.aws/credentials ] && [ -z "$AWS_ACCESS_KEY_ID" ]; then
    echo "❌ Error: AWS credentials not found!"
    echo "   Please configure them manually:"
    echo "   mkdir -p /home/ec2-user/.aws"
    echo "   aws configure --profile default"
    echo "   Or set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY environment variables"
    echo ""
    echo "   Using IAM user: lightsail-parameter-store-reader"
    echo "   This user has minimal permissions (only Parameter Store read access)"
    echo ""
    echo "   See SETUP_LIGHTSAIL_CREDENTIALS.md for detailed instructions"
    exit 1
fi

# Create .env file
echo "📝 Creating .env file..."

# Fetch all parameters and create .env
# Use a temporary file to capture errors
TEMP_OUTPUT=$(mktemp)
TEMP_ERROR=$(mktemp)

if ! aws ssm get-parameters-by-path \
    --path "${PARAM_PREFIX}" \
    --with-decryption \
    --region "${AWS_REGION}" \
    --query 'Parameters[*].[Name,Value]' \
    --output text > "$TEMP_OUTPUT" 2> "$TEMP_ERROR"; then
    
    echo "❌ Error: Failed to fetch parameters from Parameter Store!"
    cat "$TEMP_ERROR"
    echo ""
    echo "Possible causes:"
    echo "  1. AWS credentials not configured (see SETUP_LIGHTSAIL_CREDENTIALS.md)"
    echo "  2. Parameters not created in Parameter Store (see PARAMETER_STORE_SETUP.md)"
    echo "  3. IAM user doesn't have permissions"
    echo "  4. Wrong AWS region (current: ${AWS_REGION})"
    
    rm -f "$TEMP_OUTPUT" "$TEMP_ERROR"
    exit 1
fi

# Process parameters
if [ -s "$TEMP_OUTPUT" ]; then
    while IFS=$'\t' read -r name value; do
        # Skip empty lines
        [ -z "$name" ] && continue
        
        # Extract parameter name (remove prefix)
        param_name=$(echo "$name" | sed "s|${PARAM_PREFIX}/||")
        
        # For StringList parameters, join values with comma (they come as space-separated)
        # But Parameter Store StringList already returns comma-separated, so just use as-is
        echo "${param_name}=${value}" >> .env
    done < "$TEMP_OUTPUT"
else
    echo "⚠️  Warning: No parameters found in Parameter Store!"
    echo "   Path: ${PARAM_PREFIX}"
    echo "   Region: ${AWS_REGION}"
fi

rm -f "$TEMP_OUTPUT" "$TEMP_ERROR"

# Check if .env was created successfully and is not empty
if [ ! -f .env ] || [ ! -s .env ]; then
    echo "❌ Error: Failed to create .env file or file is empty!"
    echo "   Checking for backup..."
    
    if [ -f /home/ec2-user/.env.backup ] && [ -s /home/ec2-user/.env.backup ]; then
        echo "📦 Restoring .env from backup..."
        cp /home/ec2-user/.env.backup .env
        echo "✅ Restored .env from backup"
    else
        echo "❌ No backup found or backup is empty! Deployment cannot continue."
        echo ""
        echo "Please ensure:"
        echo "  1. AWS credentials are configured (see SETUP_LIGHTSAIL_CREDENTIALS.md)"
        echo "  2. All parameters are created in Parameter Store (see PARAMETER_STORE_SETUP.md)"
        exit 1
    fi
else
    echo "✅ .env file created successfully ($(wc -l < .env) parameters)"
fi

# Ensure proper permissions
echo "Setting permissions..."
chown -R ec2-user:ec2-user /home/ec2-user/movie_finder
chmod 600 .env

# Build Docker images
echo "Building Docker images..."
docker-compose -f docker-compose.lightsail.yml build

# Run database migrations
echo "Running database migrations..."
docker-compose -f docker-compose.lightsail.yml run --rm web poetry run python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
docker-compose -f docker-compose.lightsail.yml run --rm web poetry run python manage.py collectstatic --noinput

echo "After Install completed successfully"
