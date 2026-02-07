# Run tests on the host against the local Postgres in Docker.
# Requires: Docker DB running (docker compose up -d), Poetry and deps installed.
# Uses DB_HOST=localhost, DB_PORT=5433 and default postgres/postgres/postgres.
# If your container was created with other POSTGRES_* in .env, set $env:DB_USER etc before sourcing.

$env:DB_HOST = "localhost"
$env:DB_PORT = "5433"
$env:DB_USER = "postgres"
$env:DB_PASSWORD = "postgres"
$env:DB_NAME = "postgres"

Set-Location $PSScriptRoot\..
& poetry run coverage run -m pytest
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& poetry run coverage report -m --fail-under=100
