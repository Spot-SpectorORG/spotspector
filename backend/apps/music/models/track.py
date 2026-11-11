from django.db import models


from utils.models import generate_short_uuid, track_audio_upload_to


class Track(models.Model):
    id = models.BigAutoField(primary_key=True)

    public_id = models.CharField(
        max_length=10,
        default=generate_short_uuid,
        unique=True,
        editable=False,
    )

    title = models.CharField(max_length=100, verbose_name="Title of track")

    album = models.ForeignKey(
        to="music.Album",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tracks",
        verbose_name="Track album",
    )

    release_date = models.DateField(verbose_name="Date of release", blank=False)

    genres = models.ManyToManyField(
        to="music.Genre",
        related_name="tracks",
        verbose_name="Track genres",
        blank=False,
    )

    duration_ms = models.PositiveIntegerField(
        verbose_name="Duration of track", blank=True, null=True
    )

    artists = models.ManyToManyField(
        to="music.Artist",
        related_name="tracks",
        verbose_name="Track artists",
        blank=False,
    )

    plays_count = models.PositiveIntegerField(
        default=0, verbose_name="Track plays", blank=True
    )

    track_position = models.PositiveSmallIntegerField(
        default=1, verbose_name="Track position", blank=False
    )

    audio_file = models.FileField(
        upload_to=track_audio_upload_to, max_length=512, null=True
    )

    class Meta:
        verbose_name = "Track"
        verbose_name_plural = "Tracks"

        ordering = ["-plays_count"]

        db_table = "tracks"

    def __str__(self):
        return self.title
