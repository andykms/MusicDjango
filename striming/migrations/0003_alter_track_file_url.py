# Generated by Django 5.1.5 on 2025-01-30 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('striming', '0002_alter_album_cover_url_alter_artist_photo_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='file_url',
            field=models.FileField(blank=True, null=True, upload_to='tracks/'),
        ),
    ]
