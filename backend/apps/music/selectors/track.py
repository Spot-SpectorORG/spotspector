from django.shortcuts import get_object_or_404

from math import ceil

from apps.music.models.track import Track

from apps.music.services.track import update_track_plays_count


def get_track_stream_url(public_id):
    track = get_object_or_404(Track, public_id=public_id)

    update_track_plays_count(track)

    track_seconds = ceil((track.duration_ms or 0) / 1000)
    expires_in = max(900, track_seconds + 900)

    stream_url = track.audio_file.storage.url(
        track.audio_file.name,
        expire=expires_in,
    )

    return stream_url, expires_in
