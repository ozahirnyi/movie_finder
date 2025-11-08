from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class AccountTierCode(models.TextChoices):
    FREE = ('free', 'Free')
    PREMIUM = ('premium', 'Premium')
    ADMIN = ('admin', 'Admin')


class AccountTier(models.Model):
    code = models.CharField(max_length=32, choices=AccountTierCode.choices, unique=True)
    name = models.CharField(max_length=64)
    daily_ai_search_limit = models.PositiveIntegerField(default=0)
    is_default = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return f'{self.name} ({self.daily_ai_search_limit}/day)'


class UserManager(BaseUserManager):
    def _resolve_account_tier(self, account_tier: 'AccountTier | None' = None) -> 'AccountTier':
        from .repositories import AccountTierRepository

        return AccountTierRepository().resolve(account_tier)

    def create_user(self, email, password=None, account_tier: AccountTier | None = None, **extra_fields):
        if email is None:
            raise TypeError('Users must have an email address.')

        tier = self._resolve_account_tier(account_tier)
        user = self.model(email=self.normalize_email(email), account_tier=tier, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        if password is None:
            raise TypeError('Superusers must have a password.')

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        user = self.create_user(email, password, **extra_fields)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(db_index=True, unique=True)
    account_tier = models.ForeignKey(AccountTier, on_delete=models.PROTECT, related_name='users')
    ai_search_count = models.PositiveIntegerField(default=0)
    ai_search_count_reset_at = models.DateField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email
