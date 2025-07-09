from rest_framework import serializers
from apps.cuerposagua.infrastructure.models import CuerpoAguaModel

from apps.cuerposagua.infrastructure.models import ImagenCuerpoAgua

class ImagenCuerpoAguaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenCuerpoAgua
        fields = ['id', 'imagen']

class CuerpoAguaSerializer(serializers.ModelSerializer):
    imagenes = ImagenCuerpoAguaSerializer(many=True, read_only=True)

    class Meta:
        model = CuerpoAguaModel
        fields = '__all__'
