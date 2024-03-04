from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from forum.models import User, Song, Playlist, Post, Commentary

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("about_me", "instagram")}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {
                "fields": (
                    "about_me",
                    "instagram",
                )
            },
        ),
    )


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ("title", "artist", "owner")


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ("name", "owner")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("content", "created_time", "user", "post")
