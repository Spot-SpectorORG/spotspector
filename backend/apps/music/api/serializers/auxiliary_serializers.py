from rest_framework import serializers

from apps.music.models.album import Album
from apps.music.models.artist import Artist


class ArtistNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["public_id", "name"]


class AlbumShortInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["public_id", "title", "release_date"]
