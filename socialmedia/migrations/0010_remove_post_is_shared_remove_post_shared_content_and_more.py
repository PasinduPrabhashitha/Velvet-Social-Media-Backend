# Generated by Django 4.0.1 on 2022-01-05 02:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialmedia', '0009_post_is_shared_post_shared_content_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='is_shared',
        ),
        migrations.RemoveField(
            model_name='post',
            name='shared_content',
        ),
        migrations.AddField(
            model_name='share',
            name='shared_content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 5, 8, 12, 47, 819945)),
        ),
    ]
