from django.contrib import admin
from .models import SalidaCampoModel

@admin.register(SalidaCampoModel)
class SalidaCampoAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha_inicio', 'fecha_fin', 'descripcion_corta', 'contador_cuerpos_agua', 'contador_analisis')
    filter_horizontal = ('tecnicos', 'cuerpos_agua')
    search_fields = ('descripcion',)
    list_filter = ('fecha_inicio', 'fecha_fin')

    def descripcion_corta(self, obj):
        return obj.descripcion[:50] + '...' if len(obj.descripcion) > 50 else obj.descripcion

    descripcion_corta.short_description = 'Descripción'