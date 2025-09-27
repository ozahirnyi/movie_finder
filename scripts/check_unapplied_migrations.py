#!/usr/bin/env python
"""Pre-commit helper to ensure Django migrations are applied when possible."""

from __future__ import annotations

import os
import sys

import django
from django.core.management import call_command
from django.db.utils import OperationalError

DJANGO_SETTINGS_MODULE = os.getenv('DJANGO_SETTINGS_MODULE', 'movie_finder_django.settings')
TRANSIENT_ERRORS = (
    'could not translate host name',
    'could not connect to server',
    'connection refused',
)


def main() -> int:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', DJANGO_SETTINGS_MODULE)

    try:
        django.setup()
    except Exception as exc:  # pragma: no cover
        print(f'[check-unapplied-migrations] Failed to initialise Django: {exc}', file=sys.stderr)
        return 1

    try:
        call_command('migrate', check=True, interactive=False, verbosity=0)
    except OperationalError as exc:
        message = str(exc)
        lowered = message.lower()
        if any(token in lowered for token in TRANSIENT_ERRORS):
            print(f'[check-unapplied-migrations] Skipping check (database unavailable): {message}')
            return 0
        print(f'[check-unapplied-migrations] OperationalError: {message}', file=sys.stderr)
        return 1
    except Exception as exc:  # pragma: no cover
        print(f'[check-unapplied-migrations] Unexpected error: {exc}', file=sys.stderr)
        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main())
