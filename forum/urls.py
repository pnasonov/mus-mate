from django.urls import path

from forum.views import PostListView, index

urlpatterns = [
    path("", index, name="home"),
    path("posts/", PostListView.as_view(), name="post_list"),
]

app_name = "forum"
