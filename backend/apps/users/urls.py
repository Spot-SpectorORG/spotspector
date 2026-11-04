from django.urls import path

from apps.users.api.views.auth import RegisterView

from rest_framework_simplejwt.views import TokenObtainPairView

app_name = "users"

urlpatterns = [
    path(
        "register/",
        RegisterView.as_view(),
        name="agent-metrics-resource-history",
    ),
    path("login/", TokenObtainPairView.as_view(), name="login"),
]
