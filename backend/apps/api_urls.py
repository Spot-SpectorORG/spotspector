from django.urls import include, path

urlpatterns = [
    path("users/", include("apps.users.urls")),
    path("music/", include("apps.music.urls")),
]
