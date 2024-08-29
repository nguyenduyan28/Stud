# Generated by Django 5.0.7 on 2024-08-28 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0023_alter_profile_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.TextField(choices=[('LN', 'learner'), ('AD', 'admin'), ('HO', 'host')], default='LN', max_length=10),
        ),
    ]
