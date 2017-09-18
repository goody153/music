from django import forms

from playlist.models import Song, Playlist


class PlaylistForm(forms.ModelForm):
    """To Add/Edit Playlist
    """

    class Meta:
        model = Playlist
        fields = ['title', 'description']


class SongForm(forms.ModelForm):
    """To Add/Edit Playlist
    """

    class Meta:
        model = Song
        fields = ['title', 'link']