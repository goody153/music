from django.views.generic import TemplateView, View
from django.shortcuts import render, redirect

from playlist.models import Playlist, Song
from playlist.forms import PlaylistForm, SongForm


class PlaylistsView(TemplateView):
    """List Playlists && Create Playlist
    """

    template_name = "playlist/playlists.html"
    form = PlaylistForm

    def get(self,*args,**kwargs):
        playlists = Playlist.objects.all().order_by('-date_created')
        context = {'playlists':playlists,
                   'form':self.form}
        return render(self.request,self.template_name,context)

    def post(self,*args,**kwargs):
        form = self.form(self.request.POST)
        form.save()
        return redirect('playlists')