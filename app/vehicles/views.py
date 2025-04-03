from rest_framework import generics
from .models import Vehicle
from .serializers import VehicleSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner


class CreateVehicleView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user.cliente_profile)


class ListVehicleView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()


class RetrieveVehicleView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()


class UpdateVehicleView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()


class DeleteVehicleView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
