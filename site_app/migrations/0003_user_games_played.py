# Generated by Django 2.2 on 2021-08-24 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0002_gamesplayed'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='games_played',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
