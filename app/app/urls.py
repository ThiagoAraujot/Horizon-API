from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

# Swagger Schema View
schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Horizon API",
        default_version='v1',
        description="API Documentation",
    ),
    public=True,
)

api_urls = [
    # path('', include('user.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),

    # API V1
    path('api/v1/', include([
        path('', include(api_urls)),
        path('docs/', schema_view.with_ui('swagger',
             cache_timeout=0), name='schema-swagger-ui'),
    ])),
]
