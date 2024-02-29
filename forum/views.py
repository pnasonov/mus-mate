from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from forum.models import Post


class PostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    ordering = "created_time"
    paginate_by = 5
