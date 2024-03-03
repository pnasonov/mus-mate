from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from forum.models import Post, Playlist, User, Song
from forum.forms import (
    CommentaryForm,
    PostSearchForm,
    PostForm,
    SongSearchForm,
    SongForm,
    PlaylistSearchForm,
)


def index(request: HttpRequest) -> HttpResponse:
    """View function for the home page of the site."""
    if request.user.is_authenticated:
        num_posts = Post.objects.filter(owner=request.user).count()
        num_playlists = Playlist.objects.filter(owner=request.user).count()
        num_songs = Song.objects.filter(owner=request.user).count()

        context = {
            "num_posts": num_posts,
            "num_playlists": num_playlists,
            "num_songs": num_songs,
        }

        return render(request, "forum/index.html", context=context)

    num_posts = Post.objects.count()
    num_playlists = Playlist.objects.count()
    num_songs = Song.objects.count()

    context = {
        "num_posts": num_posts,
        "num_playlists": num_playlists,
        "num_songs": num_songs,
    }

    return render(request, "forum/index.html", context=context)


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(PostListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")

        context["search_form"] = PostSearchForm(initial={"title": title})

        return context

    def get_queryset(self) -> QuerySet:
        queryset = (
            Post.objects.select_related("owner")
            .prefetch_related("commentaries")
            .order_by("-created_time")
        )
        title = self.request.GET.get("title")

        if title:
            return queryset.filter(title__icontains=title)

        return queryset


class MyPostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    ordering = "-created_time"
    paginate_by = 5
    template_name = "forum/post_list_my.html"

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(MyPostListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")

        context["search_form"] = PostSearchForm(initial={"title": title})

        return context

    def get_queryset(self) -> QuerySet:
        queryset = (
            Post.objects.filter(owner=self.request.user.id)
            .select_related("owner")
            .prefetch_related("commentaries")
        )

        title = self.request.GET.get("title")

        if title:
            return queryset.filter(title__icontains=title)

        return queryset


class PostDetailView(
    generic.edit.FormMixin,
    generic.DetailView,
):
    model = Post
    queryset = Post.objects.select_related("owner").prefetch_related(
        "commentaries"
    )
    form_class = CommentaryForm

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        return context

    def form_valid(self, form: CommentaryForm) -> HttpResponseRedirect:
        form.instance.post = self.get_object()
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def post(
        self, request: HttpRequest, *args, **kwargs
    ) -> HttpResponseRedirect:
        form = self.get_form()

        if form.is_valid() and request.user.is_authenticated:
            return self.form_valid(form)
        return self.form_invalid(form)

    def get_success_url(self) -> str:
        return self.request.path


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("forum:post-list")

    def form_valid(self, form: PostForm) -> HttpResponseRedirect:
        form.instance.created_by = self.request.user
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("forum:post-list")

    def form_valid(self, form: PostForm) -> HttpResponseRedirect:
        form.instance.created_by = self.request.user
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    success_url = reverse_lazy("forum:post-list")


class MySongListView(LoginRequiredMixin, generic.ListView):
    model = Song
    paginate_by = 15
    template_name = "forum/song_list_my.html"

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(MySongListView, self).get_context_data(**kwargs)
        artist = self.request.GET.get("artist", "")

        context["search_form"] = SongSearchForm(initial={"artist": artist})

        return context

    def get_queryset(self) -> QuerySet:
        queryset = Song.objects.filter(owner=self.request.user).order_by(
            "title"
        )
        artist = self.request.GET.get("artist")

        if artist:
            return queryset.filter(artist__icontains=artist)

        return queryset


class SongCreateView(LoginRequiredMixin, generic.CreateView):
    model = Song
    form_class = SongForm
    success_url = reverse_lazy("forum:song-my")

    def form_valid(self, form: SongForm) -> HttpResponseRedirect:
        form.instance.created_by = self.request.user
        form.instance.owner = self.request.user
        return super().form_valid(form)


class SongUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Song
    form_class = SongForm
    success_url = reverse_lazy("forum:song-my")

    def form_valid(self, form: SongForm) -> HttpResponseRedirect:
        form.instance.created_by = self.request.user
        form.instance.owner = self.request.user
        return super().form_valid(form)


class SongDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Song
    success_url = reverse_lazy("forum:song-my")


class PlaylistListView(generic.ListView):
    model = Playlist
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(PlaylistListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")

        context["search_form"] = PlaylistSearchForm(initial={"name": name})

        return context

    def get_queryset(self) -> QuerySet:
        queryset = (
            Playlist.objects.select_related("owner")
            .prefetch_related("songs")
            .order_by("-created_time")
        )
        name = self.request.GET.get("name")

        if name:
            return queryset.filter(name__icontains=name)

        return queryset


class MyPlaylistListView(LoginRequiredMixin, generic.ListView):
    model = Playlist
    paginate_by = 5
    template_name = "forum/playlist_list_my.html"

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(MyPlaylistListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")

        context["search_form"] = PlaylistSearchForm(initial={"name": name})

        return context

    def get_queryset(self) -> QuerySet:
        queryset = (
            Playlist.objects.filter(owner=self.request.user)
            .select_related("owner")
            .prefetch_related("songs")
            .order_by("-created_time")
        )
        name = self.request.GET.get("name")

        if name:
            return queryset.filter(name__icontains=name)

        return queryset


class PlaylistDetailView(generic.DetailView):
    model = Playlist
    queryset = Playlist.objects.select_related("owner").prefetch_related(
        "songs"
    )


class PlaylistCreateView(LoginRequiredMixin, generic.CreateView):
    pass


class PlaylistUpdateView(LoginRequiredMixin, generic.UpdateView):
    pass


class PlaylistDeleteView(LoginRequiredMixin, generic.DeleteView):
    pass
