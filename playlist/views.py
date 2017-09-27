from django.views.generic import TemplateView, View
from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from django.http import Http404, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from playlist.models import Playlist, Song, SongHistory
from users.models import User
from playlist.forms import SongForm, PlaylistForm
from playlist.YoutubeApi import Youtube


class AllPlaylistView(LoginRequiredMixin, TemplateView):
    """Displays all playlist and can create playlist
    """
    template_name = 'playlist/playlists.html'

    def get(self, *args, **kwargs):
        """show all playlists
        """
        form = PlaylistForm()
        return render(self.request, self.template_name, {
            'playlists': Playlist.objects.all(),
            'form':form
        })

    def post(self, *args, **kwargs):
        """create playlist
        """
        form = PlaylistForm(self.request.POST, user=self.request.user)
        if form.is_valid():
            form.save()
            return redirect('all_playlist')
        return render(self.request, self.template_name, {
            'playlists': Playlist.objects.all(),
            'form': form
        })


class PlaylistView(LoginRequiredMixin, TemplateView):
    """Display a playlist and can add a song on that playlist
    """
    template_name = 'playlist/playlist.html'

    def get(self, *args, **kwargs):
        """show all songs from playlist
        """
        playlist = get_object_or_404(Playlist, id=kwargs['playlist_id'])
        form = SongForm(user=self.request.user, playlist=playlist)
        songs = Song.objects.filter(playlist=playlist, archive=False)
        song_ids = songs.values_list('link', flat=True)
        return render(self.request, self.template_name, {
            'playlist': playlist,
            'songs': songs,
            'form':form,
            'song_ids': list(song_ids)
        })

    def post(self,*args,**kwargs):
        """add song to playlist
        """
        playlist = get_object_or_404(Playlist, id=kwargs['playlist_id'])
        songs = Song.objects.filter(playlist=playlist, archive=False)
        form = SongForm(
            self.request.POST,
            user=self.request.user,
            playlist=playlist
        )
        if form.is_valid():
            form.save()
            return JsonResponse(
                {
                'title':form.instance.title,
                'link':form.instance.link,
                'edit_url':reverse('song_detail', kwargs={
                    'playlist_id':form.playlist.id,
                    'song_id':form.instance.id
                    }),
                'delete_url':reverse('song_delete', kwargs={
                    'playlist_id':form.playlist.id,
                    'song_id':form.instance.id
                    }),
                'thumb_url':form.instance.thumb_url,
                'duration':form.instance.duration,
                'user':form.instance.user.email
                },
                safe = False
            )

        return JsonResponse(form.errors, status=400)


class SongDetail(LoginRequiredMixin, TemplateView):
    """ Display song details and can edit song from a playlist
    """
    template_name = 'playlist/detail.html'

    def get(self, *args, **kwargs): 
        """show song details
        """
        song = get_object_or_404(
            Song,
            id=kwargs['song_id'],
            user=self.request.user
        )
        form = SongForm(instance=song)
        return render(self.request, self.template_name, {
                'form': form,
                'song': song
        })

    def post(self, *args, **kwargs):
        """update song details
        """
        song = get_object_or_404(
            Song,
            id=kwargs['song_id'],
            user=self.request.user
        )
        form = SongForm(self.request.POST, instance=song)
        if form.is_valid():
            form.save()
            return redirect('playlist', kwargs['playlist_id'])
        return render(self.request, self.template_name, {
            'form': form
        })


class SongDelete(LoginRequiredMixin, View):
    """Delete Song from Playlist
    """

    def get(self, *args, **kwargs):
        song = get_object_or_404(
            Song,
            id=kwargs['song_id'],
            user=self.request.user
        )
        # passes archive True to the overriden save method to represent as delete
        song.save(archive=True)
        return redirect('playlist', kwargs['playlist_id'])


class SearchSongYoutube(Youtube, LoginRequiredMixin, TemplateView):
    """ Search song on youtube from inside the app
    """
    template_name = 'playlist/search.html'

    def post(self, *args, **kwargs):
        searches = self.search_list_by_keyword(
            self.authenticate_yt(),
            part='snippet',
            maxResults=25,
            q=self.request.POST.get('youtube_keyboard'),
            type='video'
        )
        # import pdb;pdb.set_trace()
        return render(self.request, self.template_name, {
            'searches':searches
        })