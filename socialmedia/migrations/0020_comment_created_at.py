# Generated by Django 4.0.1 on 2022-01-16 18:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialmedia', '0019_alter_post_created_at_alter_share_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
