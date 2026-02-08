# Copy Movie Finder Logs dashboard to prod and restart Grafana.
# Run from project root. Requires SSH key and access to the instance.
#
# Usage: .\scripts\deploy\update-grafana-logs-dashboard-on-prod.ps1
#        .\scripts\deploy\update-grafana-logs-dashboard-on-prod.ps1 -KeyPath ".\LightsailDefaultKey-eu-central-1.pem" -Host "3.75.113.52"

param(
    [string]$KeyPath = ".\LightsailDefaultKey-eu-central-1.pem",
    [string]$TargetHost = "3.75.113.52"
)

$ErrorActionPreference = "Stop"
$User = "ec2-user"
$DashboardJson = "monitoring\grafana\provisioning\dashboards\json\movie-finder-logs.json"
$RemoteDir = "/home/ec2-user/movie_finder"

if (-not (Test-Path $KeyPath)) {
    Write-Error "Key file not found: $KeyPath"
    exit 1
}
if (-not (Test-Path $DashboardJson)) {
    Write-Error "Dashboard not found: $DashboardJson (run from project root)"
    exit 1
}

Write-Host "Uploading dashboard to ${User}@${TargetHost}..."
scp -i $KeyPath -o StrictHostKeyChecking=no $DashboardJson "${User}@${TargetHost}:/tmp/movie-finder-logs.json"

Write-Host "Installing dashboard and restarting Grafana..."
$Commands = @"
cd $RemoteDir && sed -i '1s/^\xEF\xBB\xBF//' /tmp/movie-finder-logs.json 2>/dev/null; cp /tmp/movie-finder-logs.json monitoring/grafana/provisioning/dashboards/json/movie-finder-logs.json && docker-compose -f docker-compose.lightsail.yml -f docker-compose.monitoring.yml restart grafana && echo Done.
"@
ssh -i $KeyPath -o StrictHostKeyChecking=accept-new "${User}@${TargetHost}" $Commands

Write-Host "Done. Open https://grafana.moviefinder.cc and check folder Movie Finder for 'Movie Finder Logs'."
