from django import forms
from .models import Post, Author


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "audio", "author", "tags"]
