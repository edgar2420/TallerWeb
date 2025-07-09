from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnalisisViewSet, SubirImagenAnalisisView

router = DefaultRouter()
router.register(r'analisis', AnalisisViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('analisis/<int:analisis_id>/subir-imagen/', SubirImagenAnalisisView.as_view(), name='subir_imagen_analisis'),
]
