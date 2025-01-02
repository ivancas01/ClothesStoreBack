# tienda_ropa/serializers.py
from rest_framework import serializers
from .models import Coleccion, Elemento, TerminosLegales

class ElementoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elemento
        fields = '__all__'

class ColeccionSerializer(serializers.ModelSerializer):
    elementos = ElementoSerializer(many=True, read_only=True)

    class Meta:
        model = Coleccion
        fields = '__all__'

class TerminosLegalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TerminosLegales
        fields = '__all__'