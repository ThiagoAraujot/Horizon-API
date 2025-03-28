from django.urls import path
from .views import VehicleViewSet
from rest_framework.routers import DefaultRouter
from django.urls import include

router = DefaultRouter()
router.register(r'vehicle', VehicleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
