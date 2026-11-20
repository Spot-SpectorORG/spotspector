from apps.music.models.artist import Artist
from apps.music.models.playlist import Playlist
from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

User = get_user_model()


class UserFollowedArtistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["public_id", "name"]


class UserFriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["public_id", "username"]


class UserOwnedPlaylistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist

        fields = ["public_id", "title", "saves_count"]


class UserPublicProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = ["public_id", "username"]


class UserPublicDetailProfileSerializer(serializers.ModelSerializer):
    followed_artists = UserFollowedArtistsSerializer(many=True, read_only=True)
    friends = UserFriendsSerializer(many=True, read_only=True)
    owned_playlists = UserOwnedPlaylistsSerializer(many=True, read_only=True)

    class Meta:
        model = User

        fields = [
            "public_id",
            "username",
            "followed_artists",
            "friends",
            "owned_playlists",
        ]


class UserPrivateProfileSerializer(serializers.ModelSerializer):
    friends = UserFriendsSerializer(many=True, read_only=True)
    followed_artists = UserFollowedArtistsSerializer(many=True, read_only=True)
    owned_playlists = UserOwnedPlaylistsSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "public_id",
            "username",
            "email",
            "owned_playlists",
            "friends",
            "followed_artists",
            "date_joined",
        ]

        read_only_fields = ["date_joined"]
