import shortuuid
from uuid import uuid4

from pathlib import Path

from django.utils.deconstruct import deconstructible

from django.db import models

from django.core.files.storage import storages

from utils.images import compress_image_to_webp


def generate_short_uuid():
    return shortuuid.ShortUUID().random(length=10)


@deconstructible
class UploadToPath:
    def __init__(self, base_path: str):
        self.base_path = base_path.rstrip("/")

    def __call__(self, instance, filename: str) -> str:
        extension = Path(filename).suffix.lower()
        return f"{self.base_path}/{instance.public_id}/{uuid4().hex}{extension}"


class ImageOptimizationMixin(models.Model):
    image_size_config = {}

    class Meta:
        abstract = True

    @staticmethod
    def get_image_storage():
        return storages["public_media"]

    def save(self, *args, **kwargs) -> None:
        if self.image_size_config:

            for field_name, max_size in self.image_size_config.items():
                image_field = getattr(self, field_name, None)

                if image_field and not image_field._committed:
                    compressed = compress_image_to_webp(image_field, max_size)

                    if compressed:
                        setattr(self, field_name, compressed)

        return super().save(*args, **kwargs)
