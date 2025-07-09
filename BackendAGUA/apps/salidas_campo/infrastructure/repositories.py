from .models import SalidaCampoModel

class SalidaCampoRepository:
    @staticmethod
    def listar_salidas():
        return SalidaCampoModel.objects.all()

    @staticmethod
    def crear_salida(data):
        return SalidaCampoModel.objects.create(**data)

    @staticmethod
    def obtener_por_id(salida_id):
        return SalidaCampoModel.objects.get(id=salida_id)

    @staticmethod
    def actualizar_salida(salida, data):
        for attr, value in data.items():
            setattr(salida, attr, value)
        salida.save()
        return salida

    @staticmethod
    def eliminar_salida(salida):
        salida.delete()
