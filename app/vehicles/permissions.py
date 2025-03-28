from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Permissão personalizada que permite que um usuário
    apenas modifique seu próprio perfil.
    """

    def has_object_permission(self, request, view, obj):
        return obj.customer == request.user.cliente_profile
