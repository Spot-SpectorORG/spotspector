from rest_framework import serializers

from apps.music.models.artist import Artist
from apps.music.models.genre import Genre

from apps.music.api.serializers.genre import GenreTypeSerializer

from apps.music.api.serializers.auxiliary_serializers import AlbumShortInfoSerializer


class ArtistListSerializer(serializers.ModelSerializer):
    genres = GenreTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ["public_id", "name", "genres"]


class ArtistCreateSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(many=True, queryset=Genre.objects.all())

    class Meta:
        model = Artist
        fields = ["public_id", "name", "genres"]


class ArtistDetailSerializer(serializers.ModelSerializer):
    genres = GenreTypeSerializer(many=True, read_only=True)

    albums = AlbumShortInfoSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ["public_id", "name", "followers", "genres", "albums"]

        read_only_fields = ["followers"]
