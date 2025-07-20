from django.urls import path
from .views import SearchView, ArtistView, AlbumView

urlpatterns = [
    path("", SearchView.as_view() , name="index_je"),
    path("artist_albums/<str:artist_id>", ArtistView.as_view() , name="artist_albums"),
    path("album/<str:album_id>", AlbumView.as_view() , name="album_info"),
]