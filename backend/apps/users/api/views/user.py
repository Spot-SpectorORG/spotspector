from django.db.models import Prefetch
from django.db.models import prefetch_related_objects

from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend

from drf_spectacular.utils import extend_schema

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from rest_framework.filters import OrderingFilter, SearchFilter


from apps.users.api.serializers.user import (
    UserPublicDetailProfileSerializer,
    UserPublicProfileSerializer,
    UserPrivateProfileSerializer,
)

from apps.users.api.pagination.user import UserListPagination

from apps.music.models.playlist import Playlist

User = get_user_model()


@extend_schema(tags=["User Management & Profiles"])
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()

    filter_backends = [
        SearchFilter,
    ]

    search_fields = ["username"]

    serializer_class = UserPublicProfileSerializer


@extend_schema(tags=["User Management & Profiles"])
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.prefetch_related(
        "followed_artists",
        "friends",
        Prefetch(
            "owned_playlists",
            queryset=Playlist.objects.filter(visibility=Playlist.Status.PUBLIC),
        ),
    )

    serializer_class = UserPublicDetailProfileSerializer

    lookup_field = "public_id"


@extend_schema(tags=["User Management & Profiles"])
class MeProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserPrivateProfileSerializer

    def get_object(self):
        user = self.request.user
        prefetch_related_objects(
            [user],
            "followed_artists",
            "friends",
            "owned_playlists",
        )

        return user
