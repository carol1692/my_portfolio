from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_morse, name="index_morse"),
]