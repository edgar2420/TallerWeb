from .models import AnalisisModel

class AnalisisRepository:
    @staticmethod
    def listar():
        return AnalisisModel.objects.all()

    @staticmethod
    def obtener(id):
        return AnalisisModel.objects.get(id=id)

    @staticmethod
    def crear(data):
        return AnalisisModel.objects.create(**data)

    @staticmethod
    def actualizar(id, data):
        AnalisisModel.objects.filter(id=id).update(**data)
        return AnalisisModel.objects.get(id=id)

    @staticmethod
    def eliminar(id):
        AnalisisModel.objects.filter(id=id).delete()
