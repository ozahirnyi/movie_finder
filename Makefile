.PHONY: help start restart stop ps logs install test lint format check coverage migrate makemigrations collectstatic createsuperuser shell shell_plus build clean

.DEFAULT_GOAL := help

POETRY ?= poetry
DOCKER_COMPOSE ?= docker compose
RUNSERVER_PORT ?= 8000

ifdef USE_DOCKER
RUN := $(DOCKER_COMPOSE) exec web $(POETRY) run
else
RUN := $(POETRY) run
endif

MANAGE := $(RUN) python manage.py

help: ## Show available commands
	@echo "Available make targets:"
	@grep -E '^[a-zA-Z_-]+:.*##' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS=":.*## "}{printf "  %-18s %s\n", $$1, $$2}'

start: ## Build and start the docker stack in the background
	$(DOCKER_COMPOSE) up --build -d

restart: ## Restart the docker stack
	$(MAKE) stop
	$(MAKE) start

stop: ## Stop the docker stack
	$(DOCKER_COMPOSE) down --remove-orphans

ps: ## Show container status
	$(DOCKER_COMPOSE) ps

logs: ## Tail container logs
	$(DOCKER_COMPOSE) logs -f

install: ## Install python dependencies with poetry
	$(POETRY) install

test: ## Run test suite with pytest
	$(RUN) pytest

coverage: ## Run tests with coverage and show report
	$(RUN) coverage run -m pytest
	$(RUN) coverage report -m --fail-under=100

lint: ## Run static analysis via ruff
	$(RUN) ruff check

format: ## Format code via ruff
	$(RUN) ruff format

check: lint test ## Run lint and test suite

migrate: ## Apply database migrations
	$(MANAGE) migrate

makemigrations: ## Create new migrations
	$(MANAGE) makemigrations

collectstatic: ## Collect static files
	$(MANAGE) collectstatic --noinput

createsuperuser: ## Create django superuser
	$(MANAGE) createsuperuser

shell: ## Open Django shell
	$(MANAGE) shell

shell_plus: ## Open Django shell_plus (requires django-extensions)
	$(MANAGE) shell_plus

build: ## Build docker images
	$(DOCKER_COMPOSE) build

clean: ## Remove Python cache artifacts
	find . -name '__pycache__' -type d -prune -exec rm -rf {} + && rm -rf .pytest_cache
