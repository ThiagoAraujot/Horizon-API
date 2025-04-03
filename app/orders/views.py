from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsMecanico, IsMecanicoOrFornecedor


class CreateOrderView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsMecanico]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def perform_create(self, serializer):
        serializer.save(mecanico=self.request.user.mecanico_profile)


class ListOrderView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsMecanicoOrFornecedor]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.role == 'mecanico':
            queryset = queryset.filter(
                mecanico=self.request.user.mecanico_profile)
        elif self.request.user.role == 'fornecedor':
            queryset = queryset.filter(
                fornecedor=self.request.user.fornecedor_profile)
        return queryset


class RetrieveOrderView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsMecanicoOrFornecedor]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class UpdateOrderView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsMecanico]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class DeleteOrderView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsMecanico]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
