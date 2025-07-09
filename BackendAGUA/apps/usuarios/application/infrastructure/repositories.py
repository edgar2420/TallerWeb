from apps.usuarios.application.infrastructure.models import Usuario as UsuarioModel
from apps.usuarios.application.domain.usuario import Usuario

class UsuarioRepository:
    def get_by_id(self, id):
        user = UsuarioModel.objects.get(id=id)
        return Usuario(
            id=user.id,
            username=user.username,
            email=user.email,
            rol=user.rol,
            activo=user.activo
        )

    def save(self, usuario: Usuario):
        return UsuarioModel.objects.create(
            username=usuario.username,
            email=usuario.email,
            rol=usuario.rol,
            activo=usuario.activo
        )
