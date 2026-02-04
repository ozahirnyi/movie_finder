# Grafana, Prometheus та Loki для Movie Finder

Як розгорнути стек моніторингу (метрики + логи) на тому ж Lightsail інстансі та які метрики збираються.

---

## Що додано в проект

### Метрики в Django

- **HTTP:** кількість запитів і латентність по ендпоінтах (`movie_finder_http_requests_total`, `movie_finder_http_request_duration_seconds`).
- **AI search квота:**
  - `movie_finder_ai_search_used_total{tier_code}` — успішні AI-пошуки по тарифах.
  - `movie_finder_ai_search_limit_hit_total{tier_code}` — відмови через денний ліміт.
  - `movie_finder_users_ai_search_used_today{tier_code}` — скільки користувачів сьогодні використали хоча б один AI-пошук (по тарифах).
  - `movie_finder_users_at_daily_limit_today{tier_code}` — скільки користувачів сьогодні вже на ліміті (по тарифах).

Ендпоінт метрик: **`GET /metrics`** (формат Prometheus). За замовчуванням метрики увімкнені (`METRICS_ENABLED=True`); вимкнути: `METRICS_ENABLED=False` у `.env`.

### Стек моніторингу (Docker)

- **Prometheus** — збирає метрики з Django (`/metrics`).
- **Grafana** — дашборди, графіки, логи й трейси.
- **Loki** — зберігання логів.
- **Promtail** — збір логів контейнерів Docker і відправка в Loki (парсинг Docker JSON).
- **Tempo** — зберігання трейсів (OpenTelemetry OTLP від Django).

Файли:

- `docker-compose.monitoring.yml` — сервіси моніторингу; для `web` задано `OTEL_EXPORTER_OTLP_ENDPOINT` і `OTEL_SERVICE_NAME` для трейсингу.
- `monitoring/prometheus/prometheus.yml` — конфіг Prometheus (scrape `web:8000/metrics`).
- `monitoring/loki/loki-config.yml`, `monitoring/promtail/promtail-config.yml` — Loki та Promtail.
- `monitoring/tempo/tempo.yml` — Tempo (OTLP gRPC/HTTP).
- `monitoring/grafana/provisioning/` — datasources (Prometheus, Loki, Tempo) і дашборд **Movie Finder Overview**.
- `movie_finder_django/tracing.py` — ініціалізація OpenTelemetry (Django instrumentation); активна лише якщо задано `OTEL_EXPORTER_OTLP_ENDPOINT`.

---

## Запуск на Lightsail

### 1. Деплой з моніторингом

Якщо на інстансі є `docker-compose.monitoring.yml` (його додано в репо), після деплою CodeDeploy сам піднімає і app, і моніторинг:

- у `application_start.sh` викликається  
  `docker compose -f docker-compose.lightsail.yml -f docker-compose.monitoring.yml up -d`.

Якщо моніторинг не потрібен — видаліть або перейменуйте `docker-compose.monitoring.yml` на інстансі; тоді стартуватиме лише `docker-compose.lightsail.yml`.

### 2. Порти та доступ

- **Grafana:** `http://<IP_інстансу>:3000`  
  Логін за замовчуванням: `admin` / `admin` (при першому вході варто змінити пароль).
- **Prometheus:** `http://<IP_інстансу>:9090`.
- Loki/Promtail не мають публічних портів у зовнішній мережі; вони використовуються лише всередині Docker-мережі.

У Lightsail у **Networking → Firewall** додайте правило для **TCP 3000** (Grafana); 9090 можна відкрити тільки якщо потрібен прямий доступ до Prometheus.

### 3. Змінні оточення (опційно)

У `.env` на інстансі можна задати:

```bash
# Grafana
GRAFANA_ADMIN_USER=admin
GRAFANA_ADMIN_PASSWORD=<надійний_пароль>
GRAFANA_ROOT_URL=https://grafana.yourdomain.com   # якщо є домен і reverse proxy
```

Після зміни перезапустіть контейнери:

```bash
docker compose -f docker-compose.lightsail.yml -f docker-compose.monitoring.yml up -d
```

### 4. Доставка на прод

Моніторинг уже інтегрований у деплой:

1. **CodeDeploy** за допомогою `appspec.yml` копіює весь репо (включно з `docker-compose.monitoring.yml` та папкою `monitoring/`) на інстанс.
2. **application_start.sh** при наявності `docker-compose.monitoring.yml` запускає і app, і моніторинг одним викликом.
3. Пуш у `main` або тег `v*` (після успішного CI) запускає workflow **Deploy to Lightsail via CodeDeploy** — після деплою на проді будуть працювати web, db, Prometheus, Grafana, Loki, Promtail, Tempo.

**Що зробити на проді один раз:**

- У **Lightsail → Networking → Firewall** додати правило **TCP 3000** (щоб відкрити Grafana ззовні, якщо потрібно).
- На інстансі в `.env` задати `GRAFANA_ADMIN_PASSWORD=<сильний_пароль>` (і за бажанням `GRAFANA_ROOT_URL`), щоб не лишати логін admin/admin.

Архітектура образів не зафіксована (`platform` прибрано з compose), тому на Lightsail (amd64 чи arm64) Docker підбере відповідні образи.

---

## Дашборд «Movie Finder Overview»

Після першого входу в Grafana має з’явитися дашборд **Movie Finder** → **Movie Finder Overview** з панелями:

1. **Request rate by endpoint** — RPS по ендпоінтах.
2. **HTTP latency p95 by endpoint** — латентність (p95).
3. **AI search consumed (24h) by tier** — скільки AI-пошуків спожито за останні 24 год по тарифах.
4. **AI search limit rejected (24h) by tier** — скільки відмов через ліміт за 24 год.
5. **Users who used AI search today (by tier)** — кількість користувачів, що сьогодні використали ліміт (хоча б один пошук), по тарифах.
6. **Users at daily AI search limit today (by tier)** — кількість користувачів, які сьогодні вже вичерпали денний ліміт, по тарифах.

Останні дві панелі як раз дають метрику «скільки юзери використовують лімітів за день» (по тарифах і в розрізі «використали сьогодні» / «вже на ліміті»).

---

## Логи в Grafana (Loki)

1. Відкрийте **Explore** (іконка компаса).
2. Оберіть datasource **Loki**.
3. У запросі можна фільтрувати по лейблу, наприклад: `{service="web"}` або `{container=~"movie_finder.*"}` (залежить від імен контейнерів у вашому compose).

Якщо контейнери пишуть логи в stdout/stderr, Promtail їх підхопить і відправить у Loki.

---

## Трейси в Grafana (Tempo)

1. Відкрийте **Explore** і оберіть datasource **Tempo**.
2. Можна шукати трейси за **Service Name** = `movie_finder` або за **Tags**.
3. У datasource Tempo налаштовано зв’язок з Loki (traces → logs) для переходу від спану до логів.

Трейси надсилаються з Django лише коли в оточенні контейнера `web` задано `OTEL_EXPORTER_OTLP_ENDPOINT` (у `docker-compose.monitoring.yml` це вже налаштовано).

---

## Локальна перевірка

```bash
# Тільки додаток
docker compose -f docker-compose.lightsail.yml up -d

# Додаток + моніторинг
docker compose -f docker-compose.lightsail.yml -f docker-compose.monitoring.yml up -d
```

Перевірка метрик:

```bash
curl http://localhost/metrics
# або, якщо web слухає тільки 8000:
curl http://localhost:8000/metrics
```

Grafana: `http://localhost:3000`.

---

## Вимкнення метрик у Django

У `.env`:

```bash
METRICS_ENABLED=False
```

Після цього middleware метрик не підключається і ендпоінт `/metrics` не обробляється (404). Prometheus продовжить отримувати помилки при scrape; можна або прибрати job `movie_finder` з `monitoring/prometheus/prometheus.yml`, або залишити — на дашборді просто не буде даних по додатку.

---

## Підсумок

- **Де:** той самий Lightsail інстанс; контейнери з `docker-compose.monitoring.yml`.
- **Що:** Prometheus (метрики), Grafana (дашборди), Loki + Promtail (логи), Tempo (трейси з OpenTelemetry).
- **Метрика «скільки юзери використовують лімітів за день»:** панелі **Users who used AI search today** та **Users at daily AI search limit today** на дашборді **Movie Finder Overview** у Grafana.
