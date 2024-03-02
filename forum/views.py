from django.contrib.auth.decorators import login_required
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from forum.models import Post, Playlist, User, Song
from forum.forms import CommentaryForm, PostSearchForm, PostForm


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
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(PostListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")

        context["search_form"] = PostSearchForm(initial={"title": title})

        return context

    def get_queryset(self) -> QuerySet:
        queryset = Post.objects.prefetch_related(
            "owner", "commentaries"
        ).order_by("-created_time")
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
        queryset = Post.objects.prefetch_related(
            "owner", "commentaries"
        ).filter(owner=self.request.user.id)

        title = self.request.GET.get("title")

        if title:
            return queryset.filter(title__icontains=title)

        return queryset


class PostDetailView(
    LoginRequiredMixin,
    generic.edit.FormMixin,
    generic.DetailView,
):
    model = Post
    queryset = Post.objects.prefetch_related("commentaries")
    form_class = CommentaryForm

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        return context

    def form_valid(self, form: CommentaryForm) -> HttpResponse:
        form.instance.post = self.get_object()
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
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

    def form_valid(self, form: PostForm):
        form.instance.created_by = self.request.user
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("forum:post-list")


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    success_url = reverse_lazy("forum:post-list")
