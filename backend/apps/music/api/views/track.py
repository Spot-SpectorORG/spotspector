from drf_spectacular.utils import extend_schema

from rest_framework import generics, status

from rest_framework.permissions import AllowAny

from rest_framework.views import APIView

from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from django_filters.rest_framework import DjangoFilterBackend

from apps.music.models.track import Track

from apps.music.api.serializers.track import (
    TrackListSerializer,
    TrackCreateSerializer,
    TrackDetailSerializer,
)


from apps.music.api.pagination.track import TrackListPagination
from apps.music.selectors.track import get_track_stream_url


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

    parser_classes = [MultiPartParser, FormParser]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return TrackCreateSerializer

        return TrackListSerializer


@extend_schema(tags=["Music Catalog - Tracks"])
class TrackDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()

    serializer_class = TrackDetailSerializer

    lookup_field = "public_id"


@extend_schema(tags=["Music Catalog - Tracks"])
class TrackStreamView(APIView):
    """Update play count and response track stream URL and expires seconds"""

    permission_classes = [AllowAny]

    def get(self, request, public_id):

        stream_url, expire_time = get_track_stream_url(public_id)

        return Response(
            {
                "stream_url": stream_url,
                "expires_in": expire_time,
            }
        )
