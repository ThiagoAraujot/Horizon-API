from django.db import models
from orders.models import Order
from products.models import Product
import uuid


class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='ordem_items')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='ordem_items')
    quantity = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product.name} - {self.quantity}'
