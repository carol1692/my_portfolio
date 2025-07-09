from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.main , name="index_collab_songs")
] 