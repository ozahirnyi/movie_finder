"""
Prometheus metrics for Movie Finder API.

Exposes request counts, latency, AI search quota usage, and daily limit usage
for Grafana dashboards.
"""

from prometheus_client import (
    CONTENT_TYPE_LATEST,
    REGISTRY,
    Counter,
    Histogram,
    generate_latest,
)
from prometheus_client.core import GaugeMetricFamily

# Registry used by the app (can be replaced in tests)
metrics_registry = REGISTRY

# --- HTTP ---
request_count = Counter(
    'movie_finder_http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status'],
    registry=metrics_registry,
)
request_latency_seconds = Histogram(
    'movie_finder_http_request_duration_seconds',
    'HTTP request latency in seconds',
    ['method', 'endpoint'],
    buckets=(0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0),
    registry=metrics_registry,
)

# --- AI search quota (per request) ---
ai_search_used_total = Counter(
    'movie_finder_ai_search_used_total',
    'Total AI searches consumed (successful)',
    ['tier_code'],
    registry=metrics_registry,
)
ai_search_limit_hit_total = Counter(
    'movie_finder_ai_search_limit_hit_total',
    'Total requests rejected due to daily AI search limit',
    ['tier_code'],
    registry=metrics_registry,
)

# --- Daily usage gauges (filled on scrape from DB) ---
# We use a custom collector to avoid importing Django models at module load.
# Gauges are registered in _register_gauges() when metrics are enabled.


def _get_daily_usage_gauges():
    """Query DB for current-day AI search usage and expose as gauges."""
    from django.db.models import F
    from django.utils import timezone

    from auth_app.models import AccountTier, User

    today = timezone.now().date()
    tiers = AccountTier.objects.all()
    result = []
    for tier in tiers:
        used_today = User.objects.filter(
            account_tier=tier,
            ai_search_count_reset_at=today,
            ai_search_count__gt=0,
        ).count()
        at_limit = User.objects.filter(
            account_tier=tier,
            ai_search_count_reset_at=today,
            ai_search_count__gte=F('account_tier__daily_ai_search_limit'),
            account_tier__daily_ai_search_limit__gt=0,
        ).count()
        result.append((tier.code, used_today, at_limit))
    return result


class DailyUsageCollector:
    """Prometheus collector that fills gauges from DB on each /metrics scrape."""

    def __init__(self, registry=metrics_registry):
        self._registry = registry

    def collect(self):
        try:
            rows = _get_daily_usage_gauges()
            used_family = GaugeMetricFamily(
                'movie_finder_users_ai_search_used_today',
                'Number of users who used at least one AI search today',
                labels=['tier_code'],
            )
            limit_family = GaugeMetricFamily(
                'movie_finder_users_at_daily_limit_today',
                'Number of users who hit their daily AI search limit today',
                labels=['tier_code'],
            )
            for tier_code, users_used_today, users_at_limit in rows:
                used_family.add_metric([tier_code], users_used_today)
                limit_family.add_metric([tier_code], users_at_limit)
            yield used_family
            yield limit_family
        except Exception:
            pass


_daily_usage_registered = False


def register_daily_usage_collector(registry=metrics_registry) -> None:
    """Register the daily usage collector. Call once when metrics are enabled."""
    global _daily_usage_registered
    if _daily_usage_registered:
        return
    try:
        registry.register(DailyUsageCollector(registry))
        _daily_usage_registered = True
    except Exception:
        pass


def metrics_view(request):
    """Django view that serves Prometheus metrics."""
    register_daily_usage_collector()
    data = generate_latest(metrics_registry)
    from django.http import HttpResponse

    return HttpResponse(data, content_type=CONTENT_TYPE_LATEST)


def normalize_path(path: str) -> str:
    """Reduce path to endpoint label (e.g. /api/movies/123/ -> /api/movies/{id}/)."""
    if not path or path == '/':
        return '/'
    path = path.rstrip('/') or '/'
    parts = path.split('/')
    normalized = []
    for p in parts:
        if p.isdigit():
            normalized.append('{id}')
        else:
            normalized.append(p)
    return '/' + '/'.join(normalized).strip('/') or ''


class PrometheusMiddleware:
    """Record request count and latency for Prometheus."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/metrics':
            return self.get_response(request)
        import time

        path = normalize_path(request.path)
        method = request.method or 'GET'
        start = time.perf_counter()
        status = 500
        try:
            response = self.get_response(request)
            status = response.status_code
            return response
        finally:
            duration = time.perf_counter() - start
            request_latency_seconds.labels(method=method, endpoint=path).observe(duration)
            status_class = str(status)[0] + 'xx' if str(status) else 'xxx'
            request_count.labels(method=method, endpoint=path, status=status_class).inc()
