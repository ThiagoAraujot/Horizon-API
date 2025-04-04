from rest_framework import generics
from .models import OrderItem
from .serializers import OrderItemSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsMecanico, IsMecanicoOrFornecedor


class CreateOrderItemView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsMecanico]
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()


class ListOrderItemView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsMecanicoOrFornecedor]
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()


class RetrieveOrderItemView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsMecanicoOrFornecedor]
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()


class UpdateOrderItemView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsMecanico]
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()


class DeleteOrderItemView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsMecanico]
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
