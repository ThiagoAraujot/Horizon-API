from rest_framework import serializers
from .models import Order
from users.models import FornecedorProfile
from users.serializers import MecanicoProfileSerializer


class OrderSerializer(serializers.ModelSerializer):
    fornecedor = serializers.PrimaryKeyRelatedField(
        queryset=FornecedorProfile.objects.all(), write_only=True)

    fornecedor_data = MecanicoProfileSerializer(
        source="fornecedor", read_only=True)
    mecanico_data = MecanicoProfileSerializer(
        source="mecanico", read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        extra_kwargs = {'mecanico': {'read_only': True}}
