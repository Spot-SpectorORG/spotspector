from drf_spectacular.utils import extend_schema

from rest_framework import generics

from django.contrib.auth import get_user_model

from rest_framework.permissions import IsAuthenticated

from rest_framework.filters import OrderingFilter, SearchFilter

from django_filters.rest_framework import DjangoFilterBackend

from apps.users.api.serializers.user import (
    UserPublicDetailProfileSerializer,
    UserPublicProfileSerializer,
    UserPrivateProfileSerializer,
)

from apps.users.api.pagination.user import UserListPagination

User = get_user_model()


@extend_schema(tags=["User Management & Profiles"])
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()

    pagination_class = UserListPagination

    filter_backends = [
        SearchFilter,
    ]

    search_fields = ["username"]

    serializer_class = UserPublicProfileSerializer


@extend_schema(tags=["User Management & Profiles"])
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()

    serializer_class = UserPublicDetailProfileSerializer

    lookup_field = "public_id"


@extend_schema(tags=["User Management & Profiles"])
class MeProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserPrivateProfileSerializer

    def get_object(self):
        return self.request.user
