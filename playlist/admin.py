from django.contrib import admin

from .models import Playlist, Song, SongHistory


admin.site.register(Playlist)
admin.site.register(Song)
admin.site.register(SongHistory)