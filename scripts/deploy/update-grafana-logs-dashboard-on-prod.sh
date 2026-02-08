#!/usr/bin/env bash
# Copy Movie Finder Logs dashboard to prod and restart Grafana.
# Run from project root. Requires SSH key and access to the instance.
#
# Usage: ./scripts/deploy/update-grafana-logs-dashboard-on-prod.sh [KEY_PATH] [HOST]
# Example: ./scripts/deploy/update-grafana-logs-dashboard-on-prod.sh
#          ./scripts/deploy/update-grafana-logs-dashboard-on-prod.sh ./LightsailDefaultKey-eu-central-1.pem 3.75.113.52

set -e

KEY="${1:-./LightsailDefaultKey-eu-central-1.pem}"
HOST="${2:-3.75.113.52}"
USER="ec2-user"
DASHBOARD_JSON="monitoring/grafana/provisioning/dashboards/json/movie-finder-logs.json"
REMOTE_DIR="/home/ec2-user/movie_finder"

if [ ! -f "$KEY" ]; then
  echo "Error: Key file not found: $KEY"
  exit 1
fi
if [ ! -f "$DASHBOARD_JSON" ]; then
  echo "Error: Dashboard not found: $DASHBOARD_JSON (run from project root)"
  exit 1
fi

echo "Uploading dashboard to ${USER}@${HOST}..."
scp -i "$KEY" -o StrictHostKeyChecking=no "$DASHBOARD_JSON" "${USER}@${HOST}:/tmp/movie-finder-logs.json"

echo "Installing dashboard and restarting Grafana..."
ssh -i "$KEY" -o StrictHostKeyChecking=accept-new "${USER}@${HOST}" "cd ${REMOTE_DIR} && sed -i '1s/^\xEF\xBB\xBF//' /tmp/movie-finder-logs.json 2>/dev/null; cp /tmp/movie-finder-logs.json monitoring/grafana/provisioning/dashboards/json/movie-finder-logs.json && docker-compose -f docker-compose.lightsail.yml -f docker-compose.monitoring.yml restart grafana && echo Done. Open https://grafana.moviefinder.cc and check folder Movie Finder for 'Movie Finder Logs'."

echo "Done."
