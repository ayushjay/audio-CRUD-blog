from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    RedirectView,
    DeleteView,
)
from .models import Post, Author
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from .forms import PostForm


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/create_post.html"
    success_url = "posts/"


class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    fields = ["title", "content", "audio", "date", "author", "tags"]
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("post-list")
