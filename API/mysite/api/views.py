from django.shortcuts import render
from .models import Song,Playlist,PlaylistSong
from .serializers import SongSerializer,PlaylistSerializer,PlaylistSongSerializer
from rest_framework import generics

# Create your views here.
class SongListCreateAPIView(generics.ListCreateAPIView):
    queryset=Song.objects.all()
    serializer_class=SongSerializer

class PlaylistListCreateAPIView(generics.ListCreateAPIView):
    queryset=Playlist.objects.all()
    serializer_class=PlaylistSerializer

class PlaylistSongListAPIView(generics.ListAPIView):
    serialize_class=PlaylistSerializer


    def get_queryset(self):
        playlist_id=self.kwargs['playlist_id']
        return PlaylistSong.objects.filter(playlist_id=playlist_id)
