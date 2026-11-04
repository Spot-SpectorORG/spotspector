from rest_framework import generics, status

from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from apps.music.models.album import Album

from apps.music.api.serializers.album import (
    AlbumListSerializer,
    AlbumCreateSerializer,
    AlbumDetailSerializer,
)


class AlbumListView(generics.ListCreateAPIView):
    queryset = Album.objects.all().order_by("-pk")

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


class AlbumDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all().prefetch_related("artists")
    serializer_class = AlbumDetailSerializer
