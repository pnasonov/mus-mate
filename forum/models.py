from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=40)
    artist = models.CharField(max_length=40)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )


class Playlist(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=255, blank=True)
    songs = models.ManyToManyField(Song, related_name="playlists")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )


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
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )


class User(AbstractUser):
    about_me = models.CharField(max_length=255, blank=True)
