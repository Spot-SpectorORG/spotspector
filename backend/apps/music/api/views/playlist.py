from drf_spectacular.utils import extend_schema

from rest_framework import generics, status

from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from apps.music.models.playlist import Playlist

from apps.music.api.serializers.playlist import (
    PlaylistCreateSerializer,
    PlaylistDetailSerializer,
    PlaylistListSerializer,
)

from apps.music.api.pagination.playlist import PlaylistListPagination

from apps.music.selectors.playlist import (
    get_playlists_by_owner,
    get_playlist_by_permission,
)


@extend_schema(tags=["User Playlists & Libraries"])
class PlaylistListView(generics.ListCreateAPIView):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_fields = ["genres__name", "owner_id"]
    search_fields = ["title", "description", "owner__username"]
    ordering_fields = ["saves_count", "duration"]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return PlaylistCreateSerializer

        return PlaylistListSerializer

    def get_queryset(self):
        user = self.request.user
        owner_id = self.request.query_params.get("owner_id")

        return get_playlists_by_owner(user, owner_id)


@extend_schema(tags=["User Playlists & Libraries"])
class PlaylistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()

    lookup_field = "public_id"

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return PlaylistCreateSerializer

        return PlaylistDetailSerializer

    def get_object(self):
        playlist = super().get_object()
        user = self.request.user

        return get_playlist_by_permission(user, playlist)
