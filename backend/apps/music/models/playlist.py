from django.db import models

from utils.models import generate_short_uuid


class Playlist(models.Model):
    class Status(models.TextChoices):
        PUBLIC = "Public"
        PRIVATE = "Private"

    public_id = models.CharField(
        max_length=10,
        default=generate_short_uuid,
        unique=True,
        editable=False,
    )

    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="owned_playlists",
        verbose_name="Owner of playlist",
        blank=False,
    )

    collaborators = models.ManyToManyField(
        "users.User",
        related_name="collaborative_playlists",
        verbose_name="Collaborators of playlist",
        blank=True,
    )

    title = models.CharField(max_length=50, verbose_name="Title of playlist")

    description = models.TextField(
        max_length=500, blank=True, null=True, verbose_name="Description of playlist"
    )

    genres = models.ManyToManyField(
        to="music.Genre",
        related_name="playlists",
        verbose_name="Genres of playlist",
        blank=True,
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
