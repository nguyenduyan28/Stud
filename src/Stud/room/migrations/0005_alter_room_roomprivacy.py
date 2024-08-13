# Generated by Django 5.0.7 on 2024-08-13 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0004_alter_image_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='roomPrivacy',
            field=models.CharField(choices=[('PR', 'private'), ('PB', 'public')], default='PB', max_length=10),
        ),
    ]