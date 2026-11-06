from django.db import models

from utils.models import generate_short_uuid


class Album(models.Model):
    public_id = models.CharField(
        max_length=10,
        default=generate_short_uuid,
        unique=True,
        db_index=True,
        editable=False,
    )

    title = models.CharField(max_length=100, blank=False, verbose_name="Title of album")

    artists = models.ManyToManyField(
        to="music.Artist", related_name="albums", verbose_name="Artists of album"
    )

    release_date = models.DateField(verbose_name="Date of release")

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"

        ordering = ["title"]

        unique_together = [["title", "release_date"]]

        db_table = "albums"

    def __str__(self):
        return self.title
