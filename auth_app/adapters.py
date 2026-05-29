from urllib.parse import quote, urlencode

from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken

from .repositories import AccountTierRepository


def build_jwt_oauth_callback_url(request) -> str:
    """Redirect target for the Next.js app to store JWT in localStorage."""
    refresh = RefreshToken.for_user(request.user)
    query = urlencode(
        {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        },
        quote_via=quote,
    )
    stored = request.session.pop('oauth_return_origin', None)
    if isinstance(stored, str) and stored.strip():
        base = stored.strip().rstrip('/')
    else:
        base = settings.FRONTEND_URL.rstrip('/')
    return f'{base}/auth/google/callback/?{query}'


class MovieFinderAccountAdapter(DefaultAccountAdapter):
    """Allauth account logins (incl. Google) use this adapter for post-login redirect."""

    def get_login_redirect_url(self, request):  # type: ignore[override]
        if getattr(request, 'user', None) and request.user.is_authenticated:
            return build_jwt_oauth_callback_url(request)
        return super().get_login_redirect_url(request)

    def get_signup_redirect_url(self, request):  # type: ignore[override]
        if getattr(request, 'user', None) and request.user.is_authenticated:
            return build_jwt_oauth_callback_url(request)
        return super().get_signup_redirect_url(request)


class MovieFinderSocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):  # type: ignore[override]
        user = sociallogin.user
        if getattr(user, "account_tier_id", None) is None:
            user.account_tier = AccountTierRepository().resolve(None)
        return super().save_user(request, sociallogin, form=form)

    def get_login_redirect_url(self, request):  # type: ignore[override]
        return build_jwt_oauth_callback_url(request)

    def get_signup_redirect_url(self, request):  # type: ignore[override]
        return build_jwt_oauth_callback_url(request)

    def get_connect_redirect_url(self, request):  # type: ignore[override]
        return build_jwt_oauth_callback_url(request)
