from django.urls import path
from .views import RegisterUserView
from rest_framework.routers import DefaultRouter
from django.urls import include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ClienteProfileViewSet, MecanicoProfileViewSet, FornecedorProfileViewSet

router = DefaultRouter()
router.register(r'cliente', ClienteProfileViewSet)
router.register(r'mecanico', MecanicoProfileViewSet)
router.register(r'fornecedor', FornecedorProfileViewSet)

urlpatterns = [
    path('user/register/', RegisterUserView.as_view(), name='register'),
    path('user/login/', TokenObtainPairView.as_view(), name='login'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', include(router.urls)),
]
