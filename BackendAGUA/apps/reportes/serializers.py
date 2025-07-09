from rest_framework import serializers

class FiltroFechaSerializer(serializers.Serializer):
    fecha_inicio = serializers.DateField()
    fecha_fin = serializers.DateField()

class TecnicoFiltroSerializer(serializers.Serializer):
    tecnico_id = serializers.IntegerField()
