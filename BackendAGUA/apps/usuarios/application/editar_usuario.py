from apps.usuarios.application.infrastructure.models import Usuario

class EditarUsuarioUseCase:
    def __init__(self, usuario_id, datos):
        self.usuario_id = usuario_id
        self.datos = datos

    def execute(self):
        usuario = Usuario.objects.get(id=self.usuario_id)
        for key, value in self.datos.items():
            setattr(usuario, key, value)
        usuario.save()