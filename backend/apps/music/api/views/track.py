from drf_spectacular.utils import extend_schema

from rest_framework import generics, status

from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from apps.music.models.track import Track

from apps.music.api.serializers.track import (
    TrackListSerializer,
    TrackCreateSerializer,
    TrackDetailSerializer,
)

from apps.music.api.pagination.track import TrackListPagination


@extend_schema(tags=["Music Catalog - Tracks"])
class TrackListView(generics.ListCreateAPIView):
    queryset = Track.objects.all()

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = ["release_date", "artists__id"]
    search_fields = ["title", "artists__name"]
    ordering_fields = ["release_date"]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return TrackCreateSerializer

        return TrackListSerializer


@extend_schema(tags=["Music Catalog - Tracks"])
class TrackDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()

    serializer_class = TrackDetailSerializer

    slug_field = "public_id"
