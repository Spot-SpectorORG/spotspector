from django.contrib import admin

from apps.users.models.user import CustomUser

admin.site.register(CustomUser)
