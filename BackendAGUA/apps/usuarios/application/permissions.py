from rest_framework.permissions import BasePermission

class IsAdministrador(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.rol == 'administrador'

class IsTecnico(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.rol == 'tecnico'