from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings
from apps.cuerposagua.views import (
    CuerpoAguaViewSet,
    SubirImagenCuerpoAguaView,
    DetalleCuerpoAguaView
)

router = DefaultRouter()
router.register(r'cuerpos-agua', CuerpoAguaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(
        'cuerpos-agua/<int:cuerpo_agua_id>/subir-imagen/',
        SubirImagenCuerpoAguaView.as_view(),
        name='subir_imagen'
    ),
    path(
        'cuerpos-agua/<int:pk>/detalle/',
        DetalleCuerpoAguaView.as_view(),
        name='detalle_cuerpo_agua'
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
