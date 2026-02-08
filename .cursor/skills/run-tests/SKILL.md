---
name: run-tests
description: How to run the test suite (pytest) and lint in the Movie Finder project. Use when the user asks to run tests, run lint, or how to run tests locally.
---

# Run tests locally

## Prerequisites

- **Postgres**: Docker Compose DB must be running (`docker compose up -d` so that Postgres is on `localhost:5433`).
- **Dependencies**: `poetry install` must have been run (project uses Poetry).

## Environment variables (DB)

Set before running tests so Django connects to the local Postgres:

```powershell
$env:DB_HOST = "localhost"
$env:DB_PORT = "5433"
$env:DB_USER = "postgres"
$env:DB_PASSWORD = "postgres"
$env:DB_NAME = "postgres"
```

## Running tests

### When Poetry is in PATH

```powershell
cd o:\projects\movie_finder
poetry run pytest
```

Or via Makefile: `make test`.

### When Poetry is not in PATH (e.g. some IDE shells)

Use the full path to Poetry (typical Windows install):

```powershell
cd o:\projects\movie_finder
$env:DB_HOST="localhost"; $env:DB_PORT="5433"; $env:DB_USER="postgres"; $env:DB_PASSWORD="postgres"; $env:DB_NAME="postgres"
& "$env:APPDATA\pypoetry\venv\Scripts\poetry.exe" run pytest -q
```

### Via project script

If Poetry is in PATH:

```powershell
.\scripts\run-tests-local.ps1
```

This sets the DB env vars and runs `poetry run coverage run -m pytest` then `coverage report --fail-under=100`.

## Lint and format

- Lint: `poetry run ruff check .` (or `make lint`)
- Format: `poetry run ruff format .` (or `make format`)

With Poetry not in PATH:

```powershell
& "$env:APPDATA\pypoetry\venv\Scripts\poetry.exe" run ruff check .
& "$env:APPDATA\pypoetry\venv\Scripts\poetry.exe" run ruff format .
```

## Full check (lint + tests, like pre-commit)

```powershell
pre-commit run --all-files
```

If pre-commit is not in PATH, run lint and tests separately as above. The project enforces 100% coverage; use `poetry run coverage run -m pytest` then `poetry run coverage report -m --fail-under=100` to verify.
