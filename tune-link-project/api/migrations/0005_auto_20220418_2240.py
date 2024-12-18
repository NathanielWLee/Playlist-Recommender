# Generated by Django 3.2.12 on 2022-04-18 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_playlist_numsongs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=50, unique=True)),
                ('var', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Playlist',
        ),
    ]
