# Generated by Django 5.0.7 on 2024-11-15 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_alter_movie_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='plot',
            field=models.TextField(null=True),
        ),
    ]
