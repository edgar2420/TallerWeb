from rest_framework import generics, permissions
from apps.usuarios.application.infrastructure.models import Usuario
from apps.usuarios.serializers import UsuarioSerializer
from apps.usuarios.application.crear_usuario import CrearUsuarioUseCase
from apps.usuarios.application.editar_usuario import EditarUsuarioUseCase
from apps.usuarios.application.permissions import IsAdministrador

class CrearUsuarioView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        use_case = CrearUsuarioUseCase(serializer.validated_data)
        use_case.execute()

class PerfilUsuarioView(generics.RetrieveAPIView):
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class EditarUsuarioView(generics.UpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAdministrador]

    def perform_update(self, serializer):
        use_case = EditarUsuarioUseCase(self.get_object().id, serializer.validated_data)
        use_case.execute()

class DesactivarUsuarioView(generics.UpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAdministrador]

    def perform_update(self, serializer):
        usuario = self.get_object()
        usuario.is_active = False
        usuario.save()

class ListarUsuariosView(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAdministrador]
