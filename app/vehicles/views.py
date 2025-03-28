from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from .models import Vehicle
from .serializers import VehicleSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsOwner()]
        return super().get_permissions()
    
    def get_queryset(self):
        return self.queryset.filter(customer=self.request.user.cliente_profile)

    def perform_create(self, serializer):
        print(self.request.user.cliente_profile)
        serializer.save(customer=self.request.user.cliente_profile)
