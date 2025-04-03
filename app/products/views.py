from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsFornecedor


class CreateProductView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsFornecedor]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ListProductView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class RetrieveProductView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class UpdateProductView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsFornecedor]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class DeleteProductView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsFornecedor]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
