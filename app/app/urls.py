from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view
from django.conf import settings
from django.conf.urls.static import static


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
    path('', include('users.urls')),
    path('', include('vehicles.urls')),
    path('', include('scheduling.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),

    # API V1
    path('api/v1/', include([
        path('', include(api_urls)),
        path('docs/', schema_view.with_ui('swagger',
             cache_timeout=0), name='schema-swagger-ui'),
    ])),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
