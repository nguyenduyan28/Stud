# Generated by Django 5.0.7 on 2024-08-28 05:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0024_alter_profile_role'),
        ('room', '0008_auto_20240823_0327'),
    ]

    operations = [
        migrations.CreateModel(
            name='tracking_time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.profile')),
            ],
        ),
    ]
