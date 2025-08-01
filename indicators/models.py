from django.db import models

class MonthlyConsumptionKPI(models.Model):
    """
    Modelo para almacenar los KPIs de consumo, generación y balance total mensual pre-calculados.
    Solo debe haber una instancia de este modelo.
    """
    total_consumption_current_month = models.FloatField(default=0.0, help_text="Consumo total acumulado del mes actual en kWh.")
    total_consumption_previous_month = models.FloatField(default=0.0, help_text="Consumo total acumulado del mes anterior en kWh.")
    
    total_generation_current_month = models.FloatField(default=0.0, help_text="Generación total acumulada del mes actual en Wh.")
    total_generation_previous_month = models.FloatField(default=0.0, help_text="Generación total acumulada del mes anterior en Wh.")

    avg_instantaneous_power_current_month = models.FloatField(default=0.0, help_text="Potencia instantánea promedio de inversores del mes actual en Watts.")
    avg_instantaneous_power_previous_month = models.FloatField(default=0.0, help_text="Potencia instantánea promedio de inversores del mes anterior en Watts.")

    avg_daily_temp_current_month = models.FloatField(default=0.0, help_text="Temperatura promedio diaria del mes actual en °C.")
    avg_daily_temp_previous_month = models.FloatField(default=0.0, help_text="Temperatura promedio diaria del mes anterior en °C.")

    avg_relative_humidity_current_month = models.FloatField(default=0.0, help_text="Humedad relativa promedio del mes actual en %RH.")
    avg_relative_humidity_previous_month = models.FloatField(default=0.0, help_text="Humedad relativa promedio del mes anterior en %RH.")

    # Nuevos campos para la velocidad del viento promedio (en km/h)
    avg_wind_speed_current_month = models.FloatField(default=0.0, help_text="Velocidad del viento promedio del mes actual en km/h.")
    avg_wind_speed_previous_month = models.FloatField(default=0.0, help_text="Velocidad del viento promedio del mes anterior en km/h.")

    last_calculated = models.DateTimeField(auto_now=True, help_text="Fecha y hora de la última vez que se calculó este KPI.")

    class Meta:
        verbose_name = "KPI de Consumo, Generación y Balance Mensual"
        verbose_name_plural = "KPIs de Consumo, Generación y Balance Mensual"

    def __str__(self):
        return f"KPI Mensual (Actualizado: {self.last_calculated.strftime('%Y-%m-%d %H:%M')})"