# Data migration: create a set of curated public collections (empty).
# Owner: first superuser, or first user. If no users exist, no collections are created.
# Seed is skipped when running under pytest (see 0006 for skip logic).

import os

from django.db import migrations

COLLECTIONS = [
    {'name': 'Новорічна', 'description': 'Фільми для новорічного настрою'},
    {'name': 'Хорор', 'description': 'Жахи та трилери'},
    {'name': 'Комедія', 'description': 'Комедійні фільми'},
    {'name': 'Драма', 'description': 'Драматичні фільми'},
    {'name': 'Бойовик', 'description': 'Бойовики та пригоди'},
    {'name': 'Романтика', 'description': 'Романтичні фільми'},
    {'name': 'Фантастика', 'description': 'Наукова фантастика та фентезі'},
    {'name': 'Документальні', 'description': 'Документальне кіно'},
    {'name': 'Аніме', 'description': 'Аніме та анімація'},
    {'name': 'Класика', 'description': 'Класичне кіно'},
    {'name': 'Для всієї родини', 'description': 'Фільми для перегляду з дітьми'},
    {'name': 'Топ IMDb', 'description': 'Популярні фільми за рейтингом'},
]


def seed_curated_collections(apps, schema_editor):
    if os.environ.get('DJANGO_TESTING') == '1':
        return
    db_name = schema_editor.connection.settings_dict.get('NAME', '')
    if db_name.startswith('test_'):
        return
    User = apps.get_model('auth_app', 'User')
    Collection = apps.get_model('collection', 'Collection')
    owner = User.objects.filter(is_superuser=True).first() or User.objects.first()
    if not owner:
        return
    for item in COLLECTIONS:
        Collection.objects.get_or_create(
            owner=owner,
            name=item['name'],
            defaults={
                'description': item['description'],
                'is_public': True,
            },
        )


def noop_reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('collection', '0004_collection_design'),
    ]

    operations = [
        migrations.RunPython(seed_curated_collections, noop_reverse),
    ]
