import shortuuid

from pathlib import Path
from uuid import uuid4


def generate_short_uuid():
    return shortuuid.ShortUUID().random(length=10)


def track_audio_upload_to(instance, filename):
    extension = Path(filename).suffix.lower()

    return f"tracks/{instance.public_id}/" f"{uuid4().hex}{extension}"
