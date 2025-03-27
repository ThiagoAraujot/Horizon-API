from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import User, ClienteProfile, MecanicoProfile, FornecedorProfile
from .serializers import UserSerializer, ClienteProfileSerializer, MecanicoProfileSerializer, FornecedorProfileSerializer

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        if user.role == 'cliente':
            ClienteProfile.objects.create(user=user)
        elif user.role == 'mecanico':
            MecanicoProfile.objects.create(user=user)
        elif user.role == 'fornecedor':
            FornecedorProfile.objects.create(user=user)
