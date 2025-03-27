from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import ClienteProfile, MecanicoProfile, FornecedorProfile

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'role')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ClienteProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClienteProfile
        fields = ['id', 'user', 'name', 'last_name',
                  'phone', 'address', 'avatar', 'score']


class MecanicoProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MecanicoProfile
        fields = ['id', 'user', 'address', 'open_time', 'close_time',
                  'phone', 'level', 'avatar', 'score']


class FornecedorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FornecedorProfile
        fields = ['id', 'user']
