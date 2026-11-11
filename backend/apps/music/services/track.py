from apps.music.models.track import Track

from django.db.models import F


def update_track_plays_count(track: Track):
    track.plays_count = F("plays_count") + 1
    track.save(update_fields=["plays_count"])
