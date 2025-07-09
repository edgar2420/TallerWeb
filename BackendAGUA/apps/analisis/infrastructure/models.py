from django.db import models

class AnalisisModel(models.Model):
    TIPO_CHOICES = [
        ('turbidez', 'Turbidez'),
        ('caudal', 'Caudal'),
        ('ph', 'pH'),
        ('quimico', 'Análisis Químico'),
    ]

    salida_campo = models.ForeignKey('salidas_campo.SalidaCampoModel', on_delete=models.CASCADE, related_name='analisis')
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    parametro = models.CharField(max_length=100)
    valor = models.FloatField()
    unidad = models.CharField(max_length=20)
    fecha = models.DateField()

    ancho = models.FloatField(null=True, blank=True)
    profundidad = models.FloatField(null=True, blank=True)
    velocidad = models.FloatField(null=True, blank=True)
    caudal = models.FloatField(null=True, blank=True)
    observacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.tipo} - {self.parametro}"


class ImagenAnalisisModel(models.Model):
    analisis = models.ForeignKey(AnalisisModel, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='imagenes_analisis/')

    def __str__(self):
        return f"Imagen de {self.analisis.parametro}"