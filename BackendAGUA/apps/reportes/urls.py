from django.urls import path
from .views import (
    ReportePorTecnicoView,
    ReportePorFechaView,
    ReporteDashboardView
)

urlpatterns = [
    path('por-tecnico/', ReportePorTecnicoView.as_view(), name='reporte_por_tecnico'),
    path('por-fecha/', ReportePorFechaView.as_view(), name='reporte_por_fecha'),
    path('dashboard/', ReporteDashboardView.as_view(), name='reporte_dashboard'),
]
