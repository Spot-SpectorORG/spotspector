from rest_framework import serializers

from django.contrib.auth import get_user_model

from drf_spectacular.utils import extend_schema_field

from apps.music.models.artist import Artist
from apps.music.models.playlist import Playlist

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

    owned_playlists = serializers.SerializerMethodField()

    class Meta:
        model = User

        fields = [
            "public_id",
            "username",
            "followed_artists",
            "friends",
            "owned_playlists",
        ]

    @extend_schema_field(UserOwnedPlaylistsSerializer(many=True))
    def get_owned_playlists(self, obj):

        public_playlists = obj.owned_playlists.filter(visibility=Playlist.Status.PUBLIC)

        return UserOwnedPlaylistsSerializer(public_playlists, many=True).data


class UserPrivateProfileSerializer(serializers.ModelSerializer):
    owned_playlists = serializers.SerializerMethodField()
    friends = UserFriendsSerializer(many=True, read_only=True)
    followed_artists = UserFollowedArtistsSerializer(many=True, read_only=True)

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

    @extend_schema_field(UserOwnedPlaylistsSerializer(many=True))
    def get_owned_playlists(self, obj):
        all_my_playlists = obj.owned_playlists.all()

        return UserOwnedPlaylistsSerializer(all_my_playlists, many=True).data
