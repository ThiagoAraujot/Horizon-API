from rest_framework import permissions


class IsMecanico(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.role == 'mecanico'

class IsMecanicoOrFornecedor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.role == 'mecanico'or request.user.role == 'fornecedor'
