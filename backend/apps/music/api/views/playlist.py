from drf_spectacular.utils import extend_schema

from rest_framework import generics, status

from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from apps.music.models.playlist import Playlist

from apps.music.api.serializers.playlist import (
    PlaylistCreateSerializer,
    PlaylistDetailSerializer,
)

from apps.music.api.pagination.playlist import PlaylistListPagination


@extend_schema(tags=["User Playlists & Libraries"])
class PlaylistListView(generics.ListCreateAPIView):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_fields = ["genres__name", "owner_id"]
    search_fields = ["title", "description", "owner__username"]
    ordering_fields = ["saves_count", "duration"]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return PlaylistCreateSerializer

        return PlaylistDetailSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Playlist.objects.all()

        owner_id = self.request.query_params.get("owner_id")
        if owner_id is not None:
            if not user.is_authenticated or str(user.id) != str(owner_id):
                queryset = queryset.filter(visibility=Playlist.Status.PUBLIC)
        else:
            queryset = queryset.filter(visibility=Playlist.Status.PUBLIC)

        return queryset


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

        if playlist.visibility == Playlist.Status.PRIVATE:
            if not user.is_authenticated or (
                playlist.owner != user and user not in playlist.collaborators.all()
            ):
                raise exceptions.PermissionDenied("This playlist is private.")

        return playlist
