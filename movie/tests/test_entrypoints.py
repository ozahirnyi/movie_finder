from importlib import reload
from unittest.mock import MagicMock, patch

from django.test import SimpleTestCase


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
        self.assertEqual(response.get('Content-Type', ''), 'text/plain; charset=utf-8')
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
                with patch(
                    'opentelemetry.instrumentation.django.DjangoInstrumentor'
                ) as mock_instr:
                    mock_instr.return_value.instrument = MagicMock()
                    setup_tracing()
                    mock_instr.return_value.instrument.assert_called_once()
