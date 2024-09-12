from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


# Custom SpectacularSchemaView to exclude from schema documentation
class SpectacularSchemaView(SpectacularAPIView):
    EXCLUDE_FROM_SCHEMA = True


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("tasks.urls")),
    # This schema should NOT appear in the Swagger UI
    path("api/schema/", SpectacularSchemaView.as_view(), name="schema"),
    # Swagger and ReDoc UIs will be available
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
