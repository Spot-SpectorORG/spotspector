from django.contrib.auth.models import AbstractUser

from django.db import models

from utils.models import generate_short_uuid


class User(AbstractUser):
    public_id = models.CharField(
        max_length=10,
        default=generate_short_uuid,
        unique=True,
        db_index=True,
        editable=False,
    )

    username = models.CharField(
        max_length=20,
        unique=True,
    )
    email = models.EmailField(blank=False, verbose_name="User email")

    liked_tracks = models.ManyToManyField(
        "music.Track",
        related_name="liked_users",
        verbose_name="Tracks liked by user",
        blank=True,
    )

    followed_artists = models.ManyToManyField(
        "music.Artist",
        related_name="followed_users",
        verbose_name="Artists followed by user",
        blank=True,
    )

    friends = models.ManyToManyField(
        to="self",
        symmetrical=False,
        related_name="friended_by",
        verbose_name="User friends",
        blank=True,
    )

    class Meta:
        ordering = ["username"]

    def __str__(self) -> str:
        return self.username
