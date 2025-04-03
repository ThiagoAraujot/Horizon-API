from django.db import models
from users.models import MecanicoProfile, FornecedorProfile
import uuid


STATUS_CHOICES = (
    ('novo', 'Novo'),
    ('processando', 'Processando'),
    ('concluido', 'Concluído'),
)


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mecanico = models.ForeignKey(
        MecanicoProfile, on_delete=models.CASCADE, related_name='orders')
    fornecedor = models.ForeignKey(
        FornecedorProfile, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='novo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} - {self.status} - {self.mecanico} - {self.fornecedor}"
