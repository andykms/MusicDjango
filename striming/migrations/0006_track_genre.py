# Generated by Django 5.1.5 on 2025-01-31 01:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('striming', '0005_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='striming.genre', verbose_name='Жанр'),
        ),
    ]
