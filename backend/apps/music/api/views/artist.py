from drf_spectacular.utils import extend_schema

from rest_framework import generics, status

from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from apps.music.models.artist import Artist

from apps.music.api.serializers.artist import (
    ArtistDetailSerializer,
    ArtistListSerializer,
    ArtistCreateSerializer,
)

from apps.music.api.pagination.artist import ArtistListPagination


@extend_schema(tags=["Music Catalog - Artists"])
class ArtistListView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = ["genres"]
    search_fields = ["name"]
    ordering_fields = ["genres", "followers", "name"]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ArtistCreateSerializer

        return ArtistListSerializer


@extend_schema(tags=["Music Catalog - Artists"])
class ArtistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()

    serializer_class = ArtistDetailSerializer

    slug_field = "public_id"
