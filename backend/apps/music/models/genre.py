from django.db import models

from utils.models import generate_short_uuid


class Genre(models.Model):
    public_id = models.CharField(
        max_length=10,
        default=generate_short_uuid,
        unique=True,
        editable=False,
    )

    name = models.CharField(max_length=50, verbose_name="Name of genre")

    description = models.TextField(
        max_length=1000, blank=True, null=True, verbose_name="Description of genre"
    )

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

        ordering = ["name"]

        db_table = "music_genres"

    def __str__(self):
        return self.name
