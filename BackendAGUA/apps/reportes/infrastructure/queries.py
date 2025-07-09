from apps.analisis.infrastructure.models import AnalisisModel
from django.db.models import Count, Q
from datetime import date

def analisis_por_tecnico(tecnico_id):
    return AnalisisModel.objects.filter(
        salida_campo__tecnicos__id=tecnico_id
    ).values('tipo').annotate(total=Count('id'))

def analisis_por_fecha(fecha_inicio, fecha_fin):
    return AnalisisModel.objects.filter(
        fecha__range=(fecha_inicio, fecha_fin)
    ).values('tipo').annotate(total=Count('id'))

def analisis_totales_dashboard():
    return AnalisisModel.objects.values('tipo').annotate(total=Count('id'))
