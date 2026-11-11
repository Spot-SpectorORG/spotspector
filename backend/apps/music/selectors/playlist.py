from django.core.exceptions import PermissionDenied

from apps.music.models.playlist import Playlist


def get_playlists_by_owner(requesting_user, owner_id):
    queryset = Playlist.objects.all()

    if owner_id is not None:
        queryset = queryset.filter(owner__public_id=owner_id)

        is_owner = (
            requesting_user.is_authenticated and requesting_user.public_id == owner_id
        )

        if not is_owner:
            queryset = queryset.filter(visibility=Playlist.Status.PUBLIC)

    else:
        queryset = queryset.filter(visibility=Playlist.Status.PUBLIC)

    return queryset


def get_playlist_by_permission(user, playlist):
    if playlist.visibility == Playlist.Status.PRIVATE:
        if not user.is_authenticated or (
            playlist.owner != user and user not in playlist.collaborators.all()
        ):
            raise PermissionDenied("This playlist is private.")

    return playlist
