from django.shortcuts import render
from django.views.generic import FormView
from django.conf import settings
from .forms import SearchForm
from .services.spotify import search_artists_and_tracks, search_albums, album_info

class FormBaseView(FormView):
    form_class = SearchForm

    def handle_search(self, form):
        search = form.cleaned_data['search']
        return search_artists_and_tracks(search, 6)

    def get_initial(self):
        return {'search': self.request.GET.get('search')}
    

class SearchView(FormBaseView):
    template_name = "je_assistant/index.html"

    def form_valid(self, form):
        search_data = self.handle_search(form)
        context = self.get_context_data(form=form, list_artists_tracks=search_data)
        return self.render_to_response(context)
      

class ArtistView(FormBaseView):
    template_name = "je_assistant/artists_list_albums.html"

    def form_valid(self, form):
        search_data = self.handle_search(form)
        return render(self.request, "je_assistant/index.html", {'form': form, 'list_artists_tracks':search_data})
 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_artist = self.kwargs.get('artist_id')
        if id_artist:
            context['list_albums'] = search_albums(id_artist)
        return context
    

class AlbumView(FormBaseView):
    template_name = "je_assistant/album_info.html"

    def form_valid(self, form):
        search_data = self.handle_search(form)
        return render(self.request, "je_assistant/index.html", {'form': form, 'list_artists_tracks':search_data})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_album = self.kwargs.get('album_id')
        if id_album:
            context['album_info']= album_info(id_album)
        return context