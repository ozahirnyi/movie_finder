"""
OpenTelemetry tracing for Movie Finder.

Initializes the OTLP exporter and Django instrumentation when
OTEL_EXPORTER_OTLP_ENDPOINT is set (e.g. in Docker with Tempo).
"""

import os


def setup_tracing() -> None:
    """Configure OpenTelemetry and instrument Django. Idempotent; no-op if disabled."""
    if not os.environ.get('OTEL_EXPORTER_OTLP_ENDPOINT'):
        return
    try:
        from opentelemetry import trace
        from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
        from opentelemetry.instrumentation.django import DjangoInstrumentor
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import BatchSpanProcessor
        from opentelemetry.sdk.resources import Resource

        resource = Resource.create({
            'service.name': os.environ.get('OTEL_SERVICE_NAME', 'movie_finder'),
        })
        provider = TracerProvider(resource=resource)
        provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter()))
        trace.set_tracer_provider(provider)
        DjangoInstrumentor().instrument()
    except Exception:
        pass
