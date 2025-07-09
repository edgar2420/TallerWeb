from rest_framework import viewsets, generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from apps.cuerposagua.infrastructure.models import CuerpoAguaModel, ImagenCuerpoAgua
from apps.cuerposagua.serializers import CuerpoAguaSerializer, ImagenCuerpoAguaSerializer
from rest_framework.generics import RetrieveAPIView


# ViewSet principal con filtros por localidad, municipio y departamento
class CuerpoAguaViewSet(viewsets.ModelViewSet):
    queryset = CuerpoAguaModel.objects.all()
    serializer_class = CuerpoAguaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'localidad__nombre': ['exact', 'icontains'],
        'localidad__municipio__nombre': ['exact', 'icontains'],
        'localidad__municipio__departamento__nombre': ['exact', 'icontains'],
    }


# Subida de imágenes para galería
class SubirImagenCuerpoAguaView(generics.CreateAPIView):
    serializer_class = ImagenCuerpoAguaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        cuerpo_agua_id = self.kwargs.get('cuerpo_agua_id')
        serializer.save(cuerpo_agua_id=cuerpo_agua_id)



# Visualización detallada de un cuerpo de agua con galería e información de ubicación
class DetalleCuerpoAguaView(RetrieveAPIView):
    queryset = CuerpoAguaModel.objects.all()
    serializer_class = CuerpoAguaSerializer
    permission_classes = [permissions.AllowAny]
