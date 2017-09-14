from django import forms

from playlist.models import Song


class SongForm(forms.ModelForm):
    """To Add/Edit Playlist
    """
    class Meta:
        model = Song
        fields = ['title','link']