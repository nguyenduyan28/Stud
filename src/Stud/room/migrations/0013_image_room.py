# Generated by Django 5.0.7 on 2024-08-28 16:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0012_room_invite_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='room',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='room.room'),
        ),
    ]
