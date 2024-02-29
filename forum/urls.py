from django.urls import path

from forum.views import PostListView

urlpatterns = [
    path("", PostListView.as_view(), name="home")
]

app_name = "forum"
