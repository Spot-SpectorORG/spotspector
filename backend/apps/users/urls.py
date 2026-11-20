from apps.users.api.views.auth import UserLoginView, UserRegisterView
from apps.users.api.views.user import (MeProfileView, UserDetailView,
                                       UserListView)
from django.urls import path

app_name = "users"

urlpatterns = [
    path(
        "register/",
        UserRegisterView.as_view(),
        name="register",
    ),
    path("login/", UserLoginView.as_view(), name="login"),
    path("me/", MeProfileView.as_view(), name="user-profile"),
    path("", UserListView.as_view(), name="users-list"),
    path("<str:public_id>/", UserDetailView.as_view(), name="user-detail"),
]
