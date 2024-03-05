from autoslug import AutoSlugField
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=40)
    artist = models.CharField(max_length=40)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="songs",
    )

    def __str__(self) -> str:
        return f"{self.title} - {self.artist}"


class Playlist(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=255, blank=True)
    songs = models.ManyToManyField(Song, related_name="playlists")
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="playlists",
    )


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
    )

    def __str__(self) -> str:
        return f"{self.title} (by {self.owner})"


class Commentary(models.Model):
    class Meta:
        verbose_name = "commentary"
        verbose_name_plural = "commentaries"

    content = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="commentaries"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="commentaries",
    )


class User(AbstractUser):
    about_me = models.CharField(max_length=255, blank=True)
    instagram = models.CharField(
        max_length=255, blank=True, null=True, default=None
    )
    slug = AutoSlugField(
        populate_from="username", default=None, null=True, db_index=False
    )
