from django.db import models
from scheduling.models import Scheduling
from users.models import ClienteProfile
import uuid


class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(
        ClienteProfile, on_delete=models.CASCADE, related_name='reviews')
    scheduling = models.ForeignKey(
        Scheduling, on_delete=models.CASCADE, related_name='reviews')
    stars = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Review {self.id} - Stars: {self.stars}'
