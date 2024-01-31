from django.db import models
from taggit.managers import TaggableManager
from django.urls import reverse


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_id = models.EmailField(max_length=100)

    def __str__(self):
        return self.last_name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=800)
    audio = models.FileField(upload_to="media/songdir")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateTimeField(
        auto_now=True,
    )
    tags = TaggableManager()

    # def get_absolute_url(self):
    #    return reverse("report_user", kwargs={"username": self.reported})

    def __str__(self):
        return self.title
