from django.db import models

class LocalidadModel(models.Model):
    nombre = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre} - {self.municipio}, {self.departamento}'
