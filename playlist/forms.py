from django import forms
from playlist.models import Playlist,Song 

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['title','description']

class SongListForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title','link']