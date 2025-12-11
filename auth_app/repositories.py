from django.db import transaction
from django.utils import timezone

from .exceptions import AiSearchLimitExceeded
from .models import AccountTier, User


class AccountTierRepository:
    def resolve(self, account_tier: AccountTier | None) -> AccountTier:
        if account_tier:
            return account_tier
        default_tier = self.get_default()
        if default_tier:
            return default_tier
        fallback = self.get_first()
        if fallback:
            return fallback
        raise ValueError('No account tiers configured. Create one via admin first.')

    def get_default(self) -> AccountTier | None:
        return AccountTier.objects.filter(is_default=True).first()

    def get_first(self) -> AccountTier | None:
        return AccountTier.objects.first()

    def enforce_single_default(self, tier: AccountTier) -> None:
        if tier.is_default:
            AccountTier.objects.exclude(pk=tier.pk).update(is_default=False)


class UserRepository:
    def consume_ai_search_quota(self, user: User) -> User:
        today = timezone.now().date()
        with transaction.atomic():
            locked_user = User.objects.select_for_update().get(pk=user.pk)
            if locked_user.ai_search_count_reset_at != today:
                locked_user.ai_search_count = 0
                locked_user.ai_search_count_reset_at = today

            limit = locked_user.account_tier.daily_ai_search_limit
            if limit and locked_user.ai_search_count >= limit:
                raise AiSearchLimitExceeded

            locked_user.ai_search_count += 1
            locked_user.save(update_fields=['ai_search_count', 'ai_search_count_reset_at'])

        user.ai_search_count = locked_user.ai_search_count
        user.ai_search_count_reset_at = locked_user.ai_search_count_reset_at
        return user
