# Generated by Django 4.1.5 on 2023-09-24 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0023_alter_newpost_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpost',
            name='post',
            field=models.TextField(default=True, max_length=1000),
        ),
    ]
