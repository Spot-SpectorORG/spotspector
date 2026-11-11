from rest_framework import serializers

from apps.music.models.album import Album
from apps.music.models.artist import Artist
from apps.music.models.track import Track

from apps.music.api.serializers.auxiliary_serializers import ArtistNameSerializer
from apps.music.api.serializers.genre import GenreTypeSerializer


class AlbumListSerializer(serializers.ModelSerializer):
    artists = ArtistNameSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ["public_id", "title", "artists", "release_date"]


class AlbumCreateSerializer(serializers.ModelSerializer):
    artists = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Artist.objects.all()
    )

    class Meta:
        model = Album
        fields = ["public_id", "title", "artists", "release_date"]


class TrackInfoInsideAlbumSerializer(serializers.ModelSerializer):
    genres = GenreTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Track
        fields = [
            "public_id",
            "title",
            "duration_ms",
            "plays_count",
            "genres",
            "track_position",
        ]


class AlbumDetailSerializer(serializers.ModelSerializer):
    artists = ArtistNameSerializer(many=True, read_only=True)

    tracks = TrackInfoInsideAlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ["public_id", "title", "artists", "tracks", "release_date"]
