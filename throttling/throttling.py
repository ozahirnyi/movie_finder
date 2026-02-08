from rest_framework.exceptions import ValidationError
from rest_framework.throttling import SimpleRateThrottle


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
        if forwarded_for := request.META.get('HTTP_X_FORWARDED_FOR'):
            client_ip = forwarded_for.split(',')[0].strip()
        else:
            client_ip = request.META.get('REMOTE_ADDR')
        return f'throttle_forwarded_{client_ip}'


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
