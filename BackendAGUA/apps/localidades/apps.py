from django.apps import AppConfig

class LocalidadesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.localidades'

    def ready(self):

        import apps.localidades.infrastructure.models
