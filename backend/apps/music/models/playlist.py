from random import choice

from django.db import models


class Playlist(models.Model):
    class Status(models.TextChoices):
        PUBLIC = "Public"
        PRIVATE = "Private"

    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="owned_playlists",
        verbose_name="Owner of playlist",
    )

    collaborators = models.ManyToManyField(
        "users.User",
        blank=True,
        related_name="collaborative_playlists",
        verbose_name="Collaborators of playlist",
    )

    title = models.CharField(max_length=50, verbose_name="Title of playlist")

    description = models.TextField(
        max_length=500, blank=True, null=True, verbose_name="Description of playlist"
    )

    genres = models.ManyToManyField(
        to="music.Genre", related_name="playlists", verbose_name="Genres of playlist"
    )

    saves_count = models.PositiveIntegerField(default=0, blank=True)

    tracks = models.ManyToManyField(
        to="music.Track", related_name="playlists", verbose_name="Tracks in playlist"
    )

    visibility = models.CharField(
        max_length=7,
        choices=Status,
        default=Status.PUBLIC,
    )

    class Meta:
        verbose_name = "Playlist"
        verbose_name_plural = "Playlists"

        ordering = ["-saves_count"]

        db_table = "playlists"

    def __str__(self) -> str:
        return self.title
