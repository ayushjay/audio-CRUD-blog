from django.contrib import admin
from django.urls import path, include
from .views import PostCreateView, PostDetailView, PostListView

app_name = "blog"

urlpatterns = [
    # path("", Home, name="home"),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("create/", PostCreateView.as_view(), name="post-create"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post-detail"),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
