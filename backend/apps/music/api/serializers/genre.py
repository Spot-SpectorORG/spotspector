from rest_framework import serializers

from apps.music.models.genre import Genre


class GenreTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class GenreListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name", "description"]
