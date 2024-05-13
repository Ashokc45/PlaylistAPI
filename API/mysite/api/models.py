from django.db import models

# Create your models here.
class Song(models.Model):
    name=models.CharField(max_length=100)
    artist=models.CharField(max_length=100)
    release_year=models.IntegerField()
class Playlist(models.Model):
    name=models.CharField(max_length=100)
    songs=models.ManyToManyField(Song,through='PlaylistSong')
class PlaylistSong(models.Model):
    playlist=models.ForeignKey(Playlist,on_delete=models.CASCADE)
    song=models.ForeignKey(Song,on_delete=models.CASCADE)
    position=models.IntegerField()