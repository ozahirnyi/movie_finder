import django.db.models.deletion
from django.db import migrations, models


def create_account_tiers(apps, schema_editor):
    AccountTier = apps.get_model('auth_app', 'AccountTier')
    User = apps.get_model('auth_app', 'User')

    tiers = [
        ('free', 'Free', 3, True),
        ('premium', 'Premium', 30, False),
        ('admin', 'Admin', 100, False),
    ]

    default_tier = None
    for code, name, limit, is_default in tiers:
        tier, created = AccountTier.objects.get_or_create(
            code=code,
            defaults={
                'name': name,
                'daily_ai_search_limit': limit,
                'is_default': is_default,
            },
        )
        if not created:
            tier.name = name
            tier.daily_ai_search_limit = limit
            tier.is_default = is_default
            tier.save(update_fields=['name', 'daily_ai_search_limit', 'is_default'])
        if is_default:
            default_tier = tier

    if default_tier is None:
        default_tier = AccountTier.objects.filter(code='free').first()

    if default_tier:
        AccountTier.objects.exclude(pk=default_tier.pk).update(is_default=False)
        User.objects.filter(account_tier__isnull=True).update(account_tier=default_tier)


class Migration(migrations.Migration):
    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountTier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(choices=[('free', 'Free'), ('premium', 'Premium'), ('admin', 'Admin')], max_length=32, unique=True)),
                ('name', models.CharField(max_length=64)),
                ('daily_ai_search_limit', models.PositiveIntegerField(default=0)),
                ('is_default', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='user',
            name='ai_search_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='ai_search_count_reset_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='account_tier',
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='users', to='auth_app.accounttier'
            ),
        ),
        migrations.RunPython(create_account_tiers, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='user',
            name='account_tier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='users', to='auth_app.accounttier'),
        ),
    ]
