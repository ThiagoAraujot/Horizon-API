from rest_framework import serializers
from .models import Product
from users.models import FornecedorProfile
from users.serializers import FornecedorProfileSerializer


class ProductSerializer(serializers.ModelSerializer):
    fornecedor = serializers.PrimaryKeyRelatedField(
        queryset=FornecedorProfile.objects.all(), write_only=True)

    fornecedor_data = FornecedorProfileSerializer(
        source="fornecedor", read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
