from django.contrib import admin
from .models import LocalidadModel

@admin.register(LocalidadModel)
class LocalidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'municipio', 'departamento')
    search_fields = ('nombre', 'municipio', 'departamento')
