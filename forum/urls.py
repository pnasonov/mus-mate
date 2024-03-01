from django.urls import path

from forum.views import index, PostDetailView, PostListView

urlpatterns = [
    path("", index, name="home"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post-detail"),
]

app_name = "forum"
