# Локальний запуск з метриками (Docker)

## Один раз

У корені проєкту створено `.env` з `env_example` (якщо його не було). Можна відредагувати при потребі.

## Запуск

```bash
cd o:\projects\movie_finder

docker compose -f docker-compose.lightsail.yml -f docker-compose.monitoring.yml up -d --build
```

Через кілька хвилин (після збірки образу та старту БД):

- **Додаток:** http://localhost (порт 80)
- **Метрики (сирий Prometheus):** http://localhost/metrics
- **Prometheus UI:** http://localhost:9090 → Status → Targets (має бути `movie_finder` UP)
- **Grafana (дашборди):** http://localhost:3000 — логін `admin` / `admin`

У Grafana: **Dashboards** → **Movie Finder** → **Movie Finder Overview**.

## Зупинка

```bash
docker compose -f docker-compose.lightsail.yml -f docker-compose.monitoring.yml down
```

## Тільки додаток (без Prometheus/Grafana)

```bash
docker compose -f docker-compose.lightsail.yml up -d --build
```

Метрики все одно будуть доступні на http://localhost/metrics.
