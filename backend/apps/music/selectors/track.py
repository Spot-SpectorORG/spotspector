from django.shortcuts import get_object_or_404

from rest_framework.exceptions import NotFound

from math import ceil

from apps.music.models.track import Track

from apps.music.services.track import update_track_plays_count


def get_track_stream_url(public_id) -> tuple[str, int] | None:
    track = get_object_or_404(
        Track.objects.only("id", "duration_ms", "audio_file"),
        public_id=public_id,
    )

    if not track.audio_file:
        raise NotFound("Audio file for this track is not available.")

    update_track_plays_count(track)

    track_seconds = ceil((track.duration_ms or 0) / 1000)
    expires_in = max(900, track_seconds + 900)

    stream_url = track.audio_file.storage.url(
        track.audio_file.name,
        expire=expires_in,
    )

    return stream_url, expires_in
