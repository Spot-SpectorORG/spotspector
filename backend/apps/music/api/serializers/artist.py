from apps.music.api.serializers.auxiliary_serializers import \
    AlbumShortInfoSerializer
from apps.music.api.serializers.genre import GenreTypeSerializer
from apps.music.models.artist import Artist
from apps.music.models.genre import Genre
from rest_framework import serializers


class ArtistListSerializer(serializers.ModelSerializer):
    genres = GenreTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ["public_id", "name", "genres", "avatar"]


class ArtistCreateSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(many=True, queryset=Genre.objects.all())

    class Meta:
        model = Artist
        fields = ["public_id", "name", "genres", "avatar"]


class ArtistDetailSerializer(serializers.ModelSerializer):
    genres = GenreTypeSerializer(many=True, read_only=True)

    albums = AlbumShortInfoSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ["public_id", "name", "followers", "genres", "albums", "avatar"]

        read_only_fields = ["followers"]
