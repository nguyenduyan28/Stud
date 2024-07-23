# Generated by Django 4.1.5 on 2024-07-23 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0004_alter_profile_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="role",
            field=models.TextField(
                choices=[("LN", "learner"), ("HO", "host"), ("AD", "admin")],
                default="LN",
                max_length=10,
            ),
        ),
    ]