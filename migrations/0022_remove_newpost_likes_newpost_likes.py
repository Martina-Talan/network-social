# Generated by Django 4.1.5 on 2023-09-24 09:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0021_rename_postlike_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newpost',
            name='likes',
        ),
        migrations.AddField(
            model_name='newpost',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
