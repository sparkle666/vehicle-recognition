# Generated by Django 4.2 on 2024-01-08 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_vehicleimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleimage',
            name='plate_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]