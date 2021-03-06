# Generated by Django 4.0 on 2022-01-04 12:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialmedia', '0008_alter_comment_user_alter_like_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_shared',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='shared_content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 4, 18, 7, 11, 90872)),
        ),
    ]
