from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from .models import Post, Author
from django.shortcuts import redirect, reverse


class PostCreateView(CreateView):
    model = Post
    template_name = "blog/create_post.html"
    fields = ["title", "content", "audio", "date", "author", "tags"]


class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    fields = ["title", "content", "audio", "date", "author", "tags"]
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"


"""

<a class="active" href=" {% url 'post_list' %} ">Home</a>
        <a href=" {% url 'post_detail'  pk=post.pk %} ">Detail</a>"""
