from django.db import models

class SalidaCampoModel(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.TextField()

    tecnicos = models.ManyToManyField('usuarios.Usuario', related_name='salidas_asignadas')
    cuerpos_agua = models.ManyToManyField('cuerposagua.CuerpoAguaModel', related_name='salidas_programadas')

    condiciones_climaticas = models.CharField(max_length=255, blank=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Salida {self.id} - {self.fecha_inicio} a {self.fecha_fin}"

    def contador_cuerpos_agua(self):
        return self.cuerpos_agua.count()

    def contador_analisis(self):
        return self.analisis.count()