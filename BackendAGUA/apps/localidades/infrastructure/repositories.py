from apps.localidades.infrastructure.models import LocalidadModel

class LocalidadRepository:
    @staticmethod
    def listar_todas():
        return LocalidadModel.objects.all()

    @staticmethod
    def obtener_por_id(localidad_id):
        return LocalidadModel.objects.get(id=localidad_id)

    @staticmethod
    def crear_localidad(data):
        return LocalidadModel.objects.create(**data)

    @staticmethod
    def actualizar_localidad(instance, data):
        for key, value in data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    @staticmethod
    def eliminar_localidad(instance):
        instance.delete()
