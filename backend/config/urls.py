from config import settings
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

admin.site.site_title = "Spotspector Admin"
admin.site.site_header = "Spotspector Admin Panel"
admin.site.index_title = "Welcome To Spotspector Admin"

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
