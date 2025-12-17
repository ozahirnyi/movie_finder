from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('movie', '0012_topmovie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='title_ua',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
    ]
