# Generated by Django 4.1.5 on 2023-09-24 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0022_remove_newpost_likes_newpost_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpost',
            name='post',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
