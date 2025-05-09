from rest_framework import permissions


class IsFornecedor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.role == 'fornecedor'
