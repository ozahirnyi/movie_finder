from rest_framework.throttling import SimpleRateThrottle


class UaBaseThrottle(SimpleRateThrottle):
    scope = "ua"

    def get_cache_key(self, request, view):
        user_agent = request.META.get('HTTP_USER_AGENT')
        if not user_agent:
            return None
        return f"throttle_ua_{user_agent}"


class IpBaseThrottle(SimpleRateThrottle):
    scope = "ip"

    def get_cache_key(self, request, view):
        ip_address = self.get_ident(request)
        return f"throttle_ip_{ip_address}"


class ForwardedForBaseThrottle(SimpleRateThrottle):
    scope = "forwarded"

    def get_cache_key(self, request, view):
        forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if not forwarded_for:
            return None

        client_ip = forwarded_for.split(',')[0].strip()
        return f"throttle_forwarded_{client_ip}"


class AiSearchUaThrottle(UaBaseThrottle):
    scope = "ai_search_ua"
    rate = "2/day"


class AiSearchIpThrottle(IpBaseThrottle):
    scope = "ai_search_ip"
    rate = "6/day"


class AiSearchForwardedThrottle(ForwardedForBaseThrottle):
    scope = "ai_search_forwarded"
    rate = "6/day"


class RegularSearchUaThrottle(UaBaseThrottle):
    scope = "regular_search_ua"
    rate = "10/day"


class RegularSearchIpThrottle(IpBaseThrottle):
    scope = "regular_search_ip"
    rate = "20/day"


class RegularSearchForwardedThrottle(ForwardedForBaseThrottle):
    scope = "regular_search_forwarded"
    rate = "20/day"
