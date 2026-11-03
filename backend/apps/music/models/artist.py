from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=50, verbose_name="Artist name")

    followers = models.PositiveIntegerField(
        default=0, blank=True, verbose_name="Artist followers count"
    )

    genres = models.ManyToManyField(
        to="music.Genre",
        related_name="artists",
        verbose_name="Artist's genres",
    )

    class Meta:
        verbose_name = "Artist"
        verbose_name_plural = "Artists"

        ordering = ["-followers"]

        db_table = "artists"

    def __str__(self):
        return self.name
