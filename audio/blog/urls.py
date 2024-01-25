from django.contrib import admin
from django.urls import path, include
from .views import (
    PostCreateView,
    PostDetailView,
    PostListView,
    PostDeleteView,
)
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

app_name = "blog"

urlpatterns = [
    path("", RedirectView.as_view(url="http://localhost:8000/posts/"), name="home"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("create/", PostCreateView.as_view(), name="post-create"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("delete/<str:pk>/", PostDeleteView.as_view(), name="post-delete"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
