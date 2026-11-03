from django.contrib.auth.models import AbstractUser

from django.db import models


class User(AbstractUser):
    username = models.CharField(
        max_length=20,
        unique=True,
    )
    email = models.EmailField(blank=False, verbose_name="User email")

    liked_tracks = models.ManyToManyField(
        "music.Track", related_name="liked_users", verbose_name="Tracks liked by user"
    )

    followed_artists = models.ManyToManyField(
        "music.Artist",
        related_name="followed_users",
        verbose_name="Artists followed by user",
    )

    friends = models.ManyToManyField(
        to="self",
        symmetrical=False,
        blank=True,
        related_name="friended_by",
        verbose_name="User friends",
    )

    class Meta:
        ordering = ["username"]

    def __str__(self) -> str:
        return self.username
