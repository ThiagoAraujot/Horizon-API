from rest_framework import serializers
from .models import Review
from users.serializers import ClienteProfileSerializer
from users.models import ClienteProfile
from scheduling.models import Scheduling


class ReviewSerializer(serializers.ModelSerializer):
    # Para escrita (POST/PUT) - Apenas IDs
    scheduling = serializers.PrimaryKeyRelatedField(
        queryset=Scheduling.objects.all(), write_only=True)

    # Para leitura (GET) - Retorna os objetos completos
    customer_data = ClienteProfileSerializer(source="customer", read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        extra_kwargs = {
            'customer': {'read_only': True}
        }
