from django.conf import settings

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id = settings.SPOTIFY_CLIENT_ID,
    client_secret = settings.SPOTIFY_CLIENT_SECRET
))

def album_info(id_album):
    result_album = sp.album(id_album)
    
    dados={
        'album_image': result_album['images'][0]['url'] if result_album['images'] else None ,
        'album_name':result_album['name'],
        'artist_name': result_album['artists'][0]['name'],
        'album_upc':result_album['external_ids']['upc']
    }
    return dados

def search_albums(id_artist):
    results_artist_albums = sp.artist_albums(id_artist)
    list_artist_albums = results_artist_albums['items']

    dados = [
            {
            'album_image':album['images'][0]['url'] if album['images'] else None ,
            'album_name':album['name'],
            'artist_name': album['artists'][0]['name'],
            'album_id':album['id']
            } for album in list_artist_albums
            ]
    
    return dados

def search_artists_and_tracks(query, search_limit):
    results_artists = sp.search(q=query, type='artist,track', limit=search_limit)
    list_artist = results_artists['artists']['items']
    list_tracks = results_artists['tracks']['items']
   
    dados = { 'artists':[{
                'artist_image':artist['images'][0]['url'] if artist['images'] else None ,
                'artist_name':artist['name'],
                'artist_id':artist['id']
            } for artist in list_artist],
            'tracks':[{
                'track_image':track['album']['images'][0]['url'] if track['album']['images'] else None ,
                'track_name':track['name'],
                'track_id':track['id'],
                'track_artist':track['artists'][0]['name'],
                'track_artist_id':track['artists'][0]['id'],
                'track_album':track['album']['name'],
                'track_album_id':track['album']['id'],
            } for track in list_tracks]
    }
    return dados