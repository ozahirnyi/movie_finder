# Generated by Django 3.2.9 on 2021-12-08 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0006_alter_favoritemovieuser_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='favoritemovieuser',
            name='poster',
            field=models.CharField(max_length=255, null=True),
        ),
    ]