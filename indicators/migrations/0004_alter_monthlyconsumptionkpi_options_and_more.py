# Generated by Django 5.2.4 on 2025-07-23 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0003_alter_monthlyconsumptionkpi_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='monthlyconsumptionkpi',
            options={'verbose_name': 'KPI de Consumo, Generación y Balance Mensual', 'verbose_name_plural': 'KPIs de Consumo, Generación y Balance Mensual'},
        ),
        migrations.AddField(
            model_name='monthlyconsumptionkpi',
            name='total_exported_current_month',
            field=models.FloatField(default=0.0, help_text='Energía total exportada del mes actual en kWh.'),
        ),
        migrations.AddField(
            model_name='monthlyconsumptionkpi',
            name='total_exported_previous_month',
            field=models.FloatField(default=0.0, help_text='Energía total exportada del mes anterior en kWh.'),
        ),
        migrations.AddField(
            model_name='monthlyconsumptionkpi',
            name='total_imported_current_month',
            field=models.FloatField(default=0.0, help_text='Energía total importada del mes actual en kWh.'),
        ),
        migrations.AddField(
            model_name='monthlyconsumptionkpi',
            name='total_imported_previous_month',
            field=models.FloatField(default=0.0, help_text='Energía total importada del mes anterior en kWh.'),
        ),
    ]
