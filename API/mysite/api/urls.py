# urls.py
from django.urls import path
from .views import SongListCreateAPIView,PlaylistListCreateAPIView,PlaylistSongListAPIView

urlpatterns = [
    path('Song/', SongListCreateAPIView.as_view(), name='song-list-create'),
    path('Playlist/', PlaylistListCreateAPIView.as_view(), name='playlist-list-create'),
    path('PlaylistSong/<int:playlist_id>/Song/', PlaylistSongListAPIView.as_view(), name='playlist-song-list'),
]
