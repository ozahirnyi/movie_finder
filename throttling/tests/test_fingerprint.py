import hashlib

from django.test import SimpleTestCase
from user_agents import parse

from throttling.fingerprint import get_fingerprint


class _RequestStub:
    def __init__(self, meta: dict[str, str]):
        self.META = meta


class FingerprintTests(SimpleTestCase):
    def test_generates_stable_hash(self):
        meta = {
            'HTTP_USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36',
            'REMOTE_ADDR': '203.0.113.10',
        }
        request = _RequestStub(meta)

        fingerprint = get_fingerprint(request)

        agent = parse(meta['HTTP_USER_AGENT'])
        expected_payload = f'{agent.browser.family}-{agent.os.family}-{agent.device.family}-{meta["REMOTE_ADDR"]}'
        expected_hash = hashlib.sha256(expected_payload.encode()).hexdigest()

        self.assertEqual(fingerprint, expected_hash)

    def test_uses_empty_defaults_when_headers_missing(self):
        request = _RequestStub({})

        fingerprint = get_fingerprint(request)

        agent = parse('')
        expected_payload = f'{agent.browser.family}-{agent.os.family}-{agent.device.family}-'
        self.assertEqual(fingerprint, hashlib.sha256(expected_payload.encode()).hexdigest())
