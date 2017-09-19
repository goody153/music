from django.db import models

from users.models import User


class Playlist(models.Model):
    """Songlist
    """
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.title)


class Song(models.Model):
    """Song
    """
    playlist = models.ForeignKey(Playlist)
    title = models.CharField(max_length=255)
    link = models.URLField()
    user = models.ForeignKey(User)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.title)

    def save(self, *args, **kwargs):
        """ Override the save function to 
            add song history
        """
        if self.id:
            # the user edited the added song
            log = SongHistory.objects.create(user=self.user,
                                             title=self.title,
                                             link=self.link,
                                             action='Updated')
            log.save()
        else:
            # the user added song
            log = SongHistory.objects.create(user=self.user,
                                             title=self.title,
                                             link=self.link,
                                             action='Added')
            log.save()
        super(Song, self).save(*args, **kwargs) # Calls the real save method


class SongHistory(models.Model):
    """ Tracks action done on Song model 
    """
    user = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    link = models.URLField()
    action = models.CharField(max_length=16)
    date = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return "{}-{}".format(self.title, self.action)