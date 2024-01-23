from django.db import models
from taggit.managers import TaggableManager


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_id = models.EmailField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=800)
    audio = models.FileField(upload_to="static/audio/")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateTimeField(
        auto_now=True,
    )
    tags = TaggableManager()
