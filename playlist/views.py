from django.views.generic import TemplateView, View
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from playlist.models import Playlist, Song
from users.models import User
from playlist.forms import SongForm


class PlaylistView(TemplateView):
    """ViewPlaylist && Add song
    """
    template_name = ''
    form = SongForm

    def get(self,*args,**kwargs):
        playlist = get_object_or_404(Playlist, id=kwargs['playlist_id'])
        context={
            'playlist':playlist,
            'form':form,
        }
        return render(self.request, self.template_name, context)

    def post(self,*args,**kwargs):
        playlist = get_object_or_404(Playlist, id=kwargs['playlist_id'])
        form = self.Form(self.request.POST)
        form.instance.playlist = playlist
        form.user.instance = 
        form.save()
        return redirect('playlist',kwargs['playlist_id'])
