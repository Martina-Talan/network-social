# Generated by Django 4.1.5 on 2023-09-24 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0019_remove_newpost_likes_newpost_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newpost',
            name='likes',
        ),
        migrations.AddField(
            model_name='newpost',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
