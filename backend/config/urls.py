from django.contrib import admin

from django.urls import include, path

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from config import settings

urlpatterns = [
    path("admin/", admin.site.urls),  # the admin panel
    path(
        "api/schema/",
        SpectacularAPIView.as_view(),
        name="schema",
    ),  # the schema in format JSON/YAML
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),  # the Swagger UI
    path("api/v1/", include("apps.api_urls")),  # the API
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
