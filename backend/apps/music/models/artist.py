from django.db import models

from utils.models import generate_short_uuid


class Artist(models.Model):
    public_id = models.CharField(
        max_length=10,
        default=generate_short_uuid,
        unique=True,
        editable=False,
    )

    name = models.CharField(max_length=50, verbose_name="Artist name")

    followers = models.PositiveIntegerField(
        default=0, blank=True, verbose_name="Artist followers count"
    )

    genres = models.ManyToManyField(
        to="music.Genre",
        related_name="artists",
        verbose_name="Artist's genres",
        blank=False,
    )

    class Meta:
        verbose_name = "Artist"
        verbose_name_plural = "Artists"

        ordering = ["-followers"]

        db_table = "artists"

    def __str__(self):
        return self.name
