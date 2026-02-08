---
name: pre-commit-and-tests
description: Before any commit or push in this project, run tests and pre-commit. Use when committing, pushing, or when the user asks to commit or push changes.
---

# Pre-commit and tests before commit/push

## Rule

**Before every commit or push**, run:

1. **Pre-commit** (includes ruff, ruff-format, migration checks, and pytest):
   ```bash
   pre-commit run --all-files
   ```
2. If the project uses Poetry and pre-commit is not available in the current shell, run equivalent checks:
   - `make lint` and `make format` (or `poetry run ruff check . --fix` and `poetry run ruff format .`)
   - `make test` (or `poetry run pytest`)

Do **not** commit or push until pre-commit and tests pass. If hooks modify files (e.g. ruff --fix), stage those changes and run pre-commit again before committing.
