# Generated by Django 4.0.1 on 2022-01-06 07:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialmedia', '0014_alter_friend_date_confirmed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 6, 12, 49, 6, 11564)),
        ),
    ]
