from django.urls import path

from apps.music.api.views.artist import ArtistDetailView, ArtistListView
from apps.music.api.views.genre import GenreListView
from apps.music.api.views.album import AlbumDetailView, AlbumListView
from apps.music.api.views.track import TrackListView, TrackDetailView, TrackStreamView
from apps.music.api.views.playlist import PlaylistDetailView, PlaylistListView

app_name = "music"

urlpatterns = [
    # Artists
    path("artists/", ArtistListView.as_view(), name="artists-list"),
    path(
        "artists/<str:public_id>/",
        ArtistDetailView.as_view(),
        name="artist-detail",
    ),
    # Albums
    path("albums/", AlbumListView.as_view(), name="albums-list"),
    path("albums/<str:public_id>/", AlbumDetailView.as_view(), name="album-detail"),
    # Tracks
    path("tracks/", TrackListView.as_view(), name="tracks-list"),
    path("tracks/<str:public_id>/", TrackDetailView.as_view(), name="track-detail"),
    path(
        "tracks/<str:public_id>/stream/", TrackStreamView.as_view(), name="track-stream"
    ),
    # Genres
    path("genres/", GenreListView.as_view(), name="genres-list"),
    # Playlists
    path("playlists/", PlaylistListView.as_view(), name="playlists-list"),
    path(
        "playlists/<str:public_id>/",
        PlaylistDetailView.as_view(),
        name="playlists-detail",
    ),
]
