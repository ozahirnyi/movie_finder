# Generated by Django 4.0.7 on 2022-09-23 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_likemovie_watchlatermovie_delete_userfavorite'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='likemovie',
            constraint=models.UniqueConstraint(fields=('user', 'movie'), name='like-user-movie-unique'),
        ),
    ]
