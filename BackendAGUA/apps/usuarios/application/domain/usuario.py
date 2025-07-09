class Usuario:
    def __init__(self, id, username, email, rol, activo=True):
        self.id = id
        self.username = username
        self.email = email
        self.rol = rol
        self.activo = activo

    def __str__(self):
        return f"{self.username} ({self.rol})"
