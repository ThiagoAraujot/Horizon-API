from rest_framework import serializers
from .models import OrderItem
from products.models import Product
from products.serializers import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), write_only=True)
    order = serializers.PrimaryKeyRelatedField(
        queryset=OrderItem.objects.all(), write_only=True)

    product_data = ProductSerializer(source="product", read_only=True)
    order_data = serializers.PrimaryKeyRelatedField(
        source="order", read_only=True)

    class Meta:
        model = OrderItem
        fields = '__all__'
