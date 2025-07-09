from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SalidaCampoViewSet

router = DefaultRouter()
router.register(r'salidas-campo', SalidaCampoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]