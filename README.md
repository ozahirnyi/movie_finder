# Movie Finder API

A Django REST API for discovering and organising movies. The service integrates IMDB/OMDB metadata, Anthropic-powered AI recommendations, and supports personal curation features such as likes and watch-later queues. Authentication is powered by JWT and optional Google OAuth via `django-allauth`.

## Feature Highlights
- **Movie catalogue** – PostgreSQL-backed catalogue enriched on-demand from IMDB (CollectAPI) and OMDB.
- **AI-assisted discovery** – Anthropic Claude Sonnet generates contextual movie suggestions which are then resolved against OMDB.
- **Personal lists** – Users can like titles or queue them for later, with aggregate statistics across their watch-later list.
- **Search & filtering** – Rich filtering, ordering, and pagination for stored titles plus on-demand external searches.
- **Authentication** – Email-based accounts using a custom user model, JWT token issuance (`/token/`, `/token/refresh/`), Google OAuth sign-in via Allauth.
- **Throttling & safety** – Per-user-agent/IP throttles guard public search endpoints; requests must include a `User-Agent` header.
- **API documentation** – OpenAPI schema and Swagger/Redoc UIs provided by drf-spectacular.

## Architecture Overview
| Module | Responsibility |
| ------ | -------------- |
| `auth_app` | Custom `User` model, signup and password change APIs, Google OAuth wiring.
| `movie` | Domain models, serializers, filters, services integrating external data sources, AI search client, watch-later and like flows.
| `throttling` | Custom DRF throttles tied to IP, forwarded IP and user-agent fingerprints.
| `utils` | Development helpers (e.g. SQL query logging decorator).
| `movie_finder_django` | Project settings, URL routing, DRF/Allauth/SimpleJWT configuration.

## Requirements
- Python 3.12+
- Poetry 2.x (project uses `pyproject.toml` for dependency management)
- PostgreSQL (local development defaults: user `postgres`, password `postgres`, port `5433` when using Docker Compose)
- External API keys: CollectAPI IMDB key, OMDB API key, Anthropic API key

## Environment Configuration
Copy the sample file and adjust values:
```bash
cp env_example .env
```
Key variables (see `movie_finder_django/settings.py` for defaults):

| Variable | Purpose |
| -------- | ------- |
| `DEBUG` | Enables Django debug mode.
| `DJANGO_KEY` | Django secret key / JWT signing secret.
| `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` | PostgreSQL connection settings (tests use `DB_TEST_NAME`).
| `IMDB_API_KEY` | CollectAPI key for `/imdbSearchByName` and `/imdbSearchById` endpoints.
| `OMDB_API_KEY` | OMDB API key for movie details.
| `ANTHROPIC_API_KEY` | Anthropic Claude key for AI search (also used to count prompt tokens).
| `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD` | Credentials for SMTP (default Gmail settings are configured).
| `DJANGO_SETTINGS_MODULE`, `PYTHONUNBUFFERED` | Optional overrides typically left unset locally.

> ⚠️ **Headers:** Endpoints protected by throttles require a `User-Agent` header. AI and regular search also inspect `X-Forwarded-For` when present.

## Local Development
### Using Poetry directly
```bash
poetry install
poetry run python manage.py migrate
poetry run python manage.py runserver 0.0.0.0:8000
```

### Using Docker Compose
```bash
docker compose up --build
```
This builds the application container, applies migrations, and runs the development server on <http://localhost:8000> with PostgreSQL exposed on `localhost:5433`.

### Makefile shortcuts
A `Makefile` is included for common workflows:
```bash
make help              # List targets
make start             # docker compose up --build -d
make stop              # docker compose down --remove-orphans
make test              # Run pytest via poetry
make lint              # Ruff static analysis
make format            # Ruff formatter
USE_DOCKER=1 make migrate   # Run manage.py command inside the running web container
```

### Sample data
A minimal PostgreSQL snapshot captured from the shared development database lives at `data/minimal_seed.sql`. Load it after running migrations so the API has a handful of users, movies, and related entities:
```bash
make load-minimal-data
```
The command connects to the database using `DB_*` values from your environment (falling back to the Docker defaults). To refresh the snapshot from your local Dockerised Postgres instance run:
```bash
mkdir -p data && docker compose exec db pg_dump -U postgres -d postgres --schema=public --data-only --column-inserts --no-owner --no-privileges > data/minimal_seed.sql
```

### Database migrations
Run migrations anytime models change:
```bash
poetry run python manage.py makemigrations
poetry run python manage.py migrate
```

## External Services & Integrations
- **CollectAPI IMDB** (`IMDB_API_SEARCH_BY_NAME_URL`, `IMDB_API_SEARCH_BY_IMDB_ID_URL`): Supplies initial search results.
- **OMDB**: Source of authoritative movie metadata; responses are cached in the local database via `MovieRepository`.
- **Anthropic Claude**: Processes natural language prompts (`MoviesAiSearchView`) using the system prompt defined in `movie/system_prompts.py`.
- **Google OAuth**: Enabled through `django-allauth`; ensure a Google OAuth client is registered and associated via the Django admin or fixtures for production use.

## REST API
Base URL defaults to the server root (no `/api/` prefix). Selected endpoints:

| Method | Path | Auth | Description |
| ------ | ---- | ---- | ----------- |
| `POST` | `/signup/` | Public | Create a user account (email/password).
| `POST` | `/token/` | Public | Obtain JWT access/refresh tokens.
| `POST` | `/token/refresh/` | Public | Refresh JWT access token.
| `PATCH` | `/users/change_password/` | JWT | Update the authenticated user password.
| `GET` | `/movies/` | Optional | List stored movies with filtering (`imdb_id`, `title`, `genres`, `year`) and ordering (`imdb_id`, `title`, `genre`, `year`, `likes_count`).
| `GET` | `/movies/<id>/` | Optional | Retrieve a movie with like/watch-later annotations and related entities.
| `POST` | `/movies/<id>/like/` | JWT | Like a movie (idempotent via unique constraint).
| `POST` | `/movies/<id>/unlike/` | JWT | Remove a like for the movie.
| `POST` | `/movies/search/` | Optional | Search IMDB by expression, resolve titles through OMDB, return enriched payloads.
| `POST` | `/movies/ai/search/` | JWT | Anthropic-powered prompt-based discovery, falling back to OMDB for canonical metadata.
| `GET` | `/watch_later/list/` | JWT | Paginated list of the user’s watch-later titles.
| `POST` | `/watch_later/create/` | JWT | Add a movie to the watch-later list (expects `movie` id).
| `DELETE` | `/watch_later/<pk>/destroy/` | JWT | Remove a movie from watch-later.
| `GET` | `/watch_later/statistics/` | JWT | Aggregated ratings buckets and genre breakdown for the user’s queue.
| `GET` | `/api/swagger/` | Public | Interactive Swagger UI (schema at `/api/schema/`).
| `GET` | `/api/redoc/` | Public | Redoc documentation UI.

> Pagination uses DRF limit-offset with defaults of 12 items per page (`limit`/`offset` query params).

## Throttling
Rate limits are enforced on search endpoints (`MoviesListView`, `MoviesSearchView`). Daily limits apply per user agent/IP: regular search allows 10 (UA) / 20 (IP) requests per day; AI search is stricter (2 per UA, 6 per IP). Missing `User-Agent` headers trigger a validation error.

## AI usage tiers
- Django admin exposes `Account tiers` to configure per-day AI search quotas; defaults: `free` (3), `premium` (30), `admin` (100).
- Users inherit the default tier on creation and can be reassigned via the admin `Users` page.
- Each AI movie search consumes one quota unit; limits reset daily per user.

## Testing & Quality
```bash
make test          # or: poetry run pytest
make lint          # Ruff checks (PEP8, Django rules)
make format        # Ruff formatter
```

The repository includes Django test cases under `auth_app/tests.py` and `movie/tests.py` covering authentication flows, watch-later operations, and search behaviour. `pytest-django` is available; set `DJANGO_SETTINGS_MODULE=movie_finder_django.settings` if running outside the provided commands.

Optional: install pre-commit hooks (`pre-commit install`) to enforce code style and check migrations before commits.

## Troubleshooting
- **Throttling errors**: Ensure `User-Agent` and (optionally) `X-Forwarded-For` headers are supplied; wait for the rate window to reset.
- **Anthropic token limit**: Prompts exceeding `MAX_PROMPT_TOKENS_LENGTH` return an empty AI result set.
- **OAuth setup**: Configure a Google `SocialApp` via the Django admin (`/admin/`) or fixtures; without it OAuth flows will fail.

## Useful Links
- Swagger UI: `http://localhost:8000/api/swagger/`
- Redoc UI: `http://localhost:8000/api/redoc/`
- Django Admin: `http://localhost:8000/admin/`

Happy movie hunting!
