from datetime import date

from django import forms
from django.contrib import admin

from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html, format_html_join

from django.urls import reverse

from .models import *


class DecadeReleaseDateFilter(admin.SimpleListFilter):
    title = _("decade release")

    parameter_name = "decade"

    def lookups(self, request, model_admin):
        return [
            ("70s", _("in the seventies")),
            ("80s", _("in the eighties")),
            ("90s", _("in the nineties")),
            ("00s", _("in the two-thousands")),
        ]

    def queryset(self, request, queryset):

        if self.value() == "70s":
            return queryset.filter(
                release_date__gte=date(1970, 1, 1),
                release_date__lte=date(1979, 12, 31),
            )
        if self.value() == "80s":
            return queryset.filter(
                release_date__gte=date(1980, 1, 1),
                release_date__lte=date(1989, 12, 31),
            )
        if self.value() == "90s":
            return queryset.filter(
                release_date__gte=date(1990, 1, 1),
                release_date__lte=date(1999, 12, 31),
            )
        if self.value() == "00s":
            return queryset.filter(
                release_date__gte=date(2000, 1, 1),
                release_date__lte=date(2009, 12, 31),
            )


class HTML5DateAdminMixin:
    formfield_overrides = {
        models.DateField: {
            "widget": forms.DateInput(
                attrs={"type": "date"},
                format="%Y-%m-%d",
            )
        }
    }


@admin.register(Track)
class TrackAdmin(HTML5DateAdminMixin, admin.ModelAdmin):
    list_display = ["title", "album_link", "release_date"]
    readonly_fields = ["duration_ms", "plays_count", "album_link"]

    search_fields = ["release_date", "title", "album__title"]

    autocomplete_fields = ["artists", "album"]

    list_filter = [
        DecadeReleaseDateFilter,
        "genres",
    ]

    date_hierarchy = "release_date"

    fieldsets = [
        (
            None,
            {
                "fields": [
                    "title",
                    (
                        "artists",
                        "album",
                    ),
                    "genres",
                    "audio_file",
                    "track_position",
                    "release_date",
                ],
            },
        ),
    ]

    @admin.display(description="Album", ordering="album__title")
    def album_link(self, obj):
        if not obj.album:
            return "-"

        app_label = obj.album._meta.app_label
        model_name = obj.album._meta.model_name
        url = reverse(f"admin:{app_label}_{model_name}_change", args=[obj.album.pk])

        return format_html('<a href="{}">{}</a>', url, obj.album.title)


@admin.register(Album)
class AlbumAdmin(HTML5DateAdminMixin, admin.ModelAdmin):
    list_display = ["title", "display_artists", "release_date"]
    list_filter = [DecadeReleaseDateFilter]
    date_hierarchy = "release_date"

    autocomplete_fields = ["artists"]

    search_fields = ["title", "artists__name"]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("artists")

    @admin.display(description="Artists")
    def display_artists(self, obj):
        artists = obj.artists.all()
        if not artists:
            return "-"

        app_label = artists[0]._meta.app_label
        model_name = artists[0]._meta.model_name
        url_name = f"admin:{app_label}_{model_name}_change"

        return format_html_join(
            ", ",
            '<a href="{}">{}</a>',
            ((reverse(url_name, args=[artist.pk]), artist.name) for artist in artists),
        )


@admin.register(Artist)
class ArtistAdmin(HTML5DateAdminMixin, admin.ModelAdmin):
    list_display = ["name", "followers", "foundation_date"]
    search_fields = ["name", "foundation_date"]

    autocomplete_fields = ["genres"]

    fieldsets = [
        (
            None,
            {
                "fields": ["avatar", "name", "genres", "foundation_date"],
            },
        ),
    ]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]

    fieldsets = [
        (
            None,
            {
                "fields": ["name", "description"],
            },
        ),
    ]


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ["title", "owner", "saves_count", "visibility"]
    search_fields = [
        "title",
        "public_id",
        "owner__username",
        "collaborators__username",
    ]

    list_filter = ["visibility"]

    autocomplete_fields = ["owner", "tracks", "genres", "collaborators"]

    fieldsets = [
        (
            None,
            {
                "fields": [
                    "title",
                    "description",
                    "owner",
                    "collaborators",
                    "genres",
                    "tracks",
                    "visibility",
                ],
            },
        ),
    ]

    readonly_fields = ["saves_count"]
