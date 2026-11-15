from drf_spectacular.utils import extend_schema

from rest_framework import generics, status

from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from django.db.models import Prefetch

from apps.music.models.album import Album
from apps.music.models.track import Track

from apps.music.api.serializers.album import (
    AlbumListSerializer,
    AlbumCreateSerializer,
    AlbumDetailSerializer,
)

from apps.music.api.pagination.album import AlbumListPagination


@extend_schema(tags=["Music Catalog - Albums"])
class AlbumListView(generics.ListCreateAPIView):
    queryset = Album.objects.all().prefetch_related("artists")

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = ["release_date"]
    search_fields = ["title", "artists__name"]
    ordering_fields = ["release_date"]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AlbumCreateSerializer

        return AlbumListSerializer


@extend_schema(tags=["Music Catalog - Albums"])
class AlbumDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all().prefetch_related(
        "artists",
        Prefetch(
            "tracks",
            queryset=Track.objects.order_by("track_position").prefetch_related(
                "genres"
            ),
        ),
    )
    serializer_class = AlbumDetailSerializer

    lookup_field = "public_id"
