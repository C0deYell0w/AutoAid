# Generated by Django 4.1.5 on 2023-02-08 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0006_admindb_newusr_usr_photo'),
        ('User', '0004_rename_booking_status_mfbschedule_mfbbooking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mfbschedule',
            name='mfbid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.newmfb'),
        ),
    ]