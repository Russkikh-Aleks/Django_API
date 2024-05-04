# Generated by Django 5.0.4 on 2024-05-04 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_alter_measurement_id_sensor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurement',
            name='image',
        ),
        migrations.AlterField(
            model_name='measurement',
            name='temperature',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
