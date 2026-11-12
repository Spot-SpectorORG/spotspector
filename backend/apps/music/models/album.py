from django.db import models

from utils.models import ImageOptimizationMixin, UploadToPath, generate_short_uuid


class Album(ImageOptimizationMixin, models.Model):
    image_fields_config = {
        "cover": (1000, 1000),
    }

    public_id = models.CharField(
        max_length=10,
        default=generate_short_uuid,
        unique=True,
        editable=False,
    )

    cover = models.ImageField(
        upload_to=UploadToPath("images/albums/"),
        verbose_name="Album cover",
        storage=ImageOptimizationMixin.get_image_storage,
        null=True,
        blank=True,
    )

    title = models.CharField(max_length=100, blank=False, verbose_name="Title of album")

    artists = models.ManyToManyField(
        to="music.Artist",
        related_name="albums",
        verbose_name="Artists of album",
        blank=False,
    )

    release_date = models.DateField(verbose_name="Date of release", blank=False)

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"

        ordering = ["title"]

        unique_together = [["title", "release_date"]]

        db_table = "albums"

    def __str__(self):
        return self.title
