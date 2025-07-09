from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_blog, name="index_blog"),
    path("posts", views.posts_blog, name="list_posts"),
    path("posts/<int:id>", views.post, name="post"),
    path("upload", views.CreateProfileView.as_view(), name="upload_test")
]
