from django.db import models


class Song(models.Model):
    """
    Songs per Playlist
    """
    title = models.CharField(max_length=100)
    link = models.URLField(max_length=400)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def get_url_end(self):
        #javascript for playing the video only needs the end of the link
        crimped_link = ""+self.link
        return crimped_link.split("watch?v=",1)[1]

class Playlist(models.Model):
    """
    Songlist
    """
    title = models.CharField(max_length=128)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.title