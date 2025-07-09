from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count
from .infrastructure.models import SalidaCampoModel
from .serializers import SalidaCampoSerializer, SalidaCampoDetalleSerializer
from apps.usuarios.application.permissions import IsAdministrador
from apps.analisis.infrastructure.models import AnalisisModel
from ..cuerposagua.infrastructure.models import CuerpoAguaModel


class SalidaCampoViewSet(viewsets.ModelViewSet):
    queryset = SalidaCampoModel.objects.all()
    serializer_class = SalidaCampoSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdministrador]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'tecnicos__id': ['exact'],
        'cuerpos_agua__id': ['exact'],
        'cuerpos_agua__localidad__municipio__departamento__id': ['exact'],
    }

    @action(detail=True, methods=['get'])
    def resumen(self, request, pk=None):
        salida = self.get_object()
        return Response({
            "id": salida.id,
            "descripcion": salida.descripcion,
            "fecha_inicio": salida.fecha_inicio,
            "fecha_fin": salida.fecha_fin,
            "condiciones_climaticas": salida.condiciones_climaticas,
            "observaciones": salida.observaciones,
            "tecnicos": [t.username for t in salida.tecnicos.all()],
            "cuerpos_agua": [
                {
                    "nombre": c.nombre,
                    "latitud": c.latitud,
                    "longitud": c.longitud,
                    "comunidad": c.localidad.nombre if c.localidad else None
                } for c in salida.cuerpos_agua.all()
            ],
            "total_cuerpos_agua": salida.cuerpos_agua.count(),
            "total_analisis": salida.analisis.count(),
        })

    @action(detail=False, methods=['get'])
    def reporte_por_comunidad(self, request):
        datos = (
            AnalisisModel.objects
            .values('salida_campo__cuerpos_agua__localidad__nombre')
            .annotate(total_analisis=Count('id'))
            .order_by('-total_analisis')
        )
        return Response(datos)

    @action(detail=False, methods=['get'])
    def reporte_por_cuerpo_agua(self, request):
        cuerpos = CuerpoAguaModel.objects.all()
        data = []

        for cuerpo in cuerpos:
            analisis = AnalisisModel.objects.filter(salida_campo__cuerpos_agua=cuerpo)
            analisis_data = [
                {
                    "id": a.id,
                    "tipo": a.tipo,
                    "parametro": a.parametro,
                    "valor": a.valor,
                    "unidad": a.unidad,
                    "fecha": a.fecha
                }
                for a in analisis
            ]
            data.append({
                "cuerpo_agua": cuerpo.nombre,
                "tipo": cuerpo.tipo,
                "localidad": cuerpo.localidad.nombre,
                "total_analisis": analisis.count(),
                "analisis": analisis_data
            })
        return Response(data)
    @action(detail=False, methods=['get'], url_path='mis-salidas')
    def mis_salidas(self, request):
        user = request.user
        if not user.es_tecnico():
            return Response({"error": "Solo los técnicos pueden acceder a esta vista."}, status=403)

        salidas = SalidaCampoModel.objects.filter(tecnicos=user)
        serializer = self.get_serializer(salidas, many=True)
        return Response(serializer.data)