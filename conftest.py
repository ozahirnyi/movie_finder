# Set before any test runs so migration 0006 skips curated seed when creating test DB.
import os


def pytest_configure(config):
    os.environ['DJANGO_TESTING'] = '1'
