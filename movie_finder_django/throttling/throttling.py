from rest_framework.throttling import SimpleRateThrottle, UserRateThrottle
from .fingerprint import get_fingerprint


class MovieAnonRateThrottle(SimpleRateThrottle):
    scope = "anon"
    rate = "5/min"

    def get_cache_key(self, request, view):
        fingerprint = get_fingerprint(request)
        return f"anon-{fingerprint}"


class MovieUserRateThrottle(SimpleRateThrottle):
    scope = "user"
    rate = "5/min"

    def get_cache_key(self, request, view):
        if request.user.is_authenticated:
            user_id = request.user.id
            fingerprint = get_fingerprint(request)
            return f"user-{user_id}-{fingerprint}"
        return None
