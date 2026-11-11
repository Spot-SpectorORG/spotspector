from rest_framework import serializers

from apps.music.models.track import Track
from apps.music.models.artist import Artist

from apps.music.services.validation import validate_audio_file

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
            "duration_ms",
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
            "audio_file",
            "genres",
            "release_date",
        ]

    def validate_audio_file(self, file):

        file = validate_audio_file(file)

        return file

    def create(self, validated_data):
        audio_file = validated_data.get("audio_file")

        if audio_file and hasattr(audio_file, "extracted_duration_ms"):
            validated_data["duration_ms"] = audio_file.extracted_duration_ms

        return super().create(validated_data)


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
            "duration_ms",
        ]
        read_only_fields = ["duration_ms", "plays_count"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        from apps.music.api.serializers.genre import GenreTypeSerializer

        representation["genres"] = GenreTypeSerializer(
            instance.genres.all(), many=True
        ).data

        return representation
