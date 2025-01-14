import hashlib
from user_agents import parse


def get_fingerprint(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    ip_address = request.META.get('REMOTE_ADDR', '')

    ua = parse(user_agent)
    device_info = f"{ua.browser.family}-{ua.os.family}-{ua.device.family}"

    fingerprint_data = f"{device_info}-{ip_address}"
    fingerprint_hash = hashlib.sha256(fingerprint_data.encode()).hexdigest()

    return fingerprint_hash
