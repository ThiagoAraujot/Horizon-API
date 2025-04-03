from rest_framework import serializers
from .models import Scheduling
from users.serializers import ClienteProfileSerializer, MecanicoProfileSerializer
from users.models import ClienteProfile, MecanicoProfile
from vehicles.serializers import VehicleSerializer
from vehicles.models import Vehicle


class SchedulingSerializer(serializers.ModelSerializer):
    # Para escrita (POST/PUT) - Apenas IDs
    mecanico = serializers.PrimaryKeyRelatedField(
        queryset=MecanicoProfile.objects.all(), write_only=True)
    vehicle = serializers.PrimaryKeyRelatedField(
        queryset=Vehicle.objects.all(), write_only=True)

    # Para leitura (GET) - Retorna os objetos completos
    customer_data = ClienteProfileSerializer(source="customer", read_only=True)
    mecanico_data = MecanicoProfileSerializer(
        source="mecanico", read_only=True)
    vehicle_data = VehicleSerializer(source="vehicle", read_only=True)

    class Meta:
        model = Scheduling
        fields = '__all__'
        extra_kwargs = {
            'customer': {'read_only': True}
        }
