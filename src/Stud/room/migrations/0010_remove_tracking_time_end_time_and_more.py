# Generated by Django 5.0.7 on 2024-08-29 04:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0009_tracking_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracking_time',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='tracking_time',
            name='start_time',
        ),
        migrations.AddField(
            model_name='tracking_time',
            name='num_sessions',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tracking_time',
            name='total_time',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
    ]