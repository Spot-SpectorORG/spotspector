from django.db import models


class Track(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title of track")

    album = models.ForeignKey(
        to="music.Album",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tracks",
        verbose_name="Track album",
    )

    release_date = models.DateField(verbose_name="Date of release")

    genres = models.ManyToManyField(
        to="music.Genre", related_name="tracks", verbose_name="Track genres"
    )

    duration = models.DurationField(verbose_name="Duration of track")

    artists = models.ManyToManyField(
        to="music.Artist", related_name="tracks", verbose_name="Track artists"
    )

    plays_count = models.PositiveIntegerField(
        default=0, verbose_name="Track plays", blank=True
    )

    track_position = models.PositiveSmallIntegerField(
        default=1, verbose_name="Track position"
    )

    class Meta:
        verbose_name = "Track"
        verbose_name_plural = "Tracks"

        ordering = ["-plays_count"]

        db_table = "tracks"

    def __str__(self):
        return self.title
