from rest_framework import serializers
from .models import Indicator

class IndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicator
        fields = '__all__' # Incluye todos los campos del modelo
