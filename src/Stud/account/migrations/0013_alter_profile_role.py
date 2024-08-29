# Generated by Django 5.0.7 on 2024-08-13 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_merge_20240813_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.TextField(choices=[('LN', 'learner'), ('AD', 'admin'), ('HO', 'host')], default='LN', max_length=10),
        ),
    ]
