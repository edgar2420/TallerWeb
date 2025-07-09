from django.contrib import admin
from apps.analisis.infrastructure.models import AnalisisModel

@admin.register(AnalisisModel)
class AnalisisAdmin(admin.ModelAdmin):
    list_display = ('salida_campo', 'fecha_analisis', 'parametro', 'valor', 'unidad')
    search_fields = ('parametro', 'salida_campo__id')
    list_filter = ('parametro',)
