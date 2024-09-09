# Generated by Django 5.1.1 on 2024-09-08 19:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_manga', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manga',
            name='artist',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api_manga.artist'),
        ),
    ]
