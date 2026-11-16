from django.contrib import admin

from apps.users.models.user import User

from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email"]
    search_fields = ["username", "email"]

    list_filter = ["is_superuser"]

    autocomplete_fields = ["liked_tracks", "followed_artists", "friends"]

    fieldsets = [
        (
            None,
            {
                "fields": [
                    "avatar",
                    ("first_name", "last_name"),
                    "username",
                    "email",
                    "liked_tracks",
                    "followed_artists",
                    "friends",
                ],
            },
        ),
    ]
