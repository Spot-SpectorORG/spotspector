from rest_framework import serializers

from apps.music.models import Playlist
from apps.music.models import Track
from apps.music.models import Genre

from apps.music.api.serializers.genre import GenreTypeSerializer
from apps.music.api.serializers.auxiliary_serializers import ArtistNameSerializer

from django.contrib.auth import get_user_model

User = get_user_model()


class TrackInfoInsidePlaylistSerializer(serializers.ModelSerializer):
    artists = ArtistNameSerializer(many=True, read_only=True)

    class Meta:
        model = Track
        fields = ["public_id", "title", "duration", "artists"]


class PlaylistUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["public_id", "username"]


class PlaylistListSerializer(serializers.ModelSerializer):
    owner = PlaylistUserSerializer(read_only=True)
    collaborators = PlaylistUserSerializer(many=True, read_only=True)
    genres = GenreTypeSerializer(many=True, read_only=True)
    tracks = TrackInfoInsidePlaylistSerializer(many=True, read_only=True)

    class Meta:
        model = Playlist
        fields = [
            "public_id",
            "title",
            "description",
            "owner",
            "collaborators",
            "genres",
            "tracks",
            "visibility",
            "saves_count",
            "duration",
        ]


class PlaylistCreateSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    collaborators = serializers.PrimaryKeyRelatedField(
        many=True, queryset=User.objects.all(), required=False
    )
    genres = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Genre.objects.all(), required=False
    )
    tracks = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Track.objects.all(), required=False
    )

    class Meta:
        model = Playlist
        fields = [
            "public_id",
            "title",
            "description",
            "owner",
            "collaborators",
            "genres",
            "tracks",
            "visibility",
        ]


class PlaylistDetailSerializer(serializers.ModelSerializer):
    owner = PlaylistUserSerializer(read_only=True)
    collaborators = PlaylistUserSerializer(many=True, read_only=True)
    genres = GenreTypeSerializer(many=True, read_only=True)
    tracks = TrackInfoInsidePlaylistSerializer(many=True, read_only=True)

    class Meta:
        model = Playlist
        fields = [
            "id",
            "title",
            "description",
            "owner",
            "collaborators",
            "genres",
            "tracks",
            "visibility",
            "saves_count",
        ]
