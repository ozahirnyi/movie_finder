# AGENTS.md

Authoritative playbook for coding agents collaborating on the Movie Finder API. Follow these conventions to ensure reliable, reproducible work.

---

## Project Snapshot
- Framework: **Django 5.2.6** (ASGI-ready, DRF enabled)
- Python: **3.12** (managed with Poetry 2.x)
- Package manager: **Poetry** (`pyproject.toml` is the single source of truth)
- Database: **PostgreSQL** (dev defaults: user `postgres`, password `postgres`, port `5433` via Docker Compose)
- Primary apps: `auth_app`, `movie`, `throttling`, `movie_finder_django`
- Entry points: `manage.py`, `Makefile`, `docker-compose.yml`

---

## First-Time Setup
1. Install dependencies:
   ```bash
   poetry install
   ```
2. Copy environment template and fill secrets/API keys:
   ```bash
   cp env_example .env
   ```
   - Minimum required for local work: `DJANGO_KEY`, DB credentials, `IMDB_API_KEY`, `OMDB_API_KEY`, `ANTHROPIC_API_KEY`.
3. Start services:
   - Native: `poetry run python manage.py migrate && poetry run python manage.py runserver 0.0.0.0:8000`
   - Docker: `docker compose up --build`
     - PostgreSQL becomes available on `localhost:5433`.
4. Create a superuser when admin access is needed: `poetry run python manage.py createsuperuser`.

> Tip: `Makefile` targets mirror the common commands (`make install`, `make migrate`, `make test`, `make lint`, `make start`). Set `USE_DOCKER=1` to run manage.py commands inside the running container.

---

## Day-to-Day Workflow
- Activate the Poetry environment (`poetry shell`) or prefix commands with `poetry run`.
- Keep migrations in sync: run `poetry run python manage.py makemigrations` then `migrate` whenever models change; include new migration files in your edits.
- External data flows rely on CollectAPI (IMDB) and OMDB. Tests that touch these endpoints should use mocks; see `movie/tests/` for patterns.
- Watch throttling rules when touching search endpoints: they expect a `User-Agent` header and respect per-IP/U-A quotas (defined in `throttling/`).
- API schema lives under `/api/schema/`; drf-spectacular generates Swagger (`/api/swagger/`) and Redoc (`/api/redoc/`). Update serializers/viewsets accordingly.

---

## Quality & Tooling Expectations
- **Testing:**
  - `make test` (pytest via Poetry) is the default; `pytest-django` is preconfigured with `DJANGO_SETTINGS_MODULE=movie_finder_django.settings`.
  - Add or update tests in `auth_app/tests.py`, `movie/tests/`, `throttling/tests/` when behaviors change.
  - For coverage checks use `make coverage`.
  - When running tests or applying migrations locally, prefer the Makefile targets over raw Poetry/Django commands.
- **Static analysis:**
  - `make lint` runs Ruff (`select = [E, F, I, DJ]`, ignore `DJ008`). Fix findings before handing work back.
  - `make format` enforces Ruff formatting (single quotes, 4-space indentation, max line length 150).
- **Type hints:** Where practical, maintain existing typing; new services/helpers should include return type annotations.
- **Pre-commit:** Run `pre-commit install` if you need local hooks (optional but encouraged).

---

## Coding Guidelines for Agents
- Operate within ASCII unless the target file already uses Unicode.
- Mirror existing module boundaries: domain code in `movie/`, authentication in `auth_app/`, shared utilities in `utils/`.
- When integrating new external APIs, surface configuration keys in `.env`, update `movie_finder_django/settings.py`, and document them in `README.md`.
- Persist secrets and tokens only through environment variables; never commit credentials or real keys.
- Ensure new endpoints are covered by DRF serializers, URLs, and permission classes; update throttling rules if rates change.
- When modifying AI search behaviour (`movie/ai_find_movie.py` and related services), adjust `movie/system_prompts.py` and account for token limits (`MAX_PROMPT_TOKENS_LENGTH`).
- Keep business logic inside the service layer (`movie/services.py`, `movie/ai_find_movie.py`) and make services framework-agnostic; exchange data via lightweight DTOs (`movie/dataclasses.py`) rather than direct Django models or DRF serializers.
- Keep every DTO/dataclass definition consolidated in `movie/dataclasses.py`; don't scatter DTOs across repositories or services.
- Persisted data access belongs in the repository layer (`movie/repositories.py`); strive to minimise query counts (use batching, `select_related`, `prefetch_related`, in-memory aggregation when viable).
- Document noteworthy behaviour changes in `CHANGELOG.md` if it exists; otherwise provide context in the pull request description.

---

## Debugging & Support
- Use `poetry run python manage.py shell_plus` (Django Extensions) for interactive debugging.
- Database inspection: connect to the Dockerised Postgres instance (`psql -h localhost -p 5433 -U postgres`).
- Stuck with throttling or auth flows? Inspect DRF throttles in `throttling/` and JWT configuration in `movie_finder_django/settings.py`.
- External API issues often stem from missing keys or exceeding daily limits; mock responses during tests to keep CI deterministic.

Stick to these instructions for consistent, high-quality contributions.
