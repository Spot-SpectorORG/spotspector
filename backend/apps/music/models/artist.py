from django.db import models

from utils.models import (
    ImageOptimizationMixin,
    UploadToPath,
    generate_short_uuid,
)


class Artist(ImageOptimizationMixin, models.Model):
    image_size_config = {"avatar": (600, 600)}

    public_id = models.CharField(
        max_length=10,
        default=generate_short_uuid,
        unique=True,
        editable=False,
    )

    avatar = models.ImageField(
        upload_to=UploadToPath("images/artists"),
        verbose_name="Artist avatar",
        storage=ImageOptimizationMixin.get_image_storage,
        blank=True,
        null=True,
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
