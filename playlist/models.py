from django.db import models

from users.models import User


class Playlist(models.Model):
    """Playlist
    """
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.title)


class Song(models.Model):
    """Song
    """
    playlist = models.ForeignKey(Playlist)
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=11)
    user = models.ForeignKey(User)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    archive = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.title)

    def save(self, *args, **kwargs):
        """ Override the save function to 
            add song history
        """
        if kwargs.pop('archive', None): # if archive isn't None then the song is deleted
            self.archive = True
        log = SongHistory.objects.create(
            user=self.user,
            title=self.title,
            link=self.link
        )
        if self.id: #  if id is empty the user added a song
            if self.archive == True: #  if true the user deleted the song
                log.action = SongHistory.DELETED
            else:
                log.action = SongHistory.UPDATED
        else:
            log.action = SongHistory.ADDED

        log.save()
        return super(Song, self).save(*args, **kwargs) # Calls the real save method


class SongHistory(models.Model):
    """ Tracks action done on Song model 
    """
    ADDED = 'Added'
    UPDATED = 'Updated'
    DELETED = 'Deleted'
    
    actions = (
        (ADDED, 'Added'),
        (UPDATED, 'Updated'),
        (DELETED, 'Deleted'),
    )
    user = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=11)
    action = models.CharField(max_length=16, choices=actions)
    date = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return "{}-{}".format(self.title, self.action)

