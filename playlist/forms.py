from django import forms

from playlist.models import Song, Playlist


class PlaylistForm(forms.ModelForm):
    """Form for creating playlist
    """

    class Meta:
        model = Playlist
        fields = ['title', 'description']


class SongForm(forms.ModelForm):
    """Form for adding song on a playlist
    """

    class Meta:
        model = Song
        fields = ['title', 'link']

    def __init__(self, *args, **kwargs):
        """ User and playlist are used for creation of song
        """
        self.user = kwargs.pop('user', None)
        self.playlist = kwargs.pop('playlist', None)

        return super(SongForm, self).__init__(*args, **kwargs)

    def save(self):
        """ Song creation needs user and playlist 
        """
        song = Song.objects.create(
            title=self.cleaned_data['title'],
            link=self.cleaned_data['link'],
            user=self.user,
            playlist=self.playlist
        )
        return song

    def clean_link(self):
        """ check youtube id length
        """
        if len(self.cleaned_data['link']) < 11:
            raise forms.ValidationError("Youtube id length is invalid.")
        return self.cleaned_data['link']


class UpdateSongForm(forms.ModelForm):
    """ Form for editing a song from a playlist
    """

    class Meta:
        model = Song
        fields = ['title', 'link']