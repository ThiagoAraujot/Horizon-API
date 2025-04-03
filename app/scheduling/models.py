from django.db import models
from users.models import ClienteProfile, MecanicoProfile
from vehicles.models import Vehicle
import uuid

STATUS_CHOICES = (
    ('pendente', 'Pendente'),
    ('confirmado', 'Confirmado'),
    ('cancelado', 'Cancelado'),
    ('concluido', 'Concluído'),
)


class Scheduling(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(
        ClienteProfile, on_delete=models.CASCADE, related_name='scheduling')
    mecanico = models.ForeignKey(
        MecanicoProfile, on_delete=models.CASCADE, related_name='scheduling')
    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.CASCADE, related_name='scheduling')
    date_time = models.DateTimeField()
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='pendente')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Scheduling {self.id} - {self.customer} - {self.mecanico} - {self.date_time} - {self.status}"
