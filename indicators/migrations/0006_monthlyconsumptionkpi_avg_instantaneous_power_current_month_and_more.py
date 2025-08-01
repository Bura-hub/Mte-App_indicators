# Generated by Django 5.2.4 on 2025-07-24 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0005_remove_monthlyconsumptionkpi_total_exported_current_month_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthlyconsumptionkpi',
            name='avg_instantaneous_power_current_month',
            field=models.FloatField(default=0.0, help_text='Potencia instantánea promedio de inversores del mes actual en Watts.'),
        ),
        migrations.AddField(
            model_name='monthlyconsumptionkpi',
            name='avg_instantaneous_power_previous_month',
            field=models.FloatField(default=0.0, help_text='Potencia instantánea promedio de inversores del mes anterior en Watts.'),
        ),
    ]
