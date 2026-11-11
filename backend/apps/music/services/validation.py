import os

from mutagen import File as MutagenFile

from rest_framework.serializers import ValidationError


def validate_audio_file(file):
    max_size_mb = 30

    if file.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"File must not exceed {max_size_mb} MB.")

    ext = os.path.splitext(file.name)[1].lower()
    allowed_extensions = [".mp3", ".wav", ".ogg", ".m4a", ".flac"]
    if ext not in allowed_extensions:
        raise ValidationError(
            f"File format is not valid. Allowed: {', '.join(allowed_extensions)}"
        )

    try:
        audio = MutagenFile(file)

        if (
            audio is None
            or not hasattr(audio, "info")
            or not getattr(audio.info, "length", None)
        ):
            raise ValidationError("File contains errors or not audio")

        if audio.info.length < 10.0:
            raise ValidationError("File duration must be longer than 10 seconds")

        file.extracted_duration_ms = int(audio.info.length * 1000)

    except ValidationError:
        raise

    except Exception:
        raise ValidationError("Error reading metadata from file.")

    finally:
        file.seek(0)

    return file
