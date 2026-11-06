from rest_framework import serializers

from apps.music.models.track import Track
from apps.music.models.artist import Artist

from apps.music.api.serializers.auxiliary_serializers import (
    AlbumShortInfoSerializer,
    ArtistNameSerializer,
)


class TrackListSerializer(serializers.ModelSerializer):
    artists = ArtistNameSerializer(many=True, read_only=True)
    album = AlbumShortInfoSerializer(read_only=True)

    class Meta:
        model = Track
        fields = [
            "public_id",
            "title",
            "artists",
            "album",
            "plays_count",
            "duration",
        ]


class TrackCreateSerializer(serializers.ModelSerializer):
    artists = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Artist.objects.all()
    )

    class Meta:
        model = Track
        fields = [
            "public_id",
            "title",
            "artists",
            "album",
            "genres",
            "duration",
            "release_date",
        ]


class TrackDetailSerializer(serializers.ModelSerializer):
    artists = ArtistNameSerializer(many=True, read_only=True)
    album = AlbumShortInfoSerializer(read_only=True)

    class Meta:
        model = Track
        fields = [
            "public_id",
            "title",
            "artists",
            "album",
            "genres",
            "plays_count",
            "track_position",
            "duration",
        ]
        read_only_fields = ["duration", "plays_count"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        from apps.music.api.serializers.genre import GenreTypeSerializer

        representation["genres"] = GenreTypeSerializer(
            instance.genres.all(), many=True
        ).data

        return representation
