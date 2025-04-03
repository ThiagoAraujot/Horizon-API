from .models import Scheduling
from rest_framework import generics
from .models import Scheduling
from .serializers import SchedulingSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner


class CreateSchedulingView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SchedulingSerializer
    queryset = Scheduling.objects.all()

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user.cliente_profile)


class ListSchedulingView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = SchedulingSerializer
    queryset = Scheduling.objects.all()

    def get_queryset(self):
        if self.request.user.role == 'cliente':
            return self.queryset.filter(customer=self.request.user.cliente_profile)
        elif self.request.user.role == 'mecanico':
            return self.queryset.filter(mecanico=self.request.user.mecanico_profile)
        else:
            return Scheduling.objects.all()


class RetrieveSchedulingView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = SchedulingSerializer
    queryset = Scheduling.objects.all()


class UpdateSchedulingView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = SchedulingSerializer
    queryset = Scheduling.objects.all()


class DeleteSchedulingView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = SchedulingSerializer
    queryset = Scheduling.objects.all()
