from django.urls import path

from forum.views import index, PostDetailView, PostListView, MyPostListView

urlpatterns = [
    path("", index, name="home"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("posts/my", MyPostListView.as_view(), name="post-my"),
]

app_name = "forum"
