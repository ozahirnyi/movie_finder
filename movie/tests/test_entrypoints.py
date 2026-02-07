from importlib import reload
from unittest.mock import MagicMock, patch

from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from django.utils import timezone

from auth_app.models import AccountTier


class EntryPointTests(SimpleTestCase):
    def test_asgi_application_is_initialised(self):
        module = reload(__import__('movie_finder_django.asgi', fromlist=['application']))
        self.assertIsNotNone(module.application)

    def test_wsgi_application_is_initialised(self):
        module = reload(__import__('movie_finder_django.wsgi', fromlist=['application']))
        self.assertIsNotNone(module.application)

    def test_metrics_endpoint_returns_prometheus_text(self):
        response = self.client.get('/metrics')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            response.get('Content-Type', '').startswith('text/plain') and 'charset=utf-8' in response.get('Content-Type', ''),
            msg=f"Content-Type should be text/plain with charset=utf-8, got {response.get('Content-Type')}",
        )
        self.assertIn(b'movie_finder', response.content)

    def test_setup_tracing_no_op_without_otel_endpoint(self):
        from movie_finder_django.tracing import setup_tracing

        with patch.dict('os.environ', {'OTEL_EXPORTER_OTLP_ENDPOINT': ''}, clear=False):
            setup_tracing()

    def test_setup_tracing_instruments_when_otel_endpoint_set(self):
        from movie_finder_django.tracing import setup_tracing

        with patch.dict(
            'os.environ',
            {'OTEL_EXPORTER_OTLP_ENDPOINT': 'http://tempo:4317', 'OTEL_SERVICE_NAME': 'mf'},
            clear=False,
        ):
            with patch(
                'opentelemetry.exporter.otlp.proto.grpc.trace_exporter.OTLPSpanExporter',
                MagicMock(),
            ):
                with patch('opentelemetry.instrumentation.django.DjangoInstrumentor') as mock_instr:
                    mock_instr.return_value.instrument = MagicMock()
                    setup_tracing()
                    mock_instr.return_value.instrument.assert_called_once()

    def test_setup_tracing_swallows_exception_when_otel_fails(self):
        from movie_finder_django.tracing import setup_tracing

        with patch.dict(
            'os.environ',
            {'OTEL_EXPORTER_OTLP_ENDPOINT': 'http://tempo:4317'},
            clear=False,
        ):
            with patch(
                'opentelemetry.exporter.otlp.proto.grpc.trace_exporter.OTLPSpanExporter',
                side_effect=RuntimeError('grpc unavailable'),
            ):
                setup_tracing()


class MetricsWithDBTests(TestCase):
    """Tests that require DB to exercise daily usage gauges and collector."""

    def test_metrics_scrape_includes_daily_usage_gauges_when_tiers_exist(self):
        today = timezone.now().date()
        tier = AccountTier.objects.create(
            code='test_tier',
            name='Test',
            daily_ai_search_limit=10,
            is_default=False,
        )
        get_user_model().objects.create_user(
            email='metrics@test.example',
            password='testpass123',
            account_tier=tier,
            ai_search_count_reset_at=today,
            ai_search_count=1,
        )
        response = self.client.get('/metrics')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'movie_finder_users_ai_search_used_today', response.content)
        self.assertIn(b'movie_finder_users_at_daily_limit_today', response.content)

    def test_register_daily_usage_collector_swallows_register_exception(self):
        import movie_finder_django.metrics as metrics_module

        mock_registry = MagicMock()
        mock_registry.register.side_effect = ValueError('registry full')
        with patch.object(metrics_module, '_daily_usage_registered', False):
            metrics_module.register_daily_usage_collector(registry=mock_registry)
        mock_registry.register.assert_called_once()

    def test_metrics_scrape_handles_daily_usage_query_failure(self):
        import movie_finder_django.metrics as metrics_module

        with patch.object(metrics_module, '_get_daily_usage_gauges', side_effect=RuntimeError('DB gone')):
            response = self.client.get('/metrics')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'movie_finder', response.content)
