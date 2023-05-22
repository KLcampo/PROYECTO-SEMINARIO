from rest_framework import serializers
from .models import Ubicaciones, Restaurantes

class UbicacionesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ubicaciones
        fields = '__all__'

class RestaurantesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Restaurantes
        fields = '__all__'

