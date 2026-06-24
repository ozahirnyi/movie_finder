import hashlib

from django.core.cache import cache
from rest_framework.exceptions import ValidationError
from rest_framework.throttling import SimpleRateThrottle

GUEST_AI_SEARCH_SCOPE = 'guest_ai_search'
GUEST_AI_SEARCH_CACHE_PREFIX = f'throttle_{GUEST_AI_SEARCH_SCOPE}'
GUEST_AI_SEARCH_CACHE_TIMEOUT = None


def _hashed_cache_key(suffix: str, payload: str) -> str:
    fingerprint = hashlib.sha256(payload.encode()).hexdigest()
    return f'{GUEST_AI_SEARCH_CACHE_PREFIX}_{suffix}_{fingerprint}'


def get_forwarded_client_ip(request) -> str:
    if forwarded_for := request.META.get('HTTP_X_FORWARDED_FOR'):
        return forwarded_for.split(',')[0].strip()
    return request.META.get('REMOTE_ADDR', '')


def get_guest_ai_search_cache_keys(request) -> list[str]:
    user_agent = request.META.get('HTTP_USER_AGENT')
    if not user_agent:
        raise ValidationError('User agent is required')

    forwarded_ip = get_forwarded_client_ip(request)
    remote_ip = request.META.get('REMOTE_ADDR', '')
    return [
        _hashed_cache_key('forwarded', forwarded_ip),
        _hashed_cache_key('remote', remote_ip),
        _hashed_cache_key('fingerprint', f'{forwarded_ip}:{remote_ip}:{user_agent}'),
    ]


def get_guest_ai_search_cache_key(request) -> str:
    return get_guest_ai_search_cache_keys(request)[0]


def consume_guest_ai_search_quota(request) -> bool:
    cache_keys = get_guest_ai_search_cache_keys(request)
    if any(cache.get(cache_key) is not None for cache_key in cache_keys):
        return False
    claimed = cache.add(cache_keys[0], 1, timeout=GUEST_AI_SEARCH_CACHE_TIMEOUT)
    if not claimed:
        return False
    for cache_key in cache_keys[1:]:
        cache.add(cache_key, 1, timeout=GUEST_AI_SEARCH_CACHE_TIMEOUT)
    return True


class UaBaseThrottle(SimpleRateThrottle):
    scope = 'ua'

    def get_cache_key(self, request, view):
        user_agent = request.META.get('HTTP_USER_AGENT')
        if not user_agent:
            raise ValidationError('User agent is required')
        return f'throttle_ua_{user_agent}'


class IpBaseThrottle(SimpleRateThrottle):
    scope = 'ip'

    def get_cache_key(self, request, view):
        ip_address = self.get_ident(request)
        return f'throttle_ip_{ip_address}'


class ForwardedForBaseThrottle(SimpleRateThrottle):
    scope = 'forwarded'

    def get_cache_key(self, request, view):
        return f'throttle_forwarded_{get_forwarded_client_ip(request)}'


# AI search: tuned for several users per IP (e.g. household) with tier limits; still caps abuse per IP/UA.
class AiSearchUaThrottle(UaBaseThrottle):
    scope = 'ai_search_ua'
    rate = '40/day'  # one user's tier (e.g. 30) per browser; was 2/day


class AiSearchIpThrottle(IpBaseThrottle):
    scope = 'ai_search_ip'
    rate = '100/day'  # e.g. 3 users x ~30 tier; was 6/day


class AiSearchForwardedThrottle(ForwardedForBaseThrottle):
    scope = 'ai_search_forwarded'
    rate = '100/day'  # same as IP when behind proxy


# Regular search: allow several users per IP without hitting throttle.
class RegularSearchUaThrottle(UaBaseThrottle):
    scope = 'regular_search_ua'
    rate = '30/day'  # was 10/day


class RegularSearchIpThrottle(IpBaseThrottle):
    scope = 'regular_search_ip'
    rate = '60/day'  # was 20/day


class RegularSearchForwardedThrottle(ForwardedForBaseThrottle):
    scope = 'regular_search_forwarded'
    rate = '60/day'  # was 20/day
