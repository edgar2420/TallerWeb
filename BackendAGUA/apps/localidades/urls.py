from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.localidades.views import LocalidadViewSet

router = DefaultRouter()
router.register(r'localidades', LocalidadViewSet, basename='localidades')

urlpatterns = [
    path('', include(router.urls)),
]
