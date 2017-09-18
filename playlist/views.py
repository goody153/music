from django.views.generic import TemplateView, View
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from playlist.models import Playlist, Song
from users.models import User
from playlist.forms import SongForm, PlaylistForm


class PlaylistsView(TemplateView):
    """ViewPlaylists && Add PLAYLIST
    """
    template_name = 'playlist/playlists.html'
    form = PlaylistForm

    def get(self, *args, **kwargs):
        """show all playlist
        """
        context = {
            'playlists': Playlist.objects.all(),
            'form': self.form,
        }
        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs):
        """create playlist
        """
        form = self.form(self.request.POST)
        if form.is_valid():
            form.save()
            return redirect('playlists')
        context = {
            'playlists': Playlist.objects.all(),
            'form': form,
        }
        return render(self.request, self.template_name, context)


class PlaylistView(TemplateView):
    """ViewPlaylist && Add SONG
    """
    template_name = 'playlist/playlist.html'
    form = SongForm

    def get(self, *args, **kwargs):
        """show all songs from playlist
        """
        playlist = get_object_or_404(Playlist, id=kwargs['playlist_id'])
        songs = Song.objects.filter(playlist=playlist)
        context={
            'playlist': playlist,
            'form': self.form,
            'songs': songs,
        }
        return render(self.request, self.template_name, context)

    def post(self,*args,**kwargs):
        """add song to playlist
        """
        playlist = get_object_or_404(Playlist, id=kwargs['playlist_id'])
        songs = Song.objects.filter(playlist=playlist)
        form = self.form(self.request.POST)
        if form.is_valid():
            form.instance.playlist = playlist
            form.instance.user = self.request.user
            form.save()
            return redirect('playlist', kwargs['playlist_id'])
        context={
            'playlist': playlist,
            'form': form,
            'songs': songs,
        }
        return render(self.request, self.template_name, context)


class SongDetail(View):
    """ View song && edit song from playlist
    """
    template_name = 'playlist/songdetail.html'
    form = SongForm

    def get(self, *args, **kwargs):
        """show song details
        """
        playlist = get_object_or_404(Playlist, id=kwargs['playlist_id'])
        song = get_object_or_404(Song, id=kwargs['song_id'])
        form = self.form(instance=song)
        context = {
            'form': form,
            'playlist': playlist,
        }
        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs):
        """update song details
        """
        song = get_object_or_404(Song, id=kwargs['song_id'])
        if self.request.user == song.user:
            form = self.form(self.request.POST,instance=song)
            form.save()
        return redirect('playlist',kwargs['playlist_id'])


class SongDelete(View):
    """Delete Song from Playlist
    """

    def get(self, *args, **kwargs):
        playlist = get_object_or_404(Playlist, id=kwargs['playlist_id'])
        song = get_object_or_404(Song,id=kwargs['song_id'], playlist=playlist)
        if self.request.user == song.user:
            song.delete()
        return redirect('playlist', kwargs['playlist_id'])