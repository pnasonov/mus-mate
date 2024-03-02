from django.urls import path

from forum.views import (
    index,
    PostDetailView,
    PostListView,
    MyPostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path("", index, name="home"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/my/", MyPostListView.as_view(), name="post-my"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/create/", PostCreateView.as_view(), name="post-create"),
    path(
        "posts/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"
    ),
    path(
        "posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"
    ),
]

app_name = "forum"
