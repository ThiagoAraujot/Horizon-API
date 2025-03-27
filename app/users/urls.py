from django.urls import path
from .views import RegisterUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('user/register/', RegisterUserView.as_view(), name='register'),
    path('user/login/', TokenObtainPairView.as_view(), name='login'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
