from rest_framework import serializers
from apps.localidades.infrastructure.models import LocalidadModel

class LocalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalidadModel
        fields = '__all__'
