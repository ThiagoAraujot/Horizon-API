from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.customer == request.user.cliente_profile or obj.mecanico == request.user.mecanico_profile
