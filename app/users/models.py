from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
import uuid


class User(AbstractUser):
    ROLE_CHOICES = (
        ('cliente', 'Cliente'),
        ('mecanico', 'Mecânico'),
        ('fornecedor', 'Fornecedor'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    email = models.EmailField(unique=True)
    
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='custom_user_set', 
        blank=True, 
        help_text='The groups this user belongs to.'
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='custom_user_permissions_set', 
        blank=True, 
        help_text='Specific permissions for this user.'
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"


class ClienteProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='cliente_profile')
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = PhoneNumberField()
    address = models.CharField(max_length=500)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Cliente: {self.user.username}"


class MecanicoProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    LEVELS = (
        ('Bronze', 'Bronze'),
        ('Prata', 'Prata'),
        ('Ouro', 'Ouro'),
    )
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='mecanico_profile')
    address = models.CharField(max_length=500)
    open_time = models.TimeField()
    close_time = models.TimeField()
    phone = PhoneNumberField()
    level = models.CharField(max_length=20, choices=LEVELS, default='Bronze')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Mecânico: {self.user.username} - {self.level}"


class FornecedorProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='fornecedor_profile')

    def __str__(self):
        return f"Fornecedor: {self.user.username}"
