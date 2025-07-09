from rest_framework import viewsets
from apps.localidades.infrastructure.models import LocalidadModel
from apps.localidades.serializers import LocalidadSerializer

class LocalidadViewSet(viewsets.ModelViewSet):
    queryset = LocalidadModel.objects.all()
    serializer_class = LocalidadSerializer
