#!/usr/bin/env bash
# Fetch CodeDeploy deployment logs from Lightsail instance.
# Run locally: ./scripts/deploy/fetch-deploy-logs.sh [path-to-key.pem] [instance-ip]
# Example: ./scripts/deploy/fetch-deploy-logs.sh ~/.ssh/LightsailDefaultKey-eu-central-1.pem 3.75.113.52

set -e

KEY="${1:-LightsailDefaultKey-eu-central-1.pem}"
IP="${2:-3.75.113.52}"
USER="ec2-user"

echo "Connecting to ${USER}@${IP} (key: ${KEY})..."
echo "=== Last 250 lines of CodeDeploy agent deployment log ==="
ssh -i "$KEY" -o StrictHostKeyChecking=accept-new "${USER}@${IP}" \
  'sudo tail -250 /var/log/aws/codedeploy-agent/codedeploy-agent.log'
