from rest_framework import serializers
from .infrastructure.models import AnalisisModel, ImagenAnalisisModel

class ImagenAnalisisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenAnalisisModel
        fields = ['id', 'imagen']


class AnalisisSerializer(serializers.ModelSerializer):
    imagenes = ImagenAnalisisSerializer(many=True, read_only=True)

    class Meta:
        model = AnalisisModel
        fields = '__all__'

    def validate(self, data):
        tipo = data.get('tipo')
        valor = data.get('valor')
        if tipo == 'turbidez':
            if valor < 0:
                raise serializers.ValidationError("El valor de NTU no puede ser negativo.")
        return data

    def create(self, validated_data):
        if validated_data.get("tipo") == "caudal":
            ancho = validated_data.get("ancho") or 0
            profundidad = validated_data.get("profundidad") or 0
            velocidad = validated_data.get("velocidad") or 0
            validated_data["caudal"] = ancho * profundidad * velocidad
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if validated_data.get("tipo") == "caudal":
            ancho = validated_data.get("ancho") or instance.ancho or 0
            profundidad = validated_data.get("profundidad") or instance.profundidad or 0
            velocidad = validated_data.get("velocidad") or instance.velocidad or 0
            validated_data["caudal"] = ancho * profundidad * velocidad
        return super().update(instance, validated_data)