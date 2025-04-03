from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import User, ClienteProfile, MecanicoProfile, FornecedorProfile
from .serializers import UserSerializer, ClienteProfileSerializer, MecanicoProfileSerializer, FornecedorProfileSerializer
from rest_framework import viewsets
from .models import ClienteProfile, MecanicoProfile, FornecedorProfile
from .serializers import ClienteProfileSerializer, MecanicoProfileSerializer, FornecedorProfileSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import IsOwner


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


class ClienteProfileViewSet(viewsets.ModelViewSet):
    queryset = ClienteProfile.objects.all()
    serializer_class = ClienteProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        """
        A permissão será diferente para as ações de leitura e escrita.
        """
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsOwner()]
        return super().get_permissions()

    def perform_create(self, serializer):
        # Associa o perfil ao usuário autenticado
        serializer.save(user=self.request.user)


class MecanicoProfileViewSet(viewsets.ModelViewSet):
    queryset = MecanicoProfile.objects.all()
    serializer_class = MecanicoProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        """
        A permissão será diferente para as ações de leitura e escrita.
        """
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsOwner()]
        return super().get_permissions()

    def perform_create(self, serializer):
        # Associa o perfil ao usuário autenticado
        serializer.save(user=self.request.user)


class FornecedorProfileViewSet(viewsets.ModelViewSet):
    queryset = FornecedorProfile.objects.all()
    serializer_class = FornecedorProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        """
        A permissão será diferente para as ações de leitura e escrita.
        """
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsOwner()]
        return super().get_permissions()

    def perform_create(self, serializer):
        # Associa o perfil ao usuário autenticado
        serializer.save(user=self.request.user)
