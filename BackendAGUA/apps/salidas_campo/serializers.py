from rest_framework import serializers
from .infrastructure.models import SalidaCampoModel
from apps.usuarios.application.infrastructure.models import Usuario
from apps.cuerposagua.infrastructure.models import CuerpoAguaModel

class UsuarioSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'rol']

class CuerpoAguaSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuerpoAguaModel
        fields = ['id', 'nombre', 'tipo', 'latitud', 'longitud']

class SalidaCampoSerializer(serializers.ModelSerializer):
    contador_cuerpos_agua = serializers.SerializerMethodField()
    contador_analisis = serializers.SerializerMethodField()

    class Meta:
        model = SalidaCampoModel
        fields = '__all__'

    def get_contador_cuerpos_agua(self, obj):
        return obj.cuerpos_agua.count()

    def get_contador_analisis(self, obj):
        return obj.analisis.count()

    def update(self, instance, validated_data):
        if instance.analisis.exists():
            raise serializers.ValidationError("No se puede editar una salida de campo con análisis registrados.")
        return super().update(instance, validated_data)

class SalidaCampoDetalleSerializer(serializers.ModelSerializer):
    tecnicos = UsuarioSimpleSerializer(many=True, read_only=True)
    cuerpos_agua = CuerpoAguaSimpleSerializer(many=True, read_only=True)
    contador_cuerpos_agua = serializers.SerializerMethodField()
    contador_analisis = serializers.SerializerMethodField()

    class Meta:
        model = SalidaCampoModel
        fields = '__all__'

    def get_contador_cuerpos_agua(self, obj):
        return obj.cuerpos_agua.count()

    def get_contador_analisis(self, obj):
        return obj.analisis.count()

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SalidaCampoViewSet

router = DefaultRouter()
router.register(r'salidas-campo', SalidaCampoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
