from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLES = (
        ('administrador', 'Administrador'),
        ('tecnico', 'Técnico'),
    )
    rol = models.CharField(max_length=20, choices=ROLES)

    def es_administrador(self):
        return self.rol == 'administrador'

    def es_tecnico(self):
        return self.rol == 'tecnico'
