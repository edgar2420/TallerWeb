from django.urls import path
from .views import (
    CrearUsuarioView,
    PerfilUsuarioView,
    EditarUsuarioView,
    DesactivarUsuarioView,
    ListarUsuariosView
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('crear/', CrearUsuarioView.as_view(), name='crear_usuario'),
    path('perfil/', PerfilUsuarioView.as_view(), name='perfil_usuario'),
    path('editar/<int:pk>/', EditarUsuarioView.as_view(), name='editar_usuario'),
    path('desactivar/<int:pk>/', DesactivarUsuarioView.as_view(), name='desactivar_usuario'),
    path('listar/', ListarUsuariosView.as_view(), name='listar_usuarios'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
