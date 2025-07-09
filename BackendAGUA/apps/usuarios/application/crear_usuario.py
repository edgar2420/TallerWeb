from apps.usuarios.application.infrastructure.models import Usuario

class CrearUsuarioUseCase:
    def __init__(self, data):
        self.data = data

    def execute(self):
        return Usuario.objects.create_user(**self.data)
