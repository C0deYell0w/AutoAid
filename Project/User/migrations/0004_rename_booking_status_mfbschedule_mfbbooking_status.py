# Generated by Django 4.1.5 on 2023-02-08 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_mfbschedule'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mfbschedule',
            old_name='booking_status',
            new_name='mfbbooking_status',
        ),
    ]