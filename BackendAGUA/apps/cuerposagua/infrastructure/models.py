from django.db import models

class CuerpoAguaModel(models.Model):
    TIPO_CHOICES = [
        ('rio', 'Río'),
        ('laguna', 'Laguna'),
        ('arroyo', 'Arroyo'),
        ('humedal', 'Humedal'),
        ('otro', 'Otro'),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    ubicacion = models.TextField()

    localidad = models.ForeignKey(
        'localidades.LocalidadModel',
        on_delete=models.CASCADE,
        related_name='cuerpos_agua'
    )

    # 🌐 NUEVOS CAMPOS DE GEOLocalización
    latitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"


# 📸 NUEVO MODELO: Galería de imágenes
class ImagenCuerpoAgua(models.Model):
    cuerpo_agua = models.ForeignKey(CuerpoAguaModel, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='imagenes_cuerposagua/')

    def __str__(self):
        return f"Imagen de {self.cuerpo_agua.nombre}"
