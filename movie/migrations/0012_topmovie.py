import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('movie', '0011_alter_recommendedmovie_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('position', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='top_entries', to='movie.movie')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.AddConstraint(
            model_name='topmovie',
            constraint=models.UniqueConstraint(fields=('generated_at', 'position'), name='top_movie_unique_position_per_batch'),
        ),
        migrations.AddConstraint(
            model_name='topmovie',
            constraint=models.UniqueConstraint(fields=('generated_at', 'movie'), name='top_movie_unique_movie_per_batch'),
        ),
    ]
