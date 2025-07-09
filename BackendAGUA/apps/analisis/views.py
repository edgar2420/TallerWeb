from rest_framework import viewsets, generics, permissions
from .infrastructure.models import AnalisisModel, ImagenAnalisisModel
from .serializers import AnalisisSerializer, ImagenAnalisisSerializer

class AnalisisViewSet(viewsets.ModelViewSet):
    queryset = AnalisisModel.objects.all()
    serializer_class = AnalisisSerializer

class SubirImagenAnalisisView(generics.CreateAPIView):
    queryset = ImagenAnalisisModel.objects.all()
    serializer_class = ImagenAnalisisSerializer
    permission_classes = [permissions.IsAuthenticated]