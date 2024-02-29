from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from forum.models import Post, Playlist, User, Song


@login_required
def index(request: HttpRequest) -> HttpResponse:
    """View function for the home page of the site."""

    num_posts = Post.objects.filter(owner=request.user).count()
    num_playlists = Playlist.objects.filter(owner=request.user).count()
    num_songs = Song.objects.filter(owner=request.user).count()

    context = {
        "num_posts": num_posts,
        "num_playlists": num_playlists,
        "num_songs": num_songs,
    }

    return render(request, "forum/index.html", context=context)


class PostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    ordering = "created_time"
    paginate_by = 5
