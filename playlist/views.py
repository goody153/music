from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View

from playlist.models import Song, Playlist
from playlist.forms import PlaylistForm, SongListForm


class PlaylistView(TemplateView):
    """
    Display Index
    """
    template_name = "playlist/playlists.html"

    def get(self,*args,**kwargs):
        #Display the Playlists
        form= PlaylistForm()
        pl = Playlist.objects.all()
        context = {'form':form,
                    'pl':pl}
        return render(self.request,self.template_name,context)

    def post(self,*args,**kwargs):
        #create new playlist
        form = PlaylistForm(self.request.POST)
        form.save()
        return redirect('playlists')


class PlaylistDetail(TemplateView):
    """
    View Playlist Detail
    """
    template_name = "playlist/playlist_detail.html"

    def get(self,*args,**kwargs):
    #View Playlist Details for Edit
        playlist = Playlist.objects.get(id= kwargs['playlist_id'])
        form = PlaylistForm()
        context = {'form':form,'playlist':playlist}
        return render(self.request,self.template_name,context)

    def post(self,*args,**kwargs):
    # to edit playlist details
        playlist = Playlist.objects.get(id= kwargs['playlist_id'])
        form = PlaylistForm(self.request.POST,instance = playlist)
        form.save()
        return redirect('playlists')


class PlaylistDelete(View):

        def post(self,*args,**kwargs):
        # to delete playlist details

        #insert user restrictions here later
            Playlist.objects.get(id= kwargs['playlist_id']).delete()
            return redirect('playlists')


class PlaylistSongs(TemplateView):
    """
    View songs from a Playlist
    """
    template_name = "playlist/playlist_songs.html"
    def get(self,*args,**kwargs):
        # show songs in the playlist
        playlist = Playlist.objects.get(id= kwargs['playlist_id'])
        form = SongListForm()
        songlist = playlist.songs.all().order_by('-date_created')
        context = {'form':form,'playlist':playlist,'songlist':songlist}
        return render(self.request,self.template_name,context)

    def post(self,*args,**kwargs):
        #add song to playlist
        playlist = Playlist.objects.get(id= kwargs['playlist_id'])

        #save song
        form = SongListForm(self.request.POST)
        form.save()

        #save song to playlist
        title = form.__getitem__('title').value() # get title from form that was used
        link = form.__getitem__('link').value() # get link from form that was used
        song = Song.objects.get(title= title,link= link)
        playlist.songs.add(song)

        return redirect('playlist_songs',playlist_id=kwargs['playlist_id'])


class SongDetail(TemplateView):
    """
    View Song Detail from a specific Playlist
    """
    def get(self,*args,**kwargs):
        #display song detail
        return redirect('playlists')

    def post(self,*args,**kwargs):
        # edit song detail
        return redirect('playlists')

