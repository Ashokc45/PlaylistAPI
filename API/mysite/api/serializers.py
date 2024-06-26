from rest_framework import serializers
from .models import Song,Playlist,PlaylistSong

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields='__all__'

class PlaylistSongSerializer(serializers.ModelSerializer):
    class Meta:
        model=PlaylistSong
        fields='__all__'

class PlaylistSerializer(serializers.ModelSerializer):
    songs=SongSerializer(many=True,read_only=True)
    


    class Meta:
        model=Playlist
        fields='__all__'