FROM python:3.12-slim

RUN apt-get update \
    && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 - --version 2.1.4 \
    && ln -s /root/.local/bin/poetry /usr/local/bin/poetry

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

WORKDIR /app

COPY pyproject.toml poetry.lock README.md /app/
RUN poetry install --no-root

COPY . /app

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
