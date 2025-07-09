from apps.cuerposagua.infrastructure.models import CuerpoAguaModel

class CuerpoAguaRepository:
    @staticmethod
    def listar():
        return CuerpoAguaModel.objects.all()

    @staticmethod
    def obtener(id):
        return CuerpoAguaModel.objects.get(pk=id)

    @staticmethod
    def crear(datos):
        return CuerpoAguaModel.objects.create(**datos)

    @staticmethod
    def actualizar(instancia, datos):
        for key, value in datos.items():
            setattr(instancia, key, value)
        instancia.save()
        return instancia

    @staticmethod
    def eliminar(id):
        instancia = CuerpoAguaModel.objects.get(pk=id)
        instancia.delete()