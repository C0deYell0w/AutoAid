# Generated by Django 4.1.5 on 2023-01-30 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_district'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicletype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(max_length=50)),
            ],
        ),
    ]
