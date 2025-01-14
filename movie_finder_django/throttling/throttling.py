from rest_framework.throttling import SimpleRateThrottle


class IpBasedRateThrottle(SimpleRateThrottle):
    scope = "ip"
    rate = "6/day"

    def get_cache_key(self, request, view):
        ip_address = request.META.get('REMOTE_ADDR', '')
        if not ip_address:
            raise ValueError("Cannot determine IP address of the client.")
        return f"ip-{ip_address}"



class UserAgentRateThrottle(SimpleRateThrottle):
    scope = "user_agent"
    rate = "2/day"

    def get_cache_key(self, request, view):
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        if not user_agent:
            raise ValueError("No User-Agent found in the request.")
        return f"user_agent-{user_agent}"
