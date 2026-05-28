from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

from .repositories import AccountTierRepository


class MovieFinderSocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):  # type: ignore[override]
        user = sociallogin.user
        if getattr(user, "account_tier_id", None) is None:
            user.account_tier = AccountTierRepository().resolve(None)
        return super().save_user(request, sociallogin, form=form)

