# Generated by Django 4.2 on 2023-07-20 15:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_app', '0013_alter_pokemon_date_captured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='date_captured',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 20, 15, 52, 1, 815959, tzinfo=datetime.timezone.utc)),
        ),
    ]