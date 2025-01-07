from rest_framework.throttling import SimpleRateThrottle


class IpBasedRateThrottle(SimpleRateThrottle):
    scope = "ip"
    rate = "10/day"

    def get_cache_key(self, request, view):
        ip_address = request.META.get('REMOTE_ADDR', '')
        if not ip_address:
            return None
        return f"ip-{ip_address}"


class UserAgentRateThrottle(SimpleRateThrottle):
    scope = "user_agent"
    rate = "2/day"

    def get_cache_key(self, request, view):
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        if not user_agent:
            return None
        return f"user_agent-{user_agent}"
