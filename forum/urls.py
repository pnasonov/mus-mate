from django.urls import path

from forum.views import (
    index,
    PostDetailView,
    PostListView,
    MyPostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    MySongListView,
    SongCreateView,
    SongUpdateView,
    SongDeleteView,
    PlaylistListView,
    MyPlaylistListView,
    PlaylistCreateView,
    PlaylistUpdateView,
    PlaylistDeleteView,
    PlaylistDetailView,
    ProfileView,
    ProfileUpdate,
)

urlpatterns = [
    path("", index, name="home"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/my/", MyPostListView.as_view(), name="post-my"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/create/", PostCreateView.as_view(), name="post-create"),
    path(
        "posts/<int:pk>/update/",
        PostUpdateView.as_view(),
        name="post-update",
    ),
    path(
        "posts/<int:pk>/delete/",
        PostDeleteView.as_view(),
        name="post-delete",
    ),
    path("songs/my/", MySongListView.as_view(), name="song-my"),
    path("songs/create/", SongCreateView.as_view(), name="song-create"),
    path(
        "songs/<int:pk>/update/",
        SongUpdateView.as_view(),
        name="song-update",
    ),
    path(
        "songs/<int:pk>/delete/",
        SongDeleteView.as_view(),
        name="song-delete",
    ),
    path("playlists/", PlaylistListView.as_view(), name="playlist-list"),
    path("playlists/my/", MyPlaylistListView.as_view(), name="playlist-my"),
    path(
        "playlists/<int:pk>/",
        PlaylistDetailView.as_view(),
        name="playlist-detail",
    ),
    path(
        "playlists/create/",
        PlaylistCreateView.as_view(),
        name="playlist-create",
    ),
    path(
        "playlists/<int:pk>/update/",
        PlaylistUpdateView.as_view(),
        name="playlist-update",
    ),
    path(
        "playlists/<int:pk>/delete/",
        PlaylistDeleteView.as_view(),
        name="playlist-delete",
    ),
    path("profile/<str:slug>/", ProfileView.as_view(), name="profile"),
    path(
        "profile/<str:slug>/update/",
        ProfileUpdate.as_view(),
        name="profile-update",
    ),
]

app_name = "forum"
