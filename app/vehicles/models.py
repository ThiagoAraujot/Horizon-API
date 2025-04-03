from django.db import models
from users.models import ClienteProfile
import uuid


class Vehicle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(
        ClienteProfile, on_delete=models.CASCADE, related_name='vehicles')
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    factory_year = models.PositiveIntegerField()
    plate = models.CharField(max_length=7)
    km = models.PositiveIntegerField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.brand} {self.model} ({self.factory_year})"
