from django.contrib.auth.hashers import make_password
from django.db import migrations


def create_default_admin(apps, schema_editor):
    User = apps.get_model('auth_app', 'User')
    AccountTier = apps.get_model('auth_app', 'AccountTier')

    email = 'admin@admin.com'
    password = 'Aa!1023654'

    if User.objects.filter(email=email).exists():
        return

    admin_tier, _ = AccountTier.objects.get_or_create(
        code='admin',
        defaults={'name': 'Admin', 'daily_ai_search_limit': 100, 'is_default': False},
    )

    User.objects.create(
        email=email,
        account_tier=admin_tier,
        is_staff=True,
        is_superuser=True,
        password=make_password(password),
    )


def delete_default_admin(apps, schema_editor):
    User = apps.get_model('auth_app', 'User')
    User.objects.filter(email='admin@admin.com').delete()


class Migration(migrations.Migration):
    dependencies = [
        ('auth_app', '0002_account_tiers'),
    ]

    operations = [
        migrations.RunPython(create_default_admin, delete_default_admin),
    ]
