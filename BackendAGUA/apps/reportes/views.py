from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .infrastructure.queries import (
    analisis_por_tecnico, analisis_por_fecha, analisis_totales_dashboard
)
from .serializers import FiltroFechaSerializer, TecnicoFiltroSerializer
from apps.usuarios.application.permissions import IsAdministrador


class ReportePorTecnicoView(APIView):
    permission_classes = [IsAuthenticated, IsAdministrador]

    def post(self, request):
        serializer = TecnicoFiltroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tecnico_id = serializer.validated_data['tecnico_id']
        data = analisis_por_tecnico(tecnico_id)
        return Response(data)


class ReportePorFechaView(APIView):
    permission_classes = [IsAuthenticated, IsAdministrador]

    def post(self, request):
        serializer = FiltroFechaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        fecha_inicio = serializer.validated_data['fecha_inicio']
        fecha_fin = serializer.validated_data['fecha_fin']
        data = analisis_por_fecha(fecha_inicio, fecha_fin)
        return Response(data)


class ReporteDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = analisis_totales_dashboard()
        return Response(data)
