from rest_framework import generics, status

from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from apps.music.models.genre import Genre

from apps.music.api.serializers.genre import GenreListCreateSerializer


class GenreListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all().order_by("-pk")
    serializer_class = GenreListCreateSerializer

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = ["name"]
    search_fields = ["name"]
    ordering_fields = ["name"]
